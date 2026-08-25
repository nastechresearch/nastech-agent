# Nastech Update Report #1

- upstream sha : `4c1f53be10d0fce1d25aee1975e5149b6c54f25a`
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

- total files : 10242
- renamed     : 1422 (folders and file names)
- text-rewritten : 10144
- locked-copied  : 56
- binary-copied  : 8
- owned assets   : 34 (our logo/banner/mascot override upstream)

## Reconcile

- fixed : 254 files reconciled: .github/workflows/deploy-site.yml, .github/workflows/skills-index-freshness.yml, .mailmap, CONTRIBUTING.es.md, CONTRIBUTING.md, Dockerfile, README.es.md, README.md, README.ur-pk.md, README.zh-CN.md, SECURITY.es.md, SECURITY.md, agent/agent_runtime_helpers.py, agent/anthropic_adapter.py, agent/auxiliary_client.py, agent/billing_links.py, agent/billing_view.py, agent/chat_completion_helpers.py, agent/conversation_loop.py, agent/credits_tracker.py, agent/model_metadata.py, agent/prompt_builder.py, agent/proxy_sources/iron_proxy.py, agent/subscription_view.py, agent/usage_pricing.py, apps/bootstrap-installer/src-tauri/Cargo.toml, apps/desktop/README.md, apps/desktop/electron/backend-health.test.ts, apps/desktop/electron/backend-health.ts, apps/desktop/electron/connection-config.test.ts, apps/desktop/electron/main.ts, apps/desktop/electron/remote-lifecycle.ts, apps/desktop/package.json, apps/desktop/src/app/messaging/index.test.tsx, apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx, apps/desktop/src/app/settings/about-settings.tsx, apps/desktop/src/app/settings/billing/api.test.ts, apps/desktop/src/app/settings/billing/dev-fixtures.ts, apps/desktop/src/app/settings/billing/errors.test.ts, apps/desktop/src/app/settings/billing/types.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.ts, apps/desktop/src/app/settings/billing/use-charge-poller.test.ts, apps/desktop/src/app/settings/billing/use-step-up.test.tsx, apps/desktop/src/app/settings/constants.ts, apps/desktop/src/app/settings/gateway-settings.tsx, apps/desktop/src/app/settings/toolset-config-panel.test.tsx, apps/desktop/src/app/skills/embedded-hub-picker.tsx, apps/desktop/src/app/skills/index.test.tsx, apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts, apps/desktop/src/components/boot-failure-overlay.test.tsx, apps/desktop/src/components/boot-failure-overlay.tsx, apps/desktop/src/components/send-diagnostics-dialog.tsx, apps/desktop/src/contrib/plugin.ts, apps/desktop/src/i18n/en.ts, apps/desktop/src/i18n/ja.ts, apps/desktop/src/i18n/zh-hant.ts, apps/desktop/src/i18n/zh.ts, apps/desktop/src/plugins/nastech-bots/plugin.js, apps/desktop/src/sdk/index.ts, cli-config.yaml.example, eslint.config.shared.mjs, nastech_cli/auth.py, nastech_cli/banner.py, nastech_cli/config_defaults.py, nastech_cli/dashboard_auth/login_page.py, nastech_cli/dashboard_register.py, nastech_cli/debug.py, nastech_cli/diagnostics_upload.py, nastech_cli/fallback_cmd.py, nastech_cli/kanban.py, nastech_cli/main.py, nastech_cli/model_catalog.py, nastech_cli/model_switch.py, nastech_cli/models.py, nastech_cli/nastech_account.py, nastech_cli/nastech_billing.py, nastech_cli/plugins_cmd.py, nastech_cli/portal_cli.py, nastech_cli/providers.py, nastech_cli/proxy/__init__.py, nastech_cli/proxy/adapters/base.py, nastech_cli/proxy/adapters/nastech_portal.py, nastech_cli/setup.py, nastech_cli/setup_whatsapp_cloud.py, nastech_cli/skin_engine.py, nastech_cli/telegram_managed_bot.py, nastech_cli/tools_config.py, nastech_cli/uninstall.py, nastech_cli/update_cmd.py, nastech_cli/web_server.py, nastech_constants.py, package-lock.json, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/plugin.yaml, plugins/kanban/dashboard/dist/index.js, plugins/kanban/systemd/nastech-kanban-dispatcher.service, plugins/model-providers/ai-gateway/__init__.py, plugins/model-providers/fireworks/__init__.py, plugins/model-providers/kimi-coding/__init__.py, plugins/model-providers/nastech/__init__.py, plugins/model-providers/opencode-free/__init__.py, plugins/model-providers/opencode-zen/__init__.py, plugins/nastech-achievements/dashboard/dist/index.js, plugins/platforms/discord/adapter.py, plugins/platforms/email/adapter.py, plugins/platforms/photon/sidecar/package-lock.json, plugins/platforms/slack/adapter.py, run_agent.py, scripts/build_model_catalog.py, scripts/contributor_audit.py, scripts/dev-sandbox.sh, scripts/install.cmd, scripts/install.ps1, scripts/install.sh, scripts/release.py, scripts/whatsapp-bridge/package-lock.json, setup.py, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/references/background-systems.md, skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md, skills/autonomous-ai-agents/nastech-agent/references/configuration.md, skills/autonomous-ai-agents/nastech-agent/references/contributor-guide.md, skills/autonomous-ai-agents/nastech-agent/references/portal-auth-for-third-party-apps.md, skills/autonomous-ai-agents/nastech-agent/references/providers-and-models.md, skills/autonomous-ai-agents/nastech-agent/references/webhooks.md, tests/agent/test_anthropic_adapter.py, tests/agent/test_auxiliary_client.py, tests/agent/test_auxiliary_main_first.py, tests/agent/test_auxiliary_transport_autodetect.py, tests/agent/test_billing_links.py, tests/agent/test_credential_pool.py, tests/agent/test_credits_policy.py, tests/agent/test_error_classifier.py, tests/agent/test_model_metadata.py, tests/agent/test_nastech_credits_gauge.py, tests/agent/test_nastech_oauth_401_guidance.py, tests/agent/test_nastech_portal_anthropic_wire.py, tests/agent/test_phantom_tool_references.py, tests/agent/transports/test_chat_completions.py, tests/cli/test_cli_first_run_setup.py, tests/cli/test_cli_provider_resolution.py, tests/cli/test_show_config_credential.py, tests/docker/test_sqlite_runtime.py, tests/gateway/test_discord_format.py, tests/gateway/test_run_progress_topics.py, tests/gateway/test_status_command.py, tests/gateway/test_usage_command.py, tests/nastech_cli/test_auth_nastech_provider.py, tests/nastech_cli/test_base_url_host_identity.py, tests/nastech_cli/test_dashboard_auth_gate.py, tests/nastech_cli/test_dashboard_register.py, tests/nastech_cli/test_fireworks_provider.py, tests/nastech_cli/test_gateway_restart_loop.py, tests/nastech_cli/test_model_catalog.py, tests/nastech_cli/test_nastech_auth_keepalive.py, tests/nastech_cli/test_nastech_auth_status_cache.py, tests/nastech_cli/test_nastech_inference_url_validation.py, tests/nastech_cli/test_nastech_portal_staging_allowlist.py, tests/nastech_cli/test_nastech_reasoning_metadata.py, tests/nastech_cli/test_proxy.py, tests/nastech_cli/test_reasoning_caps_disk_cache.py, tests/nastech_cli/test_sale_pricing.py, tests/nastech_cli/test_web_oauth_dispatch.py, tests/plugins/dashboard_auth/test_nastech_provider.py, tests/plugins/image_gen/check_parity_vs_main.py, tests/plugins/image_gen/test_openrouter_compat_provider.py, tests/plugins/test_chronos_verify.py, tests/run_agent/test_anthropic_prompt_cache_policy.py, tests/run_agent/test_primary_runtime_restore.py, tests/run_agent/test_provider_attribution_headers.py, tests/run_agent/test_provider_fallback.py, tests/run_agent/test_provider_parity.py, tests/run_agent/test_run_agent.py, tests/run_agent/test_switch_model_reapplies_headers.py, tests/test_install_ps1_uv_powershell_host.py, tests/tools/test_delegate.py, tests/tools/test_managed_media_gateways.py, tests/tools/test_managed_tool_gateway.py, tests/tools/test_strict_provider_selection.py, tests/tools/test_tts_openai_config.py, tests/tools/test_url_safety.py, tests/tools/test_web_tools_config.py, tools/managed_tool_gateway.py, tools/mcp_oauth.py, tools/skills_hub.py, tools/skills_sync_client.py, trajectory_compressor.py, ui-tui/scripts/billing-fixtures.tsx, ui-tui/src/__tests__/subscriptionCommand.test.ts, ui-tui/src/__tests__/subscriptionOverlay.test.tsx, ui-tui/src/app/slash/commands/subscription.ts, ui-tui/src/domain/paths.ts, uv.lock, web/src/components/SidebarFooter.tsx, web/src/pages/DocsPage.tsx, web/src/pages/SystemPage.tsx, website/docs/developer-guide/contributing.md, website/docs/developer-guide/egress-internals.md, website/docs/getting-started/installation.md, website/docs/getting-started/platform-support.md, website/docs/getting-started/quickstart.md, website/docs/getting-started/termux.md, website/docs/guides/manage-nastech-cloud-with-mcp.md, website/docs/guides/run-nastech-with-nastech-portal.md, website/docs/guides/run-nemotron-3-ultra-free.md, website/docs/index.mdx, website/docs/integrations/nastech-portal.md, website/docs/integrations/providers.md, website/docs/reference/cli-commands.md, website/docs/reference/environment-variables.md, website/docs/reference/faq.md, website/docs/reference/model-catalog.md, website/docs/user-guide/desktop.md, website/docs/user-guide/egress/iron-proxy.md, website/docs/user-guide/features/browser.md, website/docs/user-guide/features/image-generation.md, website/docs/user-guide/features/skills.md, website/docs/user-guide/features/subscription-proxy.md, website/docs/user-guide/features/tool-gateway.md, website/docs/user-guide/features/tools.md, website/docs/user-guide/features/tts.md, website/docs/user-guide/features/web-dashboard.md, website/docs/user-guide/features/web-search.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/windows-wsl-quickstart.md, website/docusaurus.config.ts, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/contributing.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/quickstart.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-nastech-with-nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/index.mdx, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/providers.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/faq.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/model-catalog.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/subscription-proxy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tools.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tts.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-native.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-wsl-quickstart.md, website/scripts/generate-llms-txt.py, website/scripts/prebuild.mjs, website/static/api/model-catalog.json, website/static/oauth/client-metadata.json


## Direct upstream tree delta

- complete: +40 ~195 -2 ↪0
- MODIFIED `agent/agent_init.py`
- MODIFIED `agent/agent_runtime_helpers.py`
- MODIFIED `agent/auxiliary_client.py`
- MODIFIED `agent/background_review.py`
- MODIFIED `agent/chat_completion_helpers.py`
- MODIFIED `agent/coding_context.py`
- MODIFIED `agent/curator.py`
- MODIFIED `agent/deadline.py`
- MODIFIED `agent/gemini_native_adapter.py`
- MODIFIED `agent/lsp/client.py`
- MODIFIED `agent/memory_manager.py`
- MODIFIED `agent/process_bootstrap.py`
- MODIFIED `agent/prompt_builder.py`
- MODIFIED `agent/skill_utils.py`
- MODIFIED `agent/system_prompt.py`
- ADDED `agent/terminal_env_provider.py`
- ADDED `agent/terminal_env_registry.py`
- MODIFIED `agent/tool_executor.py`
- ADDED `apps/desktop/e2e/zoom-preservation.spec.ts`
- ADDED `apps/desktop/electron/backend-claim.test.ts`
- ADDED `apps/desktop/electron/backend-claim.ts`
- MODIFIED `apps/desktop/electron/backend-ready.test.ts`
- MODIFIED `apps/desktop/electron/backend-ready.ts`
- ADDED `apps/desktop/electron/hud-hyprland.test.ts`
- ADDED `apps/desktop/electron/hud-hyprland.ts`
- DELETED `apps/desktop/electron/hud-input-policy.test.ts`
- DELETED `apps/desktop/electron/hud-input-policy.ts`
- MODIFIED `apps/desktop/electron/hud-ipc.ts`
- ADDED `apps/desktop/electron/hud-overlay.test.ts`
- ADDED `apps/desktop/electron/hud-overlay.ts`
- ADDED `apps/desktop/electron/hud-windowing.test.ts`
- ADDED `apps/desktop/electron/hud-windowing.ts`
- MODIFIED `apps/desktop/electron/hyprland.ts`
- MODIFIED `apps/desktop/electron/main.ts`
- MODIFIED `apps/desktop/electron/preload.ts`
- MODIFIED `apps/desktop/electron/renderer-bundle.ts`
- MODIFIED `apps/desktop/electron/window-below.test.ts`
- MODIFIED `apps/desktop/electron/window-below.ts`
- MODIFIED `apps/desktop/electron/zoom.test.ts`
- MODIFIED `apps/desktop/electron/zoom.ts`
- ADDED `apps/desktop/src/app/chat/composer/focus-chord.test.ts`
- ADDED `apps/desktop/src/app/chat/composer/focus-chord.ts`
- MODIFIED `apps/desktop/src/app/chat/composer/index.tsx`
- MODIFIED `apps/desktop/src/app/chat/pane-mirror.ts`
- MODIFIED `apps/desktop/src/app/chat/preview-tile.test.ts`
- MODIFIED `apps/desktop/src/app/chat/preview-tile.tsx`
- MODIFIED `apps/desktop/src/app/chat/right-rail/preview-browser-bar.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/right-rail/preview-browser-bar.tsx`
- MODIFIED `apps/desktop/src/app/chat/right-rail/preview-file.tsx`
- MODIFIED `apps/desktop/src/app/chat/right-rail/preview-pane.tsx`
- MODIFIED `apps/desktop/src/app/context-menu/app-context-menu.test.tsx`
- MODIFIED `apps/desktop/src/app/context-menu/app-context-menu.tsx`
- MODIFIED `apps/desktop/src/app/context-menu/store.ts`
- MODIFIED `apps/desktop/src/app/context-menu/target.ts`
- MODIFIED `apps/desktop/src/app/gateway/hooks/use-gateway-boot.ts`
- MODIFIED `apps/desktop/src/app/hooks/use-keybinds.ts`
- MODIFIED `apps/desktop/src/app/hud/composer-drag.test.ts`
- ADDED `apps/desktop/src/app/hud/glass.test.tsx`
- MODIFIED `apps/desktop/src/app/hud/glass.ts`
- MODIFIED `apps/desktop/src/app/hud/hud-shell.tsx`
- MODIFIED `apps/desktop/src/app/hud/resize-handle.test.ts`
- MODIFIED `apps/desktop/src/app/hud/resize-handle.ts`
- MODIFIED `apps/desktop/src/app/right-sidebar/files/use-project-tree.test.ts`
- MODIFIED `apps/desktop/src/app/right-sidebar/files/use-project-tree.ts`
- MODIFIED `apps/desktop/src/app/right-sidebar/index.test.tsx`
- MODIFIED `apps/desktop/src/app/right-sidebar/index.tsx`
- MODIFIED `apps/desktop/src/app/right-sidebar/terminal/selection.ts`
- MODIFIED `apps/desktop/src/app/right-sidebar/terminal/use-terminal-session.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/clarify-hydration.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/gateway-event/input-requests.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-actions.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-actions/index.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-session-actions/restore-pending-clarify.test.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-session-actions/restore-pending-clarify.ts`
- MODIFIED `apps/desktop/src/app/session/workspace-session-target.test.ts`
- MODIFIED `apps/desktop/src/app/session/workspace-session-target.ts`
- MODIFIED `apps/desktop/src/app/settings/appearance-settings.tsx`
- MODIFIED `apps/desktop/src/app/settings/model-settings.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/clarify-tool.test.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/clarify-tool.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/assistant-message.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/message-parts.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/streaming.test.tsx`
- MODIFIED `apps/desktop/src/components/chat/diff-lines.test.tsx`
- ADDED `apps/desktop/src/components/chat/vibe-hearts.test.ts`
- MODIFIED `apps/desktop/src/components/chat/vibe-hearts.tsx`
- MODIFIED `apps/desktop/src/components/pane-shell/tree/renderer/track-model.ts`
- MODIFIED `apps/desktop/src/components/pane-shell/tree/renderer/tree-group.tsx`
- MODIFIED `apps/desktop/src/components/ui/dropdown-menu.tsx`
- MODIFIED `apps/desktop/src/global.d.ts`
- MODIFIED `apps/desktop/src/i18n/ar.ts`
- MODIFIED `apps/desktop/src/i18n/en.ts`
- MODIFIED `apps/desktop/src/i18n/ja.ts`
- MODIFIED `apps/desktop/src/i18n/types.ts`
- MODIFIED `apps/desktop/src/i18n/zh-hant.ts`
- MODIFIED `apps/desktop/src/i18n/zh.ts`
- MODIFIED `apps/desktop/src/lib/chat-messages.test.ts`
- MODIFIED `apps/desktop/src/lib/chat-messages/index.ts`
- MODIFIED `apps/desktop/src/lib/chat-messages/tool-parts.ts`
- MODIFIED `apps/desktop/src/lib/json-rpc-gateway-recovery.test.ts`
- MODIFIED `apps/desktop/src/lib/keybinds/actions.ts`
- ADDED `apps/desktop/src/lib/keybinds/chords.ts`
- MODIFIED `apps/desktop/src/store/clarify.ts`
- MODIFIED `apps/desktop/src/store/preview-open-browser.test.ts`
- MODIFIED `apps/desktop/src/store/preview.test.ts`
- MODIFIED `apps/desktop/src/store/preview.ts`
- ADDED `apps/desktop/src/store/vibe-hearts-enabled.test.ts`
- ADDED `apps/desktop/src/store/vibe-hearts-enabled.ts`
- MODIFIED `apps/desktop/src/types/nastech.ts`
- ADDED `apps/shared/src/json-rpc-gateway-replay.test.ts`
- MODIFIED `apps/shared/src/json-rpc-gateway.ts`
- MODIFIED `cli-config.yaml.example`
- MODIFIED `cli.py`
- ADDED `contributors/emails/evanlee99@qq.com`
- ADDED `contributors/emails/guilherme@artiles.com.br`
- ADDED `contributors/emails/macd@google.com`
- ADDED `contributors/emails/nathanielcrush51@gmail.com`
- ADDED `contributors/emails/vignesh@openai.com`
- MODIFIED `cron/scheduler.py`
- ADDED `gateway/media_repair.py`
- MODIFIED `gateway/platforms/base.py`
- MODIFIED `gateway/platforms/signal.py`
- MODIFIED `gateway/run.py`
- MODIFIED `nastech_cli/_subprocess_compat.py`
- MODIFIED `nastech_cli/auth.py`
- MODIFIED `nastech_cli/config.py`
- MODIFIED `nastech_cli/config_defaults.py`
- MODIFIED `nastech_cli/doctor.py`
- MODIFIED `nastech_cli/main.py`
- MODIFIED `nastech_cli/models.py`
- MODIFIED `nastech_cli/plugins.py`
- MODIFIED `nastech_cli/profiles.py`
- MODIFIED `nastech_cli/setup.py`
- MODIFIED `nastech_cli/skills_config.py`
- MODIFIED `nastech_cli/status.py`
- MODIFIED `nastech_cli/web_routers/tools.py`
- MODIFIED `nastech_cli/web_server.py`
- MODIFIED `nastech_constants.py`
- MODIFIED `plugins/memory/openviking/README.md`
- MODIFIED `plugins/memory/openviking/__init__.py`
- MODIFIED `plugins/platforms/teams/adapter.py`
- MODIFIED `plugins/platforms/telegram/adapter.py`
- MODIFIED `run_agent.py`
- MODIFIED `tests/agent/lsp/_mock_lsp_server.py`
- MODIFIED `tests/agent/lsp/test_client_e2e.py`
- MODIFIED `tests/agent/lsp/test_service.py`
- MODIFIED `tests/agent/test_auxiliary_config_bridge.py`
- MODIFIED `tests/agent/test_codex_cloudflare_headers.py`
- ADDED `tests/agent/test_codex_happy_eyeballs.py`
- ADDED `tests/agent/test_codex_usage_attribution.py`
- MODIFIED `tests/agent/test_curator.py`
- MODIFIED `tests/agent/test_memory_provider.py`
- ADDED `tests/agent/test_phantom_tool_references.py`
- MODIFIED `tests/agent/test_system_prompt.py`
- ADDED `tests/agent/test_terminal_env_registry.py`
- ADDED `tests/agent/test_treekill_consolidation.py`
- MODIFIED `tests/conftest.py`
- MODIFIED `tests/cron/test_media_send_timeout.py`
- MODIFIED `tests/e2e/conftest.py`
- MODIFIED `tests/gateway/test_73771_media_resend_dedup.py`
- MODIFIED `tests/gateway/test_media_extraction.py`
- MODIFIED `tests/gateway/test_platform_base.py`
- MODIFIED `tests/gateway/test_signal.py`
- MODIFIED `tests/gateway/test_teams.py`
- MODIFIED `tests/gateway/test_teams_dotenv_isolation.py`
- ADDED `tests/gateway/test_telegram_send_reconnect_wait.py`
- MODIFIED `tests/gateway/test_tool_response_drop_recovery.py`
- MODIFIED `tests/nastech_cli/test_model_validation.py`
- MODIFIED `tests/nastech_cli/test_profiles.py`
- ADDED `tests/nastech_cli/test_serve_port_in_use.py`
- MODIFIED `tests/nastech_cli/test_setup_blank_slate.py`
- MODIFIED `tests/openviking_plugin/test_openviking.py`
- MODIFIED `tests/plugins/memory/test_openviking_provider.py`
- MODIFIED `tests/run_agent/test_primary_runtime_restore.py`
- MODIFIED `tests/run_agent/test_provider_fallback.py`
- MODIFIED `tests/run_agent/test_retry_status_buffer.py`
- MODIFIED `tests/run_agent/test_review_prompt_class_first.py`
- MODIFIED `tests/run_agent/test_switch_model_fallback_prune.py`
- MODIFIED `tests/test_nastech_constants.py`
- ADDED `tests/test_tui_gateway_event_replay.py`
- ADDED `tests/tools/test_approval_outcome_parity.py`
- MODIFIED `tests/tools/test_browser_content_none_guard.py`
- MODIFIED `tests/tools/test_browser_hardening.py`
- MODIFIED `tests/tools/test_browser_npx_warmup.py`
- MODIFIED `tests/tools/test_browser_secret_exfil.py`
- ADDED `tests/tools/test_browser_snapshot_threshold.py`
- MODIFIED `tests/tools/test_computer_use.py`
- ADDED `tests/tools/test_local_setsid_descendant_sweep.py`
- MODIFIED `tests/tools/test_send_message_tool.py`
- MODIFIED `tests/tools/test_skill_manager_tool.py`
- MODIFIED `tools/approval.py`
- MODIFIED `tools/browser_camofox.py`
- MODIFIED `tools/browser_tool.py`
- MODIFIED `tools/code_execution_tool.py`
- MODIFIED `tools/computer_use/cua_backend.py`
- MODIFIED `tools/credential_files.py`
- MODIFIED `tools/env_probe.py`
- MODIFIED `tools/environments/local.py`
- MODIFIED `tools/file_tools.py`
- MODIFIED `tools/lazy_deps.py`
- MODIFIED `tools/mcp_oauth.py`
- MODIFIED `tools/mcp_tool.py`
- MODIFIED `tools/send_message_tool.py`
- MODIFIED `tools/skill_manager_tool.py`
- MODIFIED `tools/skills_sync.py`
- MODIFIED `tools/skills_tool.py`
- MODIFIED `tools/terminal_tool.py`
- MODIFIED `tui_gateway/entry.py`
- ADDED `tui_gateway/event_replay.py`
- MODIFIED `tui_gateway/methods_session.py`
- MODIFIED `tui_gateway/server.py`
- MODIFIED `tui_gateway/ws.py`
- MODIFIED `ui-tui/src/__tests__/gatewayClient.test.ts`
- MODIFIED `ui-tui/src/gatewayClient.ts`
- MODIFIED `web/src/pages/ModelsPage.tsx`
- ADDED `website/docs/developer-guide/terminal-environment-plugin.md`
- MODIFIED `website/docs/getting-started/quickstart.md`
- MODIFIED `website/docs/guides/google-gemini.md`
- MODIFIED `website/docs/integrations/providers.md`
- MODIFIED `website/docs/reference/cli-commands.md`
- MODIFIED `website/docs/reference/environment-variables.md`
- MODIFIED `website/docs/user-guide/configuration.md`
- MODIFIED `website/docs/user-guide/desktop.md`
- MODIFIED `website/docs/user-guide/docker.md`
- MODIFIED `website/docs/user-guide/features/browser.md`
- MODIFIED `website/docs/user-guide/features/fallback-providers.md`
- MODIFIED `website/docs/user-guide/features/plugins.md`
- MODIFIED `website/docs/user-guide/features/web-dashboard.md`
- MODIFIED `website/docs/user-guide/messaging/signal.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/tools-reference.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/configuration.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/fallback-providers.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/messaging/signal.md`
- MODIFIED `website/sidebars.ts`

## Scan

10296 files scanned [audio=5, binary=7, doc=5, font=13, image=92, text=10174]


## Diff

1335 renamed, 0 rewritten, 8563 identical, 61 locked, 0 missing, 34 owned, 249 reconciled


## Fork check (vs nastech-agent)

- 10053 identical, 203 updated (+0/-0 lines), 40 added, 0 missing, 0 fork-local-unpreserved, 0 stale-upstream, 0 locked/binary, 0 collision-safe relocated, 54 preserved fork-local files, 0 violations

- features: fork 51 -> branded 51

Auto-generated by 100Ways.
