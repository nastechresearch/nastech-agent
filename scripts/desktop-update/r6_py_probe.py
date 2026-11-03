"""PROBE BRANCH ONLY (wine2e/r6-lock-probe): what does the product's own probe answer?

Prints ``update_lock.checkout_lock_held(root)`` plus the path it resolved, so one Windows run
can compare the Python probe with the marker.ps1 probe over the same live holder.
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from nastech_cli import update_lock  # noqa: E402

root = Path(sys.argv[1])
print(f"held={update_lock.checkout_lock_held(root)} path={update_lock.checkout_lock_path(root)}", flush=True)
