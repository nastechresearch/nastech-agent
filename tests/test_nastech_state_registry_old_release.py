"""A process that loaded an older release's ``nastech_state`` before ``nastech update`` still gets a store from the
registry module it imports lazily afterwards."""

import importlib
import sys
import types


class _OldReleaseSessionDB:
    def __init__(self, db_path=None):
        self.db_path = db_path


def test_acquire_under_an_older_loaded_nastech_state_opens_that_releases_session_db(monkeypatch, tmp_path):
    old = types.ModuleType("nastech_state")
    old.SessionDB = _OldReleaseSessionDB  # type: ignore[attr-defined]
    monkeypatch.setitem(sys.modules, "nastech_state", old)
    monkeypatch.delitem(sys.modules, "nastech_state_registry", raising=False)
    registry = importlib.import_module("nastech_state_registry")
    try:
        db = registry.acquire(tmp_path / "state.db")
        assert isinstance(db, _OldReleaseSessionDB)
        assert db.db_path == tmp_path / "state.db"
    finally:
        sys.modules.pop("nastech_state_registry", None)
