"""Tests for the unified profile→machine dashboard launch routing.

`<profile> dashboard` routes to ONE machine-level dashboard instead of
spawning a per-profile server: attach (open browser at ?profile=) when one
is already listening, else re-exec as the machine dashboard with the
launching profile preselected. `--isolated` opts out.
"""
import sys
import types
import pytest


@pytest.fixture
def main_mod():
    import nastech_cli.main as main_mod
    return main_mod


def _args(**kw):
    defaults = dict(
        status=False, stop=False, host="127.0.0.1", port=9119,
        no_open=True, insecure=False, skip_build=False,
        isolated=False, open_profile="",
    )
    defaults.update(kw)
    return types.SimpleNamespace(**defaults)


class TestUnifiedDashboardRouting:


    def test_profile_launch_reexecs_machine_dashboard(self, main_mod, monkeypatch):
        monkeypatch.delenv("NASTECH_HOME", raising=False)
        monkeypatch.setattr(
            "nastech_cli.profiles.get_active_profile_name", lambda: "worker_x"
        )
        monkeypatch.setattr(main_mod, "_dashboard_listening", lambda host, port: False)
        execs = []

        def fake_exec(exe, argv, env):
            execs.append((exe, argv, env))
            raise SystemExit(0)  # execvpe never returns

        monkeypatch.setattr(main_mod.os, "execvpe", fake_exec)

        with pytest.raises(SystemExit):
            main_mod.cmd_dashboard(_args())

        assert len(execs) == 1
        exe, argv, env = execs[0]
        assert exe == sys.executable
        # Pinned to the default profile + launching profile preselected.
        assert "-p" in argv and argv[argv.index("-p") + 1] == "default"
        assert "--open-profile" in argv
        assert argv[argv.index("--open-profile") + 1] == "worker_x"
        # The child is pinned to the machine ROOT, not the launching profile's
        # NASTECH_HOME.  For a standard install (NASTECH_HOME unset) that root is
        # the platform-native default (~/.nastech), NOT dropped — see the Docker
        # test below for why we resolve explicitly instead of popping.
        from nastech_constants import get_default_nastech_root
        assert env.get("NASTECH_HOME") == str(get_default_nastech_root())


    def test_desktop_profile_backend_skips_machine_dashboard_reroute(self, main_mod, monkeypatch):
        """A desktop-spawned named-profile backend (NASTECH_DESKTOP=1) must NOT
        reroute into the machine dashboard. The reroute re-execs as the default
        profile and exits, so the desktop never sees a ready backend → boot
        loop. The guard keeps desktop pool backends per-profile."""
        monkeypatch.setenv("NASTECH_DESKTOP", "1")
        monkeypatch.setattr(
            "nastech_cli.profiles.get_active_profile_name", lambda: "worker_x"
        )
        listening_calls = []
        monkeypatch.setattr(
            main_mod, "_dashboard_listening",
            lambda host, port: listening_calls.append(1) or False,
        )
        execs = []
        monkeypatch.setattr(main_mod.os, "execvpe", lambda *a, **k: execs.append(a))
        monkeypatch.setitem(sys.modules, "fastapi", None)

        with pytest.raises((SystemExit, AttributeError, ImportError, TypeError)):
            main_mod.cmd_dashboard(_args())
        assert listening_calls == []
        assert execs == []


class TestInteractiveDashboardAuthSetup:

    def test_loopback_proxy_public_url_offers_auth_setup(
        self, main_mod, monkeypatch, capsys
    ):
        """A TTY operator is prompted when public_url gates a loopback bind."""
        from nastech_cli.dashboard_auth import clear_providers

        monkeypatch.setenv(
            "NASTECH_DASHBOARD_PUBLIC_URL",
            "https://dashboard.example.test:9443",
        )
        clear_providers()
        monkeypatch.setattr(main_mod.sys.stdin, "isatty", lambda: True)
        monkeypatch.setattr(main_mod.sys.stdout, "isatty", lambda: True)
        monkeypatch.setattr("builtins.input", lambda _prompt: "3")

        with pytest.raises(SystemExit) as exc:
            main_mod._maybe_setup_dashboard_auth_interactively(_args())

        assert exc.value.code == 1
        output = capsys.readouterr().out
        assert "configured external dashboard.public_url" in output




