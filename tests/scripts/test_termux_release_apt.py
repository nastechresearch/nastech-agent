"""The Termux apt feed is published from a GitHub release, flat and signed.

Two failures shape this file.  On 2026-10-28 the R2 staging produced
`404 ... nastech-agent_0.21.5~canary..._aarch64.deb`: an index naming a file
that was not there.  On 2026-11-03 the same tree, handed to the tag archive
instead, produced `412 PreconditionFailed` on
`releases/tag/<tag>/apt/dists/nastech-canary/InRelease`: a signed index embeds
its own generation time, so it can never live in a store that promises
"same key, same bytes".  Publishing the feed as the assets of one fixed-tag
release is what makes both impossible rather than unlikely.
"""

import gzip
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

import pytest
from tests.termux_fixtures import build_deb

from scripts.termux import release_apt, stage_apt_repo

GPG_PRESENT = shutil.which("gpg") is not None


class Result:
    def __init__(self, returncode=0, stdout="", stderr=""):
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr


def _deb_name(version: str) -> str:
    return f"nastech-agent_{version}_aarch64.deb"


def _repo(tmp_path: Path, version: str = "0.22.0") -> Path:
    """A feed directory in the shape release_apt.flatten() produces."""
    repo = tmp_path / "repo"
    repo.mkdir()
    (repo / _deb_name(version)).write_bytes(b"new")
    for name in release_apt.INDEX_FILES:
        (repo / name).write_text(f"{name}\n", encoding="utf-8")
    (repo / "Packages").write_text(
        f"Package: nastech-agent\nVersion: {version}\n"
        f"Filename: {_deb_name(version)}\n",
        encoding="utf-8",
    )
    return repo


def _gh_result(calls, assets=()):
    """A `gh` double that stores every uploaded asset under the name given."""
    def run(argv, **kwargs):
        calls.append(argv)
        if argv[:3] == ["gh", "release", "view"]:
            uploaded = [Path(c[4]).name for c in calls if c[:3] == ["gh", "release", "upload"]]
            stored = {"assets": [{"name": name} for name in [*assets, *uploaded]]}
            return Result(stdout=json.dumps(stored))
        return Result()

    return run


def _signing_debs(pool: Path, versions) -> None:
    pool.mkdir(parents=True, exist_ok=True)
    for version in versions:
        build_deb(pool / _deb_name(version),
                  {"Package": "nastech-agent", "Version": version,
                   "Architecture": "aarch64",
                   "Maintainer": "Test <test@example.invalid>",
                   "Description": "test package"},
                  compression="xz")


def test_staged_files_separates_packages_from_the_index(tmp_path):
    packages, index = release_apt.staged_files(_repo(tmp_path))
    assert [p.name for p in packages] == [_deb_name("0.22.0")]
    # The order is the contract: InRelease is apt's first read, so it flips last.
    assert [p.name for p in index] == list(release_apt.INDEX_FILES)
    assert index[-1].name == "InRelease"

    empty = tmp_path / "empty"
    empty.mkdir()
    with pytest.raises(release_apt.AptReleaseError, match="no .deb"):
        release_apt.staged_files(empty)


def test_publishing_the_staged_debian_layout_is_refused(tmp_path):
    """`pool/` and `dists/` cannot be release assets, so they cannot be published.

    A release asset name is one path component: GitHub stores `pool/n/x.deb` as
    `pool.n.x.deb`, so an index that still advertises the pool path names a file
    the tag does not hold -- the 404 this pipeline exists to end.
    """
    repo = _repo(tmp_path)
    (repo / "pool" / "n").mkdir(parents=True)
    (repo / "pool" / "n" / _deb_name("0.22.0")).write_bytes(b"new")
    (repo / _deb_name("0.22.0")).unlink()
    (repo / "Packages").write_text(
        f"Filename: pool/n/{_deb_name('0.22.0')}\n", encoding="utf-8")

    calls = []
    with pytest.raises(release_apt.AptReleaseError, match="Debian layout"):
        release_apt.publish(repo, "o/r", tag="termux-repo", run=_gh_result(calls))
    assert not [c for c in calls if c[:3] == ["gh", "release", "upload"]]


def test_an_unsigned_feed_is_never_published(tmp_path):
    """A missing signature is a stop, not a warning: the alternative to a
    signed repository is `[trusted=yes]`, which discards the verification."""
    repo = _repo(tmp_path)
    (repo / "InRelease").unlink()
    with pytest.raises(release_apt.AptReleaseError, match="missing InRelease"):
        release_apt.staged_files(repo)


def test_asset_name_drops_the_tilde_github_cannot_hold():
    """`~` is Debian's pre-release marker; GitHub stores it as `.`."""
    canary = _deb_name("0.21.5~canary.20261101T000000Z-1")
    assert release_apt.asset_name(canary) == _deb_name("0.21.5-canary.20261101T000000Z-1")
    # dpkg ranking lives in `Version:`, which keeps the `~` untouched.
    stable = _deb_name("0.21.5-1")
    assert release_apt.asset_name(stable) == stable

    with pytest.raises(release_apt.AptReleaseError, match="GitHub would rewrite"):
        release_apt.asset_name(_deb_name("1:0.21.5-1"))  # a dpkg epoch ':'


def test_each_channel_owns_exactly_one_asset_tag():
    """A canary run writing the stable tag would replace what phones install."""
    assert release_apt.tag_for_channel("stable") == "termux-repo"
    assert release_apt.tag_for_channel("canary") == "termux-repo-canary"
    assert release_apt.tag_for_channel("stable") != release_apt.tag_for_channel("canary")
    with pytest.raises(release_apt.AptReleaseError, match="no asset tag"):
        release_apt.tag_for_channel("nightly")

    with pytest.raises(SystemExit):
        release_apt.main(["publish", "--repo-dir", "/nonexistent",
                          "--repository", "o/r", "--channel", "nightly"])


def test_stale_packages_keeps_the_newest_and_the_fresh_upload():
    existing = [
        "nastech-agent_0.21.9_aarch64.deb",
        "nastech-agent_0.21.10_aarch64.deb",   # dpkg order: 0.21.10 > 0.21.9
        "nastech-agent_0.22.0_aarch64.deb",
        "Packages", "Packages.gz", "Release", "InRelease",
    ]
    deleted = release_apt.stale_packages(existing, [_deb_name("0.22.1")], keep=2)
    # keep the fresh upload plus the newest published version (0.22.0 by dpkg
    # order, not 0.21.9), so both older builds go
    assert sorted(deleted) == [
        "nastech-agent_0.21.10_aarch64.deb",
        "nastech-agent_0.21.9_aarch64.deb",
    ]
    # index assets are never deleted by the package sweep
    assert not any(name in ("Packages", "Release") for name in deleted)


def test_retention_never_dangles_a_package_a_previous_index_can_name():
    """Pruning may not outrun the index a client is still reading.

    A replaced asset keeps serving its previous bytes for a while (measured on
    this repository: a plain GET of a clobbered URL returned the OLD payload
    while the API already held the new one), so a phone can be installing from
    the publish-before-last.  Deleting a package that index names is exactly the
    404 that killed the R2 feed.
    """
    generations = [_deb_name(v) for v in
                   ("0.22.1", "0.22.2", "0.22.3", "0.22.4", "0.22.5")]
    live: list[str] = []
    uploaded: list[list[str]] = []
    for fresh in generations:
        deleted = release_apt.stale_packages(live, [fresh])
        # The indexes still reachable are this publish's and the one before it.
        still_named = {n for publish in uploaded[-2:] for n in publish}
        assert not (still_named & set(deleted)), f"{sorted(still_named & set(deleted))} pruned"
        survivors = (set(live) | {fresh}) - set(deleted)
        live = sorted(survivors)
        uploaded.append([fresh])


def test_publish_uploads_packages_before_the_index_and_prunes_after(tmp_path):
    repo = _repo(tmp_path, version="0.22.1")
    calls = []
    published = [
        "nastech-agent_0.21.7_aarch64.deb",
        "nastech-agent_0.21.8_aarch64.deb",
        "nastech-agent_0.21.9_aarch64.deb",
        "nastech-agent_0.22.0_aarch64.deb",
    ]
    deb = _deb_name("0.22.1")

    def run(argv, **kwargs):
        calls.append(argv)
        if argv[:3] == ["gh", "release", "view"]:
            # The read-back after the package upload sees what GitHub holds.
            uploaded = [c for c in calls if c[:3] == ["gh", "release", "upload"]]
            names = published + ([deb] if uploaded else [])
            return Result(stdout=json.dumps({"assets": [{"name": n} for n in names]}))
        return Result()

    report = release_apt.publish(repo, "o/r", tag="termux-repo-canary", run=run)
    uploads = [c for c in calls if c[:3] == ["gh", "release", "upload"]]
    deletes = [c for c in calls if c[:3] == ["gh", "release", "delete-asset"]]

    order = [Path(c[4]).name for c in uploads]
    assert order == [deb, *release_apt.INDEX_FILES]
    assert report["uploaded_index"][-1] == "InRelease"
    # every gh call writes this channel's own tag, and no other
    assert all(c[3] == "termux-repo-canary" for c in calls if c[:2] == ["gh", "release"])
    # the stale packages are removed through the CLI, not only dropped from the index
    assert [c[4] for c in deletes] == [
        "nastech-agent_0.21.7_aarch64.deb",
        "nastech-agent_0.21.8_aarch64.deb",
    ]
    assert report["deleted_packages"] == [
        "nastech-agent_0.21.7_aarch64.deb",
        "nastech-agent_0.21.8_aarch64.deb",
    ]


def test_publish_stops_when_github_stores_a_name_the_index_cannot_use(tmp_path):
    """GitHub rewrites an asset name it cannot hold, without telling anyone.

    The index is only uploaded once every package it advertises is provably
    fetchable under that advertised name, so a rewritten name stops the publish
    instead of dangling it.
    """
    repo = _repo(tmp_path)
    deb = _deb_name("0.22.0")
    stored = "nastech-agent_0.22.0.aarch64.deb"  # what a rewritten '_' comes back as
    calls = []
    views = []

    def run(argv, **kwargs):
        calls.append(argv)
        if argv[:3] == ["gh", "release", "view"]:
            views.append(argv)
            if len(views) > 1:
                return Result(stdout=json.dumps({"assets": [{"name": stored}]}))
            return Result(stdout=json.dumps({"assets": []}))
        return Result()

    with pytest.raises(release_apt.AptReleaseError, match="under a different name"):
        release_apt.publish(repo, "o/r", tag="termux-repo", run=run)
    assert [c[4] for c in calls if c[:3] == ["gh", "release", "upload"]] == [str(repo / deb)]


def test_the_public_key_ships_with_the_repository(tmp_path):
    """A signed repo whose public key is not published cannot be verified.

    The key is served beside the index, so installing the repository is one
    curl: apt then has something to check `InRelease` against.
    """
    repo = _repo(tmp_path)
    _packages, index = release_apt.staged_files(repo)
    names = [p.name for p in index]
    assert names.index("key.asc") < names.index("InRelease")

    calls = []
    report = release_apt.publish(repo, "o/r", tag="termux-repo",
                                 run=_gh_result(calls))
    assert report["uploaded_index"][-1] == "InRelease"
    uploads = [Path(c[4]).name for c in calls if c[:3] == ["gh", "release", "upload"]]
    # key goes with the index, and the packages precede both
    assert uploads.index("key.asc") > uploads.index(_deb_name("0.22.0"))


def test_a_pool_path_is_rewritten_to_the_flat_asset_name(tmp_path):
    """A release asset cannot contain '/', so the index must not name one.

    Debian pool layout is `pool/n/<pkg>.deb`; the release holds the bare file
    name, so an unrewritten index 404s on exactly the path it advertises.
    """
    repo = _repo(tmp_path)
    (repo / "Packages").write_text(
        "Package: nastech-agent\nVersion: 0.22.0\n"
        f"Filename: pool/n/{_deb_name('0.22.0')}\n",
        encoding="utf-8",
    )

    assert release_apt.flatten_packages(repo) is True
    flat = (repo / "Packages").read_text(encoding="utf-8-sig")
    assert f"Filename: {_deb_name('0.22.0')}" in flat
    assert "/pool/" not in flat
    # the compressed index must agree with the plain one
    assert f"Filename: {_deb_name('0.22.0')}" in gzip.open(
        repo / "Packages.gz", "rt", encoding="utf-8").read()
    # a second pass is a no-op
    assert release_apt.flatten_packages(repo) is False


def test_a_tilde_version_rewrites_to_the_asset_github_holds(tmp_path):
    """`Filename:` must name the respelled asset while `Version:` keeps the `~`."""
    repo = _repo(tmp_path)
    canary = "0.21.5~canary.20261101T000000Z-1"
    (repo / "Packages").write_text(
        f"Package: nastech-agent\nVersion: {canary}\n"
        f"Filename: pool/n/{_deb_name(canary)}\n",
        encoding="utf-8",
    )
    release_apt.flatten_packages(repo)
    text = (repo / "Packages").read_text(encoding="utf-8")
    assert f"Version: {canary}" in text
    assert f"Filename: {_deb_name(canary).replace('~', '-')}" in text


@pytest.fixture
def short_home():
    """gpg homedirs must be SHORT: the agent's AF_UNIX socket lives inside the
    homedir and pytest's tmp_path tree is longer than that."""
    made = []

    def make():
        d = Path(tempfile.mkdtemp(prefix="apt-publish-gnupg-"))
        made.append(d)
        return d

    yield make
    for d in made:
        shutil.rmtree(d, ignore_errors=True)


def _signing_key_file(home: Path) -> Path:
    stage_apt_repo._gpg_run(
        home, ["--quick-generate-key", "Nastech APT Test <apt-test@example.invalid>",
               "ed25519", "sign", "never"], passphrase="")
    listing = stage_apt_repo._gpg_run(
        home, ["--with-colons", "--list-secret-keys"]).stdout.decode("utf-8", "replace")
    fpr = next(
        line.split(":")[9] for line in listing.splitlines()
        if line.startswith("fpr:")
    )
    keyfile = home / "secret.asc"
    keyfile.write_bytes(stage_apt_repo._gpg_run(
        home, ["--armor", "--export-secret-keys", fpr], passphrase="").stdout)
    return keyfile


@pytest.mark.skipif(not GPG_PRESENT, reason="gpg binary not available")
def test_flatten_publishes_a_flat_feed_that_stays_signed(tmp_path, short_home):
    """Flattening rewrites every path the Release describes, so it re-signs.

    The whole feed contract in one run: stage a real signed Debian tree, flatten
    it, and the result must be something apt can install -- flat names, checksums
    that match the uploaded bytes, and a signature a device can check with only
    the published key.
    """
    keyfile = _signing_key_file(short_home())
    canary = "0.21.5~canary.20261101T000000Z-1"
    pool = tmp_path / "pool-in"
    _signing_debs(pool, ("0.21.4-1", canary))
    out = tmp_path / "staged"
    assert stage_apt_repo.main(["--pool", str(pool), "--out", str(out),
                                "--suite", "nastech-canary",
                                "--gpg-key-file", str(keyfile)]) == 0

    flat = release_apt.flatten(out, tmp_path / "flat", keyfile)

    assert sorted(p.name for p in flat.iterdir()) == sorted(
        [_deb_name("0.21.4-1"), _deb_name(canary).replace("~", "-"),
         *release_apt.INDEX_FILES])
    assert not (flat / "dists").is_dir() and not (flat / "pool").is_dir()

    packages_text = (flat / "Packages").read_text(encoding="utf-8")
    assert f"Filename: {_deb_name(canary).replace('~', '-')}" in packages_text
    assert f"Version: {canary}" in packages_text
    release_text = (flat / "Release").read_text(encoding="utf-8")
    assert "Acquire-By-Hash" not in release_text
    assert "main/binary-aarch64" not in release_text
    for digest, size, name in re.findall(r" ([0-9a-f]{64})\s+(\d+) (\S+)", release_text):
        data = (flat / name).read_bytes()
        assert hashlib.sha256(data).hexdigest() == digest, name
        assert len(data) == int(size), name

    # An independent keyring holding only the published key accepts both
    # signatures -- exactly the position a phone is in.
    keyring = short_home()
    stage_apt_repo._gpg_run(keyring, ["--import"], stdin=(flat / "key.asc").read_bytes())
    home = stage_apt_repo._gpg_homedir_arg(keyring)
    for args in ((str(flat / "InRelease"),),
                 (str(flat / "Release.gpg"), str(flat / "Release"))):
        verified = subprocess.run(
            ["gpgv", "--homedir", home, "--keyring", f"{home}/pubring.kbx", *args],
            capture_output=True, check=False)
        assert verified.returncode == 0, verified.stderr.decode()


def test_the_repository_release_is_created_and_published():
    """A draft release's assets 404 for everyone, so it must be published."""
    calls = []

    def run(argv, **kwargs):
        calls.append(argv)
        if argv[:3] == ["gh", "release", "view"]:
            return Result(returncode=1, stderr="release not found")
        return Result()

    release_apt.ensure_published_release("termux-repo", "o/r", run=run)
    assert calls[1][:3] == ["gh", "release", "create"]
    assert calls[-1][:3] == ["gh", "release", "edit"]
    assert "--draft=false" in calls[-1]
