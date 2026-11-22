"""First-run ``nastech setup`` after an agent import: a model the import brought is offered first and
kept by default, instead of being replaced by a sign-in step."""

from argparse import Namespace
from unittest.mock import patch

import pytest


def _fake_import(_nastech_home):
    """What an agent import leaves behind: a model in config.yaml and its key in .env."""
    from nastech_cli.config import load_config, save_config, save_env_value
    config = load_config()
    config["model"] = {"provider": "openrouter", "default": "anthropic/claude-sonnet-4.5"}
    save_config(config)
    save_env_value("OPENROUTER_API_KEY", "sk-or-demo-not-a-real-key")
    return "OpenClaw"


def _fake_nastech_flow(config):
    """The real flow logs in and saves provider ``nastech`` with a Portal model."""
    from nastech_cli.config import save_config
    config["model"] = {"provider": "nastech", "default": "Nastech-4-405B"}
    save_config(config)


@pytest.mark.parametrize("pick_portal, nastech_runs, expected_model", [
    (False, 0, {"provider": "openrouter", "default": "anthropic/claude-sonnet-4.5"}),
    (True, 1, {"provider": "nastech", "default": "Nastech-4-405B"}),
])
def test_first_run_keeps_imported_model_unless_user_picks_another(pick_portal, nastech_runs, expected_model):
    from nastech_cli.config import get_env_value, load_config
    from nastech_cli.setup import run_setup_wizard

    menus = []

    def answer(question, choices, default=0, description=None):
        menus.append((question, list(choices)))
        if pick_portal:
            return next(i for i, c in enumerate(choices) if c.startswith("Sign in to Nastech Portal"))
        return default

    with patch("nastech_cli.setup.is_interactive_stdin", return_value=True), \
            patch("nastech_cli.setup.offer_agent_import", side_effect=_fake_import), \
            patch("nastech_cli.setup.prompt_choice", side_effect=answer), \
            patch("nastech_cli.model_setup_flows._model_flow_nastech", side_effect=_fake_nastech_flow) as nastech, \
            patch("nastech_cli.setup.setup_terminal_backend") as terminal, \
            patch("nastech_cli.setup.setup_gateway") as gateway, \
            patch("nastech_cli.setup._record_setup_completed"):
        run_setup_wizard(Namespace(non_interactive=False, section=None, reset=False,
                                   reconfigure=False, quick=False))

    assert nastech.call_count == nastech_runs
    model = load_config()["model"]
    assert {k: model.get(k) for k in expected_model} == expected_model
    assert get_env_value("OPENROUTER_API_KEY") == "sk-or-demo-not-a-real-key"
    # One question: the first row keeps the import; no terminal or messaging screens follow.
    assert len(menus) == 1 and menus[0][0] == "How do you want to power Nastech?"
    assert menus[0][1][0] == "Keep my imported model (OpenRouter · anthropic/claude-sonnet-4.5)"
    terminal.assert_not_called()
    gateway.assert_not_called()
