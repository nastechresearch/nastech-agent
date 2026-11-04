"""Every workflow that moves handoff bytes names the store it moves them through.

Unset, `scripts.releases.handoff.store()` resolves the store by the bucket variable, so a
controller that consumes another workflow's staged bytes can silently read the object store
while the legs wrote draft release assets -- work that succeeded, read back as a missing
handoff. Naming the store in each workflow is what keeps a staging job and a fetching job
inside one release from disagreeing.
"""
from pathlib import Path

from ruamel.yaml import YAML

ROOT = Path(__file__).resolve().parents[2]
SEAMS = ("RELEASE_HANDOFF_STORE", "RELEASE_CHANNEL_STORE")
# The legs stage, the smoke reads, and the controller merges: one plane, one choice.
HANDOFF_PLANE = ("desktop-bundled-release.yml", "desktop-bundle-smoke.yml", "stable-release.yml")


def store_pins(name):
    workflow = YAML(typ="base").load((ROOT / ".github/workflows" / name).read_text(encoding="utf-8"))
    env = workflow.get("env") or {}
    missing = [key for key in SEAMS if key not in env]
    assert not missing, f"{name} leaves the store to the bucket variable default: {missing}"
    return {key: env[key] for key in SEAMS}


def test_the_handoff_plane_selects_the_same_store_end_to_end():
    chosen = {name: store_pins(name) for name in HANDOFF_PLANE}
    github = dict(zip(SEAMS, ("github", "github")))
    assert all(pins == github for pins in chosen.values()), chosen
