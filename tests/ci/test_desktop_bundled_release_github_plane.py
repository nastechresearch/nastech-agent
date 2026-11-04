"""Desktop-bundled-release stages and fetches on the GitHub handoff plane, not on R2.

The release plane moved from Cloudflare R2 to GitHub Release assets (handoff) plus
GitHub Pages (control), but the workflows still hand their jobs the bucket's
credentials: an env var nothing on the pinned plane reads, and one a future
``r2.credentials()`` call could silently prefer. This file pins the migrated shape
of ``desktop-bundled-release.yml`` as contracts between the workflow and the store
seams, not as a snapshot of my edits:

* the run pins one handoff store up front, so a leg's staging and a publish job's
  fetch cannot disagree (the pin is what ``handoff.store`` obeys first);
* a step that runs ``scripts.releases.handoff`` is a seam step: it resolves its
  store from the pin, so it must be handed no bucket credential — an env it cannot
  read, and the exact env a re-add would make live again;
* the signed-leg credential gate may not be weakened by the migration: the vars it
  refuses on stay refused on, and stay declared where it reads them;
* the emitted public authority stays the bucket origin, on purpose: every reader
  of ``public-base`` hands the value to ``channel_public_base(explicit)``, and an
  explicit base is passed straight through (only an omitted base resolves the
  store pin), while the channel plane still allocates and publishes through the
  bucket (``channel_disposable``/``channel_publish`` build ``R2ChannelStore``
  directly). A pin that changes a reader must not be applied where a reader
  ignores it; that changes when those writers move through
  ``ghpages.configured_store`` (fork PR #206);
* R2-bound steps (the dependency mirror, the stable receipts, the feed publishers
  and renderers that still ``r2.put`` internally) keep their credentials, so the
  residue is a documented list, not an accretion: every export must be justified
  by an R2-bound command in the very node that carries it.
"""
from __future__ import annotations

import pytest

from scripts.releases import gh_transport, handoff, r2
from tests.ci.desktop_release_roles import (
    native_builds,
    credential_gate,
    load,
    smoke_callers,
)

R2_VARS = ("CLOUDFLARE_R2_ACCOUNT_ID", "CLOUDFLARE_R2_ACCESS_KEY_ID",
           "CLOUDFLARE_R2_SECRET_ACCESS_KEY", "CLOUDFLARE_R2_BUCKET",
           "CLOUDFLARE_R2_PUBLIC_URL")
HANDOFF_SEAM = "scripts.releases.handoff"
# Modules that still talk to the bucket internally: a node running one of these
# must carry the credentials the module reads (it would SystemExit without them).
R2_BOUND_MARKS = (
    "scripts.ci.archive_inputs",               # the pinned-input dependency mirror
    "scripts.releases.channel_disposable",     # allocates an R2ChannelStore directly
    "scripts.releases.channel_publish",        # feeds are written with r2.put
    "scripts.releases.channel_releases",       # the protected-head publisher
    "scripts.releases.stable",                 # stage-receipt writes through r2.put
    "scripts.releases.r2",                     # the legacy transport CLI
    "release_artifacts",                       # publish-appinstaller writes the feed
    "render-builds-table.py",                  # lists and pages live in the bucket
    "desktop-build-cache",                     # the action archives inputs via r2
    "setup-pm",                                # archive-inputs mirrors toolchain pins
    "::error::required",                       # the credential-readiness gate
)
# Steps that keep the legacy module CLI until a store seam exists for the darwin
# feed transport (scripts/releases/darwin.py builds its transport from
# r2.signed_request/put_object; scripts.releases.r2 finalize is its re-export).
LEGACY_R2_CLI_JOBS = ("publish-darwin-updater",)


def _env_node(job: dict, step: dict) -> dict:
    return {**(job.get("env") or {}), **(step.get("env") or {})}


def _r2_keys(node: dict) -> tuple[str, ...]:
    return tuple(key for key in node if key.startswith("CLOUDFLARE_R2"))


def _run_steps(job: dict):
    for index, step in enumerate(job.get("steps") or []):
        if "run" in step:
            yield index, step


def test_the_run_pins_the_github_handoff_store():
    """The workflow-level pin is the lever every seam step resolves through."""
    workflow_env = load()["env"]
    assert workflow_env["RELEASE_HANDOFF_STORE"] == "github"
    assert workflow_env["RELEASE_CHANNEL_STORE"] == "github"


def test_the_pin_selects_github_even_where_the_bucket_is_still_configured(monkeypatch):
    """Behavior contract behind the YAML rule: pinned staging cannot fall back to R2.

    The residual bucket env this workflow still exports for the R2-bound steps is
    exactly the state where an unpinned run would split one release across stores.
    """
    monkeypatch.setenv("RELEASE_HANDOFF_STORE", "github")
    monkeypatch.setenv("CLOUDFLARE_R2_BUCKET", "nastech-releases")
    bucket_origin = "https://assets.nastech.example/nastech-releases"
    assert handoff.store() is gh_transport
    # Even a read whose public base names the bucket resolves through the pin,
    # because a job that staged here must be able to fetch what it staged.
    assert handoff.store(bucket_origin) is gh_transport
    assert handoff.store() is not r2


@pytest.mark.parametrize("target", sorted({target for target, _ in native_builds(load()["jobs"])}))
def test_native_legs_and_their_smokes_carry_no_bucket(target):
    """A build leg stages through the pinned seam; the job env must carry no credentials.

    The job-level env is inherited by every step that does not declare its own override.
    A credential-bearing step in the same job is only valid if it is the credential gate
    (tested by ``test_the_signed_leg_credential_gate_still_refuses_on_the_same_vars``)
    or is justified by ``test_residual_credentials_are_justified_by_an_r2_bound_command``.
    """
    jobs = load()["jobs"]
    legs = {name for mode in ("release", "commit") for (t, mode), name in native_builds(jobs).items()
            if t == target}
    legs |= {name for t, name in smoke_callers(jobs).items() if t == target}
    failures = []
    for name in sorted(legs):
        job = jobs[name]
        offenders = _r2_keys(job.get("env") or {})
        if offenders:
            failures.append(f"{name} job env exports {offenders}")
    assert not failures, "\n".join(failures)


def test_handoff_seam_steps_are_handed_no_credentials():
    """Every step that runs the handoff CLI resolves its store from the pin alone.

    Staging/fetching through ``scripts.releases.handoff`` never calls
    ``r2.credentials()`` while the run is pinned, so a seam step that still carries
    CLOUDFLARE_R2_* is either dead weight or the first inch of a rollback.
    """
    failures = []
    for name, job in load()["jobs"].items():
        for _, step in _run_steps(job):
            if HANDOFF_SEAM not in step.get("run", ""):
                continue
            offenders = _r2_keys(_env_node(job, step))
            if offenders:
                label = step.get("name", f"step #{_}")
                failures.append(f"{name}/{label}: seam step exports {offenders}")
    assert not failures, "\n".join(failures)


def test_the_signed_leg_credential_gate_still_refuses_on_the_same_vars():
    """Migrating the store may not delete a credential check from a publishing leg.

    The darwin gate's refusal list is part of the gate, and the vars it reads must
    be declared where the check runs: a job-level env that later disappears would
    turn a refusal into a silent pass on the empty string.
    """
    jobs = load()["jobs"]
    failures = []
    for (target, mode), name in native_builds(jobs).items():
        if target not in {"darwin-arm64", "darwin-x64"} or mode != "release":
            continue
        gate = credential_gate(jobs[name])
        run = gate.get("run", "")
        for var in ("CLOUDFLARE_R2_PUBLIC_URL", "CLOUDFLARE_R2_BUCKET"):
            if f'-z "$' not in run or var not in run:
                failures.append(f"{name}: the gate no longer refuses on {var}")
            if gate.get("env", {}).get(var) is None:
                failures.append(f"{name}: the gate reads {var} but does not declare it")
        # The signing vars remain the gate's own declarations: the migration must
        # not have quietly narrowed what a publishing leg refuses on.
        for var in ("CSC_LINK", "CSC_KEY_PASSWORD", "APPLE_API_KEY_P8",
                    "APPLE_API_KEY_ID", "APPLE_API_ISSUER"):
            if gate.get("env", {}).get(var) is None:
                failures.append(f"{name}: the gate lost its {var} declaration")
    assert not failures, "\n".join(failures)


def test_residual_credentials_are_justified_by_an_r2_bound_command():
    """Every remaining CLOUDFLARE_R2_* export sits on a node that still needs it.

    The residue is a migration ledger, not a backlog of habits: a step exports the
    bucket's env only when its own commands (or the composite action it invokes,
    which the workflow cannot re-plumb from here) still reach the bucket. A new
    export beside a seam command fails this test; so does keeping credentials for a
    node whose R2-bound caller has since been migrated.
    """
    failures = []
    for name, job in load()["jobs"].items():
        job_offenders = _r2_keys(job.get("env") or {})
        if job_offenders:
            body = " ".join(f"{step.get('run', '')} {step.get('uses', '')} {step.get('with', '')}"
                            for step in job.get("steps") or [])
            if not any(mark in body for mark in R2_BOUND_MARKS):
                failures.append(f"{name}: job exports {job_offenders} with no R2-bound command")
        for index, step in _run_steps(job):
            offenders = _r2_keys(step.get("env") or {})
            if not offenders:
                continue
            justified = any(mark in step["run"] for mark in R2_BOUND_MARKS)
            justified = justified or (HANDOFF_SEAM in step["run"] and name in LEGACY_R2_CLI_JOBS)
            if not justified:
                label = step.get("name", f"step #{index}")
                failures.append(f"{name}/{label}: exports {offenders} but runs no R2-bound command")
    assert not failures, "\n".join(failures)


def test_only_the_legacy_feed_cli_steps_invoke_the_r2_module():
    """No seam-reachable step may call the bucket transport CLI directly.

    ``python -m scripts.releases.r2 ...`` addresses the bucket with no store seam;
    every such call site must be the documented darwin-feed legacy until a seam for
    that transport lands, and a new one is a regression of this migration.
    """
    offenders = []
    for name, job in load()["jobs"].items():
        for _, step in _run_steps(job):
            if "-m scripts.releases.r2 " in step.get("run", ""):
                offenders.append(name)
    assert set(offenders) <= set(LEGACY_R2_CLI_JOBS), offenders
