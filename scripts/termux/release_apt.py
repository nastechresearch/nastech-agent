"""Publish the Termux APT repository as the assets of one fixed-tag release.

`pkg` is apt, so it needs a stable *base* URL that it can append
``Release``/``Packages`` and each stanza's ``Filename`` to.  A GitHub release
gives exactly that: ``<repo>/releases/download/<tag>/<asset>``, and apt follows
the redirect to GitHub's object store.  Cloudflare R2 no longer serves release
assets, so it serves no feed either.

The tag is fixed per channel (``termux-repo`` / ``termux-repo-canary``) and its
index assets are therefore *replaced* on every publish -- the one deliberate
exception to release-asset immutability, because a package manager cannot be
pointed at a URL that changes per build.  That replacement is exactly what
cannot live in an object store that refuses overwrite: ``Release`` carries a
mandatory ``Date:`` and ``InRelease`` a signature timestamp, so a second
publish of one tag produces different bytes under one key.

Two platform facts measured 2026-11-03 against this repository shape the layout:

* an asset name is one path component and cannot hold ``/`` (``dists/
  nastech-stable/InRelease`` is stored as ``dists.nastech-stable.InRelease``),
  so the feed is published FLAT and the source line is ``deb <base> ./`` -- apt
  then reads ``<base>/Release``, ``<base>/Packages`` and each ``Filename:``
  relative to the base.
* an asset name cannot hold ``~`` either (it is stored with ``.``), while apt
  percent-escapes the ``~`` of ``Filename:`` as ``%7e``.  So the asset name
  drops ``~`` and ``Filename:`` names that asset, while ``Version:`` keeps the
  ``~`` and dpkg's ranking is untouched.

Because flattening changes every path the ``Release`` document describes, the
flat ``Release`` is rewritten (base-relative names, no ``Acquire-By-Hash``) and
re-SIGNED with the same key by ``stage_apt_repo.sign()`` -- the feed never goes
out unsigned, and an unsigned feed is only ever reachable with
``[trusted=yes]``, which throws the signature away.

Order is the whole design:

1. upload the new ``.deb`` and confirm the tag stored each under the name the
   index is about to advertise,
2. upload the regenerated index (``Packages``, ``Packages.gz``, ``Release``,
   ``Release.gpg``, ``key.asc`` and finally ``InRelease``), ``InRelease`` last
   because it is the first file apt reads,
3. delete the packages the immediately-previous index cannot name.

A client reading mid-publish therefore sees either the old complete index or
the new complete index, never one that names a file which is not there -- which
is how the R2 staging failed on 2026-10-28
(``404 ... nastech-agent_0.21.5~canary..._aarch64.deb``) and how its successor
failed on 2026-11-03 (``412 PreconditionFailed`` on
``releases/tag/<tag>/apt/dists/nastech-canary/InRelease``).
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

from .stage_apt_repo import deb_version_key, sign

# Each channel owns one tag: an index written to another channel's tag would
# silently overwrite that channel's feed, and `pkg` cannot be repointed per build.
CHANNEL_TAGS = {"stable": "termux-repo", "canary": "termux-repo-canary"}

# Upload order, not a set: `Packages` before the documents that describe it, and
# `InRelease` LAST because it is the first file apt reads -- a client that sees
# the new InRelease must never be able to follow it onto a missing file.
# `key.asc` sits between the detached signature and `InRelease`, so whatever can
# read the new index can always fetch the key that verifies it.
INDEX_FILES = ("Packages", "Packages.gz", "Release", "Release.gpg", "key.asc", "InRelease")

# The repository's public signing key, published beside the index so a user can
# install it in one command.  Without it a signed repository is unusable: apt
# has nothing to verify `InRelease` against.
PUBLIC_KEY_NAME = "key.asc"

# A replaced asset keeps serving the previous bytes for a while, so a still
# cached index from the previous publish can still name that publish's older
# generation: keep one beyond what it can point at.
KEEP_PACKAGES = 3

# A Debian release names its index files under the component directory and
# advertises by-hash paths; a flat feed has neither, and both would 404.
_RELEASE_DROP_FIELDS = ("Acquire-By-Hash",)
_CHECKSUM_SECTION_RE = re.compile(r"^(?:MD5Sum|SHA1|SHA256|SHA512):$")


class AptReleaseError(RuntimeError):
    """The staged repository cannot be published as it stands."""


def tag_for_channel(channel: str) -> str:
    """The one asset tag a channel may write to."""
    try:
        return CHANNEL_TAGS[channel]
    except KeyError:
        raise AptReleaseError(
            f"no asset tag for channel {channel!r}; known: {', '.join(sorted(CHANNEL_TAGS))}"
        ) from None


# Every character outside this set is one GitHub was observed to rewrite: '~',
# '/' and ' ' came back stored as '.', while '+', '-', '.', '_' and alphanumerics
# were stored verbatim.  A name GitHub rewrites silently dangles the index that
# names it, so an unmeasured character (e.g. a dpkg epoch ':') stops the publish.
_SAFE_ASSET_RE = re.compile(r"^[A-Za-z0-9._+-]+$")


def asset_name(staged: str) -> str:
    """The release-asset name a staged file must be published under."""
    flat = staged.replace("~", "-")
    if not _SAFE_ASSET_RE.fullmatch(flat):
        raise AptReleaseError(
            f"{staged} holds a character GitHub would rewrite in an asset name"
        )
    return flat


def _gh(argv: list[str], run=subprocess.run) -> str:
    result = run(["gh", *argv], capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise AptReleaseError(f"gh {' '.join(argv)} failed: {result.stderr.strip()}")
    return result.stdout


_POOL_FILENAME_RE = re.compile(r"^Filename: .*/(?P<name>[^/\n]+)$", re.MULTILINE)


def flatten_packages(repo_dir: Path) -> bool:
    """Point each ``Filename:`` at the flat asset name a release can hold.

    Debian lays a pool out as ``pool/n/<package>_<version>_<arch>.deb``, but a
    release asset cannot contain ``/``, so the pool path a staged index names
    would 404 -- the very failure this migration exists to end. The package is
    uploaded under its bare name, so the index is rewritten to match and
    ``Packages.gz`` regenerated from it. Returns True when it changed anything.
    """
    packages = repo_dir / "Packages"
    if not packages.is_file():
        return False
    text = packages.read_text(encoding="utf-8-sig")
    flat = _POOL_FILENAME_RE.sub(
        lambda match: f"Filename: {asset_name(match.group('name'))}", text)
    if flat == text:
        return False
    packages.write_text(flat, encoding="utf-8")
    with gzip.open(repo_dir / "Packages.gz", "wt", encoding="utf-8") as handle:
        handle.write(flat)
    return True


def _flat_release_text(staged_release: str, flat_dir: Path) -> str:
    """The staged ``Release`` rewritten for the flat feed, checksums included.

    ``stage_apt_repo.py`` lists its index files as ``main/binary-aarch64/Packages``
    and advertises ``Acquire-By-Hash: yes``; both name paths a release asset
    cannot hold.  The names and hashes therefore have to describe the files that
    are actually uploaded -- which is why the result is re-signed rather than
    shipped with the staged signature.
    """
    lines = []
    for line in staged_release.splitlines():
        if _CHECKSUM_SECTION_RE.match(line):
            break
        if not line.startswith(_RELEASE_DROP_FIELDS):
            lines.append(line)
    for algorithm in ("SHA256", "SHA512"):
        rows = []
        for name in ("Packages", "Packages.gz"):
            data = (flat_dir / name).read_bytes()
            digest = hashlib.new(algorithm.lower(), data).hexdigest()
            rows.append(f" {digest} {len(data):8d} {name}")
        lines.append(f"{algorithm}:")
        lines.extend(rows)
    return "\n".join(lines) + "\n"


def flatten(staged: Path, out: Path, gpg_key_file: Path) -> Path:
    """Rebuild the staged ``dists/`` + ``pool/`` tree as one flat feed directory.

    A GitHub release asset name is a single path component, so the Debian
    directory layout cannot be published as it is. Flattening changes every path
    the signed ``Release`` describes, so the flat ``Release`` is rewritten and
    re-signed with the same key: the feed stays signed, never republished
    unsigned.
    """
    index_files = sorted(staged.glob("dists/*/main/binary-*/Packages"))
    if len(index_files) != 1:
        raise AptReleaseError(
            f"{staged} must stage exactly one suite and architecture; "
            f"found {len(index_files)} Packages indexes")
    binary_dir = index_files[0].parent
    suite_dir = binary_dir.parents[1]
    staged_release = suite_dir / "Release"
    if not staged_release.is_file():
        raise AptReleaseError(f"{staged_release} is missing; the feed cannot be signed")
    packages = sorted((staged / "pool").rglob("*.deb")) if (staged / "pool").is_dir() else []
    if not packages:
        raise AptReleaseError(f"no .deb staged under {staged / 'pool'}")

    out.mkdir(parents=True, exist_ok=True)
    for package in packages:
        target = out / asset_name(package.name)
        if target.exists():
            raise AptReleaseError(
                f"{package.name} and another package both publish as {target.name}")
        shutil.copyfile(package, target)
    shutil.copyfile(binary_dir / "Packages", out / "Packages")
    flatten_packages(out)
    (out / "Release").write_text(
        _flat_release_text(staged_release.read_text(encoding="utf-8-sig"), out),
        encoding="utf-8")

    # `sign()` writes InRelease/Release.gpg beside the Release it signs and the
    # public key two levels up -- which is `out`, so the published key is always
    # the key that signed this exact feed, and a failed signature never reaches
    # a tag people install from.
    signing_dir = out / ".signing" / "dists"
    signing_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(out / "Release", signing_dir / "Release")
    sign(signing_dir, signing_dir / "Release", gpg_key_file)
    for name in ("InRelease", "Release.gpg"):
        shutil.move(str(signing_dir / name), str(out / name))
    shutil.rmtree(out / ".signing")
    return out


def ensure_published_release(tag: str, repository: str, run=subprocess.run) -> None:
    """Create the repository release if absent, and make sure it is published.

    A draft release's assets answer 404 to everyone, so an apt source pointing
    at one is dead even with a perfect index. Measured 2026-10-29: every asset
    URL on a scratch draft release returned 404 by both names.
    """
    try:
        _gh(["release", "view", tag, "--repo", repository], run=run)
    except AptReleaseError:
        _gh(["release", "create", tag, "--repo", repository, "--title",
             "Nastech Termux APT repository",
             "--notes", "Generated by the release pipeline; assets are replaced on every publish."],
            run=run)
    _gh(["release", "edit", tag, "--repo", repository, "--draft=false"], run=run)


def staged_files(repo_dir: Path) -> tuple[list[Path], list[Path]]:
    """The packages and the index files a publish must carry, in upload order.

    The guards here are the point of the migration: a Debian tree cannot be a
    release asset (no ``/`` in a name), and an unsigned or keyless feed is one
    ``curl | sed`` away from ``[trusted=yes]``, so an unflattened, unsigned or
    asset-name-hostile directory stops the run instead of publishing a feed that
    404s on the first ``pkg install``.
    """
    for leftover in ("pool", "dists"):
        if (repo_dir / leftover).is_dir():
            raise AptReleaseError(
                f"{repo_dir / leftover} is still the Debian layout; a release asset "
                "cannot hold '/' -- flatten before publishing")
    packages = sorted(p for p in repo_dir.glob("*.deb") if p.is_file())
    if not packages:
        raise AptReleaseError(f"no .deb staged under {repo_dir}")
    hostile = [p.name for p in packages if asset_name(p.name) != p.name]
    if hostile:
        raise AptReleaseError(
            f"{', '.join(hostile)} name a character GitHub rewrites in an asset name")
    missing = [name for name in INDEX_FILES if not (repo_dir / name).is_file()]
    if missing:
        raise AptReleaseError(f"staged repository is missing {', '.join(missing)}")
    return packages, [repo_dir / name for name in INDEX_FILES]


_DEB_VERSION_RE = re.compile(r"^(?P<package>[^_]+)_(?P<version>[^_]+)_(?P<arch>[^_]+)\.deb$")


def deb_version_of(name: str) -> str:
    """The version inside a ``<package>_<version>_<arch>.deb`` file name."""
    match = _DEB_VERSION_RE.match(name)
    if match is None:
        raise AptReleaseError(f"{name} is not a Debian package file name")
    return match.group("version")


def stale_packages(existing: list[str], uploaded: list[str],
                   keep: int = KEEP_PACKAGES) -> list[str]:
    """Published packages to delete, keeping the newest ``keep`` versions.

    ``uploaded`` are the names this publish just added; they are always kept.
    """
    published = [name for name in existing if name.endswith(".deb")]
    known = sorted(set(published) | set(uploaded),
                   key=lambda name: deb_version_key(deb_version_of(name)),
                   reverse=True)
    keep_names = set(uploaded) | set(known[:keep])
    return [name for name in published if name not in keep_names]


def _asset_names(tag: str, repository: str, run=subprocess.run) -> list[str]:
    listing = json.loads(_gh(["release", "view", tag, "--repo", repository,
                              "--json", "assets"], run=run))
    return [asset["name"] for asset in listing.get("assets", [])]


def publish(repo_dir: Path, repository: str, tag: str,
            run=subprocess.run) -> dict:
    """Replace the repository assets in the order that never dangles."""
    ensure_published_release(tag, repository, run=run)
    packages, index = staged_files(repo_dir)
    existing = _asset_names(tag, repository, run=run)

    for package in packages:
        _gh(["release", "upload", tag, str(package), "--repo", repository,
             "--clobber"], run=run)
    # Read the names back before the index can point at them: GitHub rewrites an
    # asset name it cannot hold, and an index naming the pre-rewrite name is the
    # 404 this pipeline exists to prevent.
    stored = set(_asset_names(tag, repository, run=run))
    dangled = [p.name for p in packages if p.name not in stored]
    if dangled:
        raise AptReleaseError(
            f"{tag} stores {', '.join(dangled)} under a different name; publishing "
            "the index would advertise a file the tag cannot serve")
    # Index last: it may only become visible once every file it names exists.
    for path in index:
        _gh(["release", "upload", tag, str(path), "--repo", repository,
             "--clobber"], run=run)

    deleted = stale_packages(existing, [p.name for p in packages])
    for name in deleted:
        _gh(["release", "delete-asset", tag, name, "--repo", repository,
             "--yes"], run=run)
    return {"tag": tag,
            "uploaded_packages": [p.name for p in packages],
            "uploaded_index": [p.name for p in index],
            "deleted_packages": deleted}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python3 -m scripts.termux.release_apt",
        description="Flatten and publish the Termux APT feed as release assets.")
    sub = parser.add_subparsers(dest="command", required=True)
    flat = sub.add_parser("flatten", help="rewrite a staged dists/+pool/ tree as a flat feed")
    flat.add_argument("--staged", type=Path, required=True)
    flat.add_argument("--out", type=Path, required=True)
    # Required, never optional: the flat Release has to be re-signed, and an
    # unsigned feed is only ever reachable by disabling verification.
    flat.add_argument("--gpg-key-file", type=Path, required=True)
    publish_parser = sub.add_parser("publish", help="upload a flat feed to the channel's tag")
    publish_parser.add_argument("--repo-dir", type=Path, required=True)
    publish_parser.add_argument("--repository", required=True)
    # The channel, not a free-form tag: one channel may only ever write its own
    # tag, or a canary run would overwrite the stable index.
    publish_parser.add_argument("--channel", required=True, choices=sorted(CHANNEL_TAGS))
    args = parser.parse_args(argv)

    if args.command == "flatten":
        out = flatten(args.staged, args.out, args.gpg_key_file)
        print(f"flattened {args.staged} -> {out}")
        return 0
    report = publish(args.repo_dir, args.repository, tag=tag_for_channel(args.channel))
    print(json.dumps(report))
    return 0


if __name__ == "__main__":
    sys.exit(main())
