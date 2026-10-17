"""Honcho host-block migration for ``nastech profile rename``.

Split out of ``nastech_cli.profiles``; the profiles root is late-imported from there so its
``_get_default_nastech_home`` seam holds.
"""

import json
from pathlib import Path


def _atomic_write_json(path: Path, data: dict) -> bool:
    """Atomic rewrite of a third-party JSON config; False on OSError (nothing partially written)."""
    from utils import atomic_json_write
    try:
        atomic_json_write(path, data)
        return True
    except OSError:
        return False


def migrate_honcho_profile_host(old_name: str, new_name: str, new_dir: Path) -> None:
    """Rename Honcho host blocks for a renamed profile without changing peers."""
    from nastech_cli.profiles import _get_default_nastech_home

    old_host = f"nastech_{old_name}"
    legacy_old_host = f"nastech.{old_name}"
    new_host = f"nastech_{new_name}"
    candidates = [
        new_dir / "honcho.json", _get_default_nastech_home() / "honcho.json", Path.home() / ".honcho" / "config.json"
    ]
    seen: set[Path] = set()
    for path in candidates:
        try:
            resolved = path.resolve()
        except OSError:
            resolved = path
        if resolved in seen or not path.is_file():
            continue
        seen.add(resolved)
        try:
            raw = json.loads(path.read_text(encoding="utf-8-sig"))
        except (OSError, json.JSONDecodeError):
            continue
        hosts = raw.get("hosts")
        if not isinstance(hosts, dict):
            continue
        source_host = old_host if old_host in hosts else legacy_old_host
        if source_host not in hosts:
            continue
        if new_host in hosts:
            print(f"⚠ Honcho host block not migrated: {new_host} already exists in {path}")
            continue
        block = hosts[source_host]
        if isinstance(block, dict) and "aiPeer" not in block:
            block["aiPeer"] = old_name  # source_host is ``nastech_<old>`` or legacy ``nastech.<old>``
        hosts[new_host] = hosts.pop(source_host)
        if _atomic_write_json(path, raw):
            print(f"✓ Honcho host updated: {source_host} → {new_host}")
