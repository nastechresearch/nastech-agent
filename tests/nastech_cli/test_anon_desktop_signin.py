"""Desktop (dashboard API) sign-in over a Nastech free-tier identity.

``POST /api/providers/oauth/nastech/start`` registers the connector transfer with the account service
and hands the renderer the transfer's code and consent URL; the poller waits for the transfer, then
takes the token grant, persists the account, and settles the default model. Driven through the real
FastAPI routes against a fake account service (the same fake ``nastech auth upgrade`` is tested with).
"""

from __future__ import annotations

import time

import httpx
import pytest
from fastapi.testclient import TestClient

from nastech_cli import anon_auth
from nastech_cli.auth import _load_auth_store
from nastech_cli.web_server import _SESSION_TOKEN, app
from tests.nastech_cli.test_anon_upgrade import (
    EMAIL, FREE_PICK, INFERENCE, PORTAL, WELCOME, _model_config, _write_model_config, free_account, portal)

client = TestClient(app)
HEADERS = {"X-Nastech-Session-Token": _SESSION_TOKEN}

__all__ = ["free_account", "portal"]  # fixtures imported from the CLI test module


def _wait_for_terminal(session_id: str, timeout: float = 10.0) -> dict:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        body = client.get(f"/api/providers/oauth/nastech/poll/{session_id}", headers=HEADERS).json()
        if body["status"] != "pending":
            return body
        time.sleep(0.05)
    pytest.fail("poller never left pending")


def test_start_registers_the_transfer_and_completion_settles_the_account(portal, free_account):
    anon_auth.ensure_portal_identity(explicit=True)
    _write_model_config({"provider": "nastech", "default": anon_auth.GUEST_MODEL, "base_url": WELCOME})

    resp = client.post("/api/providers/oauth/nastech/start", headers=HEADERS)
    assert resp.status_code == 200, resp.text
    start = resp.json()
    # The renderer shows the transfer's code and consent page, not the generic device page.
    assert start["user_code"] == "clm_1"
    assert start["verification_url"] == f"{PORTAL}/device"
    assert portal.intent_bodies[0]["user_code"] == portal.user_code
    assert portal.intent_bodies[0]["device_code"] == portal.device_code

    body = _wait_for_terminal(start["session_id"])
    assert body["status"] == "approved"
    assert body["account_email"] == EMAIL
    assert body["model"] == FREE_PICK
    state = _load_auth_store()["providers"]["nastech"]
    assert "anon_token" not in state and not anon_auth.is_guest_state(state)
    model_cfg = _model_config()
    assert model_cfg["default"] == FREE_PICK
    assert model_cfg["base_url"] == INFERENCE.rstrip("/")
    assert not anon_auth.route_is_welcome_host(model_cfg["base_url"])


def test_a_transfer_the_user_declined_is_reported_with_its_reason_and_keeps_the_free_tier(portal, free_account):
    guest = anon_auth.ensure_portal_identity(explicit=True)
    portal.status_sequence = [{"status": "voided", "reason": "user_declined"}]

    start = client.post("/api/providers/oauth/nastech/start", headers=HEADERS).json()
    body = _wait_for_terminal(start["session_id"])
    assert body["status"] == "denied"
    assert body["reason"] == "user_declined"
    assert body["error_message"] == anon_auth.UPGRADE_REASON_COPY["user_declined"]
    assert portal.token_grants == 0
    assert _load_auth_store()["providers"]["nastech"]["anon_token"] == guest["anon_token"]


def test_status_routes_report_the_free_tier(portal):
    anon_auth.ensure_portal_identity(explicit=True)
    portal_status = client.get("/api/portal", headers=HEADERS).json()
    assert portal_status["free_tier"] is True
    assert portal_status["account_tier"] == "anonymous"
    providers = client.get("/api/providers/oauth", headers=HEADERS).json()["providers"]
    nastech = next(p for p in providers if p["id"] == "nastech")
    assert nastech["status"]["free_tier"] is True


def test_a_sign_in_cancelled_while_waiting_never_persists_the_account(portal, free_account, monkeypatch):
    """The poller is blocked on the transfer when the user cancels; when the wait returns completed,
    nothing may reach the auth store."""
    import threading
    from nastech_cli import web_server_oauth
    guest = anon_auth.ensure_portal_identity(explicit=True)
    release = threading.Event()

    def _wait_until_released(client, portal_base_url, claim_code, *, expires_in, interval, cancelled=None):
        release.wait(10)
        return {"status": "completed", "user_id": "nas_user:9", "account_email": EMAIL}
    monkeypatch.setattr(anon_auth, "wait_for_promotion", _wait_until_released)

    start = client.post("/api/providers/oauth/nastech/start", headers=HEADERS).json()
    assert client.delete(f"/api/providers/oauth/sessions/{start['session_id']}", headers=HEADERS).json()["ok"] is True
    release.set()
    for _ in range(100):
        time.sleep(0.05)
    assert portal.token_grants == 0
    state = _load_auth_store()["providers"]["nastech"]
    assert state["anon_token"] == guest["anon_token"] and anon_auth.is_guest_state(state)
    assert web_server_oauth._oauth_sessions.get(start["session_id"]) is None
