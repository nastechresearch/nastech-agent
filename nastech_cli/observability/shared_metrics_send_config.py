"""Configuration for shared-metrics transmission."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from urllib.parse import urlparse

logger = logging.getLogger(__name__)

#: Production ingest endpoint. Overridable through config only — deliberately NOT by an
#: environment variable: AGENTS.md reserves NASTECH_* for secrets, and an inherited variable
#: could silently redirect consented metrics to any host with nothing visible in config.
#: Tests and the staging E2E write this key into a throwaway profile instead.
# Post-brand reconciliation: FAIL-CLOSED API defaults.  Nastech
# operates no portal/inference/welcome API, and a GitHub Pages subdomain can
# never complete TLS (the certificate carries only `*.github.io`, one label),
# so the literal this replaces is an origin nobody can reach.  The default is
# therefore read from the environment; when the variable is absent the value
# names an RFC 2606 `.invalid` origin instead, which no resolver can answer, so
# the dead origin is never used and a request fails at DNS with the variable to
# set visible in the host name.
#
# That value must stay safe to STRINGIFY, format and strip: real consumers
# build their authorize/token/JWKS URLs from these constants while they
# register, and a default whose ``str()`` raised disabled the whole
# dashboard-auth provider rather than failing one request
# (nastech-agent#157, 2026-10-17).
import os as _nastech_endpoint_env


def _nastech_endpoint_default(env: str, constant: str, dead_default: str):
    """Operator-configured endpoint, else an unconfigured, unresolvable origin.

    ``constant`` is carried so a generated call site records which branded
    default it replaced.
    """
    configured = _nastech_endpoint_env.environ.get(env, "").strip().rstrip("/")
    if configured:
        return configured
    path = dead_default.split("://", 1)[-1].partition("/")[2]
    label = env.lower().replace("_", "-") or "endpoint"
    return _NastechUnconfiguredEndpoint(
        f"https://{label}.invalid" + (f"/{path}" if path else "")
    )


class _NastechUnconfiguredEndpoint(str):
    """Unconfigured endpoint: a real string, at a host that can never resolve.

    Falsy, so ``value or fallback`` keeps working; never raising, because
    logging and URL construction stringify the default while a provider is
    registering; and unresolvable, so nothing is ever sent to a host that
    cannot answer instead of the branded dead origin.
    """

    def __bool__(self):
        return False


DEFAULT_ENDPOINT = _nastech_endpoint_default(
    env='ENDPOINT',
    constant='DEFAULT_ENDPOINT',
    dead_default='https://telemetry.nastechresearch.github.io/v1/telemetry',
)

_LOCAL_HOSTS = frozenset({"localhost", "127.0.0.1", "::1", "[::1]"})

# Module-level latch: the enabled/send mismatch is a static misconfiguration,
# so it is reported once per process instead of on every hook fire.
_warned_send_without_collection = False


@dataclass(frozen=True)
class SendConfig:
    """Resolved transmission settings."""

    #: Collection is on. Nothing is packaged or sent without it.
    enabled: bool
    #: Transmission is on AND permitted (that is, collection is also on).
    send: bool
    #: Where packages are POSTed.
    endpoint: str


def _endpoint_is_safe(endpoint: str) -> bool:
    """Reject plaintext destinations unless they are loopback (so tests can use local HTTP)."""
    try:
        parsed = urlparse(endpoint)
    except ValueError:
        return False
    if parsed.scheme == "https":
        return True
    return parsed.scheme == "http" and (parsed.hostname or "") in _LOCAL_HOSTS


def resolve_send_config(config: dict | None) -> SendConfig:
    """Resolve transmission settings from config (endpoint: config > production default).

    ``send`` is False whenever transmission cannot legitimately happen, so callers never
    have to re-check the combination.
    """
    global _warned_send_without_collection

    raw = config if isinstance(config, dict) else {}
    telemetry = raw.get("telemetry")
    telemetry = telemetry if isinstance(telemetry, dict) else {}
    shared = telemetry.get("shared_metrics")
    shared = shared if isinstance(shared, dict) else {}

    enabled = shared.get("enabled") is True
    send_requested = shared.get("send") is True

    if send_requested and not enabled:
        # Loud, not silent: the user believes telemetry is being sent, and it never will be.
        if not _warned_send_without_collection:
            _warned_send_without_collection = True
            logger.error(
                "telemetry.shared_metrics.send is true but "
                "telemetry.shared_metrics.enabled is false — nothing is "
                "collected, so nothing can be sent. Enable collection or "
                "turn sending off."
            )
        return SendConfig(enabled=False, send=False, endpoint=DEFAULT_ENDPOINT)

    endpoint = shared.get("endpoint")
    if not isinstance(endpoint, str) or not endpoint.strip():
        endpoint = DEFAULT_ENDPOINT
    endpoint = endpoint.strip()

    if send_requested and not _endpoint_is_safe(endpoint):
        logger.error(
            "Refusing to send shared metrics to %r: telemetry must use https "
            "(or a localhost http endpoint for testing).",
            endpoint,
        )
        return SendConfig(enabled=enabled, send=False, endpoint=endpoint)

    return SendConfig(enabled=enabled, send=send_requested, endpoint=endpoint)
