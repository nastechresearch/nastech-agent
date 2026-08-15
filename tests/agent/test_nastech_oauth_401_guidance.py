"""Tests for the Nastech OAuth 401 actionable-guidance branch in
``agent.conversation_loop.run_conversation``.

Source-inspection style (matches ``test_gemini_fast_fallback.py``): we assert
that the guidance strings exist in the function body so that the user-facing
hint cannot be silently removed by a future refactor.

Regression context: ashh hit a Nastech 401 (OAuth token expired / portal said
account out of credits) plus a model slug ``deepseek/deepseek-v4-flash:free``
that's OpenRouter syntax, not a Nastech catalog name. The previous guidance
branch only covered ``openai-codex`` and ``xai-oauth``; ``nastech`` fell through
to a generic "Your API key was rejected... run nastech setup" message, which is
the wrong advice for a pure-OAuth provider.
"""
from __future__ import annotations

import inspect

from agent import conversation_loop


def test_nastech_provider_is_in_oauth_401_set():
    """The provider-set gate that selects OAuth-specific guidance must
    include ``nastech`` alongside ``openai-codex`` and ``xai-oauth``.
    """
    source = inspect.getsource(conversation_loop.run_conversation)

    # Be flexible about set element ordering — assert all three are listed
    # near each other in the gating expression.
    assert "\"openai-codex\"" in source
    assert "\"xai-oauth\"" in source
    assert "\"nastech\"" in source

    # And the gate string itself must mention all three so future refactors
    # that split nastech off into its own gate still get caught.
    needle = "_provider in {\"openai-codex\", \"xai-oauth\", \"nastech\"}"
    assert needle in source, (
        "Expected nastech to be co-gated with the other OAuth providers in the "
        "actionable-401-guidance branch of run_conversation."
    )


def test_nastech_401_guidance_strings_present():
    """User-facing remediation strings for Nastech OAuth 401s must exist."""
    source = inspect.getsource(conversation_loop.run_conversation)

    # Must tell the user it's an OAuth token problem, NOT an API key problem
    # (Nastech Portal has no API key path — auth_type=oauth_device_code only).
    assert "Nastech Portal OAuth token was rejected" in source

    # Must give a concrete re-auth command, not a generic "nastech setup".
    assert "nastech portal" in source

    # Must point at the portal so users can check account/credit status.
    assert "portal.nastechresearch.github.io" in source


