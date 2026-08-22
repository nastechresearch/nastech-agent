"""Tests for the Linux XDG desktop entry installed by ``nastech desktop``."""

from __future__ import annotations

import stat
from pathlib import Path

import pytest

from nastech_cli import linux_desktop_entry as lde


@pytest.fixture
def xdg_home(tmp_path, monkeypatch) -> Path:
    data_home = tmp_path / "xdg-data"
    monkeypatch.setenv("XDG_DATA_HOME", str(data_home))
    monkeypatch.setattr(lde.sys, "platform", "linux")
    return data_home


def _make_project(tmp_path: Path) -> Path:
    root = tmp_path / "nastech-agent"
    icon = root / "apps" / "desktop" / "assets" / "icon.png"
    icon.parent.mkdir(parents=True)
    icon.write_bytes(b"\x89PNG fake")
    return root


def _parse(entry_text: str) -> dict:
    values = {}
    for line in entry_text.splitlines():
        if "=" in line and not line.startswith("["):
            key, val = line.split("=", 1)
            values[key] = val
    return values


def test_install_writes_entry_with_absolute_exec_and_icon(tmp_path, xdg_home, monkeypatch):
    root = _make_project(tmp_path)
    nastech_bin = tmp_path / "bin" / "nastech"
    nastech_bin.parent.mkdir()
    nastech_bin.write_text("", encoding="utf-8")
    monkeypatch.setattr(
        "nastech_cli.relaunch.resolve_nastech_bin", lambda: str(nastech_bin)
    )
    monkeypatch.setattr(lde, "refresh_desktop_databases", lambda _dir: [])

    entry = lde.install_desktop_entry(root)

    assert entry == xdg_home / "applications" / "nastech.desktop"
    values = _parse(entry.read_text(encoding="utf-8"))

    # Exec must be the absolute path of the resolved binary. The launcher
    # runs with a minimal PATH, so a bare `nastech` would not resolve.
    assert values["Exec"] == f"{nastech_bin} desktop"
    assert Path(values["Exec"].split(" ")[0]).is_absolute()

    # Icon must be an absolute path to the real icon in the checkout.
    icon_path = Path(values["Icon"])
    assert icon_path.is_absolute()
    assert icon_path == lde.icon_path(root)
    assert icon_path.read_bytes() == b"\x89PNG fake"

    assert values["Type"] == "Application"
    assert values["Name"] == "Nastech"
    assert values["Terminal"] == "false"


def test_installed_entry_is_executable(tmp_path, xdg_home, monkeypatch):
    root = _make_project(tmp_path)
    monkeypatch.setattr("nastech_cli.relaunch.resolve_nastech_bin", lambda: "/usr/bin/nastech")
    monkeypatch.setattr(lde, "refresh_desktop_databases", lambda _dir: [])

    entry = lde.install_desktop_entry(root)

    assert entry.stat().st_mode & stat.S_IXUSR


def test_exec_falls_back_to_interpreter_module(tmp_path, xdg_home, monkeypatch):
    root = _make_project(tmp_path)
    monkeypatch.setattr("nastech_cli.relaunch.resolve_nastech_bin", lambda: None)
    monkeypatch.setattr(lde, "refresh_desktop_databases", lambda _dir: [])

    entry = lde.install_desktop_entry(root)
    exec_line = _parse(entry.read_text(encoding="utf-8"))["Exec"]

    assert exec_line.endswith("-m nastech_cli.main desktop")
    assert Path(exec_line.split(" ")[0]).is_absolute()


# #90292: the shell installer's bash wrapper makes argv[0] the repo `nastech`
# python script whose `#!/usr/bin/env python3` shebang resolves to the SYSTEM
# interpreter when the DE spawns the .desktop entry → ModuleNotFoundError,
# silent (Terminal=false). The Exec line must prefix sys.executable for any
# resolved bin that is a python script escaping the running venv.
def test_exec_prefixes_interpreter_for_env_shebang_python_script(tmp_path, xdg_home, monkeypatch):
    import sys

    root = _make_project(tmp_path)
    nastech_bin = tmp_path / "bin" / "nastech"
    nastech_bin.parent.mkdir()
    nastech_bin.write_text("#!/usr/bin/env python3\nimport nastech_cli\n", encoding="utf-8")
    nastech_bin.chmod(0o755)
    monkeypatch.setattr("nastech_cli.relaunch.resolve_nastech_bin", lambda: str(nastech_bin))
    monkeypatch.setattr(lde, "refresh_desktop_databases", lambda _dir: [])

    entry = lde.install_desktop_entry(root)
    exec_line = _parse(entry.read_text(encoding="utf-8"))["Exec"]

    interpreter = str(Path(sys.executable).resolve())
    assert exec_line.split(" ")[0].strip('"') == interpreter
    assert str(nastech_bin) in exec_line
    assert exec_line.endswith("desktop")


def test_exec_leaves_shell_wrapper_launchers_alone(tmp_path, xdg_home, monkeypatch):
    root = _make_project(tmp_path)
    nastech_bin = tmp_path / "bin" / "nastech"
    nastech_bin.parent.mkdir()
    nastech_bin.write_text('#!/bin/bash\nexec /opt/nastech/venv/bin/python "$@"\n', encoding="utf-8")
    nastech_bin.chmod(0o755)
    monkeypatch.setattr("nastech_cli.relaunch.resolve_nastech_bin", lambda: str(nastech_bin))
    monkeypatch.setattr(lde, "refresh_desktop_databases", lambda _dir: [])

    entry = lde.install_desktop_entry(root)
    exec_line = _parse(entry.read_text(encoding="utf-8"))["Exec"]

    # A bash wrapper execs the venv python itself — no interpreter prefix.
    assert exec_line == f"{nastech_bin} desktop"


def test_exec_leaves_venv_shebang_scripts_alone(tmp_path, xdg_home, monkeypatch):
    import sys

    root = _make_project(tmp_path)
    nastech_bin = tmp_path / "bin" / "nastech"
    nastech_bin.parent.mkdir()
    interpreter = str(Path(sys.executable).resolve())
    nastech_bin.write_text(f"#!{interpreter}\nimport nastech_cli\n", encoding="utf-8")
    nastech_bin.chmod(0o755)
    monkeypatch.setattr("nastech_cli.relaunch.resolve_nastech_bin", lambda: str(nastech_bin))
    monkeypatch.setattr(lde, "refresh_desktop_databases", lambda _dir: [])

    entry = lde.install_desktop_entry(root)
    exec_line = _parse(entry.read_text(encoding="utf-8"))["Exec"]

    # Console-script with the venv's own interpreter in the shebang: correct
    # as-is, prefixing would only add noise.
    assert exec_line == f"{nastech_bin} desktop"


def test_install_is_idempotent_and_skips_cache_refresh(tmp_path, xdg_home, monkeypatch):
    root = _make_project(tmp_path)
    monkeypatch.setattr("nastech_cli.relaunch.resolve_nastech_bin", lambda: "/usr/bin/nastech")
    calls: list[Path] = []
    monkeypatch.setattr(lde, "refresh_desktop_databases", lambda d: calls.append(d) or [])

    lde.install_desktop_entry(root)
    assert len(calls) == 1

    # Unchanged content → no rewrite, no menu-cache churn on every launch.
    lde.install_desktop_entry(root)
    assert len(calls) == 1


def test_install_without_source_icon_uses_themed_name(tmp_path, xdg_home, monkeypatch):
    root = tmp_path / "nastech-agent"
    root.mkdir()
    monkeypatch.setattr("nastech_cli.relaunch.resolve_nastech_bin", lambda: "/usr/bin/nastech")
    monkeypatch.setattr(lde, "refresh_desktop_databases", lambda _dir: [])

    entry = lde.install_desktop_entry(root)

    # A broken absolute path renders as no icon. The themed name resolves
    # when Nastech is installed some other way.
    assert _parse(entry.read_text(encoding="utf-8"))["Icon"] == "nastech"


@pytest.mark.macos_only
def test_install_is_a_noop_on_macos(tmp_path):
    """Faking darwin only renamed the host — the real macOS runner is the
    only place the `sys.platform` guard is exercised against a real host."""
    assert lde.install_desktop_entry(_make_project(tmp_path)) is None


@pytest.mark.windows_only
def test_install_is_a_noop_on_windows(tmp_path):
    """As above for Windows: a fake left POSIX paths and a POSIX XDG layout
    in place, so the no-op was never proven against a real one."""
    assert lde.install_desktop_entry(_make_project(tmp_path)) is None


# ---------------------------------------------------------------------------
# Cache refresh tool gating
# ---------------------------------------------------------------------------


def _stub_tools(monkeypatch, available: "set[str]") -> "list[list[str]]":
    ran: list[list[str]] = []
    monkeypatch.setattr(
        lde.shutil, "which", lambda name: f"/usr/bin/{name}" if name in available else None
    )
    monkeypatch.setattr(lde, "_run_quiet", lambda cmd: ran.append(cmd) or True)
    return ran


def test_refresh_runs_kbuildsycoca6_when_present(monkeypatch, tmp_path):
    ran = _stub_tools(monkeypatch, {"update-desktop-database", "kbuildsycoca6"})

    tools = lde.refresh_desktop_databases(tmp_path)

    assert tools == ["update-desktop-database", "kbuildsycoca6"]
    assert ran == [
        ["/usr/bin/update-desktop-database", str(tmp_path)],
        ["/usr/bin/kbuildsycoca6", "--noincremental"],
    ]


def test_refresh_falls_back_to_kbuildsycoca5(monkeypatch, tmp_path):
    ran = _stub_tools(monkeypatch, {"kbuildsycoca5"})

    tools = lde.refresh_desktop_databases(tmp_path)

    assert tools == ["kbuildsycoca5"]
    assert ran == [["/usr/bin/kbuildsycoca5", "--noincremental"]]


def test_refresh_prefers_kbuildsycoca6_over_5(monkeypatch, tmp_path):
    ran = _stub_tools(monkeypatch, {"kbuildsycoca6", "kbuildsycoca5"})

    lde.refresh_desktop_databases(tmp_path)

    assert [cmd[0] for cmd in ran] == ["/usr/bin/kbuildsycoca6"]


def test_refresh_skips_missing_tools(monkeypatch, tmp_path):
    ran = _stub_tools(monkeypatch, set())

    assert lde.refresh_desktop_databases(tmp_path) == []
    assert ran == []


def test_refresh_reports_only_tools_that_succeeded(monkeypatch, tmp_path):
    monkeypatch.setattr(lde.shutil, "which", lambda name: f"/usr/bin/{name}")
    # update-desktop-database fails (exit != 0). kbuildsycoca6 succeeds.
    monkeypatch.setattr(lde, "_run_quiet", lambda cmd: "kbuildsycoca" in cmd[0])

    assert lde.refresh_desktop_databases(tmp_path) == ["kbuildsycoca6"]


def test_run_quiet_swallows_missing_binary(tmp_path):
    assert lde._run_quiet([str(tmp_path / "definitely-not-a-binary")]) is False


def test_exec_arg_quoting_handles_spaces(tmp_path, xdg_home, monkeypatch):
    root = _make_project(tmp_path)
    spaced = tmp_path / "my apps" / "nastech"
    spaced.parent.mkdir()
    spaced.write_text("", encoding="utf-8")
    monkeypatch.setattr("nastech_cli.relaunch.resolve_nastech_bin", lambda: str(spaced))
    monkeypatch.setattr(lde, "refresh_desktop_databases", lambda _dir: [])

    entry = lde.install_desktop_entry(root)
    exec_line = _parse(entry.read_text(encoding="utf-8"))["Exec"]

    assert exec_line == f'"{spaced}" desktop'
