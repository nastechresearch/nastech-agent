"""``platform_toolsets`` rows for plugin platforms (teams, google_chat, homeassistant) that the installers
seeded from cli-config.yaml.example: inert until the plugin loads, so they must not log the #38798
"no valid toolsets" error, while a genuinely invalid row still does."""

import json
import logging

import pytest

# The rows cli-config.yaml.example seeded into every install (install.sh, install.ps1, the Docker hook,
# `nastech doctor --fix`), plus Home Assistant's from before it left core. None of these platforms is set up.
_SEEDED_ROWS = {
    "cli": ["nastech-cli"],
    "telegram": ["nastech-telegram"],
    "homeassistant": ["nastech-homeassistant"],
    "teams": ["nastech-teams"],
    "google_chat": ["nastech-google_chat"],
}


def _write_config(home, platform_toolsets):
    # JSON is valid YAML, and the CI test env has no pyyaml.
    (home / "config.yaml").write_text(json.dumps({"platform_toolsets": platform_toolsets}), encoding="utf-8")


def _toolset_errors(caplog):
    return [r.getMessage() for r in caplog.records if "#38798" in r.getMessage()]


@pytest.fixture(autouse=True)
def _fresh_warning_latch():
    import nastech_cli.tools_config as tc

    tc._warned_invalid_platform_toolsets.clear()
    yield
    tc._warned_invalid_platform_toolsets.clear()


def test_seeded_plugin_platform_rows_log_nothing_on_schema_build(caplog):
    """The kanban gate runs on every schema build and skills scan and resolves every saved row."""
    from nastech_constants import get_nastech_home
    from tools.kanban_tools import _profile_has_kanban_toolset

    _write_config(get_nastech_home(), _SEEDED_ROWS)
    with caplog.at_level(logging.WARNING, logger="nastech_cli.tools_config"):
        _profile_has_kanban_toolset()

    assert _toolset_errors(caplog) == []


def test_invalid_plugin_platform_row_still_warns(caplog):
    from nastech_constants import get_nastech_home
    from tools.kanban_tools import _profile_has_kanban_toolset

    _write_config(get_nastech_home(), {"cli": ["nastech-cli"], "teams": ["nastech-tems"]})
    with caplog.at_level(logging.WARNING, logger="nastech_cli.tools_config"):
        _profile_has_kanban_toolset()

    errors = _toolset_errors(caplog)
    assert len(errors) == 1 and "'teams'" in errors[0] and "nastech-tems" in errors[0], errors


def test_seeded_config_rows_need_no_plugin():
    """A config.yaml seeded the way the installers seed it names only toolsets that resolve without any
    plugin loaded: a plugin platform falls back to ``nastech-<platform>`` on its own."""
    from nastech_cli.config import read_raw_config, seed_config_file
    from nastech_constants import get_nastech_home
    from toolsets import validate_toolset

    assert seed_config_file(get_nastech_home() / "config.yaml") is True
    rows = read_raw_config().get("platform_toolsets") or {}
    unresolved = {p: names for p, names in rows.items() if not all(validate_toolset(n) for n in names)}
    assert unresolved == {}


def test_config_check_accepts_seeded_rows_of_uninstalled_plugin_platforms():
    """`nastech config check` and the update-time check judge the same rows the same way: Home Assistant's
    catalog plugin is not installed here, and its seeded row is inert, not an unknown toolset."""
    from nastech_cli.toolset_validation import saved_toolset_resolver, validate_platform_toolsets

    config = {"platform_toolsets": _SEEDED_ROWS}
    assert validate_platform_toolsets(_SEEDED_ROWS, saved_toolset_resolver(config)) == []

    typo = {"platform_toolsets": {"cli": ["nastech-cli"], "homeassistant": ["nastech-homeasistant"]}}
    warnings = validate_platform_toolsets(typo["platform_toolsets"], saved_toolset_resolver(typo))
    assert any("unknown toolset 'nastech-homeasistant'" in w for w in warnings), warnings


def test_misspelt_platform_key_naming_its_own_bundle_still_warns(caplog):
    """Only a KNOWN platform's own bundle is exempt: ``telegarm: [nastech-telegarm]`` is a typo of the key,
    and both the session-time check and `nastech config check` still report it."""
    from nastech_cli.tools_config import _get_platform_tools
    from nastech_cli.toolset_validation import saved_toolset_resolver, validate_platform_toolsets

    rows = {"cli": ["nastech-cli"], "telegarm": ["nastech-telegarm"]}
    config = {"platform_toolsets": rows}
    with caplog.at_level(logging.WARNING, logger="nastech_cli.tools_config"):
        _get_platform_tools(config, "telegarm")

    errors = _toolset_errors(caplog)
    assert len(errors) == 1 and "'telegarm'" in errors[0], errors
    warnings = validate_platform_toolsets(rows, saved_toolset_resolver(config))
    assert any("unknown toolset 'nastech-telegarm'" in w for w in warnings), warnings
