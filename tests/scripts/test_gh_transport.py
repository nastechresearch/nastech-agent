"""The handoff transport moves to releases; the keys and receipts do not change."""

from pathlib import Path

import pytest

from scripts.releases import gh_transport


class Result:
    def __init__(self, returncode=0, stdout="", stderr=""):
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr


def test_a_staging_key_keeps_its_shape_and_becomes_a_flat_asset_name():
    key = gh_transport.staging_key("v0.22.0", "darwin-arm64", "bundle.zip")
    assert key == "releases/tag/v0.22.0/darwin-arm64/bundle.zip"
    flat = gh_transport.asset_name(key)
    assert "/" not in flat
    assert flat == "releases__tag__v0.22.0__darwin-arm64__bundle.zip"


def test_stage_uploads_the_leg_files_to_a_draft_release(tmp_path):
    (tmp_path / "bundle.zip").write_bytes(b"z")
    (tmp_path / "metadata-darwin-arm64.json").write_text("{}", encoding="utf-8")
    calls = []

    def run(argv, **kwargs):
        calls.append(argv)
        if argv[:3] == ["gh", "release", "view"]:
            return Result(returncode=1, stderr="not found")
        return Result()

    report = gh_transport.stage("v0.22.0", "o/r", "darwin-arm64", tmp_path,
                                ["*.zip", "metadata-*.json"], run=run)
    assert report["files"] == ["bundle.zip", "metadata-darwin-arm64.json"]
    assert calls[1][:3] == ["gh", "release", "create"]
    assert "--draft" in calls[1]
    upload = [c for c in calls if c[:3] == ["gh", "release", "upload"]][0]
    assert {Path(a).name for a in upload[7:]} == {"bundle.zip", "metadata-darwin-arm64.json"}


def test_stage_refuses_an_empty_leg(tmp_path):
    with pytest.raises(gh_transport.TransportError, match="no files matched"):
        gh_transport.stage("v0.22.0", "o/r", "darwin-arm64", tmp_path, ["*.zip"],
                           run=lambda *a, **k: Result())


def test_fetch_refuses_a_tag_with_nothing_staged(tmp_path):
    with pytest.raises(gh_transport.TransportError, match="nothing was staged"):
        gh_transport.fetch("v0.22.0", "o/r", ["darwin-arm64"], tmp_path, ["*.zip"],
                           run=lambda *a, **k: Result())
