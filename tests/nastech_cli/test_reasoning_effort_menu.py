from nastech_cli.main_provider_setup import _prompt_reasoning_effort_selection
from nastech_cli.setup import _current_reasoning_effort


def test_reasoning_menu_orders_minimal_before_low(monkeypatch):
    captured = {}

    def _fake_radiolist(title, items, *, selected=0, cancel_returns=None, description=None):
        captured["items"] = items
        captured["selected"] = selected
        return selected  # pick the pre-selected (current) entry

    monkeypatch.setattr("nastech_cli.curses_ui.curses_radiolist", _fake_radiolist)

    selected = _prompt_reasoning_effort_selection(
        ["low", "minimal", "medium", "high"],
        current_effort="medium",
    )

    assert selected == "medium"
    assert [item.split()[0] for item in captured["items"][:4]] == [
        "minimal",
        "low",
        "medium",
        "high",
    ]


def test_current_reasoning_effort_reads_dict_form():
    """The setup wizard's "currently in use" lookup must see the dict form's tier (or `none`
    when it disables thinking), never `str(dict)`."""
    assert _current_reasoning_effort({"agent": {"reasoning_effort": {"enabled": True, "effort": "Thinking"}}}) == "thinking"
    assert _current_reasoning_effort({"agent": {"reasoning_effort": {"enabled": False}}}) == "none"
    assert _current_reasoning_effort({"agent": {"reasoning_effort": "high"}}) == "high"


def test_nastech_model_offers_reasoning_whenever_a_pick_is_saved(tmp_path, monkeypatch):
    """Same model ID on a new provider, or a re-pick of the current model, still gets the effort
    step (like chat /model); a flow that saves nothing does not."""
    from nastech_cli import main
    from nastech_cli.auth import _save_model_choice
    from nastech_cli.config import load_config, save_config

    monkeypatch.setenv("NASTECH_HOME", str(tmp_path))
    save_config({**load_config(), "model": {"default": "m", "provider": "openrouter"}})
    prompted = []
    monkeypatch.setattr("nastech_cli.main_provider_setup._prompt_main_reasoning_effort",
                        lambda model, provider: prompted.append((model, provider)))
    monkeypatch.setattr(main, "_clear_stale_openai_base_url", lambda: None)

    def _pick_same_model_on_nastech(config, current_model, args):
        _save_model_choice(current_model)
        save_config({**load_config(), "model": {"default": current_model, "provider": "nastech"}})

    for slug, flow, expected in (("nastech", _pick_same_model_on_nastech, [("m", "nastech")]),
                                 ("anthropic", lambda c, m, a: print("No change."), [])):
        prompted.clear()
        monkeypatch.setattr(main, "_pick_provider", lambda *a, _s=slug, **k: _s)
        monkeypatch.setitem(main._PROVIDER_MODEL_FLOWS, slug, flow)
        main.select_provider_and_model()
        assert prompted == expected
