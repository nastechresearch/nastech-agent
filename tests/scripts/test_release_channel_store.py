"""The channel store is SELECTED, never assumed.

`channel_releases` and `channel_publish` built `R2ChannelStore` and wrote feeds
with `r2.put(...)` directly, bypassing the `configured_store` seam
`ghpages.py` already provides, so a release plane with zero R2 env could not
publish even with `RELEASE_CHANNEL_STORE=github`. These tests pin the
behavioural contract: with the GitHub store selected, publication legs read and
write through the GitHub-native store with NO R2 environment at all, while an
explicitly selected r2 store keeps its exact behavior (an in-flight release is
never repointed)."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest
import nastech_yaml as yaml

from nastech_cli.release_channels import build_prefix, canonical_json, channel_key
from scripts.releases import channel_publish, channel_releases
from tests.scripts.test_release_ghpages import gh_store_server, make_store

REPO = "example/nastech-agent"
R2_ENV = ("CLOUDFLARE_R2_ACCOUNT_ID", "CLOUDFLARE_R2_ACCESS_KEY_ID",
          "CLOUDFLARE_R2_SECRET_ACCESS_KEY", "CLOUDFLARE_R2_BUCKET",
          "CLOUDFLARE_R2_PUBLIC_URL")


@pytest.fixture
def github_plane(monkeypatch):
    """The selected store is GitHub and no R2 environment exists anywhere."""
    monkeypatch.setenv("RELEASE_CHANNEL_STORE", "github")
    monkeypatch.delenv("R2_DISPOSABLE_RUN", raising=False)
    for name in R2_ENV:
        monkeypatch.delenv(name, raising=False)


def _seed_head(target) -> str:
    """Write a stable-release record with a head through the same store."""
    from scripts.releases.channels import preview_identity

    build_id = "a" * 32
    store = make_store(target, _sleep=lambda _s: None)
    manifest = {"schema": 1, "request": {"version": "9.9.9"}}
    manifest_key = build_prefix(build_id) + "build.json"
    store.put(manifest_key, canonical_json(manifest))
    record = {"schema": 1, "name": "stable", "repository": REPO, "policy": "stable-release",
              "state": "active", "revision": 2, "nextSequence": 5,
              "identity": preview_identity("stable", "0" * 16),
              "head": {"buildId": build_id, "sequence": 4, "manifestKey": manifest_key,
                       "sha256": hashlib.sha256(canonical_json(manifest)).hexdigest()}}
    store.put(channel_key("stable"), canonical_json(record))
    return manifest_key


class TestSelectedStoreReads:
    def test_stable_head_version_reads_the_github_store_with_zero_r2_env(self, github_plane, monkeypatch):
        with gh_store_server() as target:
            monkeypatch.setenv("RELEASE_GITHUB_API", target["api"])
            monkeypatch.setenv("RELEASE_PAGES_PUBLIC_BASE", target["pages"])
            _seed_head(target)
            monkeypatch.setenv("GITHUB_REPOSITORY", REPO)
            assert channel_releases.stable_head_version({"GITHUB_REPOSITORY": REPO}) == "9.9.9"

    def test_read_archive_bytes_reads_the_selected_store(self, github_plane, monkeypatch):
        # The sequencer's read leg (~407) inherits the seam: no R2 env, no R2 class.
        with gh_store_server() as target:
            monkeypatch.setenv("RELEASE_GITHUB_API", target["api"])
            monkeypatch.setenv("RELEASE_PAGES_PUBLIC_BASE", target["pages"])
            manifest_key = _seed_head(target)
            monkeypatch.setenv("GITHUB_REPOSITORY", REPO)
            found = channel_releases.read_archive_bytes(manifest_key)
            assert json.loads(found)["request"]["version"] == "9.9.9"

    def test_explicit_r2_selection_still_builds_the_r2_store(self, monkeypatch):
        # Fail-loud symmetry: selecting r2 must not be silently repointed to GitHub.
        from scripts.releases.channels import R2ChannelStore
        monkeypatch.delenv("RELEASE_CHANNEL_STORE", raising=False)
        monkeypatch.delenv("R2_DISPOSABLE_RUN", raising=False)
        monkeypatch.setattr("scripts.releases.r2.credentials",
                            lambda: ({"access_key_id": "a", "secret_key": "b"}, "http://r2-base", "bucket"))
        publisher = channel_releases.configured_channel_publisher(
            REPO, authorize=lambda _action, _record: None)
        assert isinstance(publisher.store, R2ChannelStore)

    def test_channel_public_base_moves_with_the_patched_r2_origin_seam(self, monkeypatch):
        # The store and its public origin are chosen together: an origin redirected
        # through r2.public_base_url (the release controller's own seam) must move
        # channel_public_base too, or a reader would ask keys the store never wrote.
        from scripts.releases.r2_scope import channel_public_base
        monkeypatch.delenv("RELEASE_CHANNEL_STORE", raising=False)
        monkeypatch.delenv("R2_DISPOSABLE_RUN", raising=False)
        monkeypatch.delenv("CLOUDFLARE_R2_PUBLIC_URL", raising=False)
        monkeypatch.setattr("scripts.releases.r2.public_base_url", lambda: "http://127.0.0.1:9/stub")
        assert channel_public_base() == "http://127.0.0.1:9/stub"


class TestSelectedStoreWrites:
    def test_feeds_go_through_the_store_with_digest_pinned_public_readback(self, github_plane, tmp_path,
                                                                           monkeypatch):
        with gh_store_server() as target:
            store = make_store(target, _sleep=lambda _s: None)
            monkeypatch.setattr("scripts.releases.r2.put",
                                lambda **kwargs: (_ for _ in ()).throw(AssertionError("direct r2.put bypassed the store")))
            from nastech_cli.release_channels import ChannelReader
            from scripts.releases.channels import write_immutable_feeds

            root = tmp_path / "stage"
            root.mkdir()
            feed = root / "stable-mac.yml"
            feed.write_bytes(b"feed-bytes")
            prefix = build_prefix("b" * 32)
            write_immutable_feeds(store, ChannelReader(target["pages"], REPO), prefix, root, [feed])
            assert target["blobs"][prefix + "stable-mac.yml"][0] == b"feed-bytes"
            # Create-only stays create-only: a different body cannot replace the feed.
            feed.write_bytes(b"other-bytes")
            from scripts.releases.channels import ChannelConflict
            with pytest.raises(ChannelConflict):
                write_immutable_feeds(store, ChannelReader(target["pages"], REPO), prefix, root, [feed])

    def test_channel_publish_writes_feeds_and_manifest_through_the_publisher_store(self, github_plane,
                                                                                   tmp_path, monkeypatch):
        class RecordingStore:
            def __init__(self):
                self.puts = []

            def put(self, key, body, etag=None):
                self.puts.append((key, body))

        class RecordingReader:
            def __init__(self, store):
                self.store = store
                self.digest_checks = 0

            def read_bytes(self, key, sha256=None):
                body = dict(self.store.puts)[key]
                if sha256 is not None:
                    self.digest_checks += 1
                    assert hashlib.sha256(body).hexdigest() == sha256
                return body

        class FakePublisher:
            public_base = "http://127.0.0.1:9"

            def __init__(self):
                self.store = RecordingStore()
                self.reader = RecordingReader(self.store)

            def request(self, build_id, sha256=None):
                return self.admitted

            def _read(self, name):
                return ({"policy": "preview", "state": "active"}, "etag")

            def _preview(self, action, record):
                pass

            def promote(self, build_id):
                return {"promoted": build_id}

        request = {"buildId": "c" * 32, "channel": "demo", "commit": "d" * 40,
                   "version": "0.0.1", "publicBase": "http://127.0.0.1:9"}
        publisher = FakePublisher()
        publisher.admitted = request
        root = tmp_path / "root"
        root.mkdir()
        feed = root / "stable.appinstaller"
        feed.write_bytes(b"<AppInstaller/>")
        monkeypatch.setattr(channel_publish.handoff, "fetch_channel_build", lambda *a, **k: None)
        monkeypatch.setattr(channel_publish, "assemble",
                            lambda request, root, needs: ({"schema": 1, "request": request}, [feed]))
        needs = {name: {"result": "success"} for name in channel_publish.REQUIRED_JOBS}
        # On the R2-assumed base this raises SystemExit: r2.put demands the
        # bucket env this (GitHub-selected) run no longer has.
        result = channel_publish.publish(request, root, needs=needs, publisher=publisher)
        prefix = build_prefix(request["buildId"])
        assert result == {"promoted": request["buildId"]}
        puts = dict(publisher.store.puts)
        assert puts[prefix + "stable.appinstaller"] == b"<AppInstaller/>"
        assert puts[prefix + "build.json"] == canonical_json({"schema": 1, "request": request})
        assert publisher.reader.digest_checks >= 1


class TestControllerPinning:
    @pytest.mark.parametrize("workflow", ["canary-release.yml", "release.yml"])
    def test_release_controllers_pin_both_store_seams_to_github(self, workflow):
        # The controller reads handoff/channel defaults; while a non-secret
        # CLOUDFLARE_R2_BUCKET variable exists, an unpinned job silently chose R2.
        root = Path(__file__).resolve().parents[2]
        controller = yaml.safe_load((root / ".github/workflows" / workflow).read_text(encoding="utf-8"))
        assert controller["env"]["RELEASE_CHANNEL_STORE"] == "github"
        assert controller["env"]["RELEASE_HANDOFF_STORE"] == "github"
