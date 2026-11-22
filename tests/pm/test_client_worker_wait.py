"""pm.client must not fail a completed worker result because teardown is slow."""
from __future__ import annotations

import json
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest


def test_request_tolerates_slow_worker_exit_after_result(tmp_path, monkeypatch):
    worker = tmp_path / "slow_exit_worker.py"
    worker.write_text(
        textwrap.dedent(
            """
            import json, sys, time
            req = json.loads(sys.stdin.readline())
            sys.stdout.write(json.dumps({"id": req["id"], "type": "result", "result": "ok", "receipt": None}) + "\\n")
            sys.stdout.flush()
            time.sleep(7)
            """
        ),
        encoding="utf-8",
    )

    from pm import client

    monkeypatch.setattr(client, "_worker_command", lambda spec, arguments, worker_path, environment: [sys.executable, "-I", str(worker)])
    monkeypatch.setattr(client, "runtime_environment", lambda: None)
    monkeypatch.setattr("pm.registry.package_definitions", lambda names: [])

    result = client._request("prune_cache", {"cache": str(tmp_path / "cache")})
    assert result == "ok"
