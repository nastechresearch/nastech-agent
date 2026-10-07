"""``nastech.anthropic_wire`` selects the Portal route for ``anthropic/*``: ``chat`` (default) rides
/v1/chat/completions, ``native`` rides /v1/messages. Read through the real config loader against a
temp NASTECH_HOME (the loader is keyed on config path + mtime, so a fresh home is a fresh read), and
through ``resolve_runtime_provider`` so the api_mode a live agent gets is what is asserted."""
from __future__ import annotations

import pytest

from nastech_cli import providers as _providers
from nastech_cli import runtime_provider as rp

PORTAL = "https://inference-api.nastechresearch.github.io/v1"


def _cfg(tmp_path, body: str, monkeypatch):
    monkeypatch.setenv("NASTECH_HOME", str(tmp_path))
    (tmp_path / "config.yaml").write_text(body, encoding="utf-8")


def _portal_creds(monkeypatch):
    monkeypatch.setattr(rp, "resolve_nastech_runtime_credentials",
                        lambda **kw: {"base_url": PORTAL, "api_key": "jwt", "source": "portal", "expires_at": None})
    monkeypatch.setattr(rp, "_get_model_config", lambda: {"provider": "nastech"})


def test_default_is_chat_for_anthropic_and_unchanged_for_everything_else(tmp_path, monkeypatch):
    _cfg(tmp_path, "model:\n  default: anthropic/claude-fable-5.1\n", monkeypatch)
    assert _providers.nastech_api_mode("anthropic/claude-fable-5.1") == "chat_completions"
    assert _providers.nastech_api_mode("openai/gpt-5.6-sol") == "chat_completions"
    assert _providers.determine_api_mode("nastech", PORTAL, "anthropic/claude-fable-5.1") == "chat_completions"


def test_native_opt_in_restores_the_messages_wire_for_anthropic_only(tmp_path, monkeypatch):
    _cfg(tmp_path, "nastech:\n  anthropic_wire: native\n", monkeypatch)
    assert _providers.nastech_api_mode("anthropic/claude-fable-5.1") == "anthropic_messages"
    assert _providers.nastech_api_mode("openai/gpt-5.6-sol") == "chat_completions"


@pytest.mark.parametrize("raw", ["''", "CHAT", "messages", "true", "1"])
def test_anything_but_native_reads_as_chat(tmp_path, monkeypatch, raw):
    _cfg(tmp_path, f"nastech:\n  anthropic_wire: {raw}\n", monkeypatch)
    assert _providers.nastech_api_mode("anthropic/claude-fable-5.1") == "chat_completions"


def test_runtime_resolution_hands_a_live_agent_the_selected_wire(tmp_path, monkeypatch):
    """The path an AIAgent takes: provider=nastech + anthropic model -> api_mode, both settings."""
    _portal_creds(monkeypatch)
    _cfg(tmp_path, "model:\n  provider: nastech\n", monkeypatch)
    resolved = rp.resolve_runtime_provider(requested="nastech", target_model="anthropic/claude-fable-5.1")
    assert (resolved["api_mode"], resolved["base_url"]) == ("chat_completions", PORTAL)

    _cfg(tmp_path, "model:\n  provider: nastech\nnastech:\n  anthropic_wire: native\n", monkeypatch)
    resolved = rp.resolve_runtime_provider(requested="nastech", target_model="anthropic/claude-fable-5.1")
    assert resolved["api_mode"] == "anthropic_messages"
