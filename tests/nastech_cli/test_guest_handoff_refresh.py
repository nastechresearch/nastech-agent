"""A token refresh renews the identity the shared Nastech store holds; only a sign-in replaces it.

A keepalive refresh of one profile's account used to overwrite a guest another profile had just
minted into the shared store. That recorded a move of the guest's apps into the account, and the
profile that had logged out of the account adopted it again from the store.
"""

from __future__ import annotations

import os
from types import SimpleNamespace

import httpx
import pytest

from tests.nastech_cli import test_guest_handoff as _gh

portal = _gh.portal


def _refresh_access_token():
    from nastech_cli import auth
    auth.resolve_nastech_access_token(refresh_skew_seconds=10**9)


def _refresh_runtime_credentials():
    from nastech_cli import auth
    auth.resolve_nastech_runtime_credentials(force_refresh=True)


REFRESHERS = {
    "resolve_nastech_access_token": _refresh_access_token,
    "resolve_nastech_runtime_credentials": _refresh_runtime_credentials,
}


def _shared_anon_token():
    from nastech_cli import auth_nastech
    return (auth_nastech._read_shared_nastech_state() or {}).get("anon_token")


def _guest_in(monkeypatch, home) -> str:
    """*home* mints a guest into the (empty) shared store."""
    monkeypatch.setenv("NASTECH_HOME", str(home))
    return _gh._mint_guest()


@pytest.mark.parametrize("refresh", sorted(REFRESHERS))
def test_a_refresh_over_a_guest_in_the_shared_store_records_no_move(portal, monkeypatch, tmp_path, refresh):
    from nastech_cli import auth_nastech
    mine, sibling = os.environ["NASTECH_HOME"], tmp_path / "sibling-profile"
    sibling.mkdir()
    _gh._persist(_gh._account())
    auth_nastech._clear_shared_nastech_state("logout")
    anon = _guest_in(monkeypatch, sibling)

    monkeypatch.setenv("NASTECH_HOME", mine)
    REFRESHERS[refresh]()

    assert portal.refreshes == 1
    assert _gh._records() == {} and portal.claims == []
    assert _shared_anon_token() == anon


@pytest.mark.parametrize("emptied", [False, True], ids=["store-holds-it", "store-emptied-by-a-logout"])
def test_a_refresh_still_publishes_the_rotated_token_for_profiles_on_the_same_account(portal, emptied):
    from nastech_cli import auth_nastech
    _gh._persist(_gh._account(refresh="rt_1"))
    if emptied:
        auth_nastech._clear_shared_nastech_state("logout")
    _refresh_access_token()
    assert auth_nastech._read_shared_nastech_state()["refresh_token"] == "rt_2"


def test_a_sign_in_over_the_guest_in_the_shared_store_still_hands_it_over(portal, monkeypatch, tmp_path):
    mine, sibling = os.environ["NASTECH_HOME"], tmp_path / "sibling-profile"
    sibling.mkdir()
    anon = _guest_in(monkeypatch, sibling)

    monkeypatch.setenv("NASTECH_HOME", mine)
    _gh._persist(_gh._account())

    assert [c["body"] for c in portal.claims] == [{"token": anon}]
    assert _gh._only_record()["state"] == "claimed"


def test_a_keepalive_refresh_does_not_sign_a_logged_out_profile_back_in(portal, monkeypatch, tmp_path):
    """Two profiles on one account; the first logs out and mints a guest; the second refreshes."""
    from nastech_cli import anon_auth, auth
    first, second = os.environ["NASTECH_HOME"], tmp_path / "second-profile"
    second.mkdir()
    _gh._persist(_gh._account())
    monkeypatch.setenv("NASTECH_HOME", str(second))
    _gh._persist(_gh._account())

    monkeypatch.setenv("NASTECH_HOME", first)
    auth.logout_command(SimpleNamespace(provider="nastech"))
    anon = _gh._mint_guest()

    monkeypatch.setenv("NASTECH_HOME", str(second))
    from nastech_cli import nastech_auth_keepalive
    assert nastech_auth_keepalive.refresh_nastech_auth_keepalive_once(min_access_ttl_seconds=10**9)

    monkeypatch.setenv("NASTECH_HOME", first)
    state = anon_auth.ensure_portal_identity(explicit=True)
    assert anon_auth.is_guest_state(state) and state["anon_token"] == anon
    assert _gh._records() == {} and portal.claims == []


def test_profiles_sharing_an_account_stay_in_step_while_the_store_holds_a_guest(portal, monkeypatch, tmp_path):
    """Refresh tokens are single use: a profile that refreshes with one a sibling already spent is
    signed out. Siblings on one account learn each rotated token through the shared store."""
    from nastech_cli import anon_auth, auth
    spent, answer = set(), portal.handler

    def single_use_refresh(request):
        if request.url.path == "/api/oauth/token":
            token = request.headers.get("x-nastech-refresh-token")
            if token in spent:
                return httpx.Response(400, json={"error": "refresh_token_reused"})
            spent.add(token)
        return answer(request)

    portal.handler = single_use_refresh
    first, second, third = os.environ["NASTECH_HOME"], tmp_path / "second-profile", tmp_path / "third-profile"
    _gh._persist(_gh._account())
    for home in (second, third):
        home.mkdir()
        monkeypatch.setenv("NASTECH_HOME", str(home))
        assert anon_auth.ensure_portal_identity(explicit=True)["refresh_token"] == "rt_1"   # adopts the account

    monkeypatch.setenv("NASTECH_HOME", first)
    auth.logout_command(SimpleNamespace(provider="nastech"))
    anon = _gh._mint_guest()
    for home in (second, first, third):   # the guest's own token refresh sits between the two
        monkeypatch.setenv("NASTECH_HOME", str(home))
        _refresh_access_token()

    assert auth.get_provider_auth_state("nastech")["refresh_token"] == "rt_3"
    assert _shared_anon_token() == anon and _gh._records() == {}
    fourth = tmp_path / "fourth-profile"
    fourth.mkdir()
    monkeypatch.setenv("NASTECH_HOME", str(fourth))
    adopted = anon_auth.ensure_portal_identity(explicit=True)
    assert adopted["anon_token"] == anon and "renewal" not in adopted
