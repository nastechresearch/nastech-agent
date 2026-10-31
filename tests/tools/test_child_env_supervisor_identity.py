"""A supervisor's identity describes only the process it started, never that process's children.

The launchd wrapper forwards ``NASTECH_LAUNCHD_LABEL`` to the gateway it starts (#120087), and
``gateway run --external-supervisor`` stamps ``NASTECH_GATEWAY_EXTERNAL_SUPERVISOR`` into its own
environ. A gateway an agent starts from its terminal tool is owned by no supervisor, so it must not
answer ``launchd``/supervised and take the exit-75 restart route nobody would answer. systemd's
notify socket and watchdog likewise belong to the unit's main process only.
"""

import os
import sys
from unittest.mock import patch

import pytest

from gateway.restart import is_gateway_supervisor_process, launchd_job_label
from tests.tools._child_env_fixtures import child_env, observe_terminal
from tools.environments import local

SUPERVISED_GATEWAY_ENV = {
    "NASTECH_LAUNCHD_LABEL": "ai.nastech.gateway",
    "XPC_SERVICE_NAME": "0",
    "NASTECH_GATEWAY_EXTERNAL_SUPERVISOR": "1",
    "NOTIFY_SOCKET": "/run/user/1000/systemd/notify",
    "WATCHDOG_USEC": "30000000",
    "WATCHDOG_PID": "4242",
}
OWNER_ONLY = ("NASTECH_LAUNCHD_LABEL", "NASTECH_GATEWAY_EXTERNAL_SUPERVISOR",
              "NOTIFY_SOCKET", "WATCHDOG_USEC", "WATCHDOG_PID")


def _reads_as_unsupervised(env):
    return not is_gateway_supervisor_process(env) and launchd_job_label(env) is None


@pytest.mark.parametrize("build", [
    lambda base: local.build_subprocess_env(base),
    lambda base: local.build_subprocess_env(base, scrub_secrets=False),
    lambda base: local.nastech_subprocess_env(base_env=base),
], ids=["scrubbed", "unscrubbed", "nastech_subprocess_env"])
@pytest.mark.usefixtures("child_env")
def test_child_env_factories_drop_the_supervised_gateways_identity(build):
    parent = {**os.environ, **SUPERVISED_GATEWAY_ENV}
    # Control: the gateway itself still resolves its launchd job and the restart route.
    assert launchd_job_label(parent) == "ai.nastech.gateway" and is_gateway_supervisor_process(parent)

    child = build(parent)

    assert _reads_as_unsupervised(child)
    assert not set(OWNER_ONLY) & set(child)
    # XPC_SERVICE_NAME is launchd's own per-process stamp ("0" below the wrapper); `nastech update`
    # compares it to decide whether it runs inside a job, so it passes through untouched.
    assert child["XPC_SERVICE_NAME"] == "0"


@pytest.mark.usefixtures("child_env")
def test_agent_terminal_child_sees_no_supervisor_identity(tmp_path, monkeypatch):
    for key, value in SUPERVISED_GATEWAY_ENV.items():
        monkeypatch.setenv(key, value)
    env = local.LocalEnvironment(cwd=str(tmp_path), timeout=30)
    try:
        seen = observe_terminal(env, [*OWNER_ONLY, "XPC_SERVICE_NAME"])
    finally:
        env.cleanup()

    assert {k: seen[k] for k in OWNER_ONLY} == dict.fromkeys(OWNER_ONLY)
    assert _reads_as_unsupervised({k: v for k, v in seen.items() if v is not None})


@pytest.mark.usefixtures("child_env")
def test_external_supervisor_gateways_tool_child_cli_stays_on_the_gateways_profile(tmp_path, monkeypatch):
    """Losing the supervisor claim must not unpin the agent's own `nastech ...` commands (#74872)."""
    from nastech_cli import main as cli_main

    root = tmp_path / ".nastech"
    (root / "profiles" / "work").mkdir(parents=True)
    (root / "profiles" / "work" / "config.yaml").write_text("{}\n")
    (root / "active_profile").write_text("work\n")
    monkeypatch.setattr(sys, "argv", ["nastech", "cron", "list"])

    def child_cli_home(parent_extra):
        child = local.build_subprocess_env({**os.environ, "NASTECH_HOME": str(root), **parent_extra})
        with patch.dict(os.environ, child, clear=True):
            cli_main._apply_profile_override()
            return child, os.environ["NASTECH_HOME"]

    # Control: an unpinned root-home CLI follows the sticky profile.
    assert child_cli_home({})[1] == str(root / "profiles" / "work")
    child, home = child_cli_home({"NASTECH_GATEWAY_EXTERNAL_SUPERVISOR": "1"})
    assert home == str(root)
    assert _reads_as_unsupervised(child)
