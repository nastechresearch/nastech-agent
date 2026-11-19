"""Every workflow that moves handoff bytes uses the default R2 store.

Unset, `scripts.releases.handoff.store()` resolves the store by the bucket variable, so
every leg of the plane stages and reads the same R2 objects. The old `github` pin pointed
`handoff stage` at `gh release upload` on a claim tag with no Release object: a 404 that
left each attempt with zero assets and no builds table. Leaving the seam unpinned is what
keeps a staging job and a fetching job on the one store that actually holds the bytes.
"""
from pathlib import Path

from ruamel.yaml import YAML

ROOT = Path(__file__).resolve().parents[2]
HANDOFF_SEAM = "RELEASE_HANDOFF_STORE"
# The legs stage, the smoke reads, and the controller merges: one plane, one choice.
HANDOFF_PLANE = ("desktop-bundled-release.yml", "desktop-bundle-smoke.yml", "stable-release.yml")


def workflow_env(name):
    workflow = YAML(typ="base").load((ROOT / ".github/workflows" / name).read_text(encoding="utf-8"))
    return workflow.get("env") or {}


def test_the_handoff_plane_uses_the_default_r2_store_end_to_end():
    chosen = {name: workflow_env(name).get(HANDOFF_SEAM) for name in HANDOFF_PLANE}
    pinned = [name for name, pin in chosen.items() if pin is not None]
    assert not pinned, f"{pinned} repoint the handoff plane off the R2 bucket default"


def test_the_stable_controller_does_not_pin_a_seam_its_reader_ignores():
    """The channel seam stays unpinned until the head advance moves store and origin together.

    `r2.public_base_url()` already answers `RELEASE_CHANNEL_STORE=github` with a Pages origin,
    while `channel_releases` still builds an `R2ChannelStore` here, so pinning the channel seam
    in this workflow would name one store's bytes with another store's public URL.
    """
    assert "RELEASE_CHANNEL_STORE" not in workflow_env("stable-release.yml")
