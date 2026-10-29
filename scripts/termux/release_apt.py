"""Publish the Termux APT repository as assets of one fixed-tag release.

`pkg` is apt, so it needs a stable *base* URL that it can append
``Release``/``Packages.gz`` and each stanza's ``Filename`` to.  A GitHub release
gives exactly that: ``<repo>/releases/download/<tag>/<asset>``, and apt follows
the redirect to GitHub's object store.

The tag is fixed (``termux-repo``) and its assets are therefore *replaced* on
every publish -- the one deliberate exception to release-asset immutability,
because a package manager cannot be pointed at a URL that changes per build.

Order is the whole design:

1. upload the new ``.deb`` first,
2. upload the regenerated index (``Packages``, ``Packages.gz``, ``Release``,
   ``InRelease``) last,
3. delete the packages beyond the current and previous version.

A client reading mid-publish therefore sees either the old complete index or
the new complete index, never one that names a file which is not there -- which
is exactly how the R2 staging failed on 2026-10-28:
``404 ... nastech-agent_0.21.5~canary..._aarch64.deb``.
"""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

from .stage_apt_repo import deb_version_key

REPO_TAG = "termux-repo"
INDEX_FILES = ("Packages", "Packages.gz", "Release", "InRelease")

# The repository's public signing key, published beside the index so a user can
# install it in one command.  Without it a signed repository is unusable: apt
# has nothing to verify `InRelease` against, and the only alternative is
# `[trusted=yes]`, which throws the signature away.
PUBLIC_KEY_NAME = "key.asc"
KEEP_PACKAGES = 2  # current + previous


class AptReleaseError(RuntimeError):
    """The staged repository cannot be published as it stands."""


def _gh(argv: list[str], run=subprocess.run) -> str:
    result = run(["gh", *argv], capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise AptReleaseError(f"gh {' '.join(argv)} failed: {result.stderr.strip()}")
    return result.stdout


def staged_files(repo_dir: Path) -> tuple[list[Path], list[Path]]:
    """The packages and the index files a publish must carry."""
    packages = sorted(p for p in repo_dir.rglob("*.deb") if p.is_file())
    index = [repo_dir / name for name in INDEX_FILES if (repo_dir / name).is_file()]
    key = repo_dir / PUBLIC_KEY_NAME
    if key.is_file():
        # Uploaded with the index, before the index itself: a client can fetch
        # the key it needs the moment the repository it names is visible.
        index.append(key)
    if not packages:
        raise AptReleaseError(f"no .deb staged under {repo_dir}")
    missing = [name for name in ("Packages", "Packages.gz") if not (repo_dir / name).is_file()]
    if missing:
        raise AptReleaseError(f"staged repository is missing {', '.join(missing)}")
    return packages, index


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


def publish(repo_dir: Path, repository: str, tag: str = REPO_TAG,
            run=subprocess.run) -> dict:
    """Replace the repository assets in the order that never dangles."""
    packages, index = staged_files(repo_dir)
    listing = json.loads(_gh(["release", "view", tag, "--repo", repository,
                              "--json", "assets"], run=run))
    existing = [asset["name"] for asset in listing.get("assets", [])]

    for package in packages:
        _gh(["release", "upload", tag, str(package), "--repo", repository,
             "--clobber"], run=run)
    # Index last: it may only become visible once every file it names exists.
    for path in index:
        _gh(["release", "upload", tag, str(path), "--repo", repository,
             "--clobber"], run=run)

    deleted = stale_packages(existing, [p.name for p in packages])
    for name in deleted:
        _gh(["release", "delete-asset", tag, name, "--repo", repository,
             "--yes"], run=run)
    return {"uploaded_packages": [p.name for p in packages],
            "uploaded_index": [p.name for p in index],
            "deleted_packages": deleted}
