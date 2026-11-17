"""scripts/ci/check_agents_md_size.py: every AGENTS.md chain an agent can load stays under the cap it is truncated at."""

import ast
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "ci" / "check_agents_md_size.py"


def _cap(name):
    """The cap constant as the script itself declares it, so a raise is not a test edit."""
    for node in ast.walk(ast.parse(SCRIPT.read_text(encoding="utf-8"))):
        if isinstance(node, ast.Assign) and any(getattr(t, "id", None) == name for t in node.targets):
            return int(ast.literal_eval(node.value))
    raise AssertionError(f"{SCRIPT}: no {name} assignment")


def _repo(tmp_path, files):
    (tmp_path / "agent").mkdir(parents=True)
    (tmp_path / "agent" / "subdirectory_hints.py").write_text("_MAX_HINT_CHARS = 32_000\n")
    for rel, chars in files.items():
        (tmp_path / rel).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / rel).write_text("x" * chars)
    (tmp_path / "untracked").mkdir()
    (tmp_path / "untracked" / "AGENTS.md").write_text("u" * 40_000)
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(["git", "add", "agent", *files], cwd=tmp_path, check=True)
    return tmp_path


def _check(repo):
    return subprocess.run([sys.executable, str(SCRIPT), str(repo)], capture_output=True, text=True, check=False)


def test_budget_is_per_chain_from_the_root_down(tmp_path):
    # Each file alone is small; root + app + app/src together is what an agent working in app/src loads.
    root_cap, chain_cap = _cap("ROOT_MAX_CHARS"), _cap("CHAIN_MAX_CHARS")
    # app/src sits one char under a chain that exactly fills the budget; the
    # nested repo adds one char and tips the chain over by exactly one.
    src = chain_cap - root_cap - 10_000
    fits = {"AGENTS.md": root_cap, "app/AGENTS.md": 10_000, "app/src/AGENTS.md": src, "lib/AGENTS.md": 18_000}
    ok = _check(_repo(tmp_path / "ok", fits))
    assert ok.returncode == 0, ok.stdout
    nested = _check(_repo(tmp_path / "nested", {**fits, "app/src/AGENTS.md": src + 1}))
    assert nested.returncode == 1
    assert (f"AGENTS.md + app/AGENTS.md + app/src/AGENTS.md: {chain_cap + 1} chars "
            f"> {chain_cap} chain cap") in nested.stdout
    assert "lib/" not in nested.stdout and "untracked" not in nested.stdout
    root = _check(_repo(tmp_path / "root", {"AGENTS.md": root_cap + 1}))
    assert root.returncode == 1 and f"AGENTS.md: {root_cap + 1} chars > {root_cap} cap" in root.stdout
