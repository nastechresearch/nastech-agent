"""PR #69118: a named profile served by the default multiplexer reports as running.

``nastech gateway status`` / ``gateway list`` / ``profile list`` keyed liveness
off the profile's own gateway.pid, so a satellite profile served by the default
multiplexer showed "not running" even though the multiplexer was its live
inbound process. All three now consult the same
``named_profile_served_by_running_multiplexer()`` lookup the start guard and
cron liveness use.
"""

from __future__ import annotations

import io
import os
from contextlib import redirect_stdout
from types import SimpleNamespace


def _fake_multiplexer(monkeypatch, tmp_path, *, multiplex: bool):
    import nastech_constants
    import gateway.status as status

    (tmp_path / "profiles" / "beta").mkdir(parents=True)
    (tmp_path / "config.yaml").write_text(
        f"gateway:\n  multiplex_profiles: {'true' if multiplex else 'false'}\n"
    )
    (tmp_path / "gateway.pid").write_text(str(os.getpid()))
    monkeypatch.setenv("NASTECH_HOME", str(tmp_path / "profiles" / "beta"))
    monkeypatch.setattr(nastech_constants, "_default_nastech_root_memo", None)
    monkeypatch.setattr(status, "_pid_exists", lambda pid: True)


def _run_status():
    from nastech_cli import gateway as gw

    buf = io.StringIO()
    with redirect_stdout(buf):
        gw._gateway_command_inner(
            SimpleNamespace(gateway_command="status", deep=False, full=False, system=False)
        )
    return buf.getvalue().splitlines()[0]


def test_served_named_profile_reports_running(monkeypatch, tmp_path):
    from nastech_cli.profiles import list_profiles

    _fake_multiplexer(monkeypatch, tmp_path, multiplex=True)

    beta = next(p for p in list_profiles() if p.name == "beta")
    assert beta.gateway_running is True
    assert _run_status().startswith("✓ Gateway is running via the default-profile multiplexer")


def test_unserved_named_profile_still_reports_stopped(monkeypatch, tmp_path):
    from nastech_cli.profiles import list_profiles

    _fake_multiplexer(monkeypatch, tmp_path, multiplex=False)

    beta = next(p for p in list_profiles() if p.name == "beta")
    assert beta.gateway_running is False
    assert _run_status().startswith("✗ Gateway is not running")
