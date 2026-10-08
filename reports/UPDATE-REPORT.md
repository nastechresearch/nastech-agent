# Nastech Update Report #1

- upstream sha : `0240fa4a84123406a0e5e6e7262e5b772b43f0bd`
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

- total files : 17902
- renamed     : 3021 (folders and file names)
- text-rewritten : 17723
- locked-copied  : 139
- binary-copied  : 8
- owned assets   : 34 (our logo/banner/mascot override upstream)

## Reconcile

- fixed : 400 files reconciled: .env.example, .github/workflows/deploy-site.yml, .github/workflows/deploy-site.yml, .github/workflows/install-e2e-macos-run.yml, .github/workflows/install-e2e-windows-run.yml, .github/workflows/skills-index-freshness.yml, .mailmap, AGENTS.md, CONTRIBUTING.es.md, CONTRIBUTING.md, Dockerfile, README.es.md, README.md, README.ur-pk.md, README.zh-CN.md, SECURITY.es.md, SECURITY.md, agent/agent_runtime_helpers.py, agent/anthropic_adapter.py, agent/anthropic_endpoints.py, agent/auxiliary_client.py, agent/billing_links.py, agent/billing_view.py, agent/chat_completion_helpers.py, agent/conversation_compression.py, agent/conversation_loop.py, agent/model_metadata.py, agent/prompt_builder.py, agent/proxy_sources/iron_proxy.py, agent/reasoning_params.py, agent/subscription_view.py, agent/turn_recovery.py, agent/usage_pricing.py, apps/bootstrap-installer/src-tauri/Cargo.toml, apps/desktop/README.md, apps/desktop/electron-builder.config.cjs, apps/desktop/electron/backend-health.test.ts, apps/desktop/electron/backend-health.ts, apps/desktop/electron/challenge-window.test.ts, apps/desktop/electron/cloud-session-recovery.test.ts, apps/desktop/electron/connection-config.test.ts, apps/desktop/electron/hub-iframe-policy.ts, apps/desktop/electron/oauth-partition.test.ts, apps/desktop/electron/portal-session.ts, apps/desktop/electron/remote-lifecycle.ts, apps/desktop/electron/remote-oauth-ticket.test.ts, apps/desktop/electron/updater/checkout-source.test.ts, apps/desktop/electron/window-open-policy.test.ts, apps/desktop/src/app/capabilities/index.test.tsx, apps/desktop/src/app/capabilities/plugins/plugins-tab.test.tsx, apps/desktop/src/app/capabilities/skills/embedded-hub-picker.tsx, apps/desktop/src/app/chat/sidebar/section-states.tsx, apps/desktop/src/app/messaging/index.test.tsx, apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx, apps/desktop/src/app/settings/billing/api.test.ts, apps/desktop/src/app/settings/billing/dev-fixtures.ts, apps/desktop/src/app/settings/billing/errors.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.ts, apps/desktop/src/app/settings/billing/use-charge-poller.test.ts, apps/desktop/src/app/settings/billing/use-step-up.test.tsx, apps/desktop/src/app/settings/constants.ts, apps/desktop/src/app/settings/gateway-settings.test.tsx, apps/desktop/src/app/settings/gateway-settings.tsx, apps/desktop/src/app/settings/toolset-config-panel.test.tsx, apps/desktop/src/app/shell/terms-butterbar.tsx, apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts, apps/desktop/src/components/boot-failure-overlay.test.tsx, apps/desktop/src/components/boot-failure-overlay.tsx, apps/desktop/src/components/send-diagnostics-dialog.tsx, apps/desktop/src/components/update-status.tsx, apps/desktop/src/contrib/plugin.ts, apps/desktop/src/i18n/de.ts, apps/desktop/src/i18n/en.ts, apps/desktop/src/i18n/es.ts, apps/desktop/src/i18n/fr.ts, apps/desktop/src/i18n/ja.ts, apps/desktop/src/i18n/ru.ts, apps/desktop/src/i18n/zh-hant_settings.ts, apps/desktop/src/i18n/zh.ts, apps/desktop/src/lib/docs.ts, apps/desktop/src/lib/plugin-catalog.ts, apps/desktop/src/plugins/nastech-bots/skills-hub-picker.test.tsx, apps/desktop/src/plugins/nastech-bots/skills-hub.tsx, apps/desktop/src/sdk/index.ts, apps/desktop/src/store/free-tier-challenge.test.ts, apps/desktop/src/store/shared-metrics.ts, cli-config.yaml.example, eslint.config.shared.mjs, evals/auth_pool_controls.py, evals/browser_use/single_run.py, evals/postmortem/live_ab/auth_stampede.py, evals/postmortem/live_ab/cache_concurrency_probe.py, evals/postmortem/review_probes/cache_estimator_probe.py, evals/postmortem/review_probes/credential_identity_probe.py, nastech_cli/anon_auth.py, nastech_cli/anon_auth.py, nastech_cli/anon_sign_in.py, nastech_cli/auth.py, nastech_cli/auth_codex.py, nastech_cli/auth_constants.py, nastech_cli/auth_error_copy.py, nastech_cli/auth_nastech.py, nastech_cli/banner.py, nastech_cli/config_defaults.py, nastech_cli/dashboard_auth/login_page.py, nastech_cli/dashboard_register.py, nastech_cli/debug.py, nastech_cli/diagnostics_upload.py, nastech_cli/fallback_cmd.py, nastech_cli/kanban_parser.py, nastech_cli/main.py, nastech_cli/main_dashboard.py, nastech_cli/main_desktop.py, nastech_cli/model_catalog.py, nastech_cli/model_setup_flows_common.py, nastech_cli/models.py, nastech_cli/models_pricing.py, nastech_cli/nastech_account.py, nastech_cli/nastech_account.py, nastech_cli/nastech_billing.py, nastech_cli/observability/shared_metrics_consent.py, nastech_cli/observability/shared_metrics_send_config.py, nastech_cli/plugin_catalog.py, nastech_cli/plugins_cmd.py, nastech_cli/portal_cli.py, nastech_cli/providers.py, nastech_cli/proxy/adapters/base.py, nastech_cli/proxy/adapters/nastech_portal.py, nastech_cli/setup.py, nastech_cli/setup_platforms.py, nastech_cli/setup_quick.py, nastech_cli/setup_whatsapp_cloud.py, nastech_cli/skin_engine.py, nastech_cli/source_releases.py, nastech_cli/steward.py, nastech_cli/subcommands/egress.py, nastech_cli/subcommands/fallback.py, nastech_cli/subcommands/secrets.py, nastech_cli/subcommands/worktree.py, nastech_cli/telegram_managed_bot.py, nastech_cli/tools_config.py, nastech_cli/uninstall.py, nastech_cli/update_cmd.py, nastech_cli/update_cmd_maint.py, nastech_cli/update_cmd_zip.py, nastech_cli/web_routers/status.py, nastech_cli/web_server_messaging.py, nastech_cli/web_server_oauth.py, nastech_constants.py, nastech_state_errors.py, optional-skills/productivity/memento-flashcards/SKILL.md, package-lock.json, plugin-catalog/README.md, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/plugin.yaml, plugins/kanban/dashboard/dist/index.js, plugins/kanban/systemd/nastech-kanban-dispatcher.service, plugins/model-providers/ai-gateway/__init__.py, plugins/model-providers/fireworks/__init__.py, plugins/model-providers/kimi-coding/__init__.py, plugins/model-providers/nastech/__init__.py, plugins/model-providers/opencode-zen/__init__.py, plugins/model-providers/solstice/auth.py, plugins/nastech-achievements/dashboard/dist/index.js, plugins/platforms/discord/adapter.py, plugins/platforms/discord/onboarding.py, plugins/platforms/email/adapter.py, plugins/platforms/photon/sidecar/package-lock.json, plugins/platforms/slack/adapter.py, plugins/web/perplexity/provider.py, pm/artifact-mirror.json, pm/uv.lock, scripts/build_model_catalog.py, scripts/contributor_audit.py, scripts/e2e_shared_metrics_staging.py, scripts/install.cmd, scripts/install.ps1, scripts/install.sh, scripts/release.py, scripts/releases/authors_legacy.py, scripts/releases/r2.py, scripts/sandbox/generate-e2e-matrix.mjs, scripts/termux/stage_apt_repo.py, scripts/whatsapp-bridge/package-lock.json, setup.py, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/references/background-systems.md, skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md, skills/autonomous-ai-agents/nastech-agent/references/configuration.md, skills/autonomous-ai-agents/nastech-agent/references/contributor-guide.md, skills/autonomous-ai-agents/nastech-agent/references/portal-auth-for-third-party-apps.md, skills/autonomous-ai-agents/nastech-agent/references/providers-and-models.md, skills/autonomous-ai-agents/nastech-agent/references/webhooks.md, skills/media/youtube-content/SKILL.md, skills/software-development/python-debugpy/SKILL.md, tests/agent/test_anthropic_adapter.py, tests/agent/test_anthropic_preserved_thinking_replay.py, tests/agent/test_anthropic_prompt_cache_policy.py, tests/agent/test_auxiliary_auth_rung_fallthrough.py, tests/agent/test_auxiliary_client.py, tests/agent/test_auxiliary_client_nastech_401_cache_key.py, tests/agent/test_auxiliary_main_first.py, tests/agent/test_auxiliary_transport_autodetect.py, tests/agent/test_billing_links.py, tests/agent/test_credential_pool.py, tests/agent/test_credential_pool_nastech_refresh_stampede.py, tests/agent/test_credits_cold_start.py, tests/agent/test_credits_policy.py, tests/agent/test_deepseek_anthropic_thinking.py, tests/agent/test_error_classifier.py, tests/agent/test_error_classifier_observed.py, tests/agent/test_fast_mode_auto.py, tests/agent/test_free_tier_rate_limit_class.py, tests/agent/test_model_metadata.py, tests/agent/test_nastech_credits_gauge.py, tests/agent/test_nastech_key_pre_expiry_adoption.py, tests/agent/test_nastech_portal_anthropic_wire.py, tests/agent/test_nastech_rate_guard.py, tests/agent/test_nastech_welcome_client_contract.py, tests/agent/test_nastech_wire_auto.py, tests/agent/test_nonretryable_result_carries_verdict.py, tests/agent/test_primary_runtime_restore.py, tests/agent/test_provider_attribution_headers.py, tests/agent/test_provider_fallback.py, tests/agent/test_provider_history_parity.py, tests/agent/test_provider_parity.py, tests/agent/test_run_agent.py, tests/agent/test_switch_model_reapplies_headers.py, tests/agent/test_turn_usage_log_line.py, tests/agent/test_welcome_error_identity.py, tests/agent/test_welcome_tier_recovery.py, tests/agent/transports/test_chat_completions.py, tests/agent/transports/test_chat_completions_reasoning_details_replay.py, tests/agent/transports/test_provider_wire_snapshot.py, tests/compat/old_updater_dependencies.py, tests/docker/test_sqlite_runtime.py, tests/e2e/core/live/_helpers.py, tests/e2e/core/providers/test_catalog_oauth.py, tests/e2e/core/providers/test_chat_reasoning_variants.py, tests/e2e/core/providers/test_fallback_providers.py, tests/e2e/core/upgrade/network/_seed.py, tests/e2e/core/upgrade/network/test_proxy_only_egress.py, tests/e2e/core/upgrade/network/test_release_channel_records.py, tests/fakes/providers/chat_variants.py, tests/fixtures/provider_wire_snapshot.json, tests/gateway/test_discord_format.py, tests/gateway/test_free_tier_startup_notice.py, tests/gateway/test_housekeeping_profile_scope.py, tests/gateway/test_internal_event_pin_wiring.py, tests/gateway/test_model_switch_persistence.py, tests/gateway/test_run_progress_topics.py, tests/gateway/test_session_model_override_persistence.py, tests/gateway/test_startup_warmup_profile_scope.py, tests/gateway/test_status_command.py, tests/gateway/test_status_free_tier_line.py, tests/gateway/test_telegram_mention_context.py, tests/gateway/test_usage_command.py, tests/install/macos-desktop-e2e.sh, tests/install/windows-e2e.ps1, tests/nastech_cli/anon_portal.py, tests/nastech_cli/test_anon_auth_core.py, tests/nastech_cli/test_anon_failure_modes.py, tests/nastech_cli/test_anon_failure_modes.py, tests/nastech_cli/test_anon_first_notice.py, tests/nastech_cli/test_anon_picker.py, tests/nastech_cli/test_anon_surfaces.py, tests/nastech_cli/test_anon_upgrade.py, tests/nastech_cli/test_auth_nastech_provider.py, tests/nastech_cli/test_base_url_host_identity.py, tests/nastech_cli/test_cli_first_run_setup.py, tests/nastech_cli/test_cli_init.py, tests/nastech_cli/test_cli_provider_resolution.py, tests/nastech_cli/test_dashboard_register.py, tests/nastech_cli/test_fireworks_provider.py, tests/nastech_cli/test_local_abandoned_requests.py, tests/nastech_cli/test_local_quickstart.py, tests/nastech_cli/test_model_catalog.py, tests/nastech_cli/test_model_validation.py, tests/nastech_cli/test_nastech_anthropic_wire_default.py, tests/nastech_cli/test_nastech_auth_keepalive.py, tests/nastech_cli/test_nastech_auth_status_cache.py, tests/nastech_cli/test_nastech_inference_url_validation.py, tests/nastech_cli/test_nastech_nonproduction_inference_host.py, tests/nastech_cli/test_nastech_nonproduction_inference_host.py, tests/nastech_cli/test_nastech_portal_staging_allowlist.py, tests/nastech_cli/test_nastech_reasoning_metadata.py, tests/nastech_cli/test_proxy.py, tests/nastech_cli/test_reasoning_caps_disk_cache.py, tests/nastech_cli/test_sale_pricing.py, tests/nastech_cli/test_show_config_credential.py, tests/nastech_cli/test_source_channel_integration.py, tests/nastech_cli/test_source_check.py, tests/nastech_cli/test_update_target_identity.py, tests/nastech_cli/test_web_oauth_dispatch.py, tests/plugins/dashboard_auth/test_nastech_provider.py, tests/plugins/image_gen/check_parity_vs_main.py, tests/plugins/image_gen/test_openrouter_compat_provider.py, tests/plugins/test_chronos_verify.py, tests/scripts/test_release_build_commit.py, tests/scripts/test_release_r2.py, tests/scripts/test_release_r2.py, tests/scripts/test_stage_apt_repo.py, tests/scripts/test_upload_summary.py, tests/tools/test_delegate.py, tests/tools/test_managed_media_gateways.py, tests/tools/test_managed_tool_gateway.py, tests/tools/test_stage2_hook_nastech_routing_env.py, tests/tools/test_strict_provider_selection.py, tests/tools/test_tts_openai_config.py, tests/tools/test_url_safety.py, tests/tools/test_web_tools_config.py, tests/tools/test_web_tools_perplexity.py, tests/tui_gateway/test_free_tier_rpc.py, tests/tui_gateway/test_resume_switched_provider_endpoint.py, tools/managed_gateway_auth.py, tools/managed_tool_gateway.py, tools/mcp_oauth.py, tools/skills_hub_search.py, trajectory_compressor.py, ui-tui/scripts/billing-fixtures.tsx, ui-tui/src/__tests__/subscriptionCommand.test.ts, ui-tui/src/__tests__/subscriptionOverlay.test.tsx, ui-tui/src/app/slash/commands/subscription.ts, ui-tui/src/domain/paths.ts, uv.lock, web/src/components/SharedMetricsConsentBanner.tsx, web/src/components/SidebarFooter.tsx, web/src/pages/DocsPage.tsx, web/src/pages/PluginsPage.tsx, web/src/pages/SystemPage.tsx, website/README.md, website/docs/developer-guide/egress-internals.md, website/docs/developer-guide/stable-releases.md, website/docs/getting-started/installation.md, website/docs/getting-started/platform-support.md, website/docs/getting-started/quickstart.md, website/docs/getting-started/termux.md, website/docs/guides/manage-nastech-cloud-with-mcp.md, website/docs/guides/run-nastech-with-nastech-portal.md, website/docs/guides/run-nemotron-3-ultra-free.md, website/docs/index.mdx, website/docs/integrations/nastech-portal.md, website/docs/integrations/providers.md, website/docs/reference/cli-commands.md, website/docs/reference/environment-variables.md, website/docs/reference/faq.md, website/docs/reference/model-catalog.md, website/docs/user-guide/desktop.md, website/docs/user-guide/egress/iron-proxy.md, website/docs/user-guide/features/browser.md, website/docs/user-guide/features/image-generation.md, website/docs/user-guide/features/plugin-catalog.md, website/docs/user-guide/features/skills.md, website/docs/user-guide/features/subscription-proxy.md, website/docs/user-guide/features/tool-gateway.md, website/docs/user-guide/features/tools.md, website/docs/user-guide/features/tts.md, website/docs/user-guide/features/web-dashboard.md, website/docs/user-guide/features/web-search.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/skills/bundled/media/media-youtube-content.md, website/docs/user-guide/skills/bundled/software-development/software-development-python-debugpy.md, website/docs/user-guide/skills/optional/productivity/productivity-memento-flashcards.md, website/docs/user-guide/windows-native.md, website/docs/user-guide/windows-wsl-quickstart.md, website/docusaurus.config.ts, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/plugins/index.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/quickstart.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-nastech-with-nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/index.mdx, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/providers.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/faq.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/model-catalog.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/subscription-proxy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tools.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tts.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/media/media-youtube-content.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/software-development/software-development-python-debugpy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/optional/productivity/productivity-memento-flashcards.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-native.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-wsl-quickstart.md, website/scripts/fetch-plugin-stars.py, website/scripts/generate-llms-txt.py, website/scripts/prebuild.mjs, website/src/pages/plugins/index.tsx, website/src/pages/skills/index.tsx, website/static/api/model-catalog.json, website/static/oauth/client-metadata.json


## Direct upstream tree delta

- complete: +81 ~310 -27 ↪0
- MODIFIED `.github/workflows/nix.yml`
- MODIFIED `agent/AGENTS.md`
- MODIFIED `agent/agent_init.py`
- MODIFIED `agent/conversation_compression.py`
- MODIFIED `agent/conversation_loop.py`
- MODIFIED `agent/error_classifier.py`
- ADDED `agent/first_task_prompt.py`
- ADDED `agent/initiate_setup_facts.py`
- ADDED `agent/initiate_setup_prompt.py`
- MODIFIED `agent/inline_tool_executors.py`
- MODIFIED `agent/interrupt_control.py`
- MODIFIED `agent/message_sanitization.py`
- MODIFIED `agent/nastech_rate_guard.py`
- MODIFIED `agent/onboarding.py`
- MODIFIED `agent/prompt_builder.py`
- MODIFIED `agent/skill_commands.py`
- MODIFIED `agent/tool_dispatch_helpers.py`
- MODIFIED `agent/turn_context.py`
- MODIFIED `agent/turn_facade.py`
- ADDED `agent/turn_scripted_prelude.py`
- MODIFIED `agent/turn_tool_validation.py`
- MODIFIED `agent/voice_turn_route.py`
- MODIFIED `apps/desktop/BUILDING.md`
- ADDED `apps/desktop/e2e/core/no-idle-reap.spec.ts`
- DELETED `apps/desktop/electron/chat-onboarding-window.ts`
- MODIFIED `apps/desktop/electron/link-title-window.test.ts`
- MODIFIED `apps/desktop/electron/main.ts`
- MODIFIED `apps/desktop/electron/pool-retire.test.ts`
- MODIFIED `apps/desktop/electron/pool-retire.ts`
- MODIFIED `apps/desktop/electron/preload.ts`
- MODIFIED `apps/desktop/electron/profile-migration.ts`
- MODIFIED `apps/desktop/electron/updater/relaunch-waiter-lifecycle.test.ts`
- MODIFIED `apps/desktop/electron/updater/relaunch-waiter.ts`
- MODIFIED `apps/desktop/electron/updater/relaunch-waiter.windows-live.test.ts`
- MODIFIED `apps/desktop/electron/window-focus-policy.ts`
- ADDED `apps/desktop/electron/window-growth.test.ts`
- MODIFIED `apps/desktop/electron/window-growth.ts`
- ADDED `apps/desktop/electron/window-size-types.ts`
- MODIFIED `apps/desktop/electron/window-state.ts`
- MODIFIED `apps/desktop/scripts/store-package-version.test.mjs`
- MODIFIED `apps/desktop/scripts/update-relaunch-waiter.ps1`
- MODIFIED `apps/desktop/src/api/mcp.ts`
- MODIFIED `apps/desktop/src/app/chat/built-in-tour.ts`
- ADDED `apps/desktop/src/app/chat/chat-surface-state.ts`
- MODIFIED `apps/desktop/src/app/chat/composer/hooks/use-composer-submit.ts`
- ADDED `apps/desktop/src/app/chat/composer/hooks/use-middleware-submit.ts`
- MODIFIED `apps/desktop/src/app/chat/composer/index.tsx`
- ADDED `apps/desktop/src/app/chat/composer/local-setup-card.test.tsx`
- ADDED `apps/desktop/src/app/chat/composer/local-setup-card.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/model-pill.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/status-stack/index.tsx`
- MODIFIED `apps/desktop/src/app/chat/index.tsx`
- ADDED `apps/desktop/src/app/chat/use-chat-bar-state.ts`
- MODIFIED `apps/desktop/src/app/command-palette/index.tsx`
- MODIFIED `apps/desktop/src/app/contrib/controller.tsx`
- DELETED `apps/desktop/src/app/contrib/handoff-leg.ts`
- DELETED `apps/desktop/src/app/contrib/handoff-receipt.ts`
- ADDED `apps/desktop/src/app/contrib/hooks/desktop-onboarding-metrics.test.ts`
- MODIFIED `apps/desktop/src/app/contrib/hooks/desktop-onboarding-metrics.ts`
- MODIFIED `apps/desktop/src/app/contrib/layout-presets.ts`
- DELETED `apps/desktop/src/app/contrib/onboarding-handoff.ts`
- ADDED `apps/desktop/src/app/contrib/onboarding-kickoff-machine.ts`
- MODIFIED `apps/desktop/src/app/contrib/onboarding-kickoff.ts`
- MODIFIED `apps/desktop/src/app/contrib/surfaces.tsx`
- ADDED `apps/desktop/src/app/contrib/wiring-effects.ts`
- MODIFIED `apps/desktop/src/app/contrib/wiring.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/gateway-event/message-stream.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/gateway-event/server-requests.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/gateway-event/tools.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/slash.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-session-actions/branch-create-key.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-actions/index.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-actions/restore-pending-clarify.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-actions/transcript-provenance.ts`
- MODIFIED `apps/desktop/src/app/settings/config-settings.tsx`
- ADDED `apps/desktop/src/app/settings/developer-settings.tsx`
- MODIFIED `apps/desktop/src/app/settings/local-models-settings.tsx`
- MODIFIED `apps/desktop/src/app/settings/model-settings.tsx`
- MODIFIED `apps/desktop/src/app/settings/pool-limits-setting.tsx`
- MODIFIED `apps/desktop/src/app/shell/hooks/use-status-snapshot.ts`
- ADDED `apps/desktop/src/app/shell/local-setup-menu-row.tsx`
- MODIFIED `apps/desktop/src/app/shell/model-catalog-menu.tsx`
- MODIFIED `apps/desktop/src/app/shell/model-menu-panel.tsx`
- ADDED `apps/desktop/src/app/shell/terms-butterbar.tsx`
- DELETED `apps/desktop/src/components/assistant-ui/ask-directive.tsx`
- ADDED `apps/desktop/src/components/assistant-ui/clarify/core/confirm-bar.tsx`
- ADDED `apps/desktop/src/components/assistant-ui/clarify/core/use-clarify-keys-handlers.ts`
- MODIFIED `apps/desktop/src/components/assistant-ui/clarify/core/use-clarify-keys.ts`
- MODIFIED `apps/desktop/src/components/assistant-ui/clarify/index.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/clarify/parse.ts`
- MODIFIED `apps/desktop/src/components/assistant-ui/clarify/pending.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/clarify/settled.tsx`
- ADDED `apps/desktop/src/components/assistant-ui/clarify/setup-pending-parts.tsx`
- ADDED `apps/desktop/src/components/assistant-ui/clarify/setup-pending.test.tsx`
- ADDED `apps/desktop/src/components/assistant-ui/clarify/setup-pending.tsx`
- ADDED `apps/desktop/src/components/assistant-ui/clarify/setup-pickers.tsx`
- ADDED `apps/desktop/src/components/assistant-ui/clarify/setup-rows.ts`
- ADDED `apps/desktop/src/components/assistant-ui/clarify/setup-settled.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/markdown-text.tsx`
- ADDED `apps/desktop/src/components/assistant-ui/start-chat-tool-parts.tsx`
- ADDED `apps/desktop/src/components/assistant-ui/start-chat-tool.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/assistant-message.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/index.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/list.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/message-parts.tsx`
- ADDED `apps/desktop/src/components/assistant-ui/thread/setup-learned.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/status.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/turn-activity.ts`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/user-message.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/tool/fallback-model/index.ts`
- MODIFIED `apps/desktop/src/components/free-tier/sign-in-dialog.test.tsx`
- MODIFIED `apps/desktop/src/components/free-tier/sign-in-dialog.tsx`
- MODIFIED `apps/desktop/src/components/gateway-connecting-overlay.tsx`
- MODIFIED `apps/desktop/src/components/model-picker.tsx`
- MODIFIED `apps/desktop/src/components/notifications.tsx`
- MODIFIED `apps/desktop/src/components/onboarding-chat/assembly.ts`
- DELETED `apps/desktop/src/components/onboarding-chat/cards/build.tsx`
- DELETED `apps/desktop/src/components/onboarding-chat/cards/frame.tsx`
- DELETED `apps/desktop/src/components/onboarding-chat/cards/setup.tsx`
- DELETED `apps/desktop/src/components/onboarding-chat/directive.tsx`
- DELETED `apps/desktop/src/components/onboarding-chat/first-build.ts`
- ADDED `apps/desktop/src/components/onboarding-chat/gate.test.tsx`
- MODIFIED `apps/desktop/src/components/onboarding-chat/gate.tsx`
- DELETED `apps/desktop/src/components/onboarding-chat/guide-loading.css`
- DELETED `apps/desktop/src/components/onboarding-chat/guide-loading.tsx`
- ADDED `apps/desktop/src/components/onboarding-chat/intro-copy.css`
- ADDED `apps/desktop/src/components/onboarding-chat/intro-copy.tsx`
- ADDED `apps/desktop/src/components/onboarding-chat/intro.test.ts`
- ADDED `apps/desktop/src/components/onboarding-chat/intro.ts`
- MODIFIED `apps/desktop/src/components/onboarding-chat/options.tsx`
- DELETED `apps/desktop/src/components/onboarding-chat/persisted-handoff.ts`
- DELETED `apps/desktop/src/components/onboarding-chat/setup-profile.ts`
- ADDED `apps/desktop/src/components/onboarding-chat/setup-session.ts`
- MODIFIED `apps/desktop/src/components/onboarding-chat/signpost.ts`
- MODIFIED `apps/desktop/src/components/onboarding-chat/skip.tsx`
- MODIFIED `apps/desktop/src/components/pane-shell/tree/presets.ts`
- MODIFIED `apps/desktop/src/components/pane-shell/tree/renderer/narrow-overlays.tsx`
- MODIFIED `apps/desktop/src/components/shared-metrics/consent-dialog.tsx`
- MODIFIED `apps/desktop/src/components/tips/local-runtime-update-offer.ts`
- DELETED `apps/desktop/src/components/tips/local-setup-offer.test.ts`
- DELETED `apps/desktop/src/components/tips/local-setup-offer.ts`
- MODIFIED `apps/desktop/src/components/tips/tutorial-lifetime.test.tsx`
- MODIFIED `apps/desktop/src/components/tips/use-tip-rotation.test.tsx`
- MODIFIED `apps/desktop/src/components/tips/use-tip-rotation.ts`
- MODIFIED `apps/desktop/src/global.d.ts`
- MODIFIED `apps/desktop/src/hooks/use-media-image.frames.test.tsx`
- MODIFIED `apps/desktop/src/hooks/use-mobile.ts`
- MODIFIED `apps/desktop/src/i18n/ar.ts`
- MODIFIED `apps/desktop/src/i18n/ar_assistant.ts`
- MODIFIED `apps/desktop/src/i18n/ar_boot.ts`
- MODIFIED `apps/desktop/src/i18n/ar_chat.ts`
- MODIFIED `apps/desktop/src/i18n/ar_chrome.ts`
- MODIFIED `apps/desktop/src/i18n/ar_command_center.ts`
- MODIFIED `apps/desktop/src/i18n/ar_common.ts`
- MODIFIED `apps/desktop/src/i18n/ar_settings.ts`
- MODIFIED `apps/desktop/src/i18n/de.ts`
- MODIFIED `apps/desktop/src/i18n/de_model_menu.ts`
- MODIFIED `apps/desktop/src/i18n/de_notices.ts`
- ADDED `apps/desktop/src/i18n/de_onboarding.ts`
- MODIFIED `apps/desktop/src/i18n/de_shared_metrics.ts`
- MODIFIED `apps/desktop/src/i18n/en.ts`
- MODIFIED `apps/desktop/src/i18n/en_app_tour.ts`
- MODIFIED `apps/desktop/src/i18n/en_model_menu.ts`
- MODIFIED `apps/desktop/src/i18n/en_notices.ts`
- ADDED `apps/desktop/src/i18n/en_onboarding.ts`
- MODIFIED `apps/desktop/src/i18n/en_shared_metrics.ts`
- MODIFIED `apps/desktop/src/i18n/es.ts`
- MODIFIED `apps/desktop/src/i18n/es_model_menu.ts`
- MODIFIED `apps/desktop/src/i18n/es_notices.ts`
- ADDED `apps/desktop/src/i18n/es_onboarding.ts`
- MODIFIED `apps/desktop/src/i18n/es_shared_metrics.ts`
- MODIFIED `apps/desktop/src/i18n/fr.ts`
- MODIFIED `apps/desktop/src/i18n/fr_model_menu.ts`
- MODIFIED `apps/desktop/src/i18n/fr_notices.ts`
- ADDED `apps/desktop/src/i18n/fr_onboarding.ts`
- MODIFIED `apps/desktop/src/i18n/fr_shared_metrics.ts`
- MODIFIED `apps/desktop/src/i18n/ja.ts`
- MODIFIED `apps/desktop/src/i18n/ja_model_menu.ts`
- MODIFIED `apps/desktop/src/i18n/ja_notices.ts`
- ADDED `apps/desktop/src/i18n/ja_onboarding.ts`
- MODIFIED `apps/desktop/src/i18n/ja_shared_metrics.ts`
- ADDED `apps/desktop/src/i18n/overlay-completeness.test.ts`
- ADDED `apps/desktop/src/i18n/overlay-gaps.json`
- MODIFIED `apps/desktop/src/i18n/ru.ts`
- MODIFIED `apps/desktop/src/i18n/ru_model_menu.ts`
- MODIFIED `apps/desktop/src/i18n/ru_notices.ts`
- ADDED `apps/desktop/src/i18n/ru_onboarding.ts`
- MODIFIED `apps/desktop/src/i18n/ru_shared_metrics.ts`
- MODIFIED `apps/desktop/src/i18n/types.ts`
- MODIFIED `apps/desktop/src/i18n/types_app_tour.ts`
- MODIFIED `apps/desktop/src/i18n/types_model_menu.ts`
- MODIFIED `apps/desktop/src/i18n/types_notices.ts`
- ADDED `apps/desktop/src/i18n/types_onboarding.ts`
- MODIFIED `apps/desktop/src/i18n/types_shared_metrics.ts`
- MODIFIED `apps/desktop/src/i18n/zh-hant.ts`
- MODIFIED `apps/desktop/src/i18n/zh-hant_assistant.ts`
- MODIFIED `apps/desktop/src/i18n/zh-hant_boot.ts`
- MODIFIED `apps/desktop/src/i18n/zh-hant_chat.ts`
- MODIFIED `apps/desktop/src/i18n/zh-hant_chrome.ts`
- MODIFIED `apps/desktop/src/i18n/zh-hant_command_center.ts`
- MODIFIED `apps/desktop/src/i18n/zh-hant_settings.ts`
- MODIFIED `apps/desktop/src/i18n/zh.ts`
- MODIFIED `apps/desktop/src/i18n/zh_model_menu.ts`
- MODIFIED `apps/desktop/src/i18n/zh_notices.ts`
- ADDED `apps/desktop/src/i18n/zh_onboarding.ts`
- MODIFIED `apps/desktop/src/i18n/zh_shared_metrics.ts`
- MODIFIED `apps/desktop/src/lib/chat-messages/index.ts`
- MODIFIED `apps/desktop/src/lib/chat-messages/parts.ts`
- MODIFIED `apps/desktop/src/lib/chat-messages/tool-parts.ts`
- MODIFIED `apps/desktop/src/lib/desktop-slash-registry.json`
- MODIFIED `apps/desktop/src/lib/keybinds/composer-focus-keys.ts`
- MODIFIED `apps/desktop/src/lib/layout-persistence.ts`
- DELETED `apps/desktop/src/lib/onboarding-recommendations.ts`
- MODIFIED `apps/desktop/src/lib/tips/local-cta.test.ts`
- MODIFIED `apps/desktop/src/lib/tips/local-cta.ts`
- MODIFIED `apps/desktop/src/lib/tool-render-class.ts`
- MODIFIED `apps/desktop/src/lib/tool-result-metadata.ts`
- MODIFIED `apps/desktop/src/lib/transcript-directives.ts`
- MODIFIED `apps/desktop/src/store/clarify.test.ts`
- MODIFIED `apps/desktop/src/store/clarify.ts`
- MODIFIED `apps/desktop/src/store/connector-catalog.ts`
- MODIFIED `apps/desktop/src/store/desktop-metrics.ts`
- ADDED `apps/desktop/src/store/free-tier-offer.test.ts`
- MODIFIED `apps/desktop/src/store/free-tier-sign-in.ts`
- MODIFIED `apps/desktop/src/store/free-tier.ts`
- MODIFIED `apps/desktop/src/store/local-runtime-jobs.ts`
- ADDED `apps/desktop/src/store/local-setup-offer.ts`
- DELETED `apps/desktop/src/store/machine.ts`
- MODIFIED `apps/desktop/src/store/onboarding-answers.ts`
- DELETED `apps/desktop/src/store/onboarding-capabilities.ts`
- MODIFIED `apps/desktop/src/store/onboarding-gate.ts`
- ADDED `apps/desktop/src/store/onboarding-intro.ts`
- DELETED `apps/desktop/src/store/onboarding-plugin-outcomes.ts`
- MODIFIED `apps/desktop/src/store/onboarding-plugins.ts`
- MODIFIED `apps/desktop/src/store/onboarding-presence.ts`
- DELETED `apps/desktop/src/store/onboarding-script.ts`
- MODIFIED `apps/desktop/src/store/onboarding.ts`
- ADDED `apps/desktop/src/store/start-chat.test.ts`
- ADDED `apps/desktop/src/store/start-chat.ts`
- MODIFIED `apps/desktop/src/store/thread-scroll.test.ts`
- MODIFIED `apps/desktop/src/store/thread-scroll.ts`
- MODIFIED `apps/desktop/src/store/tips.ts`
- MODIFIED `apps/desktop/src/store/windows.ts`
- MODIFIED `apps/desktop/src/styles.css`
- MODIFIED `apps/desktop/src/types/nastech.ts`
- MODIFIED `apps/shared/src/gateway-contract.generated.ts`
- MODIFIED `apps/shared/src/gateway-contract.openrpc.json`
- MODIFIED `apps/shared/src/skill-scaffold.ts`
- ADDED `contributors/emails/aslater3@googlemail.com`
- ADDED `contributors/emails/jonh.dev.br@gmail.com`
- MODIFIED `gateway/run_agent_cache.py`
- MODIFIED `gateway/run_inbound.py`
- MODIFIED `gateway/run_startup.py`
- MODIFIED `gateway/run_turn.py`
- MODIFIED `gateway/session.py`
- MODIFIED `gateway/slash_commands.py`
- MODIFIED `nastech_cli/anon_auth.py`
- MODIFIED `nastech_cli/cli_chat_turn_mixin.py`
- MODIFIED `nastech_cli/cli_commands_mixin.py`
- MODIFIED `nastech_cli/cli_session_mixin.py`
- MODIFIED `nastech_cli/commands.py`
- MODIFIED `nastech_cli/commands_platforms.py`
- MODIFIED `nastech_cli/config_defaults.py`
- MODIFIED `nastech_cli/context_switch_guard.py`
- ADDED `nastech_cli/free_tier_offer.py`
- DELETED `nastech_cli/mcp_app_detection.py`
- MODIFIED `nastech_cli/mcp_catalog.py`
- MODIFIED `nastech_cli/model_selection_guards.py`
- MODIFIED `nastech_cli/observability/schemas/nastech.shared_metrics.v3.schema.json`
- MODIFIED `nastech_cli/observability/schemas/nastech.shared_metrics.v4.schema.json`
- MODIFIED `nastech_cli/observability/shared_metrics_contract.py`
- MODIFIED `nastech_cli/plugin_validate.py`
- MODIFIED `nastech_cli/plugins_cmd.py`
- MODIFIED `nastech_cli/plugins_cmd_catalog.py`
- MODIFIED `nastech_cli/plugins_cmd_install.py`
- MODIFIED `nastech_cli/plugins_cmd_remove.py`
- MODIFIED `nastech_cli/plugins_cmd_update.py`
- MODIFIED `nastech_cli/plugins_content.py`
- MODIFIED `nastech_cli/profile_distribution.py`
- MODIFIED `nastech_cli/profiles.py`
- MODIFIED `nastech_cli/setup_profile.py`
- MODIFIED `nastech_cli/subcommands/plugins.py`
- MODIFIED `nastech_cli/update_lock.py`
- MODIFIED `nastech_cli/web_routers/mcp.py`
- MODIFIED `nastech_cli/web_routers/profiles.py`
- MODIFIED `nastech_cli/web_server_dashboard.py`
- MODIFIED `nastech_state.py`
- ADDED `nastech_state_tool_retries.py`
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
- ADDED `optional-skills/productivity/first-task/SKILL.md`
- ADDED `optional-skills/productivity/initiate-setup/SKILL.md`
- ADDED `optional-skills/productivity/initiate-setup/templates/handoff.md`
- MODIFIED `plugin-catalog/nastech-monitoring-dashboard.yaml`
- MODIFIED `plugins/dashboard_auth/_shared.py`
- MODIFIED `plugins/dashboard_auth/self_hosted/__init__.py`
- MODIFIED `pm/_uv.py`
- ADDED `pm/_venv_entry.py`
- MODIFIED `pm/environments.py`
- MODIFIED `pm/packages.py`
- MODIFIED `pm/recovery.py`
- MODIFIED `run_agent.py`
- MODIFIED `scripts/bundles/desktop_inputs.py`
- MODIFIED `scripts/bundles/native.py`
- MODIFIED `scripts/msix-shared.mjs`
- MODIFIED `scripts/release.py`
- MODIFIED `scripts/releases/entrypoint.py`
- MODIFIED `scripts/releases/versioning.py`
- MODIFIED `scripts/termux/termux-builder.Dockerfile`
- MODIFIED `scripts/termux/termux_build.sh`
- MODIFIED `tests/agent/test_error_classifier.py`
- ADDED `tests/agent/test_free_tier_rate_limit_class.py`
- MODIFIED `tests/agent/test_message_sanitization_policy.py`
- MODIFIED `tests/agent/test_onboarding.py`
- ADDED `tests/agent/test_turn_user_intervened.py`
- MODIFIED `tests/agent/test_voice_turn_route.py`
- MODIFIED `tests/agent/test_welcome_tier_recovery.py`
- MODIFIED `tests/fixtures/resolution_allowlist.json`
- MODIFIED `tests/gateway/test_yolo_command.py`
- MODIFIED `tests/nastech_cli/test_anon_auth_core.py`
- ADDED `tests/nastech_cli/test_cli_first_message.py`
- MODIFIED `tests/nastech_cli/test_cli_yolo_resume_persistence.py`
- MODIFIED `tests/nastech_cli/test_cli_yolo_toggle.py`
- MODIFIED `tests/nastech_cli/test_context_cache_switch_guard.py`
- MODIFIED `tests/nastech_cli/test_context_switch_guard.py`
- ADDED `tests/nastech_cli/test_free_tier_offer.py`
- DELETED `tests/nastech_cli/test_mcp_app_detection.py`
- DELETED `tests/nastech_cli/test_mcp_catalog_discovery.py`
- ADDED `tests/nastech_cli/test_plugin_api_hot_mount.py`
- DELETED `tests/nastech_cli/test_plugin_live_gateway_guard.py`
- ADDED `tests/nastech_cli/test_plugin_uninstall_windows_live.py`
- MODIFIED `tests/nastech_cli/test_plugin_validate.py`
- MODIFIED `tests/nastech_cli/test_session_switch_mid_turn_guard.py`
- ADDED `tests/nastech_cli/test_setup_profile_answers.py`
- ADDED `tests/nastech_cli/test_setup_profile_owner.py`
- ADDED `tests/nastech_cli/test_setup_profile_returning_user.py`
- MODIFIED `tests/nastech_cli/test_shared_metrics_model.py`
- MODIFIED `tests/nastech_cli/test_update_lock.py`
- MODIFIED `tests/install/e2e-assets/drive-update.cjs`
- MODIFIED `tests/install/windows-bundle-smoke.ps1`
- MODIFIED `tests/install/windows-e2e.ps1`
- MODIFIED `tests/plugins/dashboard_auth/test_nastech_provider.py`
- MODIFIED `tests/plugins/dashboard_auth/test_self_hosted_provider.py`
- MODIFIED `tests/pm/test_uv_python.py`
- ADDED `tests/pm/test_venv_command.py`
- MODIFIED `tests/scripts/test_bundle_native.py`
- MODIFIED `tests/scripts/test_release_entrypoint.py`
- MODIFIED `tests/scripts/test_release_version_from_ref.py`
- ADDED `tests/tools/test_approval_yolo.py`
- ADDED `tests/tools/test_setup_choose_name_card.py`
- MODIFIED `tests/tui_gateway/test_auto_continue.py`
- MODIFIED `tests/tui_gateway/test_deferred_model_switch_confirm.py`
- MODIFIED `tests/tui_gateway/test_first_contact_onboarding.py`
- MODIFIED `tests/tui_gateway/test_free_tier_rpc.py`
- ADDED `tests/tui_gateway/test_free_tier_task_done.py`
- ADDED `tests/tui_gateway/test_resume_session_yolo.py`
- MODIFIED `tools/AGENTS.md`
- ADDED `tools/approval_yolo.py`
- MODIFIED `tools/delegate_tool_toolsets.py`
- ADDED `tools/setup_choose_tool.py`
- ADDED `tools/start_chat_tool.py`
- MODIFIED `toolsets.py`
- MODIFIED `tui_gateway/agent_callbacks.py`
- MODIFIED `tui_gateway/contracts/config_free_tier_control.py`
- MODIFIED `tui_gateway/contracts/profiles_vault_complete_foreign_subagents.py`
- MODIFIED `tui_gateway/contracts/server_requests.py`
- MODIFIED `tui_gateway/contracts/sessions.py`
- ADDED `tui_gateway/free_tier_task_done.py`
- MODIFIED `tui_gateway/methods_config.py`
- MODIFIED `tui_gateway/methods_config_set.py`
- MODIFIED `tui_gateway/methods_free_tier.py`
- MODIFIED `tui_gateway/methods_onboarding.py`
- MODIFIED `tui_gateway/methods_profiles.py`
- MODIFIED `tui_gateway/methods_session.py`
- MODIFIED `tui_gateway/methods_session_interrupt.py`
- ADDED `tui_gateway/methods_start_chat.py`
- MODIFIED `tui_gateway/methods_tools.py`
- MODIFIED `tui_gateway/model_switch.py`
- DELETED `tui_gateway/onboarding_personalization.py`
- MODIFIED `tui_gateway/prompt_turn.py`
- MODIFIED `tui_gateway/server.py`
- MODIFIED `tui_gateway/session_auto_continue.py`
- MODIFIED `tui_gateway/session_compression.py`
- MODIFIED `tui_gateway/session_history.py`
- MODIFIED `tui_gateway/session_workdir.py`
- ADDED `tui_gateway/start_chat.py`
- DELETED `website/docs/developer-guide/onboarding-recommendations.md`
- MODIFIED `website/docs/developer-guide/plugins/index.md`
- MODIFIED `website/docs/developer-guide/relay-shared-metrics.md`
- MODIFIED `website/docs/developer-guide/stable-releases.md`
- MODIFIED `website/docs/reference/optional-skills-catalog.md`
- MODIFIED `website/docs/reference/slash-commands.md`
- MODIFIED `website/docs/reference/tools-reference.md`
- MODIFIED `website/docs/reference/toolsets-reference.md`
- MODIFIED `website/docs/user-guide/configuration.md`
- MODIFIED `website/docs/user-guide/desktop.md`
- MODIFIED `website/docs/user-guide/features/delegation.md`
- MODIFIED `website/docs/user-guide/features/mcp.md`
- MODIFIED `website/docs/user-guide/security.md`
- ADDED `website/docs/user-guide/skills/optional/productivity/productivity-first-task.md`
- ADDED `website/docs/user-guide/skills/optional/productivity/productivity-initiate-setup.md`
- MODIFIED `website/sidebars.ts`

## Scan

17962 files scanned [audio=5, binary=8, doc=4, font=13, image=174, text=17758]


## Diff

2888 renamed, 0 rewritten, 14452 identical, 141 locked, 0 missing, 32 owned, 389 reconciled


## Fork check (vs nastech-agent)

- 17344 identical, 537 updated (+0/-0 lines), 81 added, 0 missing, 0 fork-local-unpreserved, 0 stale-upstream, 0 locked/binary, 0 collision-safe relocated, 60 preserved fork-local files, 0 violations

- features: fork 56 -> branded 56

Auto-generated by 100Ways.
