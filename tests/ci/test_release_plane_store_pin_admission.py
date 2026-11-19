"""Every leg of the publication plane reads handoff bytes from the R2 store.

`scripts.releases.handoff.store()` resolves the store from three signals, in
order: the `RELEASE_HANDOFF_STORE` run pin, an explicit public archive origin,
and finally the bucket variable. A GitHub pin sent `handoff stage` to
`gh release upload` on a claim tag with no Release object (HTTP 404), while the
build legs stage signed objects to R2, leaving every attempt with zero assets.
With the pin gone each leg must reach R2 through the configured bucket or an
explicit public R2 origin.
"""
from __future__ import annotations

import re
from pathlib import Path

import nastech_yaml
import pytest

from scripts.releases import handoff, r2

# Entry points whose reads and writes go through `handoff.store()`. A workflow
# that starts running one of these is a leg of this plane whether or not anyone
# remembered to add it here. `commit_build` is deliberately absent: it creates a
# git tag and never touches the handoff store.
STORE_ENTRY_POINTS = (
    "scripts.releases.channel_publish",
    "scripts.releases.channel_releases",
    "scripts.releases.handoff",
    "scripts.releases.sequencer",
)
# The R2 bucket a configured run stages into, and its public origin.
BUCKET = "nastech-assets"
BUCKET_ORIGIN = "https://nastech-assets.nastechresearch.workers.dev"
REPOSITORY = "nastechresearch/nastech-agent"
# The seam's own inputs: cleared before a leg's declared env is applied, so only
# what the workflow itself declares decides which store the leg resolves.
SEAM_KEYS = ("RELEASE_HANDOFF_STORE", "RELEASE_CHANNEL_STORE", "CLOUDFLARE_R2_BUCKET",
             "CLOUDFLARE_R2_PUBLIC_URL", "R2_DISPOSABLE_RUN", "PUBLIC_BASE")
_EXPRESSION = re.compile(r"\$\{\{([^{}]*)\}\}")


def _rendered(value: str) -> str:
    """A workflow env value with each `${{ }}` replaced by a configured stand-in.

    Only the non-secret inputs the seam reads get real values: the bucket variable
    and its public origin (including the smoke workflow's dispatched inputs),
    because populating them is what selects the store an unpinned leg resolves.
    Secrets and computed contexts are non-empty placeholders -- this is about which
    store a leg resolves, not about what it uploads.
    """
    def one(match: re.Match) -> str:
        expression = match.group(1).strip()
        if expression in ("vars.CLOUDFLARE_R2_BUCKET",):
            return BUCKET
        if (expression in ("vars.CLOUDFLARE_R2_PUBLIC_URL", "inputs.public-base",
                           "inputs.public-root")
                or expression.endswith(".outputs.public-root")
                or expression.endswith(".outputs.public-base")):
            # `validate` publishes the store's own origin as both outputs, and
            # every build/fetch leg reads it back rather than naming a URL of its
            # own. A GitHub-pinned run used to publish the Pages origin here; the
            # R2 store now publishes the bucket's origin.
            return BUCKET_ORIGIN
        if expression.startswith("secrets."):
            return "configured-secret"
        if expression.startswith("github.token"):
            return "runner-token"
        return ""

    return _EXPRESSION.sub(one, str(value))


def _legs(workflow: dict) -> list[tuple[str, dict]]:
    """(leg, declared env) for each step of *workflow* that reads or writes the store.

    A step's env is the run's, the job's and its own merged: that whole mapping is
    what the product sees, so it is what gets replayed.
    """
    run_env = workflow.get("env") or {}
    legs = []
    for job_id, job in (workflow.get("jobs") or {}).items():
        if not isinstance(job, dict):
            continue
        job_env = {**run_env, **(job.get("env") or {})}
        for number, step in enumerate(job.get("steps") or [], start=1):
            script = step.get("run") or ""
            if not any(entry in script for entry in STORE_ENTRY_POINTS):
                continue
            name = step.get("name") or step.get("id") or f"step {number}"
            legs.append((f"{job_id}/{name}", {**job_env, **(step.get("env") or {})}))
    return legs


def _plane() -> dict[str, dict]:
    """Every leg of every release workflow in the repository, found by what it runs."""
    root = Path(__file__).resolve().parents[2]
    plane = {}
    for path in sorted((root / ".github" / "workflows").glob("*.yml")):
        for leg, env in _legs(nastech_yaml.safe_load(path.read_text(encoding="utf-8-sig"))):
            plane[f"{path.name}: {leg}"] = env
    assert plane, "walk broken: no workflow leg reaches the release store"
    return plane


# Parsed once: the parametrization and each test read the same walk.
PLANE = _plane()


def _enter(leg_env: dict, monkeypatch: pytest.MonkeyPatch) -> dict:
    """Put the process env in the state a runner would hand this leg."""
    for key in SEAM_KEYS:
        monkeypatch.delenv(key, raising=False)
    declared = {key: _rendered(value) for key, value in leg_env.items()}
    for key, value in declared.items():
        monkeypatch.setenv(key, value)
    monkeypatch.setenv("GITHUB_REPOSITORY", REPOSITORY)
    return declared


@pytest.mark.parametrize("leg", sorted(PLANE))
def test_every_leg_of_the_publication_plane_uses_r2(leg, monkeypatch):
    """The bucket or an explicit R2 origin, not a legacy pin, selects the store."""
    declared = _enter(PLANE[leg], monkeypatch)
    public_base = declared.get("PUBLIC_BASE") or declared.get("CLOUDFLARE_R2_PUBLIC_URL") or None
    resolved = handoff.store(public_base)
    assert resolved is r2, (
        f"{leg} resolves {resolved.__name__}: a GitHub handoff stages draft assets "
        "that the R2 publication legs cannot read")


@pytest.mark.parametrize("leg", sorted(PLANE))
def test_every_leg_names_the_bucket_as_its_archive_origin(leg, monkeypatch):
    """The origin a leg publishes is the R2 public URL, never a GitHub release route."""
    declared = _enter(PLANE[leg], monkeypatch)
    origin = handoff.archive_origin(declared.get("CLOUDFLARE_R2_PUBLIC_URL") or None)
    assert origin == BUCKET_ORIGIN, f"{leg} resolves the archive origin to {origin}"
