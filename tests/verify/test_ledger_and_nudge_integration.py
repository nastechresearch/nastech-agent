"""Integration of the verify subsystem with the existing verification stack.

Covers the closed loop the rescoped PR is about:

- ``nastech verify`` records into the evidence ledger (pass and fail),
- a passing run satisfies the verify-on-stop guard,
- the verify-on-stop nudge names ``nastech verify --json`` when the workspace
  has a runnable recipe (start command or saved manifest),
- the CLI's detect path merges ``detect_project_facts`` verify commands the
  recipe missed.
"""

import argparse
import json

import pytest

from agent.verification_evidence import (
    mark_workspace_edited,
    record_verify_run,
    verification_status,
)
from agent.verification_stop import build_verify_on_stop_nudge
from nastech_cli.verify_cmd import run_verify_command

@pytest.fixture(autouse=True)
def _ledger_on(monkeypatch):
    """The ledger is inert unless verify-on-stop is enabled; these tests exercise the ledger."""
    monkeypatch.setenv("NASTECH_VERIFY_ON_STOP", "1")



def make_args(path, **overrides):
    defaults = dict(
        path=str(path),
        detect_only=False,
        save=False,
        skip_start=False,
        phase=None,
        port=None,
        timeout=60.0,
        ready_timeout=5.0,
        json=True,
    )
    defaults.update(overrides)
    return argparse.Namespace(**defaults)


@pytest.fixture
def nastech_home(tmp_path, monkeypatch):
    monkeypatch.setenv("NASTECH_HOME", str(tmp_path / ".nastech-home"))
    monkeypatch.delenv("NASTECH_SESSION_ID", raising=False)
    return tmp_path


def _workspace(tmp_path, *, scripts=None, manifest_recipe=None):
    """A marker-rooted workspace (package.json) with an optional saved recipe."""
    project = tmp_path / "project"
    project.mkdir()
    (project / "package.json").write_text(
        json.dumps({"scripts": scripts} if scripts else {}), encoding="utf-8"
    )
    if manifest_recipe is not None:
        nastech_dir = project / ".nastech"
        nastech_dir.mkdir()
        (nastech_dir / "environment.json").write_text(
            json.dumps({"version": 1, "recipe": manifest_recipe}), encoding="utf-8"
        )
    return project


# ---------------------------------------------------------------------------
# ledger recording
# ---------------------------------------------------------------------------


def test_record_verify_run_marks_workspace_passed(nastech_home):
    project = _workspace(nastech_home)
    event = record_verify_run(root=project, session_id="s1", ok=True, output="all green")
    assert event is not None
    assert event["status"] == "passed"
    assert event["kind"] == "verify"
    status = verification_status(session_id="s1", cwd=project)
    assert status["status"] == "passed"
    assert status["evidence"]["canonical_command"] == "nastech verify"


def test_record_verify_run_records_failure(nastech_home):
    project = _workspace(nastech_home)
    record_verify_run(root=project, session_id="s1", ok=False, output="boom")
    status = verification_status(session_id="s1", cwd=project)
    assert status["status"] == "failed"


def test_cli_passing_run_writes_ledger_evidence(nastech_home, capsys):
    project = _workspace(nastech_home, manifest_recipe={"name": "Fake", "test": ["echo ok"]})
    code = run_verify_command(make_args(project))
    assert code == 0
    assert json.loads(capsys.readouterr().out)["ok"] is True
    status = verification_status(session_id=None, cwd=project)
    assert status["status"] == "passed"
    assert status["evidence"]["scope"] == "full"


def test_cli_failing_run_writes_failed_evidence(nastech_home, capsys):
    project = _workspace(nastech_home, manifest_recipe={"name": "Fake", "test": ["false"]})
    code = run_verify_command(make_args(project))
    assert code == 1
    status = verification_status(session_id=None, cwd=project)
    assert status["status"] == "failed"


def test_cli_partial_run_records_targeted_scope(nastech_home, capsys):
    # --skip-start / --phase subsets must never present as full workspace green.
    project = _workspace(nastech_home, manifest_recipe={"name": "Fake", "test": ["echo ok"]})
    code = run_verify_command(make_args(project, skip_start=True))
    assert code == 0
    status = verification_status(session_id=None, cwd=project)
    assert status["evidence"]["scope"] == "targeted"


def test_cli_run_uses_nastech_session_id_env(nastech_home, capsys, monkeypatch):
    monkeypatch.setenv("NASTECH_SESSION_ID", "sess-42")
    project = _workspace(nastech_home, manifest_recipe={"name": "Fake", "test": ["echo ok"]})
    run_verify_command(make_args(project))
    assert verification_status(session_id="sess-42", cwd=project)["status"] == "passed"


# ---------------------------------------------------------------------------
# closed loop: edit -> stop guard nudge -> nastech verify -> guard satisfied
# ---------------------------------------------------------------------------


def test_passing_verify_run_satisfies_stop_guard(nastech_home, capsys):
    project = _workspace(nastech_home, manifest_recipe={"name": "Fake", "test": ["echo ok"]})
    changed = str(project / "src" / "app.ts")
    mark_workspace_edited(session_id="default", cwd=project, paths=[changed])
    assert build_verify_on_stop_nudge(session_id="default", changed_paths=[changed]) is not None

    assert run_verify_command(make_args(project)) == 0

    assert build_verify_on_stop_nudge(session_id="default", changed_paths=[changed]) is None


# ---------------------------------------------------------------------------
# nudge wording: recipe-aware `nastech verify --json` suggestion
# ---------------------------------------------------------------------------


def test_nudge_mentions_nastech_verify_when_recipe_has_start(nastech_home):
    project = _workspace(nastech_home, scripts={"test": "vitest", "dev": "vite"})
    changed = str(project / "src" / "app.ts")
    mark_workspace_edited(session_id="s1", cwd=project, paths=[changed])
    nudge = build_verify_on_stop_nudge(session_id="s1", changed_paths=[changed])
    assert nudge is not None
    assert "nastech verify --json" in nudge
    # The cheap verify commands are still listed first.
    assert "npm run test" in nudge


def test_nudge_mentions_nastech_verify_when_manifest_exists(nastech_home):
    # No start script, but a saved .nastech/environment.json qualifies.
    project = _workspace(
        nastech_home,
        scripts={"test": "vitest"},
        manifest_recipe={"name": "Fake", "test": ["echo ok"]},
    )
    changed = str(project / "src" / "app.ts")
    mark_workspace_edited(session_id="s1", cwd=project, paths=[changed])
    nudge = build_verify_on_stop_nudge(session_id="s1", changed_paths=[changed])
    assert nudge is not None
    assert "nastech verify --json" in nudge


def test_nudge_keeps_plain_wording_without_recipe_start(nastech_home):
    # Verify commands but no start script and no manifest: today's wording.
    project = _workspace(nastech_home, scripts={"test": "vitest"})
    changed = str(project / "src" / "app.ts")
    mark_workspace_edited(session_id="s1", cwd=project, paths=[changed])
    nudge = build_verify_on_stop_nudge(session_id="s1", changed_paths=[changed])
    assert nudge is not None
    assert "nastech verify" not in nudge


def test_nudge_recipe_detection_failure_is_silent(nastech_home, monkeypatch):
    # A broken recipe detector must never break the nudge path.
    import agent.verify.recipes as recipes

    def boom(_root):
        raise RuntimeError("detector exploded")

    monkeypatch.setattr(recipes, "detect_recipe", boom)
    project = _workspace(nastech_home, scripts={"test": "vitest", "dev": "vite"})
    changed = str(project / "src" / "app.ts")
    mark_workspace_edited(session_id="s1", cwd=project, paths=[changed])
    nudge = build_verify_on_stop_nudge(session_id="s1", changed_paths=[changed])
    assert nudge is not None
    assert "nastech verify" not in nudge


# ---------------------------------------------------------------------------
# detection unification: project-facts commands merged into detected recipes
# ---------------------------------------------------------------------------


def test_detect_path_merges_project_facts_commands(nastech_home, capsys):
    project = _workspace(nastech_home)  # package.json with no scripts
    scripts_dir = project / "scripts"
    scripts_dir.mkdir()
    (scripts_dir / "run_tests.sh").write_text("#!/bin/sh\n", encoding="utf-8")
    (project / "pytest.ini").write_text("[pytest]\n", encoding="utf-8")

    code = run_verify_command(make_args(project, detect_only=True))
    assert code == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["source"] == "detected"
    tests = payload["recipe"]["test"]
    assert "scripts/run_tests.sh" in tests
    assert "pytest" in tests


def test_manifest_recipe_is_not_merged(nastech_home, capsys):
    # A saved manifest is the user-edited source of truth; leave it alone.
    project = _workspace(nastech_home, manifest_recipe={"name": "Fake", "test": ["echo ok"]})
    (project / "pytest.ini").write_text("[pytest]\n", encoding="utf-8")
    code = run_verify_command(make_args(project, detect_only=True))
    assert code == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["source"] == "manifest"
    assert payload["recipe"]["test"] == ["echo ok"]


def test_merge_skips_commands_recipe_already_has(nastech_home, capsys):
    project = _workspace(nastech_home, scripts={"test": "vitest"})
    code = run_verify_command(make_args(project, detect_only=True))
    assert code == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["recipe"]["test"].count("npm run test") == 1
