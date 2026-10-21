# Nastech Update Report #1

- upstream sha : `369cc6b07f26f4454f56555f1001ea9eb7d8d948`
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

## Brand

- total files : 20683
- renamed     : 3461 (folders and file names)
- text-rewritten : 20498
- locked-copied  : 157
- binary-copied  : 8
- owned assets   : 22 (our logo/banner/mascot override upstream)

## Reconcile

- fixed : 512 files reconciled: .env.example, .github/workflows/deploy-site.yml, .github/workflows/deploy-site.yml, .github/workflows/desktop-bundle-smoke.yml, .github/workflows/desktop-bundled-release.yml, .github/workflows/docs-search-monitor.yml, .github/workflows/install-e2e-macos-run.yml, .github/workflows/install-e2e-windows-run.yml, .github/workflows/plugin-catalog-ci.yml, .github/workflows/skills-index-freshness.yml, .github/workflows/tests-os.yml, .github/workflows/tests.yml, .github/workflows/tests.yml, .github/workflows/windows-install-update-e2e.yml, .mailmap, AGENTS.md, AGENTS.md, CONTRIBUTING.es.md, CONTRIBUTING.md, Dockerfile, README.es.md, README.md, README.ur-pk.md, README.zh-CN.md, SECURITY.es.md, SECURITY.es.md, SECURITY.md, SECURITY.md, agent/AGENTS.md, agent/agent_runtime_helpers.py, agent/anthropic_adapter.py, agent/anthropic_endpoints.py, agent/auxiliary_client.py, agent/auxiliary_client.py, agent/billing_links.py, agent/billing_view.py, agent/chat_completion_helpers.py, agent/conversation_compression.py, agent/conversation_loop.py, agent/message_sanitization.py, agent/model_metadata.py, agent/onboarding_first_tasks.py, agent/prompt_builder.py, agent/proxy_sources/iron_proxy.py, agent/reasoning_params.py, agent/subscription_view.py, agent/turn_recovery.py, agent/usage_pricing.py, agent/usage_pricing.py, apps/bootstrap-installer/src-tauri/Cargo.toml, apps/desktop/README.md, apps/desktop/electron-builder.config.cjs, apps/desktop/electron/backend-health.test.ts, apps/desktop/electron/backend-health.ts, apps/desktop/electron/challenge-window.test.ts, apps/desktop/electron/cloud-session-recovery.test.ts, apps/desktop/electron/connection-config.test.ts, apps/desktop/electron/data-paths.test.ts, apps/desktop/electron/hub-iframe-policy.ts, apps/desktop/electron/oauth-partition.test.ts, apps/desktop/electron/portal-session.ts, apps/desktop/electron/remote-lifecycle.ts, apps/desktop/electron/remote-oauth-ticket.test.ts, apps/desktop/electron/updater/checkout-source.test.ts, apps/desktop/electron/window-open-policy.test.ts, apps/desktop/scripts/bundle-env.test.mjs, apps/desktop/src/app/chat/sidebar/section-states.tsx, apps/desktop/src/app/messaging/index.test.tsx, apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx, apps/desktop/src/app/settings/billing/api.test.ts, apps/desktop/src/app/settings/billing/dev-fixtures.ts, apps/desktop/src/app/settings/billing/errors.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.ts, apps/desktop/src/app/settings/billing/use-charge-poller.test.ts, apps/desktop/src/app/settings/billing/use-step-up.test.tsx, apps/desktop/src/app/settings/constants.ts, apps/desktop/src/app/settings/gateway-settings.test.tsx, apps/desktop/src/app/settings/gateway-settings.tsx, apps/desktop/src/app/settings/toolset-config-panel.test.tsx, apps/desktop/src/app/shell/terms-butterbar.tsx, apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts, apps/desktop/src/components/boot-failure-overlay.test.tsx, apps/desktop/src/components/boot-failure-overlay.tsx, apps/desktop/src/components/send-diagnostics-dialog.tsx, apps/desktop/src/components/update-status.tsx, apps/desktop/src/contrib/plugin.ts, apps/desktop/src/i18n/de.ts, apps/desktop/src/i18n/en.ts, apps/desktop/src/i18n/es.ts, apps/desktop/src/i18n/fr.ts, apps/desktop/src/i18n/ja.ts, apps/desktop/src/i18n/ru.ts, apps/desktop/src/i18n/zh-hant_settings.ts, apps/desktop/src/i18n/zh.ts, apps/desktop/src/lib/docs.ts, apps/desktop/src/lib/plugin-catalog.ts, apps/desktop/src/plugins/nastech-bots/skills-hub-picker.test.tsx, apps/desktop/src/plugins/nastech-bots/skills-hub.tsx, apps/desktop/src/sdk/index.ts, apps/desktop/src/store/free-tier-challenge.test.ts, apps/desktop/src/store/notifications.ts, apps/desktop/src/store/shared-metrics.ts, apps/desktop/src/themes/use-skin-command.ts, cli-config.yaml.example, cron/AGENTS.md, eslint.config.shared.mjs, evals/auth_pool_controls.py, evals/browser_use/single_run.py, evals/postmortem/live_ab/auth_stampede.py, evals/postmortem/live_ab/cache_concurrency_probe.py, evals/postmortem/review_probes/cache_estimator_probe.py, evals/postmortem/review_probes/credential_identity_probe.py, evals/reasoning_replay/harness.py, gateway/AGENTS.md, locales/_keys.desktop.json, locales/_keys.tui.json, nastech_cli/AGENTS.md, nastech_cli/anon_auth.py, nastech_cli/anon_auth.py, nastech_cli/anon_sign_in.py, nastech_cli/auth.py, nastech_cli/auth_codex.py, nastech_cli/auth_constants.py, nastech_cli/auth_constants.py, nastech_cli/auth_error_copy.py, nastech_cli/auth_nastech.py, nastech_cli/banner.py, nastech_cli/config_defaults.py, nastech_cli/dashboard_auth/login_page.py, nastech_cli/dashboard_register.py, nastech_cli/dashboard_register.py, nastech_cli/debug.py, nastech_cli/diagnostics_upload.py, nastech_cli/fallback_cmd.py, nastech_cli/gateway_chat_commands.py, nastech_cli/kanban_parser.py, nastech_cli/main.py, nastech_cli/main_dashboard.py, nastech_cli/main_desktop.py, nastech_cli/model_catalog.py, nastech_cli/model_setup_flows_common.py, nastech_cli/models.py, nastech_cli/models_pricing.py, nastech_cli/models_pricing.py, nastech_cli/nastech_account.py, nastech_cli/nastech_account.py, nastech_cli/nastech_billing.py, nastech_cli/nastech_billing.py, nastech_cli/observability/shared_metrics_consent.py, nastech_cli/observability/shared_metrics_send_config.py, nastech_cli/observability/shared_metrics_send_config.py, nastech_cli/plugin_catalog.py, nastech_cli/plugins_cmd.py, nastech_cli/portal_cli.py, nastech_cli/portal_cli.py, nastech_cli/providers.py, nastech_cli/proxy/adapters/base.py, nastech_cli/proxy/adapters/nastech_portal.py, nastech_cli/release_channels.py, nastech_cli/setup.py, nastech_cli/setup_platforms.py, nastech_cli/setup_quick.py, nastech_cli/skin_engine.py, nastech_cli/source_releases.py, nastech_cli/steward.py, nastech_cli/subcommands/egress.py, nastech_cli/subcommands/fallback.py, nastech_cli/subcommands/secrets.py, nastech_cli/subcommands/worktree.py, nastech_cli/telegram_managed_bot.py, nastech_cli/telegram_managed_bot.py, nastech_cli/tools_config.py, nastech_cli/uninstall.py, nastech_cli/update_cmd.py, nastech_cli/update_cmd_git.py, nastech_cli/update_cmd_maint.py, nastech_cli/update_cmd_zip.py, nastech_cli/update_downgrade_guard.py, nastech_cli/web_routers/status.py, nastech_cli/web_server_messaging.py, nastech_cli/web_server_messaging.py, nastech_cli/web_server_oauth.py, nastech_constants.py, nastech_state_common.py, nastech_state_errors.py, nastech_state_reconcile.py, optional-skills/creative/pretext/templates/donut-orbit.html, optional-skills/productivity/memento-flashcards/SKILL.md, package-lock.json, plugin-catalog/README.md, plugins/AGENTS.md, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/plugin.yaml, plugins/kanban/dashboard/dist/index.js, plugins/kanban/systemd/nastech-kanban-dispatcher.service, plugins/model-providers/ai-gateway/__init__.py, plugins/model-providers/fireworks/__init__.py, plugins/model-providers/kimi-coding/__init__.py, plugins/model-providers/nastech/__init__.py, plugins/model-providers/opencode-zen/__init__.py, plugins/model-providers/solstice/auth.py, plugins/model-providers/solstice/auth.py, plugins/nastech-achievements/dashboard/dist/index.js, plugins/platforms/discord/adapter.py, plugins/platforms/discord/onboarding.py, plugins/platforms/email/adapter.py, plugins/platforms/google_chat/adapter.py, plugins/platforms/irc/adapter.py, plugins/platforms/line/adapter.py, plugins/platforms/ntfy/adapter.py, plugins/platforms/photon/adapter.py, plugins/platforms/photon/sidecar/package-lock.json, plugins/platforms/raft/adapter.py, plugins/platforms/simplex/adapter.py, plugins/platforms/slack/adapter.py, plugins/platforms/teams/adapter.py, plugins/platforms/weixin/adapter.py, plugins/platforms/whatsapp_cloud/adapter.py, plugins/platforms/whatsapp_cloud/setup_wizard.py, plugins/web/perplexity/provider.py, pm/artifact-mirror.json, pm/network.py, pm/uv.lock, scripts/build_model_catalog.py, scripts/ci/check_catalog_cors.py, scripts/contributor_audit.py, scripts/e2e_shared_metrics_staging.py, scripts/install.cmd, scripts/install.ps1, scripts/install.sh, scripts/release.py, scripts/releases/authors_legacy.py, scripts/releases/entrypoint.py, scripts/releases/lanes.py, scripts/releases/pick_tags.py, scripts/releases/r2.py, scripts/sandbox/generate-e2e-matrix.mjs, scripts/sandbox/pick-release-tags.sh, scripts/termux/stage_apt_repo.py, scripts/tests/test-install-ps1-store-guard.ps1, scripts/whatsapp-bridge/package-lock.json, setup.py, skills/AGENTS.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/references/background-systems.md, skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md, skills/autonomous-ai-agents/nastech-agent/references/configuration.md, skills/autonomous-ai-agents/nastech-agent/references/contributor-guide.md, skills/autonomous-ai-agents/nastech-agent/references/portal-auth-for-third-party-apps.md, skills/autonomous-ai-agents/nastech-agent/references/providers-and-models.md, skills/autonomous-ai-agents/nastech-agent/references/webhooks.md, skills/media/youtube-content/SKILL.md, skills/software-development/python-debugpy/SKILL.md, tests-js/bundle-smoke-metadata.test.mjs, tests-js/update-ui.test.mjs, tests/agent/test_anthropic_adapter.py, tests/agent/test_anthropic_preserved_thinking_replay.py, tests/agent/test_anthropic_prompt_cache_policy.py, tests/agent/test_auxiliary_auth_rung_fallthrough.py, tests/agent/test_auxiliary_client.py, tests/agent/test_auxiliary_client_nastech_401_cache_key.py, tests/agent/test_auxiliary_main_first.py, tests/agent/test_auxiliary_transport_autodetect.py, tests/agent/test_billing_links.py, tests/agent/test_credential_pool.py, tests/agent/test_credential_pool_nastech_refresh_stampede.py, tests/agent/test_credits_cold_start.py, tests/agent/test_credits_policy.py, tests/agent/test_deepseek_anthropic_thinking.py, tests/agent/test_error_classifier.py, tests/agent/test_error_classifier_observed.py, tests/agent/test_fast_mode_auto.py, tests/agent/test_free_tier_rate_limit_class.py, tests/agent/test_model_metadata.py, tests/agent/test_nastech_credits_gauge.py, tests/agent/test_nastech_key_pre_expiry_adoption.py, tests/agent/test_nastech_portal_anthropic_wire.py, tests/agent/test_nastech_rate_guard.py, tests/agent/test_nastech_welcome_client_contract.py, tests/agent/test_nastech_wire_auto.py, tests/agent/test_nonretryable_result_carries_verdict.py, tests/agent/test_onboarding_first_tasks.py, tests/agent/test_primary_runtime_restore.py, tests/agent/test_provider_attribution_headers.py, tests/agent/test_provider_fallback.py, tests/agent/test_provider_history_parity.py, tests/agent/test_provider_parity.py, tests/agent/test_reasoning_replay_routes.py, tests/agent/test_run_agent.py, tests/agent/test_run_agent.py, tests/agent/test_switch_model_reapplies_headers.py, tests/agent/test_turn_usage_log_line.py, tests/agent/test_welcome_error_identity.py, tests/agent/test_welcome_tier_recovery.py, tests/agent/transports/test_chat_completions.py, tests/agent/transports/test_chat_completions_reasoning_details_replay.py, tests/agent/transports/test_provider_wire_snapshot.py, tests/compat/old_updater_dependencies.py, tests/conftest.py, tests/docker/test_sqlite_runtime.py, tests/e2e/core/live/_helpers.py, tests/e2e/core/providers/test_catalog_oauth.py, tests/e2e/core/providers/test_chat_reasoning_variants.py, tests/e2e/core/providers/test_fallback_providers.py, tests/e2e/core/upgrade/network/_seed.py, tests/e2e/core/windows/test_boot_lifecycle.py, tests/e2e/core/windows_update/_machine.py, tests/fakes/providers/chat_variants.py, tests/fakes/providers/vertex.py, tests/fixtures/prompt_surface/prompts/cli-code.claude.txt, tests/fixtures/prompt_surface/prompts/cli-code.claude.txt, tests/fixtures/prompt_surface/prompts/cli.claude.txt, tests/fixtures/prompt_surface/prompts/cli.claude.txt, tests/fixtures/prompt_surface/prompts/cli.gemini.txt, tests/fixtures/prompt_surface/prompts/cli.gemini.txt, tests/fixtures/prompt_surface/prompts/cli.gpt.txt, tests/fixtures/prompt_surface/prompts/cli.gpt.txt, tests/fixtures/prompt_surface/prompts/cli.nastech.txt, tests/fixtures/prompt_surface/prompts/cli.nastech.txt, tests/fixtures/prompt_surface/prompts/cron.claude.txt, tests/fixtures/prompt_surface/prompts/cron.claude.txt, tests/fixtures/prompt_surface/prompts/desktop.claude.txt, tests/fixtures/prompt_surface/prompts/desktop.claude.txt, tests/fixtures/prompt_surface/prompts/discord.claude.txt, tests/fixtures/prompt_surface/prompts/discord.claude.txt, tests/fixtures/prompt_surface/prompts/telegram.claude.txt, tests/fixtures/prompt_surface/prompts/telegram.claude.txt, tests/fixtures/prompt_surface/surfaces.json, tests/fixtures/provider_wire_snapshot.json, tests/gateway/fixtures/local_recovery_probe.py, tests/gateway/test_discord_format.py, tests/gateway/test_housekeeping_profile_scope.py, tests/gateway/test_internal_event_pin_wiring.py, tests/gateway/test_model_switch_persistence.py, tests/gateway/test_run_progress_topics.py, tests/gateway/test_session_model_override_persistence.py, tests/gateway/test_startup_warmup_profile_scope.py, tests/gateway/test_status_command.py, tests/gateway/test_telegram_mention_context.py, tests/gateway/test_usage_command.py, tests/install/macos-desktop-e2e.sh, tests/install/windows-e2e.ps1, tests/nastech_cli/anon_portal.py, tests/nastech_cli/test_anon_auth_core.py, tests/nastech_cli/test_anon_failure_modes.py, tests/nastech_cli/test_anon_failure_modes.py, tests/nastech_cli/test_anon_picker.py, tests/nastech_cli/test_anon_surfaces.py, tests/nastech_cli/test_anon_upgrade.py, tests/nastech_cli/test_auth_nastech_provider.py, tests/nastech_cli/test_base_url_host_identity.py, tests/nastech_cli/test_browse_schema_drift.py, tests/nastech_cli/test_cli_first_run_setup.py, tests/nastech_cli/test_cli_goal_parked_resume.py, tests/nastech_cli/test_cli_init.py, tests/nastech_cli/test_cli_provider_resolution.py, tests/nastech_cli/test_dashboard_register.py, tests/nastech_cli/test_fireworks_provider.py, tests/nastech_cli/test_gateway_chat_native.py, tests/nastech_cli/test_local_abandoned_requests.py, tests/nastech_cli/test_local_quickstart.py, tests/nastech_cli/test_main_merge_lifecycle.py, tests/nastech_cli/test_model_catalog.py, tests/nastech_cli/test_model_validation.py, tests/nastech_cli/test_nastech_anthropic_wire_default.py, tests/nastech_cli/test_nastech_auth_keepalive.py, tests/nastech_cli/test_nastech_auth_status_cache.py, tests/nastech_cli/test_nastech_inference_url_validation.py, tests/nastech_cli/test_nastech_nonproduction_inference_host.py, tests/nastech_cli/test_nastech_nonproduction_inference_host.py, tests/nastech_cli/test_nastech_portal_staging_allowlist.py, tests/nastech_cli/test_nastech_reasoning_metadata.py, tests/nastech_cli/test_proxy.py, tests/nastech_cli/test_reasoning_caps_disk_cache.py, tests/nastech_cli/test_release_channels.py, tests/nastech_cli/test_sale_pricing.py, tests/nastech_cli/test_show_config_credential.py, tests/nastech_cli/test_source_channel_integration.py, tests/nastech_cli/test_source_check.py, tests/nastech_cli/test_taskkill_identity_windows_live.py, tests/nastech_cli/test_update_target_identity.py, tests/nastech_cli/test_web_oauth_dispatch.py, tests/plugins/dashboard_auth/test_nastech_provider.py, tests/plugins/image_gen/check_parity_vs_main.py, tests/plugins/image_gen/test_openrouter_compat_provider.py, tests/plugins/test_chronos_verify.py, tests/scripts/desktop_update/test_desktop_update_windows_commit_outcome.py, tests/scripts/desktop_update/test_desktop_update_windows_marker.py, tests/scripts/desktop_update/test_desktop_update_windows_marker_lock.py, tests/scripts/test_release_build_commit.py, tests/scripts/test_release_channels.py, tests/scripts/test_release_entrypoint.py, tests/scripts/test_release_lanes.py, tests/scripts/test_release_r2.py, tests/scripts/test_release_r2.py, tests/scripts/test_stable_release.py, tests/scripts/test_stage_apt_repo.py, tests/scripts/test_upload_summary.py, tests/test_session_daemon_reaper.py, tests/tools/test_connector_wire_identity.py, tests/tools/test_delegate.py, tests/tools/test_managed_media_gateways.py, tests/tools/test_managed_tool_gateway.py, tests/tools/test_plugin_guard.py, tests/tools/test_stage2_hook_nastech_routing_env.py, tests/tools/test_strict_provider_selection.py, tests/tools/test_tts_openai_config.py, tests/tools/test_url_safety.py, tests/tools/test_web_tools_config.py, tests/tools/test_web_tools_perplexity.py, tests/tui_gateway/test_compute_host.py, tests/tui_gateway/test_connector_accounts_rpc.py, tests/tui_gateway/test_connector_operation_rpc.py, tests/tui_gateway/test_legacy_fallback_ticket_profile_verbs.py, tests/tui_gateway/test_resume_switched_provider_endpoint.py, tests/website/test_extract_skills.py, tools/AGENTS.md, tools/managed_gateway_auth.py, tools/managed_gateway_identity.py, tools/managed_tool_gateway.py, tools/mcp_oauth.py, tools/plugin_guard_context.py, tools/skills_hub_search.py, trajectory_compressor.py, ui-tui/scripts/billing-fixtures.tsx, ui-tui/src/__tests__/subscriptionCommand.test.ts, ui-tui/src/__tests__/subscriptionOverlay.test.tsx, ui-tui/src/app/slash/commands/subscription.ts, ui-tui/src/domain/paths.ts, uv.lock, web/src/components/SharedMetricsConsentBanner.tsx, web/src/components/SidebarFooter.tsx, web/src/pages/DocsPage.tsx, web/src/pages/PluginsPage.tsx, web/src/pages/SystemPage.tsx, website/README.md, website/docs/developer-guide/egress-internals.md, website/docs/developer-guide/stable-releases.md, website/docs/getting-started/installation.md, website/docs/getting-started/platform-support.md, website/docs/getting-started/quickstart.md, website/docs/getting-started/termux.md, website/docs/getting-started/termux.md, website/docs/guides/manage-nastech-cloud-with-mcp.md, website/docs/guides/run-nastech-with-nastech-portal.md, website/docs/guides/run-nemotron-3-ultra-free.md, website/docs/index.mdx, website/docs/integrations/nastech-portal.md, website/docs/integrations/providers.md, website/docs/reference/cli-commands.md, website/docs/reference/environment-variables.md, website/docs/reference/faq.md, website/docs/reference/model-catalog.md, website/docs/reference/skills-catalog.md, website/docs/user-guide/desktop.md, website/docs/user-guide/egress/iron-proxy.md, website/docs/user-guide/features/browser.md, website/docs/user-guide/features/image-generation.md, website/docs/user-guide/features/plugin-catalog.md, website/docs/user-guide/features/skills.md, website/docs/user-guide/features/subscription-proxy.md, website/docs/user-guide/features/tool-gateway.md, website/docs/user-guide/features/tools.md, website/docs/user-guide/features/tts.md, website/docs/user-guide/features/web-dashboard.md, website/docs/user-guide/features/web-search.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/skills/bundled/media/media-youtube-content.md, website/docs/user-guide/skills/bundled/software-development/software-development-python-debugpy.md, website/docs/user-guide/skills/optional/productivity/productivity-memento-flashcards.md, website/docs/user-guide/windows-native.md, website/docs/user-guide/windows-wsl-quickstart.md, website/docusaurus.config.ts, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/plugins/index.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/quickstart.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-nastech-with-nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/index.mdx, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/providers.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/faq.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/model-catalog.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/subscription-proxy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tools.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tts.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/media/media-youtube-content.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/software-development/software-development-python-debugpy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/optional/productivity/productivity-memento-flashcards.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-native.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-wsl-quickstart.md, website/scripts/check-live-search.mjs, website/scripts/extract-skills.py, website/scripts/fetch-plugin-stars.py, website/scripts/generate-llms-txt.py, website/scripts/prebuild.mjs, website/src/pages/plugins/index.tsx, website/src/pages/skills/index.tsx, website/static/api/model-catalog.json, website/static/oauth/client-metadata.json


## Direct upstream tree delta

- complete: +81 ~176 -2 ↪1
- DELETED `.github/actions/save-pm-cache/README.md`
- DELETED `.github/actions/save-pm-cache/action.yml`
- MODIFIED `.github/actions/setup-pm/action.yml`
- MODIFIED `.github/workflows/ci.yaml`
- MODIFIED `.github/workflows/desktop-bundled-release.yml`
- MODIFIED `.github/workflows/docker.yml`
- MODIFIED `.github/workflows/install-e2e-macos-run.yml`
- MODIFIED `.github/workflows/install-e2e-run.yml`
- MODIFIED `.github/workflows/install-e2e-windows-run.yml`
- MODIFIED `.github/workflows/install-e2e.yml`
- MODIFIED `.github/workflows/sandbox-image.yml`
- MODIFIED `.github/workflows/stable-release-publication.yml`
- MODIFIED `.github/workflows/stable-release.yml`
- MODIFIED `agent/display.py`
- MODIFIED `agent/image_gen_provider.py`
- MODIFIED `agent/terminal_env_provider.py`
- MODIFIED `apps/desktop/electron/channel-build-version.test.ts`
- ADDED `apps/desktop/electron/local-gateway-restart-detach.test.ts`
- MODIFIED `apps/desktop/electron/local-gateway.ts`
- MODIFIED `apps/desktop/electron/main.ts`
- ADDED `apps/desktop/scripts/mac-sign-cache.mjs`
- ADDED `apps/desktop/scripts/mac-sign-cache.test.mjs`
- MODIFIED `apps/desktop/scripts/mac-sign.mjs`
- ADDED `apps/desktop/src/app/settings/shared-metrics-settings.test.tsx`
- MODIFIED `apps/desktop/src/app/settings/shared-metrics-settings.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts`
- MODIFIED `apps/desktop/src/components/assistant-ui/tool/fallback-model/format.ts`
- MODIFIED `apps/desktop/src/components/assistant-ui/tool/fallback-model/index.ts`
- MODIFIED `apps/desktop/src/components/shared-metrics/consent-dialog.test.tsx`
- MODIFIED `apps/desktop/src/components/shared-metrics/consent-dialog.tsx`
- MODIFIED `apps/desktop/src/components/shared-metrics/consent-strip.test.tsx`
- MODIFIED `apps/desktop/src/components/shared-metrics/consent-strip.tsx`
- MODIFIED `apps/desktop/src/i18n/ar_common.ts`
- MODIFIED `apps/desktop/src/i18n/de_shared_metrics.ts`
- MODIFIED `apps/desktop/src/i18n/en_shared_metrics.ts`
- MODIFIED `apps/desktop/src/i18n/es_shared_metrics.ts`
- MODIFIED `apps/desktop/src/i18n/fr_shared_metrics.ts`
- MODIFIED `apps/desktop/src/i18n/ja_shared_metrics.ts`
- MODIFIED `apps/desktop/src/i18n/ru_shared_metrics.ts`
- MODIFIED `apps/desktop/src/i18n/types_shared_metrics.ts`
- MODIFIED `apps/desktop/src/i18n/zh-hant.ts`
- MODIFIED `apps/desktop/src/i18n/zh_shared_metrics.ts`
- MODIFIED `apps/desktop/src/store/shared-metrics.ts`
- ADDED `contributors/emails/123mikeyd@users.noreply.github.com`
- ADDED `contributors/emails/33976909+rezearcher@users.noreply.github.com`
- ADDED `contributors/emails/Ayshinko@users.noreply.github.com`
- ADDED `contributors/emails/andreyw441@gmail.com`
- ADDED `contributors/emails/anthony.holten1@gmail.com`
- ADDED `contributors/emails/arsiktech@users.noreply.github.com`
- ADDED `contributors/emails/eve.ai.ahh@gmail.com`
- ADDED `contributors/emails/hello@safeailabs.ai`
- ADDED `contributors/emails/jersilb@gmail.com`
- ADDED `contributors/emails/joshwardini@gmail.com`
- ADDED `contributors/emails/ljubomir@macbook2`
- ADDED `contributors/emails/mbgulden@gmail.com`
- ADDED `contributors/emails/mgrabina@itba.edu.ar`
- ADDED `contributors/emails/onkanat@users.noreply.github.com`
- ADDED `contributors/emails/quantbagel@gmail.com`
- ADDED `contributors/emails/santicorapollo@gmail.com`
- ADDED `contributors/emails/skk2010@users.noreply.github.com`
- ADDED `contributors/emails/thibault.jaigu@gmail.com`
- ADDED `contributors/emails/vincent.attali@deepip.ai`
- ADDED `contributors/emails/yashvt9404@gmail.com`
- ADDED `contributors/emails/yasmineali1d@outlook.com`
- ADDED `contributors/emails/yleven120@gmail.com`
- ADDED `contributors/emails/yunze7373@hotmail.com`
- MODIFIED `gateway/run_bootstrap.py`
- MODIFIED `nastech_cli/cli_modern_layout.py`
- MODIFIED `nastech_cli/config_defaults.py`
- MODIFIED `nastech_cli/gateway.py`
- MODIFIED `nastech_cli/gateway_launchd.py`
- MODIFIED `nastech_cli/gateway_runtime_start.py`
- MODIFIED `nastech_cli/gateway_supervised_restart.py`
- MODIFIED `nastech_cli/nastech_subscription.py`
- MODIFIED `nastech_cli/observability/schemas/nastech.shared_metrics.v4.schema.json`
- MODIFIED `nastech_cli/observability/shared_metrics_consent.py`
- MODIFIED `nastech_cli/observability/shared_metrics_contract.py`
- MODIFIED `nastech_cli/observability/shared_metrics_desktop.py`
- MODIFIED `nastech_cli/observability/shared_metrics_install.py`
- MODIFIED `nastech_cli/observability/shared_metrics_subscriber.py`
- MODIFIED `nastech_cli/pty_bridge.py`
- MODIFIED `nastech_cli/setup.py`
- MODIFIED `nastech_cli/subcommands/gateway.py`
- MODIFIED `nastech_cli/tools_config.py`
- MODIFIED `nastech_cli/update_restart_recovery.py`
- MODIFIED `nastech_platform/resolver/known_dirs.py`
- MODIFIED `nastech_state_messages.py`
- MODIFIED `locales/_keys.desktop.json`
- ADDED `optional-mcps/rentahuman/manifest.yaml`
- ADDED `plugin-catalog/aave-mcp.yaml`
- ADDED `plugin-catalog/abstract-provider.yaml`
- RENAMED `plugin-catalog/codex-account-switch.yaml` -> `plugin-catalog/account-switcher.yaml`
- ADDED `plugin-catalog/advisor.yaml`
- MODIFIED `plugin-catalog/agentwalletapi.yaml`
- ADDED `plugin-catalog/aistupidlevel.yaml`
- MODIFIED `plugin-catalog/alans-way-computer.yaml`
- MODIFIED `plugin-catalog/alans-way.yaml`
- ADDED `plugin-catalog/background-review-watch.yaml`
- ADDED `plugin-catalog/bharatcode-provider.yaml`
- MODIFIED `plugin-catalog/bilinc.yaml`
- MODIFIED `plugin-catalog/browserless.yaml`
- ADDED `plugin-catalog/burnclock.yaml`
- MODIFIED `plugin-catalog/claude-subscription-directsdk.yaml`
- MODIFIED `plugin-catalog/cognee.yaml`
- ADDED `plugin-catalog/cursor-acp.yaml`
- ADDED `plugin-catalog/day-panel.yaml`
- MODIFIED `plugin-catalog/deepseek-search-fetch.yaml`
- ADDED `plugin-catalog/degeneracy-guard.yaml`
- MODIFIED `plugin-catalog/diaktoros.yaml`
- ADDED `plugin-catalog/draft-cards.yaml`
- ADDED `plugin-catalog/empiriolabs-media.yaml`
- ADDED `plugin-catalog/empiriolabs.yaml`
- MODIFIED `plugin-catalog/enchanted-composer.yaml`
- MODIFIED `plugin-catalog/fish-audio.yaml`
- ADDED `plugin-catalog/game-dev.yaml`
- MODIFIED `plugin-catalog/genealogy-research-recipes.yaml`
- ADDED `plugin-catalog/git-review.yaml`
- ADDED `plugin-catalog/greyridge-token-safety.yaml`
- MODIFIED `plugin-catalog/heartbeat2.yaml`
- MODIFIED `plugin-catalog/nastech-adaptive-effort.yaml`
- ADDED `plugin-catalog/nastech-asgard.yaml`
- ADDED `plugin-catalog/nastech-board.yaml`
- ADDED `plugin-catalog/nastech-bot-hq.yaml`
- ADDED `plugin-catalog/nastech-context-overview.yaml`
- ADDED `plugin-catalog/nastech-dpapi-secrets.yaml`
- MODIFIED `plugin-catalog/nastech-dreaming.yaml`
- ADDED `plugin-catalog/nastech-kemet.yaml`
- MODIFIED `plugin-catalog/nastech-lang-pt-br.yaml`
- MODIFIED `plugin-catalog/nastech-project-stewardship.yaml`
- MODIFIED `plugin-catalog/nastech-rss.yaml`
- MODIFIED `plugin-catalog/nastech-teammates.yaml`
- ADDED `plugin-catalog/nastech-token-speed.yaml`
- ADDED `plugin-catalog/nastech-tripo.yaml`
- ADDED `plugin-catalog/nastech-wincred.yaml`
- ADDED `plugin-catalog/hermetic.yaml`
- MODIFIED `plugin-catalog/homeassistant.yaml`
- MODIFIED `plugin-catalog/hyatlas.yaml`
- MODIFIED `plugin-catalog/hydradb.yaml`
- MODIFIED `plugin-catalog/intelligent-tool-break.yaml`
- MODIFIED `plugin-catalog/jp-address.yaml`
- MODIFIED `plugin-catalog/jp-egov-law.yaml`
- MODIFIED `plugin-catalog/jp-subsidies.yaml`
- ADDED `plugin-catalog/kanban-stream.yaml`
- ADDED `plugin-catalog/llmslim.yaml`
- ADDED `plugin-catalog/mcp-plugin-creator.yaml`
- ADDED `plugin-catalog/model-picker.yaml`
- MODIFIED `plugin-catalog/node-search.yaml`
- ADDED `plugin-catalog/office-desk.yaml`
- MODIFIED `plugin-catalog/offpeak-bekci.yaml`
- ADDED `plugin-catalog/orquehelx.yaml`
- ADDED `plugin-catalog/pending-queue-monitor.yaml`
- ADDED `plugin-catalog/photofresco.yaml`
- MODIFIED `plugin-catalog/post-cortex.yaml`
- ADDED `plugin-catalog/promoat.yaml`
- ADDED `plugin-catalog/provenance-gate.yaml`
- MODIFIED `plugin-catalog/pushary.yaml`
- ADDED `plugin-catalog/reaction-ledger.yaml`
- ADDED `plugin-catalog/requesty.yaml`
- ADDED `plugin-catalog/safeailabs-provider.yaml`
- MODIFIED `plugin-catalog/spotify.yaml`
- ADDED `plugin-catalog/sunshine-moonlight.yaml`
- MODIFIED `plugin-catalog/switchbot-control.yaml`
- ADDED `plugin-catalog/tidal.yaml`
- MODIFIED `plugin-catalog/tinyfish.yaml`
- ADDED `plugin-catalog/unicode-ref.yaml`
- MODIFIED `plugin-catalog/usage-guard.yaml`
- ADDED `plugin-catalog/web-deepseek.yaml`
- ADDED `plugin-catalog/web-local.yaml`
- MODIFIED `plugin-catalog/web-search-plus.yaml`
- ADDED `plugin-catalog/wireguard.yaml`
- ADDED `plugin-catalog/world-clock.yaml`
- MODIFIED `plugin-catalog/xmemo.yaml`
- ADDED `plugin-catalog/yandex.yaml`
- ADDED `plugin-catalog/yandex_calendar.yaml`
- MODIFIED `plugins/image_gen/krea/__init__.py`
- MODIFIED `plugins/image_gen/krea/plugin.yaml`
- MODIFIED `pm/build_operations.py`
- MODIFIED `scripts/build/README.md`
- MODIFIED `scripts/bundles/desktop_toolchain.py`
- MODIFIED `scripts/bundles/native.py`
- MODIFIED `scripts/bundles/release_artifacts.py`
- MODIFIED `scripts/ci/desktop_build_cache.py`
- MODIFIED `scripts/releases/handoff.py`
- MODIFIED `scripts/releases/pick_tags.py`
- MODIFIED `scripts/releases/sequencer.py`
- MODIFIED `scripts/releases/stable.py`
- MODIFIED `scripts/releases/store.py`
- MODIFIED `scripts/sandbox/pick-release-tags.sh`
- MODIFIED `scripts/windows-build-deps.ps1`
- MODIFIED `tests-js/scripts/desktop-smoke-process.ts`
- MODIFIED `tests-js/scripts/desktop-smoke.test.ts`
- MODIFIED `tests-js/setup-pm-cache.test.mjs`
- MODIFIED `tests/ci/test_desktop_bundle_smoke.py`
- MODIFIED `tests/e2e/core/upgrade/git/test_hostile_lock.py`
- MODIFIED `tests/gateway/test_replace_ownership_guard.py`
- MODIFIED `tests/gateway/test_runner_startup_failures.py`
- MODIFIED `tests/nastech_cli/test_cli_modern_layout.py`
- MODIFIED `tests/nastech_cli/test_gateway_host_verbs.py`
- MODIFIED `tests/nastech_cli/test_gateway_restart_no_unit_linger.py`
- MODIFIED `tests/nastech_cli/test_pty_bridge.py`
- MODIFIED `tests/nastech_cli/test_relay_shared_metrics.py`
- MODIFIED `tests/nastech_cli/test_setup_telemetry.py`
- MODIFIED `tests/nastech_cli/test_shared_metrics_tools_toggle.py`
- MODIFIED `tests/nastech_cli/test_update_restart_recovery.py`
- ADDED `tests/nastech_state/test_resume_summary_carrier_once.py`
- MODIFIED `tests/install/e2e-assets/desktop-smoke.ts`
- MODIFIED `tests/install/macos-bundle-smoke.sh`
- MODIFIED `tests/install/windows-bundle-smoke.ps1`
- MODIFIED `tests/plugins/image_gen/test_krea_provider.py`
- MODIFIED `tests/scripts/test_desktop_build_cache.py`
- MODIFIED `tests/scripts/test_desktop_toolchain.py`
- ADDED `tests/scripts/test_pick_release_tags.py`
- MODIFIED `tests/scripts/test_release_artifacts.py`
- MODIFIED `tests/scripts/test_release_sequencer.py`
- MODIFIED `tests/scripts/test_release_store.py`
- MODIFIED `tests/scripts/test_release_tag_sampling.py`
- MODIFIED `tests/scripts/test_stable_release.py`
- MODIFIED `tests/scripts/test_termux_assembly_permissions.py`
- ADDED `tests/tools/test_drain_high_fd.py`
- MODIFIED `tests/tools/test_image_generate_schema.py`
- ADDED `tests/tools/test_terminal_plugin_cwd_and_streams.py`
- MODIFIED `tests/tui_gateway/test_shared_metrics_consent_rpc.py`
- MODIFIED `tests/tui_gateway/test_show_reasoning_display_gate.py`
- MODIFIED `tools/bot_desktop/placement.py`
- MODIFIED `tools/bot_desktop/runtime.py`
- MODIFIED `tools/bot_desktop/sandbox_host.py`
- MODIFIED `tools/browser_tool_session.py`
- MODIFIED `tools/environments/base_output.py`
- ADDED `tools/environments/fd_wait.py`
- MODIFIED `tools/environments/streams.py`
- MODIFIED `tools/file_tools_paths.py`
- MODIFIED `tools/image_generation_managed.py`
- MODIFIED `tools/image_generation_tool.py`
- MODIFIED `tools/process_registry.py`
- MODIFIED `tools/terminal_tool.py`
- MODIFIED `tools/terminal_tool_backends.py`
- MODIFIED `tools/terminal_tool_config.py`
- MODIFIED `tui_gateway/tool_progress.py`
- MODIFIED `web/src/components/SharedMetricsConsentBanner.tsx`
- MODIFIED `web/src/i18n/en.ts`
- MODIFIED `web/src/i18n/types.ts`
- MODIFIED `website/docs/developer-guide/image-gen-provider-plugin.md`
- MODIFIED `website/docs/developer-guide/relay-shared-metrics.md`
- MODIFIED `website/docs/developer-guide/stable-releases.md`
- MODIFIED `website/docs/developer-guide/terminal-environment-plugin.md`
- MODIFIED `website/docs/getting-started/platform-support.md`
- MODIFIED `website/docs/getting-started/quickstart.md`
- MODIFIED `website/docs/reference/cli-commands.md`
- MODIFIED `website/docs/reference/environment-variables.md`
- MODIFIED `website/docs/user-guide/bot-mode.md`
- MODIFIED `website/docs/user-guide/cli.md`
- MODIFIED `website/docs/user-guide/features/bot-screen.md`
- MODIFIED `website/docs/user-guide/features/computer-use.md`
- MODIFIED `website/docs/user-guide/features/image-generation.md`
- MODIFIED `website/docs/user-guide/features/tool-gateway.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/optional-skills-catalog.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/skills-catalog.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md`
- MODIFIED `website/sidebars.ts`
- MODIFIED `website/src/data/userStories.json`

## Scan

20732 files scanned [audio=5, binary=7, doc=4, font=13, image=165, text=20538]


## Diff

3315 renamed, 0 rewritten, 16717 identical, 158 locked, 0 missing, 20 owned, 473 reconciled


## Fork check (vs nastech-agent)

- 20470 identical, 180 updated (+0/-0 lines), 82 added, 0 missing, 0 fork-local-unpreserved, 0 stale-upstream, 0 registry-retired owned assets, 0 locked/binary, 0 collision-safe relocated, 49 preserved fork-local files, 0 violations

- features: fork 56 -> branded 56

Auto-generated by 100Ways.
