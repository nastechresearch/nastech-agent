"""pm.client must not fail a completed worker result because teardown is slow."""
from __future__ import annotations

import json
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest


def test_request_tolerates_slow_worker_exit_after_result(tmp_path, monkeypatch):
    # Fake worker: speaks the single-shot protocol, returns a result, then sleeps
    # longer than the old 5s post-result wait so the old code raised TimeoutExpired.
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

    import pm.client as client

    monkeypatch.setattr(client, "_worker_command", lambda spec, arguments, worker_path, environment: [sys.executable, "-I", str(worker)])
    monkeypatch.setattr(client, "runtime_environment", lambda: None)

    # Minimal operation spec; _request looks up OPERATIONS[operation]
    from pm.client import OPERATIONS

    op_name = next(iter(OPERATIONS))
    spec = OPERATIONS[op_name]
    # Build a request that matches the spec's expected argument shape.
    if spec.packages is not None:
        args = {}
        if "names" in spec.__dataclass_fields__ if False else False:
            pass
    # Use a simple operation: 'prune_cache' takes cache arg in worker, but easier to
    # bypass by calling _request with a real op name and harmless args.
    # 'doctor' takes no required packages in some setups? Let's be robust: monkeypatch
    # package_definitions and use prune_cache shape.
    monkeypatch.setattr("pm.registry.package_definitions", lambda names: [])

    result = client._request("prune_cache", {"cache": str(tmp_path / "cache")})
    assert result == "ok"
