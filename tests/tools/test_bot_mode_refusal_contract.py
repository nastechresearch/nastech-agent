from types import SimpleNamespace


def test_one_shot_cli_preserves_refusal_reason(monkeypatch, capsys):
    from cli import NastechCLI
    from nastech_cli import active_sessions
    refusal = active_sessions.ActiveSessionRefusal("Ce chat est occupé.", reason=active_sessions.SESSION_NOT_OWNED)
    monkeypatch.setattr(active_sessions, "try_acquire_active_session", lambda **kwargs: (None, refusal))
    cli = SimpleNamespace(_active_session_lease=None, session_id="isolated", config={})
    assert not NastechCLI._claim_active_session(cli, stderr=True)
    assert "nastech-refusal-reason: SESSION_NOT_OWNED\n" in capsys.readouterr().err
