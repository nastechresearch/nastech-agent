"""
Nastech Agent Uninstaller.

Provides options for:
- Full uninstall: Remove everything including configs and data
- Keep data: Remove code but keep ~/.nastech/ (configs, sessions, logs)
"""

import os
import shutil
import subprocess
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

def get_project_root() -> Path:
    """Get the project installation directory."""
    return Path(__file__).parent.parent.resolve()


def find_shell_configs() -> list:
    """Find shell configuration files that might have PATH entries."""
    home = Path.home()
    configs = []
    
    candidates = [
        home / ".bashrc",
        home / ".bash_profile",
        home / ".profile",
        home / ".zshrc",
        home / ".zprofile",
    ]
    
    for config in candidates:
        if config.exists():
            configs.append(config)
    
    return configs


def remove_path_from_shell_configs():
    """Remove Nastech PATH entries from shell configuration files."""
    configs = find_shell_configs()
    removed_from = []
    
    for config_path in configs:
        try:
            content = config_path.read_text(encoding="utf-8")
            original_content = content
            
            # Remove lines containing nastech-agent or nastech PATH entries
            new_lines = []
            skip_next = False
            
            for line in content.split('\n'):
                # Skip the "# Nastech Agent" comment and following line
                if '# Nastech Agent' in line or '# nastech-agent' in line:
                    skip_next = True
                    continue
                if skip_next and ('nastech' in line.lower() and 'PATH' in line):
                    skip_next = False
                    continue
                skip_next = False
                
                # Remove any PATH line containing nastech
                if 'nastech' in line.lower() and ('PATH=' in line or 'path=' in line.lower()):
                    continue
                    
                new_lines.append(line)
            
            new_content = '\n'.join(new_lines)
            
            # Clean up multiple blank lines
            while '\n\n\n' in new_content:
                new_content = new_content.replace('\n\n\n', '\n\n')
            
            if new_content != original_content:
                from utils import atomic_write_text

                # This is the user's own shell rc, not a Nastech-owned file, and
                # nothing in this function backs it up. A bare write_text()
                # truncates it before the new content lands, so a crash or
                # SIGINT mid-write leaves the user with an empty or truncated
                # ~/.zshrc -- and the enclosing `except Exception` downgrades
                # that to a warning, so the next login just starts a bare
                # shell. atomic_replace also resolves a symlinked rc file, so a
                # dotfiles-repo setup keeps the symlink instead of having it
                # replaced by a regular file. preserve_mode keeps the rc's
                # permission bits (normally 0644) and owner (sudo-run
                # uninstalls) instead of mkstemp's 0600/root.
                atomic_write_text(config_path, new_content, preserve_mode=True)
                removed_from.append(config_path)
                
        except Exception as e:
            log_warn(f"Could not update {config_path}: {e}")
    
    return removed_from


def remove_wrapper_script():
    """Remove the nastech wrapper script if it exists."""
    wrapper_paths = [
        Path.home() / ".local" / "bin" / "nastech",
        Path.home() / ".local" / "bin" / "nastech-acp",
        Path.home() / ".local" / "bin" / "nastech-agent",
        Path("/usr/local/bin/nastech"),
        Path("/usr/local/bin/nastech-acp"),
        Path("/usr/local/bin/nastech-agent"),
    ]
    
    removed = []
    for wrapper in wrapper_paths:
        if wrapper.exists():
            try:
                # Check if it's our wrapper (contains nastech_cli reference)
                content = wrapper.read_text(encoding="utf-8")
                if 'nastech_cli' in content or 'nastech-agent' in content:
                    wrapper.unlink()
                    removed.append(wrapper)
            except Exception as e:
                log_warn(f"Could not remove {wrapper}: {e}")
    
    return removed


def _node_symlink_candidate_dirs() -> "list[Path]":
    """Directories where the installer may have placed node/npm/npx symlinks."""
    dirs: list[Path] = [Path.home() / ".local" / "bin"]
    # Root FHS installs put links in /usr/local/bin.
    if sys.platform == "linux":
        dirs.append(Path("/usr/local/bin"))
    # Termux installs put links in $PREFIX/bin.
    prefix = os.environ.get("PREFIX", "")
    if prefix and "com.termux" in prefix:
        dirs.append(Path(prefix) / "bin")
    return dirs


def remove_node_symlinks(nastech_home: Path) -> list:
    """Remove the node/npm/npx symlinks the installer placed on PATH.

    The POSIX installer (``scripts/install.sh`` / ``scripts/lib/node-bootstrap.sh``)
    symlinks node/npm/npx into the same directory as the ``nastech`` command:

    - ``/usr/local/bin/`` on root FHS installs (Linux, uid 0)
    - ``$PREFIX/bin/`` on Termux
    - ``~/.local/bin/`` otherwise (the common non-root case)

    We check all candidate directories so that uninstall works regardless of
    how the install was done (e.g. a root FHS install that placed links in
    ``/usr/local/bin``, or an older install that used ``~/.local/bin`` before
    the FHS fix).  Only symlinks that resolve into this Nastech home's ``node``
    directory are removed — links the user has repointed elsewhere (nvm, fnm,
    etc.) are left untouched.
    """
    node_dir = (nastech_home / "node").resolve()
    removed = []

    for name in ("node", "npm", "npx"):
        for bin_dir in _node_symlink_candidate_dirs():
            link = bin_dir / name
            try:
                # Only act on symlinks — never delete a real binary the user put here.
                if not link.is_symlink():
                    continue

                # Resolve the link target and confirm it points into our node dir.
                # os.readlink + manual join handles broken (dangling) links too;
                # Path.resolve() on a dangling link still returns the target path.
                target = Path(os.readlink(link))
                if not target.is_absolute():
                    target = (link.parent / target)
                target = target.resolve()

                if target == node_dir or node_dir in target.parents:
                    link.unlink()
                    removed.append(link)
            except Exception as e:
                log_warn(f"Could not remove {link}: {e}")

    return removed


def uninstall_gateway_service():
    """Stop and uninstall the gateway service (systemd, launchd, Windows
    Scheduled Task / Startup folder) and kill any standalone gateway processes.

    Delegates to the gateway module which handles:
    - Linux: user + system systemd services (with proper DBUS env setup)
    - macOS: launchd plists
    - Windows: Scheduled Task + Startup-folder fallback, via ``gateway_windows``
    - All platforms: standalone ``nastech gateway run`` processes
    - Termux/Android: skips systemd (no systemd on Android), still kills standalone processes
    """
    import platform
    stopped_something = False

    # 1. Kill any standalone gateway processes (all platforms, including Termux)
    try:
        from nastech_cli.gateway import kill_gateway_processes, find_gateway_pids
        pids = find_gateway_pids()
        if pids:
            killed = kill_gateway_processes()
            if killed:
                log_success(f"Killed {killed} running gateway process(es)")
                stopped_something = True
    except Exception as e:
        log_warn(f"Could not check for gateway processes: {e}")

    system = platform.system()

    # Termux/Android has no systemd and no launchd — nothing left to do.
    prefix = os.getenv("PREFIX", "")
    is_termux = bool(os.getenv("TERMUX_VERSION") or "com.termux/files/usr" in prefix)
    if is_termux:
        return stopped_something

    # 2. Linux: uninstall systemd services (both user and system scopes)
    if system == "Linux":
        try:
            from nastech_cli.gateway import (
                get_systemd_unit_path,
                get_service_name,
                _systemctl_cmd,
            )
            svc_name = get_service_name()

            for is_system in (False, True):
                unit_path = get_systemd_unit_path(system=is_system)
                if not unit_path.exists():
                    continue

                scope = "system" if is_system else "user"
                try:
                    if is_system and os.geteuid() != 0:  # windows-footgun: ok — Linux systemd uninstall path, guarded by `if system == "Linux"` above
                        log_warn(f"System gateway service exists at {unit_path} "
                                 f"but needs sudo to remove")
                        continue

                    cmd = _systemctl_cmd(is_system)
                    subprocess.run(cmd + ["stop", svc_name],
                                   capture_output=True, check=False)
                    subprocess.run(cmd + ["disable", svc_name],
                                   capture_output=True, check=False)
                    unit_path.unlink()
                    subprocess.run(cmd + ["daemon-reload"],
                                   capture_output=True, check=False)
                    log_success(f"Removed {scope} gateway service ({unit_path})")
                    stopped_something = True
                except Exception as e:
                    log_warn(f"Could not remove {scope} gateway service: {e}")
        except Exception as e:
            log_warn(f"Could not check systemd gateway services: {e}")

    # 3. macOS: uninstall launchd plist
    elif system == "Darwin":
        try:
            from nastech_cli.gateway import get_launchd_plist_path
            plist_path = get_launchd_plist_path()
            if plist_path.exists():
                subprocess.run(["launchctl", "unload", str(plist_path)],
                               capture_output=True, check=False)
                plist_path.unlink()
                log_success(f"Removed macOS gateway service ({plist_path})")
                stopped_something = True
        except Exception as e:
            log_warn(f"Could not remove launchd gateway service: {e}")

    # 4. Windows: uninstall Scheduled Task + Startup-folder entry.  The
    #    gateway_windows module already knows how to locate and remove both
    #    code paths (schtasks /Delete + .cmd unlink) and how to stop any
    #    running detached pythonw gateway process.  We call into it so the
    #    uninstall logic stays in exactly one place.
    elif system == "Windows":
        try:
            from nastech_cli import gateway_windows
            if gateway_windows.is_installed() or gateway_windows.is_task_registered() \
                    or gateway_windows.is_startup_entry_installed():
                try:
                    gateway_windows.stop()
                except Exception as e:
                    log_warn(f"Could not stop Windows gateway cleanly: {e}")
                try:
                    gateway_windows.uninstall()
                    log_success("Removed Windows gateway (Scheduled Task + Startup entry)")
                    stopped_something = True
                except Exception as e:
                    log_warn(f"Could not fully uninstall Windows gateway: {e}")
        except Exception as e:
            log_warn(f"Could not check Windows gateway service: {e}")

    return stopped_something


# ============================================================================
# Windows-specific uninstall helpers
# ============================================================================
#
# The installer (``scripts/install.ps1``) does four Windows-only things that
# ``remove_path_from_shell_configs`` / ``remove_wrapper_script`` don't cover:
#
#   1. Sets User-scope env vars ``NASTECH_HOME`` and ``NASTECH_GIT_BASH_PATH``
#      via ``[Environment]::SetEnvironmentVariable(..., "User")``.  These
#      don't live in ~/.bashrc — they're in the Windows registry at
#      HKCU\Environment.
#   2. Prepends to User-scope ``PATH`` (same registry location) entries
#      like ``%LOCALAPPDATA%\nastech\git\cmd``, ``%LOCALAPPDATA%\nastech\git\bin``,
#      ``%LOCALAPPDATA%\nastech\git\usr\bin``, ``%LOCALAPPDATA%\nastech\node``.
#      Again not in any rc file — only accessible via the registry or the
#      .NET [Environment] API.
#   3. Downloads PortableGit to ``%LOCALAPPDATA%\nastech\git\`` and Node to
#      ``%LOCALAPPDATA%\nastech\node\`` as user-scoped, isolated copies.
#      These are ~200MB combined and serve no purpose after uninstall.
#   4. On the ``nastech dashboard`` + gateway paths, drops files into
#      ``%LOCALAPPDATA%\nastech\gateway-service\`` and sometimes
#      ``%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\`` — the
#      latter is handled by ``gateway_windows.uninstall()`` already.
#
# Running a PowerShell one-liner per operation is overkill and fragile on
# locked-down machines (Constrained Language Mode, restricted ExecutionPolicy).
# Direct registry writes via ``winreg`` work without spawning any subprocess
# and apply immediately for new shells (SendMessage WM_SETTINGCHANGE would
# be nicer but requires ctypes and buys us nothing — the user will log out
# or open a new terminal anyway).


def _nastech_path_markers(nastech_home: Path) -> list[str]:
    """Path-entry substrings that identify Nastech-owned User-PATH entries."""
    root = str(nastech_home).rstrip("\\/")
    # Match on prefix so sub-entries (git\cmd, git\bin, git\usr\bin, node, etc.)
    # all get swept.  Also match the bare nastech-agent install dir.
    markers = [root + "\\nastech-agent", root + "\\git", root + "\\node", root + "\\venv"]
    # Also match if NASTECH_HOME was customised to somewhere else — find-and-nuke
    # any entry whose path component contains "nastech".  We don't want to catch
    # unrelated entries like "chermes-foo" or "ephermeral", so we look for
    # backslash-nastech as a word-ish boundary.
    return markers


def remove_path_from_windows_registry(nastech_home: Path) -> list[str]:
    """Strip Nastech-owned entries from User-scope PATH in the registry.

    Returns the list of removed path entries.  Operates on HKCU\\Environment,
    same key the installer wrote to via ``[Environment]::SetEnvironmentVariable``.
    """
    try:
        import winreg
    except ImportError:
        return []  # not on Windows, nothing to do

    removed: list[str] = []
    key_path = "Environment"
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0,
                            winreg.KEY_READ | winreg.KEY_WRITE) as key:
            try:
                path_value, path_type = winreg.QueryValueEx(key, "Path")
            except FileNotFoundError:
                return []
            # Preserve REG_EXPAND_SZ vs REG_SZ so unexpanded %VARS% survive.
            entries = [e for e in path_value.split(";") if e]
            markers = _nastech_path_markers(nastech_home)
            kept: list[str] = []
            for entry in entries:
                entry_norm = entry.rstrip("\\/")
                matched = any(entry_norm.lower().startswith(m.lower()) for m in markers)
                if matched:
                    removed.append(entry)
                else:
                    kept.append(entry)
            if removed:
                new_value = ";".join(kept)
                winreg.SetValueEx(key, "Path", 0, path_type, new_value)
    except OSError as e:
        log_warn(f"Could not edit User PATH in registry: {e}")
    return removed


def remove_nastech_env_vars_windows() -> list[str]:
    """Delete NASTECH_HOME and NASTECH_GIT_BASH_PATH from User-scope env vars."""
    try:
        import winreg
    except ImportError:
        return []

    removed: list[str] = []
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0,
                            winreg.KEY_READ | winreg.KEY_WRITE) as key:
            for name in ("NASTECH_HOME", "NASTECH_GIT_BASH_PATH"):
                try:
                    winreg.QueryValueEx(key, name)
                except FileNotFoundError:
                    continue
                try:
                    winreg.DeleteValue(key, name)
                    removed.append(name)
                except OSError as e:
                    log_warn(f"Could not delete {name} from User env: {e}")
    except OSError as e:
        log_warn(f"Could not open User Environment key: {e}")
    return removed


def remove_portable_tooling_windows(nastech_home: Path) -> list[Path]:
    """Delete PortableGit and Node installs the Windows installer created under
    ``%LOCALAPPDATA%\\nastech\\``.  Only called on full uninstall; they're
    isolated from any system Git / Node so they cannot break other tools."""
    removed: list[Path] = []
    for sub in ("git", "node", "gateway-service"):
        target = nastech_home / sub
        if target.exists():
            try:
                shutil.rmtree(target, ignore_errors=False)
                removed.append(target)
            except Exception as e:
                log_warn(f"Could not remove {target}: {e}")
    return removed


def _is_windows() -> bool:
    import sys
    return sys.platform == "win32"


def _is_default_nastech_home(nastech_home: Path) -> bool:
    """Return True when ``nastech_home`` points at the default (non-profile) root."""
    try:
        from nastech_constants import get_default_nastech_root
        return nastech_home.resolve() == get_default_nastech_root().resolve()
    except Exception:
        return False


def _discover_named_profiles():
    """Return a list of ``ProfileInfo`` for every non-default profile, or ``[]``
    if profile support is unavailable or nothing is installed beyond the
    default root."""
    try:
        from nastech_cli.profiles import list_profiles
    except Exception:
        return []
    try:
        return [p for p in list_profiles() if not getattr(p, "is_default", False)]
    except Exception as e:
        log_warn(f"Could not enumerate profiles: {e}")
        return []


def _uninstall_profile(profile) -> None:
    """Fully uninstall a single named profile: stop its gateway service,
    remove its alias wrapper, and wipe its NASTECH_HOME directory.

    We shell out to ``nastech -p <name> gateway stop|uninstall`` because
    service names, unit paths, and plist paths are all derived from the
    current NASTECH_HOME and can't be easily switched in-process.
    """
    import sys as _sys
    name = profile.name
    profile_home = profile.path

    log_info(f"Uninstalling profile '{name}'...")

    # 1. Stop and remove this profile's gateway service.
    #    Use `python -m nastech_cli.main` so we don't depend on a `nastech`
    #    wrapper that may be half-removed mid-uninstall.
    nastech_invocation = [_sys.executable, "-m", "nastech_cli.main", "--profile", name]
    for subcmd in ("stop", "uninstall"):
        try:
            subprocess.run(
                nastech_invocation + ["gateway", subcmd],
                capture_output=True,
                text=True, encoding='utf-8', errors='replace',
                timeout=60,
                check=False,
            )
        except subprocess.TimeoutExpired:
            log_warn(f"  Gateway {subcmd} timed out for '{name}'")
        except Exception as e:
            log_warn(f"  Could not run gateway {subcmd} for '{name}': {e}")

    # 2. Remove the wrapper alias script at ~/.local/bin/<name> (if any).
    alias_path = getattr(profile, "alias_path", None)
    if alias_path and alias_path.exists():
        try:
            alias_path.unlink()
            log_success(f"  Removed alias {alias_path}")
        except Exception as e:
            log_warn(f"  Could not remove alias {alias_path}: {e}")

    # 3. Wipe the profile's NASTECH_HOME directory.
    try:
        if profile_home.exists():
            shutil.rmtree(profile_home)
            log_success(f"  Removed {profile_home}")
    except Exception as e:
        log_warn(f"  Could not remove {profile_home}: {e}")


def run_gui_uninstall(args):
    """GUI-only uninstall: remove the Chat GUI, leave the agent + data intact.

    Mirrors ``nastech uninstall --gui``. Removes the desktop app's built
    artifacts, the packaged app bundle (best-effort), and the Electron
    userData dir — nothing under ``$NASTECH_HOME`` config/sessions/.env, and
    never the Python agent or its venv.
    """
    from nastech_cli.gui_uninstall import (
        agent_is_installed,
        gui_install_summary,
        uninstall_gui,
    )

    nastech_home = get_nastech_home()
    summary = gui_install_summary(nastech_home)
    skip_confirm = bool(getattr(args, "yes", False))

    print()
    print(color("┌─────────────────────────────────────────────────────────┐", Colors.MAGENTA, Colors.BOLD))
    print(color("│         ⚕ Nastech Chat GUI Uninstaller                  │", Colors.MAGENTA, Colors.BOLD))
    print(color("└─────────────────────────────────────────────────────────┘", Colors.MAGENTA, Colors.BOLD))
    print()

    if not summary["gui_installed"]:
        print("No Nastech Chat GUI installation was found.")
        print(f"  Checked: {nastech_home}, and the standard app locations for this OS.")
        return

    print(color("This removes the Chat GUI only. The Nastech agent stays installed.", Colors.CYAN))
    print()
    print(color("Will remove:", Colors.YELLOW, Colors.BOLD))
    for p in summary["source_built_artifacts"]:
        print(f"  • {p}")
    for p in summary["packaged_app_paths"]:
        print(f"  • {p}")
    if summary["userdata_exists"]:
        print(f"  • {summary['userdata_dir']}  (desktop app data)")
    print()
    if agent_is_installed(nastech_home):
        print(color("Kept intact:", Colors.GREEN, Colors.BOLD))
        print(f"  • The Nastech agent at {nastech_home / 'nastech-agent'}")
        print(f"  • Your config, sessions, and secrets under {nastech_home}")
        print()

    if not skip_confirm:
        try:
            confirm = input(f"Type '{color('yes', Colors.YELLOW)}' to remove the Chat GUI: ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print()
            print("Cancelled.")
            return
        if confirm != "yes":
            print()
            print("Uninstall cancelled.")
            return

    print()
    print(color("Uninstalling Chat GUI...", Colors.CYAN, Colors.BOLD))
    print()
    uninstall_gui(nastech_home)

    print()
    print(color("┌─────────────────────────────────────────────────────────┐", Colors.GREEN, Colors.BOLD))
    print(color("│            ✓ Chat GUI Uninstalled!                      │", Colors.GREEN, Colors.BOLD))
    print(color("└─────────────────────────────────────────────────────────┘", Colors.GREEN, Colors.BOLD))
    print()
    print("The Nastech agent is still installed. Run 'nastech' to use the CLI,")
    print("or 'nastech uninstall' to remove the agent too.")
    print()


def run_uninstall(args):
    """
    Run the uninstall process.
    
    Options:
    - Full uninstall: removes code + ~/.nastech/ (configs, data, logs)
    - Keep data: removes code but keeps ~/.nastech/ for future reinstall
    """
    project_root = get_project_root()
    nastech_home = get_nastech_home()

    if bool(getattr(args, "dry_run", False)):
        _print_uninstall_dry_run(
            project_root=project_root,
            nastech_home=nastech_home,
            full_uninstall=bool(getattr(args, "full", False)),
        )
        return

    # Detect named profiles when uninstalling from the default root —
    # offer to clean them up too instead of leaving zombie NASTECH_HOMEs
    # and systemd units behind.
    is_default_profile = _is_default_nastech_home(nastech_home)
    named_profiles = _discover_named_profiles() if is_default_profile else []

    # Non-interactive fast path (``--yes``): no prompts. ``--full`` selects a
    # full wipe (code + ~/.nastech data); otherwise keep-data. Named profiles
    # are NOT auto-removed here — that's a destructive, surprising default for
    # an unattended run, so it stays opt-in to the interactive flow. This is
    # the path the desktop app's detached cleanup script uses for its
    # lite/full modes.
    skip_confirm = bool(getattr(args, "yes", False))
    if skip_confirm:
        full_uninstall = bool(getattr(args, "full", False))
        _perform_uninstall(
            project_root=project_root,
            nastech_home=nastech_home,
            full_uninstall=full_uninstall,
            remove_profiles=False,
            named_profiles=named_profiles,
        )
        return

    print()
    print(color("┌─────────────────────────────────────────────────────────┐", Colors.MAGENTA, Colors.BOLD))
    print(color("│            ⚕ Nastech Agent Uninstaller                  │", Colors.MAGENTA, Colors.BOLD))
    print(color("└─────────────────────────────────────────────────────────┘", Colors.MAGENTA, Colors.BOLD))
    print()
    
    # Show what will be affected
    print(color("Current Installation:", Colors.CYAN, Colors.BOLD))
    print(f"  Code:    {project_root}")
    print(f"  Config:  {nastech_home / 'config.yaml'}")
    print(f"  Secrets: {nastech_home / '.env'}")
    print(f"  Data:    {nastech_home / 'cron/'}, {nastech_home / 'sessions/'}, {nastech_home / 'logs/'}")
    print()

    if named_profiles:
        print(color("Other profiles detected:", Colors.CYAN, Colors.BOLD))
        for p in named_profiles:
            running = " (gateway running)" if getattr(p, "gateway_running", False) else ""
            print(f"  • {p.name}{running}: {p.path}")
        print()
    
    # Ask for confirmation
    print(color("Uninstall Options:", Colors.YELLOW, Colors.BOLD))
    print()
    print("  1) " + color("Keep data", Colors.GREEN) + " - Remove code only, keep configs/sessions/logs")
    print("     (Recommended - you can reinstall later with your settings intact)")
    print()
    print("  2) " + color("Full uninstall", Colors.RED) + " - Remove everything including all data")
    print("     (Warning: This deletes all configs, sessions, and logs permanently)")
    print()
    print("  3) " + color("Cancel", Colors.CYAN) + " - Don't uninstall")
    print()
    
    try:
        choice = input(color("Select option [1/2/3]: ", Colors.BOLD)).strip()
    except (KeyboardInterrupt, EOFError):
        print()
        print("Cancelled.")
        return
    
    if choice == "3" or choice.lower() in {"c", "cancel", "q", "quit", "n", "no"}:
        print()
        print("Uninstall cancelled.")
        return
    
    full_uninstall = (choice == "2")

    # When doing a full uninstall from the default profile, also offer to
    # remove any named profiles — stopping their gateway services, unlinking
    # their alias wrappers, and wiping their NASTECH_HOME dirs. Otherwise
    # those leave zombie services and data behind.
    remove_profiles = False
    if full_uninstall and named_profiles:
        print()
        print(color("Other profiles will NOT be removed by default.", Colors.YELLOW))
        print(f"Found {len(named_profiles)} named profile(s): " +
              ", ".join(p.name for p in named_profiles))
        print()
        try:
            resp = input(color(
                f"Also stop and remove these {len(named_profiles)} profile(s)? [y/N]: ",
                Colors.BOLD
            )).strip().lower()
        except (KeyboardInterrupt, EOFError):
            print()
            print("Cancelled.")
            return
        remove_profiles = resp in {"y", "yes"}

    # Final confirmation
    print()
    if full_uninstall:
        print(color("⚠️  WARNING: This will permanently delete ALL Nastech data!", Colors.RED, Colors.BOLD))
        print(color("   Including: configs, API keys, sessions, scheduled jobs, logs", Colors.RED))
        if remove_profiles:
            print(color(
                f"   Plus {len(named_profiles)} profile(s): " +
                ", ".join(p.name for p in named_profiles),
                Colors.RED
            ))
    else:
        print("This will remove the Nastech code but keep your configuration and data.")
    
    print()
    try:
        confirm = input(f"Type '{color('yes', Colors.YELLOW)}' to confirm: ").strip().lower()
    except (KeyboardInterrupt, EOFError):
        print()
        print("Cancelled.")
        return
    
    if confirm != "yes":
        print()
        print("Uninstall cancelled.")
        return

    _perform_uninstall(
        project_root=project_root,
        nastech_home=nastech_home,
        full_uninstall=full_uninstall,
        remove_profiles=remove_profiles,
        named_profiles=named_profiles,
    )


def _print_uninstall_dry_run(*, project_root: Path, nastech_home: Path, full_uninstall: bool) -> None:
    """Print the uninstall plan without stopping services or deleting files."""
    print()
    print(color("Dry run: no files, services, or environment entries will be changed.", Colors.CYAN, Colors.BOLD))
    print()
    print(color("Would inspect/remove:", Colors.YELLOW, Colors.BOLD))
    print("  • Gateway services and standalone gateway processes")
    print("  • Nastech PATH entries from shell configs / Windows User PATH")
    print("  • Nastech wrapper scripts and Nastech-managed node/npm/npx symlinks")
    print("  • Desktop Chat GUI artifacts")
    print(f"  • Code checkout: {project_root}")
    if full_uninstall:
        print(f"  • Nastech config/data: {nastech_home}")
        if _is_default_nastech_home(nastech_home):
            profiles = _discover_named_profiles()
            if profiles:
                print("  • Named profiles (interactive uninstall asks before removing):")
                for prof in profiles:
                    print(f"    - {prof.name}: {prof.path}")
    else:
        print(f"  • Keep Nastech config/data: {nastech_home}")
    print()


def _perform_uninstall(
    *,
    project_root: Path,
    nastech_home: Path,
    full_uninstall: bool,
    remove_profiles: bool,
    named_profiles: list,
) -> None:
    """Execute the uninstall steps. Shared by the interactive and ``--yes``
    paths so the destructive sequence lives in exactly one place.

    Steps: stop gateway → strip PATH (rc files + Windows registry) → remove the
    ``nastech`` wrapper + node symlinks → remove the desktop Chat GUI artifacts →
    delete the code checkout → (Windows) remove PortableGit/Node → optionally
    wipe ``$NASTECH_HOME`` data and named profiles on full uninstall.
    """
    print()
    print(color("Uninstalling...", Colors.CYAN, Colors.BOLD))
    print()
    
    # 1. Stop and uninstall gateway service + kill standalone processes
    log_info("Checking for running gateway...")
    if not uninstall_gateway_service():
        log_info("No gateway service or processes found")
    
    # 2. Remove PATH entries from shell configs (POSIX) AND from the Windows
    #    User-scope registry.  Both helpers no-op on the wrong platform so we
    #    can safely call them unconditionally.
    log_info("Removing PATH entries from shell configs...")
    removed_configs = remove_path_from_shell_configs()
    if removed_configs:
        for config in removed_configs:
            log_success(f"Updated {config}")
    else:
        log_info("No PATH entries found to remove in shell rc files")

    if _is_windows():
        log_info("Removing PATH entries from Windows User environment...")
        # Expand %LOCALAPPDATA% etc. in nastech_home so the marker matching is
        # against fully resolved paths — installer writes literal strings
        # like C:\Users\<u>\AppData\Local\nastech\git\cmd, not %LOCALAPPDATA%.
        removed_path_entries = remove_path_from_windows_registry(Path(os.path.expandvars(str(nastech_home))))
        if removed_path_entries:
            for entry in removed_path_entries:
                log_success(f"Removed from User PATH: {entry}")
        else:
            log_info("No Nastech-owned PATH entries in User environment")

        log_info("Removing NASTECH_HOME / NASTECH_GIT_BASH_PATH User env vars...")
        removed_env = remove_nastech_env_vars_windows()
        if removed_env:
            for name in removed_env:
                log_success(f"Removed User env var: {name}")
        else:
            log_info("No Nastech-set User env vars to remove")
    
    # 3. Remove wrapper script
    log_info("Removing nastech command...")
    removed_wrappers = remove_wrapper_script()
    if removed_wrappers:
        for wrapper in removed_wrappers:
            log_success(f"Removed {wrapper}")
    else:
        log_info("No wrapper script found")

    # 3b. Remove node/npm/npx symlinks the installer left in ~/.local/bin
    #     (only when they still point into this Nastech home's node dir, so we
    #     never clobber an existing nvm / user-managed Node).
    log_info("Removing Nastech-managed node/npm/npx symlinks...")
    removed_node_links = remove_node_symlinks(nastech_home)
    if removed_node_links:
        for link in removed_node_links:
            log_success(f"Removed {link}")
    else:
        log_info("No Nastech-managed node/npm/npx symlinks found")

    # 3c. Remove the desktop Chat GUI's artifacts too (built renderer/release,
    #     node_modules, the packaged app bundle, and the Electron userData
    #     dir). Both the "keep data" and "full" CLI flows remove the agent
    #     code, so the GUI — which is just another consumer of the same
    #     checkout — should go with it. uninstall_gui() never touches config /
    #     sessions / .env, so it's safe in keep-data mode; on full uninstall the
    #     step-5 rmtree(nastech_home) would sweep the in-tree artifacts anyway,
    #     but the packaged app + Electron userData live OUTSIDE NASTECH_HOME and
    #     must be cleaned explicitly here.
    log_info("Removing desktop Chat GUI artifacts...")
    try:
        from nastech_cli.gui_uninstall import uninstall_gui
        gui_removed = uninstall_gui(nastech_home)
        if not gui_removed:
            log_info("No desktop GUI artifacts found")
    except Exception as e:
        log_warn(f"Could not remove desktop GUI artifacts: {e}")

    # 4. Remove installation directory (code)
    log_info("Removing installation directory...")
    
    # Check if we're running from within the install dir
    # We need to be careful here
    try:
        if project_root.exists():
            # If the install is inside ~/.nastech/, just remove the nastech-agent subdir
            if nastech_home in project_root.parents or project_root.parent == nastech_home:
                shutil.rmtree(project_root)
                log_success(f"Removed {project_root}")
            else:
                # Installation is somewhere else entirely
                shutil.rmtree(project_root)
                log_success(f"Removed {project_root}")
    except Exception as e:
        log_warn(f"Could not fully remove {project_root}: {e}")
        log_info("You may need to manually remove it")

    # 4b. Remove Windows-only installer artifacts that are NOT user data:
    #     PortableGit, bundled Node, gateway-service dir.  Installer put them
    #     under NASTECH_HOME but they're install tooling, not config — safe to
    #     remove even in "keep data" mode.  If we're doing a full uninstall
    #     the step-5 rmtree(nastech_home) would sweep them anyway; calling
    #     this helper there is a no-op since they'll already be gone.
    if _is_windows():
        log_info("Removing Windows installer artifacts (PortableGit, Node, gateway-service)...")
        removed_artifacts = remove_portable_tooling_windows(nastech_home)
        if removed_artifacts:
            for path in removed_artifacts:
                log_success(f"Removed {path}")
        else:
            log_info("No Windows installer artifacts to remove")
    
    # 5. Optionally remove ~/.nastech/ data directory (and named profiles)
    if full_uninstall:
        # 5a. Stop and remove each named profile's gateway service and
        #     alias wrapper. The profile NASTECH_HOME dirs live under
        #     ``<default>/profiles/<name>/`` and will be swept away by the
        #     rmtree below, but services + alias scripts live OUTSIDE the
        #     default root and have to be cleaned up explicitly.
        if remove_profiles and named_profiles:
            for prof in named_profiles:
                _uninstall_profile(prof)

        log_info("Removing configuration and data...")
        try:
            if nastech_home.exists():
                shutil.rmtree(nastech_home)
                log_success(f"Removed {nastech_home}")
        except Exception as e:
            log_warn(f"Could not fully remove {nastech_home}: {e}")
            log_info("You may need to manually remove it")
    else:
        log_info(f"Keeping configuration and data in {nastech_home}")
    
    # Done
    print()
    print(color("┌─────────────────────────────────────────────────────────┐", Colors.GREEN, Colors.BOLD))
    print(color("│              ✓ Uninstall Complete!                      │", Colors.GREEN, Colors.BOLD))
    print(color("└─────────────────────────────────────────────────────────┘", Colors.GREEN, Colors.BOLD))
    print()
    
    if not full_uninstall:
        print(color("Your configuration and data have been preserved:", Colors.CYAN))
        print(f"  {nastech_home}/")
        print()
        print("To reinstall later with your existing settings:")
        if _is_windows():
            print(color("  iex (irm https://nastechresearch.github.io/nastech-agent/install.ps1)", Colors.DIM))
        else:
            print(color("  curl -fsSL https://nastechresearch.github.io/nastech-agent/install.sh | bash", Colors.DIM))
        print()

    if _is_windows():
        print(color("Open a new terminal (PowerShell / Windows Terminal) to pick up", Colors.YELLOW))
        print(color("the updated User PATH and environment variables.", Colors.YELLOW))
    else:
        print(color("Reload your shell to complete the process:", Colors.YELLOW))
        print("  source ~/.bashrc  # or ~/.zshrc")
    print()
    print("Thank you for using Nastech Agent! ⚕")
    print()


class _UninstallArgs:
    """Lightweight args namespace for the module entrypoint below."""

    def __init__(self, *, mode: str):
        self.gui = mode == "gui"
        self.gui_summary = False
        self.full = mode == "full"
        self.yes = True  # the module entrypoint is always non-interactive


def main(argv=None) -> int:
    """Module entrypoint: ``python -m nastech_cli.uninstall --mode <gui|lite|full>``.

    Exists so the desktop app can run the uninstall under a Python interpreter
    OUTSIDE the venv being deleted. On Windows, ``lite``/``full`` rmtree the
    venv that contains the running ``python.exe`` — and a running .exe is
    mandatory-locked, so doing that from the venv's own interpreter half-fails.
    The desktop launches this with the system Python + ``PYTHONPATH=<agentRoot>``
    so ``import nastech_cli`` resolves from source while the venv is torn down.

    This module imports only stdlib + ``nastech_constants`` + ``nastech_cli.colors``
    (and lazily ``nastech_cli.gui_uninstall``), so it runs fine under a bare
    system Python with no site-packages from the venv.
    """
    import argparse

    parser = argparse.ArgumentParser(prog="python -m nastech_cli.uninstall")
    parser.add_argument(
        "--mode",
        choices=["gui", "lite", "full"],
        required=True,
        help="gui = Chat GUI only; lite = GUI + agent, keep data; full = everything",
    )
    ns = parser.parse_args(argv)
    args = _UninstallArgs(mode=ns.mode)

    if args.gui:
        run_gui_uninstall(args)
    else:
        run_uninstall(args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
