"""Exercise updater archaeology against real Git DAGs, not today's filenames."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest


@pytest.fixture
def audit(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location(
        "audit_old_updater_history_tests",
        Path(__file__).resolve().parents[1] / "scripts/audit-old-updater-imports.py",
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    monkeypatch.setitem(sys.modules, spec.name, module)
    spec.loader.exec_module(module)
    monkeypatch.setattr(module, "REPO_ROOT", tmp_path)
    git(tmp_path, "init", "-b", "main")
    git(tmp_path, "config", "user.name", "Audit Test")
    git(tmp_path, "config", "user.email", "audit@example.invalid")
    git(tmp_path, "config", "commit.gpgsign", "false")
    return module


def git(root, *args):
    return subprocess.run(
        ["git", *args], cwd=root, capture_output=True, text=True, check=True
    ).stdout.strip()


def put(root, path, source):
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source, encoding="utf-8")


def commit(root, message):
    git(root, "add", ".")
    git(root, "commit", "-m", message)
    sha = git(root, "rev-parse", "HEAD")
    git(root, "update-ref", "refs/remotes/origin/main", sha)
    return sha


def test_discovers_entrypoint_renames_extractions_and_deleted_helpers(audit):
    root = audit.REPO_ROOT
    put(root, "nastech_cli/ancient.py", "def cmd_update():\n    from nastech_constants import first\n")
    first = commit(root, "first updater at an unknown address")
    git(root, "mv", "nastech_cli/ancient.py", "nastech_cli/briefly.py")
    renamed = commit(root, "rename without editing the blob")
    put(root, "nastech_cli/briefly.py", "from nastech_cli.gone import phase\ndef cmd_update():\n    phase()\n")
    put(root, "nastech_cli/gone.py", "def phase():\n    from nastech_constants import extracted\n")
    extracted = commit(root, "extract a helper under an unrelated filename")
    git(root, "mv", "nastech_cli/gone.py", "nastech_cli/later.py")
    put(root, "nastech_cli/briefly.py", "from nastech_cli.later import phase\ndef cmd_update():\n    phase()\n")
    commit(root, "rename the extracted helper")
    git(root, "rm", "nastech_cli/briefly.py", "nastech_cli/later.py")
    put(root, "nastech_cli/update_cmd.py", "def cmd_update():\n    from nastech_constants import newest\n")
    commit(root, "delete every historical filename")

    surface = audit.audit_history()
    assert {("nastech_constants", s) for s in ("first", "extracted", "newest")} <= surface.required.keys()
    assert {
        "nastech_cli/ancient.py:cmd_update", "nastech_cli/briefly.py:cmd_update"
    } <= surface.sites[("nastech_constants", "first")]
    assert first[:12] in surface.required[("nastech_constants", "first")]
    assert renamed[:12] in surface.required[("nastech_constants", "first")]
    assert extracted[:12] in surface.required[("nastech_constants", "extracted")]
    assert {
        "nastech_cli/gone.py:phase", "nastech_cli/later.py:phase"
    } <= surface.sites[("nastech_constants", "extracted")]
    assert surface.stats["commits"] == int(git(root, "rev-list", "--count", "origin/main"))
    assert surface.stats["complete_history"] is True
    assert surface.stats["history_ref"] == git(root, "rev-parse", "origin/main")
    assert surface.stats["roots"] == [first]
    assert {"nastech_cli/ancient.py", "nastech_cli/briefly.py"} <= set(surface.stats["entrypoint_paths"])
    assert {"nastech_cli/gone.py", "nastech_cli/later.py"} <= set(surface.stats["files_analyzed"])
    assert not any(root.glob("nastech_cli/*gone*"))
    assert audit.audit_tree().required.keys() == {("nastech_constants", "newest")}


def test_all_merge_parents_and_merge_result_but_not_unmerged_branches(audit):
    root = audit.REPO_ROOT
    path = "nastech_cli/prehistoric.py"
    put(root, path, "def cmd_update():\n    pass\n")
    base = commit(root, "base")
    git(root, "checkout", "-b", "side")
    put(root, path, "def cmd_update():\n    from nastech_constants import side_only\n")
    side = commit(root, "side updater")
    git(root, "checkout", "main")
    put(root, path, "def cmd_update():\n    from nastech_constants import main_only\n")
    commit(root, "main updater")
    # An ours merge is TREESAME to main. Ordinary path-limited git log
    # simplifies away the side parent and its real shipped revision.
    git(root, "merge", "-s", "ours", "--no-ff", "side", "-m", "discard side changes")
    commit_sha = git(root, "rev-parse", "HEAD")
    git(root, "update-ref", "refs/remotes/origin/main", commit_sha)
    assert side[:12] in audit.audit_history().required[("nastech_constants", "side_only")]
    git(root, "checkout", "-b", "other", base)
    put(root, "unrelated.txt", "new branch\n")
    commit(root, "unrelated change")
    git(root, "checkout", "main")
    git(root, "merge", "--no-ff", "--no-commit", "other")
    put(root, path, "def cmd_update():\n    from nastech_constants import merge_only\n")
    merged = commit(root, "updater code created only by merge resolution")
    git(root, "checkout", "-b", "unshipped", base)
    put(root, path, "def cmd_update():\n    from nastech_constants import never_shipped\n")
    commit(root, "unmerged branch")
    git(root, "update-ref", "refs/remotes/origin/main", merged)

    surface = audit.audit_history()
    assert {s for m, s in surface.required if m == "nastech_constants"} == {
        "side_only", "main_only", "merge_only"
    }
    assert merged[:12] in surface.required[("nastech_constants", "merge_only")]
    assert surface.stats["commits"] == int(git(root, "rev-list", "--count", "origin/main"))


def test_deleted_siblings_and_renamed_seed_helper_are_not_tied_to_head(audit):
    root = audit.REPO_ROOT
    put(root, "nastech_cli/update_cmd.py", "def cmd_update():\n    pass\n")
    put(root, "nastech_cli/old_support.py", "def old_phase():\n    from nastech_constants import before_rename\n")
    commit(root, "support before its known name")
    git(root, "mv", "nastech_cli/old_support.py", "nastech_cli/post_update.py")
    put(root, "nastech_cli/update_cmd_removed.py", "def phase():\n    from nastech_constants import deleted_sibling\n")
    commit(root, "known helper and temporary extraction")
    git(root, "rm", "nastech_cli/post_update.py", "nastech_cli/update_cmd_removed.py")
    commit(root, "remove both helpers")
    surface = audit.audit_history()
    assert {("nastech_constants", s) for s in ("before_rename", "deleted_sibling")} <= surface.required.keys()
    assert "nastech_cli/old_support.py:old_phase" in surface.sites[("nastech_constants", "before_rename")]
    assert not audit.audit_tree().required


def test_shallow_clone_refuses_freeze_without_overwriting_and_tree_still_works(audit, tmp_path, monkeypatch, capsys):
    root = audit.REPO_ROOT
    put(root, "nastech_cli/unknown.py", "def cmd_update():\n    from nastech_constants import old\n")
    commit(root, "historical contract")
    put(root, "nastech_cli/unknown.py", "def cmd_update():\n    from nastech_constants import current\n")
    commit(root, "current contract")
    clone = tmp_path / "shallow"
    git(root, "clone", "--depth=1", root.as_uri(), str(clone))
    monkeypatch.setattr(audit, "REPO_ROOT", clone)
    assert git(clone, "rev-parse", "--is-shallow-repository") == "true"
    with pytest.raises(audit.AuditError, match="shallow"):
        audit.audit_history()
    assert set(audit.audit_tree().required) == {("nastech_constants", "current")}
    output = clone / "frozen.json"
    output.write_text("do not truncate this", encoding="utf-8")
    with pytest.raises(SystemExit) as failure:
        audit.main(["--ref", "origin/main", "--freeze", str(output)])
    assert failure.value.code != 0
    assert "--unshallow" in capsys.readouterr().err
    assert output.read_text() == "do not truncate this"


def test_freeze_requires_cutoff_and_keeps_only_shipped_loads(audit, tmp_path, capsys):
    root = audit.REPO_ROOT
    put(root, "nastech_cli/update_cmd.py", """def cmd_update():
    from nastech_constants import old_only, bare_then_guarded
    try:
        from nastech_constants import guarded_then_bare, always_guarded
    except ImportError:
        pass
""")
    commit(root, "not a tag, still a shipped updater")
    put(root, "nastech_cli/update_cmd.py", """def cmd_update():
    from nastech_constants import guarded_then_bare
    try:
        from nastech_constants import bare_then_guarded, always_guarded
    except ImportError:
        pass
""")
    cutoff = commit(root, "last updater before the PM migration")
    put(root, "nastech_cli/update_cmd.py", "def cmd_update():\n    from nastech_constants import after_cutoff\n")
    commit(root, "origin/main has advanced beyond the contract cutoff")
    put(root, "nastech_cli/update_cmd.py", "def cmd_update():\n    from nastech_constants import uncommitted\n")
    output = tmp_path / "history.json"
    output.write_text("do not overwrite without a cutoff", encoding="utf-8")
    with pytest.raises(SystemExit) as failure:
        audit.main(["--freeze", str(output)])
    assert failure.value.code != 0
    assert "--ref" in capsys.readouterr().err
    assert output.read_text() == "do not overwrite without a cutoff"

    assert audit.main(["--ref", cutoff, "--freeze", str(output)]) == 0
    frozen = json.loads(output.read_text())
    assert set(frozen["bare"]) == {
        "nastech_constants::old_only",
        "nastech_constants::bare_then_guarded", "nastech_constants::guarded_then_bare",
    }
    assert frozen["guarded_only"] == ["nastech_constants::always_guarded"]
    assert frozen["stats"]["mode"] == "history"
    assert frozen["stats"]["history_ref"] == cutoff
    assert frozen["stats"]["complete_history"] is True


@pytest.mark.parametrize("malformed", [b"def cmd_update(:\n", b"def cmd_update():\n    # \xff\n    pass\n"])
def test_malformed_historical_entrypoint_fails_closed(audit, malformed):
    root = audit.REPO_ROOT
    target = root / "forgotten.py"
    target.write_bytes(malformed)
    commit(root, "broken historical source")
    put(root, "forgotten.py", "def cmd_update():\n    pass\n")
    commit(root, "repaired at tip")
    with pytest.raises(audit.AuditError, match="forgotten.py.*blob"):
        audit.audit_history()


def test_committed_merge_conflict_audits_both_arms_and_records_recovery(audit):
    root = audit.REPO_ROOT
    put(root, "old.py", """<<<<<<< HEAD
def cmd_update():
    from nastech_constants import ours
=======
def cmd_update():
    from nastech_constants import theirs
>>>>>>> incoming
""")
    commit(root, "accidentally committed conflict")
    put(root, "old.py", "def cmd_update():\n    pass\n")
    commit(root, "fix conflict")
    surface = audit.audit_history()
    assert {("nastech_constants", "ours"), ("nastech_constants", "theirs")} <= surface.required.keys()
    assert any("old.py" in recovery for recovery in surface.parse_recoveries)


def test_identical_blobs_have_path_specific_relative_imports_and_seed_roles(audit):
    root = audit.REPO_ROOT
    source = "def cmd_update():\n    from .constants import important\ndef unrelated():\n    from nastech_constants import helper_only\n"
    put(root, "nastech_cli/unknown.py", source)
    put(root, "nastech_cli/post_update.py", source)
    put(root, "pm/unknown.py", source)
    commit(root, "identical source, distinct modules and seed modes")
    surface = audit.audit_history()
    assert ("nastech_cli.constants", "important") in surface.required
    assert ("pm.constants", "important") in surface.required
    assert surface.sites[("nastech_constants", "helper_only")] == {"nastech_cli/post_update.py:unrelated"}


def test_only_swallowed_matching_load_failures_are_guarded(audit):
    root = audit.REPO_ROOT
    put(root, "nastech_cli/update_cmd.py", """def cmd_update():
    import sys
    try:
        from nastech_constants import wrong_exception
    except AttributeError:
        pass
    try:
        from nastech_constants import name_not_module
    except ModuleNotFoundError:
        pass
    try:
        from nastech_constants import reraised
    except ImportError:
        raise
    try:
        module = sys.modules.get("nastech_constants")
        getattr(module, "optional")
    except AttributeError:
        pass
""")
    commit(root, "exception boundaries")
    surface = audit.audit_history()
    assert surface.guarded_only == {("nastech_constants", "optional")}
    assert {("nastech_constants", s) for s in ("wrong_exception", "name_not_module", "reraised")} <= surface.required.keys()


def test_suppress_context_guards_like_a_swallowing_except(audit):
    root = audit.REPO_ROOT
    put(root, "nastech_cli/update_cmd.py", """import contextlib
from contextlib import suppress


def cmd_update():
    with suppress(Exception):
        from nastech_constants import via_suppress
    with contextlib.suppress(ImportError):
        from nastech_constants import via_qualified_suppress
    with suppress(AttributeError):
        from nastech_constants import wrong_suppress
""")
    commit(root, "suppress boundaries")
    surface = audit.audit_history()
    assert {("nastech_constants", "via_suppress"), ("nastech_constants", "via_qualified_suppress")} <= surface.guarded_only
    assert ("nastech_constants", "wrong_suppress") in surface.required.keys()


def test_lazy_module_facade_follows_called_helper_not_unrelated_commands(audit):
    root = audit.REPO_ROOT
    put(root, "nastech_cli/entry.py", """def _m():
    from nastech_cli import main
    return main

def cmd_update():
    _m().phase()
""")
    put(root, "nastech_cli/main.py", """from nastech_cli.gone import phase as phase

def unrelated_command():
    from nastech_constants import not_an_updater_load
""")
    put(root, "nastech_cli/gone.py", "def phase():\n    from nastech_constants import actual_helper_load\n")
    commit(root, "lazy facade and re-exported helper")
    surface = audit.audit_history()
    assert ("nastech_constants", "actual_helper_load") in surface.required
    assert ("nastech_constants", "not_an_updater_load") not in surface.required


def test_resolver_requires_a_module_binding_not_a_nested_name(audit):
    root = audit.REPO_ROOT
    put(root, "nastech_constants.py", """def owner():
    from pathlib import Path as local_import
    local_assignment = 1
    def local_function():
        pass

class Owner:
    def method(self):
        pass

if True:
    from pathlib import Path as exported
    value = 1
""")
    for symbol in ("local_import", "local_assignment", "local_function", "method"):
        assert not audit.resolve_in_tree("nastech_constants", symbol, root)[0], symbol
    for symbol in ("owner", "Owner", "exported", "value"):
        assert audit.resolve_in_tree("nastech_constants", symbol, root)[0], symbol


def test_same_named_functions_keep_requirements_from_every_definition(audit):
    result = audit.analyse("""class First:
    def phase(self):
        from nastech_constants import first

class Second:
    def phase(self):
        from nastech_constants import second

if True:
    def platform_phase():
        from nastech_constants import platform_a
else:
    def platform_phase():
        from nastech_constants import platform_b

def cmd_update():
    Second().phase()
    platform_phase()
""", "nastech_cli/update_cmd.py", entrypoints=True)
    assert {r.symbol for r in result.requirements} == {
        "first", "second", "platform_a", "platform_b",
    }


def test_reviewed_dynamic_loads_survive_history_freeze_within_cutoff(audit, monkeypatch):
    root = audit.REPO_ROOT
    put(root, "nastech_cli/update_cmd.py", "def cmd_update():\n    from nastech_constants import anchor\n")
    witness = commit(root, "module-object call manually reviewed")
    put(root, "nastech_cli/update_cmd.py", "def cmd_update():\n    from nastech_constants import later\n")
    later = commit(root, "module-object call after the contract cutoff")
    monkeypatch.setattr(audit, "REVIEWED_DYNAMIC_LOADS", (
        ("nastech_constants", "dynamic", witness[:12], "nastech_cli/update_cmd.py:cmd_update"),
        ("nastech_constants", "after_cutoff", later[:12], "nastech_cli/update_cmd.py:cmd_update"),
    ))
    surface = audit.audit_history(witness)
    assert surface.required[("nastech_constants", "dynamic")] == {witness[:12]}
    assert surface.kinds[("nastech_constants", "dynamic")] == {"reviewed-module-call"}
    assert surface.sites[("nastech_constants", "dynamic")] == {"nastech_cli/update_cmd.py:cmd_update"}
    assert ("nastech_constants", "dynamic") not in surface.guarded_only
    assert ("nastech_constants", "after_cutoff") not in surface.required
    output = root / "history.json"
    assert audit.main(["--ref", witness, "--history", "--freeze", str(output)]) == 0
    frozen = json.loads(output.read_text())
    assert set(frozen["bare"]) == {"nastech_constants::anchor", "nastech_constants::dynamic"}
