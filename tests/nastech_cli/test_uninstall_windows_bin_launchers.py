"""Uninstall must not leave a dangling ``nastech`` command on Windows.

Every uninstall mode deletes the code checkout, but the launchers install.ps1
staged in the managed binary dir (the default Nastech root's ``bin``, shared
with the managed uv) live outside it. A surviving launcher makes ``nastech``
in a new terminal resolve and then error on its missing venv target — worse
than command-not-found. The managed uv next to them must survive keep-data
uninstalls, so the PATH sweep takes the ``bin`` entry only on a full wipe.

Platform verdicts are injected parameters (input→output, not host fakes).
"""
from __future__ import annotations

from pathlib import Path

import pytest

from nastech_cli import uninstall
from nastech_cli._install_repair import _WINDOWS_BIN_LAUNCHERS


@pytest.fixture
def managed_bin(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Default-root ``bin`` holding launchers of both forms plus managed uv."""
    home = tmp_path / "nastech"
    bin_dir = home / "bin"
    bin_dir.mkdir(parents=True)
    (bin_dir / "nastech.exe").write_bytes(b"MZ launcher")
    (bin_dir / "nastech-acp.cmd").write_text("@echo off\r\n", encoding="ascii")
    (bin_dir / "uv.exe").write_bytes(b"MZ managed uv")
    (bin_dir / "uvx.exe").write_bytes(b"MZ managed uvx")
    monkeypatch.setenv("NASTECH_HOME", str(home))
    return bin_dir


def test_removes_both_launcher_forms_and_keeps_managed_uv(managed_bin: Path):
    removed = uninstall.remove_windows_bin_launchers(windows=True)

    assert sorted(p.name for p in removed) == ["nastech-acp.cmd", "nastech.exe"]
    assert not (managed_bin / "nastech.exe").exists()
    assert not (managed_bin / "nastech-acp.cmd").exists()
    # The managed uv stays — keep-data reinstalls still need it.
    assert (managed_bin / "uv.exe").exists()
    assert (managed_bin / "uvx.exe").exists()


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


def test_noop_when_no_launchers_staged(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    home = tmp_path / "nastech"
    home.mkdir()
    monkeypatch.setenv("NASTECH_HOME", str(home))

    assert uninstall.remove_windows_bin_launchers(windows=True) == []


def test_launcher_names_stay_in_lockstep_with_install_ps1():
    """The sweep must cover exactly the names install.ps1 stages, and no
    generic name it could clobber. Reads the real installer list so the two
    sides cannot drift apart silently."""
    import re

    install_ps1 = (
        Path(uninstall.__file__).resolve().parents[1] / "scripts" / "install.ps1"
    ).read_text(encoding="ascii")
    match = re.search(r"foreach \(\$launcher in @\(([^)]*)\)\)", install_ps1)
    assert match, "launcher staging loop not found in install.ps1"
    staged = set(re.findall(r'"([^"]+)"', match.group(1)))

    assert staged == set(_WINDOWS_BIN_LAUNCHERS)
    for name in _WINDOWS_BIN_LAUNCHERS:
        assert name.startswith("nastech")  # never a generic name it could clobber


class TestManagedBinPathMarker:
    """The managed ``bin`` PATH entry goes only when the dir itself goes.

    Markers match against Windows registry PATH entries, so the inputs here
    are Windows-shaped path strings regardless of the host — feeding
    ``tmp_path`` would make the test pass only on Windows hosts.
    """

    HOME = r"C:\Users\me\AppData\Local\nastech"
    BIN_ENTRY = r"C:\Users\me\AppData\Local\nastech\bin"

    def test_keep_data_markers_spare_the_managed_bin(self):
        markers = [m.lower() for m in uninstall._nastech_path_markers(Path(self.HOME))]

        assert not any(self.BIN_ENTRY.lower().startswith(m) for m in markers)

    def test_full_wipe_markers_take_the_managed_bin(self):
        markers = [
            m.lower()
            for m in uninstall._nastech_path_markers(
                Path(self.HOME), include_managed_bin=True
            )
        ]

        assert any(self.BIN_ENTRY.lower().startswith(m) for m in markers)
