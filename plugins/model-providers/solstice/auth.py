"""Solstice sign-in: browser PKCE with a loopback redirect, token exchange and refresh brokered by the
Nastech portal (NAS), which holds the confidential client secret. Nastech keeps its own PKCE verifier and
the user's tokens; NAS never sees a prompt.

The generic ``nastech_cli.auth_oauth_pkce_plugin`` flow runs the browser leg, the credential-pool row
and the single-use-safe refresh. This module supplies only what is NAS-specific: the client config it
discovers and the token POSTs it brokers. Every NAS call carries the user's Nastech access token.
"""

from __future__ import annotations

from typing import Any, Dict, Mapping

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


DEFAULT_NAS_BASE_URL = _nastech_endpoint_default(
    env='NAS_BASE_URL',
    constant='DEFAULT_NAS_BASE_URL',
    dead_default='https://portal.nastechresearch.github.io',
)
_CONFIG_PATH = "/api/oauth/gemini-auth/config"
_TOKEN_PATHS = {"authorization_code": "/api/oauth/gemini-auth/exchange", "refresh_token": "/api/oauth/gemini-auth/refresh"}
_TIMEOUT_SECONDS = 30.0


def _err(message: str, code: str, *, relogin: bool = False):
    from nastech_cli.auth_constants import AuthError
    return AuthError(f"solstice: {message}", provider="solstice", code=code, relogin_required=relogin)


def _nas_base_url() -> str:
    """The Nastech portal the user is signed into (``NASTECH_PORTAL_BASE_URL`` override first)."""
    from nastech_cli.auth import _nastech_portal_base_url, get_provider_auth_state
    return _nastech_portal_base_url(get_provider_auth_state("nastech") or {})


def _nas_request(method: str, path: str, *, json: Mapping[str, Any] | None = None) -> dict[str, Any]:
    from nastech_cli.auth import _default_verify, resolve_nastech_access_token
    from nastech_cli.auth_constants import httpx

    try:
        token = resolve_nastech_access_token()
    except Exception as exc:
        raise _err("sign in to Nastech Portal first (`nastech auth add nastech`).", "solstice_nastech_login_required",
                   relogin=True) from exc
    try:
        response = httpx.request(method, _nas_base_url() + path, json=json, timeout=_TIMEOUT_SECONDS,
                                 headers={"Accept": "application/json", "Authorization": f"Bearer {token}"},
                                 verify=_default_verify())
    except Exception as exc:
        raise _err(f"Nastech portal request failed: {type(exc).__name__}", "solstice_broker_unreachable") from exc
    if response.status_code == 404:
        raise _err("not available on this Nastech account yet.", "solstice_not_configured")
    if response.status_code >= 400:
        raise _err(f"Nastech portal returned HTTP {response.status_code}.", "solstice_broker_failed")
    return response.json()


def discover_client() -> dict[str, str]:
    """``client_id`` / ``authorize_url`` / ``scope`` NAS serves for the shared Google client."""
    payload = _nas_request("GET", _CONFIG_PATH)
    missing = [k for k in ("client_id", "authorize_url", "scope") if not str(payload.get(k) or "").strip()]
    if missing:
        raise _err(f"Nastech portal config is missing {', '.join(missing)}.", "solstice_config_invalid")
    return {k: str(payload[k]).strip() for k in ("client_id", "authorize_url", "scope")}


def broker_token_request(grant: Mapping[str, str]) -> Mapping[str, Any]:
    """``OAuthPKCEConfig.token_request``: send the grant to NAS, which adds the client secret.

    NAS folds every Google token-endpoint failure into HTTP 502, so a refresh it rejects is treated as
    a dead grant (re-login) rather than retried against a token Google already refused.
    """
    path = _TOKEN_PATHS[grant["grant_type"]]
    body = {k: v for k, v in grant.items() if k in ("code", "code_verifier", "redirect_uri", "refresh_token")}
    try:
        return _nas_request("POST", path, json=body)
    except Exception as exc:
        if grant["grant_type"] == "refresh_token" and getattr(exc, "code", "") == "solstice_broker_failed":
            raise _err("the stored sign-in was rejected; run `nastech auth add solstice` again.",
                       "invalid_grant", relogin=True) from exc
        raise
