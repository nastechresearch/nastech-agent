"""The published release must actually carry the files it advertises.

Measured 2026-10-29: `publish_release` flipped `--draft=false` for a canary
without uploading anything -- every artifact stayed in R2 and the release had
`assets=0`, which is why no size or download has ever existed on a GitHub
release and why the R2 bucket could not be retired.
"""

import json

import pytest

from scripts.releases import channel_releases


def test_release_assets_picks_installers_metadata_and_feeds(tmp_path):
    (tmp_path / "nested").mkdir()
    for name in (
        "Nastech-1.0-mac-arm64.dmg",
        "Nastech-1.0-mac-arm64.zip",
        "Nastech-1.0-mac-arm64.dmg.blockmap",
        "Nastech-1.0-win-x64.exe",
        "Nastech-1.0-win.msixbundle",
        "canary.yml",
        "metadata-darwin-arm64.json",
        "build.log",
    ):
        (tmp_path / name).write_text("x", encoding="utf-8")
    (tmp_path / "sub").mkdir()
    (tmp_path / "sub" / "deep.zip").write_text("x", encoding="utf-8")

    found = [p.rsplit("/", 1)[-1] for p in channel_releases.release_assets(tmp_path)]
    assert found == sorted([
        "Nastech-1.0-mac-arm64.dmg", "Nastech-1.0-mac-arm64.zip",
        "Nastech-1.0-mac-arm64.dmg.blockmap", "Nastech-1.0-win-x64.exe",
        "Nastech-1.0-win.msixbundle", "canary.yml", "deep.zip",
    ])


def test_upload_assets_attaches_everything_and_refuses_an_empty_stage(tmp_path):
    (tmp_path / "a.zip").write_text("x", encoding="utf-8")
    calls = []
    channel_releases.upload_assets("v1.0.0", "o/r", tmp_path, run=calls.append)
    # a stable tag also writes the pointer installers resolve, and both files go
    # in one batched call
    assert len(calls) == 1
    assert calls[0][:5] == ["gh", "release", "upload", "v1.0.0", "--repo"]
    uploaded = [arg.rsplit("/", 1)[-1] for arg in calls[0][7:]]
    assert uploaded == ["a.zip", "latest.json"]

    empty = tmp_path / "empty"
    empty.mkdir()
    # an empty stage is refused before anything uploads; for a stable tag the
    # manifest writer is what notices first, and its message names the reason
    with pytest.raises(channel_releases.ChannelError, match="no installer"):
        channel_releases.upload_assets("v1.0.0", "o/r", empty, run=calls.append)


def test_prune_canaries_keeps_the_newest_and_never_touches_stable():
    rows = [
        {"tagName": "v0.22.0", "isPrerelease": False, "createdAt": "2026-10-29T00:00:00Z"},
        {"tagName": "v0.21.0+canary.20261029T120000Z", "isPrerelease": True,
         "createdAt": "2026-10-29T12:00:00Z"},
        {"tagName": "v0.21.0+canary.20261029T110000Z", "isPrerelease": True,
         "createdAt": "2026-10-29T11:00:00Z"},
        {"tagName": "v0.21.0+canary.20261029T100000Z", "isPrerelease": True,
         "createdAt": "2026-10-29T10:00:00Z"},
        {"tagName": "v0.21.0+canary.20261029T090000Z", "isPrerelease": True,
         "createdAt": "2026-10-29T09:00:00Z"},
    ]
    calls = []

    def run(argv):
        calls.append(argv)
        if argv[:3] == ["gh", "release", "list"]:
            return json.dumps(rows)
        return ""

    deleted = channel_releases.prune_canaries("o/r", keep=3, run=run)
    # four canaries, keep three: exactly the oldest goes, and the stable release
    # is never a candidate no matter how old it is
    assert deleted == ["v0.21.0+canary.20261029T090000Z"]
    assert all(call[:3] == ["gh", "release", "delete"] for call in calls[1:])
    # the tag is an attempt reference: delete the release, never the tag
    assert all("--cleanup-tag" not in call for call in calls)
