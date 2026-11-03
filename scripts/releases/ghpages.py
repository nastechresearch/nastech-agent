"""GitHub-native control-plane store: the fork's release plane lives on Pages.

The mutable channel records, per-channel downloads pages, release-candidate
feeds, and termux APT indexes are committed to the repository (`releases/`
tree) through the GitHub Contents API; the Deploy Site workflow copies that
tree into the Pages artifact, so `https://nastechresearch.github.io/nastech-agent/releases/…`
speaks the exact `ChannelReader` protocol the workers.dev origin spoke.

CAS semantics: the Contents API conditions every write on the `sha` of the
stored blob, which is precisely the ETag If-Match / If-None-Match contract
`R2ChannelStore` expresses. The lost-write policy stands: success is settled
by exact readback bytes, never by optimistic retry.
"""
from __future__ import annotations

from base64 import b64decode, b64encode
import json
import os
import time
import urllib.error
import urllib.request

from nastech_cli.release_channels import (
    ChannelError, artifact_key, public_base as validate_public_base,
)

DEFAULT_PUBLIC_BASE = "https://nastechresearch.github.io/nastech-agent"
DEFAULT_BRANCH = "main"
# Channels gate on MAX_METADATA (4 MiB) and every other control-plane object is
# far smaller. Refusing oversized writes up front keeps the 100 MiB per-file
# Pages limit unreachable: heavy payloads belong on GitHub Releases assets.
MAX_OBJECT_BYTES = 4 * 1024 * 1024
# Pages artifact build + deploy latency is minutes, not milliseconds; the
# publisher public readback in ChannelPublisher must not fire before Pages
# serves the committed bytes. Bounded, env-tunable wait.
_VISIBILITY_TAIL = 900


def pages_public_base(explicit: str | None = None) -> str:
    """Public origin of the fork's release control plane."""
    if explicit is None:
        explicit = os.environ.get("RELEASE_PAGES_PUBLIC_BASE", DEFAULT_PUBLIC_BASE)
    return validate_public_base(explicit)


class GithubChannelStore:
    """Same get/put/keys surface as R2ChannelStore, backed by the repository."""

    def __init__(self, repository: str, *, branch: str | None = None,
                 api_base: str | None = None, public_base: str | None = None,
                 token: str | None = None, _sleep=time.sleep):
        self.repository = repository
        self.branch = branch or os.environ.get("RELEASE_CHANNEL_BRANCH", DEFAULT_BRANCH)
        self.api_base = (api_base or os.environ.get("RELEASE_GITHUB_API", "https://api.github.com")).rstrip("/")
        self.public_base = pages_public_base(public_base)
        self.token = token or os.environ.get("GITHUB_API_TOKEN") or os.environ.get("GITHUB_TOKEN") or ""
        self._sleep = _sleep

    # -- transport ----------------------------------------------------------

    def _api(self, path: str, *, method: str = "GET", payload: dict | None = None) -> tuple[int, dict]:
        url = f"{self.api_base}{path}"
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "nastech-release",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        data = None
        if payload is not None:
            data = json.dumps(payload).encode()
            headers["Content-Type"] = "application/json"
        request = urllib.request.Request(url, data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return response.status, json.loads(response.read().decode())
        except urllib.error.HTTPError as exc:
            return exc.code, {}

    # -- CAS surface --------------------------------------------------------

    def get(self, key: str) -> tuple[bytes, str] | None:
        key = artifact_key(key)
        status, record = self._api(
            f"/repos/{self.repository}/contents/{key}?ref={self.branch}")
        if status == 404:
            return None
        if status != 200:
            raise ChannelError(f"Control-plane read failed: HTTP {status} for {key}")
        body = b64decode(record["content"])
        if len(body) > MAX_OBJECT_BYTES:
            raise ChannelError(f"Control-plane object exceeds {MAX_OBJECT_BYTES} bytes: {key}")
        return body, record["sha"]

    def put(self, key: str, body: bytes, etag: str | None = None) -> None:
        key = artifact_key(key)
        if len(body) > MAX_OBJECT_BYTES:
            raise ChannelError(f"Control-plane object exceeds {MAX_OBJECT_BYTES} bytes: {key}")
        payload = {
            "message": f"releases: set {key}",
            "content": b64encode(body).decode(),
            "branch": self.branch,
        }
        if etag is not None:
            payload["sha"] = etag
        status, _record = self._api(
            f"/repos/{self.repository}/contents/{key}", method="PUT", payload=payload)
        if status in (409, 422):
            # No sha on PUT over an existing object is GitHub's create-only
            # miss; a stale sha is a plain CAS miss. Either way settle the true
            # outcome from stored bytes: a lost 2xx may already be committed.
            current = self.get(key)
            if current is not None and current[0] == body:
                self._wait_visible(key, body)
                from scripts.releases.upload_summary import note
                note(key)
                return
            from scripts.releases.channels import ChannelConflict
            raise ChannelConflict(f"Channel write conflict: {key}") from None
        if status not in (200, 201):
            raise ChannelError(f"Channel write outcome uncertain: {key}; HTTP {status}")
        current = self.get(key)
        if current is None or current[0] != body:
            raise ChannelError(f"Channel changed before authenticated readback: {key}")
        self._wait_visible(key, body)
        from scripts.releases.upload_summary import note
        note(key)

    def keys(self, prefix: str) -> list[str]:
        prefix = prefix.removesuffix("/")
        scope_len = len(prefix) + 1 if prefix else 0
        status, tree = self._api(f"/repos/{self.repository}/git/trees/{self.branch}?recursive=1")
        if status != 200:
            raise ChannelError(f"Control-plane listing failed: HTTP {status}")
        if tree.get("truncated"):
            raise ChannelError("Control-plane tree listing was truncated")
        keys = sorted(
            blob["path"][scope_len:] for blob in tree.get("tree", [])
            if blob.get("type") == "blob" and blob["path"].startswith(prefix + "/" if prefix else "")
        )
        return keys

    # -- public visibility convergence --------------------------------------

    def _wait_visible(self, key: str, body: bytes) -> None:
        """Absorb Pages deploy latency: poll the public origin for the bytes."""
        tail = int(os.environ.get("RELEASE_PAGES_VISIBLE_TAIL", _VISIBILITY_TAIL))
        url = f"{self.public_base}/{key}"
        deadline = time.monotonic() + tail
        while True:
            try:
                request = urllib.request.Request(url, headers={"User-Agent": "nastech-release"})
                with urllib.request.urlopen(request, timeout=30) as response:
                    if response.read() == body:
                        return
            except urllib.error.HTTPError:
                pass
            except urllib.error.URLError:
                pass
            if time.monotonic() >= deadline:
                raise ChannelError(f"Committed {key}; Pages visibility timed out")
            self._sleep(20)


def configured_store(repository: str, scope=None):
    """Store selection seam: the fork's release plane is GitHub-native."""
    from scripts.releases.r2_scope import R2Scope

    resolved = scope if scope is not None else R2Scope.configured(repository)
    if os.environ.get("RELEASE_CHANNEL_STORE", "r2") == "github":
        if resolved.prefix:
            # Disposable CI namespaces are Cloudflare R2-shaped isolation; a
            # repository tree cannot host them without publishing test state
            # into the control plane. Fail closed instead of rewriting keys.
            raise ChannelError(
                "Disposable channel namespaces require R2; unset R2_DISPOSABLE_RUN to use the GitHub store")
        return GithubChannelStore(repository)
    from scripts.releases.channels import R2ChannelStore
    from scripts.releases import r2
    return R2ChannelStore(*r2.credentials(), scope=resolved)
