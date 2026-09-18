"""Tests for subprocess HOME handling in profile mode.

Nastech state stays profile-scoped through NASTECH_HOME. Host subprocesses should
keep the user's real HOME by default so external CLIs find existing credentials.
Containers still use the profile home for persistence, and users can explicitly
opt into profile HOME isolation on the host.

See: https://github.com/NastechResearch/nastech-agent/issues/25114
See: https://github.com/NastechResearch/nastech-agent/issues/36144
See: https://github.com/NastechResearch/nastech-agent/issues/29015
"""

import os
import threading
from pathlib import Path

import nastech_constants



# ---------------------------------------------------------------------------
# get_subprocess_home()
# ---------------------------------------------------------------------------

class TestGetSubprocessHome:
    """Unit tests for nastech_constants.get_subprocess_home()."""

    def _host_mode(self, monkeypatch):
        monkeypatch.setattr(nastech_constants, "is_container", lambda: False)
        monkeypatch.delenv("TERMINAL_HOME_MODE", raising=False)
        monkeypatch.delenv("NASTECH_REAL_HOME", raising=False)

    def _container_mode(self, monkeypatch):
        monkeypatch.setattr(nastech_constants, "is_container", lambda: True)
        monkeypatch.delenv("TERMINAL_HOME_MODE", raising=False)
        monkeypatch.delenv("NASTECH_REAL_HOME", raising=False)



    def test_host_auto_keeps_real_home_when_profile_home_exists(self, tmp_path, monkeypatch):
        """Host installs should not hide real ~/.ssh, ~/.gitconfig, ~/.azure, etc."""
        self._host_mode(monkeypatch)
        real_home = tmp_path / "real-home"
        nastech_home = real_home / ".nastech" / "profiles" / "coder"
        profile_home = nastech_home / "home"
        profile_home.mkdir(parents=True)
        monkeypatch.setenv("HOME", str(real_home))
        monkeypatch.setenv("NASTECH_HOME", str(nastech_home))
        from nastech_constants import get_subprocess_home
        assert get_subprocess_home() is None

    def test_container_auto_uses_profile_home_when_home_dir_exists(self, tmp_path, monkeypatch):
        self._container_mode(monkeypatch)
        nastech_home = tmp_path / ".nastech"
        profile_home = nastech_home / "home"
        profile_home.mkdir(parents=True)
        monkeypatch.setenv("NASTECH_HOME", str(nastech_home))
        from nastech_constants import get_subprocess_home
        assert get_subprocess_home() == str(profile_home)

    def test_returns_profile_specific_path(self, tmp_path, monkeypatch):
        """Explicit profile mode keeps the old per-profile HOME behavior."""
        self._host_mode(monkeypatch)
        profile_dir = tmp_path / ".nastech" / "profiles" / "coder"
        profile_dir.mkdir(parents=True)
        profile_home = profile_dir / "home"
        profile_home.mkdir()
        monkeypatch.setenv("TERMINAL_HOME_MODE", "profile")
        monkeypatch.setenv("NASTECH_HOME", str(profile_dir))
        from nastech_constants import get_subprocess_home
        assert get_subprocess_home() == str(profile_home)

    def test_real_mode_repairs_parent_home_already_pointing_at_profile(self, tmp_path, monkeypatch):
        self._host_mode(monkeypatch)
        profile_dir = tmp_path / ".nastech" / "profiles" / "coder"
        profile_home = profile_dir / "home"
        profile_home.mkdir(parents=True)
        real_home = tmp_path / "real-home"
        real_home.mkdir()
        monkeypatch.setenv("TERMINAL_HOME_MODE", "real")
        monkeypatch.setenv("NASTECH_HOME", str(profile_dir))
        monkeypatch.setenv("HOME", str(profile_home))
        monkeypatch.setenv("NASTECH_REAL_HOME", str(real_home))

        from nastech_constants import get_subprocess_home, get_real_home

        assert get_real_home() == str(real_home)
        assert get_subprocess_home() == str(real_home)


    def test_two_profiles_get_different_homes(self, tmp_path, monkeypatch):
        self._container_mode(monkeypatch)
        base = tmp_path / ".nastech" / "profiles"
        for name in ("alpha", "beta"):
            p = base / name
            p.mkdir(parents=True)
            (p / "home").mkdir()

        from nastech_constants import get_subprocess_home

        monkeypatch.setenv("NASTECH_HOME", str(base / "alpha"))
        home_a = get_subprocess_home()

        monkeypatch.setenv("NASTECH_HOME", str(base / "beta"))
        home_b = get_subprocess_home()

        assert home_a is not None
        assert home_b is not None
        assert home_a != home_b
        assert home_a.endswith("alpha/home")
        assert home_b.endswith("beta/home")



# ---------------------------------------------------------------------------
# _make_run_env() injection
# ---------------------------------------------------------------------------

class TestMakeRunEnvHomeInjection:
    """Verify _make_run_env() applies the subprocess HOME policy."""

    def test_host_auto_preserves_real_home_when_profile_home_exists(self, tmp_path, monkeypatch):
        nastech_home = tmp_path / "nastech"
        nastech_home.mkdir()
        (nastech_home / "home").mkdir()
        real_home = tmp_path / "real-home"
        real_home.mkdir()
        monkeypatch.setattr(nastech_constants, "is_container", lambda: False)
        monkeypatch.setenv("NASTECH_HOME", str(nastech_home))
        monkeypatch.setenv("HOME", str(real_home))
        monkeypatch.setenv("PATH", "/usr/bin:/bin")

        from tools.environments.local import _make_run_env
        result = _make_run_env({})

        assert result["HOME"] == str(real_home)
        assert result["NASTECH_REAL_HOME"] == str(real_home)

    def test_profile_mode_injects_profile_home_when_profile_home_exists(self, tmp_path, monkeypatch):
        nastech_home = tmp_path / "nastech"
        nastech_home.mkdir()
        (nastech_home / "home").mkdir()
        real_home = tmp_path / "real-home"
        real_home.mkdir()
        monkeypatch.setattr(nastech_constants, "is_container", lambda: False)
        monkeypatch.setenv("TERMINAL_HOME_MODE", "profile")
        monkeypatch.setenv("NASTECH_HOME", str(nastech_home))
        monkeypatch.setenv("HOME", str(real_home))
        monkeypatch.setenv("PATH", "/usr/bin:/bin")

        from tools.environments.local import _make_run_env
        result = _make_run_env({})

        assert result["HOME"] == str(nastech_home / "home")
        assert result["NASTECH_REAL_HOME"] == str(real_home)

    def test_no_injection_when_home_dir_missing(self, tmp_path, monkeypatch):
        nastech_home = tmp_path / "nastech"
        nastech_home.mkdir()
        # No home/ subdirectory
        monkeypatch.setenv("NASTECH_HOME", str(nastech_home))
        monkeypatch.setenv("HOME", "/root")
        monkeypatch.setenv("PATH", "/usr/bin:/bin")

        from tools.environments.local import _make_run_env
        result = _make_run_env({})

        assert result["HOME"] == "/root"

    def test_no_injection_when_nastech_home_unset(self, monkeypatch):
        monkeypatch.delenv("NASTECH_HOME", raising=False)
        monkeypatch.setenv("HOME", "/home/user")
        monkeypatch.setenv("PATH", "/usr/bin:/bin")

        from tools.environments.local import _make_run_env
        result = _make_run_env({})

        assert result["HOME"] == "/home/user"



# ---------------------------------------------------------------------------
# _sanitize_subprocess_env() injection
# ---------------------------------------------------------------------------

class TestSanitizeSubprocessEnvHomeInjection:
    """Verify _sanitize_subprocess_env() applies the subprocess HOME policy."""

    def test_host_auto_preserves_real_home_when_profile_home_exists(self, tmp_path, monkeypatch):
        nastech_home = tmp_path / "nastech"
        nastech_home.mkdir()
        (nastech_home / "home").mkdir()
        real_home = tmp_path / "real-home"
        real_home.mkdir()
        monkeypatch.setattr(nastech_constants, "is_container", lambda: False)
        monkeypatch.setenv("NASTECH_HOME", str(nastech_home))

        base_env = {"HOME": str(real_home), "PATH": "/usr/bin", "USER": "root"}
        from tools.environments.local import _sanitize_subprocess_env
        result = _sanitize_subprocess_env(base_env)

        assert result["HOME"] == str(real_home)
        assert result["NASTECH_REAL_HOME"] == str(real_home)

    def test_profile_mode_injects_profile_home_when_profile_home_exists(self, tmp_path, monkeypatch):
        nastech_home = tmp_path / "nastech"
        nastech_home.mkdir()
        (nastech_home / "home").mkdir()
        real_home = tmp_path / "real-home"
        real_home.mkdir()
        monkeypatch.setattr(nastech_constants, "is_container", lambda: False)
        monkeypatch.setenv("TERMINAL_HOME_MODE", "profile")
        monkeypatch.setenv("NASTECH_HOME", str(nastech_home))

        base_env = {"HOME": str(real_home), "PATH": "/usr/bin", "USER": "root"}
        from tools.environments.local import _sanitize_subprocess_env
        result = _sanitize_subprocess_env(base_env)

        assert result["HOME"] == str(nastech_home / "home")
        assert result["NASTECH_REAL_HOME"] == str(real_home)

    def test_no_injection_when_home_dir_missing(self, tmp_path, monkeypatch):
        nastech_home = tmp_path / "nastech"
        nastech_home.mkdir()
        monkeypatch.setenv("NASTECH_HOME", str(nastech_home))

        base_env = {"HOME": "/root", "PATH": "/usr/bin"}
        from tools.environments.local import _sanitize_subprocess_env
        result = _sanitize_subprocess_env(base_env)

        assert result["HOME"] == "/root"



# ---------------------------------------------------------------------------
# Profile bootstrap
# ---------------------------------------------------------------------------

class TestProfileBootstrap:
    """Verify new profiles get a home/ subdirectory."""

    def test_profile_dirs_includes_home(self):
        from nastech_cli.profiles import _PROFILE_DIRS
        assert "home" in _PROFILE_DIRS

    def test_create_profile_bootstraps_home_dir(self, tmp_path, monkeypatch):
        """create_profile() should create home/ inside the profile dir."""
        home = tmp_path / ".nastech"
        home.mkdir()
        monkeypatch.setattr(Path, "home", lambda: tmp_path)
        monkeypatch.setenv("NASTECH_HOME", str(home))

        from nastech_cli.profiles import create_profile
        profile_dir = create_profile("testbot", no_alias=True)
        assert (profile_dir / "home").is_dir()


# ---------------------------------------------------------------------------
# Python process HOME unchanged
# ---------------------------------------------------------------------------

