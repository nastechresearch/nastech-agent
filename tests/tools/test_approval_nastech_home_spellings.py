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


class TestShellEscapedSpaceInWindowsHome:
    r"""Git Bash writes an unquoted path with a space as ``John\ Smith``. The fold has to see through
    the backslash, or a profile whose name contains a space loses the gate on its config.yaml."""

    def test_the_escaped_profile_space_still_gates_a_config_edit(self, monkeypatch):
        profile = r"C:\Users\John Smith"
        monkeypatch.setenv("HOME", profile)
        monkeypatch.setenv("USERPROFILE", profile)
        monkeypatch.setenv("LOCALAPPDATA", profile + r"\AppData\Local")
        monkeypatch.setenv("NASTECH_HOME", profile + r"\AppData\Local\nastech")
        assert _is_dangerous(r"sed -i s/a/b/ /c/Users/John\ Smith/AppData/Local/nastech/config.yaml") is True
        assert _is_dangerous(r"sed -i s/a/b/ /c/Users/John\ Smith/AppData/Local/nastech2/config.yaml") is False


class TestEscapedSpaceFailsClosed:
    r"""An unquoted ``\ `` is the same character as a space, so a path spelled through it is the home.
    Whether a given ``\ `` is unquoted takes a full shell parse: a quote in a comment, a heredoc body
    or a backtick flips every lexical quote model for the rest of the command. The fold therefore
    reads every ``\ `` inside a home spelling as a space; a quoted one costs a prompt, a misread one
    would lose the gate on the approval policy file."""

    @pytest.fixture
    def spaced_nastech_home(self, monkeypatch):
        monkeypatch.setenv("HOME", "/home/tester")
        monkeypatch.setenv("NASTECH_HOME", "/home/tester/nastech data")

    @pytest.fixture
    def spaced_user_home(self, monkeypatch):
        monkeypatch.setenv("HOME", "/home/John Smith")
        monkeypatch.setenv("NASTECH_HOME", "/home/John Smith/nastech")

    def test_the_escaped_home_itself_is_still_gated(self, spaced_nastech_home):
        assert _is_dangerous(r"mv /home/tester/nastech\ data /home/tester/backup") is True
        assert _is_dangerous(r"sed -i s/a/b/ /home/tester/nastech\ data/config.yaml") is True

    def test_an_escaped_space_after_the_home_continues_the_name(self, spaced_nastech_home):
        # `nastech\ data\ backup` is one directory, a sibling of the home, not the home plus a word.
        # Quoted, the backslash is literal and the name is no closer to the home: no quote state matters.
        assert _is_dangerous(r"mv /home/tester/nastech\ data\ backup /home/tester/backup") is False
        assert _is_dangerous(r"mv '/home/tester/nastech\ data\ backup' /home/tester/backup") is False

    def test_an_escaped_space_after_a_spaceless_home_continues_the_name(self, monkeypatch):
        monkeypatch.setenv("HOME", "/home/tester")
        monkeypatch.setenv("NASTECH_HOME", "/home/tester/nastech")
        assert _is_dangerous(r"mv /home/tester/nastech\ backup /home/tester/backup") is False

    def test_an_escaped_backslash_before_a_space_ends_the_word(self, monkeypatch):
        # `\\\\` is one literal backslash, so the space after it splits words: a match ending on that
        # backslash is not followed by an escaped space and still folds, as on main.
        monkeypatch.setenv("HOME", "/home/tester")
        monkeypatch.setenv("NASTECH_HOME", "/home/tester/.nastech")
        assert _is_dangerous("sed -i s/a/b/ /home/tester/.nastech/config.yaml\\\\ x") is True

    def test_an_escaped_space_in_a_child_name_folds_the_home(self, monkeypatch):
        # `My\ Documents` and `nastech\ data-backup` are children of the user home: it still folds,
        # so an rm there is an ordinary home-relative delete, as on main, not a "delete in root path".
        monkeypatch.setenv("HOME", "/home/tester")
        for nastech_home in ("/home/tester/.nastech", "/home/tester/nastech data"):
            monkeypatch.setenv("NASTECH_HOME", nastech_home)
            assert _is_dangerous(r"rm /home/tester/My\ Documents/a.txt") is False
            assert _is_dangerous(r"rm -f /home/tester/old\ notes.txt") is False
            assert _is_dangerous(r"rm /home/tester/nastech\ data-backup/state.db") is False

    @pytest.mark.parametrize("suffix", [
        r"${u:+\ }", r"${u#\ }", r"${u%%\ }", r"${u/x/\ }",
        r"{,\ }", r"{\ ,}", r"{,}{,\ }", r"{,.x\ y}", r"{,/x\ }",
    ])
    @pytest.mark.parametrize("home, nastech_home, user_home", [
        ("/home/John Smith", "/home/John Smith/nastech", r"/home/John\ Smith"),
        ("/home/tester", "/home/tester/nastech data", "/home/tester"),
    ])
    @pytest.mark.parametrize("template", [
        "sed -i s/a/b/ {nastech}/config.yaml{suffix}",
        'sed -i s/a/b/ "{nastech}/config.yaml{suffix}"',
        "cat /tmp/evil | tee {nastech}/config.yaml{suffix}",
        "cat k | tee -a {home}/.ssh/authorized_keys{suffix}",
        "cat k >> {home}/.ssh/authorized_keys{suffix}",
        "echo x >> {home}/.bashrc{suffix}",
    ])
    def test_an_expansion_after_the_path_does_not_hide_it(
            self, monkeypatch, suffix, home, nastech_home, user_home, template):
        # An unquoted expansion can still name the original file. Bash leaves braces literal
        # inside double quotes; those rows check that the detector errs on the side of prompting.
        monkeypatch.setenv("HOME", home)
        monkeypatch.setenv("NASTECH_HOME", nastech_home)
        nastech = user_home + nastech_home[len(home):].replace(" ", "\\ ")
        assert _is_dangerous(template.format(nastech=nastech, home=user_home, suffix=suffix)) is True

    def test_an_unquoted_escaped_space_folds(self, spaced_user_home):
        assert _is_dangerous(r"sed -i s/a/b/ /home/John\ Smith/nastech/config.yaml") is True
        assert _is_dangerous(r"sed -i s/a/b/ /home/John\ Smith/nastech2/config.yaml") is False

    @pytest.mark.parametrize("prefix", [
        "echo hi # don't\n",
        "# it's\n",
        "cat <<EOF >/dev/null\nit's\nEOF\n",
        "cat <<-EOF >/dev/null\n\tit's\n\tEOF\n",
        ': <<EOF\n"\nEOF\n',
        "echo `echo '`; ",
        'echo `echo "`; ',
        "echo ${x#'}; ",
        "echo {a,'}; ",
    ])
    @pytest.mark.parametrize("home, nastech_home, path", [
        ("/home/John Smith", "/home/John Smith/nastech", r"/home/John\ Smith/nastech/config.yaml"),
        ("/home/tester", "/home/tester/nastech data", r"/home/tester/nastech\ data/config.yaml"),
    ])
    def test_a_stray_quote_earlier_does_not_hide_an_unquoted_escape(
            self, monkeypatch, prefix, home, nastech_home, path):
        # Earlier quote-like text must not prevent the detector from folding the later path,
        # even when the prefix itself would not parse in Bash.
        monkeypatch.setenv("HOME", home)
        monkeypatch.setenv("NASTECH_HOME", nastech_home)
        assert _is_dangerous(prefix + "sed -i s/a/b/ " + path) is True

    @pytest.mark.parametrize("command", [
        r"sed -i s/a/b/ '/home/John\ Smith/nastech/config.yaml'",
        r'sed -i s/a/b/ "/home/John\ Smith/nastech/config.yaml"',
        r'bash -c "sed -i s/a/b/ /home/John\ Smith/nastech/config.yaml"',
        r'echo "$(sed -i s/a/b/ /home/John\ Smith/nastech/config.yaml)"',
    ])
    def test_an_escape_in_any_quote_context_gates(self, spaced_user_home, command):
        assert _is_dangerous(command) is True

    def test_deeply_nested_substitutions_fold_without_recursing(self, spaced_user_home):
        path = r"/home/John\ Smith/nastech/config.yaml"
        # Every level is a double-quoted `"$(`, a fresh quote context the shell reads the escape in.
        command = "echo " + '"$(' * 3000 + "sed -i s/a/b/ " + path + ')"' * 3000
        assert "~/.nastech/config.yaml" in approval_home_fold._rewrite_resolved_nastech_home(command)
