"""Immutable release-file staging on GitHub Release assets instead of an R2 bucket.

`handoff` moves each leg's artifacts (packages, blockmaps, receipts, metadata)
between the build job and the publish job. This is the store it moves them
through: the same object-key language `scripts.releases.r2` defines
(`releases/tag/<tag>/…`, `releases/commit/<sha>/…`, disposable CI namespaces),
carried by release assets instead of bucket objects.

Keeping that key language is what makes the swap one import line in `handoff`:
keys stay validated, distinct per mode and reversible, and the receipt chain is
untouched -- a receipt is just another file in the staged set, and every sha256
in one still has to match the bytes it names.

Reads go to the authenticated asset endpoint, never a public download URL: a
draft release's assets 404 for the world, and staging is a draft.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import quote

from scripts.releases import r2 as _r2
from scripts.releases.r2 import (  # the pure half of the surface: key layout + validation
    R2RequestError,
    amz_timestamp,
    commit_key_for,
    commit_prefix_for,
    file_sha256,
    is_full_sha,
    relative_artifact_path,
    staging_key_for,
)

__all__ = [
    "STAGING_RELEASE",
    "R2RequestError",
    "amz_timestamp",
    "asset_name",
    "commit_key_for",
    "commit_prefix_for",
    "credentials",
    "download_object",
    "download_public_object",
    "fetch_key",
    "file_sha256",
    "get_object",
    "is_full_sha",
    "key_for_asset",
    "owns_origin",
    "prune",
    "public_base_url",
    "put",
    "read_key",
    "read_public_receipt",
    "relative_artifact_path",
    "release_tag_for",
    "repository_id",
    "staging_key_for",
]

# Keys that name no tag (commit builds, channel allocations, disposable CI runs)
# would otherwise need a git ref each, and refs must not grow with build volume.
# One draft release carries them all; the flattened key keeps them apart, and
# `prune()` is how a finished run leaves nothing behind.
STAGING_RELEASE = "nastech-handoff-staging"

_TAG_ROOT = "releases/tag/"

# The one subprocess surface, so a test can drive the store against a fake `gh`.
_run = subprocess.run


def repository_id() -> str:
    """The repository whose releases are this store, without needing a token.

    Naming the archive cannot require a credential: a public read decides *which*
    store an origin belongs to before any request is made.
    """
    repository = (os.environ.get("GITHUB_REPOSITORY")
                  or os.environ.get("NASTECH_RELEASE_REPOSITORY") or "")
    if not re.fullmatch(r"[^/\s]+/[^/\s]+", repository):
        raise ValueError("GitHub handoff staging requires GITHUB_REPOSITORY as <owner>/<repo>")
    return repository


def credentials() -> tuple[str, str, str]:
    """(token, repository, staging release) -- the store's identity.

    A missing token fails here rather than as an empty-credential error three
    layers down in an upload.
    """
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN") or ""
    if not token:
        raise ValueError("GitHub handoff staging requires GH_TOKEN or GITHUB_TOKEN")
    return token, repository_id(), STAGING_RELEASE


def asset_name(key: str) -> str:
    """The release asset name carrying an object key.

    An asset name cannot contain `/`, and the whole key is needed so two legs'
    same-named files stay distinct. `relative_artifact_path` rejects `%` in any
    artifact path, so encoding the separator as `%2F` is exactly reversible and
    no two distinct keys can share a name.
    """
    return key.replace("/", "%2F")


def key_for_asset(name: str) -> str:
    return name.replace("%2F", "/")


def release_tag_for(key: str) -> str:
    """Which release carries this key: the tag it names, or the shared staging one."""
    if key.startswith(_TAG_ROOT):
        tail = key[len(_TAG_ROOT):]
        if "/" in tail:
            return tail.split("/", 1)[0]
    return STAGING_RELEASE


def _scoped(key: str) -> tuple[str, str]:
    """(logical key, key inside its disposable CI namespace) for a store request."""
    scope = _r2.R2Scope.configured()
    logical = relative_artifact_path(key)
    return logical, scope.key(logical)


def _api(repository: str, route: str, *args: str) -> subprocess.CompletedProcess:
    return _run(["gh", "api", f"repos/{repository}/{route}", *args],
                capture_output=True, text=True, check=False)


def _fail(method: str, target: str, result: subprocess.CompletedProcess) -> None:
    status = 404 if "Not Found" in (result.stderr or "") else 500
    raise R2RequestError(method, target, status, (result.stderr or "").strip()[:400])


def _release_id(repository: str, tag: str) -> int:
    found = _api(repository, f"releases/tags/{tag}")
    if found.returncode == 0:
        return int(json.loads(found.stdout)["id"])
    created = _api(repository, "releases", "-X", "POST",
                   "-f", f"tag_name={tag}",
                   "-f", f"target_commitish={os.environ.get('GITHUB_SHA', 'main')}",
                   "-f", "title=Release handoff staging",
                   "-f", "body=Native-leg handoff staging (generated).",
                   "-F", "draft=true")
    if created.returncode != 0:
        _fail("POST", f"releases(tags/{tag})", created)
    return int(json.loads(created.stdout)["id"])


def _assets(repository: str, release_id: int) -> list[dict]:
    rows: list[dict] = []
    page = 1
    while True:
        found = _api(repository, f"releases/{release_id}/assets",
                     "-f", "per_page=100", "-f", f"page={page}")
        if found.returncode != 0:
            _fail("GET", f"releases/{release_id}/assets", found)
        batch = json.loads(found.stdout)
        rows.extend(batch)
        if len(batch) < 100:
            return rows
        page += 1


def _find(repository: str, release_id: int, name: str) -> dict | None:
    return next((row for row in _assets(repository, release_id) if row.get("name") == name), None)


def _write_asset(repository: str, asset_id: int, file: Path) -> None:
    with open(file, "wb") as handle:
        result = _run(
            ["gh", "api", f"repos/{repository}/releases/assets/{asset_id}",
             "-H", "Accept: application/octet-stream"],
            stdout=handle, stderr=subprocess.PIPE, check=False)
    if result.returncode != 0:
        _fail("GET", str(asset_id), result)


def _read_asset(repository: str, asset: dict) -> tuple[int, str]:
    """(size, sha256) of the bytes the API already holds for this asset."""
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "asset"
        _write_asset(repository, asset["id"], path)
        return path.stat().st_size, file_sha256(str(path))


def put(tag: str = "", key: str = "", file: str = "", key_is_full: bool = False,
        immutable: bool = False) -> None:
    """Stage one object, keeping the write-once rule a draft release does not give.

    R2 enforced it with `If-None-Match: *`. A release asset can be replaced
    silently, so an immutable write compares the existing bytes first: identical
    bytes make a retry idempotent, differing bytes are refused. Only a
    non-immutable write replaces, exactly as an unconditional R2 `PUT` did.
    """
    _token, repository, _staging = credentials()
    full = key if key_is_full else staging_key_for(tag, key)
    logical, scoped = _scoped(full)
    name = asset_name(scoped)
    release_id = _release_id(repository, release_tag_for(logical))
    existing = _find(repository, release_id, name)
    if existing is not None:
        if immutable:
            if _read_asset(repository, existing) == (os.path.getsize(file), file_sha256(file)):
                print(f"OK github: {name} (already staged)")
                return
            raise R2RequestError("PUT", name, 412, "staged bytes differ from the existing asset")
        deleted = _api(repository, f"releases/assets/{existing['id']}", "-X", "DELETE")
        if deleted.returncode != 0:
            _fail("DELETE", name, deleted)
    uploaded = _api(repository, f"releases/{release_id}/assets?name={quote(name, safe='')}",
                    "-X", "POST", "-H", "Content-Type: application/octet-stream",
                    "--input", str(file))
    if uploaded.returncode != 0:
        _fail("POST", name, uploaded)
    remote = json.loads(uploaded.stdout)
    size = os.path.getsize(file)
    if remote.get("size") != size:
        raise R2RequestError("HEAD", name, 500, f"size mismatch (remote {remote.get('size')}, local {size})")
    from scripts.releases.upload_summary import note

    note(name)
    print(f"OK github: {name} ({size} bytes)")


def _locate(key: str) -> tuple[str, dict]:
    """(repository, asset) for an object key, or a 404 request error."""
    _token, repository, _staging = credentials()
    logical, scoped = _scoped(key)
    release_id = _release_id(repository, release_tag_for(logical))
    asset = _find(repository, release_id, asset_name(scoped))
    if asset is None:
        raise R2RequestError("GET", key, 404)
    return repository, asset


def read_key(key: str) -> str | None:
    """The object's body, or None when nothing is staged under that key."""
    try:
        repository, asset = _locate(key)
    except R2RequestError as err:
        if err.status == 404:
            return None
        raise
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "object"
        _write_asset(repository, asset["id"], path)
        return path.read_text(encoding="utf-8-sig")


def get_object(creds: str, base: str, bucket: str, key: str, now: str = "") -> str | None:
    """`r2.get_object`'s surface.

    The credential slots are accepted and ignored: this store's identity is one
    repository plus the runner's token, both resolved inside, so a caller moved
    over from R2 keeps its call shape.
    """
    return read_key(key)


def public_base_url(explicit: str | None = None) -> str:
    """The only origin a staged receipt may be read from: this repo's releases."""
    origin = f"https://github.com/{repository_id()}/releases/download"
    if explicit is not None and explicit.rstrip("/") != origin:
        raise ValueError(f"Handoff base {explicit!r} is not this repository's release archive")
    return origin


def owns_origin(base: str) -> bool:
    """Whether an archive origin names this store, so a public read can route here."""
    try:
        origin = public_base_url()
    except ValueError:
        return False
    return base.rstrip("/") == origin


def read_public_receipt(base: str, key: str) -> dict:
    public_base_url(base)
    return json.loads(read_key(key) or "")


def fetch_key(key: str, file: Path, *, expected_size: int, expected_sha256: str) -> None:
    """Download the bytes a receipt names, and refuse to keep them if they disagree.

    A leg package is ~1.5 GB, so a truncated transfer looks exactly like a wrong
    digest: the bytes land in a side file, are checked, and only then renamed
    into place. Retries are bounded, and a digest that never matches is a
    failure rather than an infinite refetch.
    """
    repository, asset = _locate(key)
    file.parent.mkdir(parents=True, exist_ok=True)
    staging = file.with_name(file.name + ".part")
    mismatch = None
    for _attempt in range(3):
        _write_asset(repository, asset["id"], staging)
        if staging.stat().st_size != expected_size:
            mismatch = f"Artifact size mismatch: {key}"
            continue
        if file_sha256(str(staging)) != expected_sha256:
            mismatch = f"Artifact checksum mismatch: {key}"
            continue
        staging.replace(file)
        return
    staging.unlink(missing_ok=True)
    raise ValueError(mismatch)


def download_object(creds: str, base: str, bucket: str, key: str, file: Path, now: str = "",
                    *, expected_size: int, expected_sha256: str) -> None:
    fetch_key(key, file, expected_size=expected_size, expected_sha256=expected_sha256)


def download_public_object(base: str, key: str, file: Path, *, expected_size: int,
                           expected_sha256: str) -> None:
    public_base_url(base)
    fetch_key(key, file, expected_size=expected_size, expected_sha256=expected_sha256)


def prune(key_prefix: str) -> list[str]:
    """Delete every asset staged under one namespace (a finished run's leftovers)."""
    _token, repository, _staging = credentials()
    # A namespace is a prefix, so it ends in the separator the validator reads as
    # an empty path component; validate the path and put the scope back.
    logical, scoped = _scoped(key_prefix.rstrip("/"))
    if key_prefix.endswith("/"):
        scoped += "/"
    name = asset_name(scoped)
    release_id = _release_id(repository, release_tag_for(logical))
    doomed = [row for row in _assets(repository, release_id) if str(row.get("name", "")).startswith(name)]
    for row in doomed:
        deleted = _api(repository, f"releases/assets/{row['id']}", "-X", "DELETE")
        if deleted.returncode != 0:
            _fail("DELETE", row["name"], deleted)
    return [key_for_asset(row["name"]) for row in doomed]
