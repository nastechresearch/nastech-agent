"""The daily install snapshot says who hosts the install (``hosting``: ``self_hosted`` or ``nastech_cloud``).

* ``nastech_cloud`` only when the environment says so (``NASTECH_HOSTING=nastech_cloud``, set by the hosting
  platform); anything else, or nothing, reads ``self_hosted``. The variable's raw value never leaves.
* A snapshot whose group chat counts could not be read still carries ``hosting``.
* Snapshots counted before the field existed still package against the v4 schema.
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from nastech_cli.observability import shared_metrics_contract as contract
from nastech_cli.observability.shared_metrics import SharedMetricsStore
from nastech_cli.observability.shared_metrics_snapshot import collect_install_snapshot

SCHEMA_PATH = (
    Path(__file__).resolve().parents[2] / "nastech_cli" / "observability" / "schemas"
    / "nastech.shared_metrics.v4.schema.json"
)
RESOURCE = {"architecture": "x86_64", "nastech_version": "test", "install_method": "git", "os_family": "linux"}


@pytest.fixture
def root_home(tmp_path, monkeypatch):
    home = tmp_path / "root"
    home.mkdir()
    monkeypatch.setenv("NASTECH_HOME", str(home))
    monkeypatch.delenv("NASTECH_HOSTING", raising=False)
    return home


@pytest.mark.parametrize(("value", "expected"), [
    (None, "self_hosted"),
    ("nastech_cloud", "nastech_cloud"),
    (" NASTECH_CLOUD ", "nastech_cloud"),
    ("", "self_hosted"),
    ("acme-private-host", "self_hosted"),
])
def test_snapshot_reads_hosting_from_the_environment(root_home, monkeypatch, value, expected):
    if value is not None:
        monkeypatch.setenv("NASTECH_HOSTING", value)

    snapshot = collect_install_snapshot({})

    assert snapshot["hosting"] == expected
    assert contract.counter_dimensions_are_valid(contract.INSTALL_SNAPSHOT_METRIC, snapshot), snapshot


def test_snapshot_without_readable_group_chats_keeps_hosting(root_home, monkeypatch):
    (root_home / "state.db").write_bytes(b"not a sqlite database" * 64)
    monkeypatch.setenv("NASTECH_HOSTING", "nastech_cloud")

    snapshot = collect_install_snapshot({})

    assert snapshot["hosting"] == "nastech_cloud"
    assert not any(k.startswith("group_chat_") for k in snapshot)
    assert contract.counter_dimensions_are_valid(contract.INSTALL_SNAPSHOT_METRIC, snapshot), snapshot


def test_a_row_with_hosting_but_no_other_new_field_is_not_a_valid_shape(root_home):
    # hosting and the group chat counts ship together, so an older row never has hosting alone.
    snapshot = collect_install_snapshot({})
    hosting_only = {k: v for k, v in snapshot.items() if not k.startswith("group_chat_")}
    hosting_only.pop("compression_prepare_ahead")
    assert not contract.counter_dimensions_are_valid(contract.INSTALL_SNAPSHOT_METRIC, hosting_only)


def test_snapshots_with_and_without_hosting_package_against_the_v4_schema(root_home, tmp_path, monkeypatch):
    jsonschema = pytest.importorskip("jsonschema")
    monkeypatch.setenv("NASTECH_HOSTING", "nastech_cloud")
    current = collect_install_snapshot({})
    before_upgrade = {k: v for k, v in current.items() if k != "hosting" and not k.startswith("group_chat_")}

    store = SharedMetricsStore(tmp_path / "metrics.sqlite3", tmp_path / "outbox")
    store.record_counter(contract.INSTALL_SNAPSHOT_METRIC, current, RESOURCE)
    store.record_counter(contract.INSTALL_SNAPSHOT_METRIC, before_upgrade, RESOURCE)
    [package_path] = store.create_and_export_package()
    package = json.loads(package_path.read_text(encoding="utf-8-sig"))
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8-sig"))
    jsonschema.Draft202012Validator(schema).validate(package)
    snapshots = [m["dimensions"] for m in package["metrics"] if m["name"] == contract.INSTALL_SNAPSHOT_METRIC]
    assert sorted(d.get("hosting", "absent") for d in snapshots) == ["absent", "nastech_cloud"]

    dimensions = schema["$defs"]["install_snapshot_counter"]["properties"]["dimensions"]
    assert "hosting" not in dimensions["required"]
    assert set(dimensions["properties"]["hosting"]["enum"]) == contract.HOSTINGS == {"nastech_cloud", "self_hosted"}
