"""The Termux apt repository is published to a release, in a safe order.

The R2 staging step failed on 2026-10-28 with
`404 ... nastech-agent_0.21.5~canary..._aarch64.deb` because the index could name
a file that was not there. Publishing to a fixed `termux-repo` tag keeps
`pkg install`/`pkg upgrade` working without R2, and the order below is what
makes that failure impossible rather than unlikely.
"""

import json
from pathlib import Path

import pytest

from scripts.termux import release_apt


class Result:
    def __init__(self, returncode=0, stdout="", stderr=""):
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr


def _repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    (repo / "pool" / "n").mkdir(parents=True)
    (repo / "pool" / "n" / "nastech-agent_0.22.0_aarch64.deb").write_bytes(b"new")
    (repo / "Packages").write_text("Package: nastech-agent\n", encoding="utf-8")
    (repo / "Packages.gz").write_bytes(b"gz")
    (repo / "Release").write_text("Origin: Nastech\n", encoding="utf-8")
    return repo


def test_staged_files_separates_packages_from_the_index(tmp_path):
    packages, index = release_apt.staged_files(_repo(tmp_path))
    assert [p.name for p in packages] == ["nastech-agent_0.22.0_aarch64.deb"]
    assert [p.name for p in index] == ["Packages", "Packages.gz", "Release"]

    empty = tmp_path / "empty"
    empty.mkdir()
    with pytest.raises(release_apt.AptReleaseError, match="no .deb"):
        release_apt.staged_files(empty)


def test_stale_packages_keeps_the_newest_and_the_fresh_upload():
    existing = [
        "nastech-agent_0.21.9_aarch64.deb",
        "nastech-agent_0.21.10_aarch64.deb",   # dpkg order: 0.21.10 > 0.21.9
        "nastech-agent_0.22.0_aarch64.deb",
        "Packages", "Packages.gz", "Release", "InRelease",
    ]
    uploaded = ["nastech-agent_0.22.1_aarch64.deb"]
    deleted = release_apt.stale_packages(existing, uploaded, keep=2)
    # keep the fresh upload plus the newest published version (0.22.0 by dpkg
    # order, not 0.21.9), so both older builds go
    assert sorted(deleted) == [
        "nastech-agent_0.21.10_aarch64.deb",
        "nastech-agent_0.21.9_aarch64.deb",
    ]
    # index assets are never deleted by the package sweep
    assert not any(name in ("Packages", "Release") for name in deleted)


def test_publish_uploads_packages_before_the_index_and_prunes_after(tmp_path):
    repo = _repo(tmp_path)
    calls = []

    def run(argv, **kwargs):
        calls.append(argv)
        if argv[:3] == ["gh", "release", "view"]:
            return Result(stdout=json.dumps({"assets": [
                {"name": "nastech-agent_0.21.8_aarch64.deb"},
                {"name": "nastech-agent_0.21.9_aarch64.deb"},
                {"name": "nastech-agent_0.22.0_aarch64.deb"},
                {"name": "Packages"}, {"name": "Release"},
            ]}))
        return Result()

    report = release_apt.publish(repo, "o/r", run=run)
    uploads = [c for c in calls if c[:3] == ["gh", "release", "upload"]]
    deletes = [c for c in calls if c[:3] == ["gh", "release", "delete-asset"]]

    order = [Path(c[4]).name for c in uploads]
    assert order == ["nastech-agent_0.22.0_aarch64.deb",
                     "Packages", "Packages.gz", "Release"]
    assert all(c[4].endswith(".deb") for c in uploads[:1])
    # keep the fresh 0.22.0 plus the newest published 0.21.9; 0.21.8 goes
    assert report["deleted_packages"] == ["nastech-agent_0.21.8_aarch64.deb"]
    assert all("--cleanup-tag" not in c for c in calls)
