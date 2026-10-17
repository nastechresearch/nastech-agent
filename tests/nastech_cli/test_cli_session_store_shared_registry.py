"""The CLI's session store is the gateway's, never a state.db writer in the CLI process.

Main acquired ``nastech_state_registry`` (a writer handle) at startup. Rewired, the gateway is the
single writer: ``_init_session_store`` builds a ``GatewaySessionStore`` and opens no SessionDB.
"""

from types import SimpleNamespace

from cli import NastechCLI


def test_cli_session_store_is_the_gateway_store_and_opens_no_writer(monkeypatch):
    import nastech_state_registry
    from nastech_cli.gateway_session_store import GatewaySessionStore

    constructed = []
    monkeypatch.setattr(nastech_state_registry, "_open_session_db", lambda path: constructed.append(path))
    cli = SimpleNamespace()
    NastechCLI._init_session_store(cli)
    assert isinstance(cli._session_db, GatewaySessionStore) and not cli._session_db_unavailable
    assert constructed == []
