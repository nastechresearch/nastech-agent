# Nastech Update Report #1

- upstream sha : `6f31cfad7825a78b69c46eedbd31f2ac2abacfb8`
- source       : `https://github.com/Nastechresearch/nastech-agent.git`
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

- total files : 9889
- renamed     : 1356 (folders and file names)
- text-rewritten : 9789
- locked-copied  : 57
- binary-copied  : 9
- owned assets   : 34 (our logo/banner/mascot override upstream)

## Reconcile

- fixed : 243 files reconciled: .github/workflows/deploy-site.yml, .github/workflows/skills-index-freshness.yml, .mailmap, CONTRIBUTING.es.md, CONTRIBUTING.md, Dockerfile, README.es.md, README.md, README.ur-pk.md, README.zh-CN.md, SECURITY.es.md, SECURITY.md, agent/agent_runtime_helpers.py, agent/anthropic_adapter.py, agent/auxiliary_client.py, agent/billing_links.py, agent/billing_view.py, agent/chat_completion_helpers.py, agent/conversation_loop.py, agent/credits_tracker.py, agent/model_metadata.py, agent/prompt_builder.py, agent/proxy_sources/iron_proxy.py, agent/subscription_view.py, agent/usage_pricing.py, apps/bootstrap-installer/src-tauri/Cargo.toml, apps/desktop/README.md, apps/desktop/electron/connection-config.test.ts, apps/desktop/electron/main.ts, apps/desktop/electron/remote-lifecycle.ts, apps/desktop/package.json, apps/desktop/src/app/messaging/index.test.tsx, apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx, apps/desktop/src/app/settings/about-settings.tsx, apps/desktop/src/app/settings/billing/api.test.ts, apps/desktop/src/app/settings/billing/dev-fixtures.ts, apps/desktop/src/app/settings/billing/errors.test.ts, apps/desktop/src/app/settings/billing/types.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.ts, apps/desktop/src/app/settings/billing/use-charge-poller.test.ts, apps/desktop/src/app/settings/billing/use-step-up.test.tsx, apps/desktop/src/app/settings/constants.ts, apps/desktop/src/app/settings/gateway-settings.tsx, apps/desktop/src/app/settings/toolset-config-panel.test.tsx, apps/desktop/src/app/skills/embedded-hub-picker.tsx, apps/desktop/src/app/skills/index.test.tsx, apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts, apps/desktop/src/contrib/plugin.ts, apps/desktop/src/i18n/en.ts, apps/desktop/src/i18n/ja.ts, apps/desktop/src/i18n/zh-hant.ts, apps/desktop/src/i18n/zh.ts, apps/desktop/src/plugins/nastech-bots/plugin.js, apps/desktop/src/sdk/index.ts, cli-config.yaml.example, eslint.config.shared.mjs, nastech_cli/auth.py, nastech_cli/banner.py, nastech_cli/config_defaults.py, nastech_cli/dashboard_register.py, nastech_cli/diagnostics_upload.py, nastech_cli/fallback_cmd.py, nastech_cli/kanban.py, nastech_cli/main.py, nastech_cli/model_catalog.py, nastech_cli/model_switch.py, nastech_cli/models.py, nastech_cli/nastech_account.py, nastech_cli/nastech_billing.py, nastech_cli/plugins_cmd.py, nastech_cli/portal_cli.py, nastech_cli/providers.py, nastech_cli/proxy/__init__.py, nastech_cli/proxy/adapters/base.py, nastech_cli/proxy/adapters/nastech_portal.py, nastech_cli/setup.py, nastech_cli/setup_whatsapp_cloud.py, nastech_cli/skin_engine.py, nastech_cli/telegram_managed_bot.py, nastech_cli/tools_config.py, nastech_cli/uninstall.py, nastech_cli/update_cmd.py, nastech_cli/web_server.py, nastech_constants.py, package-lock.json, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/plugin.yaml, plugins/kanban/dashboard/dist/index.js, plugins/kanban/systemd/nastech-kanban-dispatcher.service, plugins/model-providers/ai-gateway/__init__.py, plugins/model-providers/fireworks/__init__.py, plugins/model-providers/kimi-coding/__init__.py, plugins/model-providers/nastech/__init__.py, plugins/model-providers/opencode-zen/__init__.py, plugins/nastech-achievements/dashboard/dist/index.js, plugins/platforms/discord/adapter.py, plugins/platforms/email/adapter.py, plugins/platforms/photon/sidecar/package-lock.json, plugins/platforms/slack/adapter.py, run_agent.py, scripts/build_model_catalog.py, scripts/contributor_audit.py, scripts/dev-sandbox.sh, scripts/install.cmd, scripts/install.ps1, scripts/install.sh, scripts/release.py, scripts/whatsapp-bridge/package-lock.json, setup.py, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/references/background-systems.md, skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md, skills/autonomous-ai-agents/nastech-agent/references/configuration.md, skills/autonomous-ai-agents/nastech-agent/references/contributor-guide.md, skills/autonomous-ai-agents/nastech-agent/references/portal-auth-for-third-party-apps.md, skills/autonomous-ai-agents/nastech-agent/references/providers-and-models.md, skills/autonomous-ai-agents/nastech-agent/references/webhooks.md, tests/agent/test_anthropic_adapter.py, tests/agent/test_auxiliary_client.py, tests/agent/test_auxiliary_main_first.py, tests/agent/test_auxiliary_transport_autodetect.py, tests/agent/test_billing_links.py, tests/agent/test_credential_pool.py, tests/agent/test_credits_policy.py, tests/agent/test_error_classifier.py, tests/agent/test_model_metadata.py, tests/agent/test_nastech_credits_gauge.py, tests/agent/test_nastech_oauth_401_guidance.py, tests/agent/test_nastech_portal_anthropic_wire.py, tests/agent/transports/test_chat_completions.py, tests/cli/test_cli_first_run_setup.py, tests/cli/test_cli_provider_resolution.py, tests/cli/test_show_config_credential.py, tests/docker/test_sqlite_runtime.py, tests/gateway/test_discord_format.py, tests/gateway/test_run_progress_topics.py, tests/gateway/test_status_command.py, tests/gateway/test_usage_command.py, tests/nastech_cli/test_auth_nastech_provider.py, tests/nastech_cli/test_base_url_host_identity.py, tests/nastech_cli/test_dashboard_register.py, tests/nastech_cli/test_fireworks_provider.py, tests/nastech_cli/test_gateway_restart_loop.py, tests/nastech_cli/test_model_catalog.py, tests/nastech_cli/test_nastech_auth_keepalive.py, tests/nastech_cli/test_nastech_auth_status_cache.py, tests/nastech_cli/test_nastech_inference_url_validation.py, tests/nastech_cli/test_nastech_portal_staging_allowlist.py, tests/nastech_cli/test_nastech_reasoning_metadata.py, tests/nastech_cli/test_proxy.py, tests/nastech_cli/test_reasoning_caps_disk_cache.py, tests/nastech_cli/test_sale_pricing.py, tests/nastech_cli/test_web_oauth_dispatch.py, tests/plugins/dashboard_auth/test_nastech_provider.py, tests/plugins/image_gen/check_parity_vs_main.py, tests/plugins/image_gen/test_openrouter_compat_provider.py, tests/plugins/test_chronos_verify.py, tests/run_agent/test_anthropic_prompt_cache_policy.py, tests/run_agent/test_primary_runtime_restore.py, tests/run_agent/test_provider_attribution_headers.py, tests/run_agent/test_provider_fallback.py, tests/run_agent/test_provider_parity.py, tests/run_agent/test_run_agent.py, tests/run_agent/test_switch_model_reapplies_headers.py, tests/test_install_ps1_uv_powershell_host.py, tests/tools/test_delegate.py, tests/tools/test_managed_media_gateways.py, tests/tools/test_managed_tool_gateway.py, tests/tools/test_strict_provider_selection.py, tests/tools/test_tts_openai_config.py, tests/tools/test_url_safety.py, tests/tools/test_web_tools_config.py, tools/managed_tool_gateway.py, tools/mcp_oauth.py, tools/skills_hub.py, tools/skills_sync_client.py, trajectory_compressor.py, ui-tui/scripts/billing-fixtures.tsx, ui-tui/src/__tests__/subscriptionCommand.test.ts, ui-tui/src/__tests__/subscriptionOverlay.test.tsx, ui-tui/src/app/slash/commands/subscription.ts, ui-tui/src/domain/paths.ts, uv.lock, web/src/components/SidebarFooter.tsx, web/src/pages/DocsPage.tsx, web/src/pages/SystemPage.tsx, website/docs/developer-guide/contributing.md, website/docs/developer-guide/egress-internals.md, website/docs/getting-started/installation.md, website/docs/getting-started/platform-support.md, website/docs/getting-started/quickstart.md, website/docs/getting-started/termux.md, website/docs/guides/run-nastech-with-nastech-portal.md, website/docs/guides/run-nemotron-3-ultra-free.md, website/docs/index.mdx, website/docs/integrations/nastech-portal.md, website/docs/integrations/providers.md, website/docs/reference/cli-commands.md, website/docs/reference/environment-variables.md, website/docs/reference/faq.md, website/docs/reference/model-catalog.md, website/docs/user-guide/desktop.md, website/docs/user-guide/egress/iron-proxy.md, website/docs/user-guide/features/browser.md, website/docs/user-guide/features/image-generation.md, website/docs/user-guide/features/skills.md, website/docs/user-guide/features/subscription-proxy.md, website/docs/user-guide/features/tool-gateway.md, website/docs/user-guide/features/tools.md, website/docs/user-guide/features/tts.md, website/docs/user-guide/features/web-dashboard.md, website/docs/user-guide/features/web-search.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/windows-wsl-quickstart.md, website/docusaurus.config.ts, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/contributing.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/quickstart.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-nastech-with-nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/index.mdx, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/providers.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/faq.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/model-catalog.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/subscription-proxy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tools.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tts.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-native.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-wsl-quickstart.md, website/scripts/generate-llms-txt.py, website/scripts/prebuild.mjs, website/static/api/model-catalog.json, website/static/oauth/client-metadata.json


## Direct upstream tree delta

- complete: +82 ~269 -6 ↪0
- MODIFIED `AGENTS.md`
- MODIFIED `agent/auxiliary_client.py`
- MODIFIED `agent/context_compressor.py`
- MODIFIED `agent/conversation_compression.py`
- MODIFIED `agent/conversation_loop.py`
- MODIFIED `agent/manual_compression_feedback.py`
- MODIFIED `agent/model_metadata.py`
- MODIFIED `agent/prompt_builder.py`
- ADDED `agent/reasoning_effort.py`
- MODIFIED `agent/relay_llm.py`
- MODIFIED `agent/relay_runtime.py`
- MODIFIED `agent/skill_commands.py`
- MODIFIED `agent/system_prompt.py`
- MODIFIED `agent/tool_executor.py`
- MODIFIED `agent/tool_guardrails.py`
- MODIFIED `agent/transports/chat_completions.py`
- MODIFIED `agent/transports/codex.py`
- MODIFIED `agent/turn_context.py`
- MODIFIED `agent/web_search_provider.py`
- MODIFIED `agent/web_search_registry.py`
- MODIFIED `apps/desktop/DESIGN.md`
- MODIFIED `apps/desktop/electron/backend-start-failure.test.ts`
- MODIFIED `apps/desktop/electron/backend-start-failure.ts`
- MODIFIED `apps/desktop/electron/connection-registry.test.ts`
- MODIFIED `apps/desktop/electron/connection-registry.ts`
- MODIFIED `apps/desktop/electron/hud-ipc.ts`
- MODIFIED `apps/desktop/electron/main.ts`
- MODIFIED `apps/desktop/electron/native-auth-decisions.test.ts`
- MODIFIED `apps/desktop/electron/native-auth-decisions.ts`
- MODIFIED `apps/desktop/electron/preload.ts`
- MODIFIED `apps/desktop/electron/session-windows.test.ts`
- MODIFIED `apps/desktop/electron/session-windows.ts`
- MODIFIED `apps/desktop/electron/translucency.test.ts`
- MODIFIED `apps/desktop/electron/translucency.ts`
- MODIFIED `apps/desktop/src/app/chat/composer/composer-utils.ts`
- ADDED `apps/desktop/src/app/chat/composer/control-classes.ts`
- MODIFIED `apps/desktop/src/app/chat/composer/controls.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/controls.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/hooks/use-composer-metrics.ts`
- MODIFIED `apps/desktop/src/app/chat/composer/index.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/model-pill.tsx`
- ADDED `apps/desktop/src/app/chat/composer/voice-menu.tsx`
- MODIFIED `apps/desktop/src/app/chat/index.tsx`
- MODIFIED `apps/desktop/src/app/chat/session-status-dot.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/connection-switcher.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/connection-switcher.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/cron-jobs-section.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/index.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/projects/entered-content.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/session-actions-menu.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/session-actions-menu.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/session-row.tsx`
- ADDED `apps/desktop/src/app/chat/sidebar/strip-fts-markers.test.ts`
- MODIFIED `apps/desktop/src/app/command-center/maintenance.tsx`
- MODIFIED `apps/desktop/src/app/command-palette/index.tsx`
- MODIFIED `apps/desktop/src/app/context-menu/app-context-menu.test.tsx`
- MODIFIED `apps/desktop/src/app/context-menu/app-context-menu.tsx`
- MODIFIED `apps/desktop/src/app/contrib/wiring.tsx`
- MODIFIED `apps/desktop/src/app/cron/index.tsx`
- MODIFIED `apps/desktop/src/app/hud/glass.ts`
- MODIFIED `apps/desktop/src/app/hud/hud-shell.tsx`
- MODIFIED `apps/desktop/src/app/right-sidebar/review/index.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-actions/index.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-session-actions/remove-archived-session.test.tsx`
- MODIFIED `apps/desktop/src/app/settings/config-settings.tsx`
- MODIFIED `apps/desktop/src/app/settings/custom-endpoints-settings.tsx`
- MODIFIED `apps/desktop/src/app/settings/env-credentials.tsx`
- MODIFIED `apps/desktop/src/app/settings/index.tsx`
- MODIFIED `apps/desktop/src/app/settings/providers-settings.test.tsx`
- MODIFIED `apps/desktop/src/app/settings/providers-settings.tsx`
- MODIFIED `apps/desktop/src/app/settings/sessions-settings.tsx`
- MODIFIED `apps/desktop/src/app/settings/toolset-config-panel.tsx`
- MODIFIED `apps/desktop/src/app/shell/gateway-menu-panel.tsx`
- MODIFIED `apps/desktop/src/app/shell/model-catalog-menu.tsx`
- MODIFIED `apps/desktop/src/app/shell/model-edit-submenu.tsx`
- ADDED `apps/desktop/src/app/shell/statusbar-context-menu.test.tsx`
- MODIFIED `apps/desktop/src/app/shell/titlebar-controls.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/embeds/mermaid-embed.tsx`
- ADDED `apps/desktop/src/components/assistant-ui/markdown-table.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/markdown-text.tsx`
- ADDED `apps/desktop/src/components/confirm-host.test.tsx`
- ADDED `apps/desktop/src/components/confirm-host.tsx`
- MODIFIED `apps/desktop/src/components/pane-shell/tree/renderer/narrow-overlays.tsx`
- MODIFIED `apps/desktop/src/components/ui/badge.tsx`
- ADDED `apps/desktop/src/components/ui/confirm-dialog.test.tsx`
- MODIFIED `apps/desktop/src/components/ui/confirm-dialog.tsx`
- MODIFIED `apps/desktop/src/components/ui/context-menu.tsx`
- MODIFIED `apps/desktop/src/components/ui/dialog.tsx`
- ADDED `apps/desktop/src/components/ui/zoomable.test.tsx`
- MODIFIED `apps/desktop/src/components/ui/zoomable.tsx`
- MODIFIED `apps/desktop/src/global.d.ts`
- MODIFIED `apps/desktop/src/i18n/ar.ts`
- MODIFIED `apps/desktop/src/i18n/en.ts`
- MODIFIED `apps/desktop/src/i18n/ja.ts`
- MODIFIED `apps/desktop/src/i18n/types.ts`
- MODIFIED `apps/desktop/src/i18n/zh-hant.ts`
- MODIFIED `apps/desktop/src/i18n/zh.ts`
- MODIFIED `apps/desktop/src/lib/icons.ts`
- ADDED `apps/desktop/src/lib/markdown-table-widths.ts`
- ADDED `apps/desktop/src/lib/svg-image.test.ts`
- MODIFIED `apps/desktop/src/lib/svg-image.ts`
- ADDED `apps/desktop/src/plugins/accent/picker.tsx`
- ADDED `apps/desktop/src/plugins/accent/plugin.tsx`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/plugin.js`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/active-now-strip.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/canonical-chat-identity.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/canonical-chat-pin.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/group-chat.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/hide-bot-chats.test.mjs`
- ADDED `apps/desktop/src/plugins/nastech-bots/tests/mention-renamed-bots.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/session-workspace.test.mjs`
- MODIFIED `apps/desktop/src/sdk/index.ts`
- ADDED `apps/desktop/src/sdk/plugin-open-session-plan.test.ts`
- ADDED `apps/desktop/src/sdk/plugin-open-session-plan.ts`
- MODIFIED `apps/desktop/src/sdk/profile-routing.test.ts`
- MODIFIED `apps/desktop/src/store/backdrop.ts`
- ADDED `apps/desktop/src/store/confirm.ts`
- MODIFIED `apps/desktop/src/store/gateway.ts`
- MODIFIED `apps/desktop/src/store/projects.test.ts`
- MODIFIED `apps/desktop/src/store/projects.ts`
- MODIFIED `apps/desktop/src/store/session-dot-state.test.ts`
- MODIFIED `apps/desktop/src/store/session-dot-state.ts`
- MODIFIED `apps/desktop/src/store/session-request-router.test.ts`
- MODIFIED `apps/desktop/src/store/session-request-router.ts`
- MODIFIED `apps/desktop/src/store/session-states.ts`
- MODIFIED `apps/desktop/src/store/translucency.test.ts`
- MODIFIED `apps/desktop/src/store/translucency.ts`
- MODIFIED `apps/desktop/src/store/updates.test.ts`
- MODIFIED `apps/desktop/src/store/updates.ts`
- MODIFIED `apps/desktop/src/store/windows.test.ts`
- MODIFIED `apps/desktop/src/store/windows.ts`
- MODIFIED `apps/desktop/src/styles.css`
- ADDED `apps/desktop/src/themes/accent-override.ts`
- MODIFIED `apps/desktop/src/themes/color.ts`
- MODIFIED `apps/desktop/src/themes/context.test.tsx`
- MODIFIED `apps/desktop/src/themes/context.tsx`
- MODIFIED `apps/desktop/src/themes/presets.ts`
- MODIFIED `apps/desktop/src/themes/profile-theme.test.ts`
- ADDED `apps/desktop/src/themes/retint.test.ts`
- ADDED `apps/desktop/src/themes/retint.ts`
- MODIFIED `apps/desktop/src/types/nastech.ts`
- MODIFIED `apps/shared/src/translucency.ts`
- MODIFIED `cli-config.yaml.example`
- MODIFIED `cli.py`
- ADDED `contributors/emails/582149912@qq.com`
- ADDED `contributors/emails/cassie@omg.lol`
- ADDED `contributors/emails/contact@grahfmusic.com`
- ADDED `contributors/emails/dhruv.modi2345@gmail.com`
- ADDED `contributors/emails/erick@kinnee.net`
- ADDED `contributors/emails/lakshya.agarwal@tavily.com`
- ADDED `contributors/emails/zhangcw1989@gmail.com`
- ADDED `default.tar.gz`
- MODIFIED `docs/middleware/README.md`
- MODIFIED `docs/observability/README.md`
- MODIFIED `docs/observability/monitoring.md`
- MODIFIED `docs/observability/relay-shared-metrics.md`
- MODIFIED `gateway/platforms/api_server.py`
- MODIFIED `gateway/platforms/base.py`
- MODIFIED `gateway/relay/adapter.py`
- MODIFIED `gateway/relay/ws_transport.py`
- MODIFIED `gateway/run.py`
- MODIFIED `gateway/stream_consumer.py`
- MODIFIED `nastech_cli/auth.py`
- MODIFIED `nastech_cli/auth_commands.py`
- MODIFIED `nastech_cli/backup.py`
- MODIFIED `nastech_cli/bundles.py`
- MODIFIED `nastech_cli/cli_commands_mixin.py`
- MODIFIED `nastech_cli/cli_output.py`
- MODIFIED `nastech_cli/commands.py`
- MODIFIED `nastech_cli/config.py`
- MODIFIED `nastech_cli/config_defaults.py`
- MODIFIED `nastech_cli/config_migrations.py`
- MODIFIED `nastech_cli/copilot_auth.py`
- MODIFIED `nastech_cli/doctor.py`
- MODIFIED `nastech_cli/foreign_sessions.py`
- MODIFIED `nastech_cli/gateway.py`
- MODIFIED `nastech_cli/inventory.py`
- MODIFIED `nastech_cli/main.py`
- MODIFIED `nastech_cli/memory_setup.py`
- MODIFIED `nastech_cli/model_setup_flows.py`
- MODIFIED `nastech_cli/models.py`
- MODIFIED `nastech_cli/nastech_subscription.py`
- MODIFIED `nastech_cli/oneshot.py`
- MODIFIED `nastech_cli/plugins.py`
- MODIFIED `nastech_cli/plugins_cmd.py`
- MODIFIED `nastech_cli/pt_input_extras.py`
- ADDED `nastech_cli/relay_plugin_cutover.py`
- MODIFIED `nastech_cli/sessions_cmd.py`
- MODIFIED `nastech_cli/setup.py`
- MODIFIED `nastech_cli/setup_whatsapp_cloud.py`
- MODIFIED `nastech_cli/skills_hub.py`
- MODIFIED `nastech_cli/tools_config.py`
- ADDED `nastech_cli/worktree_cmd.py`
- ADDED `nastech_cli/worktree_gc.py`
- MODIFIED `nastech_state.py`
- MODIFIED `plugins/image_gen/openai-codex/__init__.py`
- MODIFIED `plugins/model-providers/custom/__init__.py`
- MODIFIED `plugins/model-providers/deepseek/__init__.py`
- MODIFIED `plugins/model-providers/kimi-coding/__init__.py`
- MODIFIED `plugins/model-providers/meta-ai/__init__.py`
- MODIFIED `plugins/model-providers/nastech/__init__.py`
- MODIFIED `plugins/model-providers/ollama-cloud/__init__.py`
- MODIFIED `plugins/model-providers/opencode-zen/__init__.py`
- MODIFIED `plugins/model-providers/upstage/__init__.py`
- MODIFIED `plugins/model-providers/zai/__init__.py`
- DELETED `plugins/observability/nemo_relay/README.md`
- DELETED `plugins/observability/nemo_relay/__init__.py`
- DELETED `plugins/observability/nemo_relay/plugin.yaml`
- MODIFIED `plugins/platforms/a2a/tools.py`
- MODIFIED `plugins/platforms/telegram/adapter.py`
- MODIFIED `plugins/web/exa/provider.py`
- MODIFIED `plugins/web/firecrawl/plugin.yaml`
- MODIFIED `plugins/web/firecrawl/provider.py`
- ADDED `plugins/web/keenable/__init__.py`
- ADDED `plugins/web/keenable/plugin.yaml`
- ADDED `plugins/web/keenable/provider.py`
- ADDED `plugins/web/keyless_mcp.py`
- MODIFIED `plugins/web/parallel/provider.py`
- MODIFIED `plugins/web/tavily/plugin.yaml`
- MODIFIED `plugins/web/tavily/provider.py`
- MODIFIED `run_agent.py`
- MODIFIED `scripts/toolperf_abeval/README.md`
- MODIFIED `scripts/toolperf_abeval/ab_eval.py`
- ADDED `tests/agent/test_builtin_memory_disabled_surface.py`
- MODIFIED `tests/agent/test_compaction_anti_thrash.py`
- ADDED `tests/agent/test_manual_compression_refusal_feedback.py`
- ADDED `tests/agent/test_reasoning_effort_module.py`
- MODIFIED `tests/agent/test_relay_llm.py`
- MODIFIED `tests/agent/test_relay_runtime_bounded_scope_ops.py`
- ADDED `tests/agent/test_relay_runtime_plugins.py`
- MODIFIED `tests/agent/test_relay_session_segments.py`
- MODIFIED `tests/agent/test_relay_tools.py`
- ADDED `tests/agent/test_salvage_grown_transcript.py`
- MODIFIED `tests/agent/test_skill_commands.py`
- MODIFIED `tests/agent/test_stall_guards.py`
- ADDED `tests/agent/test_uncompressed_context_guardrail.py`
- MODIFIED `tests/agent/transports/test_chat_completions.py`
- MODIFIED `tests/agent/transports/test_reasoning_effort_sibling_sites.py`
- MODIFIED `tests/cli/test_cli_init.py`
- MODIFIED `tests/cli/test_cli_yolo_toggle.py`
- MODIFIED `tests/cli/test_ctrl_enter_newline.py`
- MODIFIED `tests/cli/test_modify_other_keys_aliases.py`
- ADDED `tests/cli/test_show_config_credential.py`
- ADDED `tests/cli/test_slash_undo_title_robustness.py`
- MODIFIED `tests/cli/test_worktree.py`
- MODIFIED `tests/gateway/relay/stub_connector.py`
- ADDED `tests/gateway/relay/test_live_cards_flow_trace.py`
- ADDED `tests/gateway/relay/test_relay_ack_ambiguity.py`
- MODIFIED `tests/gateway/relay/test_relay_adapter.py`
- ADDED `tests/gateway/relay/test_relay_inbound_dedupe.py`
- ADDED `tests/gateway/relay/test_relay_live_cards.py`
- ADDED `tests/gateway/relay/test_relay_multiplatform_semantics.py`
- MODIFIED `tests/gateway/relay/test_relay_roundtrip_telegram.py`
- ADDED `tests/gateway/relay/test_relay_seal_cancellation.py`
- ADDED `tests/gateway/relay/test_relay_state_bounds.py`
- ADDED `tests/gateway/relay/test_relay_stream_semantics_gating.py`
- ADDED `tests/gateway/relay/test_relay_task_card_failures.py`
- ADDED `tests/gateway/relay/test_relay_turn_keying.py`
- ADDED `tests/gateway/relay/test_ws_transport_hardening.py`
- ADDED `tests/gateway/test_api_server_reasoning_ladder.py`
- ADDED `tests/gateway/test_draft_id_restart_uniqueness.py`
- ADDED `tests/gateway/test_interim_send_lanes.py`
- MODIFIED `tests/gateway/test_notice_delivery.py`
- ADDED `tests/gateway/test_relay_seal_failure.py`
- MODIFIED `tests/gateway/test_slack.py`
- ADDED `tests/gateway/test_slack_turn_recipient_identity.py`
- ADDED `tests/gateway/test_split_final_suffix_reconcile.py`
- MODIFIED `tests/gateway/test_stale_finalize_suppression.py`
- ADDED `tests/gateway/test_stream_abandon_on_turn_death.py`
- MODIFIED `tests/gateway/test_stream_consumer_draft.py`
- ADDED `tests/gateway/test_stream_final_adoption_gate.py`
- ADDED `tests/gateway/test_stream_final_contract.py`
- ADDED `tests/gateway/test_telegram_polling_health_confirmation.py`
- MODIFIED `tests/nastech_cli/test_api_key_providers.py`
- ADDED `tests/nastech_cli/test_backup_path_errors.py`
- MODIFIED `tests/nastech_cli/test_cli_output.py`
- ADDED `tests/nastech_cli/test_config_set_coercion.py`
- MODIFIED `tests/nastech_cli/test_copilot_auth.py`
- MODIFIED `tests/nastech_cli/test_deprecated_cwd_warning.py`
- MODIFIED `tests/nastech_cli/test_doctor.py`
- ADDED `tests/nastech_cli/test_hatch_prompt_thread_safety.py`
- ADDED `tests/nastech_cli/test_inventory_reasoning_caps.py`
- MODIFIED `tests/nastech_cli/test_memory_setup.py`
- ADDED `tests/nastech_cli/test_nastech_reasoning_metadata.py`
- MODIFIED `tests/nastech_cli/test_nastech_subscription.py`
- ADDED `tests/nastech_cli/test_oneshot_skills.py`
- MODIFIED `tests/nastech_cli/test_plugins.py`
- MODIFIED `tests/nastech_cli/test_plugins_cmd_enable_disable_nested.py`
- ADDED `tests/nastech_cli/test_prune_spares_pinned.py`
- ADDED `tests/nastech_cli/test_reasoning_caps_disk_cache.py`
- ADDED `tests/nastech_cli/test_relay_plugin_cutover.py`
- MODIFIED `tests/nastech_cli/test_sale_pricing.py`
- ADDED `tests/nastech_cli/test_sessions_error_exit_codes.py`
- MODIFIED `tests/nastech_cli/test_set_config_value.py`
- MODIFIED `tests/nastech_cli/test_terminal_menu_fallbacks.py`
- MODIFIED `tests/nastech_cli/test_worktree_command.py`
- ADDED `tests/nastech_cli/test_worktree_gc.py`
- MODIFIED `tests/plugins/image_gen/test_openai_codex_provider.py`
- ADDED `tests/plugins/model_providers/test_nastech_profile.py`
- MODIFIED `tests/plugins/model_providers/test_ollama_cloud_profile.py`
- MODIFIED `tests/plugins/model_providers/test_opencode_go_profile.py`
- ADDED `tests/plugins/test_a2a_schema_registration.py`
- DELETED `tests/plugins/test_nemo_relay_bounded_marks.py`
- DELETED `tests/plugins/test_nemo_relay_mark_turn_parenting.py`
- DELETED `tests/plugins/test_nemo_relay_plugin.py`
- MODIFIED `tests/plugins/web/test_web_search_provider_plugins.py`
- MODIFIED `tests/providers/test_transport_parity.py`
- MODIFIED `tests/run_agent/test_callable_api_key.py`
- MODIFIED `tests/run_agent/test_compression_budget_refund.py`
- MODIFIED `tests/run_agent/test_in_place_compaction.py`
- MODIFIED `tests/run_agent/test_run_agent.py`
- MODIFIED `tests/test_desktop_update_windows_progress.py`
- MODIFIED `tests/test_output_cap_parsing.py`
- MODIFIED `tests/tools/test_computer_use.py`
- ADDED `tests/tools/test_rollback_all_directories.py`
- ADDED `tests/tools/test_web_keyless_fallback.py`
- MODIFIED `tests/tools/test_web_providers.py`
- MODIFIED `tests/tools/test_web_providers_searxng.py`
- MODIFIED `tests/tools/test_web_tools_config.py`
- MODIFIED `tests/tools/test_web_tools_tavily.py`
- MODIFIED `tests/tui_gateway/test_profiles_list_preferred_session.py`
- ADDED `tests/tui_gateway/test_profiles_list_worker_session.py`
- MODIFIED `tests/tui_gateway/test_projects_rpc.py`
- MODIFIED `tools/checkpoint_manager.py`
- MODIFIED `tools/computer_use/schema.py`
- MODIFIED `tools/computer_use/tool.py`
- MODIFIED `tools/memory_tool.py`
- MODIFIED `tools/tool_result_storage.py`
- MODIFIED `tools/web_tools.py`
- MODIFIED `tui_gateway/methods_config.py`
- MODIFIED `tui_gateway/methods_profiles.py`
- MODIFIED `tui_gateway/server.py`
- MODIFIED `ui-tui/packages/nastech-ink/src/ink/components/App.tsx`
- MODIFIED `ui-tui/packages/nastech-ink/src/ink/ink.tsx`
- MODIFIED `ui-tui/packages/nastech-ink/src/ink/terminal.test.ts`
- MODIFIED `ui-tui/packages/nastech-ink/src/ink/terminal.ts`
- MODIFIED `website/docs/integrations/index.md`
- MODIFIED `website/docs/integrations/nastech-portal.md`
- MODIFIED `website/docs/reference/environment-variables.md`
- MODIFIED `website/docs/user-guide/bot-mode.md`
- MODIFIED `website/docs/user-guide/cli.md`
- MODIFIED `website/docs/user-guide/configuration.md`
- MODIFIED `website/docs/user-guide/desktop.md`
- MODIFIED `website/docs/user-guide/features/browser.md`
- MODIFIED `website/docs/user-guide/features/built-in-plugins.md`
- MODIFIED `website/docs/user-guide/features/computer-use.md`
- MODIFIED `website/docs/user-guide/features/image-generation.md`
- MODIFIED `website/docs/user-guide/features/memory.md`
- MODIFIED `website/docs/user-guide/features/tool-gateway.md`
- MODIFIED `website/docs/user-guide/features/tts.md`
- MODIFIED `website/docs/user-guide/features/web-search.md`
- MODIFIED `website/docs/user-guide/messaging/whatsapp-cloud.md`
- MODIFIED `website/docs/user-guide/multi-connection-desktop.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md`

## Scan

9943 files scanned [archive=1, audio=5, binary=7, doc=5, font=13, image=93, text=9819]


## Diff

1273 renamed, 0 rewritten, 8281 identical, 63 locked, 0 missing, 34 owned, 238 reconciled


## Fork check (vs nastech-agent)

- 9468 identical, 393 updated (+0/-0 lines), 82 added, 0 missing, 0 fork-local-unpreserved, 0 stale-upstream, 0 locked/binary, 0 collision-safe relocated, 54 preserved fork-local files, 0 violations

- features: fork 51 -> branded 51

Auto-generated by 100Ways.
