"""Rewrite the launch files Nastech owns before ``nastech update`` starts any gateway.

A service manager starts a gateway from the definition it holds, so a unit, plist or task script
left from the previous release starts the new code under the old command line and environment.
The update therefore regenerates every profile's launch files once the inputs the generators read
are final (Python environment, published launchers, ``node_modules/.bin``) and before the first
gateway start or restart.

Only definitions this update owns are rewritten: a profile home outside the update's scope, or a
definition that launches another checkout (a worktree's update must not repoint the account's
live unit at the worktree), is left alone with a notice.

Each file is independent: a failure is reported as the ``launch_files`` follow-up and the rest
are still rewritten. A failure never keeps the source-update tail pending: every
``nastech gateway start``/``restart`` and every gateway boot regenerates its own file again.
"""

from __future__ import annotations

import os
import sys

FOLLOWUP_STEP = "launch_files"
_RETRY = "the next `nastech update` or `nastech gateway restart` rewrites it"


def refresh_launch_files() -> None:
    """Regenerate every profile's launch file that differs from what this checkout generates."""
    from nastech_cli.config_backend import ConfigBackendUnavailable
    from nastech_cli.update_fleet_scope import update_scope_homes
    from nastech_cli.update_receipt import _profile_homes, record_followup
    from nastech_constants import reset_nastech_home_override, set_nastech_home_override

    try:
        refreshers = _refreshers()
        scope = update_scope_homes() if refreshers else set()
        homes = [(p, h) for p, h in _profile_homes() if h.resolve() in scope] if refreshers else []
    except Exception as exc:  # health: allow BLE001 -- reported as a follow-up, never fails the update
        record_followup(FOLLOWUP_STEP, f"{type(exc).__name__}: {exc}", retry=_RETRY)
        return
    for profile, home in homes:
        for kind, refresh in refreshers:
            token = set_nastech_home_override(home)
            try:
                if _owned_by_this_checkout(kind):
                    refresh()
            except (Exception, ConfigBackendUnavailable) as exc:  # health: allow BLE001 -- one file never blocks the others
                record_followup(FOLLOWUP_STEP, f"{kind} for profile {profile}: {exc}", retry=_RETRY)
            finally:
                reset_nastech_home_override(token)
    if any(kind == "systemd user unit" for kind, _ in refreshers) and os.geteuid() == 0:  # windows-footgun: ok — systemd hosts only
        try:
            _refresh_systemd_system_unit()
        except (Exception, ConfigBackendUnavailable) as exc:  # health: allow BLE001 -- reported as a follow-up, never fails the update
            record_followup(FOLLOWUP_STEP, f"systemd system unit: {exc}", retry=_RETRY)


def _owned_by_this_checkout(kind: str) -> bool:
    """False (with the left-alone notice) when the active home's definition launches another checkout."""
    from nastech_cli import gateway
    from nastech_cli.update_fleet_scope import announce_skipped_runtime, definition_foreign_checkout

    paths = {"systemd user unit": lambda: gateway.get_systemd_unit_path(system=False),
             "systemd system unit": lambda: gateway.get_systemd_unit_path(system=True),
             "launchd plist": gateway.get_launchd_plist_path}
    if kind not in paths:
        return True
    path = paths[kind]()
    if (foreign := definition_foreign_checkout(path)) is None:
        return True
    announce_skipped_runtime(kind, path.name, None, checkout=foreign)
    return False


def _refresh_systemd_system_unit() -> None:
    """The invoking home's system unit; the refresh adopts the unit's ``NASTECH_HOME`` into the
    environment, which the rest of the update must not inherit."""
    from nastech_cli.gateway import refresh_systemd_unit_if_needed

    if not _owned_by_this_checkout("systemd system unit"):
        return
    launch_home = os.environ.get("NASTECH_HOME")
    try:
        refresh_systemd_unit_if_needed(system=True)
    finally:
        if launch_home is None:
            os.environ.pop("NASTECH_HOME", None)
        else:
            os.environ["NASTECH_HOME"] = launch_home


def _refreshers():
    if sys.platform == "win32":
        return [("Windows gateway launcher", _refresh_windows_launcher_scripts)]
    if sys.platform == "darwin":
        return [("launchd plist", _refresh_unloaded_launchd_plist)]
    from nastech_cli.gateway import supports_systemd_services

    if supports_systemd_services():
        return [("systemd user unit", _refresh_systemd_user_unit)]
    return []


def _refresh_systemd_user_unit() -> None:
    from nastech_cli.gateway import refresh_systemd_unit_if_needed

    refresh_systemd_unit_if_needed(system=False)  # rewrites only a stale unit, then daemon-reloads


def _refresh_unloaded_launchd_plist() -> None:
    from nastech_cli.gateway_launchd import refresh_unloaded_launchd_plist

    refresh_unloaded_launchd_plist()


def _refresh_windows_launcher_scripts() -> None:
    from nastech_cli import gateway_windows

    if gateway_windows.is_installed() and gateway_windows.launcher_script_drift():
        script = gateway_windows._write_task_script()
        print(f"  ↻ Updated the {script.stem} gateway launcher scripts")
