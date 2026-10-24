"""Nastech free tier on the read-only display surfaces and the keepalive.

Contract (R-USR-1): wherever a free-tier identity renders (``nastech auth status nastech``,
``nastech auth list``, ``nastech status``, ``nastech portal info``) the user sees the free-tier label
plus the upgrade hint, and never the internal identity vocabulary. A real account keeps its normal
rendering. The keepalive has nothing to keep alive for the free tier and must not start a thread.
"""

from __future__ import annotations

import base64
import dataclasses
import json
import re
import time
from pathlib import Path
from types import SimpleNamespace

import pytest

from nastech_cli import (
    anon_auth,
    auth_commands,
    guest_handoff,
    nastech_account,
    nastech_auth_keepalive,
    portal_cli,
    status_auth,
)
from nastech_cli.auth import _load_auth_store
from nastech_constants import get_nastech_home
from tests.nastech_cli.anon_portal import as_local_desktop_backend, off_local_desktop

WELCOME = "https://welcome-api.nastechresearch.github.io/v1"
# Words that must never appear on a user-facing free-tier surface.
_FORBIDDEN = re.compile(r"guest|anonymous|user id|org id|nas_user|nas_organisation", re.IGNORECASE)


def _jwt(**claims) -> str:
    def seg(obj):
        return base64.urlsafe_b64encode(json.dumps(obj).encode()).rstrip(b"=").decode()
    payload = {"sub": "nas_user:abc", "client_id": "nas-anonymous", "account_tier": "anonymous",
               "scope": "inference:invoke", "exp": int(time.time()) + 10 ** 8, **claims}
    return f"{seg({'alg': 'RS256'})}.{seg(payload)}.sig"


def _write_auth(nastech_state: dict) -> None:
    home = Path(get_nastech_home())
    home.mkdir(parents=True, exist_ok=True)
    (home / "auth.json").write_text(json.dumps({"active_provider": "nastech", "providers": {"nastech": nastech_state}}))


def _guest_state() -> dict:
    return {
        "auth_method": "anonymous", "account_tier": "anonymous", "anon_token": "anon_t",
        "access_token": _jwt(), "expires_at": "2030-01-01T00:00:00+00:00",
        "inference_base_url": WELCOME, "user_id": "nas_user:abc", "org_id": "nas_organisation:def",
        anon_auth.WELCOME_CLAIM_FLAG: True,
    }


def _account_state() -> dict:
    return {
        "auth_method": "oauth_device_code", "client_id": "nastech-cli",
        "access_token": _jwt(sub="nas_user:real", client_id="nastech-cli", account_tier="standard", paid_access=True),
        "refresh_token": "rt_live", "expires_at": "2030-01-01T00:00:00+00:00",
        "portal_base_url": "https://portal.nastechresearch.github.io", "inference_base_url": "https://inference-api.nastechresearch.github.io/v1",
    }


@pytest.fixture
def isolated_store(monkeypatch, tmp_path):
    monkeypatch.setenv("NASTECH_SHARED_AUTH_DIR", str(tmp_path / "shared-store"))
    # The welcome trial carries inference only on the desktop's local backend.
    as_local_desktop_backend(monkeypatch)
    for var in ("OPENROUTER_API_KEY", "OPENAI_API_KEY", "ANTHROPIC_API_KEY", "NASTECH_API_KEY"):
        monkeypatch.delenv(var, raising=False)
    # No network: the account lookup is derived from the JWT the store already holds.
    monkeypatch.setattr(nastech_account, "_fetch_nastech_account_info",
                        lambda *a, **k: pytest.fail("portal fetch must not happen on a read-only surface"))
    nastech_account.reset_nastech_portal_account_info_cache()
    import nastech_cli.auth as auth_mod
    auth_mod.invalidate_nastech_auth_status_cache()
    yield
    nastech_account.reset_nastech_portal_account_info_cache()
    auth_mod.invalidate_nastech_auth_status_cache()


def _render_all(capsys) -> dict[str, str]:
    out: dict[str, str] = {}
    auth_commands.auth_status_command(SimpleNamespace(provider="nastech"))
    out["auth status"] = capsys.readouterr().out
    auth_commands.auth_list_command(SimpleNamespace(provider="nastech"))
    out["auth list"] = capsys.readouterr().out
    ctx = SimpleNamespace(config={}, nastech_logged_in=False, nastech_inference_present=False, nastech_account_info=None)
    status_auth._render_auth_providers(ctx)
    out["nastech status"] = capsys.readouterr().out
    portal_cli._cmd_status(SimpleNamespace())
    out["portal info"] = capsys.readouterr().out
    return out


def test_free_tier_renders_free_tier_copy_on_every_surface(isolated_store, capsys):
    _write_auth(_guest_state())
    rendered = _render_all(capsys)
    for surface, text in rendered.items():
        assert "free tier" in text.lower(), f"{surface} did not name the free tier:\n{text}"
        assert anon_auth.FREE_TIER_LABEL in text and anon_auth.GUEST_MODEL in text, surface
        assert anon_auth.UPGRADE_HINT in text, f"{surface} lacks the upgrade hint:\n{text}"
        leaked = _FORBIDDEN.search(text)
        assert leaked is None, f"{surface} leaked {leaked.group(0)!r}:\n{text}"
    # Billing / entitlement copy for the free tier points at the upgrade path, never at billing.
    info = nastech_account.get_nastech_portal_account_info()
    assert info.is_anonymous_tier
    message = nastech_account.format_nastech_portal_entitlement_message(info, capability="managed web tools")
    assert message == nastech_account.FREE_TIER_NEEDS_ACCOUNT
    assert "billing" not in message.lower() and _FORBIDDEN.search(message) is None


def test_real_account_keeps_account_rendering(isolated_store, capsys):
    _write_auth(_account_state())
    rendered = _render_all(capsys)
    for surface, text in rendered.items():
        assert "free tier" not in text.lower(), f"{surface} mislabelled a real account:\n{text}"
        assert anon_auth.UPGRADE_HINT not in text, surface
    assert "logged in" in rendered["auth status"]
    assert "credentials" in rendered["auth list"]
    info = nastech_account.get_nastech_portal_account_info()
    assert not info.is_anonymous_tier
    assert nastech_account.format_nastech_portal_entitlement_message(info) is None  # paid_access claim entitles


@pytest.mark.parametrize("tier", ["Anonymous", "ANONYMOUS", " anonymous "])
def test_anonymous_tier_matches_case_and_whitespace_insensitively(isolated_store, tier):
    """The tier claim is wire data; casing must not hand a guest billing copy instead of the sign-in copy."""
    _write_auth({**_guest_state(), "account_tier": tier, "access_token": _jwt(account_tier=tier)})
    info = nastech_account.get_nastech_portal_account_info()
    assert info.is_anonymous_tier
    assert nastech_account.format_nastech_portal_entitlement_message(info) == nastech_account.FREE_TIER_NEEDS_ACCOUNT


def test_guest_whose_lookup_fails_still_gets_the_sign_in_copy(isolated_store, monkeypatch):
    """A token inside its refresh window falls through to the account API; when that fails the
    stored tier must survive on the error snapshot."""
    state = {**_guest_state(), "access_token": _jwt(exp=int(time.time()) + 30),
             "portal_base_url": "http://127.0.0.1:9"}
    _write_auth(state)
    monkeypatch.setattr(nastech_account, "_fetch_nastech_account_info",
                        lambda *a, **k: (_ for _ in ()).throw(RuntimeError("portal down")))
    info = nastech_account.get_nastech_portal_account_info()
    assert info.error is not None and info.is_anonymous_tier
    assert nastech_account.format_nastech_portal_entitlement_message(info) == nastech_account.FREE_TIER_NEEDS_ACCOUNT


def test_keepalive_does_not_start_for_free_tier(isolated_store, monkeypatch):
    started: list = []

    class _Thread:
        def __init__(self, *args, **kwargs):
            self._name = kwargs.get("name")
        def start(self):
            started.append(self._name)
        def is_alive(self):
            return True
        def join(self, timeout=None):
            pass
    monkeypatch.setattr(nastech_auth_keepalive.threading, "Thread", _Thread)
    monkeypatch.setattr(nastech_auth_keepalive, "_keepalive_thread", None)
    from nastech_cli import guest_handoff
    monkeypatch.setattr(guest_handoff, "_worker_thread", None)

    _write_auth(_guest_state())
    assert nastech_auth_keepalive.start_nastech_auth_keepalive(interval_seconds=900) is None
    # The free-tier handoff retry worker runs in a guest process too; the token keepalive does not.
    assert started == ["nastech-guest-handoff"]

    _write_auth(_account_state())
    thread = nastech_auth_keepalive.start_nastech_auth_keepalive(interval_seconds=900)
    assert thread is not None and started == ["nastech-guest-handoff", "nastech-auth-keepalive"]
    monkeypatch.setattr(nastech_auth_keepalive, "_keepalive_thread", None)


_HANDOFF_VIEWS = [
    *({"state": "claimed", "account_email": "person@example.test", "connectors_kind": kind,
       "moved_toolkits": ["gmail"], "dropped_toolkits": ["slack"]} for kind in ("moved", "conflict", "none")),
    # The retrying line names Nastech as a subject ("Nastech keeps trying"), not a command; it is not checked here.
    {"state": "failed", "error": "no_destination"}, {"state": "gone", "probably_moved": True},
]


def test_no_chat_copy_of_any_sign_in_state_leaks_a_terminal_verb_or_a_forbidden_word():
    placeholders = {
        "link": "https://example.test/sign-in",
        "code": "code-1",
        "expires_in": 900,
        "interval": 1,
        "email": "person@example.test",
        "model": "model-1",
        "model_changed": True,
        "reason": "unknown",
        "detail": "private detail",
        "retry_after": 0.0,
        # Every handoff result line a completed sign-in can carry.
        "handoff": tuple(line for view in _HANDOFF_VIEWS for line in guest_handoff.result_lines(view)),
        "handoff_status": guest_handoff.wire_status(_HANDOFF_VIEWS[0]),
    }
    forbidden = re.compile(r"claim|nastech portal|anonymous|guest", re.IGNORECASE)
    terminal_or_url = re.compile(r"nastech |https?://", re.IGNORECASE)

    for state_type in anon_auth.SignInState.__subclasses__():
        kwargs = {field.name: placeholders[field.name] for field in dataclasses.fields(state_type)}
        copy = state_type(**kwargs).copy
        assert _FORBIDDEN.search(copy) is None, state_type.__name__
        assert forbidden.search(copy) is None, state_type.__name__
        assert terminal_or_url.search(copy) is None, state_type.__name__


def test_the_paid_tool_notice_switches_wording_inside_a_chat():
    info = nastech_account.NastechPortalAccountInfo(
        logged_in=True, source="token", fresh=True, account_tier="anonymous"
    )
    assert nastech_account.format_nastech_portal_entitlement_message(
        info, in_chat=True
    ) == nastech_account.FREE_TIER_NEEDS_ACCOUNT_CHAT
    assert nastech_account.format_nastech_portal_entitlement_message(
        info, in_chat=False
    ) == nastech_account.FREE_TIER_NEEDS_ACCOUNT


def test_a_claimed_guest_reads_as_the_free_tier_on_the_cli_too(isolated_store, monkeypatch, capsys):
    """Once the Desktop claimed the trial, the CLI runs on it as well."""
    off_local_desktop(monkeypatch)
    _write_auth(_guest_state())

    auth_commands.auth_status_command(SimpleNamespace(provider="nastech"))
    text = capsys.readouterr().out
    assert "free tier" in text.lower()
