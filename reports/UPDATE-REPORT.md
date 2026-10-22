# Nastech Update Report #1

- upstream sha : `ebc9960b9d42e11e35ddbb6f0918cc163f739eb1`
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

- total measured: 467.21 s
- profile: `100ways.stage-profile.v1`

| stage | status | duration | share |
|-------|--------|----------|-------|
| brand | ok | 145.71 s | 31.2% |
| compare | ok | 133.87 s | 28.7% |
| verify | ok | 132.98 s | 28.5% |
| pull | ok | 40.44 s | 8.7% |
| reconcile | ok | 6.62 s | 1.4% |
| forkcheck | ok | 3.41 s | 0.7% |
| summary | ok | 2.91 s | 0.6% |
| preserve | ok | 0.83 s | 0.2% |
| scan | ok | 0.36 s | 0.1% |
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

Slowest: brand 145.7s, compare 133.9s, verify 133.0s.

## Brand

- total files : 20691
- renamed     : 3464 (folders and file names)
- text-rewritten : 20506
- locked-copied  : 157
- binary-copied  : 8
- owned assets   : 22 (our logo/banner/mascot override upstream)

## Reconcile

- fixed : 515 files reconciled: .env.example, .github/workflows/deploy-site.yml, .github/workflows/deploy-site.yml, .github/workflows/desktop-bundle-smoke.yml, .github/workflows/desktop-bundled-release.yml, .github/workflows/docs-search-monitor.yml, .github/workflows/install-e2e-macos-run.yml, .github/workflows/install-e2e-windows-run.yml, .github/workflows/plugin-catalog-ci.yml, .github/workflows/skills-index-freshness.yml, .github/workflows/tests-os.yml, .github/workflows/tests.yml, .github/workflows/tests.yml, .github/workflows/windows-install-update-e2e.yml, .mailmap, AGENTS.md, AGENTS.md, CONTRIBUTING.es.md, CONTRIBUTING.md, Dockerfile, README.es.md, README.md, README.ur-pk.md, README.zh-CN.md, SECURITY.es.md, SECURITY.es.md, SECURITY.md, SECURITY.md, agent/AGENTS.md, agent/agent_runtime_helpers.py, agent/anthropic_adapter.py, agent/anthropic_endpoints.py, agent/auxiliary_client.py, agent/auxiliary_client.py, agent/billing_links.py, agent/billing_view.py, agent/chat_completion_helpers.py, agent/conversation_compression.py, agent/conversation_loop.py, agent/message_sanitization.py, agent/model_metadata.py, agent/onboarding_first_tasks.py, agent/prompt_builder.py, agent/proxy_sources/iron_proxy.py, agent/reasoning_params.py, agent/subscription_view.py, agent/turn_recovery.py, agent/usage_pricing.py, agent/usage_pricing.py, apps/bootstrap-installer/src-tauri/Cargo.toml, apps/desktop/README.md, apps/desktop/electron-builder.config.cjs, apps/desktop/electron/backend-health.test.ts, apps/desktop/electron/backend-health.ts, apps/desktop/electron/challenge-window.test.ts, apps/desktop/electron/cloud-session-recovery.test.ts, apps/desktop/electron/connection-config.test.ts, apps/desktop/electron/data-paths.test.ts, apps/desktop/electron/hub-iframe-policy.ts, apps/desktop/electron/oauth-partition.test.ts, apps/desktop/electron/portal-session.ts, apps/desktop/electron/remote-lifecycle.ts, apps/desktop/electron/remote-oauth-ticket.test.ts, apps/desktop/electron/updater/checkout-source.test.ts, apps/desktop/electron/window-open-policy.test.ts, apps/desktop/scripts/bundle-env.test.mjs, apps/desktop/src/app/chat/sidebar/section-states.tsx, apps/desktop/src/app/messaging/index.test.tsx, apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx, apps/desktop/src/app/settings/billing/api.test.ts, apps/desktop/src/app/settings/billing/dev-fixtures.ts, apps/desktop/src/app/settings/billing/errors.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.ts, apps/desktop/src/app/settings/billing/use-charge-poller.test.ts, apps/desktop/src/app/settings/billing/use-step-up.test.tsx, apps/desktop/src/app/settings/constants.ts, apps/desktop/src/app/settings/gateway-settings.test.tsx, apps/desktop/src/app/settings/gateway-settings.tsx, apps/desktop/src/app/settings/toolset-config-panel.test.tsx, apps/desktop/src/app/shell/terms-butterbar.tsx, apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts, apps/desktop/src/components/boot-failure-overlay.test.tsx, apps/desktop/src/components/boot-failure-overlay.tsx, apps/desktop/src/components/send-diagnostics-dialog.tsx, apps/desktop/src/components/update-status.tsx, apps/desktop/src/contrib/plugin.ts, apps/desktop/src/i18n/de.ts, apps/desktop/src/i18n/en.ts, apps/desktop/src/i18n/es.ts, apps/desktop/src/i18n/fr.ts, apps/desktop/src/i18n/ja.ts, apps/desktop/src/i18n/ru.ts, apps/desktop/src/i18n/zh-hant_settings.ts, apps/desktop/src/i18n/zh.ts, apps/desktop/src/lib/docs.ts, apps/desktop/src/lib/plugin-catalog.ts, apps/desktop/src/plugins/nastech-bots/skills-hub-picker.test.tsx, apps/desktop/src/plugins/nastech-bots/skills-hub.tsx, apps/desktop/src/sdk/index.ts, apps/desktop/src/store/free-tier-challenge.test.ts, apps/desktop/src/store/notifications.ts, apps/desktop/src/store/shared-metrics.ts, apps/desktop/src/themes/use-skin-command.ts, cli-config.yaml.example, cron/AGENTS.md, eslint.config.shared.mjs, evals/auth_pool_controls.py, evals/browser_use/single_run.py, evals/postmortem/live_ab/auth_stampede.py, evals/postmortem/live_ab/cache_concurrency_probe.py, evals/postmortem/review_probes/cache_estimator_probe.py, evals/postmortem/review_probes/credential_identity_probe.py, evals/reasoning_replay/harness.py, gateway/AGENTS.md, locales/_keys.desktop.json, locales/_keys.tui.json, nastech_cli/AGENTS.md, nastech_cli/anon_auth.py, nastech_cli/anon_auth.py, nastech_cli/anon_sign_in.py, nastech_cli/auth.py, nastech_cli/auth_codex.py, nastech_cli/auth_constants.py, nastech_cli/auth_constants.py, nastech_cli/auth_error_copy.py, nastech_cli/auth_nastech.py, nastech_cli/banner.py, nastech_cli/config_defaults.py, nastech_cli/dashboard_auth/login_page.py, nastech_cli/dashboard_register.py, nastech_cli/dashboard_register.py, nastech_cli/debug.py, nastech_cli/diagnostics_upload.py, nastech_cli/fallback_cmd.py, nastech_cli/gateway_chat_commands.py, nastech_cli/kanban_parser.py, nastech_cli/main.py, nastech_cli/main_dashboard.py, nastech_cli/main_desktop.py, nastech_cli/model_catalog.py, nastech_cli/model_setup_flows_common.py, nastech_cli/models.py, nastech_cli/models_pricing.py, nastech_cli/models_pricing.py, nastech_cli/nastech_account.py, nastech_cli/nastech_account.py, nastech_cli/nastech_billing.py, nastech_cli/nastech_billing.py, nastech_cli/observability/shared_metrics_consent.py, nastech_cli/observability/shared_metrics_send_config.py, nastech_cli/observability/shared_metrics_send_config.py, nastech_cli/plugin_catalog.py, nastech_cli/plugins_cmd.py, nastech_cli/portal_cli.py, nastech_cli/portal_cli.py, nastech_cli/providers.py, nastech_cli/proxy/adapters/base.py, nastech_cli/proxy/adapters/nastech_portal.py, nastech_cli/release_channels.py, nastech_cli/setup.py, nastech_cli/setup_platforms.py, nastech_cli/setup_quick.py, nastech_cli/skin_engine.py, nastech_cli/source_releases.py, nastech_cli/steward.py, nastech_cli/subcommands/egress.py, nastech_cli/subcommands/fallback.py, nastech_cli/subcommands/secrets.py, nastech_cli/subcommands/worktree.py, nastech_cli/telegram_managed_bot.py, nastech_cli/telegram_managed_bot.py, nastech_cli/tools_config.py, nastech_cli/uninstall.py, nastech_cli/update_cmd.py, nastech_cli/update_cmd_git.py, nastech_cli/update_cmd_git.py, nastech_cli/update_cmd_maint.py, nastech_cli/update_cmd_zip.py, nastech_cli/update_downgrade_guard.py, nastech_cli/web_routers/status.py, nastech_cli/web_server_messaging.py, nastech_cli/web_server_messaging.py, nastech_cli/web_server_oauth.py, nastech_constants.py, nastech_state_common.py, nastech_state_errors.py, nastech_state_reconcile.py, optional-skills/creative/pretext/templates/donut-orbit.html, optional-skills/productivity/memento-flashcards/SKILL.md, package-lock.json, plugin-catalog/README.md, plugins/AGENTS.md, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/plugin.yaml, plugins/kanban/dashboard/dist/index.js, plugins/kanban/systemd/nastech-kanban-dispatcher.service, plugins/model-providers/ai-gateway/__init__.py, plugins/model-providers/fireworks/__init__.py, plugins/model-providers/kimi-coding/__init__.py, plugins/model-providers/nastech/__init__.py, plugins/model-providers/opencode-zen/__init__.py, plugins/model-providers/solstice/auth.py, plugins/model-providers/solstice/auth.py, plugins/nastech-achievements/dashboard/dist/index.js, plugins/platforms/discord/adapter.py, plugins/platforms/discord/onboarding.py, plugins/platforms/email/adapter.py, plugins/platforms/google_chat/adapter.py, plugins/platforms/irc/adapter.py, plugins/platforms/line/adapter.py, plugins/platforms/ntfy/adapter.py, plugins/platforms/photon/adapter.py, plugins/platforms/photon/sidecar/package-lock.json, plugins/platforms/raft/adapter.py, plugins/platforms/simplex/adapter.py, plugins/platforms/slack/adapter.py, plugins/platforms/teams/adapter.py, plugins/platforms/weixin/adapter.py, plugins/platforms/whatsapp_cloud/adapter.py, plugins/platforms/whatsapp_cloud/setup_wizard.py, plugins/web/perplexity/provider.py, pm/artifact-mirror.json, pm/network.py, pm/uv.lock, scripts/build_model_catalog.py, scripts/ci/check_catalog_cors.py, scripts/contributor_audit.py, scripts/e2e_shared_metrics_staging.py, scripts/install.cmd, scripts/install.ps1, scripts/install.sh, scripts/release.py, scripts/releases/authors_legacy.py, scripts/releases/entrypoint.py, scripts/releases/lanes.py, scripts/releases/pick_tags.py, scripts/releases/r2.py, scripts/sandbox/generate-e2e-matrix.mjs, scripts/sandbox/pick-release-tags.sh, scripts/termux/stage_apt_repo.py, scripts/tests/test-install-ps1-store-guard.ps1, scripts/whatsapp-bridge/package-lock.json, setup.py, skills/AGENTS.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/references/background-systems.md, skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md, skills/autonomous-ai-agents/nastech-agent/references/configuration.md, skills/autonomous-ai-agents/nastech-agent/references/contributor-guide.md, skills/autonomous-ai-agents/nastech-agent/references/portal-auth-for-third-party-apps.md, skills/autonomous-ai-agents/nastech-agent/references/providers-and-models.md, skills/autonomous-ai-agents/nastech-agent/references/webhooks.md, skills/media/youtube-content/SKILL.md, skills/software-development/python-debugpy/SKILL.md, tests-js/bundle-smoke-metadata.test.mjs, tests-js/update-ui.test.mjs, tests/agent/test_anthropic_adapter.py, tests/agent/test_anthropic_preserved_thinking_replay.py, tests/agent/test_anthropic_prompt_cache_policy.py, tests/agent/test_auxiliary_auth_rung_fallthrough.py, tests/agent/test_auxiliary_client.py, tests/agent/test_auxiliary_client_nastech_401_cache_key.py, tests/agent/test_auxiliary_main_first.py, tests/agent/test_auxiliary_transport_autodetect.py, tests/agent/test_billing_links.py, tests/agent/test_credential_pool.py, tests/agent/test_credential_pool_nastech_refresh_stampede.py, tests/agent/test_credits_cold_start.py, tests/agent/test_credits_policy.py, tests/agent/test_deepseek_anthropic_thinking.py, tests/agent/test_error_classifier.py, tests/agent/test_error_classifier_observed.py, tests/agent/test_fast_mode_auto.py, tests/agent/test_free_tier_rate_limit_class.py, tests/agent/test_model_metadata.py, tests/agent/test_nastech_credits_gauge.py, tests/agent/test_nastech_key_pre_expiry_adoption.py, tests/agent/test_nastech_portal_anthropic_wire.py, tests/agent/test_nastech_rate_guard.py, tests/agent/test_nastech_welcome_client_contract.py, tests/agent/test_nastech_wire_auto.py, tests/agent/test_nonretryable_result_carries_verdict.py, tests/agent/test_onboarding_first_tasks.py, tests/agent/test_primary_runtime_restore.py, tests/agent/test_provider_attribution_headers.py, tests/agent/test_provider_fallback.py, tests/agent/test_provider_history_parity.py, tests/agent/test_provider_parity.py, tests/agent/test_reasoning_replay_routes.py, tests/agent/test_run_agent.py, tests/agent/test_run_agent.py, tests/agent/test_switch_model_reapplies_headers.py, tests/agent/test_turn_usage_log_line.py, tests/agent/test_welcome_error_identity.py, tests/agent/test_welcome_tier_recovery.py, tests/agent/transports/test_chat_completions.py, tests/agent/transports/test_chat_completions_reasoning_details_replay.py, tests/agent/transports/test_provider_wire_snapshot.py, tests/compat/old_updater_dependencies.py, tests/conftest.py, tests/docker/test_sqlite_runtime.py, tests/e2e/core/live/_helpers.py, tests/e2e/core/providers/test_catalog_oauth.py, tests/e2e/core/providers/test_chat_reasoning_variants.py, tests/e2e/core/providers/test_fallback_providers.py, tests/e2e/core/upgrade/network/_seed.py, tests/e2e/core/windows/test_boot_lifecycle.py, tests/e2e/core/windows_update/_machine.py, tests/fakes/providers/chat_variants.py, tests/fakes/providers/vertex.py, tests/fixtures/prompt_surface/prompts/cli-code.claude.txt, tests/fixtures/prompt_surface/prompts/cli-code.claude.txt, tests/fixtures/prompt_surface/prompts/cli.claude.txt, tests/fixtures/prompt_surface/prompts/cli.claude.txt, tests/fixtures/prompt_surface/prompts/cli.gemini.txt, tests/fixtures/prompt_surface/prompts/cli.gemini.txt, tests/fixtures/prompt_surface/prompts/cli.gpt.txt, tests/fixtures/prompt_surface/prompts/cli.gpt.txt, tests/fixtures/prompt_surface/prompts/cli.nastech.txt, tests/fixtures/prompt_surface/prompts/cli.nastech.txt, tests/fixtures/prompt_surface/prompts/cron.claude.txt, tests/fixtures/prompt_surface/prompts/cron.claude.txt, tests/fixtures/prompt_surface/prompts/desktop.claude.txt, tests/fixtures/prompt_surface/prompts/desktop.claude.txt, tests/fixtures/prompt_surface/prompts/discord.claude.txt, tests/fixtures/prompt_surface/prompts/discord.claude.txt, tests/fixtures/prompt_surface/prompts/telegram.claude.txt, tests/fixtures/prompt_surface/prompts/telegram.claude.txt, tests/fixtures/prompt_surface/surfaces.json, tests/fixtures/provider_wire_snapshot.json, tests/gateway/fixtures/local_recovery_probe.py, tests/gateway/test_discord_format.py, tests/gateway/test_housekeeping_profile_scope.py, tests/gateway/test_internal_event_pin_wiring.py, tests/gateway/test_model_switch_persistence.py, tests/gateway/test_run_progress_topics.py, tests/gateway/test_session_model_override_persistence.py, tests/gateway/test_startup_warmup_profile_scope.py, tests/gateway/test_status_command.py, tests/gateway/test_telegram_mention_context.py, tests/gateway/test_usage_command.py, tests/install/macos-desktop-e2e.sh, tests/install/windows-e2e.ps1, tests/nastech_cli/anon_portal.py, tests/nastech_cli/test_anon_auth_core.py, tests/nastech_cli/test_anon_failure_modes.py, tests/nastech_cli/test_anon_failure_modes.py, tests/nastech_cli/test_anon_picker.py, tests/nastech_cli/test_anon_surfaces.py, tests/nastech_cli/test_anon_upgrade.py, tests/nastech_cli/test_auth_nastech_provider.py, tests/nastech_cli/test_base_url_host_identity.py, tests/nastech_cli/test_browse_schema_drift.py, tests/nastech_cli/test_cli_first_run_setup.py, tests/nastech_cli/test_cli_goal_parked_resume.py, tests/nastech_cli/test_cli_init.py, tests/nastech_cli/test_cli_provider_resolution.py, tests/nastech_cli/test_dashboard_register.py, tests/nastech_cli/test_fireworks_provider.py, tests/nastech_cli/test_gateway_chat_native.py, tests/nastech_cli/test_local_abandoned_requests.py, tests/nastech_cli/test_local_quickstart.py, tests/nastech_cli/test_main_merge_lifecycle.py, tests/nastech_cli/test_model_catalog.py, tests/nastech_cli/test_model_validation.py, tests/nastech_cli/test_nastech_anthropic_wire_default.py, tests/nastech_cli/test_nastech_auth_keepalive.py, tests/nastech_cli/test_nastech_auth_status_cache.py, tests/nastech_cli/test_nastech_inference_url_validation.py, tests/nastech_cli/test_nastech_nonproduction_inference_host.py, tests/nastech_cli/test_nastech_nonproduction_inference_host.py, tests/nastech_cli/test_nastech_portal_staging_allowlist.py, tests/nastech_cli/test_nastech_reasoning_metadata.py, tests/nastech_cli/test_proxy.py, tests/nastech_cli/test_reasoning_caps_disk_cache.py, tests/nastech_cli/test_release_channels.py, tests/nastech_cli/test_sale_pricing.py, tests/nastech_cli/test_show_config_credential.py, tests/nastech_cli/test_source_channel_integration.py, tests/nastech_cli/test_source_check.py, tests/nastech_cli/test_taskkill_identity_windows_live.py, tests/nastech_cli/test_update_fetch_failure_classifier.py, tests/nastech_cli/test_update_target_identity.py, tests/nastech_cli/test_web_oauth_dispatch.py, tests/plugins/dashboard_auth/test_nastech_provider.py, tests/plugins/image_gen/check_parity_vs_main.py, tests/plugins/image_gen/test_openrouter_compat_provider.py, tests/plugins/test_chronos_verify.py, tests/scripts/desktop_update/test_desktop_update_windows_commit_outcome.py, tests/scripts/desktop_update/test_desktop_update_windows_marker.py, tests/scripts/desktop_update/test_desktop_update_windows_marker_lock.py, tests/scripts/test_release_build_commit.py, tests/scripts/test_release_channels.py, tests/scripts/test_release_entrypoint.py, tests/scripts/test_release_lanes.py, tests/scripts/test_release_r2.py, tests/scripts/test_release_r2.py, tests/scripts/test_stable_release.py, tests/scripts/test_stage_apt_repo.py, tests/scripts/test_upload_summary.py, tests/test_session_daemon_reaper.py, tests/tools/test_connector_wire_identity.py, tests/tools/test_delegate.py, tests/tools/test_managed_media_gateways.py, tests/tools/test_managed_tool_gateway.py, tests/tools/test_plugin_guard.py, tests/tools/test_stage2_hook_nastech_routing_env.py, tests/tools/test_strict_provider_selection.py, tests/tools/test_tts_openai_config.py, tests/tools/test_url_safety.py, tests/tools/test_web_tools_config.py, tests/tools/test_web_tools_perplexity.py, tests/tui_gateway/test_compute_host.py, tests/tui_gateway/test_connector_accounts_rpc.py, tests/tui_gateway/test_connector_operation_rpc.py, tests/tui_gateway/test_legacy_fallback_ticket_profile_verbs.py, tests/tui_gateway/test_resume_switched_provider_endpoint.py, tests/website/test_extract_skills.py, tools/AGENTS.md, tools/managed_gateway_auth.py, tools/managed_gateway_identity.py, tools/managed_tool_gateway.py, tools/mcp_oauth.py, tools/plugin_guard_context.py, tools/skills_hub_search.py, trajectory_compressor.py, ui-tui/scripts/billing-fixtures.tsx, ui-tui/src/__tests__/subscriptionCommand.test.ts, ui-tui/src/__tests__/subscriptionOverlay.test.tsx, ui-tui/src/app/slash/commands/subscription.ts, ui-tui/src/domain/paths.ts, uv.lock, web/src/components/SharedMetricsConsentBanner.tsx, web/src/components/SidebarFooter.tsx, web/src/pages/DocsPage.tsx, web/src/pages/PluginsPage.tsx, web/src/pages/SystemPage.tsx, website/README.md, website/docs/developer-guide/egress-internals.md, website/docs/developer-guide/stable-releases.md, website/docs/getting-started/installation.md, website/docs/getting-started/platform-support.md, website/docs/getting-started/quickstart.md, website/docs/getting-started/termux.md, website/docs/getting-started/termux.md, website/docs/getting-started/updating.md, website/docs/guides/manage-nastech-cloud-with-mcp.md, website/docs/guides/run-nastech-with-nastech-portal.md, website/docs/guides/run-nemotron-3-ultra-free.md, website/docs/index.mdx, website/docs/integrations/nastech-portal.md, website/docs/integrations/providers.md, website/docs/reference/cli-commands.md, website/docs/reference/environment-variables.md, website/docs/reference/faq.md, website/docs/reference/model-catalog.md, website/docs/reference/skills-catalog.md, website/docs/user-guide/desktop.md, website/docs/user-guide/egress/iron-proxy.md, website/docs/user-guide/features/browser.md, website/docs/user-guide/features/image-generation.md, website/docs/user-guide/features/plugin-catalog.md, website/docs/user-guide/features/skills.md, website/docs/user-guide/features/subscription-proxy.md, website/docs/user-guide/features/tool-gateway.md, website/docs/user-guide/features/tools.md, website/docs/user-guide/features/tts.md, website/docs/user-guide/features/web-dashboard.md, website/docs/user-guide/features/web-search.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/skills/bundled/media/media-youtube-content.md, website/docs/user-guide/skills/bundled/software-development/software-development-python-debugpy.md, website/docs/user-guide/skills/optional/productivity/productivity-memento-flashcards.md, website/docs/user-guide/windows-native.md, website/docs/user-guide/windows-wsl-quickstart.md, website/docusaurus.config.ts, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/plugins/index.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/quickstart.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-nastech-with-nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/index.mdx, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/providers.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/faq.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/model-catalog.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/subscription-proxy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tools.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tts.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/media/media-youtube-content.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/software-development/software-development-python-debugpy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/optional/productivity/productivity-memento-flashcards.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-native.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-wsl-quickstart.md, website/scripts/check-live-search.mjs, website/scripts/extract-skills.py, website/scripts/fetch-plugin-stars.py, website/scripts/generate-llms-txt.py, website/scripts/prebuild.mjs, website/src/pages/plugins/index.tsx, website/src/pages/skills/index.tsx, website/static/api/model-catalog.json, website/static/oauth/client-metadata.json


## Direct upstream tree delta

- complete: +24 ~193 -16 ↪0
- MODIFIED `.github/workflows/desktop-bundled-release.yml`
- MODIFIED `.github/workflows/docker.yml`
- MODIFIED `.github/workflows/sandbox-image.yml`
- MODIFIED `.github/workflows/stable-release-publication.yml`
- MODIFIED `.github/workflows/stable-release.yml`
- MODIFIED `.npmrc`
- MODIFIED `agent/auxiliary_client.py`
- MODIFIED `agent/chat_completion_helpers.py`
- MODIFIED `agent/error_classifier.py`
- MODIFIED `agent/error_surface.py`
- MODIFIED `agent/message_metadata.py`
- MODIFIED `agent/moa_loop.py`
- MODIFIED `agent/tool_executor.py`
- MODIFIED `agent/transports/chat_completions.py`
- MODIFIED `agent/turn_failure_copy.py`
- MODIFIED `agent/turn_recovery.py`
- MODIFIED `apps/bootstrap-installer/package.json`
- MODIFIED `apps/desktop/electron/git-review-ops.test.ts`
- MODIFIED `apps/desktop/electron/git-review-ops.ts`
- MODIFIED `apps/desktop/package.json`
- MODIFIED `apps/desktop/src/api/mcp.ts`
- MODIFIED `apps/desktop/src/api/system.ts`
- MODIFIED `apps/desktop/src/app/chat/composer/hooks/use-composer-draft.ts`
- MODIFIED `apps/desktop/src/app/chat/composer/index.tsx`
- DELETED `apps/desktop/src/app/chat/composer/suggestion-pills.test.tsx`
- DELETED `apps/desktop/src/app/chat/composer/suggestion-pills.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/gateway-event/tools.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-session-actions/branch-approval-owner.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-actions/index.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-session-actions/runtime-owner.test.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-session-actions/runtime-owner.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-actions/utils.ts`
- MODIFIED `apps/desktop/src/app/shell/approval-mode-menu.test.tsx`
- MODIFIED `apps/desktop/src/app/shell/approval-mode-menu.tsx`
- MODIFIED `apps/desktop/src/app/shell/hooks/use-statusbar-items.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/mcp-setup-tool.tsx`
- MODIFIED `apps/desktop/src/i18n/ar_boot.ts`
- MODIFIED `apps/desktop/src/i18n/de.ts`
- MODIFIED `apps/desktop/src/i18n/de_notices.ts`
- MODIFIED `apps/desktop/src/i18n/en.ts`
- MODIFIED `apps/desktop/src/i18n/en_notices.ts`
- MODIFIED `apps/desktop/src/i18n/es.ts`
- MODIFIED `apps/desktop/src/i18n/es_notices.ts`
- MODIFIED `apps/desktop/src/i18n/fr.ts`
- MODIFIED `apps/desktop/src/i18n/fr_notices.ts`
- MODIFIED `apps/desktop/src/i18n/ja_notices.ts`
- MODIFIED `apps/desktop/src/i18n/overlay-gaps.json`
- MODIFIED `apps/desktop/src/i18n/ru.ts`
- MODIFIED `apps/desktop/src/i18n/ru_notices.ts`
- MODIFIED `apps/desktop/src/i18n/types.ts`
- MODIFIED `apps/desktop/src/i18n/types_notices.ts`
- MODIFIED `apps/desktop/src/i18n/zh-hant_boot.ts`
- MODIFIED `apps/desktop/src/i18n/zh.ts`
- MODIFIED `apps/desktop/src/i18n/zh_notices.ts`
- MODIFIED `apps/desktop/src/lib/mcp-brands.tsx`
- MODIFIED `apps/desktop/src/lib/mcp-reload.test.ts`
- MODIFIED `apps/desktop/src/lib/mcp-reload.ts`
- DELETED `apps/desktop/src/store/composer-suggestions.test.ts`
- DELETED `apps/desktop/src/store/composer-suggestions.ts`
- MODIFIED `apps/desktop/src/store/profile-remote-override.ts`
- DELETED `apps/desktop/src/store/suggestion-providers/cron.test.ts`
- DELETED `apps/desktop/src/store/suggestion-providers/cron.ts`
- DELETED `apps/desktop/src/store/suggestion-providers/github.test.ts`
- DELETED `apps/desktop/src/store/suggestion-providers/github.ts`
- DELETED `apps/desktop/src/store/suggestion-providers/mcp.test.ts`
- DELETED `apps/desktop/src/store/suggestion-providers/mcp.ts`
- DELETED `apps/desktop/src/store/suggestion-providers/repair.test.ts`
- DELETED `apps/desktop/src/store/suggestion-providers/repair.ts`
- DELETED `apps/desktop/src/store/suggestion-providers/skill.test.ts`
- DELETED `apps/desktop/src/store/suggestion-providers/skill.ts`
- MODIFIED `cron/scheduler.py`
- MODIFIED `gateway/control_socket.py`
- MODIFIED `gateway/slash_commands_model.py`
- MODIFIED `gateway/slash_commands_session.py`
- MODIFIED `gateway/status.py`
- MODIFIED `gateway/status_scoped_locks.py`
- MODIFIED `nastech_cli/_parser.py`
- MODIFIED `nastech_cli/agent_plugins.py`
- MODIFIED `nastech_cli/cli_commands_mixin.py`
- MODIFIED `nastech_cli/config_defaults.py`
- MODIFIED `nastech_cli/console_engine.py`
- MODIFIED `nastech_cli/doctor_state.py`
- MODIFIED `nastech_cli/left_core_migration.py`
- MODIFIED `nastech_cli/main.py`
- MODIFIED `nastech_cli/mcp_config.py`
- MODIFIED `nastech_cli/plugin_validate.py`
- MODIFIED `nastech_cli/plugin_validate_desktop.py`
- MODIFIED `nastech_cli/plugins_cmd_install.py`
- MODIFIED `nastech_cli/plugins_transaction.py`
- MODIFIED `nastech_cli/subcommands/mcp.py`
- MODIFIED `nastech_cli/update_cmd.py`
- MODIFIED `nastech_cli/update_cmd_git.py`
- MODIFIED `nastech_cli/update_cmd_maint.py`
- MODIFIED `nastech_cli/update_pause_record.py`
- MODIFIED `nastech_cli/web_models.py`
- MODIFIED `nastech_cli/web_routers/messaging.py`
- MODIFIED `nastech_cli/web_server_messaging.py`
- ADDED `nastech_cli/web_whatsapp_session.py`
- MODIFIED `nastech_state_dbfile.py`
- MODIFIED `nastech_state_fts.py`
- MODIFIED `nastech_state_messages.py`
- MODIFIED `nastech_state_repair.py`
- MODIFIED `nastech_state_runtime.py`
- MODIFIED `nastech_state_schema.py`
- MODIFIED `nastech_state_search.py`
- MODIFIED `locales/_keys.desktop.json`
- MODIFIED `locales/af.yaml`
- MODIFIED `locales/ar.yaml`
- MODIFIED `locales/de.yaml`
- MODIFIED `locales/en.yaml`
- MODIFIED `locales/es.yaml`
- MODIFIED `locales/fr.yaml`
- MODIFIED `locales/ga.yaml`
- MODIFIED `locales/hu.yaml`
- MODIFIED `locales/it.yaml`
- MODIFIED `locales/ja.yaml`
- MODIFIED `locales/ko.yaml`
- MODIFIED `locales/pt.yaml`
- MODIFIED `locales/ru.yaml`
- MODIFIED `locales/tr.yaml`
- MODIFIED `locales/uk.yaml`
- MODIFIED `locales/zh-hant.yaml`
- MODIFIED `locales/zh.yaml`
- DELETED `mcp_serve.py`
- MODIFIED `package-lock.json`
- MODIFIED `package.json`
- MODIFIED `plugin-catalog/README.md`
- ADDED `plugin-catalog/agent-importers.yaml`
- ADDED `plugin-catalog/bubblewrap.yaml`
- MODIFIED `plugin-catalog/cua-spaces.yaml`
- MODIFIED `plugin-catalog/nastech-telegram-business.yaml`
- ADDED `plugin-catalog/inbox.yaml`
- ADDED `plugin-catalog/mcp-serve.yaml`
- ADDED `plugin-catalog/meshy.yaml`
- ADDED `plugin-catalog/singularity.yaml`
- ADDED `plugin-catalog/workflow-record.yaml`
- MODIFIED `plugins/AGENTS.md`
- MODIFIED `plugins/model-providers/nastech/__init__.py`
- MODIFIED `pm/AGENTS.md`
- MODIFIED `pm/cli.py`
- MODIFIED `pm/downloader.py`
- MODIFIED `pm/plugin_declarations.py`
- MODIFIED `pyproject.toml`
- MODIFIED `scripts/ci/classify_changes.py`
- MODIFIED `scripts/install.ps1`
- MODIFIED `scripts/install.sh`
- MODIFIED `skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md`
- MODIFIED `tests-js/scripts/desktop-smoke-process.ts`
- MODIFIED `tests-js/scripts/desktop-smoke.test.ts`
- MODIFIED `tests-js/scripts/mock-server.ts`
- MODIFIED `tests/agent/test_auxiliary_client.py`
- ADDED `tests/agent/test_error_classifier_data_policy.py`
- MODIFIED `tests/agent/test_moa_loop_mode.py`
- MODIFIED `tests/agent/test_nastech_portal_anthropic_wire.py`
- MODIFIED `tests/agent/test_provider_parity.py`
- MODIFIED `tests/agent/test_tool_call_incremental_persistence.py`
- ADDED `tests/e2e/core/windows_update/test_damaged_checkout.py`
- MODIFIED `tests/gateway/test_api_server_active_work_drain.py`
- MODIFIED `tests/gateway/test_branch_routing_columns.py`
- MODIFIED `tests/gateway/test_control_socket_peer_security.py`
- ADDED `tests/gateway/test_scoped_process_reservations.py`
- MODIFIED `tests/nastech_cli/test_argparse_flag_propagation.py`
- MODIFIED `tests/nastech_cli/test_cli_startup_trim.py`
- MODIFIED `tests/nastech_cli/test_fts_optimize_notice.py`
- MODIFIED `tests/nastech_cli/test_left_core_migration.py`
- MODIFIED `tests/nastech_cli/test_mcp_startup.py`
- MODIFIED `tests/nastech_cli/test_plugin_dependency_consent.py`
- MODIFIED `tests/nastech_cli/test_plugin_validate.py`
- MODIFIED `tests/nastech_cli/test_update_fetch_failure_classifier.py`
- MODIFIED `tests/nastech_cli/test_update_pause_record.py`
- ADDED `tests/nastech_cli/test_whatsapp_dashboard_repair.py`
- ADDED `tests/nastech_state/test_fts_layout_drift.py`
- MODIFIED `tests/nastech_state/test_nastech_state.py`
- MODIFIED `tests/nastech_state/test_nastech_state_readonly_preflight.py`
- MODIFIED `tests/nastech_state/test_state_db_stats.py`
- MODIFIED `tests/install/e2e-assets/desktop-smoke-windows.ps1`
- MODIFIED `tests/install/e2e-assets/desktop-smoke.ts`
- MODIFIED `tests/install/e2e-assets/mock-provider.mjs`
- MODIFIED `tests/install/e2e-assets/mock-provider.sh`
- MODIFIED `tests/install/e2e-assets/update-window-chat.d.mts`
- MODIFIED `tests/install/e2e-assets/update-window-chat.mjs`
- MODIFIED `tests/install/macos-desktop-e2e.sh`
- MODIFIED `tests/install/windows-e2e.ps1`
- MODIFIED `tests/pm/test_download_mirrors.py`
- MODIFIED `tests/pm/test_plugin_declarations.py`
- MODIFIED `tests/pm/test_source_update_launch.py`
- MODIFIED `tests/pm/test_update_artifact_refresh.py`
- MODIFIED `tests/pm/test_update_dependency_legs.py`
- MODIFIED `tests/pm/test_update_failure_status.py`
- MODIFIED `tests/scripts/install/test_install_sh_repository_stage.py`
- DELETED `tests/test_mcp_serve.py`
- MODIFIED `tests/test_packaging_metadata.py`
- MODIFIED `tests/tools/test_connector_dispatch_policy.py`
- MODIFIED `tests/tools/test_connectors_gateway_client.py`
- ADDED `tests/tools/test_mcp_tool_client_info.py`
- ADDED `tests/tools/test_mcp_tool_costs.py`
- MODIFIED `tests/tools/test_process_registry.py`
- ADDED `tests/tools/test_process_registry_env_spawn_cwd.py`
- ADDED `tests/tools/test_terminal_background_spawn_failure.py`
- MODIFIED `tools/approval_yolo.py`
- ADDED `tools/connectors/data_use.py`
- MODIFIED `tools/connectors/dispatch.py`
- MODIFIED `tools/connectors/gateway/client.py`
- MODIFIED `tools/connectors/gateway/merge.py`
- MODIFIED `tools/connectors/gateway/wire.py`
- MODIFIED `tools/mcp_tool.py`
- MODIFIED `tools/mcp_tool_config.py`
- ADDED `tools/mcp_tool_costs.py`
- MODIFIED `tools/mcp_tool_handlers.py`
- MODIFIED `tools/mcp_tool_registration.py`
- MODIFIED `tools/mcp_tool_scope.py`
- MODIFIED `tools/mcp_tool_transport.py`
- MODIFIED `tools/process_registry.py`
- MODIFIED `uv.lock`
- MODIFIED `web/package.json`
- ADDED `web/src/lib/api-whatsapp.ts`
- MODIFIED `web/src/lib/api.test.ts`
- MODIFIED `web/src/lib/api.ts`
- MODIFIED `web/src/pages/ChannelsPage.tsx`
- ADDED `web/src/pages/ChannelsPage.whatsapp.test.tsx`
- MODIFIED `website/.npmrc`
- MODIFIED `website/docs/developer-guide/plugins/catalog-submission.md`
- MODIFIED `website/docs/developer-guide/plugins/index.md`
- MODIFIED `website/docs/getting-started/updating.md`
- MODIFIED `website/docs/reference/cli-commands.md`
- MODIFIED `website/docs/reference/mcp-config-reference.md`
- MODIFIED `website/docs/reference/package-management.md`
- MODIFIED `website/docs/user-guide/features/hooks.md`
- MODIFIED `website/docs/user-guide/features/mcp.md`
- MODIFIED `website/docs/user-guide/features/plugin-catalog.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/mcp.md`
- MODIFIED `website/package-lock.json`
- MODIFIED `website/package.json`

## Scan

20740 files scanned [audio=5, binary=7, doc=4, font=13, image=165, text=20546]


## Diff

3317 renamed, 0 rewritten, 16721 identical, 158 locked, 0 missing, 20 owned, 475 reconciled


## Fork check (vs nastech-agent)

- 20519 identical, 192 updated (+0/-0 lines), 24 added, 0 missing, 0 fork-local-unpreserved, 0 stale-upstream, 0 registry-retired owned assets, 5 locked/binary, 0 collision-safe relocated, 49 preserved fork-local files, 0 violations

- features: fork 56 -> branded 56

Auto-generated by 100Ways.
