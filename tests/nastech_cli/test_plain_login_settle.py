"""Every plain device login that saves a Nastech account over the free tier settles the config itself.

The guest handoff only moves apps; moving a config left on the free tier's route (the welcome model
on the welcome host) to the account is each sign-in's own completion step, run once the auth-store
locks are released. Driven against the fake portal ``nastech auth upgrade`` is tested with.
"""

from __future__ import annotations

import argparse
from datetime import UTC, datetime, timedelta
from types import SimpleNamespace

import pytest

from nastech_cli import anon_auth, auth_nastech
from tests.nastech_cli.test_guest_handoff import holds_auth_locks
from tests.nastech_cli.test_anon_upgrade import (
    EMAIL, FREE_PICK, INFERENCE, PORTAL, REFRESH_TOKEN, WELCOME, _jwt, _model_config, _write_model_config,
    free_account, portal)

__all__ = ["free_account", "portal"]


def _account() -> dict:
    return {"access_token": _jwt(sub="nas_user:9", client_id="nastech-cli", account_tier="free", email=EMAIL),
            "refresh_token": REFRESH_TOKEN, "portal_base_url": PORTAL, "inference_base_url": INFERENCE,
            "client_id": "nastech-cli", "expires_in": 900,
            "expires_at": (datetime.now(UTC) + timedelta(minutes=15)).isoformat()}


def _terminal_login(monkeypatch):
    monkeypatch.setattr(auth_nastech, "_offer_shared_nastech_import", lambda timeout: None)
    monkeypatch.setattr(auth_nastech, "_pick_nastech_model_after_login", lambda *a: None)
    from nastech_cli.auth import PROVIDER_REGISTRY
    auth_nastech._login_nastech(argparse.Namespace(no_browser=True, timeout=15.0), PROVIDER_REGISTRY["nastech"])


def _auth_add(monkeypatch):
    from nastech_cli import auth_commands
    auth_commands._add_nastech_oauth_credential(SimpleNamespace(label=None, timeout=None, no_browser=True), "nastech")


def _step_up(monkeypatch):
    auth_nastech.step_up_nastech_billing_scope(open_browser=False)


def _tool_login(monkeypatch):
    from nastech_cli import nastech_subscription
    monkeypatch.setattr(nastech_subscription, "_confirm", lambda prompt: True)
    assert nastech_subscription._run_nastech_portal_login_only(capability="Web search") is True


@pytest.mark.parametrize("surface", [_terminal_login, _auth_add, _step_up, _tool_login],
                         ids=["nastech model / login", "auth add nastech", "billing step-up", "tool setup login"])
def test_the_sign_in_settles_the_config_once_after_its_locks_are_released(
        portal, free_account, monkeypatch, surface):
    from nastech_cli import auth
    anon_auth.ensure_portal_identity(explicit=True)
    _write_model_config({"provider": "nastech", "default": anon_auth.GUEST_MODEL, "base_url": WELCOME})
    monkeypatch.setattr(auth, "_nastech_device_code_login", lambda **kw: _account())
    monkeypatch.setattr(auth_nastech, "_nastech_device_code_login", lambda **kw: _account())
    settles = []
    real_settle = anon_auth.settle_after_upgrade

    def _recording(state):
        settles.append(holds_auth_locks())
        return real_settle(state)
    monkeypatch.setattr(anon_auth, "settle_after_upgrade", _recording)

    surface(monkeypatch)

    assert settles == [False]
    model_cfg = _model_config()
    assert model_cfg["default"] == FREE_PICK
    assert model_cfg["base_url"] == INFERENCE.rstrip("/")


@pytest.mark.parametrize("surface", [_terminal_login, _auth_add, _tool_login],
                         ids=["nastech model / login", "auth add nastech", "tool setup login"])
def test_the_terminal_sign_in_prints_what_moved(portal, free_account, monkeypatch, capsys, surface):
    from nastech_cli import auth
    anon_auth.ensure_portal_identity(explicit=True)
    portal.claim_reply = {**portal.claim_reply, "connectors": {
        "kind": "moved", "moved_toolkits": ["gmail"], "dropped_toolkits": ["slack"]}}
    monkeypatch.setattr(auth, "_nastech_device_code_login", lambda **kw: _account())
    monkeypatch.setattr(auth_nastech, "_nastech_device_code_login", lambda **kw: _account())

    surface(monkeypatch)

    out = capsys.readouterr().out
    assert f"Your apps moved to {EMAIL}: Gmail." in out
    assert f"Reconnect in {EMAIL}: Slack." in out
