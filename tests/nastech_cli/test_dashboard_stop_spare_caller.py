"""Root selection for ``dashboard --stop`` / update cleanup must spare the caller.

The argv substring scan (``_DASHBOARD_PATTERNS``) matches any process whose command
line merely mentions ``nastech dashboard`` / ``nastech serve`` — including the shell the
``--stop`` was typed into (``bash -c 'nastech dashboard --stop'``). Killing it takes down
the invoking terminal; the historical fix for the hosted-TUI case is descendant hygiene
(#113819), which is orthogonal to root selection.
"""

from __future__ import annotations

from unittest.mock import patch

from nastech_cli.dashboard_procs import _is_caller_wrapper_shell
from nastech_cli.main_dashboard import _find_stale_dashboard_pids


def test_scan_spares_only_the_callers_wrapper_shell(capsys):
    """The bash the ``--stop`` was typed into is dropped; the real backend and an unrelated
    wrapper with the same argv shape (another user's ``bash -c 'nastech serve'``) stay targets."""
    processes = [
        (111, "/opt/nastech/bin/python nastech dashboard --port 9119"),
        (222, "bash -c nastech dashboard --stop"),
        (333, "bash -c nastech serve"),
    ]
    with (
        patch("nastech_cli.dashboard_procs._scan_dashboard_processes", return_value=processes),
        patch("nastech_cli.dashboard_procs._caller_ancestor_pids", return_value={222}),
        patch("nastech_cli.dashboard_procs._argv_head_command",
              side_effect=lambda pid: "bash" if pid in (222, 333) else "python3.12"),
    ):
        assert _find_stale_dashboard_pids() == [111, 333]


def test_python_headed_or_unreadable_ancestor_stays_killed():
    """A python-headed ancestor is a real backend (hosted TUI case) and must stay stoppable —
    ``--stop`` from inside the dashboard's own TUI — and an unreadable argv head is never spared."""
    with patch("nastech_cli.dashboard_procs._argv_head_command", return_value="python3.12"):
        assert _is_caller_wrapper_shell(4242, {4242}) is False
    with patch("nastech_cli.dashboard_procs._argv_head_command", return_value=None):
        assert _is_caller_wrapper_shell(4242, {4242}) is False
    with patch("nastech_cli.dashboard_procs._argv_head_command", return_value="bash"):
        assert _is_caller_wrapper_shell(4242, {4242}) is True
