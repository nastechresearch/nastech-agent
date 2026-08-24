# Nastech Update Report #1

- upstream sha : `057dcdf236f8a6a26721c10fcc6ccb72726e272a`
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

- total files : 10204
- renamed     : 1421 (folders and file names)
- text-rewritten : 10106
- locked-copied  : 56
- binary-copied  : 8
- owned assets   : 34 (our logo/banner/mascot override upstream)

## Reconcile

- fixed : 253 files reconciled: .github/workflows/deploy-site.yml, .github/workflows/skills-index-freshness.yml, .mailmap, CONTRIBUTING.es.md, CONTRIBUTING.md, Dockerfile, README.es.md, README.md, README.ur-pk.md, README.zh-CN.md, SECURITY.es.md, SECURITY.md, agent/agent_runtime_helpers.py, agent/anthropic_adapter.py, agent/auxiliary_client.py, agent/billing_links.py, agent/billing_view.py, agent/chat_completion_helpers.py, agent/conversation_loop.py, agent/credits_tracker.py, agent/model_metadata.py, agent/prompt_builder.py, agent/proxy_sources/iron_proxy.py, agent/subscription_view.py, agent/usage_pricing.py, apps/bootstrap-installer/src-tauri/Cargo.toml, apps/desktop/README.md, apps/desktop/electron/backend-health.test.ts, apps/desktop/electron/backend-health.ts, apps/desktop/electron/connection-config.test.ts, apps/desktop/electron/main.ts, apps/desktop/electron/remote-lifecycle.ts, apps/desktop/package.json, apps/desktop/src/app/messaging/index.test.tsx, apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx, apps/desktop/src/app/settings/about-settings.tsx, apps/desktop/src/app/settings/billing/api.test.ts, apps/desktop/src/app/settings/billing/dev-fixtures.ts, apps/desktop/src/app/settings/billing/errors.test.ts, apps/desktop/src/app/settings/billing/types.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.ts, apps/desktop/src/app/settings/billing/use-charge-poller.test.ts, apps/desktop/src/app/settings/billing/use-step-up.test.tsx, apps/desktop/src/app/settings/constants.ts, apps/desktop/src/app/settings/gateway-settings.tsx, apps/desktop/src/app/settings/toolset-config-panel.test.tsx, apps/desktop/src/app/skills/embedded-hub-picker.tsx, apps/desktop/src/app/skills/index.test.tsx, apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts, apps/desktop/src/components/boot-failure-overlay.test.tsx, apps/desktop/src/components/boot-failure-overlay.tsx, apps/desktop/src/components/send-diagnostics-dialog.tsx, apps/desktop/src/contrib/plugin.ts, apps/desktop/src/i18n/en.ts, apps/desktop/src/i18n/ja.ts, apps/desktop/src/i18n/zh-hant.ts, apps/desktop/src/i18n/zh.ts, apps/desktop/src/plugins/nastech-bots/plugin.js, apps/desktop/src/sdk/index.ts, cli-config.yaml.example, eslint.config.shared.mjs, nastech_cli/auth.py, nastech_cli/banner.py, nastech_cli/config_defaults.py, nastech_cli/dashboard_auth/login_page.py, nastech_cli/dashboard_register.py, nastech_cli/debug.py, nastech_cli/diagnostics_upload.py, nastech_cli/fallback_cmd.py, nastech_cli/kanban.py, nastech_cli/main.py, nastech_cli/model_catalog.py, nastech_cli/model_switch.py, nastech_cli/models.py, nastech_cli/nastech_account.py, nastech_cli/nastech_billing.py, nastech_cli/plugins_cmd.py, nastech_cli/portal_cli.py, nastech_cli/providers.py, nastech_cli/proxy/__init__.py, nastech_cli/proxy/adapters/base.py, nastech_cli/proxy/adapters/nastech_portal.py, nastech_cli/setup.py, nastech_cli/setup_whatsapp_cloud.py, nastech_cli/skin_engine.py, nastech_cli/telegram_managed_bot.py, nastech_cli/tools_config.py, nastech_cli/uninstall.py, nastech_cli/update_cmd.py, nastech_cli/web_server.py, nastech_constants.py, package-lock.json, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/plugin.yaml, plugins/kanban/dashboard/dist/index.js, plugins/kanban/systemd/nastech-kanban-dispatcher.service, plugins/model-providers/ai-gateway/__init__.py, plugins/model-providers/fireworks/__init__.py, plugins/model-providers/kimi-coding/__init__.py, plugins/model-providers/nastech/__init__.py, plugins/model-providers/opencode-free/__init__.py, plugins/model-providers/opencode-zen/__init__.py, plugins/nastech-achievements/dashboard/dist/index.js, plugins/platforms/discord/adapter.py, plugins/platforms/email/adapter.py, plugins/platforms/photon/sidecar/package-lock.json, plugins/platforms/slack/adapter.py, run_agent.py, scripts/build_model_catalog.py, scripts/contributor_audit.py, scripts/dev-sandbox.sh, scripts/install.cmd, scripts/install.ps1, scripts/install.sh, scripts/release.py, scripts/whatsapp-bridge/package-lock.json, setup.py, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/references/background-systems.md, skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md, skills/autonomous-ai-agents/nastech-agent/references/configuration.md, skills/autonomous-ai-agents/nastech-agent/references/contributor-guide.md, skills/autonomous-ai-agents/nastech-agent/references/portal-auth-for-third-party-apps.md, skills/autonomous-ai-agents/nastech-agent/references/providers-and-models.md, skills/autonomous-ai-agents/nastech-agent/references/webhooks.md, tests/agent/test_anthropic_adapter.py, tests/agent/test_auxiliary_client.py, tests/agent/test_auxiliary_main_first.py, tests/agent/test_auxiliary_transport_autodetect.py, tests/agent/test_billing_links.py, tests/agent/test_credential_pool.py, tests/agent/test_credits_policy.py, tests/agent/test_error_classifier.py, tests/agent/test_model_metadata.py, tests/agent/test_nastech_credits_gauge.py, tests/agent/test_nastech_oauth_401_guidance.py, tests/agent/test_nastech_portal_anthropic_wire.py, tests/agent/transports/test_chat_completions.py, tests/cli/test_cli_first_run_setup.py, tests/cli/test_cli_provider_resolution.py, tests/cli/test_show_config_credential.py, tests/docker/test_sqlite_runtime.py, tests/gateway/test_discord_format.py, tests/gateway/test_run_progress_topics.py, tests/gateway/test_status_command.py, tests/gateway/test_usage_command.py, tests/nastech_cli/test_auth_nastech_provider.py, tests/nastech_cli/test_base_url_host_identity.py, tests/nastech_cli/test_dashboard_auth_gate.py, tests/nastech_cli/test_dashboard_register.py, tests/nastech_cli/test_fireworks_provider.py, tests/nastech_cli/test_gateway_restart_loop.py, tests/nastech_cli/test_model_catalog.py, tests/nastech_cli/test_nastech_auth_keepalive.py, tests/nastech_cli/test_nastech_auth_status_cache.py, tests/nastech_cli/test_nastech_inference_url_validation.py, tests/nastech_cli/test_nastech_portal_staging_allowlist.py, tests/nastech_cli/test_nastech_reasoning_metadata.py, tests/nastech_cli/test_proxy.py, tests/nastech_cli/test_reasoning_caps_disk_cache.py, tests/nastech_cli/test_sale_pricing.py, tests/nastech_cli/test_web_oauth_dispatch.py, tests/plugins/dashboard_auth/test_nastech_provider.py, tests/plugins/image_gen/check_parity_vs_main.py, tests/plugins/image_gen/test_openrouter_compat_provider.py, tests/plugins/test_chronos_verify.py, tests/run_agent/test_anthropic_prompt_cache_policy.py, tests/run_agent/test_primary_runtime_restore.py, tests/run_agent/test_provider_attribution_headers.py, tests/run_agent/test_provider_fallback.py, tests/run_agent/test_provider_parity.py, tests/run_agent/test_run_agent.py, tests/run_agent/test_switch_model_reapplies_headers.py, tests/test_install_ps1_uv_powershell_host.py, tests/tools/test_delegate.py, tests/tools/test_managed_media_gateways.py, tests/tools/test_managed_tool_gateway.py, tests/tools/test_strict_provider_selection.py, tests/tools/test_tts_openai_config.py, tests/tools/test_url_safety.py, tests/tools/test_web_tools_config.py, tools/managed_tool_gateway.py, tools/mcp_oauth.py, tools/skills_hub.py, tools/skills_sync_client.py, trajectory_compressor.py, ui-tui/scripts/billing-fixtures.tsx, ui-tui/src/__tests__/subscriptionCommand.test.ts, ui-tui/src/__tests__/subscriptionOverlay.test.tsx, ui-tui/src/app/slash/commands/subscription.ts, ui-tui/src/domain/paths.ts, uv.lock, web/src/components/SidebarFooter.tsx, web/src/pages/DocsPage.tsx, web/src/pages/SystemPage.tsx, website/docs/developer-guide/contributing.md, website/docs/developer-guide/egress-internals.md, website/docs/getting-started/installation.md, website/docs/getting-started/platform-support.md, website/docs/getting-started/quickstart.md, website/docs/getting-started/termux.md, website/docs/guides/manage-nastech-cloud-with-mcp.md, website/docs/guides/run-nastech-with-nastech-portal.md, website/docs/guides/run-nemotron-3-ultra-free.md, website/docs/index.mdx, website/docs/integrations/nastech-portal.md, website/docs/integrations/providers.md, website/docs/reference/cli-commands.md, website/docs/reference/environment-variables.md, website/docs/reference/faq.md, website/docs/reference/model-catalog.md, website/docs/user-guide/desktop.md, website/docs/user-guide/egress/iron-proxy.md, website/docs/user-guide/features/browser.md, website/docs/user-guide/features/image-generation.md, website/docs/user-guide/features/skills.md, website/docs/user-guide/features/subscription-proxy.md, website/docs/user-guide/features/tool-gateway.md, website/docs/user-guide/features/tools.md, website/docs/user-guide/features/tts.md, website/docs/user-guide/features/web-dashboard.md, website/docs/user-guide/features/web-search.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/windows-wsl-quickstart.md, website/docusaurus.config.ts, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/contributing.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/quickstart.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-nastech-with-nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/index.mdx, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/providers.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/faq.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/model-catalog.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/subscription-proxy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tools.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tts.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-native.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-wsl-quickstart.md, website/scripts/generate-llms-txt.py, website/scripts/prebuild.mjs, website/static/api/model-catalog.json, website/static/oauth/client-metadata.json


## Direct upstream tree delta

- complete: +53 ~205 -0 ↪0
- MODIFIED `Dockerfile`
- MODIFIED `agent/agent_runtime_helpers.py`
- MODIFIED `agent/auxiliary_client.py`
- MODIFIED `agent/codex_runtime.py`
- MODIFIED `agent/context_compressor.py`
- MODIFIED `agent/conversation_loop.py`
- MODIFIED `agent/model_metadata.py`
- MODIFIED `agent/turn_context.py`
- MODIFIED `agent/usage_pricing.py`
- ADDED `apps/desktop/electron/api-transport.test.ts`
- ADDED `apps/desktop/electron/api-transport.ts`
- MODIFIED `apps/desktop/electron/connection-config.test.ts`
- MODIFIED `apps/desktop/electron/connection-config.ts`
- MODIFIED `apps/desktop/electron/gateway-file-download-transport.test.ts`
- MODIFIED `apps/desktop/electron/gateway-file-download.test.ts`
- MODIFIED `apps/desktop/electron/gateway-file-download.ts`
- MODIFIED `apps/desktop/electron/hardening.ts`
- ADDED `apps/desktop/electron/hud-game-overlay.test.ts`
- ADDED `apps/desktop/electron/hud-game-overlay.ts`
- ADDED `apps/desktop/electron/hud-geometry.test.ts`
- ADDED `apps/desktop/electron/hud-geometry.ts`
- ADDED `apps/desktop/electron/hud-input-policy.test.ts`
- ADDED `apps/desktop/electron/hud-input-policy.ts`
- MODIFIED `apps/desktop/electron/hud-ipc.ts`
- MODIFIED `apps/desktop/electron/main.ts`
- MODIFIED `apps/desktop/electron/media-protocol.test.ts`
- MODIFIED `apps/desktop/electron/media-protocol.ts`
- MODIFIED `apps/desktop/electron/preload.ts`
- MODIFIED `apps/desktop/electron/renderer-bundle.test.ts`
- MODIFIED `apps/desktop/electron/renderer-bundle.ts`
- MODIFIED `apps/desktop/electron/window-below.ts`
- MODIFIED `apps/desktop/electron/zoom.test.ts`
- MODIFIED `apps/desktop/electron/zoom.ts`
- MODIFIED `apps/desktop/src/app/chat/composer/controls.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/controls.tsx`
- ADDED `apps/desktop/src/app/chat/composer/hooks/use-auto-speak-replies.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/index.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/micro-actions.tsx`
- MODIFIED `apps/desktop/src/app/chat/preview-tile.test.ts`
- MODIFIED `apps/desktop/src/app/chat/preview-tile.tsx`
- MODIFIED `apps/desktop/src/app/chat/session-tile-actions.ts`
- MODIFIED `apps/desktop/src/app/chat/sidebar/cron-jobs-section.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/session-row.tsx`
- MODIFIED `apps/desktop/src/app/gateway/hooks/use-gateway-boot.test.tsx`
- MODIFIED `apps/desktop/src/app/gateway/hooks/use-gateway-boot.ts`
- MODIFIED `apps/desktop/src/app/hud/click-through.ts`
- MODIFIED `apps/desktop/src/app/hud/composer-drag.test.ts`
- MODIFIED `apps/desktop/src/app/hud/composer-drag.ts`
- ADDED `apps/desktop/src/app/hud/game-overlay.ts`
- MODIFIED `apps/desktop/src/app/hud/hud-shell.tsx`
- ADDED `apps/desktop/src/app/hud/resize-handle.test.ts`
- MODIFIED `apps/desktop/src/app/hud/resize-handle.ts`
- MODIFIED `apps/desktop/src/app/right-sidebar/files/use-project-tree.test.ts`
- MODIFIED `apps/desktop/src/app/right-sidebar/files/use-project-tree.ts`
- MODIFIED `apps/desktop/src/app/right-sidebar/index.test.tsx`
- MODIFIED `apps/desktop/src/app/right-sidebar/index.tsx`
- MODIFIED `apps/desktop/src/app/right-sidebar/terminal/rail.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/index.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/rewind.test.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/rewind.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-actions.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-actions/index.ts`
- MODIFIED `apps/desktop/src/app/skills/index.test.tsx`
- ADDED `apps/desktop/src/components/chat/diff-lines.test.tsx`
- MODIFIED `apps/desktop/src/components/chat/diff-lines.tsx`
- MODIFIED `apps/desktop/src/components/ui/sidebar.tsx`
- MODIFIED `apps/desktop/src/components/ui/tabs.tsx`
- MODIFIED `apps/desktop/src/components/ui/text-tab.tsx`
- MODIFIED `apps/desktop/src/global.d.ts`
- MODIFIED `apps/desktop/src/i18n/ar.ts`
- MODIFIED `apps/desktop/src/i18n/en.ts`
- MODIFIED `apps/desktop/src/i18n/ja.ts`
- MODIFIED `apps/desktop/src/i18n/types.ts`
- MODIFIED `apps/desktop/src/i18n/zh-hant.ts`
- MODIFIED `apps/desktop/src/i18n/zh.ts`
- MODIFIED `apps/desktop/src/lib/chat-messages.test.ts`
- MODIFIED `apps/desktop/src/lib/chat-messages/hydration.ts`
- MODIFIED `apps/desktop/src/lib/desktop-fs.test.ts`
- MODIFIED `apps/desktop/src/lib/desktop-fs.ts`
- MODIFIED `apps/desktop/src/lib/desktop-git.test.ts`
- MODIFIED `apps/desktop/src/lib/desktop-git.ts`
- ADDED `apps/desktop/src/lib/json-rpc-gateway-heartbeat.test.ts`
- ADDED `apps/desktop/src/lib/json-rpc-gateway-recovery.test.ts`
- MODIFIED `apps/desktop/src/lib/media.remote.test.ts`
- MODIFIED `apps/desktop/src/lib/media.ts`
- MODIFIED `apps/desktop/src/lib/platform.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/plugin.js`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/bot-relay.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/embed-real-capabilities.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/group-chat.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/group-room-ux.test.mjs`
- ADDED `apps/desktop/src/plugins/nastech-bots/tests/group-turn-lease.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/multi-source-roster.test.mjs`
- ADDED `apps/desktop/src/plugins/nastech-bots/tests/orphaned-connection-members.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/relay-push-drain.test.mjs`
- ADDED `apps/desktop/src/plugins/nastech-bots/tests/relay-socket-retention.test.mjs`
- MODIFIED `apps/desktop/src/sdk/index.ts`
- MODIFIED `apps/desktop/src/store/gateway-profile-request.test.ts`
- ADDED `apps/desktop/src/store/gateway-relay-retention.test.ts`
- MODIFIED `apps/desktop/src/store/gateway.ts`
- MODIFIED `apps/desktop/src/store/hud.test.ts`
- MODIFIED `apps/desktop/src/store/hud.ts`
- MODIFIED `apps/desktop/src/store/session-dot-state.test.ts`
- MODIFIED `apps/desktop/src/store/session-dot-state.ts`
- MODIFIED `apps/desktop/src/store/updates.test.ts`
- MODIFIED `apps/desktop/src/store/updates.ts`
- MODIFIED `apps/desktop/src/styles.css`
- MODIFIED `apps/desktop/src/types/nastech.ts`
- MODIFIED `apps/shared/src/json-rpc-gateway.ts`
- MODIFIED `batch_runner.py`
- MODIFIED `cli.py`
- ADDED `contributors/emails/KHALIDagara@users.noreply.github.com`
- ADDED `contributors/emails/beplee@users.noreply.github.com`
- ADDED `contributors/emails/bradmarshall987@users.noreply.github.com`
- ADDED `contributors/emails/breakout@protonmail.com`
- ADDED `contributors/emails/cycorld.com@gmail.com`
- ADDED `contributors/emails/doug@buck.co`
- ADDED `contributors/emails/jeremy.randria@gmail.com`
- ADDED `contributors/emails/kaloyan.chernev@aifnet.com`
- ADDED `contributors/emails/quexl1@chinatelecom.cn`
- ADDED `contributors/emails/ragingbullniu@gmail.com`
- ADDED `contributors/emails/shanthan@oneam.ai`
- MODIFIED `cron/__init__.py`
- MODIFIED `cron/jobs.py`
- MODIFIED `cron/scheduler.py`
- MODIFIED `cron/scheduler_provider.py`
- MODIFIED `gateway/pairing.py`
- MODIFIED `gateway/platforms/signal.py`
- MODIFIED `gateway/platforms/weixin.py`
- MODIFIED `gateway/platforms/yuanbao.py`
- MODIFIED `gateway/run.py`
- MODIFIED `gateway/session.py`
- MODIFIED `gateway/slash_commands.py`
- MODIFIED `nastech_cli/_parser.py`
- MODIFIED `nastech_cli/auth.py`
- MODIFIED `nastech_cli/cli_output.py`
- MODIFIED `nastech_cli/config_defaults.py`
- MODIFIED `nastech_cli/config_migrations.py`
- MODIFIED `nastech_cli/console_engine.py`
- MODIFIED `nastech_cli/cron.py`
- MODIFIED `nastech_cli/curator.py`
- MODIFIED `nastech_cli/curses_ui.py`
- MODIFIED `nastech_cli/dashboard_auth/base.py`
- MODIFIED `nastech_cli/dashboard_auth/cookies.py`
- MODIFIED `nastech_cli/dashboard_auth/routes.py`
- MODIFIED `nastech_cli/main.py`
- MODIFIED `nastech_cli/setup.py`
- MODIFIED `nastech_cli/subcommands/cron.py`
- MODIFIED `nastech_cli/update_cmd.py`
- MODIFIED `nastech_cli/web_routers/sessions.py`
- MODIFIED `nastech_cli/web_server.py`
- MODIFIED `nastech_constants.py`
- MODIFIED `nastech_state.py`
- MODIFIED `nastech_state_portability.py`
- MODIFIED `plugins/memory/hindsight/__init__.py`
- MODIFIED `plugins/platforms/telegram/adapter.py`
- MODIFIED `plugins/platforms/wecom/adapter.py`
- MODIFIED `run_agent.py`
- MODIFIED `scripts/desktop-update/posix.sh`
- MODIFIED `scripts/desktop-update/windows.ps1`
- MODIFIED `tests/agent/test_auxiliary_client.py`
- MODIFIED `tests/agent/test_model_metadata_local_ctx.py`
- MODIFIED `tests/agent/test_reference_handoff_active_turn.py`
- MODIFIED `tests/agent/test_usage_pricing.py`
- MODIFIED `tests/cli/test_cli_retry.py`
- ADDED `tests/cron/test_87033_cronjob_gateway_liveness.py`
- ADDED `tests/cron/test_cron_empty_payload.py`
- ADDED `tests/cron/test_misfire_backstop_oneshot_grace.py`
- ADDED `tests/cron/test_oneshot_grace_due_scan.py`
- ADDED `tests/cron/test_oneshot_guard_warning.py`
- MODIFIED `tests/cron/test_rewrite_skill_refs.py`
- ADDED `tests/cron/test_terminal_job_rearm.py`
- MODIFIED `tests/gateway/test_multiplex_profile_authz.py`
- MODIFIED `tests/gateway/test_pairing.py`
- ADDED `tests/gateway/test_platform_authz_scope.py`
- MODIFIED `tests/gateway/test_replace_child_reap.py`
- MODIFIED `tests/gateway/test_retry_replacement.py`
- MODIFIED `tests/gateway/test_runner_startup_failures.py`
- MODIFIED `tests/gateway/test_telegram_init_deadline.py`
- MODIFIED `tests/gateway/test_undo_rewind_session.py`
- MODIFIED `tests/gateway/test_wecom.py`
- MODIFIED `tests/gateway/test_weixin_secret_scope.py`
- ADDED `tests/gateway/test_yuanbao_secret_scope.py`
- ADDED `tests/nastech_cli/test_auth_key_prefix_skip.py`
- MODIFIED `tests/nastech_cli/test_cli_output.py`
- MODIFIED `tests/nastech_cli/test_config.py`
- ADDED `tests/nastech_cli/test_curator_pin_unmanaged.py`
- ADDED `tests/nastech_cli/test_curator_pin_visibility.py`
- MODIFIED `tests/nastech_cli/test_curses_arrow_keys.py`
- MODIFIED `tests/nastech_cli/test_dashboard_auth_cookies.py`
- ADDED `tests/nastech_cli/test_desktop_cron_ticker_profiles.py`
- MODIFIED `tests/nastech_cli/test_gui_command.py`
- MODIFIED `tests/nastech_cli/test_setup_prompt_menus.py`
- MODIFIED `tests/nastech_cli/test_setup_reconfigure.py`
- MODIFIED `tests/nastech_cli/test_startup_plugin_gating.py`
- MODIFIED `tests/nastech_cli/test_terminal_menu_fallbacks.py`
- ADDED `tests/nastech_cli/test_top_level_value_flags_parity.py`
- ADDED `tests/nastech_cli/test_update_fleet_check_fail_closed.py`
- ADDED `tests/nastech_cli/test_update_handoff_exit.py`
- MODIFIED `tests/nastech_cli/test_web_server.py`
- MODIFIED `tests/nastech_cli/test_web_server_pty_reconnect.py`
- ADDED `tests/nastech_state/test_composite_carrier_rewind.py`
- MODIFIED `tests/plugins/memory/test_hindsight_provider.py`
- MODIFIED `tests/run_agent/test_anthropic_prompt_cache_policy.py`
- ADDED `tests/run_agent/test_codex_sdk_transform_bypass.py`
- MODIFIED `tests/run_agent/test_identity_flush.py`
- MODIFIED `tests/run_agent/test_native_compaction.py`
- MODIFIED `tests/run_agent/test_run_agent.py`
- MODIFIED `tests/run_agent/test_run_agent_codex_responses.py`
- MODIFIED `tests/run_agent/test_thinking_only_sanitizer.py`
- ADDED `tests/test_89315_replace_ownership_guard.py`
- MODIFIED `tests/test_batch_runner_checkpoint.py`
- ADDED `tests/test_batch_runner_discard_resume.py`
- MODIFIED `tests/test_compression_watermark_commit.py`
- MODIFIED `tests/test_nastech_constants.py`
- MODIFIED `tests/test_tui_gateway_server.py`
- MODIFIED `tests/test_tui_gateway_ws.py`
- MODIFIED `tests/tools/test_base_environment.py`
- ADDED `tests/tools/test_bot_relay_windows_paths.py`
- MODIFIED `tests/tools/test_bot_retry_policy.py`
- MODIFIED `tests/tools/test_bot_turn_lock.py`
- MODIFIED `tests/tools/test_docker_environment.py`
- MODIFIED `tests/tools/test_hardline_blocklist.py`
- ADDED `tests/tools/test_mcp_timeout_resolution.py`
- ADDED `tests/tools/test_singularity_persistent_overlay.py`
- MODIFIED `tests/tools/test_watch_patterns.py`
- MODIFIED `tests/tui_gateway/test_bot_relay_methods.py`
- ADDED `tests/tui_gateway/test_composite_carrier_rewind.py`
- ADDED `tests/tui_gateway/test_ping_probe.py`
- MODIFIED `tests/tui_gateway/test_stranded_session_adoption.py`
- MODIFIED `tools/approval.py`
- MODIFIED `tools/bot_mode_dm.py`
- MODIFIED `tools/bot_relay.py`
- MODIFIED `tools/cronjob_tools.py`
- MODIFIED `tools/environments/base.py`
- MODIFIED `tools/environments/docker.py`
- MODIFIED `tools/environments/singularity.py`
- MODIFIED `tools/mcp_tool.py`
- MODIFIED `tools/process_registry.py`
- MODIFIED `tools/skill_usage.py`
- MODIFIED `tools/terminal_tool.py`
- MODIFIED `tui_gateway/methods_bot_relay.py`
- MODIFIED `tui_gateway/methods_prompt.py`
- MODIFIED `tui_gateway/methods_session.py`
- MODIFIED `tui_gateway/methods_tools.py`
- MODIFIED `tui_gateway/server.py`
- MODIFIED `tui_gateway/ws.py`
- MODIFIED `ui-tui/src/__tests__/gatewayClient.test.ts`
- MODIFIED `ui-tui/src/gatewayClient.ts`
- MODIFIED `ui-tui/src/gatewayTypes.ts`
- MODIFIED `web/src/lib/pty-scroll.test.ts`
- MODIFIED `web/src/lib/pty-scroll.ts`
- MODIFIED `web/src/pages/ChatPage.tsx`
- MODIFIED `website/docs/guides/cron-troubleshooting.md`
- MODIFIED `website/docs/user-guide/configuring-models.md`
- MODIFIED `website/docs/user-guide/desktop.md`
- MODIFIED `website/docs/user-guide/features/web-dashboard.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/cron-troubleshooting.md`

## Scan

10258 files scanned [audio=5, binary=7, doc=5, font=13, image=92, text=10136]


## Diff

1334 renamed, 0 rewritten, 8527 identical, 61 locked, 0 missing, 34 owned, 248 reconciled


## Fork check (vs nastech-agent)

- 9991 identical, 214 updated (+0/-0 lines), 53 added, 0 missing, 0 fork-local-unpreserved, 0 stale-upstream, 0 locked/binary, 0 collision-safe relocated, 54 preserved fork-local files, 0 violations

- features: fork 51 -> branded 51

Auto-generated by 100Ways.
