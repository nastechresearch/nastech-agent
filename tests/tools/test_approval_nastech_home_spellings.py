"""A sed -i of Nastech's own config.yaml is gated whichever way the shell spells NASTECH_HOME (#144033).

The home fold knew only the absolute native path. On Windows the default home is
``%LOCALAPPDATA%\\nastech``, and the agent's Git Bash terminal writes that file as
``/c/Users/<me>/AppData/Local/nastech/config.yaml``, ``~/AppData/Local/nastech/config.yaml``,
``$HOME/AppData/Local/nastech/config.yaml`` or ``$LOCALAPPDATA/nastech/config.yaml``. Every one of
those passed as safe, so an in-place edit there rewrote the approval policy (approvals.mode, yolo,
allowlist) mid-session. Platform-independent: the spellings are folded from the resolved home, and a
custom NASTECH_HOME under the user home reproduces the same gap on any OS.
"""

import pytest

from tools import approval_home_fold
from tools.approval import detect_dangerous_command

_PROFILE = r"C:\Users\tester"


def _is_dangerous(cmd: str) -> bool:
    return bool(detect_dangerous_command(cmd)[0])


@pytest.fixture
def windows_default_home(monkeypatch):
    """The Windows default NASTECH_HOME, reached through the profile the way Git Bash spells it."""
    monkeypatch.setenv("HOME", _PROFILE)
    monkeypatch.setenv("USERPROFILE", _PROFILE)
    monkeypatch.setenv("LOCALAPPDATA", _PROFILE + r"\AppData\Local")
    monkeypatch.setenv("NASTECH_HOME", _PROFILE + r"\AppData\Local\nastech")


class TestSpellingsOfTheNastechHome:
    def test_the_native_and_forward_slash_forms_were_always_gated(self, windows_default_home):
        assert _is_dangerous("sed -i s/a/b/ ~/.nastech/config.yaml") is True
        assert _is_dangerous("sed -i s/a/b/ C:/Users/tester/AppData/Local/nastech/config.yaml") is True

    @pytest.mark.parametrize("target", [
        "/c/Users/tester/AppData/Local/nastech/config.yaml",  # Git Bash drive form
        "/C/Users/tester/AppData/Local/nastech/config.yaml",
        "~/AppData/Local/nastech/config.yaml",  # home-relative
        "$HOME/AppData/Local/nastech/config.yaml",
        "${HOME}/AppData/Local/nastech/config.yaml",
        "$LOCALAPPDATA/nastech/config.yaml",  # the variable the default is built from
        "${LOCALAPPDATA}/nastech/config.yaml",
        "${USERPROFILE}/AppData/Local/nastech/config.yaml",
        r"%LOCALAPPDATA%\nastech\config.yaml",
    ])
    def test_every_spelling_of_the_windows_default_home_is_gated(self, windows_default_home, target):
        assert _is_dangerous(f"sed -i s/a/b/ {target}") is True

    def test_the_nastech_env_file_is_gated_too(self, windows_default_home):
        assert _is_dangerous("sed -i s/a/b/ /c/Users/tester/AppData/Local/nastech/.env") is True
        assert _is_dangerous("sed -i s/a/b/ $LOCALAPPDATA/nastech/.env") is True

    def test_the_long_in_place_flag_and_perl_are_gated(self, windows_default_home):
        assert _is_dangerous("sed --in-place s/a/b/ ~/AppData/Local/nastech/config.yaml") is True
        assert _is_dangerous("perl -pi -e s/a/b/ ${HOME}/AppData/Local/nastech/config.yaml") is True

    def test_a_custom_home_under_the_user_home_is_gated_on_any_os(self, monkeypatch):
        monkeypatch.setenv("HOME", "/home/tester")
        monkeypatch.setenv("NASTECH_HOME", "/home/tester/nastech-data")
        assert _is_dangerous("sed -i s/a/b/ ~/nastech-data/config.yaml") is True
        assert _is_dangerous("sed -i s/a/b/ $HOME/nastech-data/config.yaml") is True

    @pytest.mark.platforms("windows")
    def test_a_home_spelled_in_another_case_still_folds_on_windows(self, monkeypatch):
        monkeypatch.setenv("HOME", r"c:\users\tester")
        monkeypatch.setenv("NASTECH_HOME", r"C:\Users\tester\AppData\Local\nastech")
        assert _is_dangerous("sed -i s/a/b/ ~/AppData/Local/nastech/config.yaml") is True


class TestPathBelowCaseFold:
    """``_path_below`` folds case only on a Windows host, so a HOME and NASTECH_HOME that differ
    only in case still nest there. Runs on every lane by stubbing the host fact."""

    @pytest.mark.parametrize(("family", "expected"), [("win32", "AppData/Local/nastech"), ("linux", None)])
    def test_case_fold_follows_the_host_os_family(self, monkeypatch, family, expected):
        monkeypatch.setattr(approval_home_fold.facts, "os_family", lambda: family)
        assert approval_home_fold._path_below(r"c:\users\tester", r"C:\Users\tester\AppData\Local\nastech") == expected


class TestUnrelatedPathsStaySafe:
    """Folding a spelling must not turn a sibling config.yaml into Nastech's own policy file."""

    @pytest.mark.parametrize("target", [
        "/c/Users/tester/projects/app/config.yaml",
        "~/projects/app/config.yaml",
        "$LOCALAPPDATA/other/config.yaml",
        "/c/Users/tester/AppData/Local/nastech2/config.yaml",
    ])
    def test_a_sibling_config_yaml_is_not_flagged_as_nastech_policy(self, windows_default_home, target):
        assert _is_dangerous(f"sed -i s/a/b/ {target}") is False

    def test_a_sibling_of_a_custom_home_is_not_flagged(self, monkeypatch):
        monkeypatch.setenv("HOME", "/home/tester")
        monkeypatch.setenv("NASTECH_HOME", "/home/tester/nastech-data")
        assert _is_dangerous("sed -i s/a/b/ ~/nastech-data-old/config.yaml") is False
        assert _is_dangerous("sed -i s/a/b/ $HOME/nastech-data-old/config.yaml") is False
