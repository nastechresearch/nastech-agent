"""Regression tests for Nastech Portal inference_base_url host-allowlist validation.

A poisoned ``inference_base_url`` from a Portal refresh response (network
MITM, malicious response injection) would otherwise be persisted to
auth.json and forwarded with the user's legitimate invoke JWT
bearer on every subsequent proxy request, exfiltrating their inference
budget and opening a response-injection channel into the IDE / chat
client. ``_validate_nastech_inference_url_from_network()`` blocks any URL
outside the allowlist at the source.

These tests verify:

1. The validator's host + scheme rules.
2. Each of the two NETWORK call sites in ``auth.py`` calls the validator
   rather than the unrestricted ``_optional_base_url`` helper.
3. The proxy adapter applies the validator as belt-and-suspenders.
4. The env-var override path (``NASTECH_INFERENCE_BASE_URL``) is NOT
   gated by the validator — that's the documented dev/staging escape
   hatch.
"""

from __future__ import annotations

import logging

from nastech_cli.auth import (
    DEFAULT_NASTECH_INFERENCE_URL,
    _ALLOWED_NASTECH_INFERENCE_HOSTS,
    _validate_nastech_inference_url_from_network,
)


class TestValidatorRules:


    def test_attacker_host_rejected(self, caplog):
        with caplog.at_level(logging.WARNING, logger="nastech_cli.auth"):
            assert (
                _validate_nastech_inference_url_from_network("https://attacker.com/v1")
                is None
            )
        assert any("attacker.com" in rec.message for rec in caplog.records)



    def test_default_inference_url_is_in_allowlist(self):
        """Sanity check: DEFAULT_NASTECH_INFERENCE_URL must itself validate.

        If anyone retargets the default away from
        ``inference-api.nastechresearch.github.io``, they MUST update the allowlist
        in the same change — otherwise the allowlist would reject the
        Portal's own legitimate default and break every install.
        """
        assert (
            _validate_nastech_inference_url_from_network(DEFAULT_NASTECH_INFERENCE_URL)
            == DEFAULT_NASTECH_INFERENCE_URL.rstrip("/")
        )



class TestCallSiteWiring:
    """Verify the validator is actually wired into all auth.py NETWORK call sites.

    These are not behaviour-end-to-end tests (the surrounding code is
    several hundred lines per site with extensive HTTP mocking
    requirements). They're text-grep contracts: if anyone replaces
    ``_validate_nastech_inference_url_from_network`` with the un-validated
    ``_optional_base_url`` again, the test catches it.

    Each site lives inside ``resolve_nastech_runtime_credentials`` and one
    helper (``_extend_state_from_refresh``). The shape we guard against
    is ``<helper>_url = _optional_base_url(<payload>.get("inference_base_url"))``
    — that's what the unsafe pre-fix code looked like, and the only
    semantic difference between the safe and unsafe helpers is the
    host-allowlist check.
    """

    def _read_auth_source(self):
        import nastech_cli.auth as _auth_mod
        from pathlib import Path
        return Path(_auth_mod.__file__).read_text(encoding="utf-8")

    def test_no_unvalidated_inference_base_url_assignments_remain(self):
        """No remaining ``_optional_base_url(...inference_base_url...)`` reads
        from Portal payloads. If you see a failure here, you've either
        added a new NETWORK site that needs validation, or downgraded an
        existing one back to the unsafe helper."""
        source = self._read_auth_source()
        for needle in (
            '_optional_base_url(refreshed.get("inference_base_url"))',
            '_optional_base_url(mint_payload.get("inference_base_url"))',
        ):
            assert needle not in source, (
                f"Found unvalidated network read: {needle!r}. "
                f"Use _validate_nastech_inference_url_from_network() instead."
            )

    def test_validator_wired_at_all_known_call_sites(self):
        """All 2 known auth.py NETWORK sites use the validator. If this count
        drops, someone removed protection; if it grows, audit the new
        site to be sure validation is appropriate."""
        source = self._read_auth_source()
        refresh_count = source.count(
            '_validate_nastech_inference_url_from_network(refreshed.get("inference_base_url"))'
        )
        mint_count = source.count(
            '_validate_nastech_inference_url_from_network(mint_payload.get("inference_base_url"))'
        )
        assert refresh_count == 2, f"expected 2 refresh sites, found {refresh_count}"
        assert mint_count == 0, f"expected 0 mint sites, found {mint_count}"

    def test_proxy_adapter_also_validates(self):
        """The Nastech proxy adapter applies the validator as defense-in-depth
        even though auth.py already validates at the source, so a future
        bypass at the source layer still gets caught at the forward
        boundary."""
        from pathlib import Path
        import nastech_cli.proxy.adapters.nastech_portal as _nastech_adapter
        source = Path(_nastech_adapter.__file__).read_text(encoding="utf-8")
        assert "_validate_nastech_inference_url_from_network" in source


class TestEnvOverrideNotGated:
    """The documented dev/staging env-var override must keep working.

    ``NASTECH_INFERENCE_BASE_URL`` is read by ``resolve_nastech_runtime_credentials``
    via ``os.getenv`` — that path doesn't pass through the validator
    (env values are trusted because the user set them themselves).
    Verify the env-var read site does NOT consult the validator, so a
    user running against a non-allowlisted staging host via env is not
    inadvertently broken by this fix.
    """

    def test_env_override_path_does_not_call_validator(self):
        """In resolve_nastech_runtime_credentials, the env override is
        read via os.getenv directly, not via the validator. Grep the
        source to confirm: the env line should NOT mention the
        validator."""
        import nastech_cli.auth as _auth_mod
        from pathlib import Path
        source = Path(_auth_mod.__file__).read_text(encoding="utf-8")
        # Find the env-override read line.
        for line in source.splitlines():
            if "NASTECH_INFERENCE_BASE_URL" in line and "os.getenv" in line:
                assert "_validate_nastech_inference_url_from_network" not in line, (
                    "env override path must not gate through the network "
                    "validator — it would break documented dev/staging use."
                )


class TestHealsPoisonedStoredValue:
    """A stored inference_base_url that is NOT in the allowlist (e.g. a
    stale ``stg-inference-api.nastechresearch.github.io`` persisted before the
    allowlist existed) must be HEALED back to the production default on
    the next refresh — not silently retained.

    Before the fix, the refresh sites only assigned the validated URL
    ``if refreshed_url:`` and otherwise left the poisoned value in place,
    so the "falling back to default" warning was logged but never
    actually took effect — every subsequent call kept hitting the dead
    staging endpoint (real incident: opus-4.8 routed to nastech, nastech pinned
    to staging, every request + the aux compression call 401'd).
    """

    def test_refresh_resets_rejected_url_to_default(self, monkeypatch):
        import nastech_cli.auth as auth

        poisoned = "https://stg-inference-api.nastechresearch.github.io/v1"
        state = {
            "access_token": "tok",
            "refresh_token": "rtok",
            "client_id": "nastech-cli",
            "portal_base_url": auth.DEFAULT_NASTECH_PORTAL_URL,
            "inference_base_url": poisoned,
        }

        # Force the refresh branch and return another rejected (staging) URL,
        # exercising the validator-returns-None heal path.
        monkeypatch.setattr(auth, "_nastech_invoke_jwt_status", lambda *a, **k: "needs_refresh")
        monkeypatch.setattr(
            auth,
            "_refresh_access_token",
            lambda **k: {
                "access_token": "newtok",
                "refresh_token": "newrtok",
                "expires_in": 3600,
                "inference_base_url": poisoned,  # Portal still hands back staging
            },
        )
        # Skip the JWT usability assertions (orthogonal to URL healing).
        monkeypatch.setattr(auth, "_assert_nastech_inference_jwt_usable", lambda *a, **k: None)
        monkeypatch.setattr(auth, "_select_nastech_invoke_jwt", lambda *a, **k: None)

        result = auth.refresh_nastech_oauth_from_state(state, force_refresh=True)

        assert result["inference_base_url"] == auth.DEFAULT_NASTECH_INFERENCE_URL, (
            "rejected Portal URL must heal to the production default, "
            f"got {result['inference_base_url']!r}"
        )


class TestEnvOverrideWins:
    """``NASTECH_INFERENCE_BASE_URL`` must win over the stored value for the
    URL used to build the inference client / returned to callers.

    This is the documented dev/staging escape hatch. The breakage it
    regresses against: the security allowlist (#30611) plus the refresh
    heal (#49735) mean a staging login's stored ``inference_base_url`` is
    rejected and rewritten to the production default, and the runtime
    resolver previously read that stored (prod) value *before* the env
    var — so an OAuth user could not reach staging at all, even with the
    env override set. The override is consulted FIRST here, while the
    PERSISTED value stays the validated, network-provenance one (the env
    override is a runtime overlay, never written to auth.json).
    """

    STAGING = "https://stg-inference-api.nastechresearch.github.io/v1"

    def _patch_no_refresh(self, monkeypatch, auth, state):
        import contextlib

        # No refresh fires: the stored access token is a usable invoke JWT.
        monkeypatch.setattr(auth, "_nastech_invoke_jwt_status", lambda *a, **k: None)
        monkeypatch.setattr(
            auth, "_auth_store_lock", lambda *a, **k: contextlib.nullcontext()
        )
        monkeypatch.setattr(auth, "_load_auth_store", lambda *a, **k: {})
        monkeypatch.setattr(auth, "_load_provider_state", lambda store, pid: state)
        monkeypatch.setattr(
            auth,
            "_load_provider_state_with_source",
            lambda store, pid: (state, None),
        )
        monkeypatch.setattr(auth, "_save_provider_state", lambda *a, **k: None)
        monkeypatch.setattr(auth, "_save_provider_state_to_source", lambda *a, **k: None)
        monkeypatch.setattr(auth, "_save_auth_store", lambda *a, **k: None)
        monkeypatch.setattr(auth, "_write_shared_nastech_state", lambda *a, **k: None)
        monkeypatch.setattr(auth, "_sync_nastech_pool_from_auth_store", lambda *a, **k: None)
        monkeypatch.setattr(auth, "_resolve_verify", lambda *a, **k: True)
        monkeypatch.setattr(auth, "_assert_nastech_inference_jwt_usable", lambda *a, **k: None)
        monkeypatch.setattr(auth, "_select_nastech_invoke_jwt", lambda *a, **k: None)

    def _base_state(self, auth, stored):
        return {
            "access_token": "tok",
            "refresh_token": "rtok",
            "client_id": "nastech-cli",
            "portal_base_url": auth.DEFAULT_NASTECH_PORTAL_URL,
            "inference_base_url": stored,
            "agent_key": "ak-123",
        }


    def test_no_refresh_env_override_not_persisted(self, monkeypatch):
        """The env override is a runtime overlay: it must never be written
        back into the stored state (auth.json)."""
        import nastech_cli.auth as auth

        state = self._base_state(auth, auth.DEFAULT_NASTECH_INFERENCE_URL)
        self._patch_no_refresh(monkeypatch, auth, state)
        monkeypatch.setenv("NASTECH_INFERENCE_BASE_URL", self.STAGING)

        auth.resolve_nastech_runtime_credentials()

        assert state["inference_base_url"] == auth.DEFAULT_NASTECH_INFERENCE_URL, (
            "env override leaked into persisted state — it must stay a "
            f"runtime overlay, got {state['inference_base_url']!r}"
        )


    def test_no_refresh_heals_poisoned_stored_without_env(self, monkeypatch):
        """A poisoned stored staging host (persisted before the allowlist)
        still heals to the default when no env override is present — the
        #50265 no-refresh-read-path heal, folded in here."""
        import nastech_cli.auth as auth

        state = self._base_state(auth, self.STAGING)
        self._patch_no_refresh(monkeypatch, auth, state)
        monkeypatch.delenv("NASTECH_INFERENCE_BASE_URL", raising=False)

        result = auth.resolve_nastech_runtime_credentials()
        assert result["base_url"] == auth.DEFAULT_NASTECH_INFERENCE_URL, (
            "poisoned stored URL must heal to the production default on the "
            f"no-refresh read path, got {result['base_url']!r}"
        )



class TestProxyAdapterEnvOverride:
    """The Nastech proxy adapter is the second chokepoint: it re-validates the
    base_url returned by resolve_nastech_runtime_credentials() against the prod
    allowlist. That re-validation must not clobber a legitimate
    NASTECH_INFERENCE_BASE_URL staging override.
    """

    def test_proxy_adapter_consults_env_override(self):
        """Grep contract: the proxy adapter's forward-boundary base_url
        resolution consults the env override before the network validator,
        so a staging override survives the defense-in-depth re-validation."""
        from pathlib import Path
        import nastech_cli.proxy.adapters.nastech_portal as _nastech_adapter

        source = Path(_nastech_adapter.__file__).read_text(encoding="utf-8")
        assert "_nastech_inference_env_override()" in source, (
            "proxy adapter must layer the env override on top of the network "
            "validator, else a staging override is rejected at the forward boundary"
        )
        # The validator must still be present (defense-in-depth preserved).
        assert "_validate_nastech_inference_url_from_network" in source
