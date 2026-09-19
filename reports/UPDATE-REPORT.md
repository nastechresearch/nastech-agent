# Nastech Update Report #1

- upstream sha : `8df0a03793784205833f9e0db12395aa33ada433`
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

- total files : 14104
- renamed     : 2384 (folders and file names)
- text-rewritten : 14002
- locked-copied  : 60
- binary-copied  : 8
- owned assets   : 34 (our logo/banner/mascot override upstream)

## Reconcile

- fixed : 340 files reconciled: .github/workflows/deploy-site.yml, .github/workflows/deploy-site.yml, .github/workflows/install-e2e-macos-run.yml, .github/workflows/install-e2e-windows-run.yml, .github/workflows/skills-index-freshness.yml, .mailmap, CONTRIBUTING.es.md, CONTRIBUTING.md, Dockerfile, README.es.md, README.md, README.ur-pk.md, README.zh-CN.md, SECURITY.es.md, SECURITY.md, agent/agent_runtime_helpers.py, agent/anthropic_adapter.py, agent/anthropic_endpoints.py, agent/auxiliary_client.py, agent/billing_links.py, agent/billing_view.py, agent/chat_completion_helpers.py, agent/conversation_compression.py, agent/conversation_loop.py, agent/model_metadata.py, agent/prompt_builder.py, agent/proxy_sources/iron_proxy.py, agent/reasoning_params.py, agent/subscription_view.py, agent/turn_recovery.py, agent/usage_pricing.py, apps/bootstrap-installer/src-tauri/Cargo.toml, apps/desktop/README.md, apps/desktop/electron/backend-health.test.ts, apps/desktop/electron/backend-health.ts, apps/desktop/electron/connection-config.test.ts, apps/desktop/electron/main.ts, apps/desktop/electron/oauth-partition.test.ts, apps/desktop/electron/remote-lifecycle.ts, apps/desktop/electron/remote-oauth-ticket.test.ts, apps/desktop/package.json, apps/desktop/src/app/messaging/index.test.tsx, apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx, apps/desktop/src/app/settings/about-settings.tsx, apps/desktop/src/app/settings/billing/api.test.ts, apps/desktop/src/app/settings/billing/dev-fixtures.ts, apps/desktop/src/app/settings/billing/errors.test.ts, apps/desktop/src/app/settings/billing/types.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.ts, apps/desktop/src/app/settings/billing/use-charge-poller.test.ts, apps/desktop/src/app/settings/billing/use-step-up.test.tsx, apps/desktop/src/app/settings/constants.ts, apps/desktop/src/app/settings/gateway-settings.tsx, apps/desktop/src/app/settings/toolset-config-panel.test.tsx, apps/desktop/src/app/skills/embedded-hub-picker.tsx, apps/desktop/src/app/skills/index.test.tsx, apps/desktop/src/app/skills/plugins-tab.test.tsx, apps/desktop/src/app/skills/plugins-tab.tsx, apps/desktop/src/app/updates-overlay.tsx, apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts, apps/desktop/src/components/boot-failure-overlay.test.tsx, apps/desktop/src/components/boot-failure-overlay.tsx, apps/desktop/src/components/send-diagnostics-dialog.tsx, apps/desktop/src/contrib/plugin.ts, apps/desktop/src/i18n/en.ts, apps/desktop/src/i18n/ja.ts, apps/desktop/src/i18n/ru.ts, apps/desktop/src/i18n/zh-hant.ts, apps/desktop/src/i18n/zh.ts, apps/desktop/src/plugins/nastech-bots/skills-hub-picker.test.tsx, apps/desktop/src/plugins/nastech-bots/skills-hub.tsx, apps/desktop/src/sdk/index.ts, cli-config.yaml.example, eslint.config.shared.mjs, evals/auth_pool_controls.py, evals/browser_use/single_run.py, evals/postmortem/live_ab/auth_stampede.py, evals/postmortem/live_ab/cache_concurrency_probe.py, evals/postmortem/review_probes/cache_estimator_probe.py, evals/postmortem/review_probes/credential_identity_probe.py, gateway/run_notifications.py, nastech_cli/anon_auth.py, nastech_cli/anon_auth.py, nastech_cli/anon_sign_in.py, nastech_cli/auth.py, nastech_cli/auth_codex.py, nastech_cli/auth_constants.py, nastech_cli/auth_error_copy.py, nastech_cli/auth_nastech.py, nastech_cli/banner.py, nastech_cli/config_defaults.py, nastech_cli/dashboard_auth/login_page.py, nastech_cli/dashboard_register.py, nastech_cli/debug.py, nastech_cli/diagnostics_upload.py, nastech_cli/fallback_cmd.py, nastech_cli/kanban_parser.py, nastech_cli/main.py, nastech_cli/main_dashboard.py, nastech_cli/model_catalog.py, nastech_cli/model_setup_flows_common.py, nastech_cli/models.py, nastech_cli/models_pricing.py, nastech_cli/nastech_account.py, nastech_cli/nastech_account.py, nastech_cli/nastech_billing.py, nastech_cli/observability/shared_metrics_send_config.py, nastech_cli/plugin_catalog.py, nastech_cli/plugins_cmd.py, nastech_cli/portal_cli.py, nastech_cli/providers.py, nastech_cli/proxy/adapters/base.py, nastech_cli/proxy/adapters/nastech_portal.py, nastech_cli/setup.py, nastech_cli/setup_platforms.py, nastech_cli/setup_quick.py, nastech_cli/setup_whatsapp_cloud.py, nastech_cli/skin_engine.py, nastech_cli/subcommands/egress.py, nastech_cli/subcommands/fallback.py, nastech_cli/subcommands/secrets.py, nastech_cli/subcommands/worktree.py, nastech_cli/telegram_managed_bot.py, nastech_cli/tools_config.py, nastech_cli/uninstall.py, nastech_cli/update_cmd.py, nastech_cli/update_cmd_deps.py, nastech_cli/update_cmd_maint.py, nastech_cli/update_cmd_zip.py, nastech_cli/web_routers/status.py, nastech_cli/web_server_messaging.py, nastech_cli/web_server_oauth.py, nastech_constants.py, package-lock.json, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/plugin.yaml, plugins/kanban/dashboard/dist/index.js, plugins/kanban/systemd/nastech-kanban-dispatcher.service, plugins/model-providers/ai-gateway/__init__.py, plugins/model-providers/fireworks/__init__.py, plugins/model-providers/kimi-coding/__init__.py, plugins/model-providers/nastech/__init__.py, plugins/model-providers/opencode-zen/__init__.py, plugins/nastech-achievements/dashboard/dist/index.js, plugins/platforms/discord/adapter.py, plugins/platforms/email/adapter.py, plugins/platforms/photon/sidecar/package-lock.json, plugins/platforms/slack/adapter.py, plugins/web/perplexity/provider.py, scripts/build_model_catalog.py, scripts/contributor_audit.py, scripts/e2e_shared_metrics_staging.py, scripts/install.cmd, scripts/install.ps1, scripts/install.sh, scripts/release.py, scripts/sandbox/generate-e2e-matrix.mjs, scripts/whatsapp-bridge/package-lock.json, setup.py, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/references/background-systems.md, skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md, skills/autonomous-ai-agents/nastech-agent/references/configuration.md, skills/autonomous-ai-agents/nastech-agent/references/contributor-guide.md, skills/autonomous-ai-agents/nastech-agent/references/portal-auth-for-third-party-apps.md, skills/autonomous-ai-agents/nastech-agent/references/providers-and-models.md, skills/autonomous-ai-agents/nastech-agent/references/webhooks.md, tests/agent/test_anthropic_adapter.py, tests/agent/test_anthropic_prompt_cache_policy.py, tests/agent/test_auxiliary_auth_rung_fallthrough.py, tests/agent/test_auxiliary_client.py, tests/agent/test_auxiliary_client_nastech_401_cache_key.py, tests/agent/test_auxiliary_main_first.py, tests/agent/test_auxiliary_transport_autodetect.py, tests/agent/test_billing_links.py, tests/agent/test_credential_pool.py, tests/agent/test_credential_pool_nastech_refresh_stampede.py, tests/agent/test_credits_policy.py, tests/agent/test_deepseek_anthropic_thinking.py, tests/agent/test_error_classifier.py, tests/agent/test_fast_mode_auto.py, tests/agent/test_model_metadata.py, tests/agent/test_nastech_credits_gauge.py, tests/agent/test_nastech_key_pre_expiry_adoption.py, tests/agent/test_nastech_oauth_401_guidance.py, tests/agent/test_nastech_portal_anthropic_wire.py, tests/agent/test_nastech_rate_guard.py, tests/agent/test_nastech_welcome_client_contract.py, tests/agent/test_nastech_wire_auto.py, tests/agent/test_nonretryable_result_carries_verdict.py, tests/agent/test_phantom_tool_references.py, tests/agent/test_primary_runtime_restore.py, tests/agent/test_provider_attribution_headers.py, tests/agent/test_provider_fallback.py, tests/agent/test_provider_parity.py, tests/agent/test_run_agent.py, tests/agent/test_switch_model_reapplies_headers.py, tests/agent/test_turn_usage_log_line.py, tests/agent/test_welcome_error_identity.py, tests/agent/test_welcome_tier_recovery.py, tests/agent/transports/test_chat_completions.py, tests/docker/test_sqlite_runtime.py, tests/gateway/test_discord_format.py, tests/gateway/test_free_tier_startup_notice.py, tests/gateway/test_free_tier_startup_notice.py, tests/gateway/test_run_progress_topics.py, tests/gateway/test_startup_warmup_profile_scope.py, tests/gateway/test_status_command.py, tests/gateway/test_status_free_tier_line.py, tests/gateway/test_telegram_mention_context.py, tests/gateway/test_usage_command.py, tests/install/macos-desktop-e2e.sh, tests/install/windows-e2e.ps1, tests/nastech_cli/anon_portal.py, tests/nastech_cli/test_anon_auth_core.py, tests/nastech_cli/test_anon_failure_modes.py, tests/nastech_cli/test_anon_failure_modes.py, tests/nastech_cli/test_anon_first_notice.py, tests/nastech_cli/test_anon_picker.py, tests/nastech_cli/test_anon_surfaces.py, tests/nastech_cli/test_anon_surfaces.py, tests/nastech_cli/test_anon_upgrade.py, tests/nastech_cli/test_auth_nastech_provider.py, tests/nastech_cli/test_base_url_host_identity.py, tests/nastech_cli/test_cli_first_run_setup.py, tests/nastech_cli/test_cli_init.py, tests/nastech_cli/test_cli_provider_resolution.py, tests/nastech_cli/test_dashboard_auth_gate.py, tests/nastech_cli/test_dashboard_register.py, tests/nastech_cli/test_fireworks_provider.py, tests/nastech_cli/test_local_abandoned_requests.py, tests/nastech_cli/test_local_quickstart.py, tests/nastech_cli/test_model_catalog.py, tests/nastech_cli/test_model_validation.py, tests/nastech_cli/test_nastech_anthropic_wire_default.py, tests/nastech_cli/test_nastech_auth_keepalive.py, tests/nastech_cli/test_nastech_auth_status_cache.py, tests/nastech_cli/test_nastech_inference_url_validation.py, tests/nastech_cli/test_nastech_nonproduction_inference_host.py, tests/nastech_cli/test_nastech_nonproduction_inference_host.py, tests/nastech_cli/test_nastech_portal_staging_allowlist.py, tests/nastech_cli/test_nastech_reasoning_metadata.py, tests/nastech_cli/test_proxy.py, tests/nastech_cli/test_reasoning_caps_disk_cache.py, tests/nastech_cli/test_sale_pricing.py, tests/nastech_cli/test_show_config_credential.py, tests/nastech_cli/test_ux_messages_auth_config.py, tests/nastech_cli/test_web_oauth_dispatch.py, tests/plugins/dashboard_auth/test_nastech_provider.py, tests/plugins/image_gen/check_parity_vs_main.py, tests/plugins/image_gen/test_openrouter_compat_provider.py, tests/plugins/test_chronos_verify.py, tests/scripts/install/test_install_ps1_uv_powershell_host.py, tests/tools/test_delegate.py, tests/tools/test_managed_media_gateways.py, tests/tools/test_managed_tool_gateway.py, tests/tools/test_stage2_hook_nastech_routing_env.py, tests/tools/test_strict_provider_selection.py, tests/tools/test_tts_openai_config.py, tests/tools/test_url_safety.py, tests/tools/test_web_tools_config.py, tests/tools/test_web_tools_perplexity.py, tests/tui_gateway/test_free_tier_rpc.py, tools/managed_gateway_auth.py, tools/managed_tool_gateway.py, tools/mcp_oauth.py, tools/skills_hub_search.py, tools/skills_sync_client.py, trajectory_compressor.py, ui-tui/scripts/billing-fixtures.tsx, ui-tui/src/__tests__/subscriptionCommand.test.ts, ui-tui/src/__tests__/subscriptionOverlay.test.tsx, ui-tui/src/app/slash/commands/subscription.ts, ui-tui/src/domain/paths.ts, uv.lock, web/src/components/SidebarFooter.tsx, web/src/pages/DocsPage.tsx, web/src/pages/PluginsPage.tsx, web/src/pages/SystemPage.tsx, website/README.md, website/docs/developer-guide/contributing.md, website/docs/developer-guide/egress-internals.md, website/docs/getting-started/installation.md, website/docs/getting-started/platform-support.md, website/docs/getting-started/quickstart.md, website/docs/getting-started/termux.md, website/docs/guides/manage-nastech-cloud-with-mcp.md, website/docs/guides/run-nastech-with-nastech-portal.md, website/docs/guides/run-nemotron-3-ultra-free.md, website/docs/index.mdx, website/docs/integrations/nastech-portal.md, website/docs/integrations/providers.md, website/docs/reference/cli-commands.md, website/docs/reference/environment-variables.md, website/docs/reference/faq.md, website/docs/reference/model-catalog.md, website/docs/user-guide/desktop.md, website/docs/user-guide/egress/iron-proxy.md, website/docs/user-guide/features/browser.md, website/docs/user-guide/features/image-generation.md, website/docs/user-guide/features/plugin-catalog.md, website/docs/user-guide/features/skills.md, website/docs/user-guide/features/subscription-proxy.md, website/docs/user-guide/features/tool-gateway.md, website/docs/user-guide/features/tools.md, website/docs/user-guide/features/tts.md, website/docs/user-guide/features/web-dashboard.md, website/docs/user-guide/features/web-search.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/windows-wsl-quickstart.md, website/docusaurus.config.ts, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/contributing.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/quickstart.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-nastech-with-nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/index.mdx, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/providers.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/faq.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/model-catalog.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/subscription-proxy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tools.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tts.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-native.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-wsl-quickstart.md, website/scripts/fetch-plugin-stars.py, website/scripts/generate-llms-txt.py, website/scripts/prebuild.mjs, website/static/api/model-catalog.json, website/static/oauth/client-metadata.json


## Direct upstream tree delta

- complete: +17 ~106 -12 ↪0
- MODIFIED `agent/agent_init.py`
- MODIFIED `agent/agent_runtime_helpers.py`
- MODIFIED `agent/anthropic_credentials.py`
- MODIFIED `agent/context_compressor.py`
- MODIFIED `agent/conversation_loop.py`
- MODIFIED `agent/credential_pool.py`
- MODIFIED `agent/turn_final_response.py`
- MODIFIED `apps/desktop/DESIGN.md`
- MODIFIED `apps/desktop/src/app/chat/sidebar/project-dialog.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/project-dialog.tsx`
- MODIFIED `apps/desktop/src/app/contrib/hooks/use-desktop-integrations.test.tsx`
- MODIFIED `apps/desktop/src/app/contrib/hooks/use-desktop-integrations.ts`
- MODIFIED `apps/desktop/src/app/gateway/hooks/use-gateway-boot.ts`
- MODIFIED `apps/desktop/src/app/master-detail.tsx`
- MODIFIED `apps/desktop/src/app/settings/plugin-install-modal.test.tsx`
- DELETED `apps/desktop/src/app/skills/capability-tabs.tsx`
- DELETED `apps/desktop/src/app/skills/catalog-browser.test.tsx`
- DELETED `apps/desktop/src/app/skills/catalog-browser.tsx`
- DELETED `apps/desktop/src/app/skills/catalog-data.test.ts`
- DELETED `apps/desktop/src/app/skills/catalog-data.ts`
- ADDED `apps/desktop/src/app/skills/embedded-hub-picker.tsx`
- MODIFIED `apps/desktop/src/app/skills/index.test.tsx`
- MODIFIED `apps/desktop/src/app/skills/index.tsx`
- MODIFIED `apps/desktop/src/app/skills/plugins-tab.test.tsx`
- MODIFIED `apps/desktop/src/app/skills/plugins-tab.tsx`
- DELETED `apps/desktop/src/app/skills/skill-catalog.tsx`
- MODIFIED `apps/desktop/src/app/skills/store.ts`
- DELETED `apps/desktop/src/app/skills/update-skills-button.tsx`
- MODIFIED `apps/desktop/src/components/confirm-host.test.tsx`
- MODIFIED `apps/desktop/src/components/confirm-host.tsx`
- MODIFIED `apps/desktop/src/components/ui/confirm-dialog.tsx`
- DELETED `apps/desktop/src/components/ui/segmented-control.test.tsx`
- MODIFIED `apps/desktop/src/components/ui/segmented-control.tsx`
- MODIFIED `apps/desktop/src/i18n/ar.ts`
- MODIFIED `apps/desktop/src/i18n/en.ts`
- MODIFIED `apps/desktop/src/i18n/ja.ts`
- MODIFIED `apps/desktop/src/i18n/ru.ts`
- MODIFIED `apps/desktop/src/i18n/types.ts`
- MODIFIED `apps/desktop/src/i18n/zh-hant.ts`
- MODIFIED `apps/desktop/src/i18n/zh.ts`
- DELETED `apps/desktop/src/lib/catalog-install.test.ts`
- MODIFIED `apps/desktop/src/lib/deeplink-routes.test.ts`
- MODIFIED `apps/desktop/src/lib/deeplink-routes.ts`
- MODIFIED `apps/desktop/src/lib/gateway-liveness-policy.ts`
- MODIFIED `apps/desktop/src/lib/nastech-open-target.test.ts`
- MODIFIED `apps/desktop/src/lib/nastech-open-target.ts`
- MODIFIED `apps/desktop/src/lib/query-client.ts`
- MODIFIED `apps/desktop/src/store/confirm.ts`
- MODIFIED `apps/desktop/src/store/gateway-activation-prune-lease.test.ts`
- MODIFIED `apps/desktop/src/store/gateway-connection-lifecycle.test.ts`
- MODIFIED `apps/desktop/src/store/gateway-connection-scope.test.ts`
- MODIFIED `apps/desktop/src/store/gateway-foreground-retention.test.ts`
- MODIFIED `apps/desktop/src/store/gateway.ts`
- MODIFIED `apps/desktop/src/store/session-request-router.test.ts`
- DELETED `apps/desktop/src/store/skill-deeplink-install.test.ts`
- DELETED `apps/desktop/src/store/skill-deeplink-install.ts`
- DELETED `apps/shared/src/catalog-install.ts`
- MODIFIED `apps/shared/src/index.ts`
- ADDED `apps/shared/src/json-rpc-gateway-connect.test.ts`
- MODIFIED `apps/shared/src/json-rpc-gateway.ts`
- MODIFIED `cli.py`
- ADDED `contributors/emails/155116265+psam-717@users.noreply.github.com`
- ADDED `contributors/emails/anton.vykhovanets@icloud.com`
- ADDED `contributors/emails/brandan@wrengineers.com`
- ADDED `contributors/emails/italo.feernandes@gmail.com`
- ADDED `contributors/emails/patrickeliasrs@gmail.com`
- MODIFIED `gateway/AGENTS.md`
- MODIFIED `gateway/authz_mixin.py`
- MODIFIED `gateway/config.py`
- MODIFIED `gateway/kanban_watchers_notifier.py`
- MODIFIED `gateway/platforms/ADDING_A_PLATFORM.md`
- MODIFIED `gateway/platforms/base.py`
- MODIFIED `gateway/platforms/weixin.py`
- MODIFIED `gateway/platforms/yuanbao.py`
- MODIFIED `gateway/profile_routing.py`
- MODIFIED `gateway/run.py`
- MODIFIED `gateway/run_adapters.py`
- MODIFIED `gateway/run_inbound.py`
- MODIFIED `gateway/run_topics.py`
- MODIFIED `gateway/run_voice.py`
- ADDED `gateway/session_identity.py`
- MODIFIED `gateway/session_recovery.py`
- MODIFIED `nastech_cli/kanban_db_notify.py`
- MODIFIED `nastech_cli/model_switch.py`
- MODIFIED `nastech_cli/sessions_cmd.py`
- ADDED `nastech_cli/sessions_cmd_repair_profiles.py`
- ADDED `nastech_cli/sessions_repair_profiles.py`
- MODIFIED `nastech_cli/subcommands/sessions.py`
- MODIFIED `nastech_state.py`
- ADDED `nastech_state_profile_repair.py`
- MODIFIED `plugins/platforms/raft/adapter.py`
- MODIFIED `plugins/platforms/slack/adapter.py`
- MODIFIED `plugins/platforms/telegram/adapter.py`
- MODIFIED `scripts/check_profile_scope_patterns.py`
- MODIFIED `scripts/ci/profile_scope_patterns.json`
- MODIFIED `tests/agent/test_anthropic_borrowed_row_authority.py`
- MODIFIED `tests/agent/test_anthropic_keychain.py`
- MODIFIED `tests/agent/test_auxiliary_client.py`
- ADDED `tests/agent/test_degenerate_final_recovery.py`
- MODIFIED `tests/agent/test_ollama_num_ctx.py`
- MODIFIED `tests/agent/test_strip_reasoning_tags_cli.py`
- MODIFIED `tests/conftest.py`
- ADDED `tests/gateway/test_adapter_session_key_seam.py`
- MODIFIED `tests/gateway/test_heartbeat_watch_restore.py`
- ADDED `tests/gateway/test_identity_canonical_ingress.py`
- MODIFIED `tests/gateway/test_kanban_routed_transport.py`
- MODIFIED `tests/gateway/test_multiplex_session_db_profile_scope.py`
- MODIFIED `tests/gateway/test_profile_resolution.py`
- MODIFIED `tests/gateway/test_profile_routing.py`
- ADDED `tests/gateway/test_session_identity.py`
- MODIFIED `tests/gateway/test_slack.py`
- MODIFIED `tests/gateway/test_teams.py`
- MODIFIED `tests/gateway/test_voice_command.py`
- MODIFIED `tests/nastech_cli/test_kanban_notify.py`
- MODIFIED `tests/nastech_cli/test_model_switch_custom_providers.py`
- ADDED `tests/nastech_cli/test_sessions_repair_profiles.py`
- MODIFIED `tests/scripts/test_check_profile_scope_patterns.py`
- ADDED `tests/tui_gateway/test_out_of_band_history_adoption.py`
- MODIFIED `tests/tui_gateway/test_tui_gateway_server.py`
- MODIFIED `tests/website/test_extract_skills.py`
- MODIFIED `tui_gateway/prompt_turn.py`
- MODIFIED `tui_gateway/session_reaper.py`
- MODIFIED `website/docs/developer-guide/multiplexing-gateway.md`
- MODIFIED `website/docs/reference/cli-commands.md`
- MODIFIED `website/docs/user-guide/desktop.md`
- MODIFIED `website/docs/user-guide/features/plugin-catalog.md`
- MODIFIED `website/docs/user-guide/features/plugins.md`
- MODIFIED `website/docs/user-guide/features/skills.md`
- MODIFIED `website/docs/user-guide/multi-profile-gateways.md`
- MODIFIED `website/docs/user-guide/sessions.md`
- MODIFIED `website/scripts/extract-skills.py`
- MODIFIED `website/src/pages/plugins/index.tsx`
- MODIFIED `website/src/pages/plugins/styles.module.css`
- MODIFIED `website/src/pages/skills/index.tsx`
- MODIFIED `website/src/pages/skills/styles.module.css`

## Scan

14160 files scanned [audio=5, binary=7, doc=4, font=13, image=97, text=14034]


## Diff

2253 renamed, 0 rewritten, 11425 identical, 64 locked, 0 missing, 34 owned, 328 reconciled


## Fork check (vs nastech-agent)

- 14037 identical, 106 updated (+0/-0 lines), 17 added, 0 missing, 0 fork-local-unpreserved, 0 stale-upstream, 0 locked/binary, 0 collision-safe relocated, 56 preserved fork-local files, 0 violations

- features: fork 54 -> branded 54

Auto-generated by 100Ways.
