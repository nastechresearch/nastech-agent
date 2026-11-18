"""``/usage`` shows the active provider's block, then the Nastech balance whenever Nastech is signed in.

On a Claude session the Nastech balance printed inside the Claude block with "/topup to add to your
balance", which read as a Claude balance. Hiding it lost a balance the user holds, so the Nastech
section now always follows a signed-in profile's provider block: off a Nastech route it has its own
heading, no top-up nudge, and is read with the stored token only (a /usage read never refreshes
the Nastech credential the session is not running on).
"""
from __future__ import annotations

import time
from datetime import UTC, datetime, timedelta

import pytest

from agent.account_usage_nastech import NASTECH_OTHER_ROUTE_HEADING, nastech_usage_lines
from tests.nastech_cli.test_nastech_account import _account_payload, _jwt

_PAYLOAD = _account_payload(allowed=True, subscription=None, subscription_credits=0, purchased_credits=7.75)


@pytest.fixture
def portal(monkeypatch):
    """A signed-in profile whose portal answers ``_PAYLOAD``; records each account fetch's token and any refresh."""
    seen = {"tokens": [], "refreshed": 0}
    state = {"access_token": _jwt({"sub": "u", "exp": int(time.time()) + 900}), "client_id": "nastech-cli",
             "portal_base_url": "https://portal.example.test",
             "expires_at": (datetime.now(UTC) + timedelta(minutes=15)).isoformat()}

    def refresh(**kw):
        seen["refreshed"] += 1
        return state["access_token"]

    def fetch(token, base=None):
        seen["tokens"].append(token)
        return _PAYLOAD
    monkeypatch.setattr("nastech_cli.auth.get_provider_auth_state", lambda provider: state if seen.get("signed_in", True) else {})
    monkeypatch.setattr("nastech_cli.auth.resolve_nastech_access_token", refresh)
    monkeypatch.setattr("nastech_cli.nastech_account._fetch_nastech_account_info", fetch)
    monkeypatch.delenv("NASTECH_DEV_CREDITS_FIXTURE", raising=False)
    return seen, state


def test_another_providers_session_gets_the_labelled_nastech_balance_without_topup_actions(portal):
    seen, state = portal
    lines = nastech_usage_lines(nastech_route=False)
    assert lines[0] == NASTECH_OTHER_ROUTE_HEADING and "Top-up credits: $7.75" in lines
    assert not any("/topup" in line or line.startswith("Top up:") for line in lines), lines
    assert seen == {"tokens": [state["access_token"]], "refreshed": 0}  # the stored token, never refreshed
    assert "(or run /topup)" in nastech_usage_lines(nastech_route=True)

