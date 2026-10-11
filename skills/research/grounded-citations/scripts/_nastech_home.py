"""Resolve NASTECH_HOME for standalone skill scripts.

Skill scripts may run outside the Nastech process (system Python, nix env,
CI) where ``nastech_constants`` is not importable.  This module provides the
same ``get_nastech_home()`` contract without requiring it on ``sys.path``.

When ``nastech_constants`` IS available it is used directly so profile
resolution and any future enhancements are picked up automatically.
"""

from __future__ import annotations

import os
from pathlib import Path

try:
    from nastech_constants import get_nastech_home
except (ModuleNotFoundError, ImportError):

    def get_nastech_home() -> Path:
        """Return the Nastech home directory (default: ``~/.nastech``)."""
        val = os.environ.get("NASTECH_HOME", "").strip()
        return Path(val) if val else Path.home() / ".nastech"
