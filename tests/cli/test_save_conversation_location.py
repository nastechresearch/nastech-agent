"""Tests for /save — the conversation snapshot slash command.

Regression: the old implementation wrote ``nastech_conversation_<ts>.json``
to the current working directory (CWD). Users who ran /save expected the
file to be discoverable via ``nastech sessions browse``, but CWD-resident
snapshots are not indexed in the state DB and are generally invisible.
The fix writes snapshots under ``~/.nastech/sessions/saved/`` and prints
the absolute path plus the resume hint for the live session.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace

import pytest


@pytest.fixture
def nastech_home(tmp_path, monkeypatch):
    home = tmp_path / ".nastech"
    home.mkdir()
    monkeypatch.setattr(Path, "home", lambda: tmp_path)
    monkeypatch.setenv("NASTECH_HOME", str(home))
    # Clear any cached nastech_home computation
    import nastech_constants
    if hasattr(nastech_constants, "_nastech_home_cache"):
        nastech_constants._nastech_home_cache = None
    return home


def _make_stub_cli(history):
    """Build a minimal object exposing just what save_conversation uses."""
    return SimpleNamespace(
        conversation_history=history,
        model="test-model",
        session_id="20260101_120000_abc123",
        session_start=datetime(2026, 1, 1, 12, 0, 0),
    )


def test_save_conversation_writes_under_nastech_home(nastech_home, tmp_path, monkeypatch, capsys):
    """Snapshot must land under ~/.nastech/sessions/saved/, not CWD."""
    # Change CWD to a different directory to prove the file does NOT go there.
    work = tmp_path / "somewhere-else"
    work.mkdir()
    monkeypatch.chdir(work)

    # Import fresh to pick up the NASTECH_HOME fixture
    for mod in [m for m in sys.modules if m.startswith("cli") or m == "nastech_constants"]:
        sys.modules.pop(mod, None)

    import cli  # noqa: F401  (module under test)

    stub = _make_stub_cli([
        {"role": "user", "content": "hi"},
        {"role": "assistant", "content": "hello"},
    ])

    # Call the unbound method against our stub.
    cli.NastechCLI.save_conversation(stub, "/save json")

    # File must NOT be in CWD
    cwd_leak = list(work.glob("nastech_conversation_*.json"))
    assert not cwd_leak, f"snapshot leaked to CWD: {cwd_leak}"

    # File MUST be under ~/.nastech/sessions/saved/
    saved_dir = nastech_home / "sessions" / "saved"
    assert saved_dir.is_dir(), "expected saved/ subdirectory to be created"
    files = list(saved_dir.glob("nastech_conversation_*.json"))
    assert len(files) == 1, files

    payload = json.loads(files[0].read_text())
    assert payload["model"] == "test-model"
    # /save now emits the canonical export_session shape: the session id
    # lives under "id" (was "session_id" in the legacy snapshot format).
    assert payload["id"] == "20260101_120000_abc123"
    assert payload["messages"] == [
        {"role": "user", "content": "hi"},
        {"role": "assistant", "content": "hello"},
    ]

    # User-facing message must include the absolute path AND the resume hint.
    out = capsys.readouterr().out
    assert str(files[0]) in out, out
    assert "nastech --resume 20260101_120000_abc123" in out, out


def test_save_conversation_empty_history_does_nothing(nastech_home, capsys):
    for mod in [m for m in sys.modules if m.startswith("cli") or m == "nastech_constants"]:
        sys.modules.pop(mod, None)
    import cli

    stub = _make_stub_cli([])
    cli.NastechCLI.save_conversation(stub, "/save json")

    saved_dir = nastech_home / "sessions" / "saved"
    assert not saved_dir.exists() or not list(saved_dir.iterdir())
    out = capsys.readouterr().out
    assert "No conversation to save" in out


def test_save_conversation_bare_shows_usage(nastech_home, capsys):
    """Bare /save prints the usage card and writes nothing."""
    for mod in [m for m in sys.modules if m.startswith("cli") or m == "nastech_constants"]:
        sys.modules.pop(mod, None)
    import cli

    stub = _make_stub_cli([{"role": "user", "content": "hi"}])
    cli.NastechCLI.save_conversation(stub, "/save")

    saved_dir = nastech_home / "sessions" / "saved"
    assert not saved_dir.exists() or not list(saved_dir.iterdir())
    out = capsys.readouterr().out
    # Usage card lists every format and the redact option
    for token in ("json", "md", "html", "redact", "Usage:"):
        assert token in out, (token, out)


def test_save_conversation_bad_format_shows_usage(nastech_home, capsys):
    for mod in [m for m in sys.modules if m.startswith("cli") or m == "nastech_constants"]:
        sys.modules.pop(mod, None)
    import cli

    stub = _make_stub_cli([{"role": "user", "content": "hi"}])
    cli.NastechCLI.save_conversation(stub, "/save pdf")

    saved_dir = nastech_home / "sessions" / "saved"
    assert not saved_dir.exists() or not list(saved_dir.iterdir())
    out = capsys.readouterr().out
    assert "Usage:" in out
