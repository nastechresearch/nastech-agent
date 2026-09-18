#!/usr/bin/env python3
"""Boot-time re-seed of a terminally-dead Nastech bootstrap session.

Background
----------
A Nastech bootstrap session (client_id ``nastech-cli-vps``) can take a terminal
``invalid_grant`` and be quarantined locally — the refresh path clears the dead
tokens from ``auth.json`` and stamps
``providers.nastech.last_auth_error.relogin_required = true``. From then on every
inference turn hard-fails with a provider-auth error until the credential is
replaced, even though the gateway and dashboard otherwise look healthy.

``stage2-hook.sh`` seeds ``auth.json`` from ``NASTECH_AUTH_JSON_BOOTSTRAP`` only
on a *blank* volume (``[ ! -f auth.json ]``) — that guard is load-bearing: it
stops a container restart from clobbering a healthy, rotated refresh token. So a
plain restart with a fresh seed env can NOT recover a container whose volume
already has an auth.json.

This script is the narrow, safe exception. An orchestrator that manages the
container can supply a freshly-issued bootstrap session via
``NASTECH_AUTH_JSON_REBOOTSTRAP`` (plus a restart). On boot we re-seed the Nastech
provider entry from that env when the on-disk entry is provably terminal, or
when the orchestrator seed's ``obtained_at`` is newer than the local session.
The latter matters because an orchestrator may revoke the previous session
before restart while its still-present local tokens look healthy. Older or
incomparable seeds remain no-ops, so a retained env cannot roll auth backward.

Design constraints
------------------
- Pure stdlib, no nastech_cli imports: runs early in the boot hook, before the
  app venv/modules are guaranteed importable, as its own subprocess.
- Surgical: replaces ONLY ``providers.nastech`` in the existing auth.json, leaving
  every other provider, the version, and any other top-level state untouched.
- Fail-safe: any parse/IO error leaves auth.json exactly as-is and exits 0 (a
  failed re-seed must never take the container further down than it already is).
"""
from __future__ import annotations

import json
import os
import sys
import tempfile
from datetime import datetime, timezone
from typing import Any, Optional

# Env var the orchestrator sets to the re-seed payload. Deliberately DISTINCT
# from NASTECH_AUTH_JSON_BOOTSTRAP (create-only, blank-volume seed) so the two
# paths can never be confused: BOOTSTRAP seeds a fresh volume; REBOOTSTRAP
# overwrites a terminally-dead Nastech entry on an existing volume.
REBOOTSTRAP_ENV = "NASTECH_AUTH_JSON_REBOOTSTRAP"
BOOTSTRAP_CLIENT_ID = "nastech-cli-vps"


def _nastech_entry_is_terminal(nastech_state: Any) -> bool:
    """True iff the on-disk Nastech provider entry is in the terminal/quarantined
    state AND holds no usable credential.

    Mirrors the ``terminal`` predicate in ``nastech_cli.auth.get_nastech_session_validity``:
    a persisted ``last_auth_error.relogin_required`` with the token material
    already cleared. Keeping this in lockstep is what guarantees we only re-seed
    a session that is genuinely dead.
    """
    if not isinstance(nastech_state, dict):
        return False
    last_err = nastech_state.get("last_auth_error")
    if not (isinstance(last_err, dict) and last_err.get("relogin_required")):
        return False
    # Only terminal while there is no usable credential left. If a live token is
    # somehow present, treat it as healthy and do NOT clobber it.
    if nastech_state.get("access_token") or nastech_state.get("refresh_token"):
        return False
    return True


def _extract_nastech_from_seed(seed_raw: str) -> Optional[dict]:
    """Pull the ``providers.nastech`` block out of a NASTECH_AUTH_JSON_REBOOTSTRAP
    payload. The payload is a full auth.json document (same shape as
    NASTECH_AUTH_JSON_BOOTSTRAP). Returns None unless it carries the expected VPS
    bootstrap client plus non-empty access and refresh tokens — caller treats
    None as "nothing to do"."""
    try:
        seed = json.loads(seed_raw)
    except (ValueError, TypeError):
        return None
    if not isinstance(seed, dict):
        return None
    providers = seed.get("providers")
    if not isinstance(providers, dict):
        return None
    nastech = providers.get("nastech")
    if not isinstance(nastech, dict) or not nastech:
        return None
    if nastech.get("client_id") != BOOTSTRAP_CLIENT_ID:
        return None
    if not (
        isinstance(nastech.get("access_token"), str)
        and nastech["access_token"].strip()
        and isinstance(nastech.get("refresh_token"), str)
        and nastech["refresh_token"].strip()
    ):
        return None
    return nastech


def _parse_timestamp(value: Any) -> Optional[datetime]:
    """Parse an OAuth timestamp without guessing when either side is malformed."""
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (ValueError, OverflowError):
        return None
    if parsed.tzinfo is None:
        return None
    try:
        return parsed.astimezone(timezone.utc)
    except (OverflowError, ValueError):
        return None


def _seed_is_newer(local_nastech: Any, seed_nastech: dict) -> bool:
    """Whether NAS supplied a bootstrap session newer than the local one.

    NAS mints the replacement before restarting the machine and revokes the
    previous session.  A healthy-looking local entry can therefore already be
    stale.  ``obtained_at`` is the server-issued ordering signal that lets boot
    apply a genuinely newer replacement without allowing an old retained env
    value to roll credentials back on later restarts.
    """
    if not isinstance(local_nastech, dict):
        return False
    local_obtained = _parse_timestamp(local_nastech.get("obtained_at"))
    seed_obtained = _parse_timestamp(seed_nastech.get("obtained_at"))
    return bool(
        local_obtained is not None
        and seed_obtained is not None
        and seed_obtained > local_obtained
    )


def reseed_if_terminal(auth_path: str, seed_raw: str) -> str:
    """Core logic. Returns a short status string for logging/testing:

      - "no_seed"          — seed env empty/absent
      - "bad_seed"         — seed present but unparseable / no nastech entry
      - "no_auth_file"     — auth.json absent (blank volume → let the normal
                             NASTECH_AUTH_JSON_BOOTSTRAP path handle it)
      - "auth_unreadable"  — auth.json present but unparseable (leave as-is)
      - "not_terminal"     — local entry is healthy and at least as new → no-op
      - "reseeded"         — terminal entry replaced from seed
      - "reseeded_newer"   — healthy-but-stale entry replaced by a newer seed
    """
    if not seed_raw:
        return "no_seed"

    seed_nastech = _extract_nastech_from_seed(seed_raw)
    if seed_nastech is None:
        return "bad_seed"

    if not os.path.exists(auth_path):
        # Blank volume — this is the normal first-boot case, not a re-seed.
        return "no_auth_file"

    try:
        with open(auth_path, "r", encoding="utf-8") as fh:
            store = json.load(fh)
    except (OSError, ValueError):
        # Corrupt/unreadable auth.json: do NOT overwrite blindly. A separate
        # concern; leave it for the operator / other recovery paths.
        return "auth_unreadable"

    if not isinstance(store, dict):
        return "auth_unreadable"

    providers = store.get("providers")
    if not isinstance(providers, dict):
        providers = {}
        store["providers"] = providers

    local_nastech = providers.get("nastech")
    terminal = _nastech_entry_is_terminal(local_nastech)
    newer_seed = _seed_is_newer(local_nastech, seed_nastech)
    if not terminal and not newer_seed:
        # Healthy and at least as new as the seed, or incomparable. Never roll a
        # session back merely because an old rebootstrap env remains configured.
        return "not_terminal"

    # Surgical replacement: swap ONLY providers.nastech, preserve everything else.
    providers["nastech"] = seed_nastech

    # 0600 from creation: the seed holds a refresh token and must never sit at umask, even briefly.
    # (stdlib only by design — see module docstring — so this mirrors utils.atomic_json_write by hand.)
    # Randomly named: boot-hook PIDs inside a container repeat, so a PID-named temp left by a
    # SIGKILL'd run would collide with O_EXCL forever and main() would swallow the FileExistsError.
    fd, tmp_path = tempfile.mkstemp(
        dir=os.path.dirname(auth_path) or ".", prefix=os.path.basename(auth_path) + ".rebootstrap.", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(store, fh)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp_path, auth_path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    return "reseeded" if terminal else "reseeded_newer"


def main() -> int:
    auth_path = sys.argv[1] if len(sys.argv) > 1 else ""
    if not auth_path:
        home = os.environ.get("NASTECH_HOME", "")
        auth_path = os.path.join(home, "auth.json") if home else "auth.json"
    seed_raw = os.environ.get(REBOOTSTRAP_ENV, "")

    try:
        result = reseed_if_terminal(auth_path, seed_raw)
    except Exception as exc:  # never let a re-seed error fail the boot
        print(f"[rebootstrap] error (ignored): {exc!r}", file=sys.stderr)
        return 0

    if result == "reseeded":
        print("[rebootstrap] Nastech bootstrap session was terminal; re-seeded auth.json from "
              f"{REBOOTSTRAP_ENV}")
    elif result == "reseeded_newer":
        print("[rebootstrap] Applied newer orchestrator-issued Nastech bootstrap session from "
              f"{REBOOTSTRAP_ENV}")
    else:
        # Quiet by default for the common no-op cases; still emit a breadcrumb.
        print(f"[rebootstrap] no-op ({result})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
