"""HTTP client for the agent routes of the config plane (contract.md §7.1, §7.2).

Plain HTTP (D9), stdlib only: it runs inside ``load_nastech_dotenv`` before most of Nastech is
imported. Every request re-resolves the bearer (contract §10.2).
"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional

from .credentials import plane_token
from .destination import checked_url, display_url, open_credentialed

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


DEFAULT_URL = _nastech_endpoint_default(
    env='URL',
    constant='DEFAULT_URL',
    dead_default='https://config-config.nastechresearch.github.io',
)
URL_ENV = "NASTECH_CONFIG_REMOTE_URL"
INSTANCE_ENV = "NASTECH_CONFIG_INSTANCE_ID"
_HTTP_TIMEOUT_S = 15.0


@dataclass(frozen=True)
class Response:
    status: int
    body: dict[str, Any]
    etag: Optional[str]
    retry_after: Optional[float]

    @property
    def error(self) -> str:
        return str(self.body.get("error") or f"http_{self.status}")

    @property
    def message(self) -> str:
        return str(self.body.get("message") or f"HTTP {self.status}")


class TransportError(RuntimeError):
    """The request never produced an HTTP response (DNS, connect, TLS, timeout)."""


def base_url() -> str:
    """The configured plane origin (+ path prefix), as configured: :func:`request` checks it
    against the credential destination policy before anything is sent. Messages use :func:`shown_url`."""
    return (os.environ.get(URL_ENV, "").strip() or DEFAULT_URL).rstrip("/")


def shown_url() -> str:
    """:func:`base_url` without any user info, for messages, ``describe()`` and provenance."""
    return display_url(base_url())


def instance_id() -> str:
    return os.environ.get(INSTANCE_ENV, "").strip()


def _parse_body(raw: bytes) -> dict[str, Any]:
    if not raw:
        return {}
    try:
        data = json.loads(raw.decode("utf-8"))
    except ValueError:
        return {}
    return data if isinstance(data, dict) else {}


def _retry_after(value: Optional[str]) -> Optional[float]:
    try:
        return float(value) if value else None
    except ValueError:
        return None


def bearer(home: Path) -> str:
    """``home``'s plane bearer, resolved only once the plane destination passed the policy."""
    checked_url(base_url(), env_name=URL_ENV)
    return plane_token(home)


def request(method: str, home: Path, profile: str, *, etag: Optional[str] = None,
            body: Optional[dict[str, Any]] = None, token: Optional[str] = None) -> Response:
    """One call to ``/v1/config/self?profile=<profile>`` as ``home``'s agent, with ``token`` (a
    :func:`bearer` the caller resolved) or a bearer resolved here.

    The destination is checked before the bearer is resolved, and the request never follows a
    redirect (:mod:`.destination`): raises its :class:`CredentialDestinationError` instead."""
    plane = checked_url(base_url(), env_name=URL_ENV)
    url = f"{plane}/v1/config/self?{urllib.parse.urlencode({'profile': profile})}"
    headers = {
        "Authorization": f"Bearer {token or plane_token(home)}",
        "X-Nastech-Instance-Id": instance_id(),
        "Accept": "application/json",
    }
    data = None
    if body is not None:
        data = json.dumps(body, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        headers["Content-Type"] = "application/json"
    if etag:
        headers["If-None-Match"] = etag
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with open_credentialed(req, timeout=_HTTP_TIMEOUT_S) as resp:
            return Response(resp.status, _parse_body(resp.read()), resp.headers.get("ETag"),
                            _retry_after(resp.headers.get("Retry-After")))
    except urllib.error.HTTPError as exc:  # every non-2xx, including 304
        with exc:
            raw = exc.read() if exc.fp is not None else b""
        return Response(exc.code, _parse_body(raw), exc.headers.get("ETag") if exc.headers else None,
                        _retry_after(exc.headers.get("Retry-After") if exc.headers else None))
    except (urllib.error.URLError, OSError, TimeoutError) as exc:
        raise TransportError(f"{method} {url}: {getattr(exc, 'reason', exc)}") from exc
