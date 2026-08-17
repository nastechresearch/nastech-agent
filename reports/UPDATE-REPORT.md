# Nastech Update Report #1

- upstream sha : `d66341ab28635d9eecbd30a18d50801d927153b8`
- source       : `https://github.com/NousResearch/hermes-agent.git`
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

- total files : 9478
- renamed     : 1278 (folders and file names)
- text-rewritten : 8734
- locked-copied  : 704
- binary-copied  : 8
- owned assets   : 32 (our logo/banner/mascot override upstream)

## Reconcile

- fixed : 231 files reconciled: .github/workflows/deploy-site.yml, .github/workflows/skills-index-freshness.yml, .mailmap, CONTRIBUTING.es.md, CONTRIBUTING.md, Dockerfile, README.es.md, README.md, README.ur-pk.md, README.zh-CN.md, SECURITY.es.md, SECURITY.md, agent/agent_runtime_helpers.py, agent/anthropic_adapter.py, agent/auxiliary_client.py, agent/billing_links.py, agent/billing_view.py, agent/chat_completion_helpers.py, agent/conversation_loop.py, agent/credits_tracker.py, agent/model_metadata.py, agent/prompt_builder.py, agent/proxy_sources/iron_proxy.py, agent/subscription_view.py, agent/usage_pricing.py, apps/bootstrap-installer/src-tauri/Cargo.toml, apps/desktop/README.md, apps/desktop/electron/connection-config.test.ts, apps/desktop/electron/main.ts, apps/desktop/electron/remote-lifecycle.ts, apps/desktop/package.json, apps/desktop/src/app/messaging/index.test.tsx, apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx, apps/desktop/src/app/settings/billing/api.test.ts, apps/desktop/src/app/settings/billing/dev-fixtures.ts, apps/desktop/src/app/settings/billing/errors.test.ts, apps/desktop/src/app/settings/billing/types.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.ts, apps/desktop/src/app/settings/billing/use-charge-poller.test.ts, apps/desktop/src/app/settings/billing/use-step-up.test.tsx, apps/desktop/src/app/settings/constants.ts, apps/desktop/src/app/settings/gateway-settings.tsx, apps/desktop/src/app/settings/toolset-config-panel.test.tsx, apps/desktop/src/app/skills/embedded-hub-picker.tsx, apps/desktop/src/app/skills/index.test.tsx, apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts, apps/desktop/src/i18n/en.ts, apps/desktop/src/i18n/ja.ts, apps/desktop/src/i18n/zh-hant.ts, apps/desktop/src/i18n/zh.ts, apps/desktop/src/plugins/nastech-bots/plugin.js, cli-config.yaml.example, eslint.config.shared.mjs, nastech_cli/auth.py, nastech_cli/config_defaults.py, nastech_cli/dashboard_register.py, nastech_cli/diagnostics_upload.py, nastech_cli/fallback_cmd.py, nastech_cli/kanban.py, nastech_cli/main.py, nastech_cli/model_catalog.py, nastech_cli/model_switch.py, nastech_cli/models.py, nastech_cli/nastech_account.py, nastech_cli/nastech_billing.py, nastech_cli/plugins_cmd.py, nastech_cli/portal_cli.py, nastech_cli/providers.py, nastech_cli/proxy/__init__.py, nastech_cli/proxy/adapters/base.py, nastech_cli/proxy/adapters/nastech_portal.py, nastech_cli/setup.py, nastech_cli/setup_whatsapp_cloud.py, nastech_cli/telegram_managed_bot.py, nastech_cli/tools_config.py, nastech_cli/uninstall.py, nastech_cli/update_cmd.py, nastech_cli/web_server.py, nastech_constants.py, package-lock.json, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/plugin.yaml, plugins/kanban/dashboard/dist/index.js, plugins/kanban/systemd/nastech-kanban-dispatcher.service, plugins/model-providers/ai-gateway/__init__.py, plugins/model-providers/fireworks/__init__.py, plugins/model-providers/kimi-coding/__init__.py, plugins/model-providers/nastech/__init__.py, plugins/model-providers/opencode-zen/__init__.py, plugins/nastech-achievements/dashboard/dist/index.js, plugins/platforms/discord/adapter.py, plugins/platforms/email/adapter.py, plugins/platforms/slack/adapter.py, run_agent.py, scripts/build_model_catalog.py, scripts/contributor_audit.py, scripts/dev-sandbox.sh, scripts/install.cmd, scripts/install.ps1, scripts/install.sh, scripts/release.py, setup.py, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/references/background-systems.md, skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md, skills/autonomous-ai-agents/nastech-agent/references/configuration.md, skills/autonomous-ai-agents/nastech-agent/references/contributor-guide.md, skills/autonomous-ai-agents/nastech-agent/references/portal-auth-for-third-party-apps.md, skills/autonomous-ai-agents/nastech-agent/references/providers-and-models.md, skills/autonomous-ai-agents/nastech-agent/references/webhooks.md, tests/agent/test_anthropic_adapter.py, tests/agent/test_auxiliary_client.py, tests/agent/test_auxiliary_main_first.py, tests/agent/test_auxiliary_transport_autodetect.py, tests/agent/test_billing_links.py, tests/agent/test_credential_pool.py, tests/agent/test_credits_policy.py, tests/agent/test_error_classifier.py, tests/agent/test_model_metadata.py, tests/agent/test_nastech_credits_gauge.py, tests/agent/test_nastech_oauth_401_guidance.py, tests/agent/test_nastech_portal_anthropic_wire.py, tests/agent/transports/test_chat_completions.py, tests/cli/test_cli_first_run_setup.py, tests/cli/test_cli_provider_resolution.py, tests/docker/test_sqlite_runtime.py, tests/gateway/test_discord_format.py, tests/gateway/test_run_progress_topics.py, tests/gateway/test_status_command.py, tests/gateway/test_usage_command.py, tests/nastech_cli/test_auth_nastech_provider.py, tests/nastech_cli/test_base_url_host_identity.py, tests/nastech_cli/test_dashboard_register.py, tests/nastech_cli/test_fireworks_provider.py, tests/nastech_cli/test_gateway_restart_loop.py, tests/nastech_cli/test_model_catalog.py, tests/nastech_cli/test_nastech_auth_keepalive.py, tests/nastech_cli/test_nastech_auth_status_cache.py, tests/nastech_cli/test_nastech_inference_url_validation.py, tests/nastech_cli/test_nastech_portal_staging_allowlist.py, tests/nastech_cli/test_proxy.py, tests/nastech_cli/test_sale_pricing.py, tests/nastech_cli/test_web_oauth_dispatch.py, tests/plugins/dashboard_auth/test_nastech_provider.py, tests/plugins/image_gen/check_parity_vs_main.py, tests/plugins/image_gen/test_openrouter_compat_provider.py, tests/plugins/test_chronos_verify.py, tests/run_agent/test_anthropic_prompt_cache_policy.py, tests/run_agent/test_primary_runtime_restore.py, tests/run_agent/test_provider_attribution_headers.py, tests/run_agent/test_provider_fallback.py, tests/run_agent/test_provider_parity.py, tests/run_agent/test_run_agent.py, tests/run_agent/test_switch_model_reapplies_headers.py, tests/test_install_ps1_uv_powershell_host.py, tests/tools/test_delegate.py, tests/tools/test_managed_media_gateways.py, tests/tools/test_managed_tool_gateway.py, tests/tools/test_tts_openai_config.py, tests/tools/test_url_safety.py, tests/tools/test_web_tools_config.py, tools/managed_tool_gateway.py, tools/mcp_oauth.py, tools/skills_hub.py, tools/skills_sync_client.py, trajectory_compressor.py, ui-tui/scripts/billing-fixtures.tsx, ui-tui/src/__tests__/subscriptionCommand.test.ts, ui-tui/src/__tests__/subscriptionOverlay.test.tsx, ui-tui/src/app/slash/commands/subscription.ts, ui-tui/src/domain/paths.ts, uv.lock, web/src/components/SidebarFooter.tsx, web/src/pages/DocsPage.tsx, web/src/pages/SystemPage.tsx, website/docs/developer-guide/contributing.md, website/docs/developer-guide/egress-internals.md, website/docs/getting-started/installation.md, website/docs/getting-started/platform-support.md, website/docs/getting-started/quickstart.md, website/docs/getting-started/termux.md, website/docs/guides/run-nastech-with-nastech-portal.md, website/docs/guides/run-nemotron-3-ultra-free.md, website/docs/index.mdx, website/docs/integrations/nastech-portal.md, website/docs/integrations/providers.md, website/docs/reference/cli-commands.md, website/docs/reference/environment-variables.md, website/docs/reference/faq.md, website/docs/reference/model-catalog.md, website/docs/user-guide/desktop.md, website/docs/user-guide/egress/iron-proxy.md, website/docs/user-guide/features/browser.md, website/docs/user-guide/features/image-generation.md, website/docs/user-guide/features/skills.md, website/docs/user-guide/features/subscription-proxy.md, website/docs/user-guide/features/tool-gateway.md, website/docs/user-guide/features/tools.md, website/docs/user-guide/features/tts.md, website/docs/user-guide/features/web-dashboard.md, website/docs/user-guide/features/web-search.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/windows-wsl-quickstart.md, website/docusaurus.config.ts, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/contributing.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/quickstart.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-nastech-with-nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/index.mdx, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/providers.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/faq.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/model-catalog.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/subscription-proxy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tools.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tts.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-native.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-wsl-quickstart.md, website/scripts/generate-llms-txt.py, website/scripts/prebuild.mjs, website/static/api/model-catalog.json


## Direct upstream tree delta

- complete: +70 ~147 -0 ↪0
- MODIFIED `.gitignore`
- MODIFIED `agent/agent_init.py`
- MODIFIED `agent/background_review.py`
- MODIFIED `agent/conversation_loop.py`
- MODIFIED `agent/model_metadata.py`
- MODIFIED `agent/prompt_builder.py`
- MODIFIED `agent/skill_commands.py`
- MODIFIED `agent/system_prompt.py`
- MODIFIED `agent/tool_executor.py`
- MODIFIED `agent/turn_finalizer.py`
- MODIFIED `apps/desktop/README.md`
- MODIFIED `apps/desktop/electron/backend-connection-state.test.ts`
- MODIFIED `apps/desktop/electron/backend-connection-state.ts`
- MODIFIED `apps/desktop/electron/backend-start-failure.test.ts`
- MODIFIED `apps/desktop/electron/backend-start-failure.ts`
- MODIFIED `apps/desktop/electron/connection-config.test.ts`
- MODIFIED `apps/desktop/electron/connection-config.ts`
- MODIFIED `apps/desktop/electron/connection-registry.test.ts`
- MODIFIED `apps/desktop/electron/connection-registry.ts`
- MODIFIED `apps/desktop/electron/gateway-ws-probe.test.ts`
- MODIFIED `apps/desktop/electron/gateway-ws-probe.ts`
- MODIFIED `apps/desktop/electron/main.ts`
- ADDED `apps/desktop/electron/plugin-profile-routes.test.ts`
- ADDED `apps/desktop/electron/plugin-profile-routes.ts`
- ADDED `apps/desktop/electron/pool-touch-scope.test.ts`
- ADDED `apps/desktop/electron/pool-touch-scope.ts`
- MODIFIED `apps/desktop/electron/preload.ts`
- MODIFIED `apps/desktop/electron/ssh-bootstrap-coordinator.test.ts`
- MODIFIED `apps/desktop/electron/ssh-bootstrap-coordinator.ts`
- MODIFIED `apps/desktop/electron/ssh-connection.test.ts`
- MODIFIED `apps/desktop/electron/ssh-connection.ts`
- MODIFIED `apps/desktop/package.json`
- ADDED `apps/desktop/scripts/local-pack-publish.test.mjs`
- MODIFIED `apps/desktop/src/app/chat/composer/controls.tsx`
- MODIFIED `apps/desktop/src/app/gateway/hooks/use-gateway-boot.test.tsx`
- MODIFIED `apps/desktop/src/app/gateway/hooks/use-gateway-boot.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/gateway-event.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-message-stream/steer-arrival-order.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/utils.test.ts`
- MODIFIED `apps/desktop/src/app/settings/connections-settings.tsx`
- ADDED `apps/desktop/src/app/shell/gateway-menu-panel.test.tsx`
- MODIFIED `apps/desktop/src/app/shell/gateway-menu-panel.tsx`
- MODIFIED `apps/desktop/src/app/skills/mcp-tab.tsx`
- MODIFIED `apps/desktop/src/contrib/plugins.ts`
- MODIFIED `apps/desktop/src/contrib/runtime-loader.ts`
- MODIFIED `apps/desktop/src/global.d.ts`
- MODIFIED `apps/desktop/src/hermes-cron-scope.test.ts`
- MODIFIED `apps/desktop/src/hermes.test.ts`
- MODIFIED `apps/desktop/src/hermes.ts`
- MODIFIED `apps/desktop/src/i18n/ar.ts`
- MODIFIED `apps/desktop/src/i18n/en.ts`
- MODIFIED `apps/desktop/src/i18n/ja.ts`
- MODIFIED `apps/desktop/src/i18n/types.ts`
- MODIFIED `apps/desktop/src/i18n/zh-hant.ts`
- MODIFIED `apps/desktop/src/i18n/zh.ts`
- ADDED `apps/desktop/src/lib/connection-scoped.ts`
- MODIFIED `apps/desktop/src/lib/mcp-import.test.ts`
- ADDED `apps/desktop/src/lib/steered-turn-hydration-order.test.ts`
- ADDED `apps/desktop/src/plugin-socket-scope.test.ts`
- ADDED `apps/desktop/src/plugins/hermes-bots/LICENSE`
- ADDED `apps/desktop/src/plugins/hermes-bots/plugin.js`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/active-now-strip.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/activity-toasts.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/bot-delete.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/bot-meta-asset-sync.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/bot-meta-hydrate.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/bot-meta-persistence.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/bot-meta-sync.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/bots-search.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/canonical-chat-creation.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/canonical-chat-empty-recovery.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/canonical-chat-pin.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/create-agent-clone-default.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/create-agent-mcp-setup.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/draft-agent-discard.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/duplicate-bot.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/embed-real-capabilities.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/embed-skills-view.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/group-chat.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/hide-bot-chats.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/hub-picker-guard.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/legacy-sdk-compat.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/mention-handoff-quoting.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/model-inherit.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/multi-source-roster.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/new-compact-guard.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/pet-fetch.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/profile-prewarm.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/roster-groups.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/roster-preview.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/routine-owner.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/routine-prompt.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/routines-error.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/routines-pause-failure.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/routines-profile-scope.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/session-workspace.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/single-flight.test.mjs`
- ADDED `apps/desktop/src/plugins/hermes-bots/tests/soul-protocol-backfill.test.mjs`
- MODIFIED `apps/desktop/src/sdk/index.test.ts`
- MODIFIED `apps/desktop/src/sdk/index.ts`
- ADDED `apps/desktop/src/sdk/profile-routing.test.ts`
- MODIFIED `apps/desktop/src/store/boot.ts`
- MODIFIED `apps/desktop/src/store/gateway-agent-scope.test.ts`
- MODIFIED `apps/desktop/src/store/gateway-connection-lifecycle.test.ts`
- ADDED `apps/desktop/src/store/gateway-connection-scope.test.ts`
- ADDED `apps/desktop/src/store/gateway-profile-request.test.ts`
- ADDED `apps/desktop/src/store/gateway-reconnect.test.ts`
- ADDED `apps/desktop/src/store/gateway-reconnect.ts`
- MODIFIED `apps/desktop/src/store/gateway-shared-remote.test.ts`
- MODIFIED `apps/desktop/src/store/gateway-switch.test.ts`
- MODIFIED `apps/desktop/src/store/gateway-switch.ts`
- MODIFIED `apps/desktop/src/store/gateway.ts`
- ADDED `apps/desktop/src/store/layout-connection-scope.test.ts`
- MODIFIED `apps/desktop/src/store/layout.ts`
- MODIFIED `apps/desktop/src/store/mcp-health.ts`
- MODIFIED `apps/desktop/src/store/profile-agent-activation.test.ts`
- MODIFIED `apps/desktop/src/store/profile.test.ts`
- MODIFIED `apps/desktop/src/store/profile.ts`
- MODIFIED `apps/desktop/src/store/session-pin-sync.ts`
- ADDED `apps/desktop/src/store/session-states-scopes.test.ts`
- MODIFIED `apps/desktop/src/store/session-states.ts`
- MODIFIED `apps/desktop/src/store/session.ts`
- MODIFIED `apps/desktop/src/types/hermes.ts`
- MODIFIED `apps/shared/src/backend-scope.ts`
- MODIFIED `apps/shared/src/index.ts`
- MODIFIED `apps/shared/src/json-rpc-gateway.ts`
- MODIFIED `cli-config.yaml.example`
- ADDED `contributors/emails/50810385+tigercraft4@users.noreply.github.com`
- ADDED `contributors/emails/604maestro@protonmail.com`
- ADDED `contributors/emails/ahamoudhy@gmail.com`
- ADDED `contributors/emails/hello@jpanganiban.com`
- ADDED `contributors/emails/yukinomon@users.noreply.github.com`
- MODIFIED `gateway/platforms/base.py`
- MODIFIED `gateway/run.py`
- MODIFIED `gateway/status.py`
- MODIFIED `hermes_cli/__init__.py`
- MODIFIED `hermes_cli/config_defaults.py`
- MODIFIED `hermes_cli/dashboard_procs.py`
- MODIFIED `hermes_cli/gateway.py`
- MODIFIED `hermes_cli/main.py`
- MODIFIED `hermes_cli/tools_config.py`
- MODIFIED `hermes_cli/update_cmd.py`
- MODIFIED `hermes_cli/web_routers/cron.py`
- MODIFIED `hermes_cli/web_server.py`
- MODIFIED `hermes_state.py`
- MODIFIED `plugins/image_gen/krea/__init__.py`
- MODIFIED `pyproject.toml`
- MODIFIED `run_agent.py`
- MODIFIED `scripts/install.ps1`
- MODIFIED `scripts/install.sh`
- MODIFIED `skills/autonomous-ai-agents/computer-use/SKILL.md`
- MODIFIED `tests/agent/test_async_token_accounting.py`
- MODIFIED `tests/agent/test_background_review_usage.py`
- MODIFIED `tests/agent/test_model_metadata.py`
- MODIFIED `tests/agent/test_reasoning_stale_timeout_floor.py`
- ADDED `tests/agent/test_sequential_tool_interrupt.py`
- MODIFIED `tests/agent/test_skill_commands.py`
- MODIFIED `tests/gateway/test_media_tag_cleanup.py`
- MODIFIED `tests/gateway/test_multiplex_adapter_registry.py`
- MODIFIED `tests/gateway/test_stale_platform_lock_retryable.py`
- MODIFIED `tests/gateway/test_status.py`
- ADDED `tests/hermes_cli/test_computer_use_cli.py`
- MODIFIED `tests/hermes_cli/test_cron_fire_dashboard.py`
- MODIFIED `tests/hermes_cli/test_gateway_service.py`
- MODIFIED `tests/hermes_cli/test_install_cua_driver.py`
- MODIFIED `tests/hermes_cli/test_post_setup_gating.py`
- MODIFIED `tests/hermes_cli/test_update_fleet_restart_timeout.py`
- MODIFIED `tests/hermes_cli/test_update_stale_dashboard.py`
- MODIFIED `tests/hermes_cli/test_web_routers_tools_install_on_enable.py`
- MODIFIED `tests/hermes_cli/test_web_server_gateway_topology.py`
- MODIFIED `tests/plugins/image_gen/test_krea_provider.py`
- MODIFIED `tests/run_agent/test_agent_guardrails.py`
- MODIFIED `tests/run_agent/test_background_review.py`
- MODIFIED `tests/run_agent/test_background_review_cost_controls.py`
- MODIFIED `tests/run_agent/test_turn_completion_explainer.py`
- MODIFIED `tests/test_install_scripts_computer_use.py`
- ADDED `tests/test_session_db_context_manager.py`
- ADDED `tests/tools/test_bot_mode_probe.py`
- MODIFIED `tests/tools/test_computer_use.py`
- MODIFIED `tests/tools/test_computer_use_browser_authorization.py`
- ADDED `tests/tools/test_computer_use_browser_contract_020.py`
- MODIFIED `tests/tools/test_computer_use_cua_0_10_permissions.py`
- MODIFIED `tests/tools/test_computer_use_cua_0_9.py`
- MODIFIED `tests/tools/test_delegation_live_log.py`
- MODIFIED `tests/tools/test_image_generation.py`
- ADDED `tests/tools/test_image_generation_interrupt.py`
- MODIFIED `tests/tui_gateway/test_protocol.py`
- ADDED `tools/bot_mode_probe.py`
- MODIFIED `tools/computer_use/browser_route.py`
- MODIFIED `tools/computer_use/cua_backend.py`
- MODIFIED `tools/computer_use/schema.py`
- MODIFIED `tools/computer_use/tool.py`
- MODIFIED `tools/delegate_tool.py`
- MODIFIED `tools/delegation_live_log.py`
- MODIFIED `tools/image_generation_tool.py`
- MODIFIED `tui_gateway/methods_profiles.py`
- MODIFIED `tui_gateway/methods_tools.py`
- MODIFIED `tui_gateway/server.py`
- MODIFIED `ui-tui/packages/hermes-ink/src/ink/parse-keypress.test.ts`
- MODIFIED `ui-tui/packages/hermes-ink/src/ink/parse-keypress.ts`
- ADDED `ui-tui/packages/hermes-ink/src/ink/termio/parser.test.ts`
- MODIFIED `ui-tui/packages/hermes-ink/src/ink/termio/tokenize.test.ts`
- MODIFIED `ui-tui/packages/hermes-ink/src/ink/termio/tokenize.ts`
- MODIFIED `ui-tui/src/__tests__/terminalParity.test.ts`
- MODIFIED `ui-tui/src/__tests__/terminalSetup.test.ts`
- ADDED `ui-tui/src/__tests__/textInputReturnAction.test.ts`
- MODIFIED `ui-tui/src/components/textInput.tsx`
- MODIFIED `ui-tui/src/lib/terminalSetup.ts`
- MODIFIED `uv.lock`
- MODIFIED `website/docs/developer-guide/desktop-plugin-sdk.md`
- MODIFIED `website/docs/reference/cli-commands.md`
- MODIFIED `website/docs/user-guide/desktop.md`
- MODIFIED `website/docs/user-guide/features/computer-use.md`
- MODIFIED `website/docs/user-guide/features/image-generation.md`
- MODIFIED `website/docs/user-guide/features/memory.md`
- MODIFIED `website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-computer-use.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md`

## Scan

9541 files scanned [audio=5, binary=7, doc=5, font=13, image=91, text=9420]


## Diff

1201 renamed, 0 rewritten, 7310 identical, 707 locked, 0 missing, 32 owned, 228 reconciled


## Fork check (vs nastech-agent)

- 9198 identical, 270 updated (+0/-0 lines), 70 added, 0 missing, 0 fork-local-unpreserved, 0 stale-upstream, 3 locked/binary, 63 preserved fork-local files, 0 violations

- features: fork 51 -> branded 51

Auto-generated by 100Ways.
