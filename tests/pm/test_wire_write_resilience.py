"""PM wire writes must surface OS pipe errors cleanly.

Windows can raise OSError(errno=22, Invalid argument) when writing to a pipe
whose read end is closed/broken. The worker/client must not crash with a raw
traceback on the final result send.
"""
from __future__ import annotations

import errno
import os

import pytest


def test_worker_write_json_line_raises_clean_error_on_einval(monkeypatch):
    from pm.worker import _write_json_line

    def bad_write(fd, data):
        raise OSError(errno.EINVAL, "Invalid argument")

    monkeypatch.setattr(os, "write", bad_write)
    monkeypatch.setattr("time.sleep", lambda *_: None)
    with pytest.raises(RuntimeError, match="PM worker wire write failed"):
        _write_json_line(1, {"id": "x", "type": "result", "result": "ok"})


def test_worker_write_json_line_raises_clean_error_on_epipe(monkeypatch):
    from pm.worker import _write_json_line

    def bad_write(fd, data):
        raise BrokenPipeError(errno.EPIPE, "Broken pipe")

    monkeypatch.setattr(os, "write", bad_write)
    with pytest.raises(RuntimeError, match="PM worker wire write failed"):
        _write_json_line(1, {"id": "x", "type": "result", "result": "ok"})


def test_worker_write_json_line_retries_blocking_io(monkeypatch):
    from pm.worker import _write_json_line

    calls = []

    def flaky_write(fd, data):
        calls.append(bytes(data))
        if len(calls) == 1:
            raise BlockingIOError(errno.EAGAIN, "Resource temporarily unavailable")
        return len(data)

    monkeypatch.setattr(os, "write", flaky_write)
    monkeypatch.setattr("select.select", lambda *a, **k: ([], [1], []))
    _write_json_line(1, {"id": "x", "ok": True})
    assert len(calls) >= 2


def test_client_write_json_line_raises_clean_error_on_einval(monkeypatch):
    from pm.client import _write_json_line

    def bad_write(fd, data):
        raise OSError(errno.EINVAL, "Invalid argument")

    monkeypatch.setattr(os, "write", bad_write)
    monkeypatch.setattr("time.sleep", lambda *_: None)
    with pytest.raises(RuntimeError, match="PM client wire write failed"):
        _write_json_line(1, {"id": "x", "type": "callback", "call": 1})


def test_worker_write_json_line_retries_einval_then_succeeds(monkeypatch):
    from pm.worker import _write_json_line

    calls = []

    def flaky_write(fd, data):
        calls.append(bytes(data))
        if len(calls) < 3:
            raise OSError(errno.EINVAL, "Invalid argument")
        return len(data)

    monkeypatch.setattr(os, "write", flaky_write)
    monkeypatch.setattr("time.sleep", lambda *_: None)
    _write_json_line(1, {"id": "x", "ok": True})
    assert len(calls) == 3


def test_client_write_json_line_retries_einval_then_succeeds(monkeypatch):
    from pm.client import _write_json_line

    calls = []

    def flaky_write(fd, data):
        calls.append(bytes(data))
        if len(calls) < 3:
            raise OSError(errno.EINVAL, "Invalid argument")
        return len(data)

    monkeypatch.setattr(os, "write", flaky_write)
    monkeypatch.setattr("time.sleep", lambda *_: None)
    _write_json_line(1, {"id": "x", "ok": True})
    assert len(calls) == 3
