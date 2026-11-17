"""Validate and conditionally publish macOS update feeds."""
from __future__ import annotations

import base64
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path
from typing import Any, Callable

from . import r2 as r2_module
from .semver import compare, is_release_version
from nastech_cli.update_channel import canary_timestamp, is_canary_tag

ARCHES = ("arm64",)  # Apple Silicon only: no Intel macOS build ships
_HASH_PATTERN = re.compile(r"^[A-Za-z0-9+/]{86}==$")


def _darwin_feed(channel: str, light: bool = False) -> dict[str, Any]:
    """Legacy URL shape only, not a channel existence registry."""
    if not isinstance(channel, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", channel):
        raise ValueError("Invalid legacy feed path component")
    return {"directory": f"releases/darwin/{'light/' if light else ''}{channel}",
            "channel": channel, "fileName": f"{channel}-mac.yml"}


# ---------------------------------------------------------------------------
# Feed parsing / merging (pure)
# ---------------------------------------------------------------------------

def parse_mac_feed(text: str) -> dict[str, Any]:
    import nastech_yaml as yaml  # lazy: YAML support loads only on the feed path

    feed = yaml.safe_load(text)
    if (
        not isinstance(feed, dict)
        or not is_release_version(str(feed.get("version", "")))
        or not isinstance(feed.get("files"), list)
        or not feed["files"]
    ):
        raise ValueError("Invalid macOS update feed")
    for file_entry in feed["files"]:
        if (
            not isinstance(file_entry, dict)
            or not isinstance(file_entry.get("url"), str)
            or not isinstance(file_entry.get("sha512"), str)
            or not _HASH_PATTERN.match(file_entry["sha512"])
            or not isinstance(file_entry.get("size"), int)
            or isinstance(file_entry.get("size"), bool)
            or file_entry["size"] <= 0
        ):
            raise ValueError("Invalid macOS artifact metadata")
    if feed.get("path") and not any(
        isinstance(f, dict)
        and f.get("url") == feed.get("path")
        and f.get("sha512") == feed.get("sha512")
        for f in feed["files"]
    ):
        raise ValueError("Legacy feed path/hash disagrees with files")
    return feed


_MAC_URL_PATTERN = re.compile(
    # Attempt refs (rc.N-vX.Y.Z) key the stable archive; plain and canary
    # vX.Y.Z[+canary...] tags key the rest.
    r"^/releases/tag/(?:v|rc\.[1-9]\d*-v)[0-9A-Za-z.+-]+/[0-9A-Za-z._+-]+\.(zip|dmg)$"
)


def mac_feed_references(text: str) -> list[str]:
    """Every bucket key a published feed references (artifact + .blockmap)."""
    feed = parse_mac_feed(text)
    references: list[str] = []
    for file_entry in feed["files"]:
        # Only our immutable artifact namespace is eligible for publication
        # or pruning; anything else fails loudly instead of half-publishing.
        if not _MAC_URL_PATTERN.match(file_entry["url"]):
            raise ValueError(f"Invalid macOS artifact path: {file_entry['url']}")
        key = file_entry["url"][1:]
        references.extend([key, f"{key}.blockmap"])
    return references


def merge_mac_feeds(legs: dict[str, str], tag: str, light: bool = False,
                    archive: str | None = None) -> dict[str, Any]:
    """Validate the native leg of every ARCHES entry, merge them, and rewrite
    artifact URLs into the immutable per-release tag namespace. `archive` keys
    that namespace (the attempt ref for stable attempts); `tag` stays the
    version identity."""
    import nastech_yaml as yaml  # lazy

    version = tag[1:] if isinstance(tag, str) and tag.startswith("v") else ""
    if not is_release_version(version):
        raise ValueError("Invalid macOS release tag")
    selection = _darwin_feed("canary" if is_canary_tag(tag) else "stable", light)
    expected = [f"{arch}-{selection['fileName']}" for arch in ARCHES]
    if sorted(legs.keys()) != sorted(expected):
        raise ValueError("Expected exactly one ARM64 macOS feed")
    files: dict[str, dict[str, Any]] = {}
    first: dict[str, Any] | None = None
    for index, name in enumerate(expected):
        leg = parse_mac_feed(legs[name])
        if str(leg.get("version")) != version:
            raise ValueError(f"Feed version does not match {tag}")
        prefix = f"{'NastechLight' if light else 'NastechBundled'}-{version}-mac-{ARCHES[index]}"
        if not any(f.get("url") == f"{prefix}.zip" for f in leg["files"]):
            raise ValueError(f"Missing native ZIP for {ARCHES[index]}")
        for file_entry in leg["files"]:
            if file_entry.get("url") not in (f"{prefix}.zip", f"{prefix}.dmg"):
                raise ValueError(f"Wrong variant or architecture: {file_entry.get('url')}")
            rewritten = {**file_entry, "url": f"/releases/tag/{archive or tag}/{file_entry['url']}"}
            prior = files.get(file_entry["url"])
            if prior is not None and prior != rewritten:
                raise ValueError(f"Conflicting artifact: {file_entry['url']}")
            files[file_entry["url"]] = rewritten
        if first is None:
            first = leg
    assert first is not None
    merged = {**first, "files": list(files.values())}
    if merged.get("path"):
        merged["path"] = f"/releases/tag/{archive or tag}/{merged['path']}"
    text = yaml.safe_dump(merged, width=100000, default_flow_style=False, sort_keys=False)
    mac_feed_references(text)  # publish only a feed that parses back clean
    return {
        "key": f"{selection['directory']}/{selection['fileName']}",
        "text": text,
        "files": merged["files"],
        "tag": tag,
        "version": version,
    }


# ---------------------------------------------------------------------------
# Publication (transport-verified)
# ---------------------------------------------------------------------------

def publish_mac_feed(
    plan: dict[str, Any],
    transport: dict[str, Callable[..., Any]],
) -> None:
    """The transport verifies immutable bytes and conditionally replaces one
    pointer. Downgrade rejection: semver.compare against the live feed."""
    read = transport["read"]
    verify = transport["verify"]
    write = transport["write"]
    live = read(plan["key"])
    if live:
        old_feed = parse_mac_feed(live["text"])
        next_feed = parse_mac_feed(plan["text"])
        old_url = str(old_feed["files"][0]["url"])
        old_tag = old_url.split("/releases/tag/", 1)[1].split("/", 1)[0]
        old_canary = canary_timestamp(old_tag)
        next_canary = canary_timestamp(plan.get("tag"))
        order = (
            (next_canary > old_canary) - (next_canary < old_canary)
            if next_canary is not None and old_canary is not None
            else compare(plan["version"], str(old_feed["version"]))
        )
        if order < 0:
            raise ValueError("Refusing to move the macOS feed backward")
        if order == 0:
            if old_feed != next_feed:
                raise ValueError("Refusing to replace published version with different artifacts")
            return
    for file_entry in plan["files"]:
        verify(file_entry["url"][1:], file_entry)
    write(plan["key"], plan["text"], live["etag"] if live else None)
    published = read(plan["key"])
    if not published or published["text"] != plan["text"]:
        raise ValueError("macOS feed readback differs from publication")


# ---------------------------------------------------------------------------
# finalize (the handoff store's transport)
# ---------------------------------------------------------------------------

def _feed_etag(text: str) -> str:
    """The GitHub arm's conditional-write token: a release asset has no ETag."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _handoff_digests(directory: str) -> dict[str, dict[str, Any]]:
    """The size and sha256 the fetched handoff receipts bind, keyed by object.

    The GitHub transport verifies an artifact against the receipt that names
    its bytes; where no receipt binds one, publication refuses rather than
    point a feed at unverified bytes."""
    from scripts.releases import handoff as handoff_module

    digests: dict[str, dict[str, Any]] = {}
    for name in sorted(os.listdir(directory)):
        if not (name.startswith("handoff-") and name.endswith(".json")):
            continue
        receipt = json.loads(Path(directory, name).read_text(encoding="utf-8-sig"))
        rows = handoff_module.validate_receipt(receipt, receipt.get("tag"),
                                               receipt.get("commit"), receipt.get("name"))
        prefix = r2_module.staging_key_for(str(receipt["tag"]), "")
        for row in rows:
            key = prefix + row["path"]
            prior = digests.get(key)
            if prior is not None and prior != row:
                raise ValueError(f"Handoff receipts disagree on {key}")
            digests[key] = row
    return digests


def finalize(tag: str, dir: str, variant: str | None = None, archive: str | None = None,
             verify_bytes: bool = True) -> None:
    """Validate the native legs, verify their streamed bytes, then replace
    the feed pointer (conditional write, then readback).

    The store is `handoff`'s, so a run without R2 credentials publishes the
    same pointer, under the same key, through the release-asset transport.

    ``verify_bytes=False`` (stable promotion of an accepted candidate, whose
    artifacts are already bound by receipt sha256) checks each artifact's
    remote size instead of streaming multi-GB packages back down; the GitHub
    arm takes that size off the release API's asset listing, the same size-
    only read the R2 arm gets from a HEAD."""
    if variant and variant != "light":
        raise ValueError("Unknown macOS variant")
    from scripts.releases.handoff import store

    transport = store()
    creds, base, bucket = transport.credentials()
    now = r2_module.amz_timestamp()

    legs = {
        name: open(os.path.join(dir, name), encoding="utf-8-sig").read()
        for name in sorted(os.listdir(dir))
        if name.endswith("-mac.yml")
    }
    plan = merge_mac_feeds(legs, tag, variant == "light", archive=archive)

    if transport is r2_module:

        def read(key: str) -> dict[str, str] | None:
            try:
                response = r2_module.signed_request(
                    "GET", f"{base}/{bucket}/{r2_module.encode_key_path(key)}", creds=creds, now=now
                )
            except r2_module.R2RequestError as err:
                if err.status == 404:
                    return None  # first publish: no live feed yet
                raise
            if response.status >= 400:
                raise r2_module.R2RequestError("GET", key, response.status)
            etag = response.header("etag")
            if not etag:
                raise ValueError(f"No ETag for {key}")
            return {"text": response.text(), "etag": etag}

        def verify(key: str, file_entry: dict[str, Any]) -> None:
            if not verify_bytes:
                head = r2_module.signed_request(
                    "HEAD", f"{base}/{bucket}/{r2_module.encode_key_path(key)}", creds=creds, now=now)
                if str(head.header("content-length")) != str(file_entry["size"]):
                    raise ValueError(f"Artifact size mismatch: {key}")
                return
            r2_module.verify_remote_artifact(
                f"{base}/{bucket}/{r2_module.encode_key_path(key)}",
                creds, now, file_entry["size"], file_entry["sha512"],
            )

        def write(key: str, text: str, etag: str | None) -> None:
            r2_module.put_object(
                creds, base, bucket, key, text.encode("utf-8"), now,
                "application/yaml",
                {"If-Match": etag} if etag else {"If-None-Match": "*"},
            )
    else:
        digests = _handoff_digests(dir)

        def read(key: str) -> dict[str, str] | None:
            text = transport.read_key(key)
            if text is None:
                return None  # first publish: no live feed yet
            return {"text": text, "etag": _feed_etag(text)}

        def verify(key: str, file_entry: dict[str, Any]) -> None:
            row = digests.get(key)
            if row is None:
                raise ValueError(f"No handoff receipt binds {key}")
            if row["size"] != file_entry["size"]:
                raise ValueError(f"Feed artifact size differs from its receipt: {key}")
            if not verify_bytes:
                # The receipt already binds these bytes' sha256, so the remote
                # size is the whole promotion check -- the same one the R2 arm
                # makes with a HEAD, taken off the asset listing without
                # streaming the package back down.
                if transport.object_size(key) != file_entry["size"]:
                    raise ValueError(f"Artifact size mismatch: {key}")
                return
            with tempfile.TemporaryDirectory() as staging:
                file = Path(staging) / os.path.basename(key)
                transport.download_object(creds, base, bucket, key, file, now,
                                          expected_size=row["size"],
                                          expected_sha256=row["sha256"])
                digest = hashlib.sha512()
                for chunk in r2_module.stream_file(str(file)):
                    digest.update(chunk)
                if base64.b64encode(digest.digest()).decode("ascii") != file_entry["sha512"]:
                    raise ValueError(f"Artifact checksum mismatch: {key}")

        def write(key: str, text: str, etag: str | None) -> None:
            current = transport.read_key(key)
            if etag != (None if current is None else _feed_etag(current)):
                raise r2_module.R2RequestError("PUT", key, 412)
            with tempfile.TemporaryDirectory() as staging:
                file = Path(staging) / os.path.basename(key)
                file.write_text(text, encoding="utf-8")
                transport.put(key=key, file=str(file), key_is_full=True)

    publish_mac_feed(plan, {"read": read, "verify": verify, "write": write})
    print(f"OK {'r2' if transport is r2_module else 'github'}: finalized {tag} -> {plan['key']}")
