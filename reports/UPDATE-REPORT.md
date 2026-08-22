# Nastech Update Report #1

- upstream sha : `261a4efb90d7dbe4e71786861858f721b4ab730c`
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

- total files : 10030
- renamed     : 1379 (folders and file names)
- text-rewritten : 9930
- locked-copied  : 57
- binary-copied  : 9
- owned assets   : 34 (our logo/banner/mascot override upstream)

## Reconcile

- fixed : 251 files reconciled: .github/workflows/deploy-site.yml, .github/workflows/skills-index-freshness.yml, .mailmap, CONTRIBUTING.es.md, CONTRIBUTING.md, Dockerfile, README.es.md, README.md, README.ur-pk.md, README.zh-CN.md, SECURITY.es.md, SECURITY.md, agent/agent_runtime_helpers.py, agent/anthropic_adapter.py, agent/auxiliary_client.py, agent/billing_links.py, agent/billing_view.py, agent/chat_completion_helpers.py, agent/conversation_loop.py, agent/credits_tracker.py, agent/model_metadata.py, agent/prompt_builder.py, agent/proxy_sources/iron_proxy.py, agent/subscription_view.py, agent/usage_pricing.py, apps/bootstrap-installer/src-tauri/Cargo.toml, apps/desktop/README.md, apps/desktop/electron/backend-health.test.ts, apps/desktop/electron/backend-health.ts, apps/desktop/electron/connection-config.test.ts, apps/desktop/electron/main.ts, apps/desktop/electron/remote-lifecycle.ts, apps/desktop/package.json, apps/desktop/src/app/messaging/index.test.tsx, apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx, apps/desktop/src/app/settings/about-settings.tsx, apps/desktop/src/app/settings/billing/api.test.ts, apps/desktop/src/app/settings/billing/dev-fixtures.ts, apps/desktop/src/app/settings/billing/errors.test.ts, apps/desktop/src/app/settings/billing/types.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.ts, apps/desktop/src/app/settings/billing/use-charge-poller.test.ts, apps/desktop/src/app/settings/billing/use-step-up.test.tsx, apps/desktop/src/app/settings/constants.ts, apps/desktop/src/app/settings/gateway-settings.tsx, apps/desktop/src/app/settings/toolset-config-panel.test.tsx, apps/desktop/src/app/skills/embedded-hub-picker.tsx, apps/desktop/src/app/skills/index.test.tsx, apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts, apps/desktop/src/components/boot-failure-overlay.test.tsx, apps/desktop/src/components/boot-failure-overlay.tsx, apps/desktop/src/components/send-diagnostics-dialog.tsx, apps/desktop/src/contrib/plugin.ts, apps/desktop/src/i18n/en.ts, apps/desktop/src/i18n/ja.ts, apps/desktop/src/i18n/zh-hant.ts, apps/desktop/src/i18n/zh.ts, apps/desktop/src/plugins/nastech-bots/plugin.js, apps/desktop/src/sdk/index.ts, cli-config.yaml.example, eslint.config.shared.mjs, nastech_cli/auth.py, nastech_cli/banner.py, nastech_cli/config_defaults.py, nastech_cli/dashboard_register.py, nastech_cli/debug.py, nastech_cli/diagnostics_upload.py, nastech_cli/fallback_cmd.py, nastech_cli/kanban.py, nastech_cli/main.py, nastech_cli/model_catalog.py, nastech_cli/model_switch.py, nastech_cli/models.py, nastech_cli/nastech_account.py, nastech_cli/nastech_billing.py, nastech_cli/plugins_cmd.py, nastech_cli/portal_cli.py, nastech_cli/providers.py, nastech_cli/proxy/__init__.py, nastech_cli/proxy/adapters/base.py, nastech_cli/proxy/adapters/nastech_portal.py, nastech_cli/setup.py, nastech_cli/setup_whatsapp_cloud.py, nastech_cli/skin_engine.py, nastech_cli/telegram_managed_bot.py, nastech_cli/tools_config.py, nastech_cli/uninstall.py, nastech_cli/update_cmd.py, nastech_cli/web_server.py, nastech_constants.py, package-lock.json, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/plugin.yaml, plugins/kanban/dashboard/dist/index.js, plugins/kanban/systemd/nastech-kanban-dispatcher.service, plugins/model-providers/ai-gateway/__init__.py, plugins/model-providers/fireworks/__init__.py, plugins/model-providers/kimi-coding/__init__.py, plugins/model-providers/nastech/__init__.py, plugins/model-providers/opencode-free/__init__.py, plugins/model-providers/opencode-zen/__init__.py, plugins/nastech-achievements/dashboard/dist/index.js, plugins/platforms/discord/adapter.py, plugins/platforms/email/adapter.py, plugins/platforms/photon/sidecar/package-lock.json, plugins/platforms/slack/adapter.py, run_agent.py, scripts/build_model_catalog.py, scripts/contributor_audit.py, scripts/dev-sandbox.sh, scripts/install.cmd, scripts/install.ps1, scripts/install.sh, scripts/release.py, scripts/whatsapp-bridge/package-lock.json, setup.py, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/references/background-systems.md, skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md, skills/autonomous-ai-agents/nastech-agent/references/configuration.md, skills/autonomous-ai-agents/nastech-agent/references/contributor-guide.md, skills/autonomous-ai-agents/nastech-agent/references/portal-auth-for-third-party-apps.md, skills/autonomous-ai-agents/nastech-agent/references/providers-and-models.md, skills/autonomous-ai-agents/nastech-agent/references/webhooks.md, tests/agent/test_anthropic_adapter.py, tests/agent/test_auxiliary_client.py, tests/agent/test_auxiliary_main_first.py, tests/agent/test_auxiliary_transport_autodetect.py, tests/agent/test_billing_links.py, tests/agent/test_credential_pool.py, tests/agent/test_credits_policy.py, tests/agent/test_error_classifier.py, tests/agent/test_model_metadata.py, tests/agent/test_nastech_credits_gauge.py, tests/agent/test_nastech_oauth_401_guidance.py, tests/agent/test_nastech_portal_anthropic_wire.py, tests/agent/transports/test_chat_completions.py, tests/cli/test_cli_first_run_setup.py, tests/cli/test_cli_provider_resolution.py, tests/cli/test_show_config_credential.py, tests/docker/test_sqlite_runtime.py, tests/gateway/test_discord_format.py, tests/gateway/test_run_progress_topics.py, tests/gateway/test_status_command.py, tests/gateway/test_usage_command.py, tests/nastech_cli/test_auth_nastech_provider.py, tests/nastech_cli/test_base_url_host_identity.py, tests/nastech_cli/test_dashboard_register.py, tests/nastech_cli/test_fireworks_provider.py, tests/nastech_cli/test_gateway_restart_loop.py, tests/nastech_cli/test_model_catalog.py, tests/nastech_cli/test_nastech_auth_keepalive.py, tests/nastech_cli/test_nastech_auth_status_cache.py, tests/nastech_cli/test_nastech_inference_url_validation.py, tests/nastech_cli/test_nastech_portal_staging_allowlist.py, tests/nastech_cli/test_nastech_reasoning_metadata.py, tests/nastech_cli/test_proxy.py, tests/nastech_cli/test_reasoning_caps_disk_cache.py, tests/nastech_cli/test_sale_pricing.py, tests/nastech_cli/test_web_oauth_dispatch.py, tests/plugins/dashboard_auth/test_nastech_provider.py, tests/plugins/image_gen/check_parity_vs_main.py, tests/plugins/image_gen/test_openrouter_compat_provider.py, tests/plugins/test_chronos_verify.py, tests/run_agent/test_anthropic_prompt_cache_policy.py, tests/run_agent/test_primary_runtime_restore.py, tests/run_agent/test_provider_attribution_headers.py, tests/run_agent/test_provider_fallback.py, tests/run_agent/test_provider_parity.py, tests/run_agent/test_run_agent.py, tests/run_agent/test_switch_model_reapplies_headers.py, tests/test_install_ps1_uv_powershell_host.py, tests/tools/test_delegate.py, tests/tools/test_managed_media_gateways.py, tests/tools/test_managed_tool_gateway.py, tests/tools/test_strict_provider_selection.py, tests/tools/test_tts_openai_config.py, tests/tools/test_url_safety.py, tests/tools/test_web_tools_config.py, tools/managed_tool_gateway.py, tools/mcp_oauth.py, tools/skills_hub.py, tools/skills_sync_client.py, trajectory_compressor.py, ui-tui/scripts/billing-fixtures.tsx, ui-tui/src/__tests__/subscriptionCommand.test.ts, ui-tui/src/__tests__/subscriptionOverlay.test.tsx, ui-tui/src/app/slash/commands/subscription.ts, ui-tui/src/domain/paths.ts, uv.lock, web/src/components/SidebarFooter.tsx, web/src/pages/DocsPage.tsx, web/src/pages/SystemPage.tsx, website/docs/developer-guide/contributing.md, website/docs/developer-guide/egress-internals.md, website/docs/getting-started/installation.md, website/docs/getting-started/platform-support.md, website/docs/getting-started/quickstart.md, website/docs/getting-started/termux.md, website/docs/guides/manage-nastech-cloud-with-mcp.md, website/docs/guides/run-nastech-with-nastech-portal.md, website/docs/guides/run-nemotron-3-ultra-free.md, website/docs/index.mdx, website/docs/integrations/nastech-portal.md, website/docs/integrations/providers.md, website/docs/reference/cli-commands.md, website/docs/reference/environment-variables.md, website/docs/reference/faq.md, website/docs/reference/model-catalog.md, website/docs/user-guide/desktop.md, website/docs/user-guide/egress/iron-proxy.md, website/docs/user-guide/features/browser.md, website/docs/user-guide/features/image-generation.md, website/docs/user-guide/features/skills.md, website/docs/user-guide/features/subscription-proxy.md, website/docs/user-guide/features/tool-gateway.md, website/docs/user-guide/features/tools.md, website/docs/user-guide/features/tts.md, website/docs/user-guide/features/web-dashboard.md, website/docs/user-guide/features/web-search.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/windows-wsl-quickstart.md, website/docusaurus.config.ts, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/contributing.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/quickstart.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-nastech-with-nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/index.mdx, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/providers.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/faq.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/model-catalog.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/subscription-proxy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tools.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tts.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-native.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-wsl-quickstart.md, website/scripts/generate-llms-txt.py, website/scripts/prebuild.mjs, website/static/api/model-catalog.json, website/static/oauth/client-metadata.json


## Direct upstream tree delta

- complete: +64 ~200 -10 ↪0
- ADDED `.github/actionlint.yaml`
- ADDED `.github/scripts/run-workspace-checks.mjs`
- MODIFIED `.github/workflows/ci.yaml`
- MODIFIED `.github/workflows/docker.yml`
- MODIFIED `.github/workflows/e2e-desktop.yml`
- MODIFIED `.github/workflows/js-tests.yml`
- MODIFIED `.github/workflows/nix.yml`
- MODIFIED `.github/workflows/rust-tests.yml`
- MODIFIED `.github/workflows/tests-os.yml`
- MODIFIED `.github/workflows/tests.yml`
- ADDED `.github/workflows/windows-venv-e2e.yml`
- MODIFIED `AGENTS.md`
- MODIFIED `agent/agent_init.py`
- MODIFIED `agent/auxiliary_client.py`
- MODIFIED `agent/bedrock_adapter.py`
- ADDED `agent/compaction_display.py`
- MODIFIED `agent/context_compressor.py`
- MODIFIED `agent/conversation_compression.py`
- MODIFIED `agent/conversation_loop.py`
- MODIFIED `agent/credits_tracker.py`
- MODIFIED `agent/error_classifier.py`
- ADDED `agent/error_surface.py`
- MODIFIED `agent/model_metadata.py`
- MODIFIED `agent/reasoning_effort.py`
- MODIFIED `agent/tool_executor.py`
- MODIFIED `agent/turn_context.py`
- MODIFIED `apps/desktop/electron/backend-health.test.ts`
- MODIFIED `apps/desktop/electron/backend-health.ts`
- MODIFIED `apps/desktop/electron/connection-config.test.ts`
- MODIFIED `apps/desktop/electron/connection-config.ts`
- MODIFIED `apps/desktop/electron/fs-ipc.ts`
- MODIFIED `apps/desktop/electron/main.ts`
- MODIFIED `apps/desktop/electron/preload.ts`
- MODIFIED `apps/desktop/package.json`
- DELETED `apps/desktop/scripts/run-ui-shard.mjs`
- MODIFIED `apps/desktop/src/app/chat/pane-mirror.ts`
- MODIFIED `apps/desktop/src/app/chat/session-drag.ts`
- MODIFIED `apps/desktop/src/app/chat/session-tile.tsx`
- MODIFIED `apps/desktop/src/app/context-menu/app-context-menu.tsx`
- MODIFIED `apps/desktop/src/app/contrib/controller.tsx`
- MODIFIED `apps/desktop/src/app/contrib/surfaces.tsx`
- MODIFIED `apps/desktop/src/app/contrib/wiring.tsx`
- MODIFIED `apps/desktop/src/app/hooks/use-keybinds.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/gateway-event/message-stream.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/index.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/terminal-error-frame.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-actions/utils.ts`
- MODIFIED `apps/desktop/src/app/settings/appearance-settings.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/assistant-message.tsx`
- MODIFIED `apps/desktop/src/components/boot-failure-overlay.test.tsx`
- MODIFIED `apps/desktop/src/components/boot-failure-overlay.tsx`
- MODIFIED `apps/desktop/src/components/error-boundary.tsx`
- MODIFIED `apps/desktop/src/components/gateway-connecting-overlay.tsx`
- MODIFIED `apps/desktop/src/components/model-picker.tsx`
- MODIFIED `apps/desktop/src/components/onboarding/index.tsx`
- MODIFIED `apps/desktop/src/components/pane-shell/tree/dock-enforce.test.ts`
- MODIFIED `apps/desktop/src/components/pane-shell/tree/model.ts`
- MODIFIED `apps/desktop/src/components/pane-shell/tree/renderer/drag-session.ts`
- DELETED `apps/desktop/src/components/pane-shell/tree/renderer/lone-header.test.ts`
- DELETED `apps/desktop/src/components/pane-shell/tree/renderer/lone-header.ts`
- ADDED `apps/desktop/src/components/pane-shell/tree/renderer/strip-visibility.test.ts`
- ADDED `apps/desktop/src/components/pane-shell/tree/renderer/strip-visibility.ts`
- ADDED `apps/desktop/src/components/pane-shell/tree/renderer/tab-close-affordance.test.tsx`
- ADDED `apps/desktop/src/components/pane-shell/tree/renderer/tab-strip-hide.test.tsx`
- MODIFIED `apps/desktop/src/components/pane-shell/tree/renderer/track-model.ts`
- MODIFIED `apps/desktop/src/components/pane-shell/tree/renderer/tree-group.test.tsx`
- MODIFIED `apps/desktop/src/components/pane-shell/tree/renderer/tree-group.tsx`
- MODIFIED `apps/desktop/src/components/pane-shell/tree/store.ts`
- ADDED `apps/desktop/src/components/pane-shell/tree/tabstrip-migration.test.ts`
- MODIFIED `apps/desktop/src/components/pane-shell/tree/tool-pane-toggle.test.ts`
- ADDED `apps/desktop/src/components/send-diagnostics-dialog.tsx`
- ADDED `apps/desktop/src/components/ui/confirm-dialog-unmount.test.tsx`
- MODIFIED `apps/desktop/src/components/ui/confirm-dialog.tsx`
- MODIFIED `apps/desktop/src/components/ui/pane-tab.test.tsx`
- MODIFIED `apps/desktop/src/components/ui/pane-tab.tsx`
- MODIFIED `apps/desktop/src/components/ui/zoomable.tsx`
- MODIFIED `apps/desktop/src/global.d.ts`
- MODIFIED `apps/desktop/src/i18n/ar.ts`
- MODIFIED `apps/desktop/src/i18n/en.ts`
- MODIFIED `apps/desktop/src/i18n/ja.ts`
- MODIFIED `apps/desktop/src/i18n/types.ts`
- MODIFIED `apps/desktop/src/i18n/zh-hant.ts`
- MODIFIED `apps/desktop/src/i18n/zh.ts`
- MODIFIED `apps/desktop/src/lib/chat-messages/types.ts`
- MODIFIED `apps/desktop/src/lib/chat-runtime.ts`
- ADDED `apps/desktop/src/lib/error-surface.test.ts`
- ADDED `apps/desktop/src/lib/error-surface.ts`
- MODIFIED `apps/desktop/src/lib/icons.ts`
- MODIFIED `apps/desktop/src/lib/keybinds/actions.ts`
- MODIFIED `apps/desktop/src/lib/model-search-text.ts`
- ADDED `apps/desktop/src/lib/selection-copy-colors.test.ts`
- ADDED `apps/desktop/src/lib/selection-copy-colors.ts`
- MODIFIED `apps/desktop/src/main.tsx`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/plugin.js`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/active-now-strip.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/activity-toasts.test.mjs`
- DELETED `apps/desktop/src/plugins/nastech-bots/tests/canonical-chat-adopt-before-mint.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/canonical-chat-creation.test.mjs`
- DELETED `apps/desktop/src/plugins/nastech-bots/tests/canonical-chat-empty-recovery.test.mjs`
- DELETED `apps/desktop/src/plugins/nastech-bots/tests/canonical-chat-identity.test.mjs`
- DELETED `apps/desktop/src/plugins/nastech-bots/tests/canonical-chat-pin.test.mjs`
- ADDED `apps/desktop/src/plugins/nastech-bots/tests/canonical-chat-registry.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/hide-bot-chats.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/hide-bots.test.mjs`
- DELETED `apps/desktop/src/plugins/nastech-bots/tests/mention-handoff-quoting.test.mjs`
- ADDED `apps/desktop/src/plugins/nastech-bots/tests/mention-identification.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/mention-roster-cache-key.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/new-compact-guard.test.mjs`
- DELETED `apps/desktop/src/plugins/nastech-bots/tests/remote-dm-delivery.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/roster-preview.test.mjs`
- ADDED `apps/desktop/src/plugins/nastech-bots/tests/routine-deliver-target.test.mjs`
- ADDED `apps/desktop/src/store/send-diagnostics.test.ts`
- ADDED `apps/desktop/src/store/send-diagnostics.ts`
- ADDED `apps/desktop/src/store/tabstrip-prefs.ts`
- MODIFIED `apps/desktop/src/styles.css`
- MODIFIED `apps/desktop/src/types/nastech.ts`
- MODIFIED `cli-config.yaml.example`
- ADDED `contributors/emails/dhanesh@users.noreply.github.com`
- ADDED `contributors/emails/epicstorage0@gmail.com`
- ADDED `contributors/emails/gc@erek.ai`
- ADDED `contributors/emails/mike@vorburger.ch`
- ADDED `contributors/emails/nate@vulcan-tech.com`
- ADDED `contributors/emails/openclaww@gmail.com`
- ADDED `contributors/emails/samtcam@gmail.com`
- ADDED `contributors/emails/switchstatement@gmail.com`
- ADDED `contributors/emails/troy.rowe@re-source.au`
- ADDED `contributors/emails/tsungyuan.hung@gmail.com`
- ADDED `contributors/emails/vinayshah2006@gmail.com`
- ADDED `contributors/emails/willfrombr@Willians-MacBook-Pro.local`
- MODIFIED `cron/scheduler.py`
- ADDED `gateway/browser_control_artifacts.py`
- ADDED `gateway/browser_control_broker.py`
- MODIFIED `gateway/kanban_watchers.py`
- MODIFIED `gateway/platforms/api_server.py`
- MODIFIED `gateway/run.py`
- MODIFIED `gateway/session.py`
- MODIFIED `gateway/session_context.py`
- MODIFIED `gateway/shutdown_forensics.py`
- MODIFIED `nastech_cli/_install_repair.py`
- MODIFIED `nastech_cli/auth.py`
- MODIFIED `nastech_cli/backup.py`
- MODIFIED `nastech_cli/cli_agent_setup_mixin.py`
- MODIFIED `nastech_cli/config_defaults.py`
- MODIFIED `nastech_cli/debug.py`
- MODIFIED `nastech_cli/gateway.py`
- MODIFIED `nastech_cli/inventory.py`
- MODIFIED `nastech_cli/linux_desktop_entry.py`
- MODIFIED `nastech_cli/main.py`
- MODIFIED `nastech_cli/model_search.py`
- MODIFIED `nastech_cli/models.py`
- MODIFIED `nastech_cli/profiles.py`
- MODIFIED `nastech_cli/runtime_provider.py`
- MODIFIED `nastech_cli/subcommands/cron.py`
- MODIFIED `nastech_cli/subcommands/update.py`
- MODIFIED `nastech_cli/update_cmd.py`
- MODIFIED `nastech_cli/web_server.py`
- MODIFIED `nastech_state.py`
- MODIFIED `nastech_state_common.py`
- MODIFIED `nastech_state_portability.py`
- MODIFIED `nastech_state_schema.py`
- MODIFIED `nix/checks.nix`
- MODIFIED `nix/desktop.nix`
- MODIFIED `nix/homeManagerModules.nix`
- MODIFIED `nix/moduleCommon.nix`
- MODIFIED `nix/nixosModules.nix`
- MODIFIED `plugins/model-providers/zai/__init__.py`
- MODIFIED `plugins/platforms/discord/adapter.py`
- MODIFIED `plugins/platforms/telegram/adapter.py`
- MODIFIED `run_agent.py`
- ADDED `scripts/ci/test_install_ps1_cli_launchers.ps1`
- MODIFIED `scripts/install.ps1`
- MODIFIED `scripts/run_tests_parallel.py`
- MODIFIED `tests/agent/test_arcee_trinity_overrides.py`
- MODIFIED `tests/agent/test_auxiliary_client.py`
- MODIFIED `tests/agent/test_bedrock_integration.py`
- MODIFIED `tests/agent/test_credits_policy.py`
- MODIFIED `tests/agent/test_error_classifier.py`
- ADDED `tests/agent/test_error_surface.py`
- MODIFIED `tests/agent/test_model_metadata.py`
- MODIFIED `tests/agent/test_reference_handoff_active_turn.py`
- ADDED `tests/agent/test_would_grow_refusal_runway.py`
- MODIFIED `tests/cli/test_resume_display.py`
- ADDED `tests/cron/test_cron_bot_chat_delivery.py`
- MODIFIED `tests/cron/test_run_one_job.py`
- MODIFIED `tests/cron/test_scheduler.py`
- ADDED `tests/gateway/test_api_server_compaction_projection.py`
- ADDED `tests/gateway/test_browser_control_api.py`
- ADDED `tests/gateway/test_browser_control_artifacts.py`
- ADDED `tests/gateway/test_browser_control_broker.py`
- ADDED `tests/gateway/test_browser_control_broker_hardening.py`
- ADDED `tests/gateway/test_browser_control_cloud.py`
- MODIFIED `tests/gateway/test_delivery_ledger.py`
- ADDED `tests/gateway/test_discord_model_picker_partition.py`
- MODIFIED `tests/gateway/test_gateway_shutdown.py`
- MODIFIED `tests/gateway/test_goal_resume_restart.py`
- MODIFIED `tests/gateway/test_multiplex_lifecycle.py`
- MODIFIED `tests/gateway/test_platform_reconnect.py`
- MODIFIED `tests/gateway/test_restart_resume_pending.py`
- MODIFIED `tests/gateway/test_telegram_network_reconnect.py`
- MODIFIED `tests/gateway/test_telegram_rich_messages.py`
- MODIFIED `tests/gateway/test_telegram_send_path_health.py`
- MODIFIED `tests/gateway/test_telegram_topic_mode.py`
- MODIFIED `tests/nastech_cli/test_backup.py`
- ADDED `tests/nastech_cli/test_backup_all_profiles.py`
- MODIFIED `tests/nastech_cli/test_bedrock_model_picker.py`
- MODIFIED `tests/nastech_cli/test_chat_query_file.py`
- MODIFIED `tests/nastech_cli/test_cmd_update.py`
- MODIFIED `tests/nastech_cli/test_config_read_guard.py`
- MODIFIED `tests/nastech_cli/test_dashboard_auth_ws_auth.py`
- MODIFIED `tests/nastech_cli/test_gateway_service.py`
- MODIFIED `tests/nastech_cli/test_inventory_pricing.py`
- MODIFIED `tests/nastech_cli/test_linux_desktop_entry.py`
- MODIFIED `tests/nastech_cli/test_model_search.py`
- MODIFIED `tests/nastech_cli/test_sale_pricing.py`
- MODIFIED `tests/nastech_cli/test_update_parked_branch_guard.py`
- ADDED `tests/nastech_cli/test_update_zip_fallback_guards.py`
- ADDED `tests/nastech_cli/test_update_zip_release_preserve.py`
- MODIFIED `tests/nastech_cli/test_update_zip_symlink_reject.py`
- ADDED `tests/nastech_cli/test_venv_holder_classifier.py`
- ADDED `tests/nastech_cli/test_venv_holder_windows_live.py`
- ADDED `tests/nastech_cli/test_windows_cli_launcher_repair.py`
- MODIFIED `tests/plugins/model_providers/test_zai_profile.py`
- MODIFIED `tests/state/test_fts_runtime_rebuild.py`
- MODIFIED `tests/test_session_skill_previews.py`
- ADDED `tests/test_state_db_repair_live_writer_guard.py`
- ADDED `tests/test_state_db_repair_loop_mtime.py`
- ADDED `tests/test_state_db_write_durability.py`
- MODIFIED `tests/test_tui_gateway_server.py`
- ADDED `tests/tools/test_bot_mode_dm.py`
- MODIFIED `tests/tools/test_bot_mode_probe.py`
- ADDED `tests/tools/test_browser_extension_router.py`
- ADDED `tests/tools/test_browser_extension_router_wiring.py`
- MODIFIED `tests/tools/test_process_registry_write_stdin_surrogates.py`
- MODIFIED `tests/tools/test_shared_container_task_id.py`
- MODIFIED `tests/tools/test_snapshot_session_id_leak.py`
- ADDED `tests/tui_gateway/test_diagnostics_share_nastech.py`
- MODIFIED `tests/tui_gateway/test_failed_turn_retention.py`
- ADDED `tests/tui_gateway/test_profiles_list_canonical_session.py`
- DELETED `tests/tui_gateway/test_profiles_list_preferred_session.py`
- MODIFIED `tests/tui_gateway/test_session_db_ownership_teardown.py`
- MODIFIED `tests/tui_gateway/test_session_resume_db_ownership.py`
- ADDED `tools/bot_mode_dm.py`
- MODIFIED `tools/bot_mode_probe.py`
- MODIFIED `tools/browser_cdp_tool.py`
- ADDED `tools/browser_extension_router.py`
- MODIFIED `tools/browser_tool.py`
- MODIFIED `tools/cronjob_tools.py`
- MODIFIED `tools/environments/base.py`
- MODIFIED `tools/registry.py`
- MODIFIED `tools/terminal_tool.py`
- ADDED `tui_gateway/methods_browser_control.py`
- MODIFIED `tui_gateway/methods_config.py`
- MODIFIED `tui_gateway/methods_profiles.py`
- MODIFIED `tui_gateway/methods_prompt.py`
- MODIFIED `tui_gateway/methods_session.py`
- MODIFIED `tui_gateway/methods_tools.py`
- MODIFIED `tui_gateway/server.py`
- MODIFIED `tui_gateway/ws.py`
- MODIFIED `ui-tui/src/lib/model-search-text.test.ts`
- MODIFIED `ui-tui/src/lib/model-search-text.ts`
- MODIFIED `web/src/lib/model-search-text.ts`
- MODIFIED `website/docs/developer-guide/cron-internals.md`
- MODIFIED `website/docs/developer-guide/programmatic-integration.md`
- MODIFIED `website/docs/getting-started/nix-setup.md`
- MODIFIED `website/docs/getting-started/updating.md`
- MODIFIED `website/docs/guides/automate-with-cron.md`
- MODIFIED `website/docs/guides/aws-bedrock.md`
- MODIFIED `website/docs/index.mdx`
- MODIFIED `website/docs/reference/cli-commands.md`
- MODIFIED `website/docs/user-guide/bot-mode.md`
- MODIFIED `website/docs/user-guide/desktop.md`
- MODIFIED `website/docs/user-guide/features/api-server.md`
- MODIFIED `website/docs/user-guide/features/cron.md`
- MODIFIED `website/static/api/model-catalog.json`

## Scan

10084 files scanned [archive=1, audio=5, binary=7, doc=5, font=13, image=93, text=9960]


## Diff

1294 renamed, 0 rewritten, 8393 identical, 63 locked, 0 missing, 34 owned, 246 reconciled


## Fork check (vs nastech-agent)

- 9678 identical, 342 updated (+0/-0 lines), 64 added, 0 missing, 0 fork-local-unpreserved, 0 stale-upstream, 0 locked/binary, 0 collision-safe relocated, 54 preserved fork-local files, 0 violations

- features: fork 51 -> branded 51

Auto-generated by 100Ways.
