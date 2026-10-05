"""Default-root isolation through the real Python resolution chain."""

import json
import os
from pathlib import Path
import subprocess
import sys

import pytest


# Win32 strips a trailing space from every path component, so the literal-suffix contract is
# only checkable with the leading space there.
_SPACED = " spaced" if sys.platform == "win32" else " spaced "


@pytest.mark.platforms("linux", "macos", "windows")
@pytest.mark.parametrize("suffix", ["", "-asdfasdf", "magic-test", _SPACED])
def test_suffix_scopes_default_home_and_profiles(tmp_path, suffix):
    env = dict(os.environ)
    env.pop("NASTECH_HOME", None)
    env.update(
        HOME=str(tmp_path), USERPROFILE=str(tmp_path),
        LOCALAPPDATA=str(tmp_path / "AppData" / "Local"),
        NASTECH_DATA_DIR_SUFFIX=suffix,
    )
    script = """
import json
import os
from pathlib import Path
from nastech_constants import get_nastech_home, get_process_nastech_home, get_default_nastech_root
from nastech_cli.profiles import _get_profiles_root, _get_active_profile_path, resolve_profile_env
root = get_default_nastech_root()
profile = root / 'profiles' / 'coder'
profile.mkdir(parents=True)
(profile / 'config.yaml').write_text('', encoding='utf-8')
result = [str(get_nastech_home()), str(get_process_nastech_home()), str(root),
          str(_get_profiles_root()), str(_get_active_profile_path()), resolve_profile_env('coder')]
os.environ['NASTECH_HOME'] = str(profile)
result.extend([str(get_nastech_home()), str(get_default_nastech_root())])
os.environ.pop('NASTECH_HOME')
os.environ['NASTECH_DATA_DIR_SUFFIX'] += '-changed'
result.append(str(get_default_nastech_root()))
print(json.dumps(result))
"""
    result = subprocess.run(
        [sys.executable, "-c", script], env=env,
        cwd=Path(__file__).resolve().parents[2],
        text=True, capture_output=True,
    )
    assert result.returncode == 0, result.stderr
    base = tmp_path / "AppData" / "Local" / "nastech" if sys.platform == "win32" else tmp_path / ".nastech"
    root = Path(str(base) + suffix)
    profile = root / "profiles" / "coder"
    assert json.loads(result.stdout) == list(map(str, [
        root, root, root, root / "profiles", root / "active_profile", profile,
        profile, root, Path(str(root) + "-changed"),
    ]))


@pytest.mark.platforms("linux", "macos", "windows")
def test_startup_readers_use_the_suffixed_home(tmp_path, monkeypatch):
    from nastech_constants import get_process_nastech_home
    from nastech_cli.dashboard_procs import _nastech_home_dir
    from nastech_cli.env_loader import load_nastech_dotenv
    from nastech_startup_watchdog import get_startup_watchdog_dump_path

    monkeypatch.setattr(Path, "home", lambda: tmp_path)
    monkeypatch.setenv("LOCALAPPDATA", str(tmp_path / "AppData" / "Local"))
    monkeypatch.delenv("NASTECH_HOME", raising=False)
    monkeypatch.setenv("NASTECH_DATA_DIR_SUFFIX", "magic-test")
    monkeypatch.delenv("SUFFIX_TEST_CREDENTIAL", raising=False)
    home = get_process_nastech_home()
    home.mkdir(parents=True)
    (home / ".env").write_text("SUFFIX_TEST_CREDENTIAL=suffixed\n", encoding="utf-8")

    load_nastech_dotenv(project_env=tmp_path / "absent.env", load_external_secrets=False)
    assert os.environ.get("SUFFIX_TEST_CREDENTIAL") == "suffixed"
    assert _nastech_home_dir() == home
    assert get_startup_watchdog_dump_path() == home / "logs" / "gateway-startup-watchdog.log"


def test_suffix_does_not_change_explicit_or_context_home(tmp_path, monkeypatch):
    from nastech_constants import (
        get_default_nastech_root, get_nastech_home, get_process_nastech_home,
        reset_nastech_home_override, set_nastech_home_override,
    )

    monkeypatch.setattr(Path, "home", lambda: tmp_path)
    monkeypatch.setenv("LOCALAPPDATA", str(tmp_path / "AppData" / "Local"))
    explicit = tmp_path / "explicit"
    scoped = tmp_path / "scoped"
    monkeypatch.setenv("NASTECH_HOME", str(explicit))
    monkeypatch.setenv("NASTECH_DATA_DIR_SUFFIX", "magic-test")
    assert get_nastech_home() == get_process_nastech_home() == get_default_nastech_root() == explicit
    token = set_nastech_home_override(scoped)
    try:
        assert get_nastech_home() == scoped
        assert get_process_nastech_home() == get_default_nastech_root() == explicit
    finally:
        reset_nastech_home_override(token)
