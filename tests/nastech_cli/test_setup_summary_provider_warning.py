"""Setup summary must warn loudly when no provider got configured.

Regression test for the "wizard silently succeeds with no model" dead end:
cancelling the API-key prompt mid-wizard printed "Cancelled." but the wizard
continued through the remaining sections and finished "successfully" with no
working model configured (consumer-onboarding audit finding #7, Aug 2026).
"""

from unittest.mock import patch

from nastech_cli.auth import AuthError
from nastech_cli import nastech_subscription


def _summary_output(capsys, provider_ready: bool):
    from nastech_cli import setup as setup_mod

    if provider_ready:
        resolver = lambda *a, **k: "openrouter"  # noqa: E731
    else:
        def resolver(*a, **k):
            raise AuthError(
                "No inference provider configured.",
                code="no_provider_configured",
            )

    # Keep the summary fast/hermetic: stub the heavier feature probes.
    with patch("nastech_cli.auth.resolve_provider", resolver), \
         patch.object(nastech_subscription, "get_nastech_subscription_features") as feats:
        feats.side_effect = Exception("stubbed")
        try:
            setup_mod._print_setup_summary({}, "/tmp/nowhere")
        except Exception:
            # Downstream summary sections may fail from the stubbed
            # features — the provider warning prints first and is what
            # this test asserts on.
            pass
    return capsys.readouterr().out


def test_summary_warns_when_no_provider(capsys):
    out = _summary_output(capsys, provider_ready=False)
    assert "No inference provider is configured" in out
    assert "nastech model" in out
    assert "nastech setup --portal" in out


def test_summary_quiet_when_provider_ready(capsys):
    out = _summary_output(capsys, provider_ready=True)
    assert "No inference provider is configured" not in out
