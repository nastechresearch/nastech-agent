"""Unit tests for scripts/docker_rebootstrap_nastech_session.py.

The boot-time re-seed is the load-bearing "does not clobber a healthy session"
guard: it may overwrite the on-disk Nastech provider entry when that entry is
provably terminal (quarantine marker + no usable tokens), or when an
orchestrator seed is demonstrably newer. Older/incomparable seeds must no-op.
These are pure-stdlib tmp_path tests (no container build).
"""
from __future__ import annotations

import importlib.util
import os
import json
from pathlib import Path

# Import the stdlib-only boot helper by path (it lives under scripts/, not an
# installed package) — mirrors the repo's other scripts/-helper tests.
_SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "docker_rebootstrap_nastech_session.py"
_spec = importlib.util.spec_from_file_location("docker_rebootstrap_nastech_session", _SCRIPT)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def _terminal_nastech_state():
    """On-disk shape after a terminal quarantine: tokens cleared, marker set."""
    return {
        "portal_base_url": "https://portal.example.com",
        "client_id": "nastech-cli-vps",
        "last_auth_error": {
            "provider": "nastech",
            "code": "invalid_grant",
            "relogin_required": True,
        },
    }


def _healthy_nastech_state():
    return {
        "portal_base_url": "https://portal.example.com",
        "client_id": "nastech-cli-vps",
        "access_token": "live-at",
        "refresh_token": "live-rt",
    }


def _write_auth(tmp_path: Path, providers: dict) -> str:
    p = tmp_path / "auth.json"
    p.write_text(json.dumps({"version": 1, "providers": providers}))
    return str(p)


_FRESH_SEED = json.dumps({
    "version": 1,
    "providers": {
        "nastech": {
            "portal_base_url": "https://portal.example.com",
            "client_id": "nastech-cli-vps",
            "access_token": "FRESH-at",
            "refresh_token": "FRESH-rt",
        }
    },
})


def test_reseeds_terminal_entry(tmp_path):
    """Terminal on-disk entry + valid seed → providers.nastech replaced."""
    auth = _write_auth(tmp_path, {"nastech": _terminal_nastech_state()})
    result = mod.reseed_if_terminal(auth, _FRESH_SEED)
    assert result == "reseeded"
    store = json.loads(Path(auth).read_text())
    assert store["providers"]["nastech"]["refresh_token"] == "FRESH-rt"
    assert "last_auth_error" not in store["providers"]["nastech"]


def test_does_not_clobber_healthy_entry(tmp_path):
    """LOAD-BEARING: a healthy (live-token) entry must never be overwritten."""
    auth = _write_auth(tmp_path, {"nastech": _healthy_nastech_state()})
    result = mod.reseed_if_terminal(auth, _FRESH_SEED)
    assert result == "not_terminal"
    store = json.loads(Path(auth).read_text())
    # Untouched — still the live tokens, not the seed.
    assert store["providers"]["nastech"]["refresh_token"] == "live-rt"


def test_marker_but_live_token_is_not_terminal(tmp_path):
    """Stale marker + a live token present → NOT terminal (don't clobber)."""
    state = _terminal_nastech_state()
    state["refresh_token"] = "somehow-live"
    auth = _write_auth(tmp_path, {"nastech": state})
    assert mod.reseed_if_terminal(auth, _FRESH_SEED) == "not_terminal"


def test_timezone_less_local_timestamp_is_incomparable(tmp_path):
    auth = _write_auth(tmp_path, {"nastech": {
        **_healthy_nastech_state(),
        "obtained_at": "2026-07-14T19:00:00",
    }})
    seed = json.dumps({
        "providers": {
            "nastech": {
                "client_id": "nastech-cli-vps",
                "access_token": "FRESH-at",
                "refresh_token": "FRESH-rt",
                "obtained_at": "2026-07-14T19:05:00Z",
            }
        },
    })

    assert mod.reseed_if_terminal(auth, seed) == "not_terminal"


def test_terminal_entry_missing_marker_is_not_terminal(tmp_path):
    """No last_auth_error at all (e.g. a merely-expired but not-quarantined
    entry) → not terminal, no re-seed."""
    auth = _write_auth(tmp_path, {"nastech": {"client_id": "nastech-cli-vps"}})
    assert mod.reseed_if_terminal(auth, _FRESH_SEED) == "not_terminal"


def test_stale_temp_from_a_killed_prior_run_does_not_block_reseed(tmp_path):
    """Boot-hook PIDs repeat inside a container: a temp left by a SIGKILL'd run must never make
    the next re-seed fail (main() swallows the exception, so the recovery path would be dead)."""
    home = tmp_path / "home"
    home.mkdir()
    auth = _write_auth(home, {"nastech": _terminal_nastech_state()})
    stale = Path(f"{auth}.rebootstrap.{os.getpid()}.tmp")
    stale.write_text("{torn", encoding="utf-8")

    assert mod.reseed_if_terminal(auth, _FRESH_SEED) == "reseeded"
    store = json.loads(Path(auth).read_text())
    assert store["providers"]["nastech"]["refresh_token"] == "FRESH-rt"
    assert sorted(p.name for p in home.iterdir()) == sorted(["auth.json", stale.name]), "no new temp survives"
