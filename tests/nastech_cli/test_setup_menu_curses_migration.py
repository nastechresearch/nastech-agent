"""Regression tests confirming the setup model/provider/reasoning pickers route
through the shared curses radiolist (ESC + arrow-key handling that works across
terminals, incl. Ghostty) instead of simple_term_menu.

Guards against silently regressing back to simple_term_menu, whose ESC/arrow
handling was unreliable in `nastech setup` (the provider->model sub-menu).
"""
from unittest.mock import patch


def test_prompt_model_selection_uses_curses_radiolist():
    from inspect import signature

    from nastech_cli import curses_ui
    from nastech_cli.auth import _prompt_model_selection
    from nastech_cli.curses_ui import radio_item_plain

    seen = {}
    # Reject an unsupported call against the live signature, never a copy of it:
    # a mirrored parameter list goes red on every upstream addition (`headings`,
    # added upstream in 15307dece7) while production stays correct.
    bind = signature(curses_ui.curses_radiolist).bind

    def _fake(*args, **kwargs):
        seen.update(bind(*args, **kwargs).arguments)
        return 1  # pick second model

    with patch("nastech_cli.curses_ui.curses_radiolist", side_effect=_fake), \
         patch("builtins.print"):
        result = _prompt_model_selection(["model-a", "model-b"])

    assert result == "model-b"
    assert seen["title"] == "Select default model:"
    # Items are the models plus the custom/skip entries. Model rows may be
    # rich (text, style) segments for sale chrome — compare the plain text.
    plain = [radio_item_plain(item) for item in seen["items"]]
    assert plain[:2] == ["model-a", "model-b"]
    assert "Skip (keep current)" in plain
    assert seen.get("search_labels") is not None
    assert len(seen["search_labels"]) == len(seen["items"])


def test_prompt_model_selection_esc_cancels():
    from nastech_cli.auth import _prompt_model_selection

    # curses_radiolist returns the cancel sentinel (-1) on ESC.
    with patch("nastech_cli.curses_ui.curses_radiolist", return_value=-1), \
         patch("builtins.print"):
        result = _prompt_model_selection(["model-a", "model-b"])

    assert result is None


def test_reasoning_effort_uses_curses_radiolist():
    from nastech_cli.main import _prompt_reasoning_effort_selection

    with patch("nastech_cli.curses_ui.curses_radiolist", return_value=2), \
         patch("builtins.print"):
        result = _prompt_reasoning_effort_selection(["low", "medium", "high"], current_effort="")

    assert result == "high"


