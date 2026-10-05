"""Generic managed-tool gateway helpers for Nastech-hosted vendor passthroughs."""

from __future__ import annotations

import json
import logging
import os
from datetime import datetime, timezone
from dataclasses import dataclass
from typing import Callable, Optional

from nastech_constants import get_nastech_home
from tools.tool_backend_helpers import managed_nastech_tools_enabled

logger = logging.getLogger(__name__)

_DEFAULT_TOOL_GATEWAY_DOMAIN = "nastechresearch.github.io"
_DEFAULT_TOOL_GATEWAY_SCHEME = "https"
_NASTECH_ACCESS_TOKEN_REFRESH_SKEW_SECONDS = 120


@dataclass(frozen=True)
class ManagedToolGatewayConfig:
    vendor: str
    gateway_origin: str
    nastech_user_token: str
    managed_mode: bool


def _clean(value: object) -> Optional[str]:
    """*value* stripped when it is a non-blank string, else None."""
    return value.strip() if isinstance(value, str) and value.strip() else None


def auth_json_path():
    """Return the Nastech auth store path, respecting NASTECH_HOME overrides."""
    return get_nastech_home() / "auth.json"


def _read_nastech_provider_state() -> Optional[dict]:
    """The profile's Nastech state, or None. A free-tier identity counts only while the free tier is on:
    with ``nastech.guest: false`` it is invisible here, so no cached or refreshed token of it is ever
    attached to a request.

    Resolves through the same profile-then-global-root fallback every other credential reader
    uses: a profile created with ``share_auth`` has no ``auth.json`` of its own and signs in with
    the root identity. Reading only ``NASTECH_HOME/auth.json`` made that profile look signed out to
    the connector gate alone, so ``manage_connections`` vanished from its tool list."""
    try:
        from nastech_cli.auth import get_provider_auth_state

        nastech_provider = get_provider_auth_state("nastech")
        if not isinstance(nastech_provider, dict):
            return None
        from nastech_cli.anon_auth import guest_enabled, is_guest_state

        if is_guest_state(nastech_provider) and not guest_enabled():
            return None
        return nastech_provider
    except Exception:
        return None


def _parse_timestamp(value: object) -> Optional[datetime]:
    normalized = _clean(value)
    if normalized is None:
        return None
    try:
        parsed = datetime.fromisoformat(normalized[:-1] + "+00:00" if normalized.endswith("Z") else normalized)
    except ValueError:
        return None
    return (parsed if parsed.tzinfo is not None else parsed.replace(tzinfo=timezone.utc)).astimezone(timezone.utc)


def _access_token_is_expiring(expires_at: object, skew_seconds: int) -> bool:
    expires = _parse_timestamp(expires_at)
    return expires is None or (expires - datetime.now(timezone.utc)).total_seconds() <= max(0, int(skew_seconds))


def _read_user_token_override() -> Optional[str]:
    """Read the TOOL_GATEWAY_USER_TOKEN override through the secret scope. Scope verdict is authoritative
    when installed (a scoped miss must NOT borrow the process env under multiplex); ``os.environ`` only
    when unscoped. Any non-UnscopedSecretError failure propagates -- a failed scoped read must never
    silently borrow the ambient env."""
    from agent.secret_scope import UnscopedSecretError, get_secret

    try:
        explicit = get_secret("TOOL_GATEWAY_USER_TOKEN")
    except UnscopedSecretError:
        explicit = os.getenv("TOOL_GATEWAY_USER_TOKEN")
    return _clean(explicit)


def peek_nastech_access_token() -> Optional[str]:
    """Cheap token probe: env override or cached auth-store token, no expiry check and no network —
    availability scans must stay off the synchronous OAuth refresh path (:func:`read_nastech_access_token`)."""
    return _read_user_token_override() or _clean((_read_nastech_provider_state() or {}).get("access_token"))


def read_nastech_access_token() -> Optional[str]:
    """Read a Nastech Subscriber OAuth access token from auth store or env override.

    A read: with no Nastech identity there is no bearer and the answer is None. The free-tier identity
    is created by the boot bootstrap (``nastech_cli.free_tier_bootstrap``), never on a token-read
    path (NS-845 Q1.2). A retired free-tier credential IS replaced here, once: that is the explicit
    dead-credential rule, shared with inference.
    """
    if explicit := _read_user_token_override():
        return explicit
    nastech_provider = _read_nastech_provider_state() or {}
    if not nastech_provider:
        return None
    cached_token = peek_nastech_access_token()
    if cached_token and not _access_token_is_expiring(nastech_provider.get("expires_at"), _NASTECH_ACCESS_TOKEN_REFRESH_SKEW_SECONDS):
        return cached_token
    try:
        from nastech_cli.auth import resolve_nastech_access_token

        if refreshed_token := _clean(resolve_nastech_access_token(refresh_skew_seconds=_NASTECH_ACCESS_TOKEN_REFRESH_SKEW_SECONDS)):
            return refreshed_token
    except Exception as exc:
        # Same dead-credential rule as inference (one place decides it: anon_auth): a retired free-tier
        # identity is replaced once, here, instead of handing back its stale token forever.
        from nastech_cli.anon_auth import AnonCredentialDead

        if isinstance(exc, AnonCredentialDead):
            return _replace_dead_guest_token(nastech_provider, str(exc.code or "anon_credential_dead"))
        logger.debug("Nastech access token refresh failed: %s", exc)
    return cached_token


def _replace_dead_guest_token(dead_state: dict, code: str = "anon_credential_dead") -> Optional[str]:
    from nastech_cli.anon_auth import ANON_ACCOUNT_LOCKED, clear_dead_guest, ensure_portal_identity
    from nastech_cli.auth import resolve_nastech_access_token

    clear_dead_guest(code, dead_token=dead_state.get("anon_token"))
    # Same rule as inference: a locked account is retired but never silently replaced.
    if code == ANON_ACCOUNT_LOCKED:
        return None
    try:
        if ensure_portal_identity(explicit=True) is None:
            return None
        return _clean(resolve_nastech_access_token(refresh_skew_seconds=_NASTECH_ACCESS_TOKEN_REFRESH_SKEW_SECONDS))
    except Exception as exc:
        logger.debug("Nastech free tier replacement after a retired credential failed: %s", exc)
        return None


def get_tool_gateway_scheme() -> str:
    """Return configured shared gateway URL scheme."""
    scheme = os.getenv("TOOL_GATEWAY_SCHEME", "").strip().lower() or _DEFAULT_TOOL_GATEWAY_SCHEME
    if scheme not in {"http", "https"}:
        raise ValueError("TOOL_GATEWAY_SCHEME must be 'http' or 'https'")
    return scheme


def build_vendor_gateway_url(vendor: str) -> str:
    """Return the gateway origin for a specific vendor."""
    if explicit_vendor_url := os.getenv(f"{vendor.upper().replace('-', '_')}_GATEWAY_URL", "").strip().rstrip("/"):
        return explicit_vendor_url
    shared_domain = os.getenv("TOOL_GATEWAY_DOMAIN", "").strip().strip("/") or _DEFAULT_TOOL_GATEWAY_DOMAIN
    return f"{get_tool_gateway_scheme()}://{vendor}-gateway.{shared_domain}"


def _vendor_gateway(vendor: str, gateway_builder, token_reader) -> Optional[ManagedToolGatewayConfig]:
    gateway_origin = (gateway_builder or build_vendor_gateway_url)(vendor)
    nastech_user_token = (token_reader or read_nastech_access_token)()
    if not gateway_origin or not nastech_user_token:
        return None
    return ManagedToolGatewayConfig(vendor=vendor, gateway_origin=gateway_origin, nastech_user_token=nastech_user_token, managed_mode=True)


def resolve_managed_tool_gateway(
    vendor: str, gateway_builder: Optional[Callable[[str], str]] = None,
    token_reader: Optional[Callable[[], Optional[str]]] = None) -> Optional[ManagedToolGatewayConfig]:
    """Resolve shared managed-tool gateway config for a vendor (entitled accounts only)."""
    if not managed_nastech_tools_enabled():
        return None
    return _vendor_gateway(vendor, gateway_builder, token_reader)


def resolve_free_search_gateway(token_reader: Optional[Callable[[], Optional[str]]] = None) -> Optional[ManagedToolGatewayConfig]:
    """Perplexity ``search_type: "fast"`` is served to every Nastech identity with no funding check, the
    anonymous guest tier included, so it needs a token this profile may use (guest-disabled and refresh
    rules live in the reader), not paid entitlement or a registered account. Search only: every other
    vendor route goes through :func:`resolve_managed_tool_gateway`."""
    return _vendor_gateway("perplexity", None, token_reader)


def is_managed_tool_gateway_ready(
    vendor: str, gateway_builder: Optional[Callable[[str], str]] = None,
    token_reader: Optional[Callable[[], Optional[str]]] = None) -> bool:
    """True when a gateway URL and a likely-usable Nastech token are present. Defaults to
    :func:`peek_nastech_access_token` (no OAuth refresh); callers about to make a real request use
    :func:`resolve_managed_tool_gateway` instead."""
    return resolve_managed_tool_gateway(vendor, gateway_builder=gateway_builder, token_reader=token_reader or peek_nastech_access_token) is not None
