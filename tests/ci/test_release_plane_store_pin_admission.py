"""Every leg that moves receipt-bound release bytes names the store it reads them from.

`scripts.releases.handoff.store()` resolves the store from three signals, and the
run-wide pin is the first of them; unset, the non-secret bucket variable decides
(handoff.py's own fallback). That is enough to lose a release: the legs stage their
packages as draft release assets, while a later leg that *fetches* them sees a
populated bucket variable and asks the object store for keys nobody wrote -- work
that succeeded, read back as a missing handoff. PR #212 moved the bundled workflow's
admission leg onto the seam; this is the same contract for the whole publication
plane, including the stable publication pass that runs the sequencer.

The scenario each leg is replayed in is the one that broke: the bucket variable and
the bucket's public origin both populated, as they stay for an r2-selected run. A leg
that resolves its store from those values instead of from the pin names an origin the
GitHub-native plane never writes, and a test that only checked the pin's presence
would never see it.
"""
from __future__ import annotations

import re
from pathlib import Path

import nastech_yaml
import pytest

from scripts.releases import gh_transport, handoff

# The entry points whose reads and writes go through `handoff.store()`. A workflow
# that starts running one of these is a leg of this plane whether or not anyone
# remembered to add it here.
STORE_ENTRY_POINTS = (
    "scripts.releases.channel_publish",
    "scripts.releases.channel_releases",
    "scripts.releases.commit_build",
    "scripts.releases.handoff",
    "scripts.releases.sequencer",
)
# The stale-but-configured bucket a fork that moved to GitHub releases still carries.
BUCKET = "nastech-releases"
BUCKET_ORIGIN = "https://nastech-assets.nastechresearch.workers.dev"
REPOSITORY = "nastechresearch/nastech-agent"
RELEASE_ORIGIN = f"https://github.com/{REPOSITORY}/releases/download"
# The seam's own inputs: cleared before a leg's declared env is applied, so only
# what the workflow itself declares decides which store the leg resolves.
SEAM_KEYS = ("RELEASE_HANDOFF_STORE", "RELEASE_CHANNEL_STORE", "CLOUDFLARE_R2_BUCKET",
             "CLOUDFLARE_R2_PUBLIC_URL", "R2_DISPOSABLE_RUN")
_EXPRESSION = re.compile(r"\$\{\{([^{}]*)\}\}")


def _rendered(value: str) -> str:
    """A workflow env value with each `${{ }}` replaced by a configured stand-in.

    Only the non-secret inputs the seam reads get a real value: the bucket variable
    and its public origin, because populating them is what selects the wrong store.
    Secrets and computed contexts are non-empty placeholders -- this is about which
    store a leg resolves, not about what it uploads.
    """
    def one(match: re.Match) -> str:
        expression = match.group(1).strip()
        if expression == "vars.CLOUDFLARE_R2_BUCKET":
            return BUCKET
        if expression == "vars.CLOUDFLARE_R2_PUBLIC_URL":
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
def test_a_leg_of_the_publication_plane_selects_the_pinned_store(leg, monkeypatch):
    """The run's pin, not the bucket variable, decides which store a leg reads."""
    _enter(PLANE[leg], monkeypatch)
    resolved = handoff.store()
    assert resolved is gh_transport, (
        f"{leg} resolves {resolved.__name__} from the bucket variable: its legs stage draft "
        "release assets, so this fetch asks an object store for keys nothing wrote")


@pytest.mark.parametrize("leg", sorted(PLANE))
def test_no_leg_names_the_bucket_as_its_archive_origin(leg, monkeypatch):
    """The origin a leg publishes comes from its store, never from a bucket variable.

    A pinned leg either answers this repository's release-download route, or refuses
    the foreign origin outright; quietly serving bucket URLs is the bug.
    """
    declared = _enter(PLANE[leg], monkeypatch)
    try:
        origin = handoff.archive_origin(declared.get("CLOUDFLARE_R2_PUBLIC_URL") or None)
    except ValueError:
        return
    assert origin != BUCKET_ORIGIN, (
        f"{leg} names {BUCKET_ORIGIN} as the origin of bytes staged to the release archive")
    assert origin == RELEASE_ORIGIN, f"{leg} resolves the archive origin to {origin}"
