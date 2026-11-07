from __future__ import annotations

import os
import pstats
import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]


def _run(args: list[str], nastech_home: Path, **extra_env: str) -> subprocess.CompletedProcess:
    env = {k: v for k, v in os.environ.items() if not k.startswith(("NASTECH_", "TERMUX_"))}
    env.update({"NASTECH_HOME": str(nastech_home), "PYTHONPATH": str(REPO), **extra_env})
    return subprocess.run(
        [sys.executable, *args], cwd=REPO, env=env, capture_output=True, text=True, timeout=120, check=False)


def test_relative_cpu_profile_path_lands_in_the_profile_logs(tmp_path: Path):
    nastech_home = tmp_path / "home"
    nastech_home.mkdir()

    result = _run(["-m", "nastech_cli.main", "--cpu-profile", "run.prof", "completion", "bash"], nastech_home)

    assert result.returncode == 0, result.stderr[-1000:]
    target = nastech_home / "logs" / "profiles" / "run.prof"
    assert f"CPU profiling enabled: {target.resolve()}" in result.stderr
    assert pstats.Stats(str(target)).total_calls > 0
    assert "cumulative" in (target.parent / "run.prof.txt").read_text(encoding="utf-8")


def test_oneshot_hard_exit_still_writes_the_profile(tmp_path: Path):
    """``-z`` leaves through ``os._exit`` (atexit skipped); the profile must still be written."""
    nastech_home = tmp_path / "home"
    nastech_home.mkdir()
    target = tmp_path / "oneshot.prof"
    code = (
        "from nastech_cli.cpu_profile import enable_cpu_profile\n"
        f"enable_cpu_profile({str(target)!r})\n"
        "from nastech_cli.main import _exit_after_oneshot\n"
        "_exit_after_oneshot(0)\n"
    )

    result = _run(["-c", code], nastech_home)

    assert result.returncode == 0, result.stderr[-1000:]
    assert pstats.Stats(str(target)).total_calls > 0


def test_gateway_graceful_hard_exit_still_writes_the_profile(tmp_path: Path):
    """Every gateway exit funnels through ``os._exit`` (atexit skipped); the profile must still be written."""
    nastech_home = tmp_path / "home"
    nastech_home.mkdir()
    target = tmp_path / "gateway.prof"
    code = (
        "from nastech_cli.cpu_profile import enable_cpu_profile\n"
        f"enable_cpu_profile({str(target)!r})\n"
        "from gateway.run import _exit_after_graceful_shutdown\n"
        "_exit_after_graceful_shutdown(0)\n"
    )

    result = _run(["-c", code], nastech_home)

    assert result.returncode == 0, result.stderr[-1000:]
    assert pstats.Stats(str(target)).total_calls > 0


def test_version_writes_the_profile(tmp_path: Path):
    """``--version`` returns before agent startup; the parsed flag must still profile."""
    nastech_home = tmp_path / "home"
    nastech_home.mkdir()
    target = tmp_path / "version.prof"

    result = _run(["-m", "nastech_cli.main", "--cpu-profile", str(target), "--version"], nastech_home)

    assert result.returncode == 0, result.stderr[-1000:]
    assert pstats.Stats(str(target)).total_calls > 0


def test_termux_interactive_fast_launch_still_writes_the_profile(tmp_path: Path):
    """Termux's interactive fast path defers agent startup; ``--cpu-profile`` must still profile."""
    nastech_home = tmp_path / "home"
    nastech_home.mkdir()
    target = tmp_path / "termux.prof"
    code = (
        "import os, sys\n"
        "import nastech_cli.main as main\n"
        "main.cmd_chat = lambda args: None  # the interactive REPL needs a TTY\n"
        f"sys.argv = ['nastech', '--cpu-profile', {str(target)!r}]\n"
        "assert main._try_termux_fast_cli_launch()\n"
        "assert os.environ.get('NASTECH_DEFER_AGENT_STARTUP') == '1'  # lazy start kept\n"
    )

    result = _run(["-c", code], nastech_home, TERMUX_VERSION="0.118")

    assert result.returncode == 0, result.stderr[-1000:]
    assert pstats.Stats(str(target)).total_calls > 0


def test_in_place_relaunch_still_writes_the_profile(tmp_path: Path):
    """``relaunch`` replaces the process with ``exec`` on POSIX (atexit skipped); the profile must still be written."""
    nastech_home = tmp_path / "home"
    nastech_home.mkdir()
    target = tmp_path / "relaunch.prof"
    code = (
        "import sys\n"
        "from nastech_cli.cpu_profile import enable_cpu_profile\n"
        f"enable_cpu_profile({str(target)!r})\n"
        "import nastech_cli.relaunch as relaunch\n"
        "relaunch.build_relaunch_argv = lambda *a, **k: [sys.executable, '-c', 'pass']  # exec a no-op\n"
        "relaunch.relaunch(['--resume', 'x'])\n"
    )

    result = _run(["-c", code], nastech_home)

    assert result.returncode == 0, result.stderr[-1000:]
    assert pstats.Stats(str(target)).total_calls > 0


@pytest.mark.platforms("posix")  # Windows reroutes through Popen + wait, which atexit already covers
def test_named_profile_dashboard_reroute_still_writes_the_profile(tmp_path: Path):
    """A named profile's dashboard re-execs into the machine dashboard (atexit skipped); the profile must be written."""
    profile_home = tmp_path / ".nastech" / "profiles" / "work"
    profile_home.mkdir(parents=True)
    (profile_home / "config.yaml").write_text("model: {}\n", encoding="utf-8")
    target = tmp_path / "dashboard.prof"
    code = (
        "import argparse, os, sys\n"
        "from nastech_cli.cpu_profile import enable_cpu_profile\n"
        f"enable_cpu_profile({str(target)!r})\n"
        "import nastech_cli.main_dashboard as md\n"
        "real_exec = os.execvpe\n"
        "os.execvpe = lambda file, argv, env: real_exec(sys.executable, [sys.executable, '-c', 'pass'], env)\n"
        "args = argparse.Namespace(port=9119, host='127.0.0.1', no_open=True, isolated=False, open_profile='')\n"
        "md._route_named_profile_dashboard(args, False, None, None)\n"
        "sys.exit('the named profile was not rerouted')\n"
    )

    result = _run(["-c", code], profile_home, HOME=str(tmp_path))

    assert result.returncode == 0, result.stderr[-1000:]
    assert pstats.Stats(str(target)).total_calls > 0
