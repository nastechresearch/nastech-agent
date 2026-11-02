"""The #97905 offset invariant across a DST boundary, with the clock frozen.

``test_cron_next_run_profile_timezone.py`` proves the ticked profile's zone wins
over the backend process's, but it can only do that inside the weeks where the
two zones agree — a job stored the day before a transition fires the day after,
so the correct stored offset is one the running process has never observed.

Freezing ``cron.jobs._nastech_now`` (the seam ``compute_next_run`` reads its
base from) puts the tick at 14:30 EDT and the 14:00 fire in EST, so the
boundary is exercised on every run instead of twice a year.
"""
from datetime import UTC, datetime, timedelta
from zoneinfo import ZoneInfo

import pytest

import nastech_time

pytest.importorskip("croniter")

EASTERN = ZoneInfo("America/New_York")
# 2026-10-31 18:30Z is 14:30 EDT; the fall-back happens at 02:00 local the next
# morning, so the following 14:00 wall clock is 14:00 EST.
TICK = datetime(2026, 10, 31, 18, 30, tzinfo=UTC)
FIRE_IN_EST = datetime(2026, 11, 1, 14, 0, tzinfo=EASTERN)


@pytest.fixture(autouse=True)
def _fresh_tz_cache(monkeypatch):
    monkeypatch.delenv("NASTECH_TIMEZONE", raising=False)
    nastech_time.reset_cache()
    yield
    nastech_time.reset_cache()


def test_foreign_process_tick_across_dst_persists_fire_instant_offset(
    tmp_path, monkeypatch
):
    backend_home = tmp_path / "backend"
    profile_a = tmp_path / "north-caribbean"
    backend_home.mkdir()
    profile_a.mkdir()
    (backend_home / "config.yaml").write_text("timezone: UTC\n", encoding="utf-8")
    (profile_a / "config.yaml").write_text(
        "timezone: America/New_York\n", encoding="utf-8"
    )
    monkeypatch.setenv("NASTECH_HOME", str(backend_home))

    from cron import jobs
    monkeypatch.setattr(jobs, "_nastech_now", lambda: TICK)

    from nastech_constants import (
        reset_nastech_home_override,
        set_nastech_home_override,
    )

    token = set_nastech_home_override(str(profile_a))
    try:
        with jobs.use_cron_store(profile_a):
            jobs.create_job(name="daily-2pm", prompt="x", schedule="0 14 * * *")
            job = jobs.load_jobs()[0]
    finally:
        reset_nastech_home_override(token)

    next_run = datetime.fromisoformat(job["next_run_at"])
    assert (next_run.hour, next_run.minute) == (14, 0), (
        f"next_run_at {job['next_run_at']} left the cron wall clock behind "
        "(#97905: croniter must be anchored to the owning profile's zone)"
    )
    assert next_run == FIRE_IN_EST, (
        f"job due at {next_run.isoformat()}, expected {FIRE_IN_EST.isoformat()} — "
        f"stored offset {next_run.utcoffset()} is the tick instant's season, not "
        "the fire instant's"
    )
    assert next_run.utcoffset() == timedelta(hours=-5) != TICK.astimezone(
        EASTERN
    ).utcoffset(), "the fall-back offset must be resolved, not inherited from now"
    assert next_run > TICK, "a boundary-day schedule must never come due in the past"
