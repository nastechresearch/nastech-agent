"""A failed snapshot copy logs its warning under main's logger name, ``nastech_cli.backup_sqlite``, the name main's
``nastech_cli/backup_sqlite.py`` logs under (``logging.getLogger(__name__)``), so ``nastech logs`` selects the record
where it selected main's."""

from __future__ import annotations

import logging

import pytest

from nastech_cli import backup_sqlite
from persistence.sqlite.admin import _backup

_MAIN_LOGGER = "nastech_cli.backup_sqlite"


@pytest.mark.parametrize("copy", [backup_sqlite._safe_copy_db, _backup._safe_copy_db], ids=["main", "backend"])
def test_a_failed_copy_warns_under_mains_logger(tmp_path, caplog, copy):
    dst = tmp_path / "copy.db"
    with caplog.at_level(logging.WARNING):
        assert copy(tmp_path / "missing.db", dst) is False
    assert [(r.name, r.levelno) for r in caplog.records if r.getMessage().startswith("SQLite safe copy failed")] == [
        (_MAIN_LOGGER, logging.WARNING)]
    assert not dst.exists()
