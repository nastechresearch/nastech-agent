"""An unsigned desktop leg builds, audits and stages its own packages.

``skip-signed: true`` is the fork's only desktop lane until the org holds Azure
Trusted Signing and Apple Developer ID credentials.  Upstream reads that switch
as "build nothing Windows-related", which is right for a project whose channel
only ever carries signed bytes and wrong here: the leg then has no release
directory, so its architecture audit crashes on a missing root and its handoff
refuses with ``No files match release handoff pattern: *.msix`` (canary run
41776230035).  The macOS legs never had that problem -- they build the bundle
and simply have no certificate to sign it with.  This file pins that shape:
every desktop leg builds and verifies the bytes its lane names, and signing
gates only what leaves the leg for a feed.

Two checks stay signed-only, because they read a signature rather than a
package: the release row ``release_artifacts record`` writes (Developer ID team
for macOS, Authenticode identity for the MSIX) and the publication of the
updater feed.  Both directions are pinned per leg, per skip-signed and
skip-store -- no signed row without signed bytes, no retired check when signed
bytes are there to record, and no unsigned byte reaching a publisher.  A leg
that produced nothing at all still fails loudly (``test_a_handoff_that_produced_
nothing_is_a_loud_failure``); this repair removes the empty leg, not the error.
"""
from __future__ import annotations

import fnmatch
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
    universal_assembler,
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
    # `vars.` and `secrets.` also appear inside larger expressions (the build step
    # masks its signing vars behind `inputs.skip-signed`); resolve them the way the
    # runner does -- an unset repository variable is the empty string, a secret is
    # an opaque non-empty value -- so the rest of the expression still evaluates.
    body = re.sub(r"\bvars\.([A-Za-z_]\w*)", "''", body)
    body = re.sub(r"\bsecrets\.([A-Za-z_]\w*)", "'inert-credential'", body)
    return _stringify(evaluate(body, inputs, needs))


def _env_of(node: dict, *, inputs: dict, needs: dict, matrix: dict) -> dict[str, str]:
    return {key: _render(value, inputs=inputs, needs=needs, matrix=matrix)
            for key, value in (node.get("env") or {}).items()}


def _step(job: dict, needle: str) -> dict:
    (matches,) = [step for step in job["steps"] if needle in step.get("run", "")]
    return matches


def _step_runs(step: dict, inputs: dict, needs: dict, env: dict[str, str] | None = None) -> bool:
    """Whether Actions would run *step*: a step with no ``if:`` always runs."""
    return "if" not in step or bool(gate(step["if"], inputs, needs, job_if=False, env=env))


def _guard_holds(guard: str, env_map: dict[str, str]) -> bool:
    """Evaluate one PowerShell build guard against the environment the step is given."""
    text = re.sub(r"\$env:(\w+)", lambda m: repr(env_map.get(m.group(1), "")), guard)
    operand = r"(\([^()]+\)|'[^']*'|\"[^\"]*\"|\S+)"
    text = re.sub(rf"{operand} -notlike {operand}", r"(not _like(\1, \2))", text)
    text = re.sub(rf"{operand} -ne {operand}", r"(\1 != \2)", text)
    text = re.sub(rf"-not {operand}", r"(not \1)", text)
    text = text.replace("-and", " and ").replace("-or", " or ")
    scope = {"_like": lambda value, pattern: fnmatch.fnmatch(value, pattern.strip("\"'"))}
    return bool(eval(text, {"__builtins__": {}}, scope))


def _guard_spans(run: str) -> list[tuple[int, int, str]]:
    """``(block start, block end, condition)`` for every ``if (cond) { ... }`` in a step body.

    The block is found by matching braces from its opening ``{``, so a guard's span covers
    its whole body and a nested guard's span sits inside the outer one's.
    """
    spans = []
    for match in re.finditer(r"if \((.+?)\)\s*\{", run):
        depth, index = 0, run.index("{", match.end() - 1)
        start = index
        while index < len(run):
            if run[index] == "{":
                depth += 1
            elif run[index] == "}":
                depth -= 1
                if depth == 0:
                    break
            index += 1
        spans.append((start, index + 1, match.group(1)))
    return spans


def _variants_built(step: dict, env_map: dict[str, str]) -> set[str]:
    """Which package variants this leg's build step produces for this dispatch.

    A ``--variant`` call behind a PowerShell ``if`` builds only while that guard holds; a
    call outside every guard (both legs' bundled variant) always builds.
    """
    run = step["run"]
    spans = _guard_spans(run)
    built: set[str] = set()
    for call in re.finditer(r"--variant (\S+)", run):
        holders = [span for span in spans if span[0] <= call.start() < span[1]]
        if not holders:
            built.add(call.group(1))
            continue
        condition = min(holders, key=lambda span: span[1] - span[0])[2]
        if _guard_holds(condition, env_map):
            built.add(call.group(1))
    return built


@pytest.mark.parametrize("dispatch", sorted(DOWNLOADABLE_DISPATCHES))
def test_audit_runs_exactly_on_the_bytes_the_leg_built(dispatch):
    """Every bundle gets its architecture audit; no audit runs on bytes that are not there.

    The audit answers an unsigned question (which architecture is each Mach-O/PE in the
    bundle), so it owes nothing to signing, and every leg that builds a bundle must answer it.
    The two are pinned as one invariant across skip-signed and skip-store: an audit of a
    directory nothing was written to crashes on a missing root, and an audit retired while its
    bytes are there to scan is an architecture check deleted.
    """
    jobs = load()["jobs"]
    failures = []
    for (target, mode), name in sorted(native_builds(jobs).items()):
        job = jobs[name]
        build, audit = _step(job, BUNDLE_BUILDER), _step(job, BUNDLE_AUDITOR)
        for skip_signed, skip_store in [(x, y) for x in (True, False) for y in (True, False)]:
            inputs = {**DOWNLOADABLE_DISPATCHES[dispatch], "skip-signed": skip_signed,
                      "skip-store": skip_store}
            needs = admitted(needs_of(job), channel=dispatch == "channel")
            env_map = {**_env_of(job, inputs=inputs, needs=needs, matrix=_matrix_of(job)),
                       **_env_of(build, inputs=inputs, needs=needs, matrix=_matrix_of(job))}
            built, audited = bool(_variants_built(build, env_map)), _step_runs(audit, inputs, needs, env=env_map)
            if built and not _step_runs(build, inputs, needs, env=env_map):
                failures.append(f"{name} built a variant its build step would not run")
            if audited != built:
                failures.append(f"{name} audited={audited} built={sorted(_variants_built(build, env_map))} "
                                f"skip-signed={skip_signed} skip-store={skip_store}")
    assert not failures, "\n".join(failures)


@pytest.mark.parametrize("dispatch", sorted(DOWNLOADABLE_DISPATCHES))
def test_every_desktop_leg_builds_the_bundled_package(dispatch):
    """A leg builds the package its lane names, whatever it signs.

    Upstream gates the Windows bundled variant behind ``SKIP_SIGNED``, which turns an unsigned
    leg into a leg that builds nothing: no release directory for the audit, no package for the
    handoff (canary run 41776230035).  The macOS legs never gate the call -- they build, and
    the absent certificate decides whether the bytes end up signed -- so this pins every native
    leg to that shape, across skip-signed and skip-store.
    """
    jobs = load()["jobs"]
    failures = []
    for (target, mode), name in sorted(native_builds(jobs).items()):
        job = jobs[name]
        build = _step(job, BUNDLE_BUILDER)
        for skip_signed, skip_store in [(x, y) for x in (True, False) for y in (True, False)]:
            inputs = {**DOWNLOADABLE_DISPATCHES[dispatch], "skip-signed": skip_signed,
                      "skip-store": skip_store}
            needs = admitted(needs_of(job), channel=dispatch == "channel")
            env_map = {**_env_of(job, inputs=inputs, needs=needs, matrix=_matrix_of(job)),
                       **_env_of(build, inputs=inputs, needs=needs, matrix=_matrix_of(job))}
            if "bundled" not in _variants_built(build, env_map):
                failures.append(f"{name} built no bundled package with skip-signed={skip_signed} "
                                f"skip-store={skip_store}")
    assert not failures, "\n".join(failures)


def _run_release_step(tmp_path: Path, job: dict, step: dict, inputs: dict, *, channel: bool = False,
                      packages: bool = True, shims: tuple[str, ...] = ("python", "python3")) -> list[str]:
    """Run one release-leg step for real, logging every command it makes to a shimmed interpreter.

    The step's own guards decide what it calls, so this is the only honest way to ask what a
    dispatch builds or stages: the workflow text is never parsed for a shape, it is executed.
    """
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir(exist_ok=True)
    suffix = f"{job['name']}-{packages}-{'channel' if channel else 'tag'}"
    log = tmp_path / f"python-calls-{suffix}.log"
    log.unlink(missing_ok=True)
    for name in shims:
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
    needs = admitted(needs_of(job), channel=channel)
    environment = _child_env(**{**_env_of(job, inputs=inputs, needs=needs, matrix=_matrix_of(job)),
                                **_env_of(step, inputs=inputs, needs=needs, matrix=_matrix_of(job)),
                                "PATH": str(bin_dir) + os.pathsep + os.environ["PATH"],
                                "GITHUB_OUTPUT": str(tmp_path / "output.txt"),
                                "GITHUB_WORKSPACE": str(tmp_path),
                                "RUNNER_TEMP": str(tmp_path)})
    (tmp_path / "channel-request.json").write_text('{"version": "0.21.5"}', encoding="utf-8")
    script = tmp_path / f"step-{suffix}.sh"
    script.write_text(step["run"], encoding="utf-8", newline="\n")
    result = subprocess.run([_BASH, "-e", "-o", "pipefail", str(script)], cwd=tmp_path, env=environment,
                            capture_output=True, text=True, encoding="utf-8", timeout=60, check=False)
    assert result.returncode == 0, f"the leg step failed: {result.stdout}\n{result.stderr}"
    return log.read_text(encoding="utf-8").splitlines() if log.exists() else []


def _staged_commands(tmp_path: Path, job: dict, step: dict, inputs: dict, *, packages: bool,
                     channel: bool = False) -> list[str]:
    """Run one native leg's staging step for real, logging every python call it makes."""
    commands = _run_release_step(tmp_path, job, step, inputs, channel=channel, packages=packages)
    assert any("scripts.releases.handoff stage" in line for line in commands), commands
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


@pytest.mark.parametrize("skip_signed", [True, False])
@pytest.mark.parametrize("target", ["darwin-arm64", "win32-x64"])
def test_a_channel_leg_writes_a_signed_row_only_if_it_signed(tmp_path, target, skip_signed):
    """The channel recorder is the same signed-only question on the sibling path.

    A channel dispatch asks for a Developer ID team and an Authenticode-bound MSIX
    identity exactly as the tag dispatch does, so an unsigned channel leg stages
    its packages and writes no row, while a signed one still writes its own.
    """
    jobs = load()["jobs"]
    job = jobs[native_builds(jobs)[(target, "release")]]
    step = stage_step(job, channel=True)
    inputs = {**DOWNLOADABLE_DISPATCHES["channel"], "skip-signed": skip_signed}
    needs = admitted(needs_of(job), channel=True)
    assert _step_runs(step, inputs, needs), "a channel leg must stage the bytes it built"
    platform = "macos" if target.startswith("darwin") else "windows"
    commands = _staged_commands(tmp_path, job, step, inputs, packages=True, channel=True)
    recorded = [line for line in commands if f"record --platform {platform}" in line]
    staged = [line for line in commands if "scripts.releases.handoff stage" in line][-1]
    if skip_signed:
        assert not recorded, f"an unsigned {target} channel leg wrote a signed row: {recorded}"
        assert "metadata-*.json" not in staged, f"an unsigned {target} leg staged a row it never wrote"
    else:
        assert len(recorded) == 1, f"a signed {target} channel leg must still record its row: {commands}"
        assert "metadata-*.json" in staged


@pytest.mark.parametrize("dispatch", sorted(DOWNLOADABLE_DISPATCHES))
def test_the_universal_leg_stages_the_bundle_it_assembles(tmp_path, dispatch):
    """A leg may not stage a package kind its own build step refused to assemble.

    ``Stage universal bundles to R2`` is unconditional and globs ``*.msixbundle``, while the
    step before it called ``stage-msixbundle.mjs`` only under ``SKIP_SIGNED != true``.  That
    guard is the same empty-handoff crash the per-arch legs had, one job deeper: assembling
    needs no account (``makeappx``), signing does, and the script assembles and warns when
    ``AZURE_SIGN_*`` are absent.  So every mode that reaches this job assembles.
    """
    jobs = load()["jobs"]
    job = jobs[universal_assembler(jobs)]
    assemble, stage = _step(job, "stage-msixbundle.mjs"), _step(job, "--name windows-universal")
    needs = admitted(needs_of(job), channel=dispatch == "channel")
    for skip_signed in (True, False):
        inputs = {**DOWNLOADABLE_DISPATCHES[dispatch], "skip-signed": skip_signed}
        commands = _run_release_step(tmp_path, job, assemble, inputs, channel=dispatch == "channel",
                                     shims=("node", "python"))
        assembled = any("stage-msixbundle.mjs" in line for line in commands)
        assert assembled == _step_runs(stage, inputs, needs), (
            f"{dispatch} skip-signed={skip_signed}: assembled={assembled} staged="
            f"{_step_runs(stage, inputs, needs)} commands={commands}")


STABLE_RECEIPTS = ("darwin-arm64", "darwin-x64", "win32-bundle")


def _receipt_gates(jobs: dict) -> dict[str, list[dict]]:
    """receipt -> every node that decides it: its job, plus the step's own gate when the
    receipt is one step of a bigger job (win32-bundle rides the bundle assembler)."""
    gates: dict[str, list[dict]] = {}
    for _name, job in jobs.items():
        for step in job.get("steps", []):
            for receipt in STABLE_RECEIPTS:
                if f"stage-receipt --receipt {receipt}" in (step.get("run") or ""):
                    assert receipt not in gates, f"{receipt} is staged by two nodes"
                    gates[receipt] = [job, step]
    assert set(gates) == set(STABLE_RECEIPTS), gates
    return gates


def test_no_stable_receipt_is_staged_without_its_signed_rows() -> None:
    """A candidate receipt is assembled from the recorder's rows, and a handoff fetch
    that matches nothing returns nothing: staging one for an unsigned leg would publish
    a record of zero packages instead of failing. Every signed candidate still receipts.
    """
    jobs = load()["jobs"]
    for skip_signed in (True, False):
        inputs = {**DOWNLOADABLE_DISPATCHES["candidate"], "skip-signed": skip_signed}
        for receipt, nodes in sorted(_receipt_gates(jobs).items()):
            job = nodes[0]
            staged = all(_step_runs(node, inputs, admitted(needs_of(job))) for node in nodes)
            if skip_signed:
                assert not staged, f"{receipt}: an unsigned candidate staged a receipt of no rows"
            else:
                assert staged, f"{receipt}: a signed candidate lost its receipt — a check was deleted"


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
