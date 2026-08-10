"""
Nastech Desktop (Chat GUI) uninstaller.

The desktop GUI ships in two shapes and this module knows how to find and
remove the artifacts of both, on Linux, macOS, and Windows, WITHOUT touching
the Python agent or the user's config/data:

  1. Source-built GUI (``nastech desktop`` / ``nastech gui``)
     Built inside the agent checkout under ``$NASTECH_HOME/nastech-agent/``:
       - ``apps/desktop/dist``      (compiled renderer)
       - ``apps/desktop/release``   (electron-builder unpacked app + installers)
       - ``apps/desktop/node_modules`` and the workspace-root ``node_modules``
         (Electron itself, ~200MB) — only removed on a GUI uninstall because
         the agent does not need them.
       - ``$NASTECH_HOME/desktop-build-stamp.json`` (the build freshness stamp)

  2. Packaged distributable (DMG / NSIS / AppImage / deb / rpm)
     Installed by the OS to a standard application location and carrying its
     own bundled Electron + a per-user Electron ``userData`` directory:
       - macOS:   ``/Applications/Nastech.app`` or ``~/Applications/Nastech.app``
       - Windows: ``%LOCALAPPDATA%\\Programs\\Nastech`` (NSIS per-user)
       - Linux:   ``~/.local/share/applications`` .desktop entry + AppImage

In both shapes the Electron runtime keeps a ``userData`` directory keyed on
the app name ("Nastech"), separate from ``$NASTECH_HOME``:
  - macOS:   ``~/Library/Application Support/Nastech``
  - Windows: ``%APPDATA%\\Nastech``
  - Linux:   ``$XDG_CONFIG_HOME/Nastech`` (default ``~/.config/Nastech``)

This holds the desktop's own ``connection.json`` / ``updates.json`` and
Chromium cache — pure GUI state, safe to remove on a GUI uninstall.

The functions here are deliberately import-light and side-effect-free at
import time so the Electron main process can shell out to
``nastech uninstall --gui`` (and friends) without paying for the full CLI.
"""

import os
import shutil
import sys
from pathlib import Path

from nastech_constants import get_nastech_home

from nastech_cli.colors import Colors, color


def log_info(msg: str):
    print(f"{color('→', Colors.CYAN)} {msg}")


def log_success(msg: str):
    print(f"{color('✓', Colors.GREEN)} {msg}")


def log_warn(msg: str):
    print(f"{color('⚠', Colors.YELLOW)} {msg}")


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------


def _agent_root(nastech_home: Path) -> Path:
    """The agent checkout root — same layout install.sh / install.ps1 use."""
    return nastech_home / "nastech-agent"


def desktop_userdata_dir() -> Path:
    """Return the Electron ``userData`` directory for the desktop app.

    Mirrors Electron's ``app.getPath('userData')`` for an app named "Nastech"
    on each platform. This is GUI-only state (connection.json, updates.json,
    Chromium cache) and never holds agent config or sessions.
    """
    home = Path.home()
    if sys.platform == "darwin":
        return home / "Library" / "Application Support" / "Nastech"
    if sys.platform == "win32":
        appdata = os.environ.get("APPDATA")
        base = Path(appdata) if appdata else (home / "AppData" / "Roaming")
        return base / "Nastech"
    # Linux / other POSIX — XDG config home.
    xdg = os.environ.get("XDG_CONFIG_HOME")
    base = Path(xdg) if xdg else (home / ".config")
    return base / "Nastech"


def source_built_gui_artifacts(nastech_home: Path) -> "list[Path]":
    """GUI build artifacts produced by ``nastech desktop`` inside the checkout.

    These are removable on a GUI uninstall without harming the agent: the
    Python agent runs from ``nastech-agent/`` source + ``venv/`` and never
    needs the Electron build output or node_modules.
    """
    agent_root = _agent_root(nastech_home)
    desktop_dir = agent_root / "apps" / "desktop"
    return [
        desktop_dir / "dist",
        desktop_dir / "release",
        desktop_dir / "node_modules",
        # Workspace-root node_modules carries Electron (devDependency of the
        # desktop workspace, ~200MB). The agent does not use any npm package,
        # so this is GUI tooling — safe to drop on a GUI uninstall.
        agent_root / "node_modules",
        nastech_home / "desktop-build-stamp.json",
    ]


def packaged_gui_app_paths() -> "list[Path]":
    """Standard install locations of the packaged desktop distributable.

    Returns every candidate for the current OS; the caller filters to those
    that actually exist. We never glob system-wide — only the well-known
    electron-builder output locations for the "Nastech" product.
    """
    home = Path.home()
    paths: list[Path] = []
    if sys.platform == "darwin":
        paths += [
            Path("/Applications/Nastech.app"),
            home / "Applications" / "Nastech.app",
        ]
    elif sys.platform == "win32":
        local = os.environ.get("LOCALAPPDATA")
        local_base = Path(local) if local else (home / "AppData" / "Local")
        paths += [
            # NSIS per-user install (perMachine=false → Programs\Nastech).
            local_base / "Programs" / "Nastech",
            # Older / alternate layout some builds used.
            local_base / "nastech-desktop",
        ]
        program_files = os.environ.get("ProgramFiles")
        if program_files:
            # NSIS per-machine fallback (needs admin to remove).
            paths.append(Path(program_files) / "Nastech")
    else:
        # Linux: AppImage is a single file the user placed somewhere; we can
        # only reliably clean the desktop entry + icon we know the name of.
        # The AppImage itself lives wherever the user put it, so we surface a
        # hint rather than guessing. deb/rpm installs are owned by the system
        # package manager and must be removed via apt/dnf — see the message in
        # ``uninstall_gui``.
        from nastech_cli.linux_desktop_entry import desktop_entry_path

        data = os.environ.get("XDG_DATA_HOME")
        data_base = Path(data) if data else (home / ".local" / "share")
        paths += [
            # The launcher entry `nastech desktop` installs. Its icon lives
            # in the checkout, not in the installed app.
            desktop_entry_path(),
            # Some packaged builds emit this casing.
            data_base / "applications" / "Nastech.desktop",
        ]
    return paths


def agent_is_installed(nastech_home: Path) -> bool:
    """Return True when a usable Python agent install exists under NASTECH_HOME.

    Used by the desktop UI to decide which uninstall options to offer: if the
    agent isn't present (a future "lite" GUI-only client), the "remove agent"
    options are hidden.
    """
    agent_root = _agent_root(nastech_home)
    # A real install has the package source + a venv. Either signal alone is
    # enough — a source checkout without a venv is still "the agent is here".
    if (agent_root / "nastech_cli").is_dir():
        return True
    if (agent_root / "venv").is_dir() or (agent_root / ".venv").is_dir():
        return True
    return False


def gui_is_installed(nastech_home: Path) -> bool:
    """Return True when any desktop GUI artifact exists (built or packaged)."""
    for p in source_built_gui_artifacts(nastech_home):
        if p.exists():
            return True
    for p in packaged_gui_app_paths():
        if p.exists():
            return True
    if desktop_userdata_dir().exists():
        return True
    return False


def gui_install_summary(nastech_home: "Path | None" = None) -> dict:
    """Structured snapshot of what's installed, for the desktop UI to render.

    Returns JSON-serializable primitives so the Electron main process can
    forward it to the renderer via IPC (paths as strings, booleans for the
    high-level questions the UI gates options on).
    """
    home: Path = nastech_home if nastech_home is not None else get_nastech_home()

    source_artifacts = [p for p in source_built_gui_artifacts(home) if p.exists()]
    packaged = [p for p in packaged_gui_app_paths() if p.exists()]
    userdata = desktop_userdata_dir()

    return {
        "nastech_home": str(home),
        "agent_installed": agent_is_installed(home),
        "gui_installed": gui_is_installed(home),
        "source_built_artifacts": [str(p) for p in source_artifacts],
        "packaged_app_paths": [str(p) for p in packaged],
        "userdata_dir": str(userdata),
        "userdata_exists": userdata.exists(),
        "platform": sys.platform,
    }


# ---------------------------------------------------------------------------
# Removal
# ---------------------------------------------------------------------------


def _remove_path(path: Path) -> bool:
    """Remove a file or directory tree. Returns True when something was removed."""
    try:
        if path.is_symlink() or path.is_file():
            path.unlink()
            return True
        if path.is_dir():
            shutil.rmtree(path)
            return True
    except Exception as e:
        log_warn(f"Could not remove {path}: {e}")
    return False


def uninstall_gui(nastech_home: "Path | None" = None, *, remove_userdata: bool = True) -> "list[Path]":
    """Remove the desktop GUI's artifacts, leaving the agent + user data intact.

    Removes:
      - source-built GUI artifacts (dist/release/node_modules/build-stamp)
      - the packaged app bundle / install dir (best-effort; deb/rpm need the
        system package manager and are reported, not force-removed)
      - the Electron ``userData`` directory (unless ``remove_userdata=False``)

    Never touches ``nastech-agent/nastech_cli`` (agent source), ``venv/``, or any
    config / sessions / .env under ``$NASTECH_HOME``.

    Returns the list of paths actually removed.
    """
    home: Path = nastech_home if nastech_home is not None else get_nastech_home()

    removed: list[Path] = []

    log_info("Removing built GUI artifacts (renderer, release, node_modules)...")
    for path in source_built_gui_artifacts(home):
        if path.exists() and _remove_path(path):
            log_success(f"Removed {path}")
            removed.append(path)

    log_info("Removing installed desktop app...")
    found_packaged = False
    for path in packaged_gui_app_paths():
        if path.exists():
            found_packaged = True
            if _remove_path(path):
                log_success(f"Removed {path}")
                removed.append(path)
    if not found_packaged:
        log_info("No packaged desktop app found in standard locations")

    if remove_userdata:
        userdata = desktop_userdata_dir()
        if userdata.exists():
            log_info("Removing desktop app data (Electron userData)...")
            if _remove_path(userdata):
                log_success(f"Removed {userdata}")
                removed.append(userdata)

    if not removed:
        log_info("No desktop GUI artifacts found to remove")

    # Linux deb/rpm installs are owned by the package manager; we can't (and
    # shouldn't) rmtree files under /usr. Surface the hint so the user can
    # finish the job. AppImages live wherever the user dropped them.
    if sys.platform.startswith("linux"):
        # The desktop entry was removed above (it is in
        # ``packaged_gui_app_paths``), but the menu caches still list it.
        # Reindex so Nastech disappears from the launcher.
        try:
            from nastech_cli.linux_desktop_entry import (
                desktop_entry_path,
                refresh_desktop_databases,
            )

            entry = desktop_entry_path()
            if entry in removed:
                for tool in refresh_desktop_databases(entry.parent):
                    log_success(f"Refreshed the application menu cache ({tool})")
        except Exception as e:
            log_warn(f"Could not refresh the application menu cache: {e}")

        log_info(
            "If you installed the desktop via a .deb / .rpm package, remove it "
            "with your package manager (e.g. 'sudo apt remove nastech' or "
            "'sudo dnf remove nastech'). AppImage builds are a single file you "
            "can delete from wherever you saved it."
        )

    return removed
