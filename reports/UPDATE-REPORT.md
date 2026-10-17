# Nastech Update Report #1

- upstream sha : `e6f57427c198cfd96854522b7a9159eb007e13c2`
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

- total files : 20215
- renamed     : 3368 (folders and file names)
- text-rewritten : 20034
- locked-copied  : 153
- binary-copied  : 8
- owned assets   : 22 (our logo/banner/mascot override upstream)

## Reconcile

- fixed : 493 files reconciled: .env.example, .github/workflows/deploy-site.yml, .github/workflows/deploy-site.yml, .github/workflows/desktop-bundle-smoke.yml, .github/workflows/docs-search-monitor.yml, .github/workflows/install-e2e-macos-run.yml, .github/workflows/install-e2e-windows-run.yml, .github/workflows/plugin-catalog-ci.yml, .github/workflows/skills-index-freshness.yml, .github/workflows/tests-os.yml, .github/workflows/tests.yml, .github/workflows/windows-install-update-e2e.yml, .mailmap, AGENTS.md, AGENTS.md, CONTRIBUTING.es.md, CONTRIBUTING.md, Dockerfile, README.es.md, README.md, README.ur-pk.md, README.zh-CN.md, SECURITY.es.md, SECURITY.es.md, SECURITY.md, SECURITY.md, agent/agent_runtime_helpers.py, agent/anthropic_adapter.py, agent/anthropic_endpoints.py, agent/auxiliary_client.py, agent/auxiliary_client.py, agent/billing_links.py, agent/billing_view.py, agent/chat_completion_helpers.py, agent/conversation_compression.py, agent/conversation_loop.py, agent/message_sanitization.py, agent/model_metadata.py, agent/onboarding_first_tasks.py, agent/prompt_builder.py, agent/proxy_sources/iron_proxy.py, agent/reasoning_params.py, agent/subscription_view.py, agent/turn_recovery.py, agent/usage_pricing.py, agent/usage_pricing.py, apps/bootstrap-installer/src-tauri/Cargo.toml, apps/desktop/README.md, apps/desktop/electron-builder.config.cjs, apps/desktop/electron/backend-health.test.ts, apps/desktop/electron/backend-health.ts, apps/desktop/electron/challenge-window.test.ts, apps/desktop/electron/cloud-session-recovery.test.ts, apps/desktop/electron/connection-config.test.ts, apps/desktop/electron/data-paths.test.ts, apps/desktop/electron/hub-iframe-policy.ts, apps/desktop/electron/oauth-partition.test.ts, apps/desktop/electron/portal-session.ts, apps/desktop/electron/remote-lifecycle.ts, apps/desktop/electron/remote-oauth-ticket.test.ts, apps/desktop/electron/updater/checkout-source.test.ts, apps/desktop/electron/window-open-policy.test.ts, apps/desktop/scripts/bundle-env.test.mjs, apps/desktop/src/app/capabilities/index.test.tsx, apps/desktop/src/app/capabilities/plugins/plugins-tab.test.tsx, apps/desktop/src/app/capabilities/skills/embedded-hub-picker.tsx, apps/desktop/src/app/chat/sidebar/section-states.tsx, apps/desktop/src/app/messaging/index.test.tsx, apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx, apps/desktop/src/app/settings/billing/api.test.ts, apps/desktop/src/app/settings/billing/dev-fixtures.ts, apps/desktop/src/app/settings/billing/errors.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.ts, apps/desktop/src/app/settings/billing/use-charge-poller.test.ts, apps/desktop/src/app/settings/billing/use-step-up.test.tsx, apps/desktop/src/app/settings/constants.ts, apps/desktop/src/app/settings/gateway-settings.test.tsx, apps/desktop/src/app/settings/gateway-settings.tsx, apps/desktop/src/app/settings/toolset-config-panel.test.tsx, apps/desktop/src/app/shell/terms-butterbar.tsx, apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts, apps/desktop/src/components/boot-failure-overlay.test.tsx, apps/desktop/src/components/boot-failure-overlay.tsx, apps/desktop/src/components/send-diagnostics-dialog.tsx, apps/desktop/src/components/update-status.tsx, apps/desktop/src/contrib/plugin.ts, apps/desktop/src/i18n/de.ts, apps/desktop/src/i18n/en.ts, apps/desktop/src/i18n/es.ts, apps/desktop/src/i18n/fr.ts, apps/desktop/src/i18n/ja.ts, apps/desktop/src/i18n/ru.ts, apps/desktop/src/i18n/zh-hant_settings.ts, apps/desktop/src/i18n/zh.ts, apps/desktop/src/lib/docs.ts, apps/desktop/src/lib/plugin-catalog.ts, apps/desktop/src/plugins/nastech-bots/skills-hub-picker.test.tsx, apps/desktop/src/plugins/nastech-bots/skills-hub.tsx, apps/desktop/src/sdk/index.ts, apps/desktop/src/store/free-tier-challenge.test.ts, apps/desktop/src/store/notifications.ts, apps/desktop/src/store/shared-metrics.ts, apps/desktop/src/themes/use-skin-command.ts, cli-config.yaml.example, eslint.config.shared.mjs, evals/auth_pool_controls.py, evals/browser_use/single_run.py, evals/postmortem/live_ab/auth_stampede.py, evals/postmortem/live_ab/cache_concurrency_probe.py, evals/postmortem/review_probes/cache_estimator_probe.py, evals/postmortem/review_probes/credential_identity_probe.py, evals/reasoning_replay/harness.py, locales/_keys.desktop.json, locales/_keys.tui.json, nastech_cli/anon_auth.py, nastech_cli/anon_auth.py, nastech_cli/anon_sign_in.py, nastech_cli/auth.py, nastech_cli/auth_codex.py, nastech_cli/auth_constants.py, nastech_cli/auth_constants.py, nastech_cli/auth_error_copy.py, nastech_cli/auth_nastech.py, nastech_cli/banner.py, nastech_cli/config_defaults.py, nastech_cli/dashboard_auth/login_page.py, nastech_cli/dashboard_register.py, nastech_cli/dashboard_register.py, nastech_cli/debug.py, nastech_cli/diagnostics_upload.py, nastech_cli/fallback_cmd.py, nastech_cli/gateway_chat_commands.py, nastech_cli/kanban_parser.py, nastech_cli/main.py, nastech_cli/main_dashboard.py, nastech_cli/main_desktop.py, nastech_cli/model_catalog.py, nastech_cli/model_setup_flows_common.py, nastech_cli/models.py, nastech_cli/models_pricing.py, nastech_cli/models_pricing.py, nastech_cli/nastech_account.py, nastech_cli/nastech_account.py, nastech_cli/nastech_billing.py, nastech_cli/nastech_billing.py, nastech_cli/observability/shared_metrics_consent.py, nastech_cli/observability/shared_metrics_send_config.py, nastech_cli/observability/shared_metrics_send_config.py, nastech_cli/plugin_catalog.py, nastech_cli/plugins_cmd.py, nastech_cli/portal_cli.py, nastech_cli/portal_cli.py, nastech_cli/providers.py, nastech_cli/proxy/adapters/base.py, nastech_cli/proxy/adapters/nastech_portal.py, nastech_cli/release_channels.py, nastech_cli/setup.py, nastech_cli/setup_platforms.py, nastech_cli/setup_quick.py, nastech_cli/skin_engine.py, nastech_cli/source_releases.py, nastech_cli/steward.py, nastech_cli/subcommands/egress.py, nastech_cli/subcommands/fallback.py, nastech_cli/subcommands/secrets.py, nastech_cli/subcommands/worktree.py, nastech_cli/telegram_managed_bot.py, nastech_cli/telegram_managed_bot.py, nastech_cli/tools_config.py, nastech_cli/uninstall.py, nastech_cli/update_cmd.py, nastech_cli/update_cmd_git.py, nastech_cli/update_cmd_maint.py, nastech_cli/update_cmd_zip.py, nastech_cli/update_downgrade_guard.py, nastech_cli/web_routers/status.py, nastech_cli/web_server_messaging.py, nastech_cli/web_server_messaging.py, nastech_cli/web_server_oauth.py, nastech_constants.py, nastech_state_common.py, nastech_state_errors.py, optional-skills/creative/pretext/templates/donut-orbit.html, optional-skills/productivity/memento-flashcards/SKILL.md, package-lock.json, plugin-catalog/README.md, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/plugin.yaml, plugins/kanban/dashboard/dist/index.js, plugins/kanban/systemd/nastech-kanban-dispatcher.service, plugins/model-providers/ai-gateway/__init__.py, plugins/model-providers/fireworks/__init__.py, plugins/model-providers/kimi-coding/__init__.py, plugins/model-providers/nastech/__init__.py, plugins/model-providers/opencode-zen/__init__.py, plugins/model-providers/solstice/auth.py, plugins/model-providers/solstice/auth.py, plugins/nastech-achievements/dashboard/dist/index.js, plugins/platforms/discord/adapter.py, plugins/platforms/discord/onboarding.py, plugins/platforms/email/adapter.py, plugins/platforms/google_chat/adapter.py, plugins/platforms/irc/adapter.py, plugins/platforms/line/adapter.py, plugins/platforms/ntfy/adapter.py, plugins/platforms/photon/adapter.py, plugins/platforms/photon/sidecar/package-lock.json, plugins/platforms/raft/adapter.py, plugins/platforms/simplex/adapter.py, plugins/platforms/slack/adapter.py, plugins/platforms/teams/adapter.py, plugins/platforms/weixin/adapter.py, plugins/platforms/whatsapp_cloud/adapter.py, plugins/platforms/whatsapp_cloud/setup_wizard.py, plugins/web/perplexity/provider.py, pm/artifact-mirror.json, pm/network.py, pm/uv.lock, scripts/build_model_catalog.py, scripts/ci/check_catalog_cors.py, scripts/contributor_audit.py, scripts/e2e_shared_metrics_staging.py, scripts/install.cmd, scripts/install.ps1, scripts/install.sh, scripts/release.py, scripts/releases/authors_legacy.py, scripts/releases/lanes.py, scripts/releases/r2.py, scripts/sandbox/generate-e2e-matrix.mjs, scripts/termux/stage_apt_repo.py, scripts/tests/test-install-ps1-store-guard.ps1, scripts/whatsapp-bridge/package-lock.json, setup.py, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/references/background-systems.md, skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md, skills/autonomous-ai-agents/nastech-agent/references/configuration.md, skills/autonomous-ai-agents/nastech-agent/references/contributor-guide.md, skills/autonomous-ai-agents/nastech-agent/references/portal-auth-for-third-party-apps.md, skills/autonomous-ai-agents/nastech-agent/references/providers-and-models.md, skills/autonomous-ai-agents/nastech-agent/references/webhooks.md, skills/media/youtube-content/SKILL.md, skills/software-development/python-debugpy/SKILL.md, tests-js/bundle-smoke-metadata.test.mjs, tests-js/update-ui.test.mjs, tests/agent/test_anthropic_adapter.py, tests/agent/test_anthropic_preserved_thinking_replay.py, tests/agent/test_anthropic_prompt_cache_policy.py, tests/agent/test_auxiliary_auth_rung_fallthrough.py, tests/agent/test_auxiliary_client.py, tests/agent/test_auxiliary_client_nastech_401_cache_key.py, tests/agent/test_auxiliary_main_first.py, tests/agent/test_auxiliary_transport_autodetect.py, tests/agent/test_billing_links.py, tests/agent/test_credential_pool.py, tests/agent/test_credential_pool_nastech_refresh_stampede.py, tests/agent/test_credits_cold_start.py, tests/agent/test_credits_policy.py, tests/agent/test_deepseek_anthropic_thinking.py, tests/agent/test_error_classifier.py, tests/agent/test_error_classifier_observed.py, tests/agent/test_fast_mode_auto.py, tests/agent/test_free_tier_rate_limit_class.py, tests/agent/test_model_metadata.py, tests/agent/test_nastech_credits_gauge.py, tests/agent/test_nastech_key_pre_expiry_adoption.py, tests/agent/test_nastech_portal_anthropic_wire.py, tests/agent/test_nastech_rate_guard.py, tests/agent/test_nastech_welcome_client_contract.py, tests/agent/test_nastech_wire_auto.py, tests/agent/test_nonretryable_result_carries_verdict.py, tests/agent/test_onboarding_first_tasks.py, tests/agent/test_primary_runtime_restore.py, tests/agent/test_provider_attribution_headers.py, tests/agent/test_provider_fallback.py, tests/agent/test_provider_history_parity.py, tests/agent/test_provider_parity.py, tests/agent/test_reasoning_replay_routes.py, tests/agent/test_run_agent.py, tests/agent/test_run_agent.py, tests/agent/test_switch_model_reapplies_headers.py, tests/agent/test_turn_usage_log_line.py, tests/agent/test_welcome_error_identity.py, tests/agent/test_welcome_tier_recovery.py, tests/agent/transports/test_chat_completions.py, tests/agent/transports/test_chat_completions_reasoning_details_replay.py, tests/agent/transports/test_provider_wire_snapshot.py, tests/compat/old_updater_dependencies.py, tests/docker/test_sqlite_runtime.py, tests/e2e/core/live/_helpers.py, tests/e2e/core/providers/test_catalog_oauth.py, tests/e2e/core/providers/test_chat_reasoning_variants.py, tests/e2e/core/providers/test_fallback_providers.py, tests/e2e/core/upgrade/network/_seed.py, tests/e2e/core/windows/test_boot_lifecycle.py, tests/e2e/core/windows_update/_machine.py, tests/fakes/providers/chat_variants.py, tests/fakes/providers/vertex.py, tests/fixtures/prompt_surface/prompts/cli-code.claude.txt, tests/fixtures/prompt_surface/prompts/cli-code.claude.txt, tests/fixtures/prompt_surface/prompts/cli.claude.txt, tests/fixtures/prompt_surface/prompts/cli.claude.txt, tests/fixtures/prompt_surface/prompts/cli.gemini.txt, tests/fixtures/prompt_surface/prompts/cli.gemini.txt, tests/fixtures/prompt_surface/prompts/cli.gpt.txt, tests/fixtures/prompt_surface/prompts/cli.gpt.txt, tests/fixtures/prompt_surface/prompts/cli.nastech.txt, tests/fixtures/prompt_surface/prompts/cli.nastech.txt, tests/fixtures/prompt_surface/prompts/cron.claude.txt, tests/fixtures/prompt_surface/prompts/cron.claude.txt, tests/fixtures/prompt_surface/prompts/desktop.claude.txt, tests/fixtures/prompt_surface/prompts/desktop.claude.txt, tests/fixtures/prompt_surface/prompts/discord.claude.txt, tests/fixtures/prompt_surface/prompts/discord.claude.txt, tests/fixtures/prompt_surface/prompts/telegram.claude.txt, tests/fixtures/prompt_surface/prompts/telegram.claude.txt, tests/fixtures/prompt_surface/surfaces.json, tests/fixtures/provider_wire_snapshot.json, tests/gateway/fixtures/local_recovery_probe.py, tests/gateway/test_discord_format.py, tests/gateway/test_housekeeping_profile_scope.py, tests/gateway/test_internal_event_pin_wiring.py, tests/gateway/test_model_switch_persistence.py, tests/gateway/test_run_progress_topics.py, tests/gateway/test_session_model_override_persistence.py, tests/gateway/test_startup_warmup_profile_scope.py, tests/gateway/test_status_command.py, tests/gateway/test_telegram_mention_context.py, tests/gateway/test_usage_command.py, tests/install/macos-desktop-e2e.sh, tests/install/windows-e2e.ps1, tests/nastech_cli/anon_portal.py, tests/nastech_cli/test_anon_auth_core.py, tests/nastech_cli/test_anon_failure_modes.py, tests/nastech_cli/test_anon_failure_modes.py, tests/nastech_cli/test_anon_picker.py, tests/nastech_cli/test_anon_surfaces.py, tests/nastech_cli/test_anon_upgrade.py, tests/nastech_cli/test_auth_nastech_provider.py, tests/nastech_cli/test_base_url_host_identity.py, tests/nastech_cli/test_cli_first_run_setup.py, tests/nastech_cli/test_cli_goal_parked_resume.py, tests/nastech_cli/test_cli_init.py, tests/nastech_cli/test_cli_provider_resolution.py, tests/nastech_cli/test_dashboard_register.py, tests/nastech_cli/test_fireworks_provider.py, tests/nastech_cli/test_gateway_chat_native.py, tests/nastech_cli/test_local_abandoned_requests.py, tests/nastech_cli/test_local_quickstart.py, tests/nastech_cli/test_main_merge_lifecycle.py, tests/nastech_cli/test_model_catalog.py, tests/nastech_cli/test_model_validation.py, tests/nastech_cli/test_nastech_anthropic_wire_default.py, tests/nastech_cli/test_nastech_auth_keepalive.py, tests/nastech_cli/test_nastech_auth_status_cache.py, tests/nastech_cli/test_nastech_inference_url_validation.py, tests/nastech_cli/test_nastech_nonproduction_inference_host.py, tests/nastech_cli/test_nastech_nonproduction_inference_host.py, tests/nastech_cli/test_nastech_portal_staging_allowlist.py, tests/nastech_cli/test_nastech_reasoning_metadata.py, tests/nastech_cli/test_proxy.py, tests/nastech_cli/test_reasoning_caps_disk_cache.py, tests/nastech_cli/test_release_channels.py, tests/nastech_cli/test_sale_pricing.py, tests/nastech_cli/test_show_config_credential.py, tests/nastech_cli/test_source_channel_integration.py, tests/nastech_cli/test_source_check.py, tests/nastech_cli/test_taskkill_identity_windows_live.py, tests/nastech_cli/test_update_target_identity.py, tests/nastech_cli/test_web_oauth_dispatch.py, tests/plugins/dashboard_auth/test_nastech_provider.py, tests/plugins/image_gen/check_parity_vs_main.py, tests/plugins/image_gen/test_openrouter_compat_provider.py, tests/plugins/test_chronos_verify.py, tests/scripts/desktop_update/test_desktop_update_windows_commit_outcome.py, tests/scripts/desktop_update/test_desktop_update_windows_marker.py, tests/scripts/desktop_update/test_desktop_update_windows_marker_lock.py, tests/scripts/test_release_build_commit.py, tests/scripts/test_release_r2.py, tests/scripts/test_release_r2.py, tests/scripts/test_stage_apt_repo.py, tests/scripts/test_upload_summary.py, tests/test_session_daemon_reaper.py, tests/tools/test_connector_wire_identity.py, tests/tools/test_delegate.py, tests/tools/test_managed_media_gateways.py, tests/tools/test_managed_tool_gateway.py, tests/tools/test_plugin_guard.py, tests/tools/test_stage2_hook_nastech_routing_env.py, tests/tools/test_strict_provider_selection.py, tests/tools/test_tts_openai_config.py, tests/tools/test_url_safety.py, tests/tools/test_web_tools_config.py, tests/tools/test_web_tools_perplexity.py, tests/tui_gateway/test_compute_host.py, tests/tui_gateway/test_connector_accounts_rpc.py, tests/tui_gateway/test_connector_operation_rpc.py, tests/tui_gateway/test_resume_switched_provider_endpoint.py, tools/managed_gateway_auth.py, tools/managed_gateway_identity.py, tools/managed_tool_gateway.py, tools/mcp_oauth.py, tools/plugin_guard_context.py, tools/skills_hub_search.py, trajectory_compressor.py, ui-tui/scripts/billing-fixtures.tsx, ui-tui/src/__tests__/subscriptionCommand.test.ts, ui-tui/src/__tests__/subscriptionOverlay.test.tsx, ui-tui/src/app/slash/commands/subscription.ts, ui-tui/src/domain/paths.ts, uv.lock, web/src/components/SharedMetricsConsentBanner.tsx, web/src/components/SidebarFooter.tsx, web/src/pages/DocsPage.tsx, web/src/pages/PluginsPage.tsx, web/src/pages/SystemPage.tsx, website/README.md, website/docs/developer-guide/egress-internals.md, website/docs/developer-guide/stable-releases.md, website/docs/getting-started/installation.md, website/docs/getting-started/platform-support.md, website/docs/getting-started/quickstart.md, website/docs/getting-started/termux.md, website/docs/getting-started/termux.md, website/docs/guides/manage-nastech-cloud-with-mcp.md, website/docs/guides/run-nastech-with-nastech-portal.md, website/docs/guides/run-nemotron-3-ultra-free.md, website/docs/index.mdx, website/docs/integrations/nastech-portal.md, website/docs/integrations/providers.md, website/docs/reference/cli-commands.md, website/docs/reference/environment-variables.md, website/docs/reference/faq.md, website/docs/reference/model-catalog.md, website/docs/reference/skills-catalog.md, website/docs/user-guide/desktop.md, website/docs/user-guide/egress/iron-proxy.md, website/docs/user-guide/features/browser.md, website/docs/user-guide/features/image-generation.md, website/docs/user-guide/features/plugin-catalog.md, website/docs/user-guide/features/skills.md, website/docs/user-guide/features/subscription-proxy.md, website/docs/user-guide/features/tool-gateway.md, website/docs/user-guide/features/tools.md, website/docs/user-guide/features/tts.md, website/docs/user-guide/features/web-dashboard.md, website/docs/user-guide/features/web-search.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/skills/bundled/media/media-youtube-content.md, website/docs/user-guide/skills/bundled/software-development/software-development-python-debugpy.md, website/docs/user-guide/skills/optional/productivity/productivity-memento-flashcards.md, website/docs/user-guide/windows-native.md, website/docs/user-guide/windows-wsl-quickstart.md, website/docusaurus.config.ts, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/plugins/index.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/quickstart.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-nastech-with-nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/index.mdx, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/providers.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/faq.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/model-catalog.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/subscription-proxy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tools.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tts.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/media/media-youtube-content.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/software-development/software-development-python-debugpy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/optional/productivity/productivity-memento-flashcards.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-native.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-wsl-quickstart.md, website/scripts/check-live-search.mjs, website/scripts/fetch-plugin-stars.py, website/scripts/generate-llms-txt.py, website/scripts/prebuild.mjs, website/src/pages/plugins/index.tsx, website/src/pages/skills/index.tsx, website/static/api/model-catalog.json, website/static/oauth/client-metadata.json


## Direct upstream tree delta

- complete: +58 ~179 -0 ↪0
- ADDED `.github/workflows/windows-desktop-attach-e2e.yml`
- MODIFIED `agent/agent_init.py`
- MODIFIED `agent/agent_runtime_helpers.py`
- MODIFIED `agent/auxiliary_client.py`
- MODIFIED `agent/credential_pool.py`
- ADDED `agent/custom_entry_pool.py`
- MODIFIED `agent/inline_tool_executors.py`
- MODIFIED `agent/interrupt_control.py`
- ADDED `agent/memory_caller_scope.py`
- ADDED `agent/memory_context.py`
- MODIFIED `agent/memory_manager.py`
- MODIFIED `agent/memory_provider.py`
- ADDED `agent/primary_runtime_snapshot.py`
- MODIFIED `agent/session_persistence.py`
- MODIFIED `agent/stream_delivery.py`
- MODIFIED `agent/tool_executor.py`
- MODIFIED `agent/turn_context.py`
- MODIFIED `agent/turn_finalizer.py`
- MODIFIED `agent/voice_turn_route.py`
- ADDED `apps/desktop/e2e/core/local-gateway-attach.spec.ts`
- ADDED `apps/desktop/e2e/core/reconnect-turn-state.spec.ts`
- MODIFIED `apps/desktop/scripts/run-electron-builder.test.mjs`
- MODIFIED `apps/desktop/src/api/canonical-deadline.test.ts`
- MODIFIED `apps/desktop/src/api/client.ts`
- MODIFIED `apps/desktop/src/app/chat/composer/discard-lost-prompt.ts`
- MODIFIED `apps/desktop/src/app/chat/composer/hooks/use-composer-queue.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/hooks/use-composer-queue.ts`
- MODIFIED `apps/desktop/src/app/chat/composer/queue-panel.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/queue-panel.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/queue-slot.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/queue-slot.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/usage.test.tsx`
- MODIFIED `apps/desktop/src/i18n/ar_session_commands.ts`
- MODIFIED `apps/desktop/src/i18n/de_session_commands.ts`
- MODIFIED `apps/desktop/src/i18n/en_session_commands.ts`
- MODIFIED `apps/desktop/src/i18n/es_session_commands.ts`
- MODIFIED `apps/desktop/src/i18n/fr_session_commands.ts`
- MODIFIED `apps/desktop/src/i18n/ja_session_commands.ts`
- MODIFIED `apps/desktop/src/i18n/ru_session_commands.ts`
- MODIFIED `apps/desktop/src/i18n/types_notices.ts`
- MODIFIED `apps/desktop/src/i18n/zh-hant_session_commands.ts`
- MODIFIED `apps/desktop/src/i18n/zh_session_commands.ts`
- MODIFIED `apps/desktop/src/store/composer-queue.ts`
- MODIFIED `apps/desktop/src/store/pending-submissions.test.ts`
- MODIFIED `apps/desktop/src/store/pending-submissions.ts`
- MODIFIED `apps/shared/src/gateway-contract.generated.ts`
- MODIFIED `apps/shared/src/gateway-contract.openrpc.json`
- MODIFIED `apps/shared/src/usage-tick.ts`
- ADDED `contributors/emails/herovivian@gmail.com`
- MODIFIED `gateway/AGENTS.md`
- MODIFIED `gateway/local_viewer_events.py`
- ADDED `gateway/parked_route_refusal.py`
- MODIFIED `gateway/platforms/api_server.py`
- MODIFIED `gateway/platforms/api_server_authority_runs.py`
- MODIFIED `gateway/platforms/api_server_openai_routes.py`
- MODIFIED `gateway/platforms/api_server_response_admissions.py`
- MODIFIED `gateway/platforms/api_server_room_dispatch.py`
- MODIFIED `gateway/platforms/api_server_runs.py`
- MODIFIED `gateway/platforms/base.py`
- MODIFIED `gateway/platforms/webhook.py`
- MODIFIED `gateway/platforms/webhook_coalesce.py`
- MODIFIED `gateway/platforms/webhook_delivery.py`
- MODIFIED `gateway/platforms/webhook_ingress.py`
- MODIFIED `gateway/profile_routing.py`
- MODIFIED `gateway/run.py`
- MODIFIED `gateway/run_api.py`
- MODIFIED `gateway/run_inbound.py`
- MODIFIED `gateway/run_profile_reconcile.py`
- MODIFIED `gateway/run_runtime.py`
- MODIFIED `gateway/run_startup.py`
- MODIFIED `gateway/run_turn.py`
- MODIFIED `gateway/run_turn_persistence.py`
- MODIFIED `gateway/run_turn_runner.py`
- MODIFIED `gateway/run_voice.py`
- MODIFIED `gateway/session_a2a.py`
- MODIFIED `gateway/session_api.py`
- MODIFIED `gateway/session_api_turn.py`
- MODIFIED `gateway/session_authorities.py`
- MODIFIED `gateway/session_authority.py`
- MODIFIED `gateway/session_bot.py`
- MODIFIED `gateway/session_busy_controls.py`
- MODIFIED `gateway/session_commands.py`
- MODIFIED `gateway/session_contract.py`
- MODIFIED `gateway/session_controls.py`
- MODIFIED `gateway/session_hosted_service.py`
- MODIFIED `gateway/session_identity.py`
- MODIFIED `gateway/session_ingress_media.py`
- ADDED `gateway/session_llm_oneshot.py`
- ADDED `gateway/session_local_adoption.py`
- MODIFIED `gateway/session_local_migration.py`
- MODIFIED `gateway/session_local_recovery.py`
- MODIFIED `gateway/session_policy.py`
- ADDED `gateway/session_queued_controls.py`
- MODIFIED `gateway/session_results.py`
- MODIFIED `gateway/session_route_identity.py`
- MODIFIED `gateway/session_settlement_recovery.py`
- MODIFIED `gateway/session_tui_ops.py`
- MODIFIED `gateway/session_usage.py`
- MODIFIED `nastech_cli/cli_chat_error_copy.py`
- MODIFIED `nastech_cli/cli_commands_mixin.py`
- MODIFIED `nastech_cli/cli_commands_session_tools.py`
- MODIFIED `nastech_cli/cli_session_mixin.py`
- MODIFIED `nastech_cli/gateway_chat_view.py`
- MODIFIED `nastech_cli/gateway_connection.py`
- MODIFIED `nastech_cli/gateway_rollback.py`
- MODIFIED `nastech_cli/gateway_runtime.py`
- MODIFIED `nastech_cli/gateway_runtime_discovery.py`
- MODIFIED `nastech_cli/runtime_provider_backends.py`
- MODIFIED `nastech_cli/runtime_provider_custom.py`
- MODIFIED `nastech_logging.py`
- MODIFIED `nastech_state_local_lineage.py`
- MODIFIED `nastech_state_local_migration.py`
- MODIFIED `nastech_state_messages.py`
- MODIFIED `nastech_state_mutation_retirement.py`
- MODIFIED `nastech_state_mutations.py`
- MODIFIED `nastech_state_portability.py`
- MODIFIED `nastech_state_runtime.py`
- MODIFIED `nastech_state_sessions.py`
- MODIFIED `nastech_state_terminal.py`
- MODIFIED `locales/_keys.desktop.json`
- MODIFIED `locales/_keys.tui.json`
- MODIFIED `locales/af.tui.yaml`
- MODIFIED `locales/ar.tui.yaml`
- MODIFIED `locales/de.tui.yaml`
- MODIFIED `locales/es.tui.yaml`
- MODIFIED `locales/fr.tui.yaml`
- MODIFIED `locales/ga.tui.yaml`
- MODIFIED `locales/hu.tui.yaml`
- MODIFIED `locales/it.tui.yaml`
- MODIFIED `locales/ja.tui.yaml`
- MODIFIED `locales/ko.tui.yaml`
- MODIFIED `locales/pt.tui.yaml`
- MODIFIED `locales/ru.tui.yaml`
- MODIFIED `locales/tr.tui.yaml`
- MODIFIED `locales/uk.tui.yaml`
- MODIFIED `locales/zh-hant.tui.yaml`
- MODIFIED `locales/zh.tui.yaml`
- MODIFIED `plugins/memory/byterover/__init__.py`
- MODIFIED `plugins/memory/retaindb/__init__.py`
- MODIFIED `plugins/platforms/google_chat/adapter.py`
- MODIFIED `scripts/build/frontend-common.mjs`
- MODIFIED `scripts/ci/classify_changes.py`
- MODIFIED `tests-js/product-builders.test.mjs`
- MODIFIED `tests/agent/test_api_content_sidecar.py`
- ADDED `tests/agent/test_aux_custom_endpoint_headers.py`
- MODIFIED `tests/agent/test_memory_context_dedupe.py`
- MODIFIED `tests/agent/test_memory_provider.py`
- ADDED `tests/agent/test_memory_provider_caller_profile.py`
- MODIFIED `tests/agent/test_primary_runtime_restore.py`
- MODIFIED `tests/agent/test_run_agent.py`
- MODIFIED `tests/agent/test_steer.py`
- MODIFIED `tests/agent/test_streaming_context_scrubber.py`
- MODIFIED `tests/agent/test_turn_finalizer_cleanup_guard.py`
- MODIFIED `tests/ci/test_classify_changes.py`
- MODIFIED `tests/e2e/core/windows_update/_machine.py`
- ADDED `tests/e2e/core/windows_update/_tokens.py`
- ADDED `tests/e2e/core/windows_update/test_upgrade_over_old_gateway.py`
- ADDED `tests/gateway/test_admission_result_reply_once.py`
- ADDED `tests/gateway/test_api_idempotency_after_delete.py`
- ADDED `tests/gateway/test_api_image_delete_scale.py`
- ADDED `tests/gateway/test_api_implicit_session_after_delete.py`
- ADDED `tests/gateway/test_api_session_create_after_delete.py`
- MODIFIED `tests/gateway/test_authority_connection.py`
- ADDED `tests/gateway/test_bot_dm_held_by_session_writer.py`
- MODIFIED `tests/gateway/test_bot_receipt_corruption.py`
- ADDED `tests/gateway/test_bot_receipt_recovery_logs.py`
- ADDED `tests/gateway/test_bot_receipt_tombstone_expiry.py`
- ADDED `tests/gateway/test_derived_generation_after_sweep.py`
- ADDED `tests/gateway/test_derived_session_after_delete.py`
- ADDED `tests/gateway/test_finite_viewer_final_send.py`
- ADDED `tests/gateway/test_legacy_session_continue_label.py`
- MODIFIED `tests/gateway/test_legacy_session_route_turn.py`
- ADDED `tests/gateway/test_legacy_stamped_bot_chat.py`
- ADDED `tests/gateway/test_local_reasoning_projection.py`
- ADDED `tests/gateway/test_local_receipt_missing_profile.py`
- ADDED `tests/gateway/test_local_receipt_untracked_compression.py`
- ADDED `tests/gateway/test_local_recovery_pre_profile_origin.py`
- ADDED `tests/gateway/test_local_viewer_reasoning.py`
- MODIFIED `tests/gateway/test_local_viewer_usage.py`
- MODIFIED `tests/gateway/test_owner_loop_writes_class.py`
- ADDED `tests/gateway/test_parked_profile_ingress.py`
- ADDED `tests/gateway/test_parked_profile_platform_refusal.py`
- ADDED `tests/gateway/test_parked_profile_rescan.py`
- ADDED `tests/gateway/test_parked_route_refusal_discord.py`
- ADDED `tests/gateway/test_parked_route_refusal_google_chat.py`
- ADDED `tests/gateway/test_parked_route_refusal_send.py`
- ADDED `tests/gateway/test_prompt_queued_controls.py`
- ADDED `tests/gateway/test_prompt_queued_transfer.py`
- ADDED `tests/gateway/test_retained_response_chain_after_delete.py`
- MODIFIED `tests/gateway/test_retired_authority_cron_fence.py`
- MODIFIED `tests/gateway/test_run_runtime_hot_serve_cleanup.py`
- ADDED `tests/gateway/test_serving_authorities.py`
- ADDED `tests/gateway/test_session_llm_oneshot.py`
- ADDED `tests/gateway/test_session_llm_oneshot_pool.py`
- MODIFIED `tests/gateway/test_session_local_reopen_on_turn.py`
- ADDED `tests/gateway/test_session_memory_review.py`
- MODIFIED `tests/gateway/test_session_policy.py`
- ADDED `tests/gateway/test_session_policy_shadowed_custom_create.py`
- MODIFIED `tests/gateway/test_session_read_commands.py`
- MODIFIED `tests/gateway/test_session_route_identity.py`
- MODIFIED `tests/gateway/test_session_tui_ops.py`
- ADDED `tests/gateway/test_session_ws_upgrade_failure_logged.py`
- ADDED `tests/gateway/test_startup_recovery_parks_profile.py`
- ADDED `tests/gateway/test_swept_bot_chat_fence.py`
- MODIFIED `tests/nastech_cli/test_cli_retry.py`
- ADDED `tests/nastech_cli/test_custom_entry_shadow_key_env.py`
- MODIFIED `tests/nastech_cli/test_gateway_agent.py`
- MODIFIED `tests/nastech_cli/test_gateway_chat_failures.py`
- MODIFIED `tests/nastech_cli/test_gateway_chat_pending_preview.py`
- MODIFIED `tests/nastech_cli/test_gateway_rollback.py`
- MODIFIED `tests/nastech_cli/test_gateway_runtime_discovery.py`
- ADDED `tests/nastech_cli/test_oneshot_streamed_live.py`
- ADDED `tests/nastech_state/test_delete_branched_root_leftovers.py`
- ADDED `tests/nastech_state/test_import_deleted_session.py`
- ADDED `tests/nastech_state/test_retired_fence_outlives_horizon.py`
- MODIFIED `tests/nastech_state/test_terminal_retirement.py`
- ADDED `tests/plugins/memory/test_provider_multiplex_contract.py`
- ADDED `tests/tui_gateway/test_rollback_restore_safe.py`
- MODIFIED `tests/tui_gateway/test_tui_gateway_server.py`
- MODIFIED `tests/tui_gateway/test_undo_command.py`
- MODIFIED `tools/bot_failure_reasons.py`
- MODIFIED `tools/bot_live_delivery.py`
- MODIFIED `tools/bot_mode_dm.py`
- MODIFIED `tools/delegate_tool_config.py`
- MODIFIED `tui_gateway/contracts/canonical_projections.py`
- MODIFIED `tui_gateway/contracts/canonical_sessions.py`
- MODIFIED `tui_gateway/contracts/events.py`
- MODIFIED `tui_gateway/contracts/tools_commands.py`
- MODIFIED `tui_gateway/methods_prompt.py`
- MODIFIED `tui_gateway/methods_tools.py`
- MODIFIED `tui_gateway/session_history.py`
- MODIFIED `ui-tui/src/__tests__/canonicalTuiOps.test.ts`
- MODIFIED `ui-tui/src/app/slash/commands/ops.ts`
- MODIFIED `ui-tui/src/gatewayTypes.ts`
- MODIFIED `ui-tui/src/i18n/en/slashCmd/ops.ts`
- MODIFIED `website/docs/developer-guide/memory-provider-plugin.md`
- MODIFIED `website/docs/user-guide/features/api-server.md`

## Scan

20264 files scanned [audio=5, binary=7, doc=4, font=13, image=161, text=20074]


## Diff

3225 renamed, 0 rewritten, 16361 identical, 154 locked, 0 missing, 20 owned, 455 reconciled


## Fork check (vs nastech-agent)

- 20025 identical, 181 updated (+0/-0 lines), 58 added, 0 missing, 0 fork-local-unpreserved, 0 stale-upstream, 0 registry-retired owned assets, 0 locked/binary, 0 collision-safe relocated, 49 preserved fork-local files, 0 violations

- features: fork 56 -> branded 56

Auto-generated by 100Ways.
