"""Why an auxiliary client could not be built — and the Nastech credential failure behind it.

``_resolve_nastech_runtime_api`` must swallow the resolver's ``AuthError`` and return None so the
ladder can still fall back (stored token, fallback_chain). Swallowing it at DEBUG left the goal
loop reporting ``judge error: RuntimeError`` while the real cause was an ``invalid_grant`` refresh
(#42177). This module remembers the latest failure so the ladder's raise and the goal judge can
name it, and warns ONCE per distinct message so operators see it without debug logging.
"""

import contextlib
import logging
import threading
from typing import Optional

logger = logging.getLogger(__name__)


class AuxiliaryClientUnavailable(RuntimeError):
    """No auxiliary client could be built for the task (missing credentials / provider)."""


_lock = threading.Lock()
_last_nastech_detail: Optional[str] = None
_warned_nastech_details: set[str] = set()


def _quarantined_nastech_error(exc: BaseException) -> BaseException:
    """Prefer the persisted terminal quarantine marker over *exc*; sentence-terminate either message.

    The pool rung swallows the real ``invalid_grant`` and wipes the dead tokens, so by the time the
    auth-store resolver runs it can only say "No access token found"; the marker it wrote still
    carries the message and code the user needs (#42177). ``format_auth_error`` appends the
    remediation sentence with a space, so an unterminated message reads "Invalid refresh token Run …".
    """
    from nastech_cli.auth import AuthError, get_provider_auth_state
    from nastech_cli.auth_nastech import _terminal_quarantine_marker

    with contextlib.suppress(Exception):
        marker = _terminal_quarantine_marker(get_provider_auth_state("nastech") or {})
        if marker and marker.get("message"):
            return AuthError(_sentence(marker["message"]), provider="nastech", code=marker.get("code"),
                             relogin_required=True)
    if isinstance(exc, AuthError):
        return AuthError(_sentence(exc), provider=exc.provider, code=exc.code,
                         relogin_required=exc.relogin_required, retry_after=exc.retry_after,
                         retryable=exc.retryable)
    return exc


def _sentence(text: object) -> str:
    return str(text).strip().rstrip(".") + "."


def missing_provider_credentials_message(provider_id: str) -> str:
    """The "Provider 'X' is set in config.yaml but …" error for an explicit provider with no credentials.

    The remedy comes from the registry, never from the provider id: ``f"{id.upper()}_API_KEY"``
    invents names nothing reads (alibaba → ALIBABA_API_KEY instead of DASHSCOPE_API_KEY, and the
    unsettable MINIMAX-OAUTH_API_KEY for OAuth ids, #114405 / #78996). OAuth providers have no key
    env var at all, so they are pointed at the sign-in command instead.
    """
    pconfig = None
    with contextlib.suppress(Exception):
        from nastech_cli.auth import PROVIDER_REGISTRY
        pconfig = PROVIDER_REGISTRY.get(provider_id)
    env_vars = tuple(getattr(pconfig, "api_key_env_vars", None) or ())
    problem, remedy = "no API key was found", ""
    if env_vars:
        remedy = f"Set the {env_vars[0]} environment variable"
    elif pconfig is None:
        remedy = f"Set the {provider_id.upper().replace('-', '_')}_API_KEY environment variable"
    elif str(pconfig.auth_type).startswith("oauth"):
        problem, remedy = "no credentials were found", f"Run `nastech auth add {provider_id}` to sign in"
    else:
        problem = "no credentials were found"
    switch = "switch to a different provider with `nastech model`."
    return (f"Provider '{provider_id}' is set in config.yaml but {problem}. "
            + (f"{remedy}, or {switch}" if remedy else switch.capitalize()))


def _nastech_credential_present(exc: BaseException) -> bool:
    """True when a Nastech credential exists that failed — a coded error (``invalid_grant``, a quarantine
    marker, ``refresh_failed``) or persisted Nastech auth state. The uncoded "not logged into Nastech Portal"
    with no stored state is the normal condition for users who never chose Nastech; the auto-route walk
    hits it on every discovery pass and must not warn (the ladder already logs its own summary).
    """
    if getattr(exc, "code", None):
        return True
    from nastech_cli.auth import get_provider_auth_state

    with contextlib.suppress(Exception):
        return bool(get_provider_auth_state("nastech"))
    return False


def record_nastech_credential_failure(exc: BaseException) -> str:
    """Remember *exc* as the latest Nastech credential failure.

    Logged once per distinct message: WARNING when a real credential failed, DEBUG when Nastech was
    simply never logged into Nastech.
    """
    from nastech_cli.auth import format_auth_error

    exc = _quarantined_nastech_error(exc)
    message = format_auth_error(exc) if isinstance(exc, Exception) else str(exc)
    message = message.strip() or type(exc).__name__
    code = getattr(exc, "code", None)
    if code and str(code) not in message:
        message = f"{message} (code: {code})"
    detail = f"Nastech Portal runtime credentials unavailable: {message}"
    global _last_nastech_detail
    with _lock:
        _last_nastech_detail = detail
        first_time = detail not in _warned_nastech_details
        _warned_nastech_details.add(detail)
    if first_time:
        level = logging.WARNING if _nastech_credential_present(exc) else logging.DEBUG
        logger.log(level, "Auxiliary Nastech client unavailable: %s", detail)
    return detail


def clear_nastech_credential_failure() -> None:
    global _last_nastech_detail
    with _lock:
        _last_nastech_detail = None


def nastech_credential_failure_detail() -> Optional[str]:
    """The latest recorded Nastech credential failure, or None when the last resolution succeeded."""
    with _lock:
        return _last_nastech_detail
