# Nastech Update Report #1

- upstream sha : `508d6ec24ed293e46e5d7d1b88a6d67285243d97`
- source       : `/home/runner/work/100Ways/100Ways/upstream-agent`
- snapshot     : `Nastech-Update#1`
- gate         : **PASS**

## Stages

| # | stage | status | detail |
|---|-------|--------|--------|
| 1 | pull | ok | fresh direct clone from configured upstream |
| 2 | source-evidence | ok | record direct upstream added/modified/deleted/renamed source evidence |
| 3 | census | ok | count upstream files before touching anything |
| 4 | plan | ok | next snapshot = Nastech-Update#1 |
| 5 | brand | ok | brand source and materialize NasTech-owned assets after source deletion |
| 6 | reconcile | ok | sync lockfile root records + apply fork-local content fixes |
| 7 | preserve | ok | carry explicit fork-owned files while rejecting retired upstream paths |
| 8 | scan | ok | classify every branded file |
| 9 | compare | ok | diff branded tree vs upstream |
| 10 | verify | ok | file-by-file parity gate |
| 11 | forkcheck | ok | diff snapshot vs nastech-agent fork (identical/updated/added/missing) |
| 12 | report | pending | write UPDATE-REPORT.md + GATE-REPORT.md |
| 13 | package | pending | zip -> nastech-agent-update.zip |
| 14 | manifest | pending | write manifest.json |
| 15 | record | ok | record pipeline state |
| 16 | notify | ok | notify interested parties |
| 17 | gate | ok | final gate decision |
| 18 | summary | ok | pipeline summary + optional AI review |
| 19 | release | ok | release happens in GitHub Actions (build + gh release) |

## Stage timing

- total measured: 870.76 s
- profile: `100ways.stage-profile.v1`

| stage | status | duration | share |
|-------|--------|----------|-------|
| brand | ok | 277.53 s | 31.9% |
| verify | ok | 257.57 s | 29.6% |
| compare | ok | 252.34 s | 29.0% |
| pull | ok | 57.01 s | 6.5% |
| reconcile | ok | 12.00 s | 1.4% |
| forkcheck | ok | 9.73 s | 1.1% |
| summary | ok | 2.22 s | 0.3% |
| preserve | ok | 1.55 s | 0.2% |
| scan | ok | 0.62 s | 0.1% |
| source-evidence | ok | 0.14 s | 0.0% |
| census | ok | 0.04 s | 0.0% |
| plan | ok | 0.00 s | 0.0% |
| report | pending | 0.00 s | 0.0% |
| package | pending | 0.00 s | 0.0% |
| manifest | pending | 0.00 s | 0.0% |
| record | ok | 0.00 s | 0.0% |
| notify | ok | 0.00 s | 0.0% |
| gate | ok | 0.00 s | 0.0% |
| release | ok | 0.00 s | 0.0% |

Slowest: brand 277.5s, verify 257.6s, compare 252.3s.

## Brand

- total files : 21601
- renamed     : 3652 (folders and file names)
- text-rewritten : 21416
- locked-copied  : 157
- binary-copied  : 8
- owned assets   : 22 (our logo/banner/mascot override upstream)

## Reconcile

- fixed : 547 files reconciled: .env.example, .github/scripts/run-workspace-checks.mjs, .github/workflows/deploy-site.yml, .github/workflows/deploy-site.yml, .github/workflows/desktop-bundle-smoke.yml, .github/workflows/desktop-bundled-release.yml, .github/workflows/desktop-bundled-release.yml, .github/workflows/desktop-bundled-release.yml, .github/workflows/desktop-bundled-release.yml, .github/workflows/docs-search-monitor.yml, .github/workflows/install-e2e-macos-run.yml, .github/workflows/install-e2e-windows-run.yml, .github/workflows/js-tests.yml, .github/workflows/plugin-catalog-ci.yml, .github/workflows/skills-index-freshness.yml, .github/workflows/stable-release.yml, .github/workflows/tests-os.yml, .github/workflows/tests.yml, .github/workflows/tests.yml, .github/workflows/windows-install-update-e2e.yml, .mailmap, AGENTS.md, AGENTS.md, CONTRIBUTING.es.md, CONTRIBUTING.md, Dockerfile, README.es.md, README.md, README.ur-pk.md, README.zh-CN.md, SECURITY.es.md, SECURITY.es.md, SECURITY.md, SECURITY.md, agent/AGENTS.md, agent/agent_runtime_helpers.py, agent/anthropic_adapter.py, agent/anthropic_endpoints.py, agent/auxiliary_client.py, agent/auxiliary_client.py, agent/billing_links.py, agent/billing_view.py, agent/chat_completion_helpers.py, agent/conversation_compression.py, agent/conversation_loop.py, agent/error_classifier.py, agent/message_sanitization.py, agent/model_metadata.py, agent/onboarding_first_tasks.py, agent/prompt_builder.py, agent/proxy_sources/iron_proxy.py, agent/rate_limit_credits.py, agent/reasoning_params.py, agent/subscription_view.py, agent/turn_recovery.py, agent/usage_pricing.py, agent/usage_pricing.py, apps/bootstrap-installer/src-tauri/Cargo.toml, apps/desktop/README.md, apps/desktop/electron-builder.config.cjs, apps/desktop/electron/backend-health.test.ts, apps/desktop/electron/backend-health.ts, apps/desktop/electron/challenge-window.test.ts, apps/desktop/electron/cloud-session-recovery.test.ts, apps/desktop/electron/connection-config.test.ts, apps/desktop/electron/data-paths.test.ts, apps/desktop/electron/hub-iframe-policy.ts, apps/desktop/electron/oauth-partition.test.ts, apps/desktop/electron/portal-session.ts, apps/desktop/electron/remote-lifecycle.ts, apps/desktop/electron/remote-oauth-ticket.test.ts, apps/desktop/electron/update-stop-remedy.ts, apps/desktop/electron/updater/checkout-source.test.ts, apps/desktop/electron/updater/system-proxy-env.ts, apps/desktop/electron/window-open-policy.test.ts, apps/desktop/scripts/bundle-env.test.mjs, apps/desktop/src/app/chat/sidebar/section-states.tsx, apps/desktop/src/app/messaging/index.test.tsx, apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx, apps/desktop/src/app/settings/billing/api.test.ts, apps/desktop/src/app/settings/billing/dev-fixtures.ts, apps/desktop/src/app/settings/billing/errors.test.ts, apps/desktop/src/app/settings/billing/keep-going-on-credits-row.test.tsx, apps/desktop/src/app/settings/billing/use-billing-state.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.ts, apps/desktop/src/app/settings/billing/use-charge-poller.test.ts, apps/desktop/src/app/settings/billing/use-step-up.test.tsx, apps/desktop/src/app/settings/constants.ts, apps/desktop/src/app/settings/gateway-settings.test.tsx, apps/desktop/src/app/settings/gateway-settings.tsx, apps/desktop/src/app/settings/toolset-config-panel.test.tsx, apps/desktop/src/app/shell/terms-butterbar.tsx, apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts, apps/desktop/src/components/boot-failure-overlay.test.tsx, apps/desktop/src/components/boot-failure-overlay.tsx, apps/desktop/src/components/send-diagnostics-dialog.tsx, apps/desktop/src/components/update-status.tsx, apps/desktop/src/contrib/plugin.ts, apps/desktop/src/i18n/de.ts, apps/desktop/src/i18n/en.ts, apps/desktop/src/i18n/es.ts, apps/desktop/src/i18n/fr.ts, apps/desktop/src/i18n/ja.ts, apps/desktop/src/i18n/ru.ts, apps/desktop/src/i18n/zh-hant_settings.ts, apps/desktop/src/i18n/zh.ts, apps/desktop/src/lib/docs.ts, apps/desktop/src/lib/plugin-catalog.ts, apps/desktop/src/plugins/nastech-bots/skills-hub-picker.test.tsx, apps/desktop/src/plugins/nastech-bots/skills-hub.tsx, apps/desktop/src/sdk/index.ts, apps/desktop/src/store/free-tier-challenge.test.ts, apps/desktop/src/store/notifications.ts, apps/desktop/src/store/shared-metrics.ts, apps/desktop/src/themes/use-skin-command.ts, cli-config.yaml.example, cron/AGENTS.md, eslint.config.shared.mjs, evals/auth_pool_controls.py, evals/browser_use/single_run.py, evals/postmortem/live_ab/auth_stampede.py, evals/postmortem/live_ab/cache_concurrency_probe.py, evals/postmortem/review_probes/cache_estimator_probe.py, evals/postmortem/review_probes/credential_identity_probe.py, evals/reasoning_replay/harness.py, gateway/AGENTS.md, locales/_keys.desktop.json, locales/_keys.tui.json, nastech_cli/AGENTS.md, nastech_cli/anon_auth.py, nastech_cli/anon_auth.py, nastech_cli/anon_sign_in.py, nastech_cli/auth.py, nastech_cli/auth_codex.py, nastech_cli/auth_constants.py, nastech_cli/auth_constants.py, nastech_cli/auth_error_copy.py, nastech_cli/auth_nastech.py, nastech_cli/banner.py, nastech_cli/config_defaults.py, nastech_cli/dashboard_auth/login_page.py, nastech_cli/dashboard_register.py, nastech_cli/dashboard_register.py, nastech_cli/debug.py, nastech_cli/diagnostics_upload.py, nastech_cli/fallback_cmd.py, nastech_cli/gateway_chat_commands.py, nastech_cli/kanban_parser.py, nastech_cli/main.py, nastech_cli/main_dashboard.py, nastech_cli/main_desktop.py, nastech_cli/model_catalog.py, nastech_cli/model_setup_flows_common.py, nastech_cli/models.py, nastech_cli/models_pricing.py, nastech_cli/models_pricing.py, nastech_cli/nastech_account.py, nastech_cli/nastech_account.py, nastech_cli/nastech_billing.py, nastech_cli/nastech_billing.py, nastech_cli/observability/shared_metrics_consent.py, nastech_cli/observability/shared_metrics_send_config.py, nastech_cli/observability/shared_metrics_send_config.py, nastech_cli/plugin_catalog.py, nastech_cli/plugins_cmd.py, nastech_cli/portal_cli.py, nastech_cli/portal_cli.py, nastech_cli/providers.py, nastech_cli/proxy/adapters/base.py, nastech_cli/proxy/adapters/nastech_portal.py, nastech_cli/release_channels.py, nastech_cli/setup.py, nastech_cli/setup_platforms.py, nastech_cli/setup_quick.py, nastech_cli/skin_engine.py, nastech_cli/source_releases.py, nastech_cli/steward.py, nastech_cli/subcommands/egress.py, nastech_cli/subcommands/fallback.py, nastech_cli/subcommands/secrets.py, nastech_cli/subcommands/worktree.py, nastech_cli/telegram_managed_bot.py, nastech_cli/telegram_managed_bot.py, nastech_cli/tools_config.py, nastech_cli/uninstall.py, nastech_cli/update_cmd.py, nastech_cli/update_cmd_git.py, nastech_cli/update_cmd_git.py, nastech_cli/update_cmd_maint.py, nastech_cli/update_cmd_zip.py, nastech_cli/update_downgrade_guard.py, nastech_cli/web_routers/status.py, nastech_cli/web_server_messaging.py, nastech_cli/web_server_messaging.py, nastech_cli/web_server_oauth.py, nastech_constants.py, nastech_state_common.py, nastech_state_errors.py, nastech_state_reconcile.py, optional-skills/creative/pretext/templates/donut-orbit.html, optional-skills/productivity/memento-flashcards/SKILL.md, package-lock.json, plugin-catalog/README.md, plugins/AGENTS.md, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/plugin.yaml, plugins/kanban/dashboard/dist/index.js, plugins/kanban/systemd/nastech-kanban-dispatcher.service, plugins/model-providers/ai-gateway/__init__.py, plugins/model-providers/fireworks/__init__.py, plugins/model-providers/kimi-coding/__init__.py, plugins/model-providers/nastech/__init__.py, plugins/model-providers/opencode-zen/__init__.py, plugins/model-providers/solstice/auth.py, plugins/model-providers/solstice/auth.py, plugins/nastech-achievements/dashboard/dist/index.js, plugins/platforms/discord/adapter.py, plugins/platforms/discord/onboarding.py, plugins/platforms/email/adapter.py, plugins/platforms/google_chat/adapter.py, plugins/platforms/irc/adapter.py, plugins/platforms/line/adapter.py, plugins/platforms/ntfy/adapter.py, plugins/platforms/photon/adapter.py, plugins/platforms/photon/sidecar/package-lock.json, plugins/platforms/raft/adapter.py, plugins/platforms/simplex/adapter.py, plugins/platforms/slack/adapter.py, plugins/platforms/teams/adapter.py, plugins/platforms/weixin/adapter.py, plugins/platforms/whatsapp_cloud/adapter.py, plugins/platforms/whatsapp_cloud/setup_wizard.py, plugins/web/perplexity/provider.py, pm/artifact-mirror.json, pm/network.py, pm/uv.lock, scripts/build_model_catalog.py, scripts/ci/check_catalog_cors.py, scripts/contributor_audit.py, scripts/e2e_shared_metrics_staging.py, scripts/install.cmd, scripts/install.ps1, scripts/install.sh, scripts/release.py, scripts/release.py, scripts/releases/authors_legacy.py, scripts/releases/entrypoint.py, scripts/releases/lanes.py, scripts/releases/pick_tags.py, scripts/releases/r2.py, scripts/sandbox/generate-e2e-matrix.mjs, scripts/sandbox/pick-release-tags.sh, scripts/termux/stage_apt_repo.py, scripts/tests/test-install-ps1-store-guard.ps1, scripts/whatsapp-bridge/package-lock.json, setup.py, skills/AGENTS.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/references/background-systems.md, skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md, skills/autonomous-ai-agents/nastech-agent/references/configuration.md, skills/autonomous-ai-agents/nastech-agent/references/contributor-guide.md, skills/autonomous-ai-agents/nastech-agent/references/portal-auth-for-third-party-apps.md, skills/autonomous-ai-agents/nastech-agent/references/providers-and-models.md, skills/autonomous-ai-agents/nastech-agent/references/webhooks.md, skills/media/youtube-content/SKILL.md, skills/software-development/python-debugpy/SKILL.md, tests-js/bundle-smoke-metadata.test.mjs, tests-js/update-ui.test.mjs, tests/agent/test_anthropic_adapter.py, tests/agent/test_anthropic_preserved_thinking_replay.py, tests/agent/test_anthropic_prompt_cache_policy.py, tests/agent/test_auxiliary_auth_rung_fallthrough.py, tests/agent/test_auxiliary_client.py, tests/agent/test_auxiliary_client_nastech_401_cache_key.py, tests/agent/test_auxiliary_main_first.py, tests/agent/test_auxiliary_transport_autodetect.py, tests/agent/test_billing_links.py, tests/agent/test_credential_pool.py, tests/agent/test_credential_pool_nastech_refresh_stampede.py, tests/agent/test_credits_cold_start.py, tests/agent/test_credits_policy.py, tests/agent/test_credits_usage_window.py, tests/agent/test_deepseek_anthropic_thinking.py, tests/agent/test_error_classifier.py, tests/agent/test_error_classifier_observed.py, tests/agent/test_fast_mode_auto.py, tests/agent/test_free_tier_rate_limit_class.py, tests/agent/test_model_metadata.py, tests/agent/test_nastech_credits_gauge.py, tests/agent/test_nastech_key_pre_expiry_adoption.py, tests/agent/test_nastech_portal_anthropic_wire.py, tests/agent/test_nastech_rate_guard.py, tests/agent/test_nastech_welcome_client_contract.py, tests/agent/test_nastech_wire_auto.py, tests/agent/test_nonretryable_result_carries_verdict.py, tests/agent/test_onboarding_first_tasks.py, tests/agent/test_plan_limits.py, tests/agent/test_primary_runtime_restore.py, tests/agent/test_provider_attribution_headers.py, tests/agent/test_provider_fallback.py, tests/agent/test_provider_history_parity.py, tests/agent/test_provider_parity.py, tests/agent/test_reasoning_replay_routes.py, tests/agent/test_run_agent.py, tests/agent/test_run_agent.py, tests/agent/test_switch_model_reapplies_headers.py, tests/agent/test_turn_usage_log_line.py, tests/agent/test_welcome_error_identity.py, tests/agent/test_welcome_tier_recovery.py, tests/agent/transports/test_chat_completions.py, tests/agent/transports/test_chat_completions_reasoning_details_replay.py, tests/agent/transports/test_provider_wire_snapshot.py, tests/ci/test_stable_release_graph.py, tests/compat/old_updater_dependencies.py, tests/conftest.py, tests/conftest.py, tests/docker/test_sqlite_runtime.py, tests/e2e/core/live/_helpers.py, tests/e2e/core/providers/test_catalog_oauth.py, tests/e2e/core/providers/test_chat_reasoning_variants.py, tests/e2e/core/providers/test_fallback_providers.py, tests/e2e/core/upgrade/network/_seed.py, tests/e2e/core/windows/test_boot_lifecycle.py, tests/e2e/core/windows_update/_machine.py, tests/fakes/providers/chat_variants.py, tests/fakes/providers/vertex.py, tests/fixtures/prompt_surface/prompts/cli-code.claude.txt, tests/fixtures/prompt_surface/prompts/cli-code.claude.txt, tests/fixtures/prompt_surface/prompts/cli.claude.txt, tests/fixtures/prompt_surface/prompts/cli.claude.txt, tests/fixtures/prompt_surface/prompts/cli.gemini.txt, tests/fixtures/prompt_surface/prompts/cli.gemini.txt, tests/fixtures/prompt_surface/prompts/cli.gpt.txt, tests/fixtures/prompt_surface/prompts/cli.gpt.txt, tests/fixtures/prompt_surface/prompts/cli.nastech.txt, tests/fixtures/prompt_surface/prompts/cli.nastech.txt, tests/fixtures/prompt_surface/prompts/cron.claude.txt, tests/fixtures/prompt_surface/prompts/cron.claude.txt, tests/fixtures/prompt_surface/prompts/desktop.claude.txt, tests/fixtures/prompt_surface/prompts/desktop.claude.txt, tests/fixtures/prompt_surface/prompts/discord.claude.txt, tests/fixtures/prompt_surface/prompts/discord.claude.txt, tests/fixtures/prompt_surface/prompts/telegram.claude.txt, tests/fixtures/prompt_surface/prompts/telegram.claude.txt, tests/fixtures/prompt_surface/surfaces.json, tests/fixtures/prompt_surface/tools/tool_search.desktop.claude.json, tests/fixtures/provider_wire_snapshot.json, tests/gateway/fixtures/local_recovery_probe.py, tests/gateway/test_discord_format.py, tests/gateway/test_housekeeping_profile_scope.py, tests/gateway/test_internal_event_pin_wiring.py, tests/gateway/test_journey_compress_restart_fifo.py, tests/gateway/test_model_switch_persistence.py, tests/gateway/test_run_progress_topics.py, tests/gateway/test_session_model_override_persistence.py, tests/gateway/test_startup_warmup_profile_scope.py, tests/gateway/test_status_command.py, tests/gateway/test_telegram_mention_context.py, tests/gateway/test_usage_command.py, tests/install/macos-desktop-e2e.sh, tests/install/windows-e2e.ps1, tests/nastech_cli/anon_portal.py, tests/nastech_cli/test_anon_auth_core.py, tests/nastech_cli/test_anon_failure_modes.py, tests/nastech_cli/test_anon_failure_modes.py, tests/nastech_cli/test_anon_picker.py, tests/nastech_cli/test_anon_sign_in_flow.py, tests/nastech_cli/test_anon_surfaces.py, tests/nastech_cli/test_anon_upgrade.py, tests/nastech_cli/test_auth_nastech_provider.py, tests/nastech_cli/test_base_url_host_identity.py, tests/nastech_cli/test_browse_schema_drift.py, tests/nastech_cli/test_cli_first_run_setup.py, tests/nastech_cli/test_cli_goal_parked_resume.py, tests/nastech_cli/test_cli_init.py, tests/nastech_cli/test_cli_provider_resolution.py, tests/nastech_cli/test_dashboard_register.py, tests/nastech_cli/test_fireworks_provider.py, tests/nastech_cli/test_gateway_chat_native.py, tests/nastech_cli/test_guest_handoff.py, tests/nastech_cli/test_local_abandoned_requests.py, tests/nastech_cli/test_local_quickstart.py, tests/nastech_cli/test_local_runtime_processes.py, tests/nastech_cli/test_main_merge_lifecycle.py, tests/nastech_cli/test_model_catalog.py, tests/nastech_cli/test_model_picker_usage.py, tests/nastech_cli/test_model_validation.py, tests/nastech_cli/test_nastech_anthropic_wire_default.py, tests/nastech_cli/test_nastech_auth_keepalive.py, tests/nastech_cli/test_nastech_auth_status_cache.py, tests/nastech_cli/test_nastech_inference_url_validation.py, tests/nastech_cli/test_nastech_nonproduction_inference_host.py, tests/nastech_cli/test_nastech_nonproduction_inference_host.py, tests/nastech_cli/test_nastech_portal_staging_allowlist.py, tests/nastech_cli/test_nastech_reasoning_metadata.py, tests/nastech_cli/test_nastech_recommendation_mirror.py, tests/nastech_cli/test_proxy.py, tests/nastech_cli/test_reasoning_caps_disk_cache.py, tests/nastech_cli/test_release_channels.py, tests/nastech_cli/test_sale_pricing.py, tests/nastech_cli/test_show_config_credential.py, tests/nastech_cli/test_source_channel_integration.py, tests/nastech_cli/test_source_check.py, tests/nastech_cli/test_taskkill_identity_windows_live.py, tests/nastech_cli/test_update_channel_release_hold.py, tests/nastech_cli/test_update_fetch_failure_classifier.py, tests/nastech_cli/test_update_target_identity.py, tests/nastech_cli/test_web_oauth_dispatch.py, tests/plugins/dashboard_auth/test_nastech_provider.py, tests/plugins/image_gen/check_parity_vs_main.py, tests/plugins/image_gen/test_openrouter_compat_provider.py, tests/plugins/test_chronos_verify.py, tests/scripts/desktop_update/test_desktop_update_windows_commit_outcome.py, tests/scripts/desktop_update/test_desktop_update_windows_marker.py, tests/scripts/desktop_update/test_desktop_update_windows_marker_lock.py, tests/scripts/test_release_build_commit.py, tests/scripts/test_release_canary_git.py, tests/scripts/test_release_channels.py, tests/scripts/test_release_entrypoint.py, tests/scripts/test_release_lanes.py, tests/scripts/test_release_r2.py, tests/scripts/test_release_r2.py, tests/scripts/test_stable_release.py, tests/scripts/test_stage_apt_repo.py, tests/scripts/test_upload_summary.py, tests/test_live_nastech_services_fence.py, tests/test_session_daemon_reaper.py, tests/tools/test_connector_wire_identity.py, tests/tools/test_delegate.py, tests/tools/test_managed_media_gateways.py, tests/tools/test_managed_tool_gateway.py, tests/tools/test_plugin_guard.py, tests/tools/test_stage2_hook_nastech_routing_env.py, tests/tools/test_strict_provider_selection.py, tests/tools/test_tts_openai_config.py, tests/tools/test_url_safety.py, tests/tools/test_web_tools_config.py, tests/tools/test_web_tools_perplexity.py, tests/tui_gateway/test_compute_host.py, tests/tui_gateway/test_legacy_fallback_ticket_profile_verbs.py, tests/tui_gateway/test_resume_switched_provider_endpoint.py, tests/website/test_extract_skills.py, tools/AGENTS.md, tools/managed_gateway_auth.py, tools/managed_gateway_identity.py, tools/managed_tool_gateway.py, tools/mcp_oauth.py, tools/plugin_guard_context.py, tools/set_theme_tool.py, tools/skills_hub_search.py, trajectory_compressor.py, ui-tui/scripts/billing-fixtures.tsx, ui-tui/src/__tests__/canonicalDetachClose.test.tsx, ui-tui/src/__tests__/canonicalDetachOrdering.test.tsx, ui-tui/src/__tests__/canonicalSwitcherClose.test.tsx, ui-tui/src/__tests__/inkResumeSnapshotFence.test.tsx, ui-tui/src/__tests__/resumeEpochRenderer.test.tsx, ui-tui/src/__tests__/subscriptionCommand.test.ts, ui-tui/src/__tests__/subscriptionOverlay.test.tsx, ui-tui/src/app/slash/commands/subscription.ts, ui-tui/src/app/useSessionLifecycle.ts, ui-tui/src/domain/paths.ts, uv.lock, web/src/components/SharedMetricsConsentBanner.tsx, web/src/components/SidebarFooter.tsx, web/src/pages/DocsPage.tsx, web/src/pages/PluginsPage.tsx, web/src/pages/SystemPage.tsx, website/README.md, website/docs/developer-guide/egress-internals.md, website/docs/developer-guide/stable-releases.md, website/docs/getting-started/installation.md, website/docs/getting-started/platform-support.md, website/docs/getting-started/quickstart.md, website/docs/getting-started/termux.md, website/docs/getting-started/termux.md, website/docs/getting-started/updating.md, website/docs/guides/manage-nastech-cloud-with-mcp.md, website/docs/guides/run-nastech-with-nastech-portal.md, website/docs/guides/run-nemotron-3-ultra-free.md, website/docs/index.mdx, website/docs/integrations/nastech-portal.md, website/docs/integrations/providers.md, website/docs/reference/cli-commands.md, website/docs/reference/environment-variables.md, website/docs/reference/faq.md, website/docs/reference/model-catalog.md, website/docs/reference/skills-catalog.md, website/docs/user-guide/desktop.md, website/docs/user-guide/egress/iron-proxy.md, website/docs/user-guide/features/browser.md, website/docs/user-guide/features/image-generation.md, website/docs/user-guide/features/plugin-catalog.md, website/docs/user-guide/features/skills.md, website/docs/user-guide/features/subscription-proxy.md, website/docs/user-guide/features/tool-gateway.md, website/docs/user-guide/features/tools.md, website/docs/user-guide/features/tts.md, website/docs/user-guide/features/web-dashboard.md, website/docs/user-guide/features/web-search.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/skills/bundled/media/media-youtube-content.md, website/docs/user-guide/skills/bundled/software-development/software-development-python-debugpy.md, website/docs/user-guide/skills/optional/productivity/productivity-memento-flashcards.md, website/docs/user-guide/windows-native.md, website/docs/user-guide/windows-wsl-quickstart.md, website/docusaurus.config.ts, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/plugins/index.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/quickstart.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-nastech-with-nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/index.mdx, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/providers.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/faq.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/model-catalog.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/subscription-proxy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tools.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tts.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/media/media-youtube-content.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/software-development/software-development-python-debugpy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/optional/productivity/productivity-memento-flashcards.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-native.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-wsl-quickstart.md, website/scripts/check-live-search.mjs, website/scripts/check-live-search.mjs, website/scripts/extract-skills.py, website/scripts/fetch-plugin-stars.py, website/scripts/generate-llms-txt.py, website/scripts/prebuild.mjs, website/src/pages/plugins/index.tsx, website/src/pages/skills/index.tsx, website/static/api/model-catalog.json, website/static/oauth/client-metadata.json


## Direct upstream tree delta

- complete: +178 ~328 -0 ↪0
- MODIFIED `Dockerfile`
- MODIFIED `agent/codex_runtime.py`
- MODIFIED `agent/message_metadata.py`
- MODIFIED `agent/message_sanitization.py`
- MODIFIED `agent/moa_loop.py`
- MODIFIED `agent/prompt_builder.py`
- MODIFIED `agent/session_persistence.py`
- MODIFIED `agent/skill_utils.py`
- MODIFIED `agent/transcript_repair.py`
- MODIFIED `agent/turn_finalizer.py`
- MODIFIED `agent/turn_recovery.py`
- MODIFIED `agent/turn_response_intake.py`
- ADDED `apps/desktop/e2e/connection-version-label.spec.ts`
- MODIFIED `apps/desktop/e2e/core/oracle.ts`
- MODIFIED `apps/desktop/e2e/core/provider.ts`
- ADDED `apps/desktop/e2e/core/reattach-running-turn.spec.ts`
- ADDED `apps/desktop/e2e/core/reply-tail-after-reconnect.spec.ts`
- ADDED `apps/desktop/e2e/core/tail-resync-merge.spec.ts`
- ADDED `apps/desktop/electron/app-relaunch.test.ts`
- ADDED `apps/desktop/electron/app-relaunch.ts`
- MODIFIED `apps/desktop/electron/app-version.test.ts`
- MODIFIED `apps/desktop/electron/bundle-skew.test.ts`
- MODIFIED `apps/desktop/electron/bundle-skew.ts`
- MODIFIED `apps/desktop/electron/desktop-uninstall.test.ts`
- MODIFIED `apps/desktop/electron/desktop-uninstall.ts`
- MODIFIED `apps/desktop/electron/entry.ts`
- ADDED `apps/desktop/electron/fixtures/nvidia-recovery.ts`
- ADDED `apps/desktop/electron/fs-probes.ts`
- MODIFIED `apps/desktop/electron/handoff-result.ts`
- ADDED `apps/desktop/electron/launch-build-identity.test.ts`
- ADDED `apps/desktop/electron/launch-build-identity.ts`
- MODIFIED `apps/desktop/electron/linux-gpu-fallback.test.ts`
- MODIFIED `apps/desktop/electron/linux-gpu-fallback.ts`
- MODIFIED `apps/desktop/electron/linux-nvidia-egl-fallback.test.ts`
- MODIFIED `apps/desktop/electron/linux-nvidia-egl-fallback.ts`
- ADDED `apps/desktop/electron/linux-nvidia-egl-recovery.native.test.ts`
- ADDED `apps/desktop/electron/linux-nvidia-egl-recovery.test.ts`
- ADDED `apps/desktop/electron/linux-nvidia-egl-recovery.ts`
- ADDED `apps/desktop/electron/linux-sandbox-relaunch.test.ts`
- ADDED `apps/desktop/electron/linux-sandbox-relaunch.ts`
- ADDED `apps/desktop/electron/local-runtime-version.test.ts`
- ADDED `apps/desktop/electron/local-runtime-version.ts`
- MODIFIED `apps/desktop/electron/local-skin.ts`
- MODIFIED `apps/desktop/electron/main.ts`
- ADDED `apps/desktop/electron/packaged-working-directory.test.ts`
- ADDED `apps/desktop/electron/packaged-working-directory.ts`
- ADDED `apps/desktop/electron/preload-version-scope.test.ts`
- MODIFIED `apps/desktop/electron/preload.ts`
- ADDED `apps/desktop/electron/relaunch-target.test.ts`
- ADDED `apps/desktop/electron/relaunch-target.ts`
- ADDED `apps/desktop/electron/release-holder-consent.test.ts`
- ADDED `apps/desktop/electron/release-holder-consent.ts`
- MODIFIED `apps/desktop/electron/renderer-heap-flags.ts`
- ADDED `apps/desktop/electron/ui-preferences-ipc.ts`
- ADDED `apps/desktop/electron/ui-preferences.test.ts`
- ADDED `apps/desktop/electron/ui-preferences.ts`
- MODIFIED `apps/desktop/electron/update-handoff-report.test.ts`
- MODIFIED `apps/desktop/electron/update-handoff-report.ts`
- ADDED `apps/desktop/electron/update-stop-remedy.test.ts`
- ADDED `apps/desktop/electron/update-stop-remedy.ts`
- MODIFIED `apps/desktop/electron/updater-process.ts`
- MODIFIED `apps/desktop/electron/updater/checkout-handoff.test.ts`
- MODIFIED `apps/desktop/electron/updater/checkout-source.ts`
- MODIFIED `apps/desktop/electron/updater/checkout.ts`
- MODIFIED `apps/desktop/electron/updater/state-db-preflight.test.ts`
- MODIFIED `apps/desktop/electron/updater/state-db-preflight.ts`
- ADDED `apps/desktop/electron/updater/system-proxy-env.test.ts`
- ADDED `apps/desktop/electron/updater/system-proxy-env.ts`
- ADDED `apps/desktop/electron/updater/update-hosts.ts`
- ADDED `apps/desktop/electron/url-filename.ts`
- MODIFIED `apps/desktop/electron/window-connection-route.test.ts`
- MODIFIED `apps/desktop/electron/window-connection-route.ts`
- MODIFIED `apps/desktop/index.html`
- MODIFIED `apps/desktop/scripts/build-webapp.mjs`
- MODIFIED `apps/desktop/src/app/capabilities/index.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/browser-popout-handoff.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/hooks/use-auto-speak-replies.cross-window.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/hooks/use-composer-draft.ts`
- MODIFIED `apps/desktop/src/app/chat/composer/hooks/use-composer-queue.ts`
- ADDED `apps/desktop/src/app/chat/composer/hooks/use-composer-submit.send-then-close.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/hooks/use-composer-submit.ts`
- MODIFIED `apps/desktop/src/app/chat/composer/send-closes-completion-list.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/transcript-backfill.ts`
- ADDED `apps/desktop/src/app/chat/transcript-receipt-turns.local-rows.test.ts`
- ADDED `apps/desktop/src/app/chat/transcript-receipt-turns.test.ts`
- ADDED `apps/desktop/src/app/chat/transcript-receipt-turns.ts`
- ADDED `apps/desktop/src/app/contrib/hooks/use-background-sync.stopped-turn.test.ts`
- MODIFIED `apps/desktop/src/app/contrib/hooks/use-background-sync.ts`
- MODIFIED `apps/desktop/src/app/contrib/wiring.tsx`
- MODIFIED `apps/desktop/src/app/cron/index.test.tsx`
- MODIFIED `apps/desktop/src/app/gateway/hooks/use-gateway-request.test.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/branch-owner-routing.integration.test.ts`
- ADDED `apps/desktop/src/app/session/hooks/reconnect-resume-barrier.test.tsx`
- ADDED `apps/desktop/src/app/session/hooks/reload-resume-stream-target.test.tsx`
- ADDED `apps/desktop/src/app/session/hooks/resume-reattach-arming.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-background-queue-drain.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/gateway-event/message-stream.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-message-stream/gateway-event/settled-during-resume.test.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/gateway-event/types.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/index.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/interrupted-reply.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/receipt-user-rows.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-message-stream/segment-identity-replay.test.tsx`
- ADDED `apps/desktop/src/app/session/hooks/use-message-stream/segment-identity.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-owner-queue-reconcile.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-prompt-actions/submit-admitted-conflict.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/submit.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/utils.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-resume-reattach.test.tsx`
- ADDED `apps/desktop/src/app/session/hooks/use-resume-reattach.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-route-resume.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-session-actions/committed-reply.test.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-session-actions/committed-reply.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-actions/index.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-session-actions/message-equivalence.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-session-actions/resume-barrier-reread.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-session-actions/resume-latches.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-session-actions/resume-reconcile.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-session-actions/settled-turns.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-session-actions/utils-overlay-tool-calls.test.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-actions/utils.ts`
- MODIFIED `apps/desktop/src/app/settings/about-settings.tsx`
- MODIFIED `apps/desktop/src/app/settings/providers-settings.terminal-disconnect.test.tsx`
- MODIFIED `apps/desktop/src/app/types.ts`
- MODIFIED `apps/desktop/src/app/updates-overlay.tsx`
- ADDED `apps/desktop/src/components/assistant-ui/clarify/clarify-one-card-per-question.test.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/clarify/clarify-tool.test.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/clarify/index.tsx`
- ADDED `apps/desktop/src/components/assistant-ui/thread/list-row-identity.test.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/list.tsx`
- ADDED `apps/desktop/src/components/chat/diff-lines-seen.test.tsx`
- MODIFIED `apps/desktop/src/components/chat/diff-lines.test.tsx`
- MODIFIED `apps/desktop/src/components/chat/diff-lines.tsx`
- MODIFIED `apps/desktop/src/components/pane-shell/tree/renderer/floating-mode-memory.test.tsx`
- MODIFIED `apps/desktop/src/components/update-status.test.tsx`
- MODIFIED `apps/desktop/src/components/update-status.tsx`
- MODIFIED `apps/desktop/src/components/version-details.test.tsx`
- MODIFIED `apps/desktop/src/components/version-details.tsx`
- MODIFIED `apps/desktop/src/contrib/runtime-loader.ts`
- ADDED `apps/desktop/src/entry.ts`
- MODIFIED `apps/desktop/src/global.d.ts`
- ADDED `apps/desktop/src/hooks/use-seen-once.ts`
- MODIFIED `apps/desktop/src/i18n/ar_boot.ts`
- MODIFIED `apps/desktop/src/i18n/de.ts`
- MODIFIED `apps/desktop/src/i18n/de_notices.ts`
- MODIFIED `apps/desktop/src/i18n/en.ts`
- MODIFIED `apps/desktop/src/i18n/en_notices.ts`
- MODIFIED `apps/desktop/src/i18n/es.ts`
- MODIFIED `apps/desktop/src/i18n/es_notices.ts`
- MODIFIED `apps/desktop/src/i18n/fr.ts`
- MODIFIED `apps/desktop/src/i18n/fr_notices.ts`
- MODIFIED `apps/desktop/src/i18n/ja.ts`
- MODIFIED `apps/desktop/src/i18n/ja_notices.ts`
- MODIFIED `apps/desktop/src/i18n/ru.ts`
- MODIFIED `apps/desktop/src/i18n/ru_notices.ts`
- MODIFIED `apps/desktop/src/i18n/types.ts`
- MODIFIED `apps/desktop/src/i18n/types_notices.ts`
- MODIFIED `apps/desktop/src/i18n/zh-hant_boot.ts`
- MODIFIED `apps/desktop/src/i18n/zh.ts`
- MODIFIED `apps/desktop/src/i18n/zh_notices.ts`
- MODIFIED `apps/desktop/src/lib/browser-connection.ts`
- MODIFIED `apps/desktop/src/lib/browser-desktop-bridge.ts`
- ADDED `apps/desktop/src/lib/browser-desktop-plugins.test.ts`
- ADDED `apps/desktop/src/lib/browser-desktop-plugins.ts`
- ADDED `apps/desktop/src/lib/browser-ui-preferences.ts`
- ADDED `apps/desktop/src/lib/chat-messages.stopped-tool-fold.test.ts`
- MODIFIED `apps/desktop/src/lib/chat-messages/hydration.ts`
- MODIFIED `apps/desktop/src/lib/chat-messages/index.ts`
- MODIFIED `apps/desktop/src/lib/chat-messages/reconciliation.ts`
- MODIFIED `apps/desktop/src/lib/chat-messages/tool-parts.ts`
- MODIFIED `apps/desktop/src/lib/chat-messages/types.ts`
- ADDED `apps/desktop/src/lib/persist-store.ts`
- MODIFIED `apps/desktop/src/lib/persisted.ts`
- MODIFIED `apps/desktop/src/lib/query-client.test.ts`
- MODIFIED `apps/desktop/src/lib/query-client.ts`
- MODIFIED `apps/desktop/src/lib/storage.ts`
- ADDED `apps/desktop/src/lib/ui-preferences/boot.test.ts`
- ADDED `apps/desktop/src/lib/ui-preferences/boot.ts`
- ADDED `apps/desktop/src/lib/ui-preferences/guidance-sync.test.ts`
- ADDED `apps/desktop/src/lib/ui-preferences/keys.ts`
- ADDED `apps/desktop/src/lib/ui-preferences/merge.ts`
- ADDED `apps/desktop/src/lib/ui-preferences/outbox.ts`
- ADDED `apps/desktop/src/lib/ui-preferences/sync-concurrent.test.ts`
- ADDED `apps/desktop/src/lib/ui-preferences/sync-defaults.test.ts`
- ADDED `apps/desktop/src/lib/ui-preferences/sync-handoff.test.ts`
- ADDED `apps/desktop/src/lib/ui-preferences/sync-store.test.ts`
- ADDED `apps/desktop/src/lib/ui-preferences/sync.test.ts`
- ADDED `apps/desktop/src/lib/ui-preferences/sync.ts`
- MODIFIED `apps/desktop/src/main.tsx`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/bot-row.tsx`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/canonical-group-capabilities.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/canonical-group-capability-gates.test.tsx`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/canonical-group-reopen-by-name.test.tsx`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/cron.tsx`
- ADDED `apps/desktop/src/plugins/nastech-bots/data.nastech-handle.test.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/data.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/group-chat-view.tsx`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/group-chat.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/group-membership.ts`
- ADDED `apps/desktop/src/plugins/nastech-bots/group-rounds.nastech-handle.test.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/group-test-utils.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/plugin.mentions.test.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/plugin.tsx`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/relay.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/row-helpers.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/soul.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/types.ts`
- MODIFIED `apps/desktop/src/sdk/index.ts`
- ADDED `apps/desktop/src/store/admitted-submissions.ts`
- MODIFIED `apps/desktop/src/store/backdrop.ts`
- MODIFIED `apps/desktop/src/store/completion-sound.ts`
- MODIFIED `apps/desktop/src/store/composer-draft-retry.ts`
- MODIFIED `apps/desktop/src/store/composer-draft-stash.test.ts`
- MODIFIED `apps/desktop/src/store/composer-draft-stash.ts`
- ADDED `apps/desktop/src/store/composer-outbox-landed.ts`
- ADDED `apps/desktop/src/store/composer-outbox.ts`
- MODIFIED `apps/desktop/src/store/composer-queue.test.ts`
- MODIFIED `apps/desktop/src/store/composer-queue.ts`
- MODIFIED `apps/desktop/src/store/composer.ts`
- MODIFIED `apps/desktop/src/store/dead-session-prune.ts`
- MODIFIED `apps/desktop/src/store/external-links.ts`
- ADDED `apps/desktop/src/store/gateway-activation-epoch-groups.test.tsx`
- ADDED `apps/desktop/src/store/gateway-activation-epoch.ts`
- MODIFIED `apps/desktop/src/store/gateway.ts`
- MODIFIED `apps/desktop/src/store/haptics.ts`
- MODIFIED `apps/desktop/src/store/keybinds.ts`
- MODIFIED `apps/desktop/src/store/layout-flipped-sides.test.ts`
- MODIFIED `apps/desktop/src/store/onboarding-decide.test.ts`
- MODIFIED `apps/desktop/src/store/onboarding.ts`
- ADDED `apps/desktop/src/store/owner-queue-reconcile.test.ts`
- ADDED `apps/desktop/src/store/owner-queue-reconcile.ts`
- MODIFIED `apps/desktop/src/store/pending-submissions.ts`
- MODIFIED `apps/desktop/src/store/profile-rail-prefs.test.tsx`
- MODIFIED `apps/desktop/src/store/profile.ts`
- MODIFIED `apps/desktop/src/store/reasoning-disclosure.ts`
- MODIFIED `apps/desktop/src/store/session-dot-state.ts`
- MODIFIED `apps/desktop/src/store/session-states-profile-rename.test.ts`
- MODIFIED `apps/desktop/src/store/session-states.ts`
- MODIFIED `apps/desktop/src/store/session.ts`
- MODIFIED `apps/desktop/src/store/thread-timeline.ts`
- MODIFIED `apps/desktop/src/store/tool-view.ts`
- MODIFIED `apps/desktop/src/store/translucency.ts`
- ADDED `apps/desktop/src/store/updates-version-scope.test.ts`
- MODIFIED `apps/desktop/src/store/updates.ts`
- MODIFIED `apps/desktop/src/store/voice-prefs.ts`
- MODIFIED `apps/desktop/src/themes/user-themes.ts`
- MODIFIED `apps/shared/src/gateway-contract.generated.ts`
- MODIFIED `apps/shared/src/gateway-contract.openrpc.json`
- MODIFIED `apps/shared/src/plan-usage.ts`
- ADDED `contributors/emails/47145541+mertkayacs@users.noreply.github.com`
- ADDED `contributors/emails/chenleshu1988@gmail.com`
- ADDED `contributors/emails/jj5638521@users.noreply.github.com`
- ADDED `contributors/emails/karmateam5555@protonmail.com`
- ADDED `contributors/emails/piggy7063@126.com`
- ADDED `contributors/emails/sahil.jagtap45@gmail.com`
- ADDED `contributors/emails/sibeliusseraphini@gmail.com`
- ADDED `contributors/emails/zwmaupin@users.noreply.github.com`
- ADDED `gateway/active_lease_io.py`
- MODIFIED `gateway/pairing.py`
- MODIFIED `gateway/platforms/api_server.py`
- MODIFIED `gateway/platforms/api_server_authority_runs.py`
- MODIFIED `gateway/platforms/api_server_openai_routes.py`
- ADDED `gateway/platforms/api_server_profile_prefix.py`
- MODIFIED `gateway/platforms/api_server_response_admissions.py`
- MODIFIED `gateway/platforms/api_server_response_store.py`
- MODIFIED `gateway/platforms/api_server_room_dispatch.py`
- MODIFIED `gateway/platforms/api_server_runs.py`
- MODIFIED `gateway/platforms/webhook.py`
- MODIFIED `gateway/response_filters.py`
- MODIFIED `gateway/run_agent_cache.py`
- MODIFIED `gateway/run_bootstrap.py`
- MODIFIED `gateway/run_goals.py`
- MODIFIED `gateway/run_profile_reconcile.py`
- MODIFIED `gateway/run_runtime.py`
- MODIFIED `gateway/run_shutdown.py`
- MODIFIED `gateway/run_turn.py`
- MODIFIED `gateway/run_turn_persistence.py`
- MODIFIED `gateway/run_turn_runner.py`
- MODIFIED `gateway/session_api_turn.py`
- MODIFIED `gateway/session_authority.py`
- MODIFIED `gateway/session_bot.py`
- MODIFIED `gateway/session_contract.py`
- MODIFIED `gateway/session_control_actions.py`
- MODIFIED `gateway/session_controls.py`
- MODIFIED `gateway/session_display.py`
- MODIFIED `gateway/session_events.py`
- MODIFIED `gateway/session_finite.py`
- MODIFIED `gateway/session_hosted_rpc.py`
- MODIFIED `gateway/session_ingress_media.py`
- MODIFIED `gateway/session_local_recovery.py`
- MODIFIED `gateway/session_managed_worker.py`
- MODIFIED `gateway/session_worker_reservation.py`
- MODIFIED `gateway/status.py`
- ADDED `gateway/status_pid_records.py`
- MODIFIED `gateway/turn_executor.py`
- ADDED `gateway/turn_thread_reset.py`
- MODIFIED `nastech_cli/_subprocess_compat.py`
- MODIFIED `nastech_cli/active_sessions.py`
- MODIFIED `nastech_cli/auth.py`
- MODIFIED `nastech_cli/auth_model_picker.py`
- MODIFIED `nastech_cli/backup_sqlite.py`
- MODIFIED `nastech_cli/commands_completion.py`
- MODIFIED `nastech_cli/config.py`
- MODIFIED `nastech_cli/config_backend.py`
- MODIFIED `nastech_cli/config_defaults.py`
- MODIFIED `nastech_cli/config_read_errors.py`
- ADDED `nastech_cli/desktop_build_reuse.py`
- ADDED `nastech_cli/desktop_release_holders.py`
- MODIFIED `nastech_cli/env_loader.py`
- MODIFIED `nastech_cli/free_tier_bootstrap.py`
- MODIFIED `nastech_cli/main_desktop.py`
- ADDED `nastech_cli/main_desktop_apparmor.py`
- MODIFIED `nastech_cli/managed_scope.py`
- MODIFIED `nastech_cli/model_catalog.py`
- MODIFIED `nastech_cli/model_picker_usage.py`
- MODIFIED `nastech_cli/model_switch.py`
- MODIFIED `nastech_cli/model_switch_providers.py`
- MODIFIED `nastech_cli/models.py`
- MODIFIED `nastech_cli/process_identity.py`
- MODIFIED `nastech_cli/profiles.py`
- MODIFIED `nastech_cli/source_build.py`
- MODIFIED `nastech_cli/source_check.py`
- MODIFIED `nastech_cli/stale_modules.py`
- MODIFIED `nastech_cli/subcommands/gui.py`
- MODIFIED `nastech_cli/subcommands/peer.py`
- ADDED `nastech_cli/ui_preferences.py`
- MODIFIED `nastech_cli/update_cmd.py`
- MODIFIED `nastech_cli/update_cmd_check.py`
- MODIFIED `nastech_cli/update_cmd_fleet.py`
- MODIFIED `nastech_cli/update_custody.py`
- ADDED `nastech_cli/update_proxy_env.py`
- MODIFIED `nastech_cli/venv_sync.py`
- ADDED `nastech_cli/web_routers/desktop_plugins.py`
- MODIFIED `nastech_cli/web_routers/files.py`
- MODIFIED `nastech_cli/web_routers/status.py`
- ADDED `nastech_cli/web_routers/ui_preferences.py`
- MODIFIED `nastech_cli/web_server.py`
- MODIFIED `nastech_cli/web_server_dashboard.py`
- MODIFIED `nastech_cli/web_server_profiles.py`
- ADDED `nastech_cli/web_server_static_assets.py`
- MODIFIED `nastech_cli/web_server_surface.py`
- MODIFIED `nastech_cli/webapp.py`
- MODIFIED `nastech_cli/webapp_launcher.py`
- ADDED `nastech_state_compaction_display.py`
- MODIFIED `nastech_state_coverage.py`
- MODIFIED `nastech_state_gateway.py`
- MODIFIED `nastech_state_local.py`
- MODIFIED `nastech_state_messages.py`
- MODIFIED `nastech_state_runtime.py`
- ADDED `nastech_state_session_list.py`
- MODIFIED `nastech_state_sessions.py`
- MODIFIED `nastech_state_terminal.py`
- MODIFIED `nastech_state_timeline.py`
- MODIFIED `nastech_state_todo.py`
- MODIFIED `nastech_state_usage.py`
- MODIFIED `nastech_state_worker_compression.py`
- MODIFIED `locales/_keys.desktop.json`
- MODIFIED `nix/nastech-agent.nix`
- MODIFIED `nix/lib.nix`
- MODIFIED `nix/packages.nix`
- MODIFIED `nix/tests/agent-references.py`
- ADDED `nix/webapp.nix`
- MODIFIED `plugins/dashboard_auth/basic/__init__.py`
- MODIFIED `plugins/platforms/feishu/adapter.py`
- MODIFIED `plugins/platforms/feishu/feishu_comment_rules.py`
- MODIFIED `pm/environments.py`
- MODIFIED `pm/install.py`
- MODIFIED `pm/install_states.py`
- MODIFIED `providers/__init__.py`
- MODIFIED `scripts/build/agent.py`
- ADDED `scripts/build/desktop-reuse.mjs`
- MODIFIED `scripts/build/inputs.py`
- MODIFIED `scripts/build/node-deps.mjs`
- MODIFIED `scripts/ci/classify_changes.py`
- MODIFIED `scripts/desktop-update/marker.sh`
- MODIFIED `scripts/desktop-update/posix.sh`
- MODIFIED `scripts/desktop-update/windows.ps1`
- MODIFIED `scripts/install.ps1`
- MODIFIED `tests-js/node-deps.test.mjs`
- MODIFIED `tests-js/product-builders.test.mjs`
- MODIFIED `tests/agent/test_close_interrupted_tool_sequence.py`
- ADDED `tests/agent/test_codex_pending_tool_text.py`
- ADDED `tests/agent/test_flush_uid_reinsert_guard.py`
- ADDED `tests/agent/test_token_read_barrier_on_loop.py`
- ADDED `tests/agent/test_turn_response_intake_relay.py`
- MODIFIED `tests/gateway/conftest.py`
- ADDED `tests/gateway/test_active_lease_release_off_loop.py`
- ADDED `tests/gateway/test_active_lease_release_order.py`
- ADDED `tests/gateway/test_api_responses_store_off_loop.py`
- ADDED `tests/gateway/test_api_room_policy_settings.py`
- ADDED `tests/gateway/test_api_server_runs_room_policy_grant.py`
- ADDED `tests/gateway/test_api_server_turn_executor.py`
- ADDED `tests/gateway/test_authority_reconnect_gap.py`
- MODIFIED `tests/gateway/test_bot_chat_unadoptable_local_title.py`
- ADDED `tests/gateway/test_control_publish_off_loop.py`
- MODIFIED `tests/gateway/test_feishu_approval_buttons.py`
- ADDED `tests/gateway/test_feishu_card_action_gateway_authz.py`
- ADDED `tests/gateway/test_local_restore_lock_free.py`
- MODIFIED `tests/gateway/test_multiplex_api_server_routing.py`
- ADDED `tests/gateway/test_profile_store_open_off_loop.py`
- ADDED `tests/gateway/test_responses_cancel_keeps_terminal.py`
- ADDED `tests/gateway/test_responses_stream_flush_race.py`
- ADDED `tests/gateway/test_resume_omit_messages.py`
- MODIFIED `tests/gateway/test_status.py`
- MODIFIED `tests/gateway/test_status_strict_identity_live.py`
- ADDED `tests/gateway/test_submission_row_identity.py`
- ADDED `tests/gateway/test_turn_executor_reuse.py`
- ADDED `tests/gateway/test_turn_runner_reply_identity.py`
- ADDED `tests/gateway/test_worker_reservation_automation_principal.py`
- MODIFIED `tests/nastech_cli/test_backup_preflight.py`
- ADDED `tests/nastech_cli/test_backup_preflight_staging.py`
- MODIFIED `tests/nastech_cli/test_bundled_desktop_launch.py`
- ADDED `tests/nastech_cli/test_config_same_tick_rewrite.py`
- ADDED `tests/nastech_cli/test_desktop_apparmor_install_non_linux.py`
- ADDED `tests/nastech_cli/test_desktop_apparmor_sandbox.py`
- ADDED `tests/nastech_cli/test_desktop_build_reuse.py`
- ADDED `tests/nastech_cli/test_desktop_release_holder_windows_live.py`
- ADDED `tests/nastech_cli/test_desktop_release_holders.py`
- ADDED `tests/nastech_cli/test_file_cache_same_tick_rewrite.py`
- ADDED `tests/nastech_cli/test_installed_hub_identifiers.py`
- ADDED `tests/nastech_cli/test_launch_relaunch_loop.py`
- MODIFIED `tests/nastech_cli/test_model_catalog.py`
- MODIFIED `tests/nastech_cli/test_model_picker_usage.py`
- ADDED `tests/nastech_cli/test_nastech_recommendation_mirror.py`
- MODIFIED `tests/nastech_cli/test_peer_cmd.py`
- MODIFIED `tests/nastech_cli/test_process_identity.py`
- MODIFIED `tests/nastech_cli/test_safe_mode.py`
- MODIFIED `tests/nastech_cli/test_shared_metrics_exit_flush.py`
- ADDED `tests/nastech_cli/test_source_check_refused_token.py`
- ADDED `tests/nastech_cli/test_spa_static_asset_misses.py`
- ADDED `tests/nastech_cli/test_status_probe_off_loop.py`
- ADDED `tests/nastech_cli/test_ui_preferences.py`
- ADDED `tests/nastech_cli/test_update_custody_tree.py`
- MODIFIED `tests/nastech_cli/test_update_launch_completion.py`
- ADDED `tests/nastech_cli/test_update_proxy_env.py`
- ADDED `tests/nastech_cli/test_update_release_tag_fetch.py`
- ADDED `tests/nastech_cli/test_update_stage_relay.py`
- MODIFIED `tests/nastech_cli/test_web_server_files.py`
- ADDED `tests/nastech_cli/test_webapp_desktop_plugins.py`
- MODIFIED `tests/nastech_cli/test_webapp_renderer_build.py`
- ADDED `tests/nastech_state/test_compacted_tool_result_paints_once.py`
- ADDED `tests/nastech_state/test_compaction_carried_tail_not_cloned.py`
- ADDED `tests/nastech_state/test_list_sessions_recency.py`
- ADDED `tests/nastech_state/test_local_lineage_cache.py`
- ADDED `tests/nastech_state/test_session_list_page_cost.py`
- ADDED `tests/plugins/dashboard_auth/test_basic_secret_shell_text.py`
- ADDED `tests/pm/test_held_identical_entry_windows_live.py`
- MODIFIED `tests/pm/test_install_states_gc.py`
- ADDED `tests/pm/test_publish_entry.py`
- MODIFIED `tests/providers/test_profile_miss_ttl.py`
- ADDED `tests/scripts/desktop_update/test_desktop_update_marker_gnu_date.py`
- MODIFIED `tests/scripts/desktop_update/test_desktop_update_posix_marker.py`
- ADDED `tests/scripts/desktop_update/test_desktop_update_posix_marker_locale.py`
- ADDED `tests/scripts/desktop_update/test_desktop_update_relaunch_proxy_env.py`
- ADDED `tests/scripts/desktop_update/test_desktop_update_windows_child_stage.py`
- ADDED `tests/scripts/desktop_update/test_desktop_update_windows_log_concurrency.py`
- ADDED `tests/scripts/desktop_update/test_desktop_update_windows_log_exit_flush.py`
- ADDED `tests/scripts/desktop_update/test_desktop_update_windows_relaunch_cwd.py`
- ADDED `tests/scripts/desktop_update/test_desktop_update_windows_release_holders.py`
- MODIFIED `tests/scripts/desktop_update/windows_handoff_support.py`
- MODIFIED `tests/scripts/test_agent_build.py`
- MODIFIED `tests/tools/test_bot_mode_dm.py`
- ADDED `tests/tools/test_bot_mode_nastech_handle.py`
- MODIFIED `tests/tools/test_connectors_catalog.py`
- ADDED `tests/tools/test_url_safety_authority.py`
- ADDED `tests/tools/test_url_safety_authority_floor.py`
- MODIFIED `tests/tui_gateway/test_fallback_chain_hot_reload.py`
- ADDED `tests/tui_gateway/test_stream_segment_identity.py`
- MODIFIED `tools/bot_mode_dm.py`
- MODIFIED `tools/bot_mode_probe.py`
- MODIFIED `tools/connectors/catalog.py`
- MODIFIED `tools/connectors/catalog_tool.py`
- MODIFIED `tools/mcp_oauth_manager.py`
- MODIFIED `tools/skills_hub.py`
- MODIFIED `tools/skills_hub_clawhub.py`
- MODIFIED `tools/url_safety.py`
- MODIFIED `tui_gateway/contracts/canonical_sessions.py`
- MODIFIED `tui_gateway/contracts/common.py`
- MODIFIED `tui_gateway/contracts/events.py`
- MODIFIED `tui_gateway/methods_bot_relay.py`
- MODIFIED `tui_gateway/methods_onboarding.py`
- MODIFIED `tui_gateway/prompt_turn.py`
- MODIFIED `tui_gateway/server.py`
- ADDED `tui_gateway/stream_segments.py`
- MODIFIED `ui-tui/src/__tests__/canonicalSessionControls.test.ts`
- MODIFIED `ui-tui/src/app/slash/canonicalSessionControls.ts`
- MODIFIED `ui-tui/src/lib/usageLimit.test.ts`
- MODIFIED `utils.py`
- ADDED `web/src/contexts/PageHeaderProvider.test.tsx`
- MODIFIED `web/src/contexts/PageHeaderProvider.tsx`
- MODIFIED `web/src/contexts/usePageHeader.ts`
- ADDED `web/src/lib/skill-hub-installed.test.ts`
- ADDED `web/src/lib/skill-hub-installed.ts`
- MODIFIED `web/src/pages/ChatPage.tsx`
- MODIFIED `web/src/pages/FilesPage.tsx`
- MODIFIED `web/src/pages/PluginsPage.tsx`
- MODIFIED `web/src/pages/SessionsPage.test.tsx`
- MODIFIED `web/src/pages/SessionsPage.tsx`
- MODIFIED `web/src/pages/SkillsPage.tsx`
- MODIFIED `website/docs/developer-guide/config-backend.md`
- MODIFIED `website/docs/getting-started/nix-setup.md`
- MODIFIED `website/docs/reference/environment-variables.md`
- MODIFIED `website/docs/reference/package-management.md`
- MODIFIED `website/docs/user-guide/desktop.md`
- MODIFIED `website/docs/user-guide/features/web-dashboard.md`
- MODIFIED `website/docs/user-guide/git-worktrees.md`

## Scan

21651 files scanned [audio=5, binary=7, doc=4, font=13, image=165, text=21457]


## Diff

3498 renamed, 0 rewritten, 17424 identical, 158 locked, 0 missing, 20 owned, 501 reconciled


## Fork check (vs nastech-agent)

- 21015 identical, 458 updated (+0/-0 lines), 178 added, 0 missing, 0 fork-local-unpreserved, 0 stale-upstream, 0 registry-retired owned assets, 0 locked/binary, 0 collision-safe relocated, 50 preserved fork-local files, 0 violations

- features: fork 56 -> branded 56

Auto-generated by 100Ways.
