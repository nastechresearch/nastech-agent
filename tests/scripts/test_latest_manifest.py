"""Installers resolve one stable URL: releases/latest/download/latest.json.

GitHub resolves `<repo>/releases/latest/download/<asset>` to the newest
*published* release, so uploading a manifest as an asset gives a permanent
address without a bucket, without a Pages build and without spending the
unauthenticated API budget (60 requests/hour/IP) on every install.
"""

import json

import pytest

from scripts.releases import channel_releases


def _stage(tmp_path):
    tmp_path.mkdir(parents=True, exist_ok=True)
    for name in ("Nastech-0.22.0-mac-arm64.dmg", "Nastech-0.22.0-mac-arm64.zip",
                 "Nastech-0.22.0-mac-arm64.dmg.blockmap", "latest.yml"):
        (tmp_path / name).write_bytes(name.encode())
    return tmp_path


def test_a_stable_release_publishes_the_pointer(tmp_path):
    root = _stage(tmp_path)
    path = channel_releases.write_latest_manifest("v0.22.0", "o/r", root)
    payload = json.loads(path.read_text(encoding="utf-8"))

    assert payload["tag"] == "v0.22.0"
    assert payload["version"] == "0.22.0"
    names = [asset["name"] for asset in payload["assets"]]
    # installers only: the updater feed and blockmaps are not install targets
    assert names == ["Nastech-0.22.0-mac-arm64.dmg", "Nastech-0.22.0-mac-arm64.zip"]
    first = payload["assets"][0]
    assert first["url"] == "https://github.com/o/r/releases/download/v0.22.0/" \
                           "Nastech-0.22.0-mac-arm64.dmg"
    assert first["size"] == len("Nastech-0.22.0-mac-arm64.dmg")
    assert len(first["sha256"]) == 64


def test_uploading_a_stable_release_writes_the_pointer_but_a_canary_does_not(tmp_path):
    stable = _stage(tmp_path / "stable")
    calls = []

    def run(argv, **kwargs):
        calls.append(argv)
        return ""

    channel_releases.upload_assets("v0.22.0", "o/r", stable, run=run)
    assert (stable / "latest.json").is_file()
    uploaded = [arg.rsplit("/", 1)[-1] for call in calls
                if call[:3] == ["gh", "release", "upload"] for arg in call[7:]]
    assert "latest.json" in uploaded

    canary = _stage(tmp_path / "canary")
    calls.clear()
    channel_releases.upload_assets("v0.22.0+canary.20261029T120000Z", "o/r", canary, run=run)
    assert not (canary / "latest.json").exists()


def test_a_stage_with_no_installer_is_refused(tmp_path):
    (tmp_path / "latest.yml").write_text("x", encoding="utf-8")
    with pytest.raises(channel_releases.ChannelError, match="no installer"):
        channel_releases.write_latest_manifest("v0.22.0", "o/r", tmp_path)
