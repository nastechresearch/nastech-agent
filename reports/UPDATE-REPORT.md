# Nastech Update Report #1

- upstream sha : `28803e68b452d39435c89b148407d327e91b0735`
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

- total files : 9784
- renamed     : 1336 (folders and file names)
- text-rewritten : 9685
- locked-copied  : 57
- binary-copied  : 8
- owned assets   : 34 (our logo/banner/mascot override upstream)

## Reconcile

- fixed : 239 files reconciled: .github/workflows/deploy-site.yml, .github/workflows/skills-index-freshness.yml, .mailmap, CONTRIBUTING.es.md, CONTRIBUTING.md, Dockerfile, README.es.md, README.md, README.ur-pk.md, README.zh-CN.md, SECURITY.es.md, SECURITY.md, agent/agent_runtime_helpers.py, agent/anthropic_adapter.py, agent/auxiliary_client.py, agent/billing_links.py, agent/billing_view.py, agent/chat_completion_helpers.py, agent/conversation_loop.py, agent/credits_tracker.py, agent/model_metadata.py, agent/prompt_builder.py, agent/proxy_sources/iron_proxy.py, agent/subscription_view.py, agent/usage_pricing.py, apps/bootstrap-installer/src-tauri/Cargo.toml, apps/desktop/README.md, apps/desktop/electron/connection-config.test.ts, apps/desktop/electron/main.ts, apps/desktop/electron/remote-lifecycle.ts, apps/desktop/package.json, apps/desktop/src/app/messaging/index.test.tsx, apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx, apps/desktop/src/app/settings/about-settings.tsx, apps/desktop/src/app/settings/billing/api.test.ts, apps/desktop/src/app/settings/billing/dev-fixtures.ts, apps/desktop/src/app/settings/billing/errors.test.ts, apps/desktop/src/app/settings/billing/types.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.ts, apps/desktop/src/app/settings/billing/use-charge-poller.test.ts, apps/desktop/src/app/settings/billing/use-step-up.test.tsx, apps/desktop/src/app/settings/constants.ts, apps/desktop/src/app/settings/gateway-settings.tsx, apps/desktop/src/app/settings/toolset-config-panel.test.tsx, apps/desktop/src/app/skills/embedded-hub-picker.tsx, apps/desktop/src/app/skills/index.test.tsx, apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts, apps/desktop/src/contrib/plugin.ts, apps/desktop/src/i18n/en.ts, apps/desktop/src/i18n/ja.ts, apps/desktop/src/i18n/zh-hant.ts, apps/desktop/src/i18n/zh.ts, apps/desktop/src/plugins/nastech-bots/plugin.js, apps/desktop/src/sdk/index.ts, cli-config.yaml.example, eslint.config.shared.mjs, nastech_cli/auth.py, nastech_cli/banner.py, nastech_cli/config_defaults.py, nastech_cli/dashboard_register.py, nastech_cli/diagnostics_upload.py, nastech_cli/fallback_cmd.py, nastech_cli/kanban.py, nastech_cli/main.py, nastech_cli/model_catalog.py, nastech_cli/model_switch.py, nastech_cli/models.py, nastech_cli/nastech_account.py, nastech_cli/nastech_billing.py, nastech_cli/plugins_cmd.py, nastech_cli/portal_cli.py, nastech_cli/providers.py, nastech_cli/proxy/__init__.py, nastech_cli/proxy/adapters/base.py, nastech_cli/proxy/adapters/nastech_portal.py, nastech_cli/setup.py, nastech_cli/setup_whatsapp_cloud.py, nastech_cli/skin_engine.py, nastech_cli/telegram_managed_bot.py, nastech_cli/tools_config.py, nastech_cli/uninstall.py, nastech_cli/update_cmd.py, nastech_cli/web_server.py, nastech_constants.py, package-lock.json, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/plugin.yaml, plugins/kanban/dashboard/dist/index.js, plugins/kanban/systemd/nastech-kanban-dispatcher.service, plugins/model-providers/ai-gateway/__init__.py, plugins/model-providers/fireworks/__init__.py, plugins/model-providers/kimi-coding/__init__.py, plugins/model-providers/nastech/__init__.py, plugins/model-providers/opencode-zen/__init__.py, plugins/nastech-achievements/dashboard/dist/index.js, plugins/platforms/discord/adapter.py, plugins/platforms/email/adapter.py, plugins/platforms/photon/sidecar/package-lock.json, plugins/platforms/slack/adapter.py, run_agent.py, scripts/build_model_catalog.py, scripts/contributor_audit.py, scripts/dev-sandbox.sh, scripts/install.cmd, scripts/install.ps1, scripts/install.sh, scripts/release.py, scripts/whatsapp-bridge/package-lock.json, setup.py, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/references/background-systems.md, skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md, skills/autonomous-ai-agents/nastech-agent/references/configuration.md, skills/autonomous-ai-agents/nastech-agent/references/contributor-guide.md, skills/autonomous-ai-agents/nastech-agent/references/portal-auth-for-third-party-apps.md, skills/autonomous-ai-agents/nastech-agent/references/providers-and-models.md, skills/autonomous-ai-agents/nastech-agent/references/webhooks.md, tests/agent/test_anthropic_adapter.py, tests/agent/test_auxiliary_client.py, tests/agent/test_auxiliary_main_first.py, tests/agent/test_auxiliary_transport_autodetect.py, tests/agent/test_billing_links.py, tests/agent/test_credential_pool.py, tests/agent/test_credits_policy.py, tests/agent/test_error_classifier.py, tests/agent/test_model_metadata.py, tests/agent/test_nastech_credits_gauge.py, tests/agent/test_nastech_oauth_401_guidance.py, tests/agent/test_nastech_portal_anthropic_wire.py, tests/agent/transports/test_chat_completions.py, tests/cli/test_cli_first_run_setup.py, tests/cli/test_cli_provider_resolution.py, tests/docker/test_sqlite_runtime.py, tests/gateway/test_discord_format.py, tests/gateway/test_run_progress_topics.py, tests/gateway/test_status_command.py, tests/gateway/test_usage_command.py, tests/nastech_cli/test_auth_nastech_provider.py, tests/nastech_cli/test_base_url_host_identity.py, tests/nastech_cli/test_dashboard_register.py, tests/nastech_cli/test_fireworks_provider.py, tests/nastech_cli/test_gateway_restart_loop.py, tests/nastech_cli/test_model_catalog.py, tests/nastech_cli/test_nastech_auth_keepalive.py, tests/nastech_cli/test_nastech_auth_status_cache.py, tests/nastech_cli/test_nastech_inference_url_validation.py, tests/nastech_cli/test_nastech_portal_staging_allowlist.py, tests/nastech_cli/test_proxy.py, tests/nastech_cli/test_sale_pricing.py, tests/nastech_cli/test_web_oauth_dispatch.py, tests/plugins/dashboard_auth/test_nastech_provider.py, tests/plugins/image_gen/check_parity_vs_main.py, tests/plugins/image_gen/test_openrouter_compat_provider.py, tests/plugins/test_chronos_verify.py, tests/run_agent/test_anthropic_prompt_cache_policy.py, tests/run_agent/test_primary_runtime_restore.py, tests/run_agent/test_provider_attribution_headers.py, tests/run_agent/test_provider_fallback.py, tests/run_agent/test_provider_parity.py, tests/run_agent/test_run_agent.py, tests/run_agent/test_switch_model_reapplies_headers.py, tests/test_install_ps1_uv_powershell_host.py, tests/tools/test_delegate.py, tests/tools/test_managed_media_gateways.py, tests/tools/test_managed_tool_gateway.py, tests/tools/test_tts_openai_config.py, tests/tools/test_url_safety.py, tests/tools/test_web_tools_config.py, tools/managed_tool_gateway.py, tools/mcp_oauth.py, tools/skills_hub.py, tools/skills_sync_client.py, trajectory_compressor.py, ui-tui/scripts/billing-fixtures.tsx, ui-tui/src/__tests__/subscriptionCommand.test.ts, ui-tui/src/__tests__/subscriptionOverlay.test.tsx, ui-tui/src/app/slash/commands/subscription.ts, ui-tui/src/domain/paths.ts, uv.lock, web/src/components/SidebarFooter.tsx, web/src/pages/DocsPage.tsx, web/src/pages/SystemPage.tsx, website/docs/developer-guide/contributing.md, website/docs/developer-guide/egress-internals.md, website/docs/getting-started/installation.md, website/docs/getting-started/platform-support.md, website/docs/getting-started/quickstart.md, website/docs/getting-started/termux.md, website/docs/guides/run-nastech-with-nastech-portal.md, website/docs/guides/run-nemotron-3-ultra-free.md, website/docs/index.mdx, website/docs/integrations/nastech-portal.md, website/docs/integrations/providers.md, website/docs/reference/cli-commands.md, website/docs/reference/environment-variables.md, website/docs/reference/faq.md, website/docs/reference/model-catalog.md, website/docs/user-guide/desktop.md, website/docs/user-guide/egress/iron-proxy.md, website/docs/user-guide/features/browser.md, website/docs/user-guide/features/image-generation.md, website/docs/user-guide/features/skills.md, website/docs/user-guide/features/subscription-proxy.md, website/docs/user-guide/features/tool-gateway.md, website/docs/user-guide/features/tools.md, website/docs/user-guide/features/tts.md, website/docs/user-guide/features/web-dashboard.md, website/docs/user-guide/features/web-search.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/windows-wsl-quickstart.md, website/docusaurus.config.ts, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/contributing.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/quickstart.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-nastech-with-nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/index.mdx, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/providers.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/faq.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/model-catalog.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/subscription-proxy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tools.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tts.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-native.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-wsl-quickstart.md, website/scripts/generate-llms-txt.py, website/scripts/prebuild.mjs, website/static/api/model-catalog.json, website/static/oauth/client-metadata.json


## Direct upstream tree delta

- complete: +92 ~276 -5 ↪2
- RENAMED `.github/workflows/ci.yml` -> `.github/workflows/ci.yaml`
- MODIFIED `.github/workflows/label-rerun.yml`
- MODIFIED `agent/agent_init.py`
- MODIFIED `agent/agent_runtime_helpers.py`
- MODIFIED `agent/tool_executor.py`
- MODIFIED `apps/bootstrap-installer/package.json`
- MODIFIED `apps/desktop/README.md`
- MODIFIED `apps/desktop/e2e/batch-clarify.spec.ts`
- MODIFIED `apps/desktop/e2e/boot.spec.ts`
- ADDED `apps/desktop/e2e/context-menu-editables.spec.ts`
- MODIFIED `apps/desktop/electron/connection-config.test.ts`
- MODIFIED `apps/desktop/electron/connection-config.ts`
- MODIFIED `apps/desktop/electron/connection-registry.test.ts`
- MODIFIED `apps/desktop/electron/connection-registry.ts`
- ADDED `apps/desktop/electron/fs-ipc.ts`
- ADDED `apps/desktop/electron/git-ipc.ts`
- MODIFIED `apps/desktop/electron/hardening.ts`
- ADDED `apps/desktop/electron/hud-ipc.ts`
- DELETED `apps/desktop/electron/image-context-menu.test.ts`
- DELETED `apps/desktop/electron/image-context-menu.ts`
- MODIFIED `apps/desktop/electron/main.ts`
- ADDED `apps/desktop/electron/pet-overlay-ipc.ts`
- MODIFIED `apps/desktop/electron/preload.ts`
- MODIFIED `apps/desktop/electron/remote-lifecycle.ts`
- MODIFIED `apps/desktop/electron/ssh-connection.ts`
- ADDED `apps/desktop/electron/terminal-ipc.ts`
- MODIFIED `apps/desktop/electron/translucency.test.ts`
- MODIFIED `apps/desktop/electron/translucency.ts`
- MODIFIED `apps/desktop/electron/windows-remote-lifecycle.ts`
- MODIFIED `apps/desktop/package.json`
- MODIFIED `apps/desktop/scripts/stage-native-deps.mjs`
- MODIFIED `apps/desktop/scripts/stage-native-deps.test.mjs`
- ADDED `apps/desktop/src/api/client.ts`
- ADDED `apps/desktop/src/api/config.ts`
- ADDED `apps/desktop/src/api/cron.ts`
- ADDED `apps/desktop/src/api/mcp.ts`
- ADDED `apps/desktop/src/api/messaging.ts`
- ADDED `apps/desktop/src/api/models.ts`
- ADDED `apps/desktop/src/api/plugins.ts`
- ADDED `apps/desktop/src/api/profiles.ts`
- ADDED `apps/desktop/src/api/sessions.ts`
- ADDED `apps/desktop/src/api/skills.ts`
- ADDED `apps/desktop/src/api/system.ts`
- ADDED `apps/desktop/src/api/toolsets.ts`
- MODIFIED `apps/desktop/src/app/artifacts/index.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/focus.ts`
- MODIFIED `apps/desktop/src/app/chat/composer/hooks/use-composer-submit.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/hooks/use-composer-submit.ts`
- MODIFIED `apps/desktop/src/app/chat/composer/hooks/use-composer-trigger.ts`
- MODIFIED `apps/desktop/src/app/chat/composer/hooks/use-composer-undo.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/hooks/use-composer-voice.ts`
- MODIFIED `apps/desktop/src/app/chat/composer/index.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/model-pill.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/rich-editor.test.ts`
- MODIFIED `apps/desktop/src/app/chat/composer/scope.tsx`
- ADDED `apps/desktop/src/app/chat/composer/test-utils.ts`
- MODIFIED `apps/desktop/src/app/chat/index.tsx`
- MODIFIED `apps/desktop/src/app/chat/right-rail/preview-browser-bar.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/right-rail/preview-browser-bar.tsx`
- MODIFIED `apps/desktop/src/app/chat/right-rail/preview-pane.tsx`
- ADDED `apps/desktop/src/app/chat/right-rail/preview-tour-runner.ts`
- ADDED `apps/desktop/src/app/chat/right-rail/preview-tour.ts`
- MODIFIED `apps/desktop/src/app/chat/session-tile-attachments.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/session-tile.tsx`
- MODIFIED `apps/desktop/src/app/chat/session-view.tsx`
- ADDED `apps/desktop/src/app/chat/sidebar/connection-switcher.test.tsx`
- ADDED `apps/desktop/src/app/chat/sidebar/connection-switcher.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/index.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/profile-rail-connect.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/profile-scope.test.ts`
- MODIFIED `apps/desktop/src/app/chat/sidebar/profile-scope.ts`
- MODIFIED `apps/desktop/src/app/chat/sidebar/profile-switcher.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/projects/workspace-groups.test.ts`
- MODIFIED `apps/desktop/src/app/command-palette/highlight-watcher.test.tsx`
- MODIFIED `apps/desktop/src/app/command-palette/marketplace-theme-page.tsx`
- MODIFIED `apps/desktop/src/app/command-palette/pet-palette-page.tsx`
- ADDED `apps/desktop/src/app/command-palette/status-row.tsx`
- ADDED `apps/desktop/src/app/context-menu/app-context-menu.test.tsx`
- ADDED `apps/desktop/src/app/context-menu/app-context-menu.tsx`
- ADDED `apps/desktop/src/app/context-menu/store.ts`
- ADDED `apps/desktop/src/app/context-menu/target.ts`
- MODIFIED `apps/desktop/src/app/contrib/controller.tsx`
- MODIFIED `apps/desktop/src/app/contrib/dev/credits-notice-demo.ts`
- MODIFIED `apps/desktop/src/app/contrib/hooks/use-background-sync.test.ts`
- MODIFIED `apps/desktop/src/app/contrib/hooks/use-background-sync.test.tsx`
- MODIFIED `apps/desktop/src/app/contrib/hooks/use-background-sync.ts`
- MODIFIED `apps/desktop/src/app/contrib/hooks/use-desktop-integrations.test.tsx`
- MODIFIED `apps/desktop/src/app/contrib/mcp-install-deeplink-dialog.tsx`
- MODIFIED `apps/desktop/src/app/contrib/surfaces.test.tsx`
- MODIFIED `apps/desktop/src/app/contrib/surfaces.tsx`
- MODIFIED `apps/desktop/src/app/contrib/wiring.tsx`
- MODIFIED `apps/desktop/src/app/cron/cron-actions.test.ts`
- MODIFIED `apps/desktop/src/app/cron/cron-actions.ts`
- MODIFIED `apps/desktop/src/app/overlays/overlay-split-layout.tsx`
- MODIFIED `apps/desktop/src/app/page-search-shell.tsx`
- MODIFIED `apps/desktop/src/app/right-sidebar/file-actions.tsx`
- MODIFIED `apps/desktop/src/app/right-sidebar/review/file-tree.tsx`
- MODIFIED `apps/desktop/src/app/right-sidebar/review/ship-bar.tsx`
- MODIFIED `apps/desktop/src/app/right-sidebar/terminal/persistent.test.tsx`
- ADDED `apps/desktop/src/app/right-sidebar/terminal/terminal-context-menu.ts`
- MODIFIED `apps/desktop/src/app/right-sidebar/terminal/use-agent-terminal.ts`
- MODIFIED `apps/desktop/src/app/right-sidebar/terminal/use-terminal-session.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-cwd-actions.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-nastech-config.test.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/agent-init-error.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/approval-mode-event.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/clarify-hydration.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/compaction-event.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/composer-model-event.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/delta-flush.test.tsx`
- DELETED `apps/desktop/src/app/session/hooks/use-message-stream/gateway-event.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-message-stream/gateway-event/desktop-bridge.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-message-stream/gateway-event/index.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-message-stream/gateway-event/input-requests.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-message-stream/gateway-event/lifecycle.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-message-stream/gateway-event/message-stream.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-message-stream/gateway-event/session-info.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-message-stream/gateway-event/status.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-message-stream/gateway-event/tools.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-message-stream/gateway-event/types.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/interim-sealing.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/moa-progress-event.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/moa-reference-event.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/pet-tool-failure-event.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/provider-wait-event.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/session-info-side-effects.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/session-reclaimed.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/stale-pending-settle.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/stream-flush.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/terminal-error-frame.test.tsx`
- ADDED `apps/desktop/src/app/session/hooks/use-message-stream/test-harness.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/timeline-events.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/todo-cleanup.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/tool-drafting-event.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/usage.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-model-controls.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/rewind.test.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/rewind.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-actions.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-actions/resolve-stored-session.test.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-actions/utils.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-list-actions.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-list-actions.ts`
- MODIFIED `apps/desktop/src/app/session/workspace-session-target.test.ts`
- MODIFIED `apps/desktop/src/app/settings/appearance-settings.tsx`
- MODIFIED `apps/desktop/src/app/settings/config-field.tsx`
- MODIFIED `apps/desktop/src/app/settings/connections-registry.test.tsx`
- MODIFIED `apps/desktop/src/app/settings/connections-registry.tsx`
- MODIFIED `apps/desktop/src/app/settings/keys-settings.test.tsx`
- MODIFIED `apps/desktop/src/app/settings/primitives.tsx`
- MODIFIED `apps/desktop/src/app/settings/searchable-select.test.tsx`
- MODIFIED `apps/desktop/src/app/settings/settings-search.test.ts`
- ADDED `apps/desktop/src/app/settings/test-utils.ts`
- MODIFIED `apps/desktop/src/app/settings/use-settings-search.ts`
- MODIFIED `apps/desktop/src/app/shell/approval-mode-menu.test.tsx`
- MODIFIED `apps/desktop/src/app/shell/hooks/use-status-snapshot.test.ts`
- MODIFIED `apps/desktop/src/app/shell/hooks/use-status-snapshot.ts`
- MODIFIED `apps/desktop/src/app/shell/hooks/use-statusbar-items.tsx`
- DELETED `apps/desktop/src/app/shell/shell-context-menu.tsx`
- MODIFIED `apps/desktop/src/app/shell/statusbar-visibility.test.tsx`
- MODIFIED `apps/desktop/src/app/skills/mcp-tab.tsx`
- ADDED `apps/desktop/src/components/assistant-ui/test-utils.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread-remount.test.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/assistant-message.test.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/assistant-message.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/block-direction.test.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/changed-files-card.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/double-click-reaction.test.tsx`
- RENAMED `apps/desktop/src/components/assistant-ui/thread/duplicate-stall-indicator.test.tsx` -> `apps/desktop/src/components/assistant-ui/thread/duplicate-activity-indicator.test.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/edit-context.test.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/status-tail-only.test.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/status.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/streaming.test.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/system-message.test.tsx`
- ADDED `apps/desktop/src/components/assistant-ui/thread/turn-activity.test.ts`
- ADDED `apps/desktop/src/components/assistant-ui/thread/turn-activity.ts`
- ADDED `apps/desktop/src/components/assistant-ui/thread/turn-gap-indicator.test.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/user-edit-composer.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/user-message-edit-gesture.test.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/user-message-edit.test.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/user-message.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/tool/delegate-model.ts`
- MODIFIED `apps/desktop/src/components/assistant-ui/tool/fallback-model/index.ts`
- MODIFIED `apps/desktop/src/components/assistant-ui/tool/run-summary.ts`
- MODIFIED `apps/desktop/src/components/assistant-ui/tool/tool-group.test.tsx`
- MODIFIED `apps/desktop/src/components/chat/image-generation-placeholder.test.tsx`
- MODIFIED `apps/desktop/src/components/gateway-connecting-overlay.tsx`
- MODIFIED `apps/desktop/src/components/language-switcher.test.tsx`
- MODIFIED `apps/desktop/src/components/onboarding/index.test.tsx`
- MODIFIED `apps/desktop/src/components/pane-shell/tree/dock-enforce.test.ts`
- MODIFIED `apps/desktop/src/components/pane-shell/tree/renderer/edit-bar.tsx`
- MODIFIED `apps/desktop/src/components/pane-shell/tree/renderer/floating-panes.test.tsx`
- MODIFIED `apps/desktop/src/components/pane-shell/tree/renderer/narrow-overlays.test.tsx`
- MODIFIED `apps/desktop/src/components/pane-shell/tree/renderer/tool-panel-close.test.tsx`
- MODIFIED `apps/desktop/src/components/pane-shell/tree/store.ts`
- MODIFIED `apps/desktop/src/components/pane-shell/tree/zone-editor.tsx`
- MODIFIED `apps/desktop/src/components/pet/pet-sprite.test.tsx`
- MODIFIED `apps/desktop/src/components/pet/use-pet-roam.test.tsx`
- MODIFIED `apps/desktop/src/components/ui/decode-text.tsx`
- MODIFIED `apps/desktop/src/components/ui/status-pulse.test.tsx`
- MODIFIED `apps/desktop/src/components/ui/tab-dropdown.tsx`
- MODIFIED `apps/desktop/src/contrib/runtime-loader.test.ts`
- MODIFIED `apps/desktop/src/contrib/runtime-loader.ts`
- MODIFIED `apps/desktop/src/global.d.ts`
- MODIFIED `apps/desktop/src/nastech.test.ts`
- MODIFIED `apps/desktop/src/nastech.ts`
- MODIFIED `apps/desktop/src/hooks/use-media-query.ts`
- MODIFIED `apps/desktop/src/i18n/ar.ts`
- MODIFIED `apps/desktop/src/i18n/en.ts`
- MODIFIED `apps/desktop/src/i18n/ja.ts`
- MODIFIED `apps/desktop/src/i18n/types.ts`
- MODIFIED `apps/desktop/src/i18n/zh-hant.ts`
- MODIFIED `apps/desktop/src/i18n/zh.ts`
- ADDED `apps/desktop/src/lib/audio-context.ts`
- MODIFIED `apps/desktop/src/lib/budgeted-loop.test.ts`
- DELETED `apps/desktop/src/lib/chat-messages.ts`
- ADDED `apps/desktop/src/lib/chat-messages/hydration.ts`
- ADDED `apps/desktop/src/lib/chat-messages/index.ts`
- ADDED `apps/desktop/src/lib/chat-messages/parts.ts`
- ADDED `apps/desktop/src/lib/chat-messages/reconciliation.ts`
- ADDED `apps/desktop/src/lib/chat-messages/tool-parts.ts`
- ADDED `apps/desktop/src/lib/chat-messages/types.ts`
- MODIFIED `apps/desktop/src/lib/completion-sound.ts`
- ADDED `apps/desktop/src/lib/connection-display.test.ts`
- ADDED `apps/desktop/src/lib/connection-display.ts`
- MODIFIED `apps/desktop/src/lib/desktop-git.ts`
- MODIFIED `apps/desktop/src/lib/external-link.tsx`
- MODIFIED `apps/desktop/src/lib/gateway-rpc.ts`
- ADDED `apps/desktop/src/lib/keyed-timeouts.ts`
- MODIFIED `apps/desktop/src/lib/mcp-import.ts`
- ADDED `apps/desktop/src/lib/mcp-servers.ts`
- MODIFIED `apps/desktop/src/lib/platform.ts`
- ADDED `apps/desktop/src/lib/pointer-drag.ts`
- MODIFIED `apps/desktop/src/lib/session-branch-tree.test.ts`
- MODIFIED `apps/desktop/src/lib/session-date-groups.test.ts`
- ADDED `apps/desktop/src/lib/spoken-reply.test.ts`
- ADDED `apps/desktop/src/lib/spoken-reply.ts`
- MODIFIED `apps/desktop/src/lib/text.ts`
- MODIFIED `apps/desktop/src/lib/thinking-sound.ts`
- ADDED `apps/desktop/src/lib/tour/app-tour.css`
- ADDED `apps/desktop/src/lib/tour/collect-targets.ts`
- ADDED `apps/desktop/src/lib/tour/engine.test.ts`
- ADDED `apps/desktop/src/lib/tour/engine.ts`
- ADDED `apps/desktop/src/lib/tour/index.ts`
- ADDED `apps/desktop/src/lib/tour/run-tour.ts`
- ADDED `apps/desktop/src/lib/tour/spotlight-blur.ts`
- MODIFIED `apps/desktop/src/lib/wake-sound.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/plugin.js`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/blobatar-shapes.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/canonical-chat-identity.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/focused-bot-highlight.test.mjs`
- ADDED `apps/desktop/src/plugins/nastech-bots/tests/group-activity.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/group-chat.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/pane-dock-layout.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/profile-prewarm.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/roster-preview.test.mjs`
- ADDED `apps/desktop/src/plugins/nastech-bots/tests/routines-selected-bot.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/session-workspace.test.mjs`
- MODIFIED `apps/desktop/src/sdk/index.ts`
- MODIFIED `apps/desktop/src/sdk/profile-routing.test.ts`
- MODIFIED `apps/desktop/src/store/approval-mode.test.ts`
- ADDED `apps/desktop/src/store/connections.test.ts`
- ADDED `apps/desktop/src/store/connections.ts`
- MODIFIED `apps/desktop/src/store/cron-model-impact.test.ts`
- MODIFIED `apps/desktop/src/store/data-url-read-max.ts`
- ADDED `apps/desktop/src/store/file-actions.test.ts`
- MODIFIED `apps/desktop/src/store/file-actions.ts`
- ADDED `apps/desktop/src/store/gateway-activation-prune-lease.test.ts`
- MODIFIED `apps/desktop/src/store/gateway-connection-lifecycle.test.ts`
- MODIFIED `apps/desktop/src/store/gateway-connection-scope.test.ts`
- MODIFIED `apps/desktop/src/store/gateway-switch.ts`
- MODIFIED `apps/desktop/src/store/gateway.ts`
- MODIFIED `apps/desktop/src/store/goals.ts`
- ADDED `apps/desktop/src/store/hub-actions.test.ts`
- MODIFIED `apps/desktop/src/store/hub-actions.ts`
- MODIFIED `apps/desktop/src/store/live-sync.ts`
- ADDED `apps/desktop/src/store/nanostores-batch-guard.test.ts`
- MODIFIED `apps/desktop/src/store/onboarding.test.ts`
- MODIFIED `apps/desktop/src/store/pet-gallery.ts`
- MODIFIED `apps/desktop/src/store/pet-generate.ts`
- MODIFIED `apps/desktop/src/store/profile-agent-activation.test.ts`
- MODIFIED `apps/desktop/src/store/profile.test.ts`
- MODIFIED `apps/desktop/src/store/profile.ts`
- MODIFIED `apps/desktop/src/store/projects.test.ts`
- MODIFIED `apps/desktop/src/store/projects.ts`
- MODIFIED `apps/desktop/src/store/review.test.ts`
- MODIFIED `apps/desktop/src/store/review.ts`
- MODIFIED `apps/desktop/src/store/session-color.test.ts`
- MODIFIED `apps/desktop/src/store/session-unread.test.ts`
- MODIFIED `apps/desktop/src/store/session.test.ts`
- MODIFIED `apps/desktop/src/store/settings-scope.ts`
- MODIFIED `apps/desktop/src/store/todos.ts`
- MODIFIED `apps/desktop/src/store/translucency.test.ts`
- MODIFIED `apps/desktop/src/store/translucency.ts`
- MODIFIED `apps/desktop/src/styles.css`
- ADDED `apps/desktop/src/test/deferred.ts`
- ADDED `apps/desktop/src/test/jsdom.ts`
- ADDED `apps/desktop/src/test/oauth-provider.ts`
- ADDED `apps/desktop/src/test/react-root.ts`
- ADDED `apps/desktop/src/test/session-info.ts`
- ADDED `apps/desktop/src/test/window-state.ts`
- MODIFIED `apps/desktop/tsconfig.electron.json`
- MODIFIED `apps/desktop/vite.config.ts`
- ADDED `apps/shared/src/data-url-read-max.ts`
- MODIFIED `apps/shared/src/index.ts`
- MODIFIED `apps/shared/src/translucency.ts`
- ADDED `contributors/emails/johnsonafuye@gmail.com`
- ADDED `contributors/emails/lucasxavier926@gmail.com`
- ADDED `contributors/emails/marketing@cflow.co.kr`
- ADDED `contributors/emails/royzhrxy-glitch@users.noreply.github.com`
- ADDED `contributors/emails/zhu2mu@qq.com`
- MODIFIED `gateway/platforms/base.py`
- MODIFIED `gateway/run.py`
- MODIFIED `nastech_cli/_parser.py`
- MODIFIED `nastech_cli/main.py`
- MODIFIED `nastech_cli/models.py`
- MODIFIED `nastech_cli/tools_config.py`
- MODIFIED `nastech_cli/update_cmd.py`
- MODIFIED `nastech_cli/web_server.py`
- MODIFIED `package-lock.json`
- MODIFIED `plugins/image_gen/openrouter/__init__.py`
- MODIFIED `plugins/image_gen/xai/__init__.py`
- MODIFIED `plugins/platforms/discord/adapter.py`
- MODIFIED `plugins/platforms/feishu/adapter.py`
- MODIFIED `plugins/platforms/matrix/adapter.py`
- MODIFIED `plugins/platforms/raft/adapter.py`
- MODIFIED `plugins/platforms/slack/adapter.py`
- MODIFIED `plugins/platforms/telegram/adapter.py`
- MODIFIED `plugins/platforms/wecom/adapter.py`
- MODIFIED `plugins/platforms/whatsapp/adapter.py`
- MODIFIED `run_agent.py`
- MODIFIED `tests/conftest.py`
- ADDED `tests/gateway/test_multiplex_adapter_session_key_namespace.py`
- MODIFIED `tests/gateway/test_multiplex_busy_input_mode.py`
- ADDED `tests/nastech_cli/test_chat_query_file.py`
- MODIFIED `tests/nastech_cli/test_noninteractive_git.py`
- MODIFIED `tests/nastech_cli/test_tools_config.py`
- ADDED `tests/nastech_cli/test_update_desktop_stale_warning.py`
- ADDED `tests/nastech_cli/test_web_server_approvals_broadcast.py`
- MODIFIED `tests/plugins/image_gen/test_openrouter_compat_provider.py`
- MODIFIED `tests/plugins/image_gen/test_xai_provider.py`
- MODIFIED `tests/run_agent/test_run_agent.py`
- ADDED `tests/tools/test_mcp_oauth_user_agent.py`
- MODIFIED `tests/tools/test_modal_sandbox_fixes.py`
- MODIFIED `tests/tools/test_tool_search.py`
- MODIFIED `tests/tui_gateway/test_gui_surface_toolsets.py`
- MODIFIED `tests/tui_gateway/test_hud_surface_note.py`
- MODIFIED `tools/bot_mode_probe.py`
- MODIFIED `tools/image_generation_tool.py`
- MODIFIED `tools/mcp_oauth.py`
- MODIFIED `tools/mcp_oauth_manager.py`
- MODIFIED `tools/tool_search.py`
- ADDED `tools/tour_tool.py`
- MODIFIED `toolsets.py`
- MODIFIED `tui_gateway/methods_prompt.py`
- MODIFIED `tui_gateway/server.py`
- MODIFIED `ui-tui/package.json`
- MODIFIED `ui-tui/packages/nastech-ink/src/ink/ansi-transition.test.ts`
- MODIFIED `ui-tui/packages/nastech-ink/src/ink/ansi-transition.ts`
- ADDED `ui-tui/packages/nastech-ink/src/ink/ink-focus-redraw.test.ts`
- MODIFIED `ui-tui/packages/nastech-ink/src/ink/ink.tsx`
- MODIFIED `ui-tui/src/__tests__/textInputFastEcho.test.ts`
- MODIFIED `ui-tui/src/components/textInput.tsx`
- MODIFIED `website/docs/getting-started/learning-path.md`
- MODIFIED `website/docs/guides/xai-grok-oauth.md`
- MODIFIED `website/docs/index.mdx`
- MODIFIED `website/docs/reference/cli-commands.md`
- MODIFIED `website/docs/reference/mcp-config-reference.md`
- MODIFIED `website/docs/reference/tools-reference.md`
- MODIFIED `website/docs/reference/toolsets-reference.md`
- MODIFIED `website/docs/user-guide/bot-mode.md`
- MODIFIED `website/docs/user-guide/cli.md`
- MODIFIED `website/docs/user-guide/desktop.md`
- MODIFIED `website/docs/user-guide/multi-connection-desktop.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/xai-grok-oauth.md`

## Scan

9838 files scanned [audio=5, binary=7, doc=5, font=13, image=93, text=9715]


## Diff

1255 renamed, 0 rewritten, 8199 identical, 62 locked, 0 missing, 34 owned, 234 reconciled


## Fork check (vs nastech-agent)

- 9466 identical, 277 updated (+0/-0 lines), 94 added, 0 missing, 0 fork-local-unpreserved, 0 stale-upstream, 1 locked/binary, 0 collision-safe relocated, 54 preserved fork-local files, 0 violations

- features: fork 51 -> branded 51

Auto-generated by 100Ways.
