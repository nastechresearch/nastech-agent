"""Regression tests for dashboard basic-auth plugin enablement (#54489).

When ``dashboard.basic_auth`` is configured but the bundled ``basic``
provider plugin is listed in ``plugins.disabled``, plugin discovery skips
it and the dashboard auth gate sees zero providers — even after the
interactive username/password setup path writes credentials to config.yaml.
"""
from __future__ import annotations

from unittest.mock import patch

import pytest
import nastech_yaml as yaml

from nastech_cli.dashboard_auth import clear_providers, list_providers
from nastech_cli.plugins import PluginManager, discover_plugins
from nastech_cli.plugins_cmd import ensure_basic_auth_plugin_enabled_in_config
import plugins.dashboard_auth.basic as basic_plugin


@pytest.fixture(autouse=True)
def _reset_auth_registry():
    clear_providers()
    yield
    clear_providers()


@pytest.fixture
def nastech_home(tmp_path, monkeypatch):
    home = tmp_path / "nastech"
    home.mkdir()
    monkeypatch.setenv("NASTECH_HOME", str(home))
    return home


def _write_config(home, cfg: dict) -> None:
    (home / "config.yaml").write_text(yaml.safe_dump(cfg), encoding="utf-8")


class TestEnsureBasicAuthPluginEnabled:
    def test_noop_when_not_disabled(self):
        cfg = {"plugins": {"disabled": ["other-plugin"]}}
        assert ensure_basic_auth_plugin_enabled_in_config(cfg) is False


class TestBasicProviderLoadsAfterUnblock:
    def test_disabled_basic_blocks_registration(self, nastech_home, monkeypatch):
        password_hash = basic_plugin.hash_password("hunter2")
        _write_config(
            nastech_home,
            {
                "dashboard": {
                    "basic_auth": {
                        "username": "admin",
                        "password_hash": password_hash,
                        "secret": "a" * 32,
                    }
                },
                "plugins": {"disabled": ["basic"]},
            },
        )

        import nastech_cli.plugins as plugins_mod

        with patch.object(plugins_mod, "_plugin_manager", None):
            discover_plugins(force=True)

        assert list_providers() == []

    def test_unblock_then_rediscover_registers_provider(
        self, nastech_home, monkeypatch,
    ):
        password_hash = basic_plugin.hash_password("hunter2")
        cfg = {
            "dashboard": {
                "basic_auth": {
                    "username": "admin",
                    "password_hash": password_hash,
                    "secret": "a" * 32,
                }
            },
            "plugins": {"disabled": ["basic"]},
        }
        _write_config(nastech_home, cfg)

        assert ensure_basic_auth_plugin_enabled_in_config(cfg) is True
        _write_config(nastech_home, cfg)

        import nastech_cli.plugins as plugins_mod

        with patch.object(plugins_mod, "_plugin_manager", None):
            discover_plugins(force=True)

        providers = list_providers()
        assert len(providers) == 1
        assert providers[0].name == "basic"
