# Nastech Update Report #1

- upstream sha : `11a75355a4c5540154597c7ea23cbc2a933539f5`
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

- total measured: 653.79 s
- profile: `100ways.stage-profile.v1`

| stage | status | duration | share |
|-------|--------|----------|-------|
| brand | ok | 206.33 s | 31.6% |
| verify | ok | 189.13 s | 28.9% |
| compare | ok | 189.01 s | 28.9% |
| pull | ok | 50.30 s | 7.7% |
| reconcile | ok | 9.31 s | 1.4% |
| forkcheck | ok | 4.85 s | 0.7% |
| summary | ok | 2.64 s | 0.4% |
| preserve | ok | 1.65 s | 0.3% |
| scan | ok | 0.48 s | 0.1% |
| source-evidence | ok | 0.05 s | 0.0% |
| census | ok | 0.03 s | 0.0% |
| plan | ok | 0.00 s | 0.0% |
| report | pending | 0.00 s | 0.0% |
| package | pending | 0.00 s | 0.0% |
| manifest | pending | 0.00 s | 0.0% |
| record | ok | 0.00 s | 0.0% |
| notify | ok | 0.00 s | 0.0% |
| gate | ok | 0.00 s | 0.0% |
| release | ok | 0.00 s | 0.0% |

Slowest: brand 206.3s, verify 189.1s, compare 189.0s.

## Brand

- total files : 21423
- renamed     : 3614 (folders and file names)
- text-rewritten : 21238
- locked-copied  : 157
- binary-copied  : 8
- owned assets   : 22 (our logo/banner/mascot override upstream)

## Reconcile

- fixed : 544 files reconciled: .env.example, .github/scripts/run-workspace-checks.mjs, .github/workflows/deploy-site.yml, .github/workflows/deploy-site.yml, .github/workflows/desktop-bundle-smoke.yml, .github/workflows/desktop-bundled-release.yml, .github/workflows/desktop-bundled-release.yml, .github/workflows/desktop-bundled-release.yml, .github/workflows/desktop-bundled-release.yml, .github/workflows/docs-search-monitor.yml, .github/workflows/install-e2e-macos-run.yml, .github/workflows/install-e2e-windows-run.yml, .github/workflows/js-tests.yml, .github/workflows/plugin-catalog-ci.yml, .github/workflows/skills-index-freshness.yml, .github/workflows/stable-release.yml, .github/workflows/tests-os.yml, .github/workflows/tests.yml, .github/workflows/tests.yml, .github/workflows/windows-install-update-e2e.yml, .mailmap, AGENTS.md, AGENTS.md, CONTRIBUTING.es.md, CONTRIBUTING.md, Dockerfile, README.es.md, README.md, README.ur-pk.md, README.zh-CN.md, SECURITY.es.md, SECURITY.es.md, SECURITY.md, SECURITY.md, agent/AGENTS.md, agent/agent_runtime_helpers.py, agent/anthropic_adapter.py, agent/anthropic_endpoints.py, agent/auxiliary_client.py, agent/auxiliary_client.py, agent/billing_links.py, agent/billing_view.py, agent/chat_completion_helpers.py, agent/conversation_compression.py, agent/conversation_loop.py, agent/error_classifier.py, agent/message_sanitization.py, agent/model_metadata.py, agent/onboarding_first_tasks.py, agent/prompt_builder.py, agent/proxy_sources/iron_proxy.py, agent/rate_limit_credits.py, agent/reasoning_params.py, agent/subscription_view.py, agent/turn_recovery.py, agent/usage_pricing.py, agent/usage_pricing.py, apps/bootstrap-installer/src-tauri/Cargo.toml, apps/desktop/README.md, apps/desktop/electron-builder.config.cjs, apps/desktop/electron/backend-health.test.ts, apps/desktop/electron/backend-health.ts, apps/desktop/electron/challenge-window.test.ts, apps/desktop/electron/cloud-session-recovery.test.ts, apps/desktop/electron/connection-config.test.ts, apps/desktop/electron/data-paths.test.ts, apps/desktop/electron/hub-iframe-policy.ts, apps/desktop/electron/oauth-partition.test.ts, apps/desktop/electron/portal-session.ts, apps/desktop/electron/remote-lifecycle.ts, apps/desktop/electron/remote-oauth-ticket.test.ts, apps/desktop/electron/updater/checkout-source.test.ts, apps/desktop/electron/window-open-policy.test.ts, apps/desktop/scripts/bundle-env.test.mjs, apps/desktop/src/app/chat/sidebar/section-states.tsx, apps/desktop/src/app/messaging/index.test.tsx, apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx, apps/desktop/src/app/settings/billing/api.test.ts, apps/desktop/src/app/settings/billing/dev-fixtures.ts, apps/desktop/src/app/settings/billing/errors.test.ts, apps/desktop/src/app/settings/billing/keep-going-on-credits-row.test.tsx, apps/desktop/src/app/settings/billing/use-billing-state.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.ts, apps/desktop/src/app/settings/billing/use-charge-poller.test.ts, apps/desktop/src/app/settings/billing/use-step-up.test.tsx, apps/desktop/src/app/settings/constants.ts, apps/desktop/src/app/settings/gateway-settings.test.tsx, apps/desktop/src/app/settings/gateway-settings.tsx, apps/desktop/src/app/settings/toolset-config-panel.test.tsx, apps/desktop/src/app/shell/terms-butterbar.tsx, apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts, apps/desktop/src/components/boot-failure-overlay.test.tsx, apps/desktop/src/components/boot-failure-overlay.tsx, apps/desktop/src/components/send-diagnostics-dialog.tsx, apps/desktop/src/components/update-status.tsx, apps/desktop/src/contrib/plugin.ts, apps/desktop/src/i18n/de.ts, apps/desktop/src/i18n/en.ts, apps/desktop/src/i18n/es.ts, apps/desktop/src/i18n/fr.ts, apps/desktop/src/i18n/ja.ts, apps/desktop/src/i18n/ru.ts, apps/desktop/src/i18n/zh-hant_settings.ts, apps/desktop/src/i18n/zh.ts, apps/desktop/src/lib/docs.ts, apps/desktop/src/lib/plugin-catalog.ts, apps/desktop/src/plugins/nastech-bots/skills-hub-picker.test.tsx, apps/desktop/src/plugins/nastech-bots/skills-hub.tsx, apps/desktop/src/sdk/index.ts, apps/desktop/src/store/free-tier-challenge.test.ts, apps/desktop/src/store/notifications.ts, apps/desktop/src/store/shared-metrics.ts, apps/desktop/src/themes/use-skin-command.ts, cli-config.yaml.example, cron/AGENTS.md, eslint.config.shared.mjs, evals/auth_pool_controls.py, evals/browser_use/single_run.py, evals/postmortem/live_ab/auth_stampede.py, evals/postmortem/live_ab/cache_concurrency_probe.py, evals/postmortem/review_probes/cache_estimator_probe.py, evals/postmortem/review_probes/credential_identity_probe.py, evals/reasoning_replay/harness.py, gateway/AGENTS.md, locales/_keys.desktop.json, locales/_keys.tui.json, nastech_cli/AGENTS.md, nastech_cli/anon_auth.py, nastech_cli/anon_auth.py, nastech_cli/anon_sign_in.py, nastech_cli/auth.py, nastech_cli/auth_codex.py, nastech_cli/auth_constants.py, nastech_cli/auth_constants.py, nastech_cli/auth_error_copy.py, nastech_cli/auth_nastech.py, nastech_cli/banner.py, nastech_cli/config_defaults.py, nastech_cli/dashboard_auth/login_page.py, nastech_cli/dashboard_register.py, nastech_cli/dashboard_register.py, nastech_cli/debug.py, nastech_cli/diagnostics_upload.py, nastech_cli/fallback_cmd.py, nastech_cli/gateway_chat_commands.py, nastech_cli/kanban_parser.py, nastech_cli/main.py, nastech_cli/main_dashboard.py, nastech_cli/main_desktop.py, nastech_cli/model_catalog.py, nastech_cli/model_setup_flows_common.py, nastech_cli/models.py, nastech_cli/models_pricing.py, nastech_cli/models_pricing.py, nastech_cli/nastech_account.py, nastech_cli/nastech_account.py, nastech_cli/nastech_billing.py, nastech_cli/nastech_billing.py, nastech_cli/observability/shared_metrics_consent.py, nastech_cli/observability/shared_metrics_send_config.py, nastech_cli/observability/shared_metrics_send_config.py, nastech_cli/plugin_catalog.py, nastech_cli/plugins_cmd.py, nastech_cli/portal_cli.py, nastech_cli/portal_cli.py, nastech_cli/providers.py, nastech_cli/proxy/adapters/base.py, nastech_cli/proxy/adapters/nastech_portal.py, nastech_cli/release_channels.py, nastech_cli/setup.py, nastech_cli/setup_platforms.py, nastech_cli/setup_quick.py, nastech_cli/skin_engine.py, nastech_cli/source_releases.py, nastech_cli/steward.py, nastech_cli/subcommands/egress.py, nastech_cli/subcommands/fallback.py, nastech_cli/subcommands/secrets.py, nastech_cli/subcommands/worktree.py, nastech_cli/telegram_managed_bot.py, nastech_cli/telegram_managed_bot.py, nastech_cli/tools_config.py, nastech_cli/uninstall.py, nastech_cli/update_cmd.py, nastech_cli/update_cmd_git.py, nastech_cli/update_cmd_git.py, nastech_cli/update_cmd_maint.py, nastech_cli/update_cmd_zip.py, nastech_cli/update_downgrade_guard.py, nastech_cli/web_routers/status.py, nastech_cli/web_server_messaging.py, nastech_cli/web_server_messaging.py, nastech_cli/web_server_oauth.py, nastech_constants.py, nastech_state_common.py, nastech_state_errors.py, nastech_state_reconcile.py, optional-skills/creative/pretext/templates/donut-orbit.html, optional-skills/productivity/memento-flashcards/SKILL.md, package-lock.json, plugin-catalog/README.md, plugins/AGENTS.md, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/plugin.yaml, plugins/kanban/dashboard/dist/index.js, plugins/kanban/systemd/nastech-kanban-dispatcher.service, plugins/model-providers/ai-gateway/__init__.py, plugins/model-providers/fireworks/__init__.py, plugins/model-providers/kimi-coding/__init__.py, plugins/model-providers/nastech/__init__.py, plugins/model-providers/opencode-zen/__init__.py, plugins/model-providers/solstice/auth.py, plugins/model-providers/solstice/auth.py, plugins/nastech-achievements/dashboard/dist/index.js, plugins/platforms/discord/adapter.py, plugins/platforms/discord/onboarding.py, plugins/platforms/email/adapter.py, plugins/platforms/google_chat/adapter.py, plugins/platforms/irc/adapter.py, plugins/platforms/line/adapter.py, plugins/platforms/ntfy/adapter.py, plugins/platforms/photon/adapter.py, plugins/platforms/photon/sidecar/package-lock.json, plugins/platforms/raft/adapter.py, plugins/platforms/simplex/adapter.py, plugins/platforms/slack/adapter.py, plugins/platforms/teams/adapter.py, plugins/platforms/weixin/adapter.py, plugins/platforms/whatsapp_cloud/adapter.py, plugins/platforms/whatsapp_cloud/setup_wizard.py, plugins/web/perplexity/provider.py, pm/artifact-mirror.json, pm/network.py, pm/uv.lock, scripts/build_model_catalog.py, scripts/ci/check_catalog_cors.py, scripts/contributor_audit.py, scripts/e2e_shared_metrics_staging.py, scripts/install.cmd, scripts/install.ps1, scripts/install.sh, scripts/release.py, scripts/release.py, scripts/releases/authors_legacy.py, scripts/releases/entrypoint.py, scripts/releases/lanes.py, scripts/releases/pick_tags.py, scripts/releases/r2.py, scripts/sandbox/generate-e2e-matrix.mjs, scripts/sandbox/pick-release-tags.sh, scripts/termux/stage_apt_repo.py, scripts/tests/test-install-ps1-store-guard.ps1, scripts/whatsapp-bridge/package-lock.json, setup.py, skills/AGENTS.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/references/background-systems.md, skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md, skills/autonomous-ai-agents/nastech-agent/references/configuration.md, skills/autonomous-ai-agents/nastech-agent/references/contributor-guide.md, skills/autonomous-ai-agents/nastech-agent/references/portal-auth-for-third-party-apps.md, skills/autonomous-ai-agents/nastech-agent/references/providers-and-models.md, skills/autonomous-ai-agents/nastech-agent/references/webhooks.md, skills/media/youtube-content/SKILL.md, skills/software-development/python-debugpy/SKILL.md, tests-js/bundle-smoke-metadata.test.mjs, tests-js/update-ui.test.mjs, tests/agent/test_anthropic_adapter.py, tests/agent/test_anthropic_preserved_thinking_replay.py, tests/agent/test_anthropic_prompt_cache_policy.py, tests/agent/test_auxiliary_auth_rung_fallthrough.py, tests/agent/test_auxiliary_client.py, tests/agent/test_auxiliary_client_nastech_401_cache_key.py, tests/agent/test_auxiliary_main_first.py, tests/agent/test_auxiliary_transport_autodetect.py, tests/agent/test_billing_links.py, tests/agent/test_credential_pool.py, tests/agent/test_credential_pool_nastech_refresh_stampede.py, tests/agent/test_credits_cold_start.py, tests/agent/test_credits_policy.py, tests/agent/test_credits_usage_window.py, tests/agent/test_deepseek_anthropic_thinking.py, tests/agent/test_error_classifier.py, tests/agent/test_error_classifier_observed.py, tests/agent/test_fast_mode_auto.py, tests/agent/test_free_tier_rate_limit_class.py, tests/agent/test_model_metadata.py, tests/agent/test_nastech_credits_gauge.py, tests/agent/test_nastech_key_pre_expiry_adoption.py, tests/agent/test_nastech_portal_anthropic_wire.py, tests/agent/test_nastech_rate_guard.py, tests/agent/test_nastech_welcome_client_contract.py, tests/agent/test_nastech_wire_auto.py, tests/agent/test_nonretryable_result_carries_verdict.py, tests/agent/test_onboarding_first_tasks.py, tests/agent/test_plan_limits.py, tests/agent/test_primary_runtime_restore.py, tests/agent/test_provider_attribution_headers.py, tests/agent/test_provider_fallback.py, tests/agent/test_provider_history_parity.py, tests/agent/test_provider_parity.py, tests/agent/test_reasoning_replay_routes.py, tests/agent/test_run_agent.py, tests/agent/test_run_agent.py, tests/agent/test_switch_model_reapplies_headers.py, tests/agent/test_turn_usage_log_line.py, tests/agent/test_welcome_error_identity.py, tests/agent/test_welcome_tier_recovery.py, tests/agent/transports/test_chat_completions.py, tests/agent/transports/test_chat_completions_reasoning_details_replay.py, tests/agent/transports/test_provider_wire_snapshot.py, tests/ci/test_stable_release_graph.py, tests/compat/old_updater_dependencies.py, tests/conftest.py, tests/conftest.py, tests/docker/test_sqlite_runtime.py, tests/e2e/core/live/_helpers.py, tests/e2e/core/providers/test_catalog_oauth.py, tests/e2e/core/providers/test_chat_reasoning_variants.py, tests/e2e/core/providers/test_fallback_providers.py, tests/e2e/core/upgrade/network/_seed.py, tests/e2e/core/windows/test_boot_lifecycle.py, tests/e2e/core/windows_update/_machine.py, tests/fakes/providers/chat_variants.py, tests/fakes/providers/vertex.py, tests/fixtures/prompt_surface/prompts/cli-code.claude.txt, tests/fixtures/prompt_surface/prompts/cli-code.claude.txt, tests/fixtures/prompt_surface/prompts/cli.claude.txt, tests/fixtures/prompt_surface/prompts/cli.claude.txt, tests/fixtures/prompt_surface/prompts/cli.gemini.txt, tests/fixtures/prompt_surface/prompts/cli.gemini.txt, tests/fixtures/prompt_surface/prompts/cli.gpt.txt, tests/fixtures/prompt_surface/prompts/cli.gpt.txt, tests/fixtures/prompt_surface/prompts/cli.nastech.txt, tests/fixtures/prompt_surface/prompts/cli.nastech.txt, tests/fixtures/prompt_surface/prompts/cron.claude.txt, tests/fixtures/prompt_surface/prompts/cron.claude.txt, tests/fixtures/prompt_surface/prompts/desktop.claude.txt, tests/fixtures/prompt_surface/prompts/desktop.claude.txt, tests/fixtures/prompt_surface/prompts/discord.claude.txt, tests/fixtures/prompt_surface/prompts/discord.claude.txt, tests/fixtures/prompt_surface/prompts/telegram.claude.txt, tests/fixtures/prompt_surface/prompts/telegram.claude.txt, tests/fixtures/prompt_surface/surfaces.json, tests/fixtures/prompt_surface/tools/tool_search.desktop.claude.json, tests/fixtures/provider_wire_snapshot.json, tests/gateway/fixtures/local_recovery_probe.py, tests/gateway/test_discord_format.py, tests/gateway/test_housekeeping_profile_scope.py, tests/gateway/test_internal_event_pin_wiring.py, tests/gateway/test_journey_compress_restart_fifo.py, tests/gateway/test_model_switch_persistence.py, tests/gateway/test_run_progress_topics.py, tests/gateway/test_session_model_override_persistence.py, tests/gateway/test_startup_warmup_profile_scope.py, tests/gateway/test_status_command.py, tests/gateway/test_telegram_mention_context.py, tests/gateway/test_usage_command.py, tests/install/macos-desktop-e2e.sh, tests/install/windows-e2e.ps1, tests/nastech_cli/anon_portal.py, tests/nastech_cli/test_anon_auth_core.py, tests/nastech_cli/test_anon_failure_modes.py, tests/nastech_cli/test_anon_failure_modes.py, tests/nastech_cli/test_anon_picker.py, tests/nastech_cli/test_anon_sign_in_flow.py, tests/nastech_cli/test_anon_surfaces.py, tests/nastech_cli/test_anon_upgrade.py, tests/nastech_cli/test_auth_nastech_provider.py, tests/nastech_cli/test_base_url_host_identity.py, tests/nastech_cli/test_browse_schema_drift.py, tests/nastech_cli/test_cli_first_run_setup.py, tests/nastech_cli/test_cli_goal_parked_resume.py, tests/nastech_cli/test_cli_init.py, tests/nastech_cli/test_cli_provider_resolution.py, tests/nastech_cli/test_dashboard_register.py, tests/nastech_cli/test_fireworks_provider.py, tests/nastech_cli/test_gateway_chat_native.py, tests/nastech_cli/test_guest_handoff.py, tests/nastech_cli/test_local_abandoned_requests.py, tests/nastech_cli/test_local_quickstart.py, tests/nastech_cli/test_local_runtime_processes.py, tests/nastech_cli/test_main_merge_lifecycle.py, tests/nastech_cli/test_model_catalog.py, tests/nastech_cli/test_model_picker_usage.py, tests/nastech_cli/test_model_validation.py, tests/nastech_cli/test_nastech_anthropic_wire_default.py, tests/nastech_cli/test_nastech_auth_keepalive.py, tests/nastech_cli/test_nastech_auth_status_cache.py, tests/nastech_cli/test_nastech_inference_url_validation.py, tests/nastech_cli/test_nastech_nonproduction_inference_host.py, tests/nastech_cli/test_nastech_nonproduction_inference_host.py, tests/nastech_cli/test_nastech_portal_staging_allowlist.py, tests/nastech_cli/test_nastech_reasoning_metadata.py, tests/nastech_cli/test_proxy.py, tests/nastech_cli/test_reasoning_caps_disk_cache.py, tests/nastech_cli/test_release_channels.py, tests/nastech_cli/test_sale_pricing.py, tests/nastech_cli/test_show_config_credential.py, tests/nastech_cli/test_source_channel_integration.py, tests/nastech_cli/test_source_check.py, tests/nastech_cli/test_taskkill_identity_windows_live.py, tests/nastech_cli/test_update_channel_release_hold.py, tests/nastech_cli/test_update_fetch_failure_classifier.py, tests/nastech_cli/test_update_target_identity.py, tests/nastech_cli/test_web_oauth_dispatch.py, tests/plugins/dashboard_auth/test_nastech_provider.py, tests/plugins/image_gen/check_parity_vs_main.py, tests/plugins/image_gen/test_openrouter_compat_provider.py, tests/plugins/test_chronos_verify.py, tests/scripts/desktop_update/test_desktop_update_windows_commit_outcome.py, tests/scripts/desktop_update/test_desktop_update_windows_marker.py, tests/scripts/desktop_update/test_desktop_update_windows_marker_lock.py, tests/scripts/test_release_build_commit.py, tests/scripts/test_release_canary_git.py, tests/scripts/test_release_channels.py, tests/scripts/test_release_entrypoint.py, tests/scripts/test_release_lanes.py, tests/scripts/test_release_r2.py, tests/scripts/test_release_r2.py, tests/scripts/test_stable_release.py, tests/scripts/test_stage_apt_repo.py, tests/scripts/test_upload_summary.py, tests/test_live_nastech_services_fence.py, tests/test_session_daemon_reaper.py, tests/tools/test_connector_wire_identity.py, tests/tools/test_delegate.py, tests/tools/test_managed_media_gateways.py, tests/tools/test_managed_tool_gateway.py, tests/tools/test_plugin_guard.py, tests/tools/test_stage2_hook_nastech_routing_env.py, tests/tools/test_strict_provider_selection.py, tests/tools/test_tts_openai_config.py, tests/tools/test_url_safety.py, tests/tools/test_web_tools_config.py, tests/tools/test_web_tools_perplexity.py, tests/tui_gateway/test_compute_host.py, tests/tui_gateway/test_legacy_fallback_ticket_profile_verbs.py, tests/tui_gateway/test_resume_switched_provider_endpoint.py, tests/website/test_extract_skills.py, tools/AGENTS.md, tools/managed_gateway_auth.py, tools/managed_gateway_identity.py, tools/managed_tool_gateway.py, tools/mcp_oauth.py, tools/plugin_guard_context.py, tools/set_theme_tool.py, tools/skills_hub_search.py, trajectory_compressor.py, ui-tui/scripts/billing-fixtures.tsx, ui-tui/src/__tests__/canonicalDetachClose.test.tsx, ui-tui/src/__tests__/canonicalDetachOrdering.test.tsx, ui-tui/src/__tests__/canonicalSwitcherClose.test.tsx, ui-tui/src/__tests__/inkResumeSnapshotFence.test.tsx, ui-tui/src/__tests__/resumeEpochRenderer.test.tsx, ui-tui/src/__tests__/subscriptionCommand.test.ts, ui-tui/src/__tests__/subscriptionOverlay.test.tsx, ui-tui/src/app/slash/commands/subscription.ts, ui-tui/src/app/useSessionLifecycle.ts, ui-tui/src/domain/paths.ts, uv.lock, web/src/components/SharedMetricsConsentBanner.tsx, web/src/components/SidebarFooter.tsx, web/src/pages/DocsPage.tsx, web/src/pages/PluginsPage.tsx, web/src/pages/SystemPage.tsx, website/README.md, website/docs/developer-guide/egress-internals.md, website/docs/developer-guide/stable-releases.md, website/docs/getting-started/installation.md, website/docs/getting-started/platform-support.md, website/docs/getting-started/quickstart.md, website/docs/getting-started/termux.md, website/docs/getting-started/termux.md, website/docs/getting-started/updating.md, website/docs/guides/manage-nastech-cloud-with-mcp.md, website/docs/guides/run-nastech-with-nastech-portal.md, website/docs/guides/run-nemotron-3-ultra-free.md, website/docs/index.mdx, website/docs/integrations/nastech-portal.md, website/docs/integrations/providers.md, website/docs/reference/cli-commands.md, website/docs/reference/environment-variables.md, website/docs/reference/faq.md, website/docs/reference/model-catalog.md, website/docs/reference/skills-catalog.md, website/docs/user-guide/desktop.md, website/docs/user-guide/egress/iron-proxy.md, website/docs/user-guide/features/browser.md, website/docs/user-guide/features/image-generation.md, website/docs/user-guide/features/plugin-catalog.md, website/docs/user-guide/features/skills.md, website/docs/user-guide/features/subscription-proxy.md, website/docs/user-guide/features/tool-gateway.md, website/docs/user-guide/features/tools.md, website/docs/user-guide/features/tts.md, website/docs/user-guide/features/web-dashboard.md, website/docs/user-guide/features/web-search.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/skills/bundled/media/media-youtube-content.md, website/docs/user-guide/skills/bundled/software-development/software-development-python-debugpy.md, website/docs/user-guide/skills/optional/productivity/productivity-memento-flashcards.md, website/docs/user-guide/windows-native.md, website/docs/user-guide/windows-wsl-quickstart.md, website/docusaurus.config.ts, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/plugins/index.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/quickstart.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-nastech-with-nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/index.mdx, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/providers.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/faq.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/model-catalog.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/subscription-proxy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tools.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tts.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/media/media-youtube-content.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/software-development/software-development-python-debugpy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/optional/productivity/productivity-memento-flashcards.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-native.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-wsl-quickstart.md, website/scripts/check-live-search.mjs, website/scripts/check-live-search.mjs, website/scripts/extract-skills.py, website/scripts/fetch-plugin-stars.py, website/scripts/generate-llms-txt.py, website/scripts/prebuild.mjs, website/src/pages/plugins/index.tsx, website/src/pages/skills/index.tsx, website/static/api/model-catalog.json, website/static/oauth/client-metadata.json


## Direct upstream tree delta

- complete: +43 ~215 -0 ↪0
- MODIFIED `.dockerignore`
- MODIFIED `Dockerfile`
- MODIFIED `agent/deadline.py`
- MODIFIED `agent/model_metadata.py`
- MODIFIED `agent/outbound_webhooks.py`
- ADDED `apps/desktop/e2e/sticky-prompt-clip.spec.ts`
- MODIFIED `apps/desktop/electron/main.ts`
- MODIFIED `apps/desktop/electron/translucency.test.ts`
- MODIFIED `apps/desktop/electron/translucency.ts`
- MODIFIED `apps/desktop/eslint.config.mjs`
- MODIFIED `apps/desktop/src/api/canonical-protocol.test.ts`
- MODIFIED `apps/desktop/src/api/canonical-protocol.ts`
- ADDED `apps/desktop/src/app/chat/composer/composer-store-writer.test.ts`
- ADDED `apps/desktop/src/app/chat/composer/composer-store-writer.ts`
- ADDED `apps/desktop/src/app/chat/composer/hooks/use-composer-draft.persist-window.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/hooks/use-composer-draft.ts`
- MODIFIED `apps/desktop/src/app/chat/composer/hooks/use-composer-queue.ts`
- ADDED `apps/desktop/src/app/chat/composer/hooks/use-composer-submit.accept-clear.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/hooks/use-composer-submit.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/hooks/use-composer-submit.ts`
- MODIFIED `apps/desktop/src/app/chat/composer/index.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/status-stack/session-control-goal.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/profile-dropdown-switcher.tsx`
- ADDED `apps/desktop/src/app/chat/sidebar/profile-menu-unserved.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/profile-switcher.tsx`
- ADDED `apps/desktop/src/app/chat/sidebar/unserved-profiles.tsx`
- MODIFIED `apps/desktop/src/app/context-menu/app-context-menu.test.tsx`
- MODIFIED `apps/desktop/src/app/context-menu/app-context-menu.tsx`
- MODIFIED `apps/desktop/src/app/context-menu/composer-menu.test.tsx`
- MODIFIED `apps/desktop/src/app/gateway/hooks/use-gateway-boot-webapp-profile.test.tsx`
- MODIFIED `apps/desktop/src/app/gateway/hooks/use-gateway-boot.ts`
- MODIFIED `apps/desktop/src/app/gateway/report-startup-latency.ts`
- MODIFIED `apps/desktop/src/app/profiles/create-profile-dialog.test.tsx`
- MODIFIED `apps/desktop/src/app/profiles/create-profile-dialog.tsx`
- MODIFIED `apps/desktop/src/app/right-sidebar/terminal/terminals.ts`
- ADDED `apps/desktop/src/app/session/hooks/browser-profile-folder.test.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/index.sleep-wake.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/index.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/prepared-submission-windows.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/prepared-submissions-spent.test.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-prompt-actions/prepared-submissions-tabs.test.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-prompt-actions/prepared-submissions-test-utils.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/prepared-submissions.test.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/prepared-submissions.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/slash.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/submission-destination.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/submit-unknown-receipt.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/submit-voice-stopped.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/submit.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-actions/index.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-actions/restore-pending-clarify.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-actions/runtime-owner.ts`
- MODIFIED `apps/desktop/src/app/settings/billing/api.ts`
- MODIFIED `apps/desktop/src/app/settings/sessions-settings.tsx`
- ADDED `apps/desktop/src/components/assistant-ui/thread/sticky-prompt-clip-registration.test.ts`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/use-sticky-prompt-clip.ts`
- ADDED `apps/desktop/src/components/assistant-ui/thread/user-message-touch-clamp.test.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/user-message.tsx`
- MODIFIED `apps/desktop/src/components/chat/generated-image-open.test.tsx`
- MODIFIED `apps/desktop/src/components/chat/generated-image-result.tsx`
- MODIFIED `apps/desktop/src/components/desktop-install-overlay.tsx`
- MODIFIED `apps/desktop/src/contrib/radio-plugin.test.ts`
- MODIFIED `apps/desktop/src/global.d.ts`
- MODIFIED `apps/desktop/src/i18n/ar_command_center.ts`
- MODIFIED `apps/desktop/src/i18n/de.ts`
- MODIFIED `apps/desktop/src/i18n/en.ts`
- MODIFIED `apps/desktop/src/i18n/es.ts`
- MODIFIED `apps/desktop/src/i18n/fr.ts`
- MODIFIED `apps/desktop/src/i18n/ja.ts`
- MODIFIED `apps/desktop/src/i18n/ru.ts`
- MODIFIED `apps/desktop/src/i18n/types.ts`
- MODIFIED `apps/desktop/src/i18n/zh-hant_command_center.ts`
- MODIFIED `apps/desktop/src/i18n/zh.ts`
- MODIFIED `apps/desktop/src/lib/browser-bridge-stubs.ts`
- MODIFIED `apps/desktop/src/lib/browser-clipboard.ts`
- MODIFIED `apps/desktop/src/lib/browser-connection.ts`
- ADDED `apps/desktop/src/lib/browser-desktop-bridge-served-profiles.test.ts`
- MODIFIED `apps/desktop/src/lib/browser-desktop-bridge.test.ts`
- MODIFIED `apps/desktop/src/lib/browser-desktop-bridge.ts`
- ADDED `apps/desktop/src/lib/browser-profile-prefs.test.ts`
- ADDED `apps/desktop/src/lib/browser-profile-prefs.ts`
- MODIFIED `apps/desktop/src/lib/browser-profile.test.ts`
- MODIFIED `apps/desktop/src/lib/browser-profile.ts`
- ADDED `apps/desktop/src/lib/browser-served-profiles.test.ts`
- ADDED `apps/desktop/src/lib/browser-served-profiles.ts`
- MODIFIED `apps/desktop/src/lib/browser-settings.ts`
- MODIFIED `apps/desktop/src/lib/browser-staged-attachments.test.ts`
- ADDED `apps/desktop/src/lib/browser-startup-profile.ts`
- MODIFIED `apps/desktop/src/lib/browser-uploads.ts`
- ADDED `apps/desktop/src/lib/browser-window.test.ts`
- MODIFIED `apps/desktop/src/lib/browser-window.ts`
- MODIFIED `apps/desktop/src/lib/clipboard.test.ts`
- MODIFIED `apps/desktop/src/lib/clipboard.ts`
- MODIFIED `apps/desktop/src/lib/media.remote.test.ts`
- MODIFIED `apps/desktop/src/lib/media.ts`
- MODIFIED `apps/desktop/src/lib/platform.ts`
- MODIFIED `apps/desktop/src/lib/preview-annotate/handoff.ts`
- MODIFIED `apps/desktop/src/lib/svg-image.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/canonical-group-attachments.test.tsx`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/canonical-group-attachments.tsx`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/canonical-group-history.test.tsx`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/canonical-group-send.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/canonical-group-workspace.tsx`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/canonical-groups.test.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/canonical-groups.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/create-agent-lazy-profile.test.tsx`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/create-dialog.tsx`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/data.roster.test.tsx`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/data.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/group-chat.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/group-test-utils.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/group-turns.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/profile-ops.test.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/profile-ops.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/types.ts`
- MODIFIED `apps/desktop/src/plugins/kanban/drawer.tsx`
- MODIFIED `apps/desktop/src/plugins/radio/plugin.js`
- MODIFIED `apps/desktop/src/sdk/index.ts`
- ADDED `apps/desktop/src/sdk/profile-local.ts`
- ADDED `apps/desktop/src/store/composer-draft-stash.test.ts`
- ADDED `apps/desktop/src/store/composer-draft-stash.ts`
- MODIFIED `apps/desktop/src/store/composer-queue.ts`
- MODIFIED `apps/desktop/src/store/composer.ts`
- MODIFIED `apps/desktop/src/store/default-profile.ts`
- MODIFIED `apps/desktop/src/store/desktop-metrics.ts`
- ADDED `apps/desktop/src/store/gateway-dial-failures.ts`
- MODIFIED `apps/desktop/src/store/gateway.ts`
- MODIFIED `apps/desktop/src/store/onboarding.ts`
- MODIFIED `apps/desktop/src/store/pet-generate.ts`
- MODIFIED `apps/desktop/src/store/preview.ts`
- ADDED `apps/desktop/src/store/profile-launch-native.test.ts`
- ADDED `apps/desktop/src/store/profile-launch-webapp.test.ts`
- ADDED `apps/desktop/src/store/profile-select-webapp-served.test.ts`
- MODIFIED `apps/desktop/src/store/profile-share.test.ts`
- MODIFIED `apps/desktop/src/store/profile-share.ts`
- MODIFIED `apps/desktop/src/store/profile.ts`
- MODIFIED `apps/desktop/src/store/projects.ts`
- MODIFIED `apps/desktop/src/store/session-states.test.ts`
- MODIFIED `apps/desktop/src/store/session-states.ts`
- ADDED `apps/desktop/src/store/session-tile-order.ts`
- MODIFIED `apps/desktop/src/store/session.ts`
- ADDED `apps/desktop/src/store/translucency.linux.test.ts`
- MODIFIED `apps/desktop/src/store/translucency.ts`
- MODIFIED `apps/desktop/src/store/windows.ts`
- MODIFIED `apps/desktop/src/styles.css`
- ADDED `apps/desktop/src/test/webapp-windows.ts`
- MODIFIED `apps/shared/src/index.ts`
- MODIFIED `apps/shared/src/session-http-mutations.ts`
- MODIFIED `apps/shared/src/translucency.ts`
- ADDED `contributors/emails/UE2020@users.noreply.github.com`
- ADDED `contributors/emails/invincibledude12@gmail.com`
- ADDED `contributors/emails/simon@puenteworks.com`
- ADDED `contributors/emails/simongonzalezdc@users.noreply.github.com`
- MODIFIED `cron/delivery_queue.py`
- MODIFIED `cron/jobs.py`
- MODIFIED `gateway/drain_control.py`
- MODIFIED `gateway/host_attach.py`
- MODIFIED `gateway/platforms/base.py`
- MODIFIED `gateway/run_api.py`
- MODIFIED `gateway/run_idle_exit.py`
- MODIFIED `gateway/session_authorities.py`
- MODIFIED `gateway/session_controls.py`
- MODIFIED `nastech_cli/browser_connect.py`
- MODIFIED `nastech_cli/data_cleanup_holders.py`
- MODIFIED `nastech_cli/gateway.py`
- MODIFIED `nastech_cli/gateway_launchd.py`
- MODIFIED `nastech_cli/gateway_migrate.py`
- MODIFIED `nastech_cli/gateway_supervised_restart.py`
- MODIFIED `nastech_cli/gateway_windows.py`
- MODIFIED `nastech_cli/kanban_db.py`
- MODIFIED `nastech_cli/kanban_db_connect.py`
- MODIFIED `nastech_cli/local_runtime/endpoint.py`
- MODIFIED `nastech_cli/models_catalog_static.py`
- MODIFIED `nastech_cli/ssh_workspace_fs.py`
- MODIFIED `nastech_cli/terminal_breadcrumbs.py`
- MODIFIED `nastech_cli/update_cmd_windows.py`
- MODIFIED `nastech_cli/web_host_terminal_sessions.py`
- MODIFIED `nastech_cli/web_server_file_tickets.py`
- MODIFIED `nastech_cli/webapp.py`
- MODIFIED `locales/_keys.desktop.json`
- MODIFIED `optional-skills/security/unbroker/README.md`
- MODIFIED `optional-skills/security/unbroker/SKILL.md`
- MODIFIED `optional-skills/security/unbroker/references/brokers/advancedbackgroundchecks.json`
- MODIFIED `optional-skills/security/unbroker/references/brokers/clustrmaps.json`
- MODIFIED `optional-skills/security/unbroker/references/brokers/cyberbackgroundchecks.json`
- MODIFIED `optional-skills/security/unbroker/references/brokers/fastpeoplesearch.json`
- MODIFIED `optional-skills/security/unbroker/references/brokers/intelius.json`
- MODIFIED `optional-skills/security/unbroker/references/brokers/nuwber.json`
- MODIFIED `optional-skills/security/unbroker/references/brokers/peekyou.json`
- MODIFIED `optional-skills/security/unbroker/references/brokers/peoplefinders.json`
- MODIFIED `optional-skills/security/unbroker/references/brokers/radaris.json`
- MODIFIED `optional-skills/security/unbroker/references/brokers/rehold.json`
- MODIFIED `optional-skills/security/unbroker/references/brokers/searchpeoplefree.json`
- MODIFIED `optional-skills/security/unbroker/references/brokers/spokeo.json`
- MODIFIED `optional-skills/security/unbroker/references/brokers/usphonebook.json`
- MODIFIED `optional-skills/security/unbroker/references/methods.md`
- MODIFIED `optional-skills/security/unbroker/references/state-machine.md`
- MODIFIED `optional-skills/security/unbroker/scripts/autopilot.py`
- MODIFIED `optional-skills/security/unbroker/scripts/dossier.py`
- MODIFIED `optional-skills/security/unbroker/scripts/ledger.py`
- MODIFIED `optional-skills/security/unbroker/scripts/pdd.py`
- MODIFIED `optional-skills/security/unbroker/scripts/registry.py`
- MODIFIED `optional-skills/security/unbroker/scripts/tiers.py`
- ADDED `plugin-catalog/backupdrill.yaml`
- MODIFIED `plugin-catalog/gonogo.yaml`
- ADDED `plugin-catalog/kinocut.yaml`
- MODIFIED `plugin-catalog/llmslim.yaml`
- MODIFIED `plugin-catalog/thomas.yaml`
- ADDED `plugin-catalog/tracekit.yaml`
- MODIFIED `plugins/dashboard_auth/basic/__init__.py`
- MODIFIED `plugins/platforms/a2a/README.md`
- MODIFIED `plugins/platforms/a2a/adapter.py`
- MODIFIED `plugins/platforms/a2a/security.py`
- MODIFIED `pyproject.toml`
- MODIFIED `scripts/build/freshness.mjs`
- MODIFIED `scripts/build/webapp.mjs`
- MODIFIED `scripts/ci/classify_changes.py`
- MODIFIED `tests-js/product-builders.test.mjs`
- ADDED `tests-js/webapp-keep-previous.test.mjs`
- MODIFIED `tests/agent/test_deadline.py`
- MODIFIED `tests/ci/test_classify_changes.py`
- ADDED `tests/docker/test_webapp_bundle.py`
- MODIFIED `tests/gateway/test_canonical_file_attach_staged_sources.py`
- MODIFIED `tests/gateway/test_restart_wait_prompt_reach.py`
- ADDED `tests/gateway/test_sibling_attach_while_profile_starting.py`
- MODIFIED `tests/gateway/test_unmanaged_idle_exit.py`
- ADDED `tests/nastech_cli/test_gateway_service_dbus_wait.py`
- MODIFIED `tests/nastech_cli/test_host_terminal_viewer_ownership.py`
- MODIFIED `tests/nastech_cli/test_ssh_workspace_fs.py`
- MODIFIED `tests/nastech_cli/test_web_server_file_ticket_generations.py`
- ADDED `tests/nastech_cli/test_web_server_file_ticket_retries.py`
- MODIFIED `tests/nastech_cli/test_web_server_files.py`
- MODIFIED `tests/nastech_cli/test_web_server_fs.py`
- MODIFIED `tests/nastech_cli/test_webapp_gated_sign_out.py`
- MODIFIED `tests/nastech_cli/test_webapp_renderer_build.py`
- MODIFIED `tests/nastech_cli/test_webapp_sign_out_sockets.py`
- MODIFIED `tests/plugins/dashboard_auth/test_basic_provider.py`
- ADDED `tests/plugins/test_a2a_no_token_guards.py`
- MODIFIED `tests/plugins/test_a2a_plugin.py`
- MODIFIED `tests/scripts/test_fresh_source_install.py`
- MODIFIED `tests/skills/test_unbroker_skill.py`
- ADDED `tests/test_utils_unlink_files_older_than.py`
- MODIFIED `tests/tui_gateway/test_tui_gateway_ws.py`
- MODIFIED `tools/approval_floors.py`
- MODIFIED `tools/bot_desktop/runtime.py`
- MODIFIED `tools/bot_desktop/sandbox_host.py`
- MODIFIED `tools/bot_mode_dm.py`
- MODIFIED `tools/bot_relay.py`
- MODIFIED `tools/voice_mode.py`
- MODIFIED `tui_gateway/methods_browser.py`
- MODIFIED `tui_gateway/ws.py`
- MODIFIED `utils.py`
- MODIFIED `uv.lock`
- MODIFIED `website/docs/reference/optional-skills-catalog.md`
- MODIFIED `website/docs/user-guide/docker.md`
- MODIFIED `website/docs/user-guide/messaging/a2a.md`
- MODIFIED `website/docs/user-guide/skills/optional/security/security-unbroker.md`
- MODIFIED `website/static/api/model-catalog.json`

## Scan

21473 files scanned [audio=5, binary=7, doc=4, font=13, image=165, text=21279]


## Diff

3461 renamed, 0 rewritten, 17286 identical, 158 locked, 0 missing, 20 owned, 498 reconciled


## Fork check (vs nastech-agent)

- 20916 identical, 513 updated (+0/-0 lines), 43 added, 0 missing, 0 fork-local-unpreserved, 0 stale-upstream, 0 registry-retired owned assets, 1 locked/binary, 0 collision-safe relocated, 50 preserved fork-local files, 0 violations

- features: fork 56 -> branded 56

Auto-generated by 100Ways.
