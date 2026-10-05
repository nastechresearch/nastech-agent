"""Uninstall sweeps every leftover: both LaunchAgent label patterns, macOS
Library app-store entries and the XDG cache/data dirs outside NASTECH_HOME
(#62209 — uninstalls reported success yet launchd respawned the gateway and
Library/XDG dirs survived until manually removed)."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

from nastech_cli import uninstall


@pytest.fixture
def fake_home(tmp_path, monkeypatch):
    home = tmp_path / "home"
    home.mkdir()
    monkeypatch.setattr(Path, "home", classmethod(lambda cls: home))
    return home


# ── LaunchAgent sweep: both label patterns ──────────────────────────────


@pytest.fixture
def launch_agents(fake_home, monkeypatch):
    agents = fake_home / "Library" / "LaunchAgents"
    agents.mkdir(parents=True)
    monkeypatch.setattr(
        uninstall, "get_launchd_plist_path",
        lambda: agents / "ai.nastech.gateway.plist", raising=False,
    )
    # _remove_launchd_gateway imports it from nastech_cli.gateway at call time.
    import nastech_cli.gateway as gateway
    monkeypatch.setattr(gateway, "get_launchd_plist_path", lambda: agents / "ai.nastech.gateway.plist")
    return agents


def _fake_launchctl(monkeypatch, calls):
    def fake_run(cmd, **kwargs):
        calls.append(list(cmd))
        return subprocess.CompletedProcess(cmd, 0)
    monkeypatch.setattr(uninstall.subprocess, "run", fake_run)


def test_remove_launchd_gateway_sweeps_both_label_patterns(launch_agents, monkeypatch):
    current = launch_agents / "ai.nastech.gateway.plist"
    profiled = launch_agents / "ai.nastech.gateway-work.plist"
    legacy = launch_agents / "io.nastechresearch.nastech-agent.gateway.plist"
    unrelated = launch_agents / "com.other.agent.plist"
    for p in (current, profiled, legacy, unrelated):
        p.write_text("<plist/>", encoding="utf-8")

    calls: list[list[str]] = []
    _fake_launchctl(monkeypatch, calls)

    assert uninstall._remove_launchd_gateway() is True
    assert not current.exists() and not profiled.exists() and not legacy.exists()
    assert unrelated.exists()  # never touch another app's agent
    labels = {c[-1].rsplit("/", 1)[-1] for c in calls if c[1] == "bootout"}
    assert labels == {"ai.nastech.gateway", "ai.nastech.gateway-work",
                      "io.nastechresearch.nastech-agent.gateway"}
    assert all(c[1] == "unload" for c in calls if c[1] == "unload")


def test_remove_launchd_gateway_returns_false_when_no_plists(launch_agents, monkeypatch):
    calls: list[list[str]] = []
    _fake_launchctl(monkeypatch, calls)
    assert uninstall._remove_launchd_gateway() is False
    assert calls == []


# ── macOS Library + XDG leftovers ────────────────────────────────────────


@pytest.mark.skipif(sys.platform != "darwin", reason="macOS Library layout")
def test_remove_desktop_app_leftovers_removes_nastech_library_entries(fake_home):
    library = fake_home / "Library"
    ours = []
    for parent, name in (
        ("Caches", "com.nastechresearch.nastech"),
        ("Logs", "Nastech"),
        ("WebKit", "com.nastechresearch.nastech"),
        ("HTTPStorages", "com.nastechresearch.nastech"),
        ("Saved Application State", "com.nastechresearch.nastech.savedState"),
    ):
        d = library / parent / name
        d.mkdir(parents=True)
        ours.append(d)
    (library / "Caches" / "com.other.vendor").mkdir(parents=True)  # untouched

    removed = uninstall.remove_desktop_app_leftovers(full_uninstall=False)

    assert all(not d.exists() for d in ours)
    assert (library / "Caches" / "com.other.vendor").exists()
    assert len(removed) == len(ours)


def test_xdg_cache_removed_and_data_mode_semantics(fake_home):
    cache = fake_home / ".cache" / "nastech"
    data = fake_home / ".local" / "share" / "nastech"
    cache.mkdir(parents=True)
    data.mkdir(parents=True)

    assert uninstall._xdg_leftover_paths(full_uninstall=False) == ([cache], [data])
    assert uninstall._xdg_leftover_paths(full_uninstall=True) == ([cache, data], [])

    removed = uninstall.remove_desktop_app_leftovers(full_uninstall=False)
    assert cache in removed and not cache.exists()
    assert data.exists()  # user data is preserved in keep-data mode


def test_xdg_data_removed_on_full_uninstall(fake_home):
    cache = fake_home / ".cache" / "nastech"
    data = fake_home / ".local" / "share" / "nastech"
    cache.mkdir(parents=True)
    data.mkdir(parents=True)

    removed = uninstall.remove_desktop_app_leftovers(full_uninstall=True)

    assert not cache.exists() and not data.exists()
    assert cache in removed and data in removed
