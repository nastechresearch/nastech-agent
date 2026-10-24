"""N86: every legacy-fallback verb from a ticket bound to a secondary profile runs in THAT profile.

Only ``@_profile_scoped`` handlers and two hand-fixed ones read the connection's profile; the
account connector path (``_profile_home(request.profile)`` with no ``profile``) and billing (which
ignores ``profile`` and resolves the Nastech token through the runtime scope) ran in the launch
profile, so bee's Ink connected accounts and charged top-ups on default's portal account.
"""
import threading
import types
from pathlib import Path

import pytest


@pytest.fixture
def homes(tmp_path, monkeypatch):
    from tui_gateway import server
    launch = tmp_path / 'root'
    bee = launch / 'profiles' / 'bee'
    bee.mkdir(parents=True)
    monkeypatch.setenv('NASTECH_HOME', str(launch))
    monkeypatch.setattr(server, '_nastech_home', launch)
    # The account connector path first mints a hosted guest (same stub as the sibling
    # connector RPC tests). This fork runs no portal, so that mint always fails and
    # `connectors.list` answers before ever reaching the profile-scoped client.
    monkeypatch.setattr('tools.connectors.ensure_guest_identity', lambda: None)
    monkeypatch.setattr('tools.connectors.managed.ensure_guest_identity', lambda: None)
    return server, launch, bee


def _call(server, profile_id, method, params):
    from gateway.runtime_bootstrap import _PURPOSE_CAPABILITIES
    from tui_gateway.ws_legacy_fallback import dispatch_legacy
    actor = types.SimpleNamespace(profile_id=str(profile_id), capabilities=frozenset(_PURPOSE_CAPABILITIES['interactive']))
    written, done = [], threading.Event()
    transport = types.SimpleNamespace(write=lambda frame: written.append(frame) or done.set() or True)
    reply = dispatch_legacy(server, {'jsonrpc': '2.0', 'id': 1, 'method': method, 'params': params}, transport, actor)
    return reply if reply is not None else (done.wait(10) and written[0])


def test_secondary_ticket_runs_connectors_and_billing_in_its_own_profile(homes, monkeypatch):
    import nastech_cli.nastech_billing
    import tools.connectors
    import tools.connectors.managed
    import tools.managed_tool_gateway
    from nastech_constants import get_nastech_home
    server, launch, bee = homes
    seen = []

    def rec(label):
        seen.append((label, Path(str(get_nastech_home())).resolve()))

    monkeypatch.setattr(tools.connectors, 'connectors_available', lambda *a, **k: True)
    monkeypatch.setattr(tools.managed_tool_gateway, 'read_nastech_access_token', lambda: 'token')
    monkeypatch.setattr(tools.connectors.managed, 'managed_client',
                        lambda **_: types.SimpleNamespace(list_connectors=lambda: rec('list') or []))
    monkeypatch.setattr(nastech_cli.nastech_billing, 'post_charge', lambda **k: rec('charge') or {'chargeId': 'c'})
    for method, params in (('connectors.list', {'owner': {'type': 'account'}}), ('billing.charge', {'amount_usd': 5})):
        _call(server, bee, method, params)
    assert {label for label, _ in seen} == {'list', 'charge'}, seen
    assert {home for _, home in seen} == {bee.resolve()}, seen

    # The launch profile's own ticket is unchanged.
    seen.clear()
    _call(server, launch, 'billing.charge', {'amount_usd': 5})
    assert [home for _, home in seen] == [launch.resolve()]


def test_ticket_whose_home_vanished_is_refused_not_the_launch_profile(homes):
    server, _launch, bee = homes
    gone = bee.parent / 'gone'
    reply = _call(server, gone, 'billing.charge', {'amount_usd': 5})
    assert reply['error']['code'] == 4064, reply
