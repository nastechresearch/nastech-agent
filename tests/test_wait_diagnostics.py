"""Host-independent invariants for the Windows harness wait diagnostics."""

from __future__ import annotations

import pytest

from tests.e2e.core.windows._helpers import wait_until


def test_wait_until_success_returns_value_without_calling_evidence():
    calls: list[int] = []
    assert wait_until(lambda: "ready", 0.05, "the thing",
                      evidence=lambda: calls.append(1)) == "ready"
    assert calls == []


def test_wait_until_timeout_reports_caller_evidence(monkeypatch):
    monkeypatch.setattr("tests.e2e.core.windows._helpers.MADE_HOMES", [])
    with pytest.raises(AssertionError) as caught:
        wait_until(lambda: False, 0.01, "the thing",
                   evidence=lambda: "CONPTY tail: hello")
    text = str(caught.value)
    assert "timed out after 0.01s waiting for the thing" in text
    assert "polls)" in text
    assert "caller evidence:" in text and "CONPTY tail" in text
