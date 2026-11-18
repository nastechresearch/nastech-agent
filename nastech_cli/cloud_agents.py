"""Nastech Cloud agents for the account this install is signed in to Nastech Portal with.

Native Desktop lists them through its own portal browser session (``electron/main.ts``
``discoverCloudAgents``). A browser tab on the Webapp has no such session, so the gateway serving
it asks the portal with this install's Nastech sign-in instead (``GET /api/cloud/agents``, the agent
picker of Settings ▸ Backup & Transfer): the same ``GET /api/agents`` call,
the same trimmed shape (``id``, ``name``, ``status``, ``dashboardUrl``, ``dashboardGatewayState``),
and the same 409 team picker.
"""

from __future__ import annotations

from typing import Any, Optional

import httpx

_TIMEOUT_S = 15.0


# "Not signed in to Nastech Portal" is a state of this install, not of the caller's dashboard session:
# 409, never 401. Every dashboard client reads a 401 (and the Webapp's AuthWidget a 403) as its own
# session being refused, so a 401 here would send a no-auth Webapp user to the Webapp sign-in page
# instead of telling them to sign in to Nastech Portal.
PORTAL_SIGNIN_STATUS = 409


class CloudAgentsError(RuntimeError):
    def __init__(self, message: str, status: int, code: str):
        super().__init__(message)
        self.status = status
        self.code = code


def _org(raw: Any) -> Optional[dict[str, Any]]:
    if not isinstance(raw, dict) or not isinstance(raw.get("id"), str):
        return None
    return {"id": raw["id"], "slug": raw.get("slug") if isinstance(raw.get("slug"), str) else None,
            "name": raw.get("name") if isinstance(raw.get("name"), str) else raw["id"],
            "isPersonal": bool(raw.get("isPersonal")), "role": raw.get("role") or "MEMBER"}


def _agent(raw: dict[str, Any]) -> dict[str, Any]:
    text = lambda key, fallback: raw[key] if isinstance(raw.get(key), str) else fallback
    return {"id": raw["id"], "name": text("name", raw["id"]), "status": text("status", "unknown"),
            "dashboardUrl": text("dashboardUrl", None),
            "dashboardGatewayState": text("dashboardGatewayState", "unknown")}


def discover(org: Optional[str] = None) -> dict[str, Any]:
    """``{agents, org}``, or ``{needsOrgSelection: True, orgs}`` for a multi-team account."""
    from nastech_cli.auth import AuthError, get_provider_auth_state, resolve_nastech_access_token
    from nastech_cli.auth_nastech import _nastech_portal_base_url

    try:
        token = resolve_nastech_access_token()
    except AuthError as exc:
        raise CloudAgentsError(f"Sign in to Nastech Portal first ({exc}).",
                                PORTAL_SIGNIN_STATUS, "portal_signin_required") from None
    portal = _nastech_portal_base_url(get_provider_auth_state("nastech") or {})
    try:
        with httpx.Client(timeout=_TIMEOUT_S) as client:
            response = client.get(f"{portal}/api/agents", params={"org": org} if org else None,
                                  headers={"Authorization": f"Bearer {token}"})
    except httpx.HTTPError as exc:
        raise CloudAgentsError(f"Could not reach Nastech Portal: {exc}", 502, "portal_unreachable") from None
    try:
        body = response.json()
    except ValueError:
        body = {}
    if response.status_code == 409 and isinstance(body, dict) and body.get("error") == "org_selection_required":
        return {"needsOrgSelection": True, "orgs": [o for o in map(_org, body.get("orgs") or []) if o]}
    if response.status_code == 401:
        raise CloudAgentsError("Your Nastech Portal sign-in has expired. Sign in again.",
                                PORTAL_SIGNIN_STATUS, "portal_signin_required")
    if response.status_code >= 400 or not isinstance(body, dict):
        raise CloudAgentsError(f"Nastech Portal answered {response.status_code}.", 502, "portal_error")
    agents = [a for a in body.get("agents") or [] if isinstance(a, dict) and isinstance(a.get("id"), str)]
    return {"agents": [_agent(a) for a in agents], "org": _org(body.get("org"))}
