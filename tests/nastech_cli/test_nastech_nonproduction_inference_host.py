"""Operator authority over Nastech routing overrides and Portal-returned inference hosts.

Portal-returned inference URLs go through a host allowlist before the user's bearer is sent
there. Two authority boundaries hold:

* Profile authority — ``NASTECH_INFERENCE_BASE_URL`` / ``NASTECH_PORTAL_BASE_URL`` are per-profile
  ``.env`` values read through the profile secret scope. A multi-profile call that has lost its
  scope gets *no* override, never the launch profile's ambient value.
* Service authority — a network-provided inference host outside the production set is accepted
  only when it equals the host the operator named in ``NASTECH_INFERENCE_BASE_URL``. Sharing the
  corporate domain is not authorization; the operator's explicit override is.
"""
from __future__ import annotations

import pytest

from nastech_cli import auth_nastech

PROD_INFERENCE = "https://inference-api.nastechresearch.github.io/v1"
ENV_INFERENCE = "https://inference.example-env.nastechresearch.github.io/v1"
OTHER_NASTECH_HOST = "https://portal.nastechresearch.github.io/v1"  # Nastech-owned, but not an inference gateway
NONPROD_PORTAL = "https://portal.example-env.nastechresearch.github.io"


@pytest.mark.parametrize("helper, var", [
    (auth_nastech._nastech_inference_env_override, "NASTECH_INFERENCE_BASE_URL"),
    (auth_nastech._nastech_portal_env_override, "NASTECH_PORTAL_BASE_URL"),
])
def test_routing_overrides_follow_the_profile_scope_and_fail_closed_without_one(monkeypatch, helper, var):
    """Unscoped single-profile: environ. Multi-profile: the scope's value wins, a scoped miss is a
    miss, and a call with NO scope gets None — never the launch profile's ambient value."""
    from agent import secret_scope as ss

    monkeypatch.setenv(var, "https://launch.example.nastechresearch.github.io")
    monkeypatch.delenv("NASTECH_PORTAL_BASE_URL_LEGACY", raising=False)
    assert helper() == "https://launch.example.nastechresearch.github.io"

    ss.set_multiplex_active(True)
    try:
        token = ss.set_secret_scope({var: "https://profile.example.nastechresearch.github.io"})
        try:
            assert helper() == "https://profile.example.nastechresearch.github.io"
        finally:
            ss.reset_secret_scope(token)
        token = ss.set_secret_scope({})
        try:
            assert helper() is None, "scoped miss must not read environ"
        finally:
            ss.reset_secret_scope(token)
        assert helper() is None, "a call that lost its profile scope has no authority over the launch value"
    finally:
        ss.set_multiplex_active(False)


@pytest.mark.parametrize(
    "inference_override, url, expected",
    [
        # The operator named the environment's gateway; the Portal's matching value survives.
        (ENV_INFERENCE, ENV_INFERENCE, ENV_INFERENCE),
        # No operator authority: a non-production host is refused however it arrived.
        (None, ENV_INFERENCE, None),
        # Another Nastech-owned host is not the named recipient — refused, DNS suffix or not.
        (ENV_INFERENCE, OTHER_NASTECH_HOST, None),
        # Production is always valid; the rule widens, never narrows.
        (None, PROD_INFERENCE, PROD_INFERENCE),
        (ENV_INFERENCE, PROD_INFERENCE, PROD_INFERENCE),
    ],
)
def test_network_inference_host_needs_the_operator_named_recipient(monkeypatch, inference_override, url, expected):
    if inference_override is None:
        monkeypatch.delenv("NASTECH_INFERENCE_BASE_URL", raising=False)
    else:
        monkeypatch.setenv("NASTECH_INFERENCE_BASE_URL", inference_override)
    assert auth_nastech._validate_nastech_inference_url_from_network(url) == expected


def test_portal_override_alone_grants_nothing(monkeypatch):
    """A non-production Portal override, with or without a matching stored Portal, does not make
    the Portal's returned host a bearer recipient; the healed value stays production. Only the
    inference override does, and scheme checks still apply to it."""
    monkeypatch.setenv("NASTECH_PORTAL_BASE_URL", NONPROD_PORTAL)
    monkeypatch.delenv("NASTECH_INFERENCE_BASE_URL", raising=False)
    state = {"portal_base_url": NONPROD_PORTAL, "inference_base_url": ENV_INFERENCE, "client_id": "cid"}
    portal, stored_inference, _effective, _ = auth_nastech._nastech_effective_routing(state)
    assert portal == NONPROD_PORTAL and stored_inference == auth_nastech.DEFAULT_NASTECH_INFERENCE_URL
    assert auth_nastech._healed_nastech_inference_url({"inference_base_url": ENV_INFERENCE}) == (
        auth_nastech.DEFAULT_NASTECH_INFERENCE_URL)
    monkeypatch.setenv("NASTECH_INFERENCE_BASE_URL", ENV_INFERENCE)
    assert auth_nastech._healed_nastech_inference_url({"inference_base_url": ENV_INFERENCE}) == ENV_INFERENCE
    assert auth_nastech._validate_nastech_inference_url_from_network(ENV_INFERENCE.replace("https", "http", 1)) is None


def test_recipient_match_follows_the_profile_scope_under_multiplex(monkeypatch):
    """The recipient is the routed profile's own override: a secondary without it refuses the
    host even when the launch profile's process env names it."""
    from agent import secret_scope as ss

    monkeypatch.setenv("NASTECH_INFERENCE_BASE_URL", ENV_INFERENCE)
    ss.set_multiplex_active(True)
    try:
        token = ss.set_secret_scope({})
        try:
            assert auth_nastech._validate_nastech_inference_url_from_network(ENV_INFERENCE) is None
        finally:
            ss.reset_secret_scope(token)
        token = ss.set_secret_scope({"NASTECH_INFERENCE_BASE_URL": ENV_INFERENCE})
        try:
            assert auth_nastech._validate_nastech_inference_url_from_network(ENV_INFERENCE) == ENV_INFERENCE
        finally:
            ss.reset_secret_scope(token)
    finally:
        ss.set_multiplex_active(False)
