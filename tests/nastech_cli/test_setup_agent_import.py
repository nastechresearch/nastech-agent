"""`nastech setup`'s "Coming from another agent?" step: it offers only the agents found on disk, installs
the agent-importers plugin through the catalog install only after a yes, then runs that plugin's
import for each pick.

Real step code, a temp NASTECH_HOME and a fake HOME; the terminal prompts, the catalog install (network)
and the child `nastech import-agent` process are stand-ins that record what the step asked for.
"""

from __future__ import annotations

import subprocess

import pytest

from nastech_cli import setup_agent_import as step
from nastech_cli.setup import prompt_yes_no as real_prompt_yes_no


@pytest.fixture
def homes(tmp_path, monkeypatch):
    user_home, nastech_home = tmp_path / "user", tmp_path / "user" / ".nastech"
    nastech_home.mkdir(parents=True)
    for var in ("HOME", "USERPROFILE"):
        monkeypatch.setenv(var, str(user_home))
    monkeypatch.setenv("NASTECH_HOME", str(nastech_home))
    monkeypatch.delenv("NASTECH_NONINTERACTIVE", raising=False)
    calls: list = []
    answers = {"yes": True, "unpick": set()}

    def ask(question, default=True, description=None):
        calls.append(("ask", question, default))
        return answers["yes"]

    def checklist(title, items, pre_selected):
        calls.append(("pick", list(items), list(pre_selected)))
        return [i for i in pre_selected if items[i] not in answers["unpick"]]

    def install(name, enable=None, brief=False, **_):
        calls.append(("install", name, enable, brief))
        (nastech_home / "plugins" / name).mkdir(parents=True)

    def run(argv, env, check=False):
        nastech_args = argv[argv.index("nastech_cli.main") + 1:]
        calls.append(("import", nastech_args, env["NASTECH_HOME"]))
        (nastech_home / "config.yaml").write_text(f"imported: {nastech_args[-1]}\n", encoding="utf-8")
        return subprocess.CompletedProcess(argv, 0)

    monkeypatch.setattr("nastech_cli.setup.prompt_yes_no", ask)
    monkeypatch.setattr("nastech_cli.setup.prompt_checklist", checklist)
    monkeypatch.setattr("nastech_cli.plugins_cmd_install.cmd_install", install)
    monkeypatch.setattr(step.subprocess, "run", run)
    return user_home, nastech_home, calls, answers


def test_found_agent_is_offered_then_installed_from_the_catalog_and_imported(homes):
    user_home, nastech_home, calls, _answers = homes
    (user_home / ".openclaw").mkdir()

    assert step.offer_agent_import(nastech_home) == "OpenClaw"

    assert calls == [
        ("ask", "Import your setup from OpenClaw?", True),
        ("install", "agent-importers", True, True),
        # core's setup migrated OpenClaw's allowlisted secrets after the preview; so does this step.
        # The root home is named explicitly, so a sticky active_profile cannot redirect the child.
        # --from-setup: the plugin words its preview and result as a step of this setup.
        ("import", ["--profile", "default", "import-agent", "openclaw", "--migrate-secrets", "--from-setup"],
         str(nastech_home)),
    ]


def test_several_found_are_offered_as_a_checklist_and_only_the_picks_import(homes):
    user_home, nastech_home, calls, answers = homes
    for d in (".claude", ".cursor"):
        (user_home / d).mkdir()
    answers["unpick"] = {"Cursor"}

    assert step.offer_agent_import(nastech_home) == "Claude Code"

    assert calls[1] == ("pick", ["Claude Code", "Cursor"], [0, 1])  # never an agent that is absent
    assert calls[2:] == [("install", "agent-importers", True, True),
                         ("import", ["--profile", "default", "import-agent", "claude-code", "--from-setup"],
                          str(nastech_home))]


def test_declining_installs_nothing(homes):
    user_home, nastech_home, calls, answers = homes
    (user_home / ".codex").mkdir()
    answers["yes"] = False

    assert step.offer_agent_import(nastech_home) == ""

    assert calls == [("ask", "Import your setup from Codex CLI?", True)]
    assert not (nastech_home / "plugins").exists()


@pytest.mark.parametrize("headless", [True, False])
def test_headless_or_nothing_found_asks_nothing(headless, homes, monkeypatch):
    user_home, nastech_home, calls, _answers = homes
    if headless:  # dashboard/Desktop-spawned setup: no one can answer
        (user_home / ".claude").mkdir()
        monkeypatch.setenv("NASTECH_NONINTERACTIVE", "1")

    assert step.offer_agent_import(nastech_home) == ""

    assert calls == []
    assert not (nastech_home / "plugins").exists()


def test_a_refused_enable_skips_the_import_and_setup_goes_on(homes, monkeypatch):
    """Installed but disabled, and PM cannot admit the enable: the error is printed, nothing is
    imported, and the step returns so the rest of setup still runs."""
    from nastech_cli.plugins_admission import AdmissionRefused
    user_home, nastech_home, calls, _answers = homes
    (user_home / ".cursor").mkdir()
    (nastech_home / "plugins" / "agent-importers").mkdir(parents=True)

    def refuse(name, **_):
        calls.append(("enable", name))
        raise AdmissionRefused("dependency conflict")
    monkeypatch.setattr("nastech_cli.plugins_cmd.cmd_enable", refuse)

    assert step.offer_agent_import(nastech_home) == ""

    assert calls == [("ask", "Import your setup from Cursor?", True), ("enable", "agent-importers")]


def test_setup_menu_shows_what_was_found_with_the_question(homes, monkeypatch):
    """Setup's yes/no is a full-screen menu that hides what was printed before it, so the detection
    lines travel with the question: "any of them" must point at text the user can see."""
    from nastech_cli import setup
    user_home, nastech_home, calls, _answers = homes
    for d in (".openclaw", ".claude", ".codex"):
        (user_home / d).mkdir()
    menus = []

    def radiolist(title, items, selected=0, *, description=None, **_):
        menus.append((title, items, description))
        return 1  # "No"
    monkeypatch.setattr("nastech_cli.setup.prompt_yes_no", real_prompt_yes_no)
    monkeypatch.setattr("nastech_cli.curses_ui.curses_radiolist", radiolist)

    with setup._setup_navigation_scope():
        assert step.offer_agent_import(nastech_home) == ""

    [(title, items, description)] = menus
    assert (title, items) == ("Import your setup from any of them?", ["Yes", "No"])
    assert ("Found on this computer: OpenClaw (~/.openclaw), Claude Code (~/.claude), Codex CLI (~/.codex)."
            in " ".join(description.split()))
    assert calls == [] and not (nastech_home / "plugins").exists()


def test_grok_bot_export_in_downloads_is_offered_like_the_other_agents(homes):
    """Grok Bot keeps its setup in the cloud: an export the Bot wrote, saved to Downloads, is enough
    for setup to offer the import."""
    user_home, nastech_home, calls, _answers = homes
    (user_home / "Downloads").mkdir()
    (user_home / "Downloads" / "grok-bot-export.json").write_text("{}", encoding="utf-8")

    assert step.offer_agent_import(nastech_home) == "Grok Bot"
    assert calls[-1] == ("import", ["--profile", "default", "import-agent", "grok-bot", "--from-setup"],
                         str(nastech_home))


def test_nastech_migrate_names_an_agent_installs_the_plugin_and_forwards_its_flags(homes, monkeypatch):
    """`nastech migrate grok-bot ...` through the real parser: the plugin is installed from the catalog
    when missing, and the import runs as its own command (no --from-setup) with the user's flags."""
    import argparse

    from nastech_cli.subcommands.migrate import build_migrate_parser
    user_home, nastech_home, calls, _answers = homes
    parser = argparse.ArgumentParser()
    build_migrate_parser(parser.add_subparsers(dest="command"))
    args = parser.parse_args(["migrate", "grok-bot", "--source", "~/export.json", "--activate-routines",
                              "--bot", "Scout", "-y"])

    assert args.func(args) == 0
    assert calls == [
        ("install", "agent-importers", True, True),
        ("import", ["--profile", "default", "import-agent", "grok-bot", "--yes", "--activate-routines",
                    "--source", str(user_home / "export.json"), "--bot", "Scout"], str(nastech_home)),
    ]
    # Setup imports OpenClaw's secrets (its old step did); `nastech migrate openclaw` only on request.
    calls.clear()
    monkeypatch.setattr(step, "_ensure_plugin", lambda home: True)
    openclaw = parser.parse_args(["migrate", "openclaw", "-y"])
    assert openclaw.func(openclaw) == 0
    assert calls[-1][1] == ["--profile", "default", "import-agent", "openclaw", "--yes"]
    # A failed import fails the command, so `nastech migrate x && ...` stops there.
    monkeypatch.setattr(step.subprocess, "run", lambda argv, env, check=False: subprocess.CompletedProcess(argv, 1))
    assert args.func(args) == 1
