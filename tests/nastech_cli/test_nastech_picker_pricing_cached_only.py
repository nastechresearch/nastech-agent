"""The Nastech picker row never starts a pricing fetch: the picker only uses the ids the Portal
unions append, and a cold pricing cache must not hold the picker open (salvage of #102099)."""

import nastech_cli.models_pricing as mp
from nastech_cli import model_switch_providers as msp


def test_nastech_picker_model_ids_reads_pricing_cache_only(monkeypatch):
    seen: list[bool] = []

    def fake_pricing(provider, *, force_refresh=False, cached_only=False):
        seen.append(cached_only)
        return {}

    monkeypatch.setattr(mp, "get_pricing_for_provider", fake_pricing)
    # Keep the sibling Portal calls off the network; only the pricing call shape is under test.
    monkeypatch.setattr("nastech_cli.models.check_nastech_free_tier", lambda **kw: False)
    monkeypatch.setattr("nastech_cli.models.fetch_nastech_recommended_models", lambda *a, **kw: None)
    monkeypatch.setattr(mp, "nastech_policy_allowed_ids", lambda **kw: None)

    assert msp._nastech_picker_model_ids({"nastech": ["nastech/a"]}, False) == ["nastech/a"]
    assert seen == [True]
