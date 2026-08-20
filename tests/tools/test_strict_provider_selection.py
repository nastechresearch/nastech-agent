"""Strict tool-provider selection: the `nastech tools` choice always wins.

Policy (owner decision): the provider string stored in config.yaml is what
runs at call time. "nastech" → managed Nastech Tool Gateway only; a vendor name →
that vendor direct with the user's own credentials; no key ever written →
today's credential autodetect. Credential presence must NEVER select or
reroute; a selected-but-broken provider produces an honest error naming the
selection and pointing at `nastech tools`.

Per category these tests pin the three strict behaviors:
  (a) managed selection + direct key present ⇒ managed route (key ignored)
  (b) vendor selection + key missing ⇒ selection-naming error, NO managed call
  (c) never-configured ⇒ legacy autodetect unchanged
"""

from types import SimpleNamespace
from unittest.mock import patch

import pytest

from tools import tool_backend_helpers as tbh


MANAGED = SimpleNamespace(
    nastech_user_token="managed-token",
    gateway_origin="https://gateway.nastechresearch.github.io",
)


# ---------------------------------------------------------------------------
# read_selection — the shared helper
# ---------------------------------------------------------------------------


class TestReadSelection:
    def _with_raw(self, raw):
        return patch(
            "nastech_cli.config.read_raw_config_readonly",
            return_value=raw,
        )

    def test_never_configured_returns_none(self):
        with self._with_raw({}):
            assert tbh.read_selection("image_gen") is None

    def test_vendor_provider_returned(self):
        with self._with_raw({"image_gen": {"provider": "fal"}}):
            assert tbh.read_selection("image_gen") == "fal"

    def test_nastech_provider_returned(self):
        with self._with_raw({"image_gen": {"provider": "nastech"}}):
            assert tbh.read_selection("image_gen") == "nastech"

    def test_legacy_use_gateway_true_maps_to_nastech(self):
        """Old configs stored use_gateway: true beside a vendor name — only
        the managed picker row ever wrote it, so it means 'nastech'."""
        with self._with_raw({"video_gen": {"provider": "fal", "use_gateway": True}}):
            assert tbh.read_selection("video_gen") == "nastech"

    def test_legacy_use_gateway_false_keeps_vendor(self):
        with self._with_raw({"tts": {"provider": "openai", "use_gateway": False}}):
            assert tbh.read_selection("tts") == "openai"

    def test_empty_string_backend_is_no_selection(self):
        """DEFAULT_CONFIG's seeded empty strings are not selections."""
        with self._with_raw({"web": {"backend": ""}}):
            assert tbh.read_selection("web") is None

    def test_raw_stt_local_is_a_selection(self):
        """A raw config.yaml ``stt.provider: local`` is a genuine pick: the
        DEFAULT_CONFIG seed never reached disk (save_config strips schema
        defaults), and the current picker's Local Whisper row writes exactly
        this shape (provider only, legacy use_gateway popped). Treating it
        as no-selection would silently discard the user's choice."""
        with self._with_raw({"stt": {"provider": "local"}}):
            assert tbh.read_selection("stt") == "local"

    def test_stt_local_with_use_gateway_key_is_a_selection(self):
        """A picker-written stt section (use_gateway key present) means
        local was a genuine choice."""
        with self._with_raw({"stt": {"provider": "local", "use_gateway": False}}):
            assert tbh.read_selection("stt") == "local"

    def test_browser_backend_key_is_not_the_cloud_selection(self):
        """browser.backend is the driver choice (browser-use CLI vs built-in
        tools), not the cloud provider selection."""
        with self._with_raw({"browser": {"backend": "browser-use"}}):
            assert tbh.read_selection("browser") is None

    def test_web_per_capability_keys_mark_configured(self):
        with self._with_raw({"web": {"search_backend": "searxng"}}):
            assert tbh.read_selection("web") is None
            assert tbh.selection_exists("web") is True


# ---------------------------------------------------------------------------
# Image generation (FAL)
# ---------------------------------------------------------------------------


class TestImageFalStrictSelection:
    def test_nastech_selection_routes_managed_even_with_fal_key(self):
        from tools import image_generation_tool as it

        with patch.object(it, "read_selection", return_value="nastech"), \
             patch.object(it, "fal_key_is_configured", return_value=True), \
             patch.object(it, "resolve_managed_tool_gateway", return_value=MANAGED) as gw:
            assert it._resolve_managed_fal_gateway() is MANAGED
        gw.assert_called_once_with("fal-queue")

    def test_nastech_selection_unentitled_raises_selection_error(self):
        from tools import image_generation_tool as it

        with patch.object(it, "read_selection", return_value="nastech"), \
             patch.object(it, "fal_key_is_configured", return_value=True), \
             patch.object(it, "resolve_managed_tool_gateway", return_value=None):
            with pytest.raises(ValueError) as exc:
                it._resolve_managed_fal_gateway()
        assert "image_gen is configured to use nastech" in str(exc.value)
        assert "nastech tools" in str(exc.value)

    def test_fal_selection_missing_key_errors_without_managed_call(self):
        from tools import image_generation_tool as it

        with patch.object(it, "read_selection", return_value="fal"), \
             patch.object(it, "fal_key_is_configured", return_value=False), \
             patch.object(it, "resolve_managed_tool_gateway") as gw:
            with pytest.raises(ValueError) as exc:
                it._resolve_managed_fal_gateway()
        gw.assert_not_called()
        assert "FAL_KEY" in str(exc.value)
        assert "image_gen is configured to use fal" in str(exc.value)
        assert "nastech tools" in str(exc.value)

    def test_fal_selection_with_key_routes_direct(self):
        from tools import image_generation_tool as it

        with patch.object(it, "read_selection", return_value="fal"), \
             patch.object(it, "fal_key_is_configured", return_value=True), \
             patch.object(it, "resolve_managed_tool_gateway") as gw:
            assert it._resolve_managed_fal_gateway() is None
        gw.assert_not_called()

    def test_never_configured_autodetect_direct_when_key_present(self):
        from tools import image_generation_tool as it

        with patch.object(it, "read_selection", return_value=None), \
             patch.object(it, "fal_key_is_configured", return_value=True):
            assert it._resolve_managed_fal_gateway() is None

    def test_never_configured_autodetect_managed_when_no_key(self):
        from tools import image_generation_tool as it

        with patch.object(it, "read_selection", return_value=None), \
             patch.object(it, "fal_key_is_configured", return_value=False), \
             patch.object(it, "resolve_managed_tool_gateway", return_value=MANAGED):
            assert it._resolve_managed_fal_gateway() is MANAGED

    def test_check_fal_api_key_reflects_selection(self):
        from tools import image_generation_tool as it

        with patch.object(it, "read_selection", return_value="fal"), \
             patch.object(it, "fal_key_is_configured", return_value=False), \
             patch.object(it, "resolve_managed_tool_gateway", return_value=MANAGED):
            # Broken vendor selection reports unavailable even though the
            # managed gateway would resolve.
            assert it.check_fal_api_key() is False


# ---------------------------------------------------------------------------
# Video generation (FAL plugin)
# ---------------------------------------------------------------------------


class TestVideoFalStrictSelection:
    def test_nastech_selection_routes_managed_even_with_fal_key(self):
        from plugins.video_gen import fal as vf

        with patch("tools.tool_backend_helpers.read_selection", return_value="nastech"), \
             patch("tools.tool_backend_helpers.fal_key_is_configured", return_value=True), \
             patch("tools.managed_tool_gateway.resolve_managed_tool_gateway", return_value=MANAGED):
            assert vf._resolve_managed_fal_video_gateway() is MANAGED

    def test_fal_selection_missing_key_errors_without_managed_call(self):
        from plugins.video_gen import fal as vf

        with patch("tools.tool_backend_helpers.read_selection", return_value="fal"), \
             patch("tools.tool_backend_helpers.fal_key_is_configured", return_value=False), \
             patch("tools.managed_tool_gateway.resolve_managed_tool_gateway") as gw:
            with pytest.raises(ValueError) as exc:
                vf._resolve_managed_fal_video_gateway()
        gw.assert_not_called()
        assert "video_gen is configured to use fal" in str(exc.value)
        assert "FAL_KEY" in str(exc.value)

    def test_never_configured_autodetect_unchanged(self):
        from plugins.video_gen import fal as vf

        with patch("tools.tool_backend_helpers.read_selection", return_value=None), \
             patch("tools.tool_backend_helpers.fal_key_is_configured", return_value=True):
            assert vf._resolve_managed_fal_video_gateway() is None


# ---------------------------------------------------------------------------
# STT (OpenAI audio resolver — previously ignored the stored intent entirely)
# ---------------------------------------------------------------------------


class TestSttStrictSelection:
    def test_nastech_selection_beats_direct_openai_key(self):
        from tools import transcription_tools as tt

        with patch.object(tt, "_load_stt_config", return_value={"openai": {"api_key": "sk-direct"}}), \
             patch("tools.tool_backend_helpers.read_selection", return_value="nastech"), \
             patch.object(tt, "resolve_managed_tool_gateway", return_value=MANAGED):
            api_key, base_url = tt._resolve_openai_audio_client_config()
        assert api_key == "managed-token"
        assert base_url.startswith("https://gateway.nastechresearch.github.io")

    def test_vendor_selection_missing_key_errors_without_managed_call(self):
        from tools import transcription_tools as tt

        with patch.object(tt, "_load_stt_config", return_value={}), \
             patch("tools.tool_backend_helpers.read_selection", return_value="openai"), \
             patch.object(tt, "resolve_openai_audio_api_key", return_value=""), \
             patch.object(tt, "resolve_managed_tool_gateway") as gw:
            with pytest.raises(ValueError) as exc:
                tt._resolve_openai_audio_client_config()
        gw.assert_not_called()
        assert "stt is configured to use openai" in str(exc.value)
        assert "nastech tools" in str(exc.value)

    def test_never_configured_keeps_legacy_ladder(self):
        from tools import transcription_tools as tt

        with patch.object(tt, "_load_stt_config", return_value={}), \
             patch("tools.tool_backend_helpers.read_selection", return_value=None), \
             patch.object(tt, "resolve_openai_audio_api_key", return_value="sk-env"):
            api_key, base_url = tt._resolve_openai_audio_client_config()
        assert api_key == "sk-env"


# ---------------------------------------------------------------------------
# Browser Use provider
# ---------------------------------------------------------------------------


class TestBrowserUseStrictSelection:
    def _provider(self):
        from plugins.browser.browser_use.provider import BrowserUseBrowserProvider

        return BrowserUseBrowserProvider()

    def test_nastech_selection_routes_managed_even_with_direct_key(self):
        provider = self._provider()
        with patch("plugins.browser.browser_use.provider.get_secret", return_value="bu-key"), \
             patch("tools.tool_backend_helpers.read_selection", return_value="nastech"), \
             patch("tools.managed_tool_gateway.resolve_managed_tool_gateway", return_value=MANAGED):
            config = provider._get_config_or_none()
        assert config["managed_mode"] is True
        assert config["api_key"] == "managed-token"

    def test_vendor_selection_missing_key_errors_without_managed_call(self):
        provider = self._provider()
        with patch("plugins.browser.browser_use.provider.get_secret", return_value=""), \
             patch("tools.tool_backend_helpers.read_selection", return_value="browser-use"), \
             patch("tools.managed_tool_gateway.resolve_managed_tool_gateway") as gw:
            with pytest.raises(ValueError) as exc:
                provider._get_config()
        gw.assert_not_called()
        assert "browser is configured to use browser-use" in str(exc.value)
        assert "BROWSER_USE_API_KEY" in str(exc.value)

    def test_never_configured_key_still_routes_direct(self):
        provider = self._provider()
        with patch("plugins.browser.browser_use.provider.get_secret", return_value="bu-key"), \
             patch("tools.tool_backend_helpers.read_selection", return_value=None):
            config = provider._get_config_or_none()
        assert config["managed_mode"] is False
        assert config["api_key"] == "bu-key"


# ---------------------------------------------------------------------------
# Camofox: selection over env var
# ---------------------------------------------------------------------------


class TestCamofoxSelection:
    def test_camofox_selection_activates_mode(self, monkeypatch):
        from tools import browser_camofox as bc

        monkeypatch.delenv("BROWSER_CDP_URL", raising=False)
        with patch.object(bc, "_config_cdp_url", return_value=""), \
             patch("tools.tool_backend_helpers.read_selection", return_value="camofox"):
            assert bc.is_camofox_mode() is True

    def test_other_selection_beats_camofox_url_env(self, monkeypatch):
        """CAMOFOX_URL is the ADDRESS, not the choice: an explicit different
        browser selection wins."""
        from tools import browser_camofox as bc

        monkeypatch.delenv("BROWSER_CDP_URL", raising=False)
        with patch.object(bc, "_config_cdp_url", return_value=""), \
             patch.object(bc, "get_camofox_url", return_value="http://localhost:9377"), \
             patch("tools.tool_backend_helpers.read_selection", return_value="local"):
            assert bc.is_camofox_mode() is False

    def test_never_configured_env_url_still_activates(self, monkeypatch):
        from tools import browser_camofox as bc

        monkeypatch.delenv("BROWSER_CDP_URL", raising=False)
        with patch.object(bc, "_config_cdp_url", return_value=""), \
             patch.object(bc, "get_camofox_url", return_value="http://localhost:9377"), \
             patch("tools.tool_backend_helpers.read_selection", return_value=None):
            assert bc.is_camofox_mode() is True


# ---------------------------------------------------------------------------
# tools_config writers: one provider string per row, no use_gateway writes
# ---------------------------------------------------------------------------


class TestWriteProviderConfig:
    def test_managed_row_writes_nastech_and_clears_legacy_flag(self):
        from nastech_cli.tools_config import _write_provider_config

        config = {"tts": {"provider": "edge", "use_gateway": False}}
        provider = {"name": "Nastech Subscription", "tts_provider": "openai"}
        _write_provider_config(provider, config, managed_feature="tts")
        assert config["tts"]["provider"] == "nastech"
        assert "use_gateway" not in config["tts"]

    def test_byok_row_writes_vendor_and_clears_legacy_flag(self):
        from nastech_cli.tools_config import _write_provider_config

        config = {"web": {"backend": "nastech", "use_gateway": True}}
        provider = {"name": "Tavily", "web_backend": "tavily"}
        _write_provider_config(provider, config, managed_feature=None)
        assert config["web"]["backend"] == "tavily"
        assert "use_gateway" not in config["web"]

    def test_managed_image_row_persists_nastech_provider(self):
        from nastech_cli.tools_config import _write_provider_config

        config = {}
        provider = {"name": "Nastech Subscription", "imagegen_backend": "fal"}
        _write_provider_config(provider, config, managed_feature="image_gen")
        assert config["image_gen"]["provider"] == "nastech"
        assert "use_gateway" not in config["image_gen"]

    def test_plugin_injected_byok_row_clears_stale_use_gateway(self):
        """Plugin-injected rows are not in TOOL_CATEGORIES' hardcoded
        provider lists; the legacy clear-loop skipped them."""
        from nastech_cli.tools_config import _write_provider_config

        config = {"stt": {"provider": "nastech", "use_gateway": True}}
        provider = {"name": "Groq Whisper", "stt_provider": "groq"}
        _write_provider_config(provider, config, managed_feature=None)
        assert config["stt"]["provider"] == "groq"
        assert "use_gateway" not in config["stt"]
