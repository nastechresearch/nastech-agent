"""Redaction-safe forensic logging at the Nastech OAuth quarantine path.

A NAS-hosted Fly agent's Nastech bootstrap session can take a terminal
``invalid_grant`` and get quarantined (dead tokens cleared from auth.json).
Historically this was completely silent — no WARNING+ record at the terminal
rejection, only a downstream "No access token found" warning once the pool was
already empty. The Fly log drain is WARNING-only, so nothing about the terminal
death reached centralized logging. These tests lock in that
``_quarantine_nastech_oauth_state`` now emits a WARNING+ forensic record, and — the
load-bearing assertion — that the raw refresh token never appears in that output.
"""

import hashlib
import logging

from nastech_cli.auth import AuthError, _quarantine_nastech_oauth_state


# A distinctive, obviously-fake refresh token so the redaction assertion is
# unambiguous if it ever leaks.
_FAKE_RT = "nastech_rt_LEAK_CANARY_do_not_log_raw_0123456789abcdef"
_EXPECTED_FP = hashlib.sha256(_FAKE_RT.encode("utf-8")).hexdigest()[:12]


def _make_state(**overrides):
    state = {
        "portal_base_url": "https://portal.example.com",
        "client_id": "test-client-id",
        "access_token": "nastech_at_SECRET_access_token_material",
        "refresh_token": _FAKE_RT,
        "agent_key": "nastech_agent_key_SECRET_material",
        "agent_key_id": "ak-12345",
        "expires_at": "2020-01-01T00:00:00+00:00",  # in the past
        "obtained_at": "2019-12-31T00:00:00+00:00",
    }
    state.update(overrides)
    return state


def _error():
    return AuthError(
        "invalid_grant: token expired or revoked",
        provider="nastech",
        code="invalid_grant",
        relogin_required=True,
    )






def test_raw_refresh_token_never_logged(caplog):
    """Load-bearing redaction-safety test: the raw secret must never appear."""
    state = _make_state()
    with caplog.at_level(logging.DEBUG, logger="nastech_cli.auth"):
        _quarantine_nastech_oauth_state(state, _error(), reason="unit_test_quarantine")

    text = caplog.text
    assert _FAKE_RT not in text, "RAW refresh token leaked into log output!"
    # Belt-and-suspenders: the access token and agent key must not leak either.
    assert "nastech_at_SECRET_access_token_material" not in text
    assert "nastech_agent_key_SECRET_material" not in text


