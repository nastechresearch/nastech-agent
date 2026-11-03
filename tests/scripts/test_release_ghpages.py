"""Exercise the GitHub-native control-plane store through real HTTP requests.

A local fake of the Contents API + Git Trees API backs the store tests, so
CAS semantics (create-only, sha match, conflict) are exercised against the
actual wire behavior they will meet in Actions, and Pages public reads are
served out of the same process.
"""
from __future__ import annotations

from base64 import b64decode, b64encode
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from threading import Lock, Thread
from urllib.parse import urlsplit

import pytest

from scripts.releases import ghpages


@contextmanager
def gh_store_server():
    """One server speaks both the Contents API and the Pages origin."""
    blobs, commits, visibility, requests = {}, {}, {}, []
    lock = Lock()

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def _send(self, status, body):
            if isinstance(body, dict | list):
                body = json.dumps(body).encode()
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def contents_path(self):
            return self.path.split("/contents/", 1)[1].split("?ref=")[0]

        def do_GET(self):
            with lock:
                requests.append(("GET", self.path))
            parts = urlsplit(self.path)
            if not parts.path.startswith(("/repos/", "/git/")):
                # Pages origin: public control-plane raw byte reads.
                body = visibility.get(parts.path.lstrip("/"))
                return self._send(200, body) if body is not None else self._send(404, b"not found")
            if parts.path.endswith("/git/trees/main"):
                with lock:
                    return self._send(200, {
                        "truncated": False,
                        "tree": [{"path": p, "type": "blob", "sha": "x"}
                                 for p in sorted(blobs)],
                    })
            if "/contents/" not in parts.path:
                return self._send(404, {"message": "not a contents route"})
            key = self.contents_path()
            with lock:
                record = blobs.get(key)
            if record is None:
                return self._send(404, {"message": "no such content"})
            return self._send(200, {
                "sha": record[1],
                "content": b64encode(record[0]).decode(),
            })

        def do_PUT(self):
            key = self.contents_path()
            payload = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            with lock:
                requests.append(("PUT", key))
                stored = blobs.get(key)
                mismatch = (stored is not None and payload.get("sha") != stored[1]) or \
                           (stored is not None and "sha" not in payload)
                if mismatch:
                    return self._send(409 if "sha" in payload else 422,
                                      {"message": "conflict"})
                new = b64decode(payload["content"])
                sha = "blob" + "0" * 36
                blobs[key] = (new, sha)
                visibility[key] = new
                commits[key] = payload
                return self._send(200, {"commit": {}, "content": {"sha": sha}})

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    server.daemon_threads = True
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield {
            "api": f"http://127.0.0.1:{server.server_port}",
            "pages": f"http://127.0.0.1:{server.server_port}",
            "blobs": blobs,
            "visibility": visibility,
            "commits": commits,
            "requests": requests,
            "lock": lock,
        }
    finally:
        server.shutdown()
        server.server_close()
        thread.join()


def make_store(target, **kwargs):
    return ghpages.GithubChannelStore(
        "example/nastech-agent",
        api_base=target["api"],
        public_base=target["pages"],
        token="fixture-token",
        **kwargs,
    )


class TestGithubChannelStore:
    def test_create_update_readback_and_visibility(self):
        with gh_store_server() as target:
            s = make_store(target, _sleep=lambda _s: None)
            s.put("releases/channels/main.json", b'{"name": "main"}')
            assert target["visibility"]["releases/channels/main.json"] == b'{"name": "main"}'
            body, etag = s.get("releases/channels/main.json")
            assert body == b'{"name": "main"}'
            assert etag == target["blobs"]["releases/channels/main.json"][1]

    def test_stale_cas_conflicts_and_lost_write_settles_by_bytes(self):
        with gh_store_server() as target:
            s = make_store(target, _sleep=lambda _s: None)
            from scripts.releases.channels import ChannelConflict
            s.put("releases/channels/stable.json", b"v1")
            _, etag = s.get("releases/channels/stable.json")
            s.put("releases/channels/stable.json", b"v2", etag)
            with pytest.raises(ChannelConflict):
                s.put("releases/channels/stable.json", b"v3", "stale-blob-sha")
            with pytest.raises(ChannelConflict):
                s.put("releases/channels/stable.json", b"v9")  # create-only over existing
            s.put("releases/channels/stable.json", b"v2", etag)  # committed bytes right back

    def test_keys_filters_the_control_plane_tree(self):
        with gh_store_server() as target:
            s = make_store(target, _sleep=lambda _s: None)
            s.put("releases/channels/main.json", b"a")
            s.put("releases/channels/stable.json", b"b")
            s.put("releases/termux/key.asc", b"c")
            assert s.keys("releases/channels/") == ["main.json", "stable.json"]
            assert s.keys("releases/missing/") == []

    def test_oversized_and_non_release_keys_are_refused_up_front(self):
        with gh_store_server() as target:
            s = make_store(target, _sleep=lambda _s: None)
            assert isinstance(s, ghpages.GithubChannelStore)
            from nastech_cli.release_channels import ChannelError
            with pytest.raises(ChannelError):
                s.put("releases/channels/big.json", b"x" * (ghpages.MAX_OBJECT_BYTES + 1))
            with pytest.raises(ChannelError):
                s.put("releases_not/evil.json", b"x")

    def test_visibility_tail_timeout_is_bounded(self, monkeypatch):
        # A Pages origin that never converges: a discard port refuses every
        # public read, so the bounded wait must raise, not spin.
        with gh_store_server() as target:
            monkeypatch.setenv("RELEASE_PAGES_VISIBLE_TAIL", "0")
            s = make_store(target, _sleep=lambda _s: None)
            s.public_base = "http://127.0.0.1:9"
            try:
                s.put("releases/channels/hidden.json", b"never-hosted")
                raise AssertionError("expected the Pages visibility timeout")
            except ghpages.ChannelError as exc:
                assert "Pages visibility timed out" in str(exc)


class TestStoreSelection:
    def test_store_selection_follows_the_environment(self, monkeypatch):
        import scripts.releases.ghpages as gh
        from scripts.releases import r2
        monkeypatch.delenv("R2_DISPOSABLE_RUN", raising=False)
        monkeypatch.delenv("RELEASE_CHANNEL_STORE", raising=False)
        monkeypatch.setattr(r2, "credentials", lambda: ({"access_key_id": "a", "secret_key": "b"}, "http://x", "bucket"))
        from scripts.releases.channels import R2ChannelStore
        assert isinstance(gh.configured_store("example/nastech-agent"), R2ChannelStore)
        monkeypatch.setenv("RELEASE_CHANNEL_STORE", "github")
        monkeypatch.setattr(gh.GithubChannelStore, "__init__", lambda self, repository, **kw: None)
        assert type(gh.configured_store("example/nastech-agent")).__name__ == "GithubChannelStore"

    def test_disposable_namespace_refused_in_github_mode(self, monkeypatch):
        monkeypatch.setenv("R2_DISPOSABLE_RUN", "41482566763")
        monkeypatch.setenv("GITHUB_REPOSITORY_ID", "12345")
        monkeypatch.setenv("RELEASE_CHANNEL_STORE", "github")
        from scripts.releases.ghpages import configured_store
        from nastech_cli.release_channels import ChannelError
        with pytest.raises(ChannelError):
            configured_store("example/nastech-agent")

    def test_r2_mode_still_selects_the_r2_store(self, monkeypatch):
        monkeypatch.setenv("RELEASE_CHANNEL_STORE", "r2")
        monkeypatch.delenv("R2_DISPOSABLE_RUN", raising=False)
        from scripts.releases.ghpages import configured_store
        from scripts.releases.channels import R2ChannelStore
        monkeypatch.setattr(
            "scripts.releases.r2.credentials",
            lambda: ({"access_key_id": "a", "secret_key": "b"}, "http://x", "bucket"),
        )
        assert isinstance(configured_store("example/nastech-agent"), R2ChannelStore)

    def test_channel_public_base_resolves_pages_in_github_mode(self, monkeypatch):
        monkeypatch.delenv("CLOUDFLARE_R2_PUBLIC_URL", raising=False)
        monkeypatch.delenv("R2_DISPOSABLE_RUN", raising=False)
        monkeypatch.setenv("RELEASE_CHANNEL_STORE", "github")
        monkeypatch.setenv("RELEASE_PAGES_PUBLIC_BASE", "https://nastechresearch.github.io/nastech-agent")
        from scripts.releases.r2_scope import channel_public_base
        assert channel_public_base() == "https://nastechresearch.github.io/nastech-agent"

    def test_channel_public_base_keeps_r2_default(self, monkeypatch):
        monkeypatch.delenv("R2_DISPOSABLE_RUN", raising=False)
        monkeypatch.delenv("RELEASE_CHANNEL_STORE", raising=False)
        monkeypatch.setenv("CLOUDFLARE_R2_PUBLIC_URL", "https://archive.example")
        from scripts.releases.r2_scope import channel_public_base
        assert channel_public_base() == "https://archive.example"



class TestReaderSeam:
    def test_reader_seam_points_at_pages(self):
        from nastech_cli import source_releases
        assert source_releases._PUBLIC_BASE == "https://nastechresearch.github.io/nastech-agent"
