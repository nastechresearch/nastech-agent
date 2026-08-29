"""Resolve NASTECH_HOME for standalone skill scripts.

Skill scripts may run outside the Nastech process (e.g. system Python,
nix env, CI) where ``nastech_constants`` is not importable.  This module
provides the same ``get_nastech_home()`` and ``display_nastech_home()``
contracts as ``nastech_constants`` without requiring it on ``sys.path``.

When ``nastech_constants`` IS available it is used directly so that any
future enhancements (profile resolution, Docker detection, etc.) are
picked up automatically.  The fallback path replicates the core logic
from ``nastech_constants.py`` using only the stdlib.

All scripts under ``google-workspace/scripts/`` should import from here
instead of duplicating the ``NASTECH_HOME = Path(os.getenv(...))`` pattern.
"""

from __future__ import annotations

import os
from pathlib import Path

try:
    from nastech_constants import display_nastech_home as display_nastech_home
    from nastech_constants import get_nastech_home as get_nastech_home
except (ModuleNotFoundError, ImportError):

    def get_nastech_home() -> Path:
        """Return the Nastech home directory (default: ~/.nastech).

        Mirrors ``nastech_constants.get_nastech_home()``."""
        val = os.environ.get("NASTECH_HOME", "").strip()
        return Path(val) if val else Path.home() / ".nastech"

    def display_nastech_home() -> str:
        """Return a user-friendly ``~/``-shortened display string.

        Mirrors ``nastech_constants.display_nastech_home()``."""
        home = get_nastech_home()
        try:
            return "~/" + home.relative_to(Path.home()).as_posix()
        except ValueError:
            return str(home)
