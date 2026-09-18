"""Tests for /tools slash command handler in the interactive CLI."""

from unittest.mock import MagicMock, patch

from cli import NastechCLI


def _make_cli(enabled_toolsets=None):
    """Build a minimal NastechCLI stub without running __init__."""
    cli_obj = NastechCLI.__new__(NastechCLI)
    cli_obj.enabled_toolsets = set(enabled_toolsets or ["web", "memory"])
    cli_obj._command_running = False
    cli_obj.console = MagicMock()
    return cli_obj


# ── /tools (no subcommand) ──────────────────────────────────────────────────


class TestToolsSlashNoSubcommand:

    def test_bare_tools_shows_tool_list(self):
        cli_obj = _make_cli()
        with patch.object(cli_obj, "show_tools") as mock_show:
            cli_obj._handle_tools_command("/tools")
        mock_show.assert_called_once()



# ── /tools list ─────────────────────────────────────────────────────────────


class TestToolsSlashList:

    def test_list_calls_backend(self, capsys):
        cli_obj = _make_cli()
        with patch("nastech_cli.tools_config.load_config",
                   return_value={"platform_toolsets": {"cli": ["web"]}}), \
             patch("nastech_cli.tools_config.save_config"):
            cli_obj._handle_tools_command("/tools list")
        out = capsys.readouterr().out
        assert "web" in out



# ── /tools disable (session reset) ──────────────────────────────────────────


class TestToolsSlashDisableWithReset:

    def test_disable_applies_directly_and_resets_session(self):
        """Disable applies immediately (no confirmation prompt) and resets session."""
        cli_obj = _make_cli(["web", "memory"])
        with patch("nastech_cli.tools_config.load_config",
                   return_value={"platform_toolsets": {"cli": ["web", "memory"]}}), \
             patch("nastech_cli.tools_config.save_config"), \
             patch("nastech_cli.tools_config._get_platform_tools", return_value={"memory"}), \
             patch("nastech_cli.config.load_config", return_value={}), \
             patch.object(cli_obj, "new_session") as mock_reset:
            cli_obj._handle_tools_command("/tools disable web")
        mock_reset.assert_called_once()
        assert "web" not in cli_obj.enabled_toolsets


    def test_disable_always_resets_session(self):
        """Even without a confirmation prompt, disable always resets the session."""
        cli_obj = _make_cli(["web", "memory"])
        with patch("nastech_cli.tools_config.load_config",
                   return_value={"platform_toolsets": {"cli": ["web", "memory"]}}), \
             patch("nastech_cli.tools_config.save_config"), \
             patch("nastech_cli.tools_config._get_platform_tools", return_value={"memory"}), \
             patch("nastech_cli.config.load_config", return_value={}), \
             patch.object(cli_obj, "new_session") as mock_reset:
            cli_obj._handle_tools_command("/tools disable web")
        mock_reset.assert_called_once()



# ── /tools enable (session reset) ───────────────────────────────────────────


class TestToolsSlashEnableWithReset:

    def test_enable_applies_directly_and_resets_session(self):
        """Enable applies immediately (no confirmation prompt) and resets session."""
        cli_obj = _make_cli(["memory"])
        with patch("nastech_cli.tools_config.load_config",
                   return_value={"platform_toolsets": {"cli": ["memory"]}}), \
             patch("nastech_cli.tools_config.save_config"), \
             patch("nastech_cli.tools_config._get_platform_tools", return_value={"memory", "web"}), \
             patch("nastech_cli.config.load_config", return_value={}), \
             patch.object(cli_obj, "new_session") as mock_reset:
            cli_obj._handle_tools_command("/tools enable web")
        mock_reset.assert_called_once()
        assert "web" in cli_obj.enabled_toolsets

    def test_enable_missing_name_prints_usage(self, capsys):
        cli_obj = _make_cli()
        cli_obj._handle_tools_command("/tools enable")
        out = capsys.readouterr().out
        assert "Usage" in out
