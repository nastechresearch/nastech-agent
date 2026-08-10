"""Background keepalive for long-lived Nastech Portal sessions."""

from __future__ import annotations

import logging
import os
import threading
from typing import Optional

from nastech_cli.auth import (
    ACCESS_TOKEN_REFRESH_SKEW_SECONDS,
    NASTECH_INVOKE_JWT_MIN_TTL_SECONDS,
    AuthError,
    _agent_key_is_usable,
    _is_expiring,
    get_provider_auth_state,
    resolve_nastech_runtime_credentials,
)

logger = logging.getLogger(__name__)

NASTECH_AUTH_KEEPALIVE_INTERVAL_SECONDS = 6 * 60 * 60
NASTECH_AUTH_KEEPALIVE_INITIAL_DELAY_SECONDS = 60

_keepalive_lock = threading.Lock()
_keepalive_stop = threading.Event()
_keepalive_thread: Optional[threading.Thread] = None


def _timeout_seconds(value: Optional[float]) -> float:
    if value is not None:
        return float(value)
    try:
        return float(os.getenv("NASTECH_NASTECH_TIMEOUT_SECONDS", "15"))
    except (TypeError, ValueError):
        return 15.0


def _entry_state(entry: object) -> dict:
    return {
        "agent_key": getattr(entry, "agent_key", None),
        "agent_key_expires_at": getattr(entry, "agent_key_expires_at", None),
        "scope": getattr(entry, "scope", None),
    }


def _refresh_selected_pool_entry(
    *,
    min_key_ttl_seconds: int,
) -> Optional[bool]:
    """Refresh the current Nastech credential pool entry when it is stale.

    Returns True when a pool entry exists and is usable/refreshed, False when a
    pool exists but no entry can be used, and None when no Nastech pool exists.
    """
    try:
        from agent.credential_pool import load_pool

        pool = load_pool("nastech")
    except Exception as exc:
        logger.debug("Nastech auth keepalive: credential pool unavailable: %s", exc)
        return None

    if not pool or not pool.has_credentials():
        return None

    try:
        entry = pool.select()
    except Exception as exc:
        logger.debug("Nastech auth keepalive: credential pool selection failed: %s", exc)
        return False

    if entry is None:
        return False

    access_expiring = _is_expiring(
        getattr(entry, "expires_at", None),
        ACCESS_TOKEN_REFRESH_SKEW_SECONDS,
    )
    key_usable = _agent_key_is_usable(_entry_state(entry), min_key_ttl_seconds)
    if access_expiring or not key_usable:
        refreshed = pool.try_refresh_current()
        if refreshed is None:
            return False
        logger.debug("Nastech auth keepalive: refreshed credential pool entry")
        return True

    return True


def refresh_nastech_auth_keepalive_once(
    *,
    min_key_ttl_seconds: int = NASTECH_INVOKE_JWT_MIN_TTL_SECONDS,
    timeout_seconds: Optional[float] = None,
) -> bool:
    """Refresh Nastech auth once if credentials are configured."""
    min_key_ttl_seconds = max(60, int(min_key_ttl_seconds))

    pool_result = _refresh_selected_pool_entry(
        min_key_ttl_seconds=min_key_ttl_seconds,
    )
    if pool_result is not None:
        return pool_result

    state = get_provider_auth_state("nastech")
    if not state:
        return False

    try:
        resolve_nastech_runtime_credentials(
            timeout_seconds=_timeout_seconds(timeout_seconds),
        )
        logger.debug("Nastech auth keepalive: refreshed singleton auth state")
        return True
    except AuthError as exc:
        if exc.relogin_required:
            logger.info("Nastech auth keepalive requires re-login: %s", exc)
        else:
            logger.debug("Nastech auth keepalive failed: %s", exc)
        return False
    except Exception as exc:
        logger.debug("Nastech auth keepalive failed: %s", exc)
        return False


def _keepalive_loop(
    stop_event: threading.Event,
    *,
    interval_seconds: int,
    initial_delay_seconds: int,
    min_key_ttl_seconds: int,
    timeout_seconds: Optional[float],
) -> None:
    if initial_delay_seconds > 0 and stop_event.wait(initial_delay_seconds):
        return

    while not stop_event.is_set():
        refresh_nastech_auth_keepalive_once(
            min_key_ttl_seconds=min_key_ttl_seconds,
            timeout_seconds=timeout_seconds,
        )
        stop_event.wait(interval_seconds)


def start_nastech_auth_keepalive(
    *,
    interval_seconds: int = NASTECH_AUTH_KEEPALIVE_INTERVAL_SECONDS,
    initial_delay_seconds: int = NASTECH_AUTH_KEEPALIVE_INITIAL_DELAY_SECONDS,
    min_key_ttl_seconds: int = NASTECH_INVOKE_JWT_MIN_TTL_SECONDS,
    timeout_seconds: Optional[float] = None,
) -> Optional[threading.Thread]:
    """Start the process-wide Nastech auth keepalive thread."""
    if interval_seconds <= 0:
        return None

    global _keepalive_thread
    with _keepalive_lock:
        if _keepalive_thread is not None and _keepalive_thread.is_alive():
            return _keepalive_thread

        _keepalive_stop.clear()
        _keepalive_thread = threading.Thread(
            target=_keepalive_loop,
            args=(_keepalive_stop,),
            kwargs={
                "interval_seconds": int(interval_seconds),
                "initial_delay_seconds": max(0, int(initial_delay_seconds)),
                "min_key_ttl_seconds": max(60, int(min_key_ttl_seconds)),
                "timeout_seconds": timeout_seconds,
            },
            daemon=True,
            name="nastech-auth-keepalive",
        )
        _keepalive_thread.start()
        logger.debug("Nastech auth keepalive started")
        return _keepalive_thread


def stop_nastech_auth_keepalive(timeout: float = 5.0) -> None:
    """Stop the keepalive thread. Intended for graceful shutdown/tests."""
    global _keepalive_thread
    with _keepalive_lock:
        thread = _keepalive_thread
        _keepalive_stop.set()
    if thread is not None and thread.is_alive():
        thread.join(timeout=timeout)
    with _keepalive_lock:
        if _keepalive_thread is thread:
            _keepalive_thread = None
