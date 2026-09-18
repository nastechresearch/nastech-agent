"""Unattended approval contexts never resolve as interactive (#110932).

A gateway sets NASTECH_EXEC_ASK=1 at startup and hands its environ to every external cron
worker; interactive launches export NASTECH_INTERACTIVE=1. Inside cron nobody can answer the
card, so ``_presence()`` must clear the trio and let the gate resolve from
``approvals.cron_mode``. Unattended platforms are NOT cleared: api_server answers via the
``/v1/runs`` approval bridge, which needs ``is_ask`` intact.
"""

import pytest

from tools import approval as approval_mod


@pytest.fixture
def leaked_presence(monkeypatch):
    monkeypatch.setenv("NASTECH_INTERACTIVE", "1")
    monkeypatch.setenv("NASTECH_EXEC_ASK", "1")
    monkeypatch.setenv("NASTECH_GATEWAY_SESSION", "1")
    monkeypatch.delenv("NASTECH_CRON_SESSION", raising=False)
    monkeypatch.delenv("NASTECH_SINGLE_QUERY_SESSION", raising=False)
    monkeypatch.delenv("NASTECH_SESSION_PLATFORM", raising=False)


def test_cron_context_clears_leaked_presence(monkeypatch, leaked_presence):
    monkeypatch.setenv("NASTECH_CRON_SESSION", "1")
    _, is_cli, is_gateway, is_ask = approval_mod._presence()
    assert (is_cli, is_gateway, is_ask) == (False, False, False)


def test_interactive_session_keeps_presence(monkeypatch, leaked_presence):
    _, is_cli, is_gateway, is_ask = approval_mod._presence()
    assert (is_cli, is_gateway, is_ask) == (True, True, True)


def test_api_server_platform_keeps_exec_ask_for_runs_approval_bridge(monkeypatch, leaked_presence):
    """api_server resolves approvals via ``approval.request`` → ``POST /v1/runs/{id}/approval``;
    clearing ``is_ask`` there would turn every dangerous command into an instant BLOCK."""
    monkeypatch.setenv("NASTECH_SESSION_PLATFORM", "api_server")
    _, _, _, is_ask = approval_mod._presence()
    assert is_ask is True
