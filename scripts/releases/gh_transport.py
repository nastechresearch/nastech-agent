"""Native-leg handoffs over GitHub releases instead of an R2 bucket.

`handoff` moves each leg's artifacts (packages, blockmaps, receipts, metadata)
between the build job and the publish job. It did that through the R2 bucket,
which is the last thing keeping Cloudflare in the release path: stage writes
`releases/tag/<tag>/<dir>/<file>`, fetch reads the same keys back.

GitHub releases carry the same thing with the same guarantees we actually use:
immutable per-tag assets, content addressed by sha256 in the receipts, and a
`gh` CLI that uploads and downloads without listing a bucket. So the transport
becomes one draft release per attempt tag, and the keys become asset names.

The receipt chain is untouched: receipts are files in the staged set, they are
uploaded and downloaded like any other, and every sha256 in them still has to
match the bytes.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

from scripts.releases import r2 as _r2  # key layout + receipt naming stay shared


class TransportError(RuntimeError):
    """A handoff could not be staged or fetched."""


def _gh(argv: list[str], run=subprocess.run) -> str:
    result = run(["gh", *argv], capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise TransportError(f"gh {' '.join(argv)} failed: {result.stderr.strip()}")
    return result.stdout


def asset_name(key: str) -> str:
    """The release asset name for a staging key.

    Keys carry `/`, which a release asset cannot, and a directory is part of
    the same leg's identity. Replacing the separator keeps `name`/`tag`
    distinguishable and stays reversible: `releases/tag/v1/darwin-arm64/x.zip`
    becomes `releases__tag__v1__darwin-arm64__x.zip`.
    """
    return key.replace("/", "__")


def staging_key(tag: str, directory: str, filename: str) -> str:
    return _r2.staging_key_for(tag, f"{directory}/{filename}" if directory else filename)


def _ensure_draft(tag: str, repository: str, run) -> None:
    try:
        _gh(["release", "view", tag, "--repo", repository], run=run)
    except TransportError:
        _gh(["release", "create", tag, "--repo", repository, "--draft",
             "--title", tag, "--notes", "Native-leg handoff staging (generated)."], run=run)


def stage(tag: str, repository: str, name: str, root: Path, includes: list[str],
          run=subprocess.run) -> dict:
    """Upload one leg's files to the attempt tag's draft release."""
    _ensure_draft(tag, repository, run)
    files = sorted({str(path) for pattern in includes for path in root.glob(pattern)
                    if path.is_file()})
    if not files:
        raise TransportError(f"no files matched {includes} under {root}")
    for start in range(0, len(files), 8):
        _gh(["release", "upload", tag, "--repo", repository, "--clobber",
             *files[start:start + 8]], run=run)
    return {"tag": tag, "name": name, "files": [Path(f).name for f in files]}


def fetch(tag: str, repository: str, legs: list[str], root: Path,
          includes: list[str], run=subprocess.run, public_base: str | None = None) -> list[Path]:
    """Download every staged file for ``legs`` at ``tag`` into ``root``."""
    root.mkdir(parents=True, exist_ok=True)
    downloaded: list[Path] = []
    for pattern in includes:
        for leg in legs:
            target = root / leg
            target.mkdir(parents=True, exist_ok=True)
            _gh(["release", "download", tag, "--repo", repository,
                 "--pattern", pattern, "--dir", str(target), "--clobber"], run=run)
            downloaded.extend(sorted(target.glob(pattern)))
    if not downloaded:
        raise TransportError(
            f"nothing was staged at {tag} for {', '.join(legs)} matching {includes}")
    return downloaded
