"""The launch home is pinned once the process serves several profiles (#119242).

``nastech_constants.pin_process_nastech_home`` (salvaged from #119129) gives the four routed-profile
decisions one stable launch-home identity; ``set_multiplex_active(True)`` pins it automatically for
a multiplexing gateway/dashboard, since neither calls the pin itself. Two contracts around that:

* ``get_process_nastech_home()`` / ``get_nastech_home()`` keep following ``NASTECH_HOME`` while the
  pin holds — a host's env mirror exists so override-less readers see the served profile, and an
  env-only home switch (``profiles._cleanup_gateway_service``) must not resolve to the launch home.
* Deactivation releases only the pin activation itself created: an embedding host's explicit pin
  survives the transient toggles in ``gateway_migrate._multiplex_read_mode`` and cron workers.
"""
from __future__ import annotations

import pytest

import nastech_constants
from agent.secret_scope import serves_routed_profile, set_multiplex_active
from nastech_constants import (
    get_nastech_home,
    get_process_nastech_home,
    get_routing_process_nastech_home,
    reset_nastech_home_override,
    set_nastech_home_override,
)


@pytest.fixture
def homes(tmp_path, monkeypatch):
    launch = tmp_path / "launch"
    served = tmp_path / "profiles" / "served"
    launch.mkdir()
    served.mkdir(parents=True)
    monkeypatch.setenv("NASTECH_HOME", str(launch))
    monkeypatch.setattr(nastech_constants, "_PINNED_PROCESS_NASTECH_HOME", None, raising=False)
    return launch, served


def test_multiplex_activation_pins_the_launch_home_but_env_readers_still_follow_the_env(homes, monkeypatch):
    launch, served = homes
    set_multiplex_active(True)
    monkeypatch.setenv("NASTECH_HOME", str(served))  # the host's per-turn mirror
    assert get_routing_process_nastech_home() == launch
    # Only routing DECISIONS are frozen; override-less readers see what the env names.
    assert get_process_nastech_home() == served
    assert get_nastech_home() == served
    set_multiplex_active(False)
    # The auto-pin is released with the mode: a standalone process follows the env again.
    assert get_routing_process_nastech_home() == served
    token = set_nastech_home_override(served)
    try:
        assert not serves_routed_profile()
    finally:
        reset_nastech_home_override(token)


def test_an_explicit_host_pin_survives_a_transient_multiplex_toggle(homes, monkeypatch):
    """#119242 contract: the embedding host pins once; ``_multiplex_read_mode`` / a cron worker
    flipping the mode True→False in the same process must not drop it."""
    launch, served = homes
    nastech_constants.pin_process_nastech_home(launch)
    monkeypatch.setenv("NASTECH_HOME", str(served))
    token = set_nastech_home_override(served)
    try:
        set_multiplex_active(True)
        set_multiplex_active(False)
        assert get_routing_process_nastech_home() == launch
        assert serves_routed_profile()
    finally:
        reset_nastech_home_override(token)
