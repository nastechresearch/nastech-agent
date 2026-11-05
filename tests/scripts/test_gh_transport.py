"""The handoff store is GitHub Release assets: same keys, same receipts, write-once bytes.

These drive the transport `handoff` now stages through, against a fake `gh` that
answers like the release-asset API. The properties are the ones R2 gave the
release plane and a draft release does not give for free: one key maps to one
asset, staged bytes cannot be silently replaced, and a download is only trusted
after its size and sha256 match the receipt that named it.
"""

import hashlib
import json
import re
import subprocess
from urllib.parse import unquote

import pytest

from scripts.releases import gh_transport, handoff, r2


class FakeReleaseApi:
    """The release-asset endpoints the transport uses, kept in memory.

    Faithful in the four ways that let broken handoff staging reach production:
    `releases/tags/{tag}` answers 404 for a draft, a POST mints a second release for
    a tag a draft already carries, the release a POST hands back has no readable
    asset route until its first upload, and -- the one that made every leg of run
    41852094357 die before uploading anything -- `gh api` infers POST from the mere
    presence of a `-f`/`-F` field.  So a store that finds its release only by the tag
    route splits one canary across a draft per leg, and a paginated read that does not
    name its method is a write GitHub answers with 404.
    """

    NOT_FOUND = "HTTP 404: Not Found"

    def __init__(self):
        self.rows: dict[int, dict] = {}
        # tag -> the release a test asserts on: the newest the API accepted for it.
        self.releases: dict[str, int] = {}
        # tag -> how many releases the API accepted for it, the thing GitHub does
        # not enforce and the plane has to.
        self.minted: dict[str, int] = {}
        self.assets: dict[int, list[dict]] = {}
        self.payloads: dict[int, bytes] = {}
        # The release the last POST opened: its asset route answers 404 until the
        # first upload, which is how run 41852094357 lost the win32-x64 leg.
        self.freshly_minted: int | None = None
        self.next_id = 1

    def create(self, tag: str, *, draft: bool = True) -> int:
        rid = self.next_id
        self.next_id += 1
        self.rows[rid] = {"id": rid, "tag_name": tag, "draft": draft}
        self.assets[rid] = []
        self.releases[tag] = rid
        self.minted[tag] = self.minted.get(tag, 0) + 1
        return rid

    @staticmethod
    def _done(stdout="", returncode=0, stderr=""):
        return subprocess.CompletedProcess(["gh"], returncode, stdout=stdout, stderr=stderr)

    @staticmethod
    def _fields(argv):
        return [argv[index + 1] for index, arg in enumerate(argv) if arg in ("-f", "-F")]

    @classmethod
    def _method(cls, argv):
        """The verb `gh api` will actually send, which is not always the one asked for."""
        for flag in ("-X", "--method"):
            if flag in argv:
                return argv[argv.index(flag) + 1].upper()
        return "POST" if cls._fields(argv) else "GET"

    def __call__(self, argv, **kwargs):
        route = re.sub(r"^repos/o/r/", "", argv[2])
        method = self._method(argv)
        if m := re.fullmatch(r"releases/tags/(.+)", route):
            if method != "GET":
                return self._done(returncode=1, stderr=self.NOT_FOUND)
            for row in self.rows.values():
                if row["tag_name"] == m.group(1) and not row["draft"]:
                    return self._done(json.dumps({"id": row["id"]}))
            return self._done(returncode=1, stderr=self.NOT_FOUND)
        if route == "releases":
            if method == "GET":
                page = int(next((field.split("=")[1] for field in self._fields(argv)
                                 if field.startswith("page=")), 1))
                rows = sorted(self.rows.values(), key=lambda row: -row["id"])
                return self._done(json.dumps(rows[(page - 1) * 100:page * 100]))
            tag = next((field.split("=", 1)[1] for field in self._fields(argv)
                        if field.startswith("tag_name=")), None)
            if tag is None:
                return self._done(returncode=1, stderr="HTTP 422: Validation Failed")
            rid = self.create(tag)
            self.freshly_minted = rid
            return self._done(json.dumps({"id": rid, "draft": True}))
        if m := re.fullmatch(r"releases/(\d+)/assets\?name=(.*)", route):
            if method != "POST":
                return self._done(returncode=1, stderr=self.NOT_FOUND)
            payload = open(argv[argv.index("--input") + 1], "rb").read()
            asset = {"id": self.next_id, "name": unquote(m.group(2)), "size": len(payload)}
            self.next_id += 1
            self.assets[int(m.group(1))].append(asset)
            self.payloads[asset["id"]] = payload
            self.freshly_minted = None
            return self._done(json.dumps(asset))
        if m := re.fullmatch(r"releases/(\d+)/assets", route):
            if method != "GET":
                return self._done(returncode=1, stderr=self.NOT_FOUND)
            if int(m.group(1)) == self.freshly_minted:
                return self._done(returncode=1, stderr=self.NOT_FOUND)
            rows = self.assets[int(m.group(1))]
            page = int(next((field.split("=")[1] for field in self._fields(argv)
                             if field.startswith("page=")), 1))
            return self._done(json.dumps(rows[(page - 1) * 100:page * 100]))
        if m := re.fullmatch(r"releases/assets/(\d+)", route):
            asset_id = int(m.group(1))
            if "DELETE" in argv:
                for rows in self.assets.values():
                    rows[:] = [row for row in rows if row["id"] != asset_id]
                return self._done("{}")
            kwargs["stdout"].write(self.payloads[asset_id])
            return self._done()
        raise AssertionError(f"unhandled gh api route: {route}")


@pytest.fixture
def store(monkeypatch):
    fake = FakeReleaseApi()
    monkeypatch.setattr(gh_transport, "_run", fake)
    monkeypatch.setenv("GH_TOKEN", "token")
    monkeypatch.setenv("GITHUB_REPOSITORY", "o/r")
    monkeypatch.delenv("R2_DISPOSABLE_RUN", raising=False)
    # The same lever the release workflows set: stage through the release store
    # whatever the surrounding CI environment happens to name as feed origin.
    monkeypatch.setenv("RELEASE_HANDOFF_STORE", "github")
    return fake


def written(root, name, body):
    root.mkdir(parents=True, exist_ok=True)
    path = root / name
    path.write_bytes(body)
    return str(path)


def test_two_keys_that_a_naive_flattening_would_merge_stay_distinct(store):
    """`a/b.zip` and `a__b.zip` must not become one asset, so `/` cannot map to `_`."""
    one = gh_transport.asset_name("releases/tag/v1/a/b.zip")
    two = gh_transport.asset_name("releases/tag/v1/a__b.zip")
    assert one != two
    assert gh_transport.key_for_asset(one) == "releases/tag/v1/a/b.zip"


def test_a_tag_stages_on_its_own_release_and_a_commit_build_needs_no_new_ref(store, tmp_path):
    store.create("v0.22.0")
    gh_transport.put(key="releases/tag/v0.22.0/darwin-arm64/app.zip",
                     file=written(tmp_path, "app.zip", b"a"), key_is_full=True, immutable=True)
    gh_transport.put(key=f"releases/commit/{'c' * 40}/win32-x64/app.msix",
                     file=written(tmp_path, "app.msix", b"b"), key_is_full=True, immutable=True)
    assert sorted(store.releases) == sorted(["v0.22.0", gh_transport.STAGING_RELEASE])
    assert sum(len(rows) for rows in store.assets.values()) == 2


def test_the_leg_that_opens_its_release_uploads_to_it_instead_of_reading_it(store, tmp_path):
    """Run 41852094357, win32-x64: the leg POSTed its release at 15:24:39 and the asset
    route of the id it was handed back answered 404 in the same second, so the leg died
    having staged nothing.  A release opened a moment ago has no assets by definition --
    reading for one is a call that can only fail."""
    tag = "v0.21.5+canary.20261104T045649Z"
    key = f"releases/tag/{tag}/win32-x64/app.zip"
    gh_transport.put(key=key, file=written(tmp_path, "app.zip", b"z"),
                     key_is_full=True, immutable=True)
    assert [row["name"] for row in store.assets[store.releases[tag]]] == \
        [gh_transport.asset_name(key)]


def test_a_paginated_read_is_a_read_and_not_the_write_gh_infers_from_a_field(store):
    """`gh api` sends POST whenever a `-f`/`-F` field is present, whatever the caller meant.

    Every asset listing asks for `per_page` and `page`, so the plane's most-called read
    was a write in GitHub's eyes: a 404 from a route that creates nothing, which the
    transport reported as a missing release and answered by opening another draft.
    """
    rid = store.create("v0.22.0", draft=False)
    store.assets[rid] = [{"id": 1000 + i, "name": f"asset-{i}.zip"} for i in range(150)]
    assert len(gh_transport._assets("o/r", rid)) == 150


def test_every_leg_of_one_unpublished_tag_shares_the_draft_the_first_leg_opened(store, tmp_path):
    """Six legs of one canary are six writers of one release, not six releases.

    GitHub answers `releases/tags/{tag}` for a published release only, and a POST
    never refuses a tag a draft already carries, so a transport that finds its
    release by the tag route mints one draft per leg -- the six identical
    `v0.22.0+canary.*` drafts. The list route is the only one that can see a draft,
    so the lookup has to go there before opening another.
    """
    tag = "v0.22.0+canary.20261104T122145Z"
    for leg in ("darwin-arm64", "darwin-x64", "win32-arm64", "win32-x64",
                "linux-x64", "termux"):
        gh_transport.put(key=f"releases/tag/{tag}/{leg}/app.zip",
                         file=written(tmp_path, f"{leg}.zip", leg.encode()),
                         key_is_full=True, immutable=True)
    assert store.minted == {tag: 1}
    assert len(store.assets[store.releases[tag]]) == 6


def test_a_restage_of_the_same_bytes_is_idempotent_and_different_bytes_are_refused(store, tmp_path):
    key = "releases/tag/v0.22.0/darwin-arm64/app.zip"
    store.create("v0.22.0")
    gh_transport.put(key=key, file=written(tmp_path, "one.zip", b"first"),
                     key_is_full=True, immutable=True)
    gh_transport.put(key=key, file=written(tmp_path, "two.zip", b"first"),
                     key_is_full=True, immutable=True)
    assert len(store.assets[store.releases["v0.22.0"]]) == 1
    with pytest.raises(gh_transport.R2RequestError, match="differ"):
        gh_transport.put(key=key, file=written(tmp_path, "three.zip", b"second"),
                         key_is_full=True, immutable=True)
    assert len(store.assets[store.releases["v0.22.0"]]) == 1


def test_an_unconditional_write_replaces_the_asset(store, tmp_path):
    key = "feeds/stable.json"
    gh_transport.put(key=key, file=written(tmp_path, "one.json", b"one"), key_is_full=True)
    gh_transport.put(key=key, file=written(tmp_path, "two.json", b"two"), key_is_full=True)
    rows = store.assets[store.releases[gh_transport.STAGING_RELEASE]]
    assert len(rows) == 1 and store.payloads[rows[0]["id"]] == b"two"


def test_a_download_is_kept_only_after_it_matches_its_receipt(store, tmp_path):
    key = "releases/tag/v0.22.0/darwin-arm64/app.zip"
    store.create("v0.22.0")
    gh_transport.put(key=key, file=written(tmp_path, "app.zip", b"z" * 32),
                     key_is_full=True, immutable=True)
    target = tmp_path / "out" / "app.zip"
    gh_transport.fetch_key(key, target, expected_size=32,
                           expected_sha256=hashlib.sha256(b"z" * 32).hexdigest())
    assert target.read_bytes() == b"z" * 32
    with pytest.raises(ValueError, match="checksum"):
        gh_transport.fetch_key(key, target, expected_size=32, expected_sha256="0" * 64)
    with pytest.raises(ValueError, match="size"):
        gh_transport.fetch_key(key, target, expected_size=7,
                               expected_sha256=hashlib.sha256(b"z" * 32).hexdigest())
    assert not (tmp_path / "out" / "app.zip.part").exists()


def test_a_stale_archive_origin_fails_instead_of_reading_github_anyway(store, tmp_path):
    """A workflow still naming the old worker must stop, not silently change store."""
    key = "releases/tag/v0.22.0/darwin-arm64/app.zip"
    store.create("v0.22.0")
    gh_transport.put(key=key, file=written(tmp_path, "app.zip", b"a"),
                     key_is_full=True, immutable=True)
    worker = "https://nastech-assets.example.workers.dev"
    with pytest.raises(ValueError, match="release archive"):
        gh_transport.read_public_receipt(worker, key)
    with pytest.raises(ValueError, match="release archive"):
        gh_transport.download_public_object(worker, key, tmp_path / "x", expected_size=1,
                                            expected_sha256=hashlib.sha256(b"a").hexdigest())
    gh_transport.download_public_object(gh_transport.public_base_url(), key, tmp_path / "x",
                                        expected_size=1,
                                        expected_sha256=hashlib.sha256(b"a").hexdigest())
    assert (tmp_path / "x").read_bytes() == b"a"


def test_handoff_stages_a_leg_and_fetches_the_same_bytes_back(store, tmp_path):
    """The wiring, not just the store: a receipt written on GitHub still round-trips."""
    root = tmp_path / "build"
    (root / "darwin-arm64").mkdir(parents=True)
    (root / "darwin-arm64" / "app.zip").write_bytes(b"payload")
    store.create("v0.22.0")
    staged = handoff.stage("v0.22.0", "a" * 40, "darwin-arm64", root, ["darwin-arm64/*.zip"])
    assert [row["path"] for row in staged["files"]] == ["darwin-arm64/app.zip"]

    back = tmp_path / "publish"
    receipts = handoff.fetch("v0.22.0", "a" * 40, ["darwin-arm64"], back)
    assert receipts[0]["name"] == "darwin-arm64"
    assert (back / "darwin-arm64" / "app.zip").read_bytes() == b"payload"
    assert json.loads((back / "handoff-darwin-arm64.json").read_text())["tag"] == "v0.22.0"


def test_a_missing_receipt_is_reported_as_missing_work(store):
    store.create("v0.22.0")
    with pytest.raises(handoff.MissingReceipt):
        handoff.read_commit_receipt("b" * 40, "termux")
    # Looking for nothing used to open the staging release to look inside it, which
    # is how a failed read added to the very draft sprawl the publish job drowns in.
    assert gh_transport.STAGING_RELEASE not in store.releases


def test_the_store_needs_a_token_and_a_repository(store, monkeypatch):
    monkeypatch.delenv("GH_TOKEN")
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    with pytest.raises(ValueError, match="GH_TOKEN"):
        gh_transport.credentials()
    monkeypatch.setenv("GITHUB_TOKEN", "token")
    monkeypatch.delenv("GITHUB_REPOSITORY")
    with pytest.raises(ValueError, match="GITHUB_REPOSITORY"):
        gh_transport.credentials()


def test_one_store_serves_a_whole_run(tmp_path, monkeypatch):
    """Legs stage to one store and the publish job fetches from it, in every calling shape.

    R2 is being deleted job by job, not atomically, so a run whose leg still names a
    bucket while its fetch job does not must not split across two stores: the pin, or
    the archive origin a public read already carries, decides.
    """
    for name in ("RELEASE_HANDOFF_STORE", "CLOUDFLARE_R2_BUCKET", "CLOUDFLARE_R2_ACCOUNT_ID"):
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setenv("GITHUB_REPOSITORY", "o/r")

    # Nothing configured means the release store.
    assert handoff.store() is gh_transport
    # R2 is selected while it can still be addressed, so an in-flight release cannot
    # be repointed mid-publish, and a stale R2 origin on a read resolves to R2 too.
    monkeypatch.setenv("CLOUDFLARE_R2_BUCKET", "nastech-releases")
    assert handoff.store() is r2
    r2_origin = "https://assets.nastech.example/nastech-releases"
    assert handoff.store(r2_origin) is r2
    # The workflow lever wins over both, in either direction.
    monkeypatch.setenv("RELEASE_HANDOFF_STORE", "github")
    assert handoff.store() is gh_transport
    assert handoff.store(r2_origin) is gh_transport
    monkeypatch.setenv("RELEASE_HANDOFF_STORE", "s3")
    with pytest.raises(ValueError, match="s3"):
        handoff.store()


def test_a_public_read_names_the_store_it_reads_from(monkeypatch):
    """A credential-free fetch decides by origin, because it has no credentials left to ask."""
    for name in ("RELEASE_HANDOFF_STORE", "CLOUDFLARE_R2_BUCKET", "GITHUB_REPOSITORY"):
        monkeypatch.delenv(name, raising=False)
    assert handoff.store("https://github.com/o/r/releases/download") is r2

    monkeypatch.setenv("GITHUB_REPOSITORY", "o/r")
    assert handoff.store("https://github.com/o/r/releases/download") is gh_transport
    # Only the exact archive origin counts; a path under it is a stale handoff's base.
    assert handoff.store("https://github.com/other/releases/download") is r2


def test_prune_clears_one_namespace_and_leaves_the_others(store, tmp_path):
    for key in (f"releases/commit/{'1' * 40}/a/app.zip",
                f"releases/commit/{'1' * 40}/b/app.zip",
                f"releases/commit/{'2' * 40}/a/app.zip"):
        gh_transport.put(key=key, file=written(tmp_path, "app.zip", b"x"),
                         key_is_full=True, immutable=True)
    doomed = gh_transport.prune(f"releases/commit/{'1' * 40}/")
    assert len(doomed) == 2
    assert len(store.assets[store.releases[gh_transport.STAGING_RELEASE]]) == 1
