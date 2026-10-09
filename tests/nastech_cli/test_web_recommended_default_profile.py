"""``GET /api/model/recommended-default?provider=nastech`` answers for the requested profile.

The Nastech branch returned before the route entered the profile scope, so ``?profile=b`` got the
tier read, Portal URL and caches of the profile that launched the dashboard, and an unknown
profile answered 200 instead of the scope's 404. Only the Portal account read is stubbed.
"""

from types import SimpleNamespace

import pytest

pytest.importorskip("fastapi")
from fastapi.testclient import TestClient


@pytest.fixture()
def client(_isolate_nastech_home, monkeypatch):
    from nastech_cli import profiles as profiles_mod

    freebie = profiles_mod.get_profile_dir("freebie")
    freebie.mkdir(parents=True, exist_ok=True)
    (freebie / "config.yaml").write_text("model: {}\n", encoding="utf-8")

    from nastech_constants import get_nastech_home
    from nastech_cli import nastech_account

    # The launch profile's account is paid, the "freebie" profile's is free tier.
    monkeypatch.setattr(nastech_account, "get_nastech_portal_account_info", lambda **_k: SimpleNamespace(
        is_free_tier=get_nastech_home().name == "freebie"))

    from nastech_cli.web_server import app, _SESSION_HEADER_NAME, _SESSION_TOKEN

    c = TestClient(app, raise_server_exceptions=False)
    c.headers[_SESSION_HEADER_NAME] = _SESSION_TOKEN
    return c


def test_nastech_recommendation_reads_the_requested_profile(client):
    launch = client.get("/api/model/recommended-default", params={"provider": "nastech"})
    named = client.get("/api/model/recommended-default",
                       params={"provider": "nastech", "profile": "freebie"})
    unknown = client.get("/api/model/recommended-default",
                         params={"provider": "nastech", "profile": "no-such-profile"})

    assert launch.status_code == named.status_code == 200
    assert launch.json()["free_tier"] is False
    assert named.json()["free_tier"] is True
    assert unknown.status_code == 404, unknown.text
    assert "no-such-profile" in unknown.json()["detail"]
