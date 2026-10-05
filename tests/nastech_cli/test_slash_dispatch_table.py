"""Slash-command dispatch semantics in cli.NastechCLI.

The pre-dispatch side effects (pre_command hook, pending-resume reset,
unknown-command fallthrough) and return semantics must hold.
"""
from unittest.mock import MagicMock, patch

from cli import NastechCLI


def _cli():
    c = NastechCLI.__new__(NastechCLI)
    c._pending_resume_sessions = ["x"]
    c.session_id = "s1"
    c.config = {}
    return c


def test_dispatch_return_semantics_and_side_effects():
    c = _cli()
    with patch.object(NastechCLI, "_toggle_yolo", return_value=None) as m, \
            patch("nastech_cli.plugins.fire_pre_command_hook") as hook:
        assert c.process_command("/yolo") is True
        m.assert_called_once_with()
        hook.assert_called_once()
        assert hook.call_args.kwargs["command"] == "yolo"
    assert c._pending_resume_sessions is None  # non-resume command disarms it

    c = _cli()
    with patch.object(NastechCLI, "_handle_resume_command") as m:
        assert c.process_command("/resume 2") is True
        m.assert_called_once_with("/resume 2")
    assert c._pending_resume_sessions == ["x"]

    c = _cli()
    assert c.process_command("/exit") is False
    c = _cli()
    with patch.object(NastechCLI, "_handle_handoff_command", return_value=False):
        assert c.process_command("/handoff telegram") is False
    with patch.object(NastechCLI, "_handle_handoff_command", return_value=True):
        assert c.process_command("/handoff telegram") is True
    with patch.object(NastechCLI, "_handle_update_command", return_value=True):
        assert c.process_command("/update") is False
    with patch.object(NastechCLI, "_handle_update_command", return_value=False):
        assert c.process_command("/update") is True


def test_unknown_command_falls_through():
    c = _cli()
    c._console_print = MagicMock()
    with patch.object(NastechCLI, "_process_unregistered_slash", return_value=True) as m:
        assert c.process_command("/definitely-not-a-command x") is True
        m.assert_called_once_with("/definitely-not-a-command x", "/definitely-not-a-command x")
