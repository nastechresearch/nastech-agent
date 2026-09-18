"""Home-channel startup notice names the free tier only when a guest carries the gateway's inference."""

import base64
import json
import time

import pytest
from unittest.mock import AsyncMock

import gateway.run as gateway_run
from gateway.config import HomeChannel, Platform
from gateway.platforms.base import SendResult
from nastech_cli import anon_auth
from nastech_cli.auth import _auth_store_lock, _load_auth_store, _save_auth_store
from tests.gateway.restart_test_helpers import make_restart_runner

FREE_TIER_LINE = "Inference: Free tier (nastech/welcome). Sign in for more: /login"


def _jwt(**claims) -> str:
    def seg(obj):
        return base64.urlsafe_b64encode(json.dumps(obj).encode()).rstrip(b"=").decode()
    payload = {"sub": "nas_user:1", "client_id": "nas-anonymous", "account_tier": "anonymous",
               "scope": "inference:invoke tool:invoke", "exp": int(time.time()) + 900, **claims}
    return f"{seg({'alg': 'RS256'})}.{seg(payload)}.sig"


def _seed_nastech(state: dict) -> None:
    with _auth_store_lock():
        store = _load_auth_store()
        store.setdefault("providers", {})["nastech"] = state
        store["active_provider"] = "nastech"
        _save_auth_store(store)


def _guest_state() -> dict:
    return {"auth_method": anon_auth.ANON_AUTH_METHOD, "account_tier": "anonymous", "anon_token": "anon_0001",
            "client_id": "nas-anonymous", "access_token": _jwt(), "expires_at": "2999-01-01T00:00:00+00:00",
            "inference_base_url": "https://welcome-api.nastechresearch.github.io/v1"}


def _account_state() -> dict:
    return {"auth_method": "oauth", "access_token": _jwt(client_id="nastech-cli", account_tier="pro"),
            "refresh_token": "rt", "expires_at": "2999-01-01T00:00:00+00:00"}


@pytest.fixture
def nastech_runner(tmp_path, monkeypatch):
    monkeypatch.setattr(gateway_run, "_nastech_home", tmp_path)
    monkeypatch.setenv("NASTECH_SHARED_AUTH_DIR", str(tmp_path / "shared-store"))
    monkeypatch.setenv("NASTECH_GUEST_ONBOARDING", "1")
    # Provider precedence gates the line and is answered from persisted state only (no network at boot).
    for var in ("OPENROUTER_API_KEY", "OPENAI_API_KEY", "ANTHROPIC_API_KEY", "NASTECH_API_KEY"):
        monkeypatch.delenv(var, raising=False)
    runner, adapter = make_restart_runner()
    runner.config.platforms[Platform.TELEGRAM].home_channel = HomeChannel(
        platform=Platform.TELEGRAM, chat_id="home-1", name="Home")
    adapter.send = AsyncMock(return_value=SendResult(success=True, message_id="home"))
    return runner, adapter


async def _startup_message(runner, adapter) -> str:
    delivered = await runner._send_home_channel_startup_notifications()
    assert delivered == {("telegram", "home-1", None)}
    adapter.send.assert_called_once()
    return adapter.send.call_args.args[1]


@pytest.mark.asyncio
async def test_guest_inference_adds_exactly_one_free_tier_line(nastech_runner):
    runner, adapter = nastech_runner
    _seed_nastech(_guest_state())
    assert anon_auth.guest_carries_inference()

    message = await _startup_message(runner, adapter)

    lines = message.splitlines()
    assert lines[0] == "♻️ Gateway online — Nastech is back and ready."
    assert lines[1:] == [FREE_TIER_LINE]
    assert "guest" not in message.lower() and "anonymous" not in message.lower()


@pytest.mark.asyncio
async def test_signed_in_account_keeps_the_plain_online_notice(nastech_runner):
    runner, adapter = nastech_runner
    _seed_nastech(_account_state())
    assert not anon_auth.guest_carries_inference()

    message = await _startup_message(runner, adapter)

    assert message == "♻️ Gateway online — Nastech is back and ready."


@pytest.mark.asyncio
async def test_non_nastech_provider_never_mentions_the_free_tier(nastech_runner, monkeypatch):
    runner, adapter = nastech_runner
    _seed_nastech(_guest_state())  # identity exists for connectors, but inference is elsewhere
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-or-test")  # an explicit key wins provider precedence

    message = await _startup_message(runner, adapter)

    assert message == "♻️ Gateway online — Nastech is back and ready."
