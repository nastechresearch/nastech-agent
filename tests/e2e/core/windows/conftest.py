"""Windows lane teardown: a prompt auto-starts the profile's gateway, which outlives the turn."""

from __future__ import annotations

import contextlib

import pytest

from tests.e2e.core.windows import _helpers as H


@pytest.fixture(autouse=True)
def _stop_auto_started_gateways():
    first = len(H.MADE_HOMES)
    yield
    made, H.MADE_HOMES[first:] = H.MADE_HOMES[first:], []
    for home, since in made:
        if not H.owned_processes(home, since=since):
            continue
        with contextlib.suppress(Exception):
            H.nastech(home, "gateway", "stop", timeout=60)
        H.kill_owned(home, since=since)
        # psutil's kill() is asynchronous on Windows: without draining the ownership scan
        # here, a just-killed prompt/gateway can still be alive when the next test starts
        # and auto-starts another one. Poll until the scan is empty (bounded; a process we
        # cannot reap is reported by the runner's leftover check, not silently inherited).
        H.owned_survivors(home, since=since, timeout=10)
