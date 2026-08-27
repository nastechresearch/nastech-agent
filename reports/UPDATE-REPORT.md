# Nastech Update Report #1

- upstream sha : `ef46ec03e11452eab74e261147668fb64a3d9fd3`
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

- total files : 10462
- renamed     : 1457 (folders and file names)
- text-rewritten : 10364
- locked-copied  : 56
- binary-copied  : 8
- owned assets   : 34 (our logo/banner/mascot override upstream)

## Reconcile

- fixed : 256 files reconciled: .github/workflows/deploy-site.yml, .github/workflows/deploy-site.yml, .github/workflows/skills-index-freshness.yml, .mailmap, CONTRIBUTING.es.md, CONTRIBUTING.md, Dockerfile, README.es.md, README.md, README.ur-pk.md, README.zh-CN.md, SECURITY.es.md, SECURITY.md, agent/agent_runtime_helpers.py, agent/anthropic_adapter.py, agent/auxiliary_client.py, agent/billing_links.py, agent/billing_view.py, agent/chat_completion_helpers.py, agent/conversation_loop.py, agent/credits_tracker.py, agent/model_metadata.py, agent/prompt_builder.py, agent/proxy_sources/iron_proxy.py, agent/subscription_view.py, agent/usage_pricing.py, apps/bootstrap-installer/src-tauri/Cargo.toml, apps/desktop/README.md, apps/desktop/electron/backend-health.test.ts, apps/desktop/electron/backend-health.ts, apps/desktop/electron/connection-config.test.ts, apps/desktop/electron/main.ts, apps/desktop/electron/oauth-partition.test.ts, apps/desktop/electron/remote-lifecycle.ts, apps/desktop/package.json, apps/desktop/src/app/messaging/index.test.tsx, apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx, apps/desktop/src/app/settings/about-settings.tsx, apps/desktop/src/app/settings/billing/api.test.ts, apps/desktop/src/app/settings/billing/dev-fixtures.ts, apps/desktop/src/app/settings/billing/errors.test.ts, apps/desktop/src/app/settings/billing/types.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.ts, apps/desktop/src/app/settings/billing/use-charge-poller.test.ts, apps/desktop/src/app/settings/billing/use-step-up.test.tsx, apps/desktop/src/app/settings/constants.ts, apps/desktop/src/app/settings/gateway-settings.tsx, apps/desktop/src/app/settings/toolset-config-panel.test.tsx, apps/desktop/src/app/skills/embedded-hub-picker.tsx, apps/desktop/src/app/skills/index.test.tsx, apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts, apps/desktop/src/components/boot-failure-overlay.test.tsx, apps/desktop/src/components/boot-failure-overlay.tsx, apps/desktop/src/components/send-diagnostics-dialog.tsx, apps/desktop/src/contrib/plugin.ts, apps/desktop/src/i18n/en.ts, apps/desktop/src/i18n/ja.ts, apps/desktop/src/i18n/zh-hant.ts, apps/desktop/src/i18n/zh.ts, apps/desktop/src/plugins/nastech-bots/plugin.js, apps/desktop/src/sdk/index.ts, cli-config.yaml.example, eslint.config.shared.mjs, nastech_cli/auth.py, nastech_cli/banner.py, nastech_cli/config_defaults.py, nastech_cli/dashboard_auth/login_page.py, nastech_cli/dashboard_register.py, nastech_cli/debug.py, nastech_cli/diagnostics_upload.py, nastech_cli/fallback_cmd.py, nastech_cli/kanban.py, nastech_cli/main.py, nastech_cli/model_catalog.py, nastech_cli/model_switch.py, nastech_cli/models.py, nastech_cli/nastech_account.py, nastech_cli/nastech_billing.py, nastech_cli/plugins_cmd.py, nastech_cli/portal_cli.py, nastech_cli/providers.py, nastech_cli/proxy/__init__.py, nastech_cli/proxy/adapters/base.py, nastech_cli/proxy/adapters/nastech_portal.py, nastech_cli/setup.py, nastech_cli/setup_whatsapp_cloud.py, nastech_cli/skin_engine.py, nastech_cli/telegram_managed_bot.py, nastech_cli/tools_config.py, nastech_cli/uninstall.py, nastech_cli/update_cmd.py, nastech_cli/web_server.py, nastech_constants.py, package-lock.json, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/plugin.yaml, plugins/kanban/dashboard/dist/index.js, plugins/kanban/systemd/nastech-kanban-dispatcher.service, plugins/model-providers/ai-gateway/__init__.py, plugins/model-providers/fireworks/__init__.py, plugins/model-providers/kimi-coding/__init__.py, plugins/model-providers/nastech/__init__.py, plugins/model-providers/opencode-free/__init__.py, plugins/model-providers/opencode-zen/__init__.py, plugins/nastech-achievements/dashboard/dist/index.js, plugins/platforms/discord/adapter.py, plugins/platforms/email/adapter.py, plugins/platforms/photon/sidecar/package-lock.json, plugins/platforms/slack/adapter.py, run_agent.py, scripts/build_model_catalog.py, scripts/contributor_audit.py, scripts/dev-sandbox.sh, scripts/install.cmd, scripts/install.ps1, scripts/install.sh, scripts/release.py, scripts/whatsapp-bridge/package-lock.json, setup.py, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/references/background-systems.md, skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md, skills/autonomous-ai-agents/nastech-agent/references/configuration.md, skills/autonomous-ai-agents/nastech-agent/references/contributor-guide.md, skills/autonomous-ai-agents/nastech-agent/references/portal-auth-for-third-party-apps.md, skills/autonomous-ai-agents/nastech-agent/references/providers-and-models.md, skills/autonomous-ai-agents/nastech-agent/references/webhooks.md, tests/agent/test_anthropic_adapter.py, tests/agent/test_auxiliary_client.py, tests/agent/test_auxiliary_main_first.py, tests/agent/test_auxiliary_transport_autodetect.py, tests/agent/test_billing_links.py, tests/agent/test_credential_pool.py, tests/agent/test_credits_policy.py, tests/agent/test_error_classifier.py, tests/agent/test_model_metadata.py, tests/agent/test_nastech_credits_gauge.py, tests/agent/test_nastech_oauth_401_guidance.py, tests/agent/test_nastech_portal_anthropic_wire.py, tests/agent/test_phantom_tool_references.py, tests/agent/transports/test_chat_completions.py, tests/cli/test_cli_first_run_setup.py, tests/cli/test_cli_provider_resolution.py, tests/cli/test_show_config_credential.py, tests/docker/test_sqlite_runtime.py, tests/gateway/test_discord_format.py, tests/gateway/test_run_progress_topics.py, tests/gateway/test_status_command.py, tests/gateway/test_usage_command.py, tests/nastech_cli/test_auth_nastech_provider.py, tests/nastech_cli/test_base_url_host_identity.py, tests/nastech_cli/test_dashboard_auth_gate.py, tests/nastech_cli/test_dashboard_register.py, tests/nastech_cli/test_fireworks_provider.py, tests/nastech_cli/test_gateway_restart_loop.py, tests/nastech_cli/test_model_catalog.py, tests/nastech_cli/test_nastech_auth_keepalive.py, tests/nastech_cli/test_nastech_auth_status_cache.py, tests/nastech_cli/test_nastech_inference_url_validation.py, tests/nastech_cli/test_nastech_portal_staging_allowlist.py, tests/nastech_cli/test_nastech_reasoning_metadata.py, tests/nastech_cli/test_proxy.py, tests/nastech_cli/test_reasoning_caps_disk_cache.py, tests/nastech_cli/test_sale_pricing.py, tests/nastech_cli/test_web_oauth_dispatch.py, tests/plugins/dashboard_auth/test_nastech_provider.py, tests/plugins/image_gen/check_parity_vs_main.py, tests/plugins/image_gen/test_openrouter_compat_provider.py, tests/plugins/test_chronos_verify.py, tests/run_agent/test_anthropic_prompt_cache_policy.py, tests/run_agent/test_primary_runtime_restore.py, tests/run_agent/test_provider_attribution_headers.py, tests/run_agent/test_provider_fallback.py, tests/run_agent/test_provider_parity.py, tests/run_agent/test_run_agent.py, tests/run_agent/test_switch_model_reapplies_headers.py, tests/test_install_ps1_uv_powershell_host.py, tests/tools/test_delegate.py, tests/tools/test_managed_media_gateways.py, tests/tools/test_managed_tool_gateway.py, tests/tools/test_strict_provider_selection.py, tests/tools/test_tts_openai_config.py, tests/tools/test_url_safety.py, tests/tools/test_web_tools_config.py, tools/managed_tool_gateway.py, tools/mcp_oauth.py, tools/skills_hub.py, tools/skills_sync_client.py, trajectory_compressor.py, ui-tui/scripts/billing-fixtures.tsx, ui-tui/src/__tests__/subscriptionCommand.test.ts, ui-tui/src/__tests__/subscriptionOverlay.test.tsx, ui-tui/src/app/slash/commands/subscription.ts, ui-tui/src/domain/paths.ts, uv.lock, web/src/components/SidebarFooter.tsx, web/src/pages/DocsPage.tsx, web/src/pages/SystemPage.tsx, website/docs/developer-guide/contributing.md, website/docs/developer-guide/egress-internals.md, website/docs/getting-started/installation.md, website/docs/getting-started/platform-support.md, website/docs/getting-started/quickstart.md, website/docs/getting-started/termux.md, website/docs/guides/manage-nastech-cloud-with-mcp.md, website/docs/guides/run-nastech-with-nastech-portal.md, website/docs/guides/run-nemotron-3-ultra-free.md, website/docs/index.mdx, website/docs/integrations/nastech-portal.md, website/docs/integrations/providers.md, website/docs/reference/cli-commands.md, website/docs/reference/environment-variables.md, website/docs/reference/faq.md, website/docs/reference/model-catalog.md, website/docs/user-guide/desktop.md, website/docs/user-guide/egress/iron-proxy.md, website/docs/user-guide/features/browser.md, website/docs/user-guide/features/image-generation.md, website/docs/user-guide/features/skills.md, website/docs/user-guide/features/subscription-proxy.md, website/docs/user-guide/features/tool-gateway.md, website/docs/user-guide/features/tools.md, website/docs/user-guide/features/tts.md, website/docs/user-guide/features/web-dashboard.md, website/docs/user-guide/features/web-search.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/windows-wsl-quickstart.md, website/docusaurus.config.ts, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/contributing.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/quickstart.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-nastech-with-nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/index.mdx, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/providers.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/faq.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/model-catalog.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/subscription-proxy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tools.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tts.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-native.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-wsl-quickstart.md, website/scripts/generate-llms-txt.py, website/scripts/prebuild.mjs, website/static/api/model-catalog.json, website/static/oauth/client-metadata.json


## Direct upstream tree delta

- complete: +30 ~108 -3 ↪0
- MODIFIED `agent/context_compressor.py`
- MODIFIED `agent/conversation_compression.py`
- MODIFIED `agent/file_safety.py`
- MODIFIED `apps/desktop/electron/backend-dial-claim.test.ts`
- MODIFIED `apps/desktop/electron/main.ts`
- ADDED `apps/desktop/electron/managed-ssh-update.test.ts`
- ADDED `apps/desktop/electron/managed-ssh-update.ts`
- MODIFIED `apps/desktop/electron/pool-eviction.test.ts`
- MODIFIED `apps/desktop/electron/preload.ts`
- MODIFIED `apps/desktop/electron/remote-lifecycle.test.ts`
- MODIFIED `apps/desktop/electron/remote-lifecycle.ts`
- MODIFIED `apps/desktop/electron/ssh-bootstrap-coordinator.ts`
- MODIFIED `apps/desktop/electron/windows-remote-lifecycle.test.ts`
- MODIFIED `apps/desktop/electron/windows-remote-lifecycle.ts`
- ADDED `apps/desktop/src/api/plugins.test.ts`
- MODIFIED `apps/desktop/src/api/plugins.ts`
- MODIFIED `apps/desktop/src/app/gateway/hooks/use-gateway-boot.test.tsx`
- MODIFIED `apps/desktop/src/app/gateway/hooks/use-gateway-boot.ts`
- MODIFIED `apps/desktop/src/app/gateway/hooks/use-gateway-request.test.ts`
- MODIFIED `apps/desktop/src/app/gateway/hooks/use-gateway-request.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-model-controls.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-actions/index.ts`
- MODIFIED `apps/desktop/src/app/settings/constants.ts`
- MODIFIED `apps/desktop/src/app/settings/gateway-settings.test.tsx`
- MODIFIED `apps/desktop/src/app/settings/gateway-settings.tsx`
- ADDED `apps/desktop/src/app/settings/managed-updates-section.tsx`
- MODIFIED `apps/desktop/src/app/shell/model-menu-panel.test.tsx`
- MODIFIED `apps/desktop/src/app/shell/model-menu-panel.tsx`
- MODIFIED `apps/desktop/src/global.d.ts`
- MODIFIED `apps/desktop/src/i18n/en.ts`
- MODIFIED `apps/desktop/src/i18n/types.ts`
- MODIFIED `apps/desktop/src/i18n/zh.ts`
- ADDED `apps/desktop/src/lib/gateway-liveness-policy.test.ts`
- ADDED `apps/desktop/src/lib/gateway-liveness-policy.ts`
- ADDED `apps/desktop/src/lib/guarded-model-switch.ts`
- MODIFIED `apps/desktop/src/lib/model-options.test.ts`
- MODIFIED `apps/desktop/src/lib/model-options.ts`
- MODIFIED `apps/desktop/src/lib/voice-playback.routing.test.ts`
- MODIFIED `apps/desktop/src/lib/voice-playback.ts`
- MODIFIED `apps/desktop/src/lib/with-timeout.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/plugin.js`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/activity-toasts.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/bot-attention-badge.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/embed-skills-view.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/group-activity.test.mjs`
- ADDED `apps/desktop/src/plugins/nastech-bots/tests/model-picker-settle.test.mjs`
- ADDED `apps/desktop/src/plugins/nastech-bots/tests/model-switch-confirm.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/multi-source-roster.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/roster-groups.test.mjs`
- MODIFIED `apps/desktop/src/sdk/index.ts`
- MODIFIED `apps/desktop/src/sdk/profile-routing.test.ts`
- MODIFIED `apps/desktop/src/store/gateway-activation-prune-lease.test.ts`
- MODIFIED `apps/desktop/src/store/gateway.test.ts`
- MODIFIED `apps/desktop/src/store/gateway.ts`
- ADDED `apps/desktop/src/store/managed-updates.test.ts`
- ADDED `apps/desktop/src/store/managed-updates.ts`
- MODIFIED `apps/desktop/src/store/profile-select-source.test.ts`
- MODIFIED `apps/desktop/src/store/profile.ts`
- MODIFIED `apps/desktop/src/store/transcript-tail-cache.test.ts`
- MODIFIED `apps/desktop/src/store/transcript-tail-cache.ts`
- MODIFIED `cli-config.yaml.example`
- ADDED `contributors/emails/fred0m@users.noreply.github.com`
- ADDED `contributors/emails/paulapsp157@gmail.com`
- ADDED `contributors/emails/potatosaladx@gmail.com`
- ADDED `contributors/emails/veeman961@gmail.com`
- MODIFIED `gateway/relay/adapter.py`
- MODIFIED `gateway/relay/media.py`
- MODIFIED `gateway/relay/ws_transport.py`
- MODIFIED `gateway/run.py`
- MODIFIED `nastech_cli/approval_mode.py`
- MODIFIED `nastech_cli/backup.py`
- MODIFIED `nastech_cli/browser_connect.py`
- MODIFIED `nastech_cli/config.py`
- MODIFIED `nastech_cli/config_defaults.py`
- MODIFIED `nastech_cli/console_engine.py`
- MODIFIED `nastech_cli/main.py`
- MODIFIED `nastech_cli/process_identity.py`
- MODIFIED `nastech_cli/update_cmd.py`
- MODIFIED `nastech_cli/web_routers/profiles.py`
- MODIFIED `nastech_cli/web_routers/tools.py`
- MODIFIED `nastech_cli/web_server.py`
- MODIFIED `plugins/platforms/slack/adapter.py`
- MODIFIED `scripts/desktop-update/posix.sh`
- MODIFIED `scripts/desktop-update/windows.ps1`
- ADDED `tests/agent/test_compaction_ops_notification_anchor.py`
- MODIFIED `tests/agent/test_compression_concurrent_fork.py`
- MODIFIED `tests/gateway/relay/test_relay_media.py`
- ADDED `tests/gateway/relay/test_relay_slack_unfurl.py`
- ADDED `tests/gateway/relay/test_wire_voice_media.py`
- MODIFIED `tests/gateway/test_compression_progress_notices.py`
- MODIFIED `tests/gateway/test_slack.py`
- MODIFIED `tests/gateway/test_slack_block_kit_adapter.py`
- MODIFIED `tests/gateway/test_slack_native_streaming.py`
- MODIFIED `tests/gateway/test_slack_sdk_response.py`
- ADDED `tests/nastech_cli/test_browser_connect_default_chromium.py`
- MODIFIED `tests/nastech_cli/test_config.py`
- MODIFIED `tests/nastech_cli/test_config_set_coercion.py`
- MODIFIED `tests/nastech_cli/test_console_engine.py`
- ADDED `tests/nastech_cli/test_mcp_helper_ledger.py`
- MODIFIED `tests/nastech_cli/test_set_config_value.py`
- ADDED `tests/nastech_cli/test_update_config_migration_on_current.py`
- ADDED `tests/nastech_cli/test_update_config_migration_on_current_checkout.py`
- MODIFIED `tests/nastech_cli/test_update_fleet_check_fail_closed.py`
- ADDED `tests/nastech_cli/test_update_fleet_probe_resume_token.py`
- ADDED `tests/nastech_cli/test_update_fleet_restart_pending.py`
- ADDED `tests/nastech_cli/test_web_server_executor_isolation.py`
- ADDED `tests/nastech_state/test_named_profile_session_db.py`
- MODIFIED `tests/run_agent/test_413_compression.py`
- MODIFIED `tests/run_agent/test_codex_app_server_compaction.py`
- MODIFIED `tests/test_desktop_update_windows_pipe_drain.py`
- MODIFIED `tests/test_desktop_update_windows_python_handoff.py`
- MODIFIED `tests/tools/test_browser_extension_router_wiring.py`
- MODIFIED `tests/tools/test_browser_open_timeout.py`
- ADDED `tests/tools/test_browser_real_profile.py`
- MODIFIED `tests/tools/test_code_execution.py`
- MODIFIED `tests/tools/test_computer_use.py`
- DELETED `tests/tools/test_computer_use_browser_authorization.py`
- DELETED `tests/tools/test_computer_use_browser_contract_020.py`
- MODIFIED `tests/tools/test_computer_use_cua_0_10_permissions.py`
- MODIFIED `tests/tools/test_computer_use_cua_0_9.py`
- ADDED `tests/tools/test_mcp_stdio_children_dead.py`
- MODIFIED `tests/tools/test_notify_on_complete.py`
- MODIFIED `tests/tools/test_watch_patterns.py`
- ADDED `tests/tui_gateway/test_compression_config_hot_reload.py`
- ADDED `tests/tui_gateway/test_profiles_configure_model_guard.py`
- MODIFIED `tools/browser_tool.py`
- MODIFIED `tools/browser_use_cli.py`
- MODIFIED `tools/code_execution_tool.py`
- MODIFIED `tools/computer_use/backend.py`
- DELETED `tools/computer_use/browser_route.py`
- MODIFIED `tools/computer_use/cua_backend.py`
- MODIFIED `tools/computer_use/schema.py`
- MODIFIED `tools/computer_use/tool.py`
- MODIFIED `tools/environments/base.py`
- MODIFIED `tools/mcp_tool.py`
- MODIFIED `tools/process_registry.py`
- MODIFIED `tools/terminal_tool.py`
- MODIFIED `tui_gateway/methods_profiles.py`
- MODIFIED `tui_gateway/server.py`
- MODIFIED `website/docs/user-guide/features/browser.md`
- MODIFIED `website/docs/user-guide/messaging/slack.md`

## Scan

10516 files scanned [audio=5, binary=7, doc=5, font=13, image=92, text=10394]


## Diff

1370 renamed, 0 rewritten, 8747 identical, 61 locked, 0 missing, 34 owned, 250 reconciled


## Fork check (vs nastech-agent)

- 10235 identical, 251 updated (+0/-0 lines), 30 added, 0 missing, 0 fork-local-unpreserved, 0 stale-upstream, 0 locked/binary, 0 collision-safe relocated, 54 preserved fork-local files, 0 violations

- features: fork 51 -> branded 51

Auto-generated by 100Ways.
