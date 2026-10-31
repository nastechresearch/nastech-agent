"""An unsigned desktop leg may only check what it could physically produce.

``skip-signed: true`` is the fork's only desktop lane until the org holds Azure
Trusted Signing and Apple Developer ID credentials. Two steps demanded inputs
such a leg cannot have, and each crashed the leg instead of reporting that it
had nothing to verify (canary run 41203876229): the Windows architecture audit
scanned a release directory the ``SKIP_SIGNED``-gated bundle build never
created, and the macOS recorder codesign-verified an ad-hoc app and then refused
it for lacking a Developer ID team.

Neither check is deleted here. Each must run on exactly the dispatches whose
bytes exist and are signed, so these tests pin both directions — no check
without signed bytes, and no silently retired check when signed bytes are there
to check. They also pin the two consequences of that rule: an unsigned handoff
carries no signed-release row and its bytes reach no publication step, while a
leg that produced nothing at all still fails loudly instead of exiting clean.
"""
from __future__ import annotations

import os
import re
import shlex
import subprocess
from pathlib import Path

import pytest

from scripts.releases import handoff
from tests.ci.desktop_release_roles import (
    DOWNLOADABLE_DISPATCHES,
    admitted,
    evaluate,
    gate,
    load,
    native_builds,
    needs_of,
    smoke_callers,
    stage_step,
    updater_publishers,
)
from tests.ci.test_desktop_release_tag_admission import _BASH, _child_env

SHA = "a" * 40
CANARY = "v0.21.5+canary.20261031T130355Z"
pytestmark = pytest.mark.platforms("posix")

# The step that writes apps/desktop/release, and the step that reads it.
BUNDLE_BUILDER = "--prepared"
BUNDLE_AUDITOR = "audit-bundle-arch.mjs"


def _stringify(value) -> str:
    """How Actions renders an expression into an environment variable."""
    if value is True:
        return "true"
    if value is False:
        return "false"
    return "" if value is None else str(value)


def _dotted(row, bits: list[str]):
    for bit in bits:
        row = row.get(bit, "") if isinstance(row, dict) else ""
    return row


def _matrix_of(job: dict) -> dict:
    """The ``matrix.`` context of a leg: its first strategy row, keyed by dimension."""
    return {dimension: rows[0] for dimension, rows in (job.get("strategy") or {}).get("matrix", {}).items()}


def _render(value, *, inputs: dict, needs: dict, matrix: dict) -> str:
    """One step/job ``env:`` entry resolved the way the runner resolves it."""
    text = str(value)
    if not (text.strip().startswith("${{") and text.strip().endswith("}}")):
        return text
    body = text.strip()[3:-2].strip()
    if body.startswith("matrix."):
        return _stringify(_dotted(matrix, body.split(".")[1:]))
    if body.startswith(("secrets.", "vars.")):
        return "inert-credential"
    return _stringify(evaluate(body, inputs, needs))


def _env_of(node: dict, *, inputs: dict, needs: dict, matrix: dict) -> dict[str, str]:
    return {key: _render(value, inputs=inputs, needs=needs, matrix=matrix)
            for key, value in (node.get("env") or {}).items()}


def _step(job: dict, needle: str) -> dict:
    (matches,) = [step for step in job["steps"] if needle in step.get("run", "")]
    return matches


def _step_runs(step: dict, inputs: dict, needs: dict) -> bool:
    """Whether Actions would run *step*: a step with no ``if:`` always runs."""
    return "if" not in step or bool(gate(step["if"], inputs, needs, job_if=False))


def _bundled_build_ran(step: dict, inputs: dict, needs: dict) -> bool:
    """Whether the leg's build step produced a bundle for this dispatch.

    The PowerShell build hides its ``--variant bundled`` call behind a guard on
    an environment variable the step maps to an input, so the bundle exists only
    when the step runs *and* that guard is false.
    """
    if not _step_runs(step, inputs, needs):
        return False
    run = step["run"]
    guarded = re.findall(r"if \(\$env:(\w+) -ne 'true'\)\s*\{[^}]*--variant bundled", run)
    if not guarded:
        return True
    (name,) = guarded
    return not gate(step["env"][name], inputs, needs, job_if=False)


@pytest.mark.parametrize("dispatch", sorted(DOWNLOADABLE_DISPATCHES))
def test_windows_audit_runs_exactly_when_the_bundle_was_built(dispatch):
    """The architecture audit has no input on a leg that built no bundle."""
    jobs = load()["jobs"]
    failures = []
    for (target, mode), name in sorted(native_builds(jobs).items()):
        job = jobs[name]
        build, audit = _step(job, BUNDLE_BUILDER), _step(job, BUNDLE_AUDITOR)
        for skip_signed in (True, False):
            inputs = {**DOWNLOADABLE_DISPATCHES[dispatch], "skip-signed": skip_signed}
            needs = admitted(needs_of(job))
            built = _bundled_build_ran(build, inputs, needs)
            audited = _step_runs(audit, inputs, needs)
            if target.startswith("win32"):
                # An audit of bytes that were never built crashes on a missing
                # release directory; skipping it once the leg builds again would
                # silently retire the check that catches mixed-architecture
                # bundles. A skip-signed Windows leg builds no bundle at all: the
                # Store variant is refused on canary, commit and channel tags.
                if audited != built:
                    failures.append(f"{name} audited={audited} built={built} skip-signed={skip_signed}")
            elif not audited:
                failures.append(f"{name} skipped its audit of a bundle it always builds")
    assert not failures, "\n".join(failures)


def _staged_commands(tmp_path: Path, job: dict, step: dict, inputs: dict, *, packages: bool) -> list[str]:
    """Run one native leg's tag staging step for real, logging every python call it makes."""
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir(exist_ok=True)
    log = tmp_path / f"python-calls-{job['name']}-{packages}.log"
    log.unlink(missing_ok=True)
    for name in ("python", "python3"):
        launcher = bin_dir / name
        launcher.write_text(f'#!/bin/sh\nprintf \'%s\\n\' "$*" >> {shlex.quote(str(log))}\nexit 0\n',
                            encoding="utf-8", newline="\n")
        launcher.chmod(0o755)
    release = tmp_path / "apps/desktop/release"
    release.mkdir(parents=True, exist_ok=True)
    if packages:
        for name in ("NastechBundled-0.21.5-mac-arm64.dmg", "NastechBundled-0.21.5-mac-arm64.zip",
                     "NastechBundled-0.21.5-mac-arm64.zip.blockmap", "arm64-canary-mac.yml",
                     "NastechBundled-26.10.31.1303-win-arm64.msix"):
            (release / name).write_bytes(b"inert package fixture")
    else:
        for file in release.iterdir():
            file.unlink()
    needs = admitted(needs_of(job))
    environment = _child_env(**{**_env_of(job, inputs=inputs, needs=needs, matrix=_matrix_of(job)),
                                **_env_of(step, inputs=inputs, needs=needs, matrix=_matrix_of(job)),
                                "PATH": str(bin_dir) + os.pathsep + os.environ["PATH"],
                                "GITHUB_OUTPUT": str(tmp_path / "output.txt"), "RUNNER_TEMP": str(tmp_path)})
    script = tmp_path / "step.sh"
    script.write_text(step["run"], encoding="utf-8", newline="\n")
    result = subprocess.run([_BASH, "-e", "-o", "pipefail", str(script)], cwd=tmp_path, env=environment,
                            capture_output=True, text=True, encoding="utf-8", timeout=60, check=False)
    assert result.returncode == 0, f"the leg failed before staging: {result.stdout}\n{result.stderr}"
    commands = log.read_text(encoding="utf-8").splitlines() if log.exists() else []
    assert any("scripts.releases.handoff stage" in line for line in commands), result.stderr
    return commands


@pytest.mark.parametrize("target", ["darwin-arm64", "win32-x64"])
def test_release_metadata_is_recorded_only_for_signed_bytes(tmp_path, target):
    """``release_artifacts record`` reads a signature no unsigned build can carry.

    The macOS recorder codesign-verifies the app and then demands a 10-character
    Developer ID team; the Windows recorder reads the Authenticode-bound MSIX
    identity. A metadata row is therefore a signed-release record: an unsigned leg
    writes none and stages none, while its own packages still stage — and a signed
    leg still records its row.
    """
    jobs = load()["jobs"]
    job = jobs[native_builds(jobs)[(target, "release")]]
    step = stage_step(job)
    platform = "macos" if target.startswith("darwin") else "windows"
    for skip_signed in (True, False):
        inputs = {**DOWNLOADABLE_DISPATCHES["tag"], "skip-signed": skip_signed}
        assert _step_runs(step, inputs, admitted(needs_of(job))), "this dispatch must stage the leg's bytes"
        commands = _staged_commands(tmp_path, job, step, inputs, packages=True)
        recorded = [line for line in commands if f"record --platform {platform}" in line]
        staged = [line for line in commands if "scripts.releases.handoff stage" in line][-1]
        if skip_signed:
            assert not recorded, f"an unsigned {target} leg recorded a signed release row: {recorded}"
            assert "metadata-*.json" not in staged, f"an unsigned {target} leg staged a row it cannot sign"
        else:
            assert len(recorded) == 1, f"a signed {target} leg must still record its row: {commands}"
            assert "metadata-*.json" in staged


def _needs_results(jobs: dict, job: dict, inputs: dict, smoke_names: set[str]) -> dict:
    """Needs rows for *job*: admitted, except a smoke its own gate refuses to run.

    Actions marks a job skipped when a job it needs did not run, so a publisher
    reads the smoke lanes exactly as the workflow's own gates decide them.
    """
    rows = admitted(needs_of(job))
    for dependency in needs_of(job):
        if dependency in smoke_names:
            dependent = jobs[dependency]
            if not gate(dependent["if"], inputs, admitted(needs_of(dependent))):
                rows[dependency]["result"] = "skipped"
    return rows


@pytest.mark.parametrize("dispatch", sorted(DOWNLOADABLE_DISPATCHES))
def test_unsigned_bytes_reach_no_publication_step(dispatch):
    """Repairing an unsigned leg may not open a path from it to a published feed.

    The updater feed is what an installed app reads, and the recorder's row is
    what the stable claim reads, so neither may publish or accept bytes no
    Developer ID or Authenticode signature stands behind.
    """
    jobs = load()["jobs"]
    smokes = set(smoke_callers(jobs).values())
    publishers = updater_publishers(jobs)
    offenders = []
    for skip_signed in (True, False):
        for platform, name in sorted(publishers.items()):
            inputs = {**DOWNLOADABLE_DISPATCHES[dispatch], "skip-signed": skip_signed}
            job = jobs[name]
            published = gate(job["if"], inputs, _needs_results(jobs, job, inputs, smokes))
            if published and skip_signed:
                offenders.append(f"{name} publishes the unsigned {platform} feed")
    assert not offenders, "\n".join(offenders)

    signed_inputs = {**DOWNLOADABLE_DISPATCHES["tag"], "skip-signed": False}
    for platform, name in sorted(publishers.items()):
        job = jobs[name]
        assert gate(job["if"], signed_inputs, _needs_results(jobs, job, signed_inputs, smokes)), \
            f"{name} stopped publishing the signed {platform} feed: a check was deleted"


def test_a_handoff_that_produced_nothing_is_a_loud_failure(tmp_path):
    """Nothing at all is an error, never an empty success."""
    root = tmp_path / "release"
    root.mkdir()
    with pytest.raises(ValueError, match=r"No files match release handoff pattern: \*\.dmg"):
        handoff.stage(CANARY, SHA, "darwin-arm64", root, ["*.dmg", "*.zip"])

    (root / "NastechBundled-0.21.5-mac-arm64.dmg").write_bytes(b"inert package fixture")
    with pytest.raises(ValueError, match=r"No files match release handoff pattern: metadata-\*\.json"):
        handoff.stage(CANARY, SHA, "darwin-arm64", root, ["*.dmg", "metadata-*.json"])
