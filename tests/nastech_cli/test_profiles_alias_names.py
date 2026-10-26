"""``nastech profile`` alias names: profiles named like Nastech' server subcommands keep their alias.

A profile's wrapper alias is its own command on PATH (``~/.local/bin/<name>``); it does not shadow
``nastech dashboard``, ``nastech serve`` or ``nastech webapp``, so ``check_alias_collision`` admits those
names as main does: ``nastech profile create dashboard`` gets its ``dashboard`` alias, and ``profile
alias``, rename and import accept them.
"""
from __future__ import annotations

import subprocess

import pytest

from nastech_cli.profiles import check_alias_collision


@pytest.mark.parametrize("name", ["dashboard", "serve", "webapp"])
def test_an_alias_named_like_a_server_subcommand_is_allowed_as_on_main(monkeypatch, name):
    # No such command on PATH, so only Nastech' own rules decide.
    monkeypatch.setattr(subprocess, "run", lambda *a, **k: subprocess.CompletedProcess(a, 1, "", ""))

    assert check_alias_collision(name) is None
