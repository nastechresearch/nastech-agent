"""No test reaches a live Nastech service unless it is a ``live`` canary (``tests/conftest.py``).

A test home has no Nastech identity, so a hosted connector action used to mint a real guest on
the production Portal: seconds per test, red when the Portal was slow, and a new production
guest on every CI run.
"""

import socket

import pytest


def test_first_connector_action_in_a_test_home_mints_no_portal_guest():
    from nastech_cli import anon_auth
    from tools.connectors.gateway.config import ensure_guest_identity

    failure = ensure_guest_identity()

    assert failure and failure.startswith("Hosted connectors could not be set up.")
    assert not anon_auth.has_guest()


@pytest.mark.parametrize("host", ["portal.nastechresearch.github.io", "inference-api.nastechresearch.github.io",
                                  b"WELCOME-API.NASTECHRESEARCH.GITHUB.IO.", "telemetry.staging-nastechresearch.github.io"])
def test_nastech_hosts_are_refused_at_the_name_lookup(host):
    with pytest.raises(socket.gaierror, match="test fence"):
        socket.getaddrinfo(host, 443)
