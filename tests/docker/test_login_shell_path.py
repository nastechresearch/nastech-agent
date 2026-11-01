"""Login shells in the image keep Nastech' own dirs on PATH.

Debian's ``/etc/profile`` resets PATH for every login shell, so without
``/etc/profile.d/nastech.sh`` a ``bash -l`` (``docker exec <c> bash -l``, ssh, the
terminal tool's background ``bash -lic``) lost ``/opt/nastech/bin`` and bare
``nastech`` exited 127 (#56634).
"""
from __future__ import annotations

import subprocess


def test_login_shell_resolves_nastech_to_the_image_shim(built_image: str) -> None:
    r = subprocess.run(
        ["docker", "run", "--rm", "-u", "nastech", "--entrypoint", "bash", built_image,
         "-lc", 'echo "nastech=$(command -v nastech)"; echo "path=$PATH"'],
        capture_output=True, text=True, timeout=60, check=False,
    )
    assert r.returncode == 0, r.stderr
    lines = dict(line.split("=", 1) for line in r.stdout.splitlines() if "=" in line)
    assert lines["nastech"] == "/opt/nastech/bin/nastech"
    entries = lines["path"].split(":")
    assert entries.index("/opt/nastech/bin") < entries.index("/opt/nastech/.venv/bin")
    assert entries.count("/opt/nastech/bin") == 1
