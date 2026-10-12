# Nastech Update Report #1

- upstream sha : `835c3dd038d903182a66ecc45e34bf5e0de65f00`
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

- total files : 18242
- renamed     : 3047 (folders and file names)
- text-rewritten : 18056
- locked-copied  : 60
- binary-copied  : 8
- owned assets   : 120 (our logo/banner/mascot override upstream)

## Reconcile

- fixed : 427 files reconciled: .env.example, .github/workflows/deploy-site.yml, .github/workflows/deploy-site.yml, .github/workflows/desktop-bundle-smoke.yml, .github/workflows/install-e2e-macos-run.yml, .github/workflows/install-e2e-windows-run.yml, .github/workflows/skills-index-freshness.yml, .github/workflows/tests-os.yml, .github/workflows/tests.yml, .github/workflows/windows-install-update-e2e.yml, .mailmap, AGENTS.md, CONTRIBUTING.es.md, CONTRIBUTING.md, Dockerfile, README.es.md, README.md, README.ur-pk.md, README.zh-CN.md, SECURITY.es.md, SECURITY.md, agent/agent_runtime_helpers.py, agent/anthropic_adapter.py, agent/anthropic_endpoints.py, agent/auxiliary_client.py, agent/billing_links.py, agent/billing_view.py, agent/chat_completion_helpers.py, agent/conversation_compression.py, agent/conversation_loop.py, agent/message_sanitization.py, agent/model_metadata.py, agent/prompt_builder.py, agent/proxy_sources/iron_proxy.py, agent/reasoning_params.py, agent/subscription_view.py, agent/turn_recovery.py, agent/usage_pricing.py, apps/bootstrap-installer/src-tauri/Cargo.toml, apps/desktop/README.md, apps/desktop/electron-builder.config.cjs, apps/desktop/electron/backend-health.test.ts, apps/desktop/electron/backend-health.ts, apps/desktop/electron/challenge-window.test.ts, apps/desktop/electron/cloud-session-recovery.test.ts, apps/desktop/electron/connection-config.test.ts, apps/desktop/electron/data-paths.test.ts, apps/desktop/electron/hub-iframe-policy.ts, apps/desktop/electron/oauth-partition.test.ts, apps/desktop/electron/portal-session.ts, apps/desktop/electron/remote-lifecycle.ts, apps/desktop/electron/remote-oauth-ticket.test.ts, apps/desktop/electron/updater/checkout-source.test.ts, apps/desktop/electron/window-open-policy.test.ts, apps/desktop/scripts/bundle-env.test.mjs, apps/desktop/src/app/capabilities/index.test.tsx, apps/desktop/src/app/capabilities/plugins/plugins-tab.test.tsx, apps/desktop/src/app/capabilities/skills/embedded-hub-picker.tsx, apps/desktop/src/app/chat/sidebar/section-states.tsx, apps/desktop/src/app/messaging/index.test.tsx, apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx, apps/desktop/src/app/settings/billing/api.test.ts, apps/desktop/src/app/settings/billing/dev-fixtures.ts, apps/desktop/src/app/settings/billing/errors.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.ts, apps/desktop/src/app/settings/billing/use-charge-poller.test.ts, apps/desktop/src/app/settings/billing/use-step-up.test.tsx, apps/desktop/src/app/settings/constants.ts, apps/desktop/src/app/settings/gateway-settings.test.tsx, apps/desktop/src/app/settings/gateway-settings.tsx, apps/desktop/src/app/settings/toolset-config-panel.test.tsx, apps/desktop/src/app/shell/terms-butterbar.tsx, apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts, apps/desktop/src/components/boot-failure-overlay.test.tsx, apps/desktop/src/components/boot-failure-overlay.tsx, apps/desktop/src/components/send-diagnostics-dialog.tsx, apps/desktop/src/components/update-status.tsx, apps/desktop/src/contrib/plugin.ts, apps/desktop/src/i18n/de.ts, apps/desktop/src/i18n/en.ts, apps/desktop/src/i18n/es.ts, apps/desktop/src/i18n/fr.ts, apps/desktop/src/i18n/ja.ts, apps/desktop/src/i18n/ru.ts, apps/desktop/src/i18n/zh-hant_settings.ts, apps/desktop/src/i18n/zh.ts, apps/desktop/src/lib/docs.ts, apps/desktop/src/lib/plugin-catalog.ts, apps/desktop/src/plugins/nastech-bots/skills-hub-picker.test.tsx, apps/desktop/src/plugins/nastech-bots/skills-hub.tsx, apps/desktop/src/sdk/index.ts, apps/desktop/src/store/free-tier-challenge.test.ts, apps/desktop/src/store/shared-metrics.ts, apps/desktop/src/themes/use-skin-command.ts, cli-config.yaml.example, eslint.config.shared.mjs, evals/auth_pool_controls.py, evals/browser_use/single_run.py, evals/postmortem/live_ab/auth_stampede.py, evals/postmortem/live_ab/cache_concurrency_probe.py, evals/postmortem/review_probes/cache_estimator_probe.py, evals/postmortem/review_probes/credential_identity_probe.py, evals/reasoning_replay/harness.py, locales/_keys.desktop.json, locales/_keys.tui.json, nastech_cli/anon_auth.py, nastech_cli/anon_auth.py, nastech_cli/anon_sign_in.py, nastech_cli/auth.py, nastech_cli/auth_codex.py, nastech_cli/auth_constants.py, nastech_cli/auth_error_copy.py, nastech_cli/auth_nastech.py, nastech_cli/banner.py, nastech_cli/config_defaults.py, nastech_cli/dashboard_auth/login_page.py, nastech_cli/dashboard_register.py, nastech_cli/debug.py, nastech_cli/diagnostics_upload.py, nastech_cli/fallback_cmd.py, nastech_cli/kanban_parser.py, nastech_cli/main.py, nastech_cli/main_dashboard.py, nastech_cli/main_desktop.py, nastech_cli/model_catalog.py, nastech_cli/model_setup_flows_common.py, nastech_cli/models.py, nastech_cli/models_pricing.py, nastech_cli/nastech_account.py, nastech_cli/nastech_account.py, nastech_cli/nastech_billing.py, nastech_cli/observability/shared_metrics_consent.py, nastech_cli/observability/shared_metrics_send_config.py, nastech_cli/plugin_catalog.py, nastech_cli/plugins_cmd.py, nastech_cli/portal_cli.py, nastech_cli/providers.py, nastech_cli/proxy/adapters/base.py, nastech_cli/proxy/adapters/nastech_portal.py, nastech_cli/setup.py, nastech_cli/setup_platforms.py, nastech_cli/setup_quick.py, nastech_cli/setup_whatsapp_cloud.py, nastech_cli/skin_engine.py, nastech_cli/source_releases.py, nastech_cli/steward.py, nastech_cli/subcommands/egress.py, nastech_cli/subcommands/fallback.py, nastech_cli/subcommands/secrets.py, nastech_cli/subcommands/worktree.py, nastech_cli/telegram_managed_bot.py, nastech_cli/tools_config.py, nastech_cli/uninstall.py, nastech_cli/update_cmd.py, nastech_cli/update_cmd_maint.py, nastech_cli/update_cmd_zip.py, nastech_cli/web_routers/status.py, nastech_cli/web_server_messaging.py, nastech_cli/web_server_oauth.py, nastech_constants.py, nastech_state_errors.py, optional-skills/productivity/memento-flashcards/SKILL.md, package-lock.json, plugin-catalog/README.md, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/plugin.yaml, plugins/kanban/dashboard/dist/index.js, plugins/kanban/systemd/nastech-kanban-dispatcher.service, plugins/model-providers/ai-gateway/__init__.py, plugins/model-providers/fireworks/__init__.py, plugins/model-providers/kimi-coding/__init__.py, plugins/model-providers/nastech/__init__.py, plugins/model-providers/opencode-zen/__init__.py, plugins/model-providers/solstice/auth.py, plugins/nastech-achievements/dashboard/dist/index.js, plugins/platforms/discord/adapter.py, plugins/platforms/discord/onboarding.py, plugins/platforms/email/adapter.py, plugins/platforms/photon/sidecar/package-lock.json, plugins/platforms/slack/adapter.py, plugins/web/perplexity/provider.py, pm/artifact-mirror.json, pm/uv.lock, scripts/build_model_catalog.py, scripts/contributor_audit.py, scripts/e2e_shared_metrics_staging.py, scripts/install.cmd, scripts/install.ps1, scripts/install.sh, scripts/release.py, scripts/releases/authors_legacy.py, scripts/releases/r2.py, scripts/sandbox/generate-e2e-matrix.mjs, scripts/termux/stage_apt_repo.py, scripts/tests/test-install-ps1-store-guard.ps1, scripts/whatsapp-bridge/package-lock.json, setup.py, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/references/background-systems.md, skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md, skills/autonomous-ai-agents/nastech-agent/references/configuration.md, skills/autonomous-ai-agents/nastech-agent/references/contributor-guide.md, skills/autonomous-ai-agents/nastech-agent/references/portal-auth-for-third-party-apps.md, skills/autonomous-ai-agents/nastech-agent/references/providers-and-models.md, skills/autonomous-ai-agents/nastech-agent/references/webhooks.md, skills/media/youtube-content/SKILL.md, skills/software-development/python-debugpy/SKILL.md, tests/agent/test_anthropic_adapter.py, tests/agent/test_anthropic_preserved_thinking_replay.py, tests/agent/test_anthropic_prompt_cache_policy.py, tests/agent/test_auxiliary_auth_rung_fallthrough.py, tests/agent/test_auxiliary_client.py, tests/agent/test_auxiliary_client_nastech_401_cache_key.py, tests/agent/test_auxiliary_main_first.py, tests/agent/test_auxiliary_transport_autodetect.py, tests/agent/test_billing_links.py, tests/agent/test_credential_pool.py, tests/agent/test_credential_pool_nastech_refresh_stampede.py, tests/agent/test_credits_cold_start.py, tests/agent/test_credits_policy.py, tests/agent/test_deepseek_anthropic_thinking.py, tests/agent/test_error_classifier.py, tests/agent/test_error_classifier_observed.py, tests/agent/test_fast_mode_auto.py, tests/agent/test_free_tier_rate_limit_class.py, tests/agent/test_model_metadata.py, tests/agent/test_nastech_credits_gauge.py, tests/agent/test_nastech_key_pre_expiry_adoption.py, tests/agent/test_nastech_portal_anthropic_wire.py, tests/agent/test_nastech_rate_guard.py, tests/agent/test_nastech_welcome_client_contract.py, tests/agent/test_nastech_wire_auto.py, tests/agent/test_nonretryable_result_carries_verdict.py, tests/agent/test_primary_runtime_restore.py, tests/agent/test_provider_attribution_headers.py, tests/agent/test_provider_fallback.py, tests/agent/test_provider_history_parity.py, tests/agent/test_provider_parity.py, tests/agent/test_reasoning_replay_routes.py, tests/agent/test_run_agent.py, tests/agent/test_switch_model_reapplies_headers.py, tests/agent/test_turn_usage_log_line.py, tests/agent/test_welcome_error_identity.py, tests/agent/test_welcome_tier_recovery.py, tests/agent/transports/test_chat_completions.py, tests/agent/transports/test_chat_completions_reasoning_details_replay.py, tests/agent/transports/test_provider_wire_snapshot.py, tests/compat/old_updater_dependencies.py, tests/docker/test_sqlite_runtime.py, tests/e2e/core/live/_helpers.py, tests/e2e/core/providers/test_catalog_oauth.py, tests/e2e/core/providers/test_chat_reasoning_variants.py, tests/e2e/core/providers/test_fallback_providers.py, tests/e2e/core/upgrade/network/_seed.py, tests/e2e/core/windows/test_boot_lifecycle.py, tests/e2e/core/windows_update/_machine.py, tests/fakes/providers/chat_variants.py, tests/fakes/providers/vertex.py, tests/fixtures/prompt_surface/prompts/cli-code.claude.txt, tests/fixtures/prompt_surface/prompts/cli.claude.txt, tests/fixtures/prompt_surface/prompts/cli.gemini.txt, tests/fixtures/prompt_surface/prompts/cli.gpt.txt, tests/fixtures/prompt_surface/prompts/cli.nastech.txt, tests/fixtures/prompt_surface/prompts/cron.claude.txt, tests/fixtures/prompt_surface/prompts/desktop.claude.txt, tests/fixtures/prompt_surface/prompts/discord.claude.txt, tests/fixtures/prompt_surface/prompts/telegram.claude.txt, tests/fixtures/provider_wire_snapshot.json, tests/gateway/test_discord_format.py, tests/gateway/test_free_tier_startup_notice.py, tests/gateway/test_housekeeping_profile_scope.py, tests/gateway/test_internal_event_pin_wiring.py, tests/gateway/test_model_switch_persistence.py, tests/gateway/test_run_progress_topics.py, tests/gateway/test_session_model_override_persistence.py, tests/gateway/test_startup_warmup_profile_scope.py, tests/gateway/test_status_command.py, tests/gateway/test_status_free_tier_line.py, tests/gateway/test_telegram_mention_context.py, tests/gateway/test_usage_command.py, tests/install/macos-desktop-e2e.sh, tests/install/windows-e2e.ps1, tests/nastech_cli/anon_portal.py, tests/nastech_cli/test_anon_auth_core.py, tests/nastech_cli/test_anon_failure_modes.py, tests/nastech_cli/test_anon_failure_modes.py, tests/nastech_cli/test_anon_first_notice.py, tests/nastech_cli/test_anon_picker.py, tests/nastech_cli/test_anon_surfaces.py, tests/nastech_cli/test_anon_upgrade.py, tests/nastech_cli/test_auth_nastech_provider.py, tests/nastech_cli/test_base_url_host_identity.py, tests/nastech_cli/test_cli_first_run_setup.py, tests/nastech_cli/test_cli_init.py, tests/nastech_cli/test_cli_provider_resolution.py, tests/nastech_cli/test_dashboard_register.py, tests/nastech_cli/test_fireworks_provider.py, tests/nastech_cli/test_local_abandoned_requests.py, tests/nastech_cli/test_local_quickstart.py, tests/nastech_cli/test_model_catalog.py, tests/nastech_cli/test_model_validation.py, tests/nastech_cli/test_nastech_anthropic_wire_default.py, tests/nastech_cli/test_nastech_auth_keepalive.py, tests/nastech_cli/test_nastech_auth_status_cache.py, tests/nastech_cli/test_nastech_inference_url_validation.py, tests/nastech_cli/test_nastech_nonproduction_inference_host.py, tests/nastech_cli/test_nastech_nonproduction_inference_host.py, tests/nastech_cli/test_nastech_portal_staging_allowlist.py, tests/nastech_cli/test_nastech_reasoning_metadata.py, tests/nastech_cli/test_proxy.py, tests/nastech_cli/test_reasoning_caps_disk_cache.py, tests/nastech_cli/test_sale_pricing.py, tests/nastech_cli/test_show_config_credential.py, tests/nastech_cli/test_source_channel_integration.py, tests/nastech_cli/test_source_check.py, tests/nastech_cli/test_update_target_identity.py, tests/nastech_cli/test_web_oauth_dispatch.py, tests/plugins/dashboard_auth/test_nastech_provider.py, tests/plugins/image_gen/check_parity_vs_main.py, tests/plugins/image_gen/test_openrouter_compat_provider.py, tests/plugins/test_chronos_verify.py, tests/scripts/test_release_build_commit.py, tests/scripts/test_release_r2.py, tests/scripts/test_release_r2.py, tests/scripts/test_stage_apt_repo.py, tests/scripts/test_upload_summary.py, tests/tools/test_delegate.py, tests/tools/test_managed_media_gateways.py, tests/tools/test_managed_tool_gateway.py, tests/tools/test_plugin_guard.py, tests/tools/test_stage2_hook_nastech_routing_env.py, tests/tools/test_strict_provider_selection.py, tests/tools/test_tts_openai_config.py, tests/tools/test_url_safety.py, tests/tools/test_web_tools_config.py, tests/tools/test_web_tools_perplexity.py, tests/tui_gateway/test_free_tier_rpc.py, tests/tui_gateway/test_resume_switched_provider_endpoint.py, tools/managed_gateway_auth.py, tools/managed_tool_gateway.py, tools/mcp_oauth.py, tools/plugin_guard_context.py, tools/skills_hub_search.py, trajectory_compressor.py, ui-tui/scripts/billing-fixtures.tsx, ui-tui/src/__tests__/subscriptionCommand.test.ts, ui-tui/src/__tests__/subscriptionOverlay.test.tsx, ui-tui/src/app/slash/commands/subscription.ts, ui-tui/src/domain/paths.ts, uv.lock, web/src/components/SharedMetricsConsentBanner.tsx, web/src/components/SidebarFooter.tsx, web/src/pages/DocsPage.tsx, web/src/pages/PluginsPage.tsx, web/src/pages/SystemPage.tsx, website/README.md, website/docs/developer-guide/egress-internals.md, website/docs/developer-guide/stable-releases.md, website/docs/getting-started/installation.md, website/docs/getting-started/platform-support.md, website/docs/getting-started/quickstart.md, website/docs/getting-started/termux.md, website/docs/guides/manage-nastech-cloud-with-mcp.md, website/docs/guides/run-nastech-with-nastech-portal.md, website/docs/guides/run-nemotron-3-ultra-free.md, website/docs/index.mdx, website/docs/integrations/nastech-portal.md, website/docs/integrations/providers.md, website/docs/reference/cli-commands.md, website/docs/reference/environment-variables.md, website/docs/reference/faq.md, website/docs/reference/model-catalog.md, website/docs/reference/skills-catalog.md, website/docs/user-guide/desktop.md, website/docs/user-guide/egress/iron-proxy.md, website/docs/user-guide/features/browser.md, website/docs/user-guide/features/image-generation.md, website/docs/user-guide/features/plugin-catalog.md, website/docs/user-guide/features/skills.md, website/docs/user-guide/features/subscription-proxy.md, website/docs/user-guide/features/tool-gateway.md, website/docs/user-guide/features/tools.md, website/docs/user-guide/features/tts.md, website/docs/user-guide/features/web-dashboard.md, website/docs/user-guide/features/web-search.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/skills/bundled/media/media-youtube-content.md, website/docs/user-guide/skills/bundled/software-development/software-development-python-debugpy.md, website/docs/user-guide/skills/optional/productivity/productivity-memento-flashcards.md, website/docs/user-guide/windows-native.md, website/docs/user-guide/windows-wsl-quickstart.md, website/docusaurus.config.ts, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/plugins/index.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/quickstart.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-nastech-with-nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/index.mdx, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/providers.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/faq.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/model-catalog.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/subscription-proxy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tools.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tts.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/media/media-youtube-content.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/software-development/software-development-python-debugpy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/optional/productivity/productivity-memento-flashcards.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-native.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-wsl-quickstart.md, website/scripts/fetch-plugin-stars.py, website/scripts/generate-llms-txt.py, website/scripts/prebuild.mjs, website/src/pages/plugins/index.tsx, website/src/pages/skills/index.tsx, website/static/api/model-catalog.json, website/static/oauth/client-metadata.json


## Direct upstream tree delta

- complete: +182 ~228 -1 ↪0
- MODIFIED `.github/CODEOWNERS`
- ADDED `.github/actions/check-clean-worktree/action.yml`
- MODIFIED `.github/actions/detect-changes/action.yml`
- ADDED `.github/blob-size-allowlist.txt`
- ADDED `.github/workflows/blob-size-check.yml`
- MODIFIED `.github/workflows/ci.yaml`
- MODIFIED `.github/workflows/desktop-bundled-release.yml`
- MODIFIED `.github/workflows/js-tests.yml`
- MODIFIED `.github/workflows/lint.yml`
- MODIFIED `.github/workflows/plugin-catalog-ci.yml`
- ADDED `.github/workflows/prompt-surface-diff.yml`
- ADDED `.github/workflows/remote-backends.yml`
- MODIFIED `.github/workflows/stable-release.yml`
- MODIFIED `.github/workflows/tests-os.yml`
- MODIFIED `.github/workflows/tests.yml`
- MODIFIED `.gitignore`
- MODIFIED `agent/anthropic_message_convert.py`
- MODIFIED `agent/bedrock_adapter.py`
- MODIFIED `agent/transports/bedrock.py`
- MODIFIED `apps/desktop/README.md`
- MODIFIED `apps/desktop/electron/updater/checkout-source.test.ts`
- ADDED `apps/desktop/src/app/capabilities/connectors/accounts-section.test.tsx`
- ADDED `apps/desktop/src/app/capabilities/connectors/accounts-section.tsx`
- ADDED `apps/desktop/src/app/capabilities/connectors/connect-element.test.tsx`
- MODIFIED `apps/desktop/src/app/capabilities/connectors/connect-element.tsx`
- MODIFIED `apps/desktop/src/app/capabilities/connectors/connector-dialog.tsx`
- MODIFIED `apps/desktop/src/app/capabilities/connectors/connector-row-card.tsx`
- MODIFIED `apps/desktop/src/app/capabilities/connectors/connectors-tab.tsx`
- ADDED `apps/desktop/src/app/capabilities/connectors/data/account-operations.test.ts`
- MODIFIED `apps/desktop/src/app/capabilities/connectors/data/account-operations.ts`
- ADDED `apps/desktop/src/app/capabilities/connectors/data/alias.ts`
- ADDED `apps/desktop/src/app/capabilities/connectors/data/connect-address.test.ts`
- ADDED `apps/desktop/src/app/capabilities/connectors/data/deep-link.test.ts`
- MODIFIED `apps/desktop/src/app/capabilities/connectors/data/deep-link.ts`
- ADDED `apps/desktop/src/app/capabilities/connectors/data/join.test.ts`
- MODIFIED `apps/desktop/src/app/capabilities/connectors/data/join.ts`
- MODIFIED `apps/desktop/src/app/capabilities/connectors/data/mutations.ts`
- MODIFIED `apps/desktop/src/app/capabilities/connectors/data/queries.ts`
- MODIFIED `apps/desktop/src/app/capabilities/connectors/data/rpc.ts`
- MODIFIED `apps/desktop/src/app/capabilities/connectors/derive.ts`
- ADDED `apps/desktop/src/app/capabilities/connectors/disconnect-confirm.tsx`
- MODIFIED `apps/desktop/src/app/capabilities/connectors/hosted-dialog.tsx`
- MODIFIED `apps/desktop/src/app/capabilities/connectors/types.ts`
- MODIFIED `apps/desktop/src/app/capabilities/scope-selector.tsx`
- MODIFIED `apps/desktop/src/app/chat/session-tile-actions.test.ts`
- MODIFIED `apps/desktop/src/app/chat/session-tile-actions.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-prompt-actions/index.deep-cut.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/index.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/index.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-prompt-actions/prompt-actions-harness.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/rewind.test.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/rewind.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/upload-composer-attachment.test.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/utils.ts`
- MODIFIED `apps/desktop/src/app/settings/constants.ts`
- MODIFIED `apps/desktop/src/components/assistant-ui/connector-tool.test.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/connector-tool.tsx`
- MODIFIED `apps/desktop/src/i18n/de.ts`
- ADDED `apps/desktop/src/i18n/de_connector_accounts.ts`
- ADDED `apps/desktop/src/i18n/de_connector_card.ts`
- MODIFIED `apps/desktop/src/i18n/en.ts`
- ADDED `apps/desktop/src/i18n/en_connector_accounts.ts`
- ADDED `apps/desktop/src/i18n/en_connector_card.ts`
- MODIFIED `apps/desktop/src/i18n/es.ts`
- ADDED `apps/desktop/src/i18n/es_connector_accounts.ts`
- ADDED `apps/desktop/src/i18n/es_connector_card.ts`
- MODIFIED `apps/desktop/src/i18n/fr.ts`
- ADDED `apps/desktop/src/i18n/fr_connector_accounts.ts`
- ADDED `apps/desktop/src/i18n/fr_connector_card.ts`
- MODIFIED `apps/desktop/src/i18n/overlay-gaps.json`
- MODIFIED `apps/desktop/src/i18n/types.ts`
- ADDED `apps/desktop/src/i18n/types_connectors.ts`
- MODIFIED `apps/desktop/src/i18n/zh.ts`
- ADDED `apps/desktop/src/i18n/zh_connector_card.ts`
- MODIFIED `apps/desktop/src/store/connection-request.ts`
- MODIFIED `apps/shared/src/gateway-contract.generated.ts`
- MODIFIED `apps/shared/src/gateway-contract.openrpc.json`
- ADDED `contributors/emails/shadus@gmail.com`
- ADDED `contributors/emails/wdjessica24@gmail.com`
- MODIFIED `gateway/run_busy.py`
- MODIFIED `gateway/run_notifications.py`
- ADDED `gateway/run_notifications_ownership.py`
- MODIFIED `gateway/run_turn.py`
- MODIFIED `nastech_cli/cli_modal_mixin.py`
- MODIFIED `nastech_cli/config_defaults.py`
- ADDED `nastech_cli/connectors_cmd.py`
- MODIFIED `nastech_cli/main.py`
- MODIFIED `nastech_cli/profiles.py`
- ADDED `nastech_cli/subcommands/connectors.py`
- MODIFIED `nastech_cli/subcommands/sessions.py`
- MODIFIED `lefthook.yml`
- MODIFIED `locales/_keys.desktop.json`
- MODIFIED `locales/_keys.tui.json`
- MODIFIED `locales/af.tui.yaml`
- MODIFIED `locales/af.yaml`
- MODIFIED `locales/ar.tui.yaml`
- MODIFIED `locales/ar.yaml`
- MODIFIED `locales/de.tui.yaml`
- MODIFIED `locales/de.yaml`
- MODIFIED `locales/en.yaml`
- MODIFIED `locales/es.tui.yaml`
- MODIFIED `locales/es.yaml`
- MODIFIED `locales/fr.tui.yaml`
- MODIFIED `locales/fr.yaml`
- MODIFIED `locales/ga.tui.yaml`
- MODIFIED `locales/ga.yaml`
- MODIFIED `locales/hu.tui.yaml`
- MODIFIED `locales/hu.yaml`
- MODIFIED `locales/it.tui.yaml`
- MODIFIED `locales/it.yaml`
- MODIFIED `locales/ja.tui.yaml`
- MODIFIED `locales/ja.yaml`
- MODIFIED `locales/ko.tui.yaml`
- MODIFIED `locales/ko.yaml`
- MODIFIED `locales/pt.tui.yaml`
- MODIFIED `locales/pt.yaml`
- MODIFIED `locales/ru.tui.yaml`
- MODIFIED `locales/ru.yaml`
- MODIFIED `locales/tr.tui.yaml`
- MODIFIED `locales/tr.yaml`
- MODIFIED `locales/uk.tui.yaml`
- MODIFIED `locales/uk.yaml`
- MODIFIED `locales/zh-hant.tui.yaml`
- MODIFIED `locales/zh-hant.yaml`
- MODIFIED `locales/zh.tui.yaml`
- MODIFIED `locales/zh.yaml`
- ADDED `optional-skills/creative/anatomy/LICENSE.txt`
- ADDED `optional-skills/creative/anatomy/SKILL.md`
- ADDED `optional-skills/creative/anatomy/examples/arcade-cabinet/arcade-cabinet.css`
- ADDED `optional-skills/creative/anatomy/examples/arcade-cabinet/build.mjs`
- ADDED `optional-skills/creative/anatomy/examples/arcade-cabinet/live.js`
- ADDED `optional-skills/creative/anatomy/examples/arcade-cabinet/parts.mjs`
- ADDED `optional-skills/creative/anatomy/examples/arcade-cabinet/screen.mjs`
- ADDED `optional-skills/creative/anatomy/examples/desk-computer/build.mjs`
- ADDED `optional-skills/creative/anatomy/examples/dial-indicator/build.mjs`
- ADDED `optional-skills/creative/anatomy/examples/raptor-engine/build.mjs`
- ADDED `optional-skills/creative/anatomy/examples/raptor-engine/live.js`
- ADDED `optional-skills/creative/anatomy/examples/raptor-engine/raptor.css`
- ADDED `optional-skills/creative/anatomy/examples/ripple-tank/build.mjs`
- ADDED `optional-skills/creative/anatomy/examples/ripple-tank/live.js`
- ADDED `optional-skills/creative/anatomy/examples/ripple-tank/model.mjs`
- ADDED `optional-skills/creative/anatomy/examples/ripple-tank/ripple.css`
- ADDED `optional-skills/creative/anatomy/examples/spot-plate/art.tsx`
- ADDED `optional-skills/creative/anatomy/examples/spot-plate/drops.ts`
- ADDED `optional-skills/creative/anatomy/examples/spot-plate/fan.ts`
- ADDED `optional-skills/creative/anatomy/examples/spot-plate/figure.tsx`
- ADDED `optional-skills/creative/anatomy/examples/spot-plate/geometry.ts`
- ADDED `optional-skills/creative/anatomy/examples/spot-plate/live.tsx`
- ADDED `optional-skills/creative/anatomy/examples/spot-plate/rig.ts`
- ADDED `optional-skills/creative/anatomy/examples/spot-plate/spot-plate.css`
- ADDED `optional-skills/creative/anatomy/examples/test-rig/art.tsx`
- ADDED `optional-skills/creative/anatomy/examples/test-rig/figure.tsx`
- ADDED `optional-skills/creative/anatomy/examples/test-rig/geometry.ts`
- ADDED `optional-skills/creative/anatomy/examples/test-rig/live.tsx`
- ADDED `optional-skills/creative/anatomy/examples/test-rig/pose.ts`
- ADDED `optional-skills/creative/anatomy/examples/test-rig/rig.ts`
- ADDED `optional-skills/creative/anatomy/examples/test-rig/stretch.css`
- ADDED `optional-skills/creative/anatomy/examples/test-rig/view.ts`
- ADDED `optional-skills/creative/anatomy/examples/turning-dial/build.mjs`
- ADDED `optional-skills/creative/anatomy/examples/turning-dial/dial.css`
- ADDED `optional-skills/creative/anatomy/examples/turning-dial/live.js`
- ADDED `optional-skills/creative/anatomy/examples/turning-dial/stress.mjs`
- ADDED `optional-skills/creative/anatomy/kit/audit.mjs`
- ADDED `optional-skills/creative/anatomy/kit/canvas-painter.mjs`
- ADDED `optional-skills/creative/anatomy/kit/gl-shared.mjs`
- ADDED `optional-skills/creative/anatomy/kit/gl.mjs`
- ADDED `optional-skills/creative/anatomy/kit/iso-kit.mjs`
- ADDED `optional-skills/creative/anatomy/kit/iso-kit.ts`
- ADDED `optional-skills/creative/anatomy/kit/iso.css`
- ADDED `optional-skills/creative/anatomy/kit/lathe.mjs`
- ADDED `optional-skills/creative/anatomy/kit/react/draw.tsx`
- ADDED `optional-skills/creative/anatomy/kit/react/live.tsx`
- ADDED `optional-skills/creative/anatomy/kit/tube.mjs`
- ADDED `optional-skills/creative/anatomy/kit/turn-audit.mjs`
- ADDED `optional-skills/creative/anatomy/kit/turn-build.mjs`
- ADDED `optional-skills/creative/anatomy/kit/turn-fixed.mjs`
- ADDED `optional-skills/creative/anatomy/kit/turn.mjs`
- ADDED `optional-skills/creative/anatomy/references/3d.md`
- ADDED `optional-skills/creative/anatomy/references/craft.md`
- ADDED `optional-skills/creative/anatomy/references/kit.md`
- ADDED `optional-skills/creative/anatomy/references/motion.md`
- ADDED `optional-skills/creative/anatomy/references/react.md`
- ADDED `optional-skills/creative/anatomy/references/verify.md`
- ADDED `optional-skills/creative/anatomy/references/walkthrough.md`
- ADDED `optional-skills/creative/anatomy/references/webgl.md`
- ADDED `optional-skills/creative/anatomy/scripts/capture.mjs`
- ADDED `optional-skills/creative/anatomy/scripts/drive.mjs`
- ADDED `optional-skills/creative/anatomy/scripts/inline-kit.mjs`
- ADDED `optional-skills/creative/anatomy/scripts/line-ends.mjs`
- ADDED `optional-skills/creative/anatomy/scripts/lines.mjs`
- ADDED `optional-skills/creative/anatomy/scripts/turn-bench.mjs`
- ADDED `optional-skills/creative/anatomy/scripts/turn-check.mjs`
- ADDED `optional-skills/creative/anatomy/scripts/turn-fidelity.mjs`
- MODIFIED `plugin-catalog/README.md`
- ADDED `plugin-catalog/accent-picker.yaml`
- MODIFIED `plugin-catalog/blender.yaml`
- MODIFIED `plugin-catalog/nastech-memory-wiki.yaml`
- MODIFIED `plugin-catalog/nastech-telegram-business.yaml`
- MODIFIED `plugin-catalog/snyk.yaml`
- DELETED `plugin-catalog/tabro.yaml`
- MODIFIED `plugin-catalog/touchdesigner.yaml`
- MODIFIED `scripts/bundles/channel_artifacts.py`
- MODIFIED `scripts/bundles/release_artifacts.py`
- MODIFIED `scripts/check`
- ADDED `scripts/ci/check_blob_size.py`
- ADDED `scripts/ci/check_docs_drift.py`
- MODIFIED `scripts/ci/classify_changes.py`
- ADDED `scripts/ci/docs_drift_baseline.json`
- ADDED `scripts/ci/prompt_surface.py`
- MODIFIED `scripts/ci/required_results.py`
- ADDED `scripts/ci/start_test_sshd.sh`
- ADDED `scripts/ci/test_sshd_container_setup.sh`
- MODIFIED `scripts/code_health/config.py`
- ADDED `scripts/code_health/py_ast.py`
- MODIFIED `scripts/code_health/py_rules.py`
- ADDED `scripts/code_health/py_rules_sleep.py`
- MODIFIED `scripts/release.py`
- MODIFIED `scripts/releases/channel_releases.py`
- MODIFIED `scripts/releases/channels.py`
- MODIFIED `scripts/releases/darwin.py`
- MODIFIED `scripts/releases/entrypoint.py`
- MODIFIED `scripts/releases/job_groups.py`
- ADDED `scripts/releases/optional_platforms.py`
- MODIFIED `scripts/releases/r2.py`
- MODIFIED `scripts/releases/sequencer.py`
- MODIFIED `scripts/releases/stable.py`
- MODIFIED `scripts/releases/store.py`
- MODIFIED `scripts/run_tests.sh`
- MODIFIED `scripts/run_tests_parallel.py`
- ADDED `scripts/scan_plugin_payloads.py`
- MODIFIED `scripts/validate_plugin_catalog.py`
- MODIFIED `tests-js/scripts/desktop-chat-smoke.ts`
- MODIFIED `tests-js/scripts/mock-provider-config.ts`
- MODIFIED `tests/AGENTS.md`
- ADDED `tests/ci/test_check_blob_size.py`
- MODIFIED `tests/ci/test_classify_changes.py`
- ADDED `tests/ci/test_clean_worktree_check.py`
- MODIFIED `tests/ci/test_desktop_bundle_smoke.py`
- ADDED `tests/ci/test_docs_drift.py`
- MODIFIED `tests/ci/test_plugin_catalog_ci_confinement.py`
- ADDED `tests/ci/test_prompt_surface.py`
- MODIFIED `tests/ci/test_required_results.py`
- MODIFIED `tests/ci/test_stable_release_graph.py`
- MODIFIED `tests/e2e/core/providers/test_chat_reasoning_variants.py`
- MODIFIED `tests/e2e/core/upgrade/network/test_offline_and_flaky.py`
- MODIFIED `tests/e2e/core/upgrade/network/test_proxy_only_egress.py`
- ADDED `tests/fixtures/prompt_surface/prompts/cli-code.claude.txt`
- ADDED `tests/fixtures/prompt_surface/prompts/cli.claude.txt`
- ADDED `tests/fixtures/prompt_surface/prompts/cli.gemini.txt`
- ADDED `tests/fixtures/prompt_surface/prompts/cli.gpt.txt`
- ADDED `tests/fixtures/prompt_surface/prompts/cli.nastech.txt`
- ADDED `tests/fixtures/prompt_surface/prompts/cron.claude.txt`
- ADDED `tests/fixtures/prompt_surface/prompts/desktop.claude.txt`
- ADDED `tests/fixtures/prompt_surface/prompts/discord.claude.txt`
- ADDED `tests/fixtures/prompt_surface/prompts/telegram.claude.txt`
- ADDED `tests/fixtures/prompt_surface/surfaces.json`
- ADDED `tests/fixtures/prompt_surface/tools/browser_back.json`
- ADDED `tests/fixtures/prompt_surface/tools/browser_cdp.json`
- ADDED `tests/fixtures/prompt_surface/tools/browser_click.json`
- ADDED `tests/fixtures/prompt_surface/tools/browser_console.json`
- ADDED `tests/fixtures/prompt_surface/tools/browser_dialog.json`
- ADDED `tests/fixtures/prompt_surface/tools/browser_exec.json`
- ADDED `tests/fixtures/prompt_surface/tools/browser_get_images.json`
- ADDED `tests/fixtures/prompt_surface/tools/browser_navigate.json`
- ADDED `tests/fixtures/prompt_surface/tools/browser_press.json`
- ADDED `tests/fixtures/prompt_surface/tools/browser_scroll.json`
- ADDED `tests/fixtures/prompt_surface/tools/browser_snapshot.json`
- ADDED `tests/fixtures/prompt_surface/tools/browser_type.json`
- ADDED `tests/fixtures/prompt_surface/tools/browser_vault_enter_code.json`
- ADDED `tests/fixtures/prompt_surface/tools/browser_vault_fill.json`
- ADDED `tests/fixtures/prompt_surface/tools/browser_vault_list.json`
- ADDED `tests/fixtures/prompt_surface/tools/browser_vault_save_login.json`
- ADDED `tests/fixtures/prompt_surface/tools/browser_vault_unlock.json`
- ADDED `tests/fixtures/prompt_surface/tools/browser_vision.json`
- ADDED `tests/fixtures/prompt_surface/tools/clarify.json`
- ADDED `tests/fixtures/prompt_surface/tools/delegate_task.json`
- ADDED `tests/fixtures/prompt_surface/tools/execute_code.json`
- ADDED `tests/fixtures/prompt_surface/tools/manage_connections.json`
- ADDED `tests/fixtures/prompt_surface/tools/memory.json`
- ADDED `tests/fixtures/prompt_surface/tools/patch.cli.gpt.json`
- ADDED `tests/fixtures/prompt_surface/tools/patch.json`
- ADDED `tests/fixtures/prompt_surface/tools/react_to_message.json`
- ADDED `tests/fixtures/prompt_surface/tools/read_file.json`
- ADDED `tests/fixtures/prompt_surface/tools/search_files.json`
- ADDED `tests/fixtures/prompt_surface/tools/skill_manage.json`
- ADDED `tests/fixtures/prompt_surface/tools/skill_view.json`
- ADDED `tests/fixtures/prompt_surface/tools/skills_list.json`
- ADDED `tests/fixtures/prompt_surface/tools/terminal.json`
- ADDED `tests/fixtures/prompt_surface/tools/text_to_speech.json`
- ADDED `tests/fixtures/prompt_surface/tools/tool_call.json`
- ADDED `tests/fixtures/prompt_surface/tools/tool_describe.json`
- ADDED `tests/fixtures/prompt_surface/tools/tool_search.desktop.claude.json`
- ADDED `tests/fixtures/prompt_surface/tools/tool_search.json`
- ADDED `tests/fixtures/prompt_surface/tools/vision_analyze.json`
- ADDED `tests/fixtures/prompt_surface/tools/web_extract.json`
- ADDED `tests/fixtures/prompt_surface/tools/web_search.json`
- ADDED `tests/fixtures/prompt_surface/tools/write_file.json`
- MODIFIED `tests/gateway/conftest.py`
- MODIFIED `tests/gateway/test_async_delegation_session_binding.py`
- ADDED `tests/gateway/test_child_notice_profile_admission.py`
- ADDED `tests/gateway/test_completion_admission_compression_race.py`
- ADDED `tests/gateway/test_completion_owner_retry.py`
- MODIFIED `tests/gateway/test_multiplex_routing_authz.py`
- MODIFIED `tests/gateway/test_platform_reconnect.py`
- ADDED `tests/nastech_cli/test_connectors_cmd.py`
- MODIFIED `tests/install/e2e-assets/source-driver.ps1`
- MODIFIED `tests/install/e2e-assets/source-update-command.sh`
- MODIFIED `tests/install/installer-script-e2e.sh`
- MODIFIED `tests/install/macos-desktop-e2e.sh`
- MODIFIED `tests/install/windows-e2e.ps1`
- MODIFIED `tests/scripts/test_code_health_cli.py`
- ADDED `tests/scripts/test_code_health_sleep_rule.py`
- MODIFIED `tests/scripts/test_job_groups.py`
- MODIFIED `tests/scripts/test_release_artifacts.py`
- MODIFIED `tests/scripts/test_release_channels.py`
- MODIFIED `tests/scripts/test_release_entrypoint.py`
- MODIFIED `tests/scripts/test_release_r2.py`
- MODIFIED `tests/scripts/test_release_sequencer.py`
- MODIFIED `tests/scripts/test_release_store.py`
- MODIFIED `tests/scripts/test_run_tests_parallel.py`
- ADDED `tests/scripts/test_scan_plugin_payloads.py`
- MODIFIED `tests/scripts/test_stable_admission.py`
- MODIFIED `tests/scripts/test_stable_release.py`
- ADDED `tests/tools/test_async_delegation_requeue.py`
- MODIFIED `tests/tools/test_browser_use_cli.py`
- ADDED `tests/tools/test_connector_accounts.py`
- MODIFIED `tests/tools/test_connectors_managed.py`
- ADDED `tests/tools/test_docker_backend_real.py`
- ADDED `tests/tools/test_local_persistent_shell.py`
- MODIFIED `tests/tools/test_plugin_guard.py`
- MODIFIED `tests/tools/test_ssh_environment.py`
- ADDED `tests/tui_gateway/test_connector_accounts_rpc.py`
- MODIFIED `tests/tui_gateway/test_protocol.py`
- MODIFIED `tests/tui_gateway/test_review_summary_callback.py`
- MODIFIED `tests/tui_gateway/test_session_profile_db.py`
- MODIFIED `tests/tui_gateway/test_tui_gateway_server.py`
- ADDED `tests/tui_gateway/test_tui_gateway_server_deep_truncate.py`
- ADDED `tests/waiting.py`
- MODIFIED `tools/async_delegation.py`
- MODIFIED `tools/browser_tool.py`
- MODIFIED `tools/browser_use_cli.py`
- MODIFIED `tools/code_execution_tool.py`
- MODIFIED `tools/connectors/account.py`
- MODIFIED `tools/connectors/dispatch.py`
- MODIFIED `tools/connectors/gateway/client.py`
- MODIFIED `tools/connectors/gateway/merge.py`
- MODIFIED `tools/connectors/gateway/wire.py`
- MODIFIED `tools/connectors/live.py`
- MODIFIED `tools/connectors/managed.py`
- MODIFIED `tools/connectors/operation.py`
- MODIFIED `tools/connectors/portal/client.py`
- MODIFIED `tools/connectors/targets.py`
- MODIFIED `tools/connectors/tool.py`
- MODIFIED `tools/environments/base.py`
- MODIFIED `tools/environments/base_session_env.py`
- MODIFIED `tools/environments/local.py`
- MODIFIED `tools/environments/ssh.py`
- MODIFIED `tools/file_tools.py`
- MODIFIED `tools/plugin_guard.py`
- MODIFIED `tools/plugin_guard_context.py`
- MODIFIED `tools/process_registry.py`
- MODIFIED `tools/process_registry_notifications.py`
- MODIFIED `tools/skills_guard.py`
- MODIFIED `tools/terminal_tool.py`
- MODIFIED `tools/terminal_tool_backends.py`
- MODIFIED `tools/terminal_tool_lifecycle.py`
- MODIFIED `tools/tool_labels.py`
- MODIFIED `tui_gateway/contracts/connectors.py`
- MODIFIED `tui_gateway/contracts/connectors_operation.py`
- MODIFIED `tui_gateway/contracts/prompt_voice.py`
- MODIFIED `tui_gateway/methods_connectors.py`
- MODIFIED `tui_gateway/methods_connectors_account.py`
- MODIFIED `tui_gateway/methods_prompt.py`
- MODIFIED `ui-tui/src/__tests__/completionApply.test.ts`
- ADDED `ui-tui/src/__tests__/connectorAccounts.test.ts`
- MODIFIED `ui-tui/src/app/connectionOperationStore.ts`
- MODIFIED `ui-tui/src/app/interfaces.ts`
- MODIFIED `ui-tui/src/app/overlayStore.ts`
- MODIFIED `ui-tui/src/app/slash/commands/core.ts`
- MODIFIED `ui-tui/src/app/slash/commands/ops.ts`
- MODIFIED `ui-tui/src/app/useInputHandlers.ts`
- MODIFIED `ui-tui/src/app/useSubmission.ts`
- MODIFIED `ui-tui/src/components/appOverlays.tsx`
- MODIFIED `ui-tui/src/components/connectionSetupOverlay.tsx`
- ADDED `ui-tui/src/components/connectorsOverlay.tsx`
- ADDED `ui-tui/src/domain/connectorAccounts.ts`
- MODIFIED `ui-tui/src/domain/slash.ts`
- MODIFIED `ui-tui/src/i18n/en.ts`
- MODIFIED `ui-tui/src/i18n/en/connection.ts`
- ADDED `ui-tui/src/i18n/en/connectors.ts`
- MODIFIED `ui-tui/src/i18n/en/slashCmd/core.ts`
- MODIFIED `website/docs/developer-guide/contributing.md`
- MODIFIED `website/docs/developer-guide/desktop-plugin-sdk.md`
- MODIFIED `website/docs/developer-guide/plugins/catalog-submission.md`
- MODIFIED `website/docs/developer-guide/programmatic-integration.md`
- MODIFIED `website/docs/developer-guide/prompt-assembly.md`
- MODIFIED `website/docs/developer-guide/stable-releases.md`
- MODIFIED `website/docs/getting-started/platform-support.md`
- MODIFIED `website/docs/reference/cli-commands.md`
- MODIFIED `website/docs/reference/environment-variables.md`
- MODIFIED `website/docs/reference/optional-skills-catalog.md`
- MODIFIED `website/docs/reference/slash-commands.md`
- MODIFIED `website/docs/reference/tools-reference.md`
- MODIFIED `website/docs/reference/toolsets-reference.md`
- MODIFIED `website/docs/user-guide/configuration.md`
- MODIFIED `website/docs/user-guide/desktop.md`
- MODIFIED `website/docs/user-guide/features/tool-gateway.md`
- MODIFIED `website/docs/user-guide/features/tool-search.md`
- ADDED `website/docs/user-guide/skills/optional/creative/creative-anatomy.md`
- MODIFIED `website/docs/user-guide/tui.md`
- MODIFIED `website/sidebars.ts`

## Scan

18406 files scanned [audio=5, binary=12, doc=4, font=13, image=265, text=18107]


## Diff

2907 renamed, 0 rewritten, 14735 identical, 66 locked, 0 missing, 118 owned, 416 reconciled


## Fork check (vs nastech-agent)

- 17994 identical, 230 updated (+0/-0 lines), 182 added, 0 missing, 0 fork-local-unpreserved, 0 stale-upstream, 0 locked/binary, 0 collision-safe relocated, 164 preserved fork-local files, 0 violations

- features: fork 56 -> branded 56

Auto-generated by 100Ways.
