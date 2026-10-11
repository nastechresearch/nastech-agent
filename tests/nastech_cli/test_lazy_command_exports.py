"""The frozen updater surface on nastech_cli.main stays lazy and resolvable.

``nastech_cli/update_cmd*.py`` (frozen: old installed versions call into it) reads
helpers off ``nastech_cli.main`` via ``_m().<name>``. main.py resolves the ones that
live in the lazily-imported command modules through PEP 562 ``__getattr__`` so
every ``nastech`` invocation (including ``nastech --version``) does not pay for
update_cmd's dependency chain (jwt, click, ...) when no subcommand runs.
"""

import subprocess
import sys
import textwrap

import pytest

import nastech_cli.main

def test_importing_main_does_not_import_command_modules():
    code = textwrap.dedent(
        """
        import sys
        import nastech_cli.main  # noqa: F401
        loaded = [
            m
            for m in (
                "nastech_cli.update_cmd",
                "nastech_cli.sessions_cmd",
                "nastech_cli.dashboard_procs",
            )
            if m in sys.modules
        ]
        assert not loaded, f"eagerly imported: {loaded}"
        """
    )
    result = subprocess.run(
        [sys.executable, "-c", code],
        capture_output=True,
        text=True,
        timeout=120,
        check=False,
    )
    assert result.returncode == 0, result.stderr

@pytest.mark.real_concurrent_gate  # conftest autouse stub would shadow one frozen name
def test_frozen_updater_surface_resolves_to_real_objects():
    for module, names in nastech_cli.main._FROZEN_UPDATER_SURFACE.items():
        mod = sys.modules[module] if module in sys.modules else __import__(module, fromlist=["_"])
        for name in names:
            got = getattr(nastech_cli.main, name)
            # Identity, or the same function after another test importlib.reload()ed the module
            # (the resolved value is cached on nastech_cli.main by design).
            assert got is getattr(mod, name) or (
                getattr(got, "__module__", None) == module and getattr(got, "__name__", None) == name
            ), name
