from pathlib import Path
from unittest.mock import MagicMock


def test_default_config_exposes_vacuum_interval():
    from nastech_cli.config import DEFAULT_CONFIG

    assert DEFAULT_CONFIG["sessions"]["min_vacuum_interval_days"] == 30


def test_default_config_auto_prune_on_with_90_day_retention():
    """#54189: state.db retention is ON by default (ended sessions, 90 days)."""
    from nastech_cli.config import DEFAULT_CONFIG

    sessions = DEFAULT_CONFIG["sessions"]
    assert sessions["auto_prune"] is True
    assert sessions["retention_days"] == 90
    assert sessions["vacuum_after_prune"] is True


def test_fresh_config_runs_auto_prune_at_startup(monkeypatch, tmp_path: Path):
    """A config.yaml with NO ``sessions:`` keys must reach the prune call with the
    new defaults (the loader deep-merges DEFAULT_CONFIG)."""
    import cli
    import nastech_cli.config
    import nastech_constants
    from nastech_cli.config import DEFAULT_CONFIG

    session_db = MagicMock()
    session_db.get_meta.return_value = "already-done"
    # Simulate load_config() on a fresh home: only defaults for the section.
    monkeypatch.setattr(
        nastech_cli.config,
        "load_config",
        lambda: {"sessions": dict(DEFAULT_CONFIG["sessions"])},
    )
    monkeypatch.setattr(nastech_constants, "get_nastech_home", lambda: tmp_path)

    cli._run_state_db_auto_maintenance(session_db)

    session_db.maybe_auto_prune_and_vacuum.assert_called_once_with(
        retention_days=90,
        min_interval_hours=24,
        min_vacuum_interval_days=30,
        vacuum=True,
        sessions_dir=tmp_path / "sessions",
    )


def test_explicit_auto_prune_false_is_respected(monkeypatch, tmp_path: Path):
    """Migration guard: an install that explicitly opted out keeps its choice."""
    import cli
    import nastech_cli.config
    import nastech_constants

    session_db = MagicMock()
    session_db.get_meta.return_value = "already-done"
    monkeypatch.setattr(
        nastech_cli.config,
        "load_config",
        lambda: {"sessions": {"auto_prune": False, "retention_days": 90}},
    )
    monkeypatch.setattr(nastech_constants, "get_nastech_home", lambda: tmp_path)

    cli._run_state_db_auto_maintenance(session_db)

    session_db.maybe_auto_prune_and_vacuum.assert_not_called()


def test_shipped_template_does_not_pin_sessions_keys():
    """Installers copy cli-config.yaml.example verbatim into config.yaml, so any
    uncommented ``sessions:`` value there becomes an EXPLICIT user setting that
    would freeze the retention defaults. The template must leave them commented
    so code defaults (and future flips) apply."""
    import yaml

    template = Path(__file__).resolve().parents[1] / "cli-config.yaml.example"
    data = yaml.safe_load(template.read_text(encoding="utf-8")) or {}
    assert "sessions" not in data


def test_loader_yields_new_defaults_for_fresh_home(monkeypatch, tmp_path: Path):
    """Real load_config() against an empty NASTECH_HOME → auto_prune on, 90 days."""
    monkeypatch.setenv("NASTECH_HOME", str(tmp_path))
    from nastech_cli.config import load_config

    sessions = load_config().get("sessions") or {}
    assert sessions.get("auto_prune") is True
    assert sessions.get("retention_days") == 90


def test_cli_auto_maintenance_forwards_vacuum_interval(monkeypatch, tmp_path: Path):
    import cli
    import nastech_cli.config
    import nastech_constants

    session_db = MagicMock()
    session_db.get_meta.return_value = "already-done"
    monkeypatch.setattr(
        nastech_cli.config,
        "load_config",
        lambda: {
            "sessions": {
                "auto_prune": True,
                "retention_days": 90,
                "vacuum_after_prune": True,
                "min_interval_hours": 24,
                "min_vacuum_interval_days": 17,
            }
        },
    )
    monkeypatch.setattr(nastech_constants, "get_nastech_home", lambda: tmp_path)

    cli._run_state_db_auto_maintenance(session_db)

    session_db.maybe_auto_prune_and_vacuum.assert_called_once_with(
        retention_days=90,
        min_interval_hours=24,
        min_vacuum_interval_days=17,
        vacuum=True,
        sessions_dir=tmp_path / "sessions",
    )
