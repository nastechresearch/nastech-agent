"""Uninstall must not leave a dangling ``nastech`` command on Windows.

Every uninstall mode deletes the code checkout, but the launcher copies
staged onto PATH in the managed binary dir (the default Nastech root's
``bin``) live outside it. A surviving launcher makes ``nastech`` in a new
terminal resolve and then error on its missing venv target — worse than
command-not-found. The dir is wholly nastech-owned (pm keeps uv in its own
store entry), so the sweep takes everything in it.

Platform verdicts are injected parameters (input→output, not host fakes).
"""
from __future__ import annotations

from pathlib import Path

import pytest

from nastech_cli import uninstall


@pytest.fixture
def managed_bin(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Default-root ``bin`` holding staged launcher copies."""
    home = tmp_path / "nastech"
    bin_dir = home / "bin"
    bin_dir.mkdir(parents=True)
    (bin_dir / "nastech.exe").write_bytes(b"MZ launcher")
    (bin_dir / "nastech-acp.cmd").write_text("@echo off\r\n", encoding="ascii")
    monkeypatch.setenv("NASTECH_HOME", str(home))
    return bin_dir


def test_removes_the_whole_managed_bin_dir(managed_bin: Path):
    removed = uninstall.remove_windows_bin_launchers(windows=True)

    assert sorted(p.name for p in removed) == ["nastech-acp.cmd", "nastech.exe"]
    assert not managed_bin.exists()


def test_anchors_on_default_root_not_profile_home(
    managed_bin: Path, monkeypatch: pytest.MonkeyPatch
):
    """The launcher dir is per-machine; a profile NASTECH_HOME must not
    redirect the sweep into ``profiles/<name>/bin``."""
    home = managed_bin.parent
    monkeypatch.setenv("NASTECH_HOME", str(home / "profiles" / "work"))

    removed = uninstall.remove_windows_bin_launchers(windows=True)

    assert sorted(p.name for p in removed) == ["nastech-acp.cmd", "nastech.exe"]
    assert not (managed_bin / "nastech.exe").exists()


def test_noop_on_posix(managed_bin: Path):
    assert uninstall.remove_windows_bin_launchers(windows=False) == []
    assert (managed_bin / "nastech.exe").exists()


def test_noop_when_no_bin_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    home = tmp_path / "nastech"
    home.mkdir()
    monkeypatch.setenv("NASTECH_HOME", str(home))

    assert uninstall.remove_windows_bin_launchers(windows=True) == []
