# Nastech Update Report #1

- upstream sha : `0dfba37b11ff2ca908ae2df85b55f4f4c9b7fd8b`
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

- total files : 10512
- renamed     : 1464 (folders and file names)
- text-rewritten : 10414
- locked-copied  : 56
- binary-copied  : 8
- owned assets   : 34 (our logo/banner/mascot override upstream)

## Reconcile

- fixed : 257 files reconciled: .github/workflows/deploy-site.yml, .github/workflows/deploy-site.yml, .github/workflows/skills-index-freshness.yml, .mailmap, CONTRIBUTING.es.md, CONTRIBUTING.md, Dockerfile, README.es.md, README.md, README.ur-pk.md, README.zh-CN.md, SECURITY.es.md, SECURITY.md, agent/agent_runtime_helpers.py, agent/anthropic_adapter.py, agent/auxiliary_client.py, agent/billing_links.py, agent/billing_view.py, agent/chat_completion_helpers.py, agent/conversation_loop.py, agent/credits_tracker.py, agent/model_metadata.py, agent/prompt_builder.py, agent/proxy_sources/iron_proxy.py, agent/subscription_view.py, agent/usage_pricing.py, apps/bootstrap-installer/src-tauri/Cargo.toml, apps/desktop/README.md, apps/desktop/electron/backend-health.test.ts, apps/desktop/electron/backend-health.ts, apps/desktop/electron/connection-config.test.ts, apps/desktop/electron/main.ts, apps/desktop/electron/oauth-partition.test.ts, apps/desktop/electron/remote-lifecycle.ts, apps/desktop/package.json, apps/desktop/src/app/messaging/index.test.tsx, apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx, apps/desktop/src/app/settings/about-settings.tsx, apps/desktop/src/app/settings/billing/api.test.ts, apps/desktop/src/app/settings/billing/dev-fixtures.ts, apps/desktop/src/app/settings/billing/errors.test.ts, apps/desktop/src/app/settings/billing/types.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.ts, apps/desktop/src/app/settings/billing/use-charge-poller.test.ts, apps/desktop/src/app/settings/billing/use-step-up.test.tsx, apps/desktop/src/app/settings/constants.ts, apps/desktop/src/app/settings/gateway-settings.tsx, apps/desktop/src/app/settings/toolset-config-panel.test.tsx, apps/desktop/src/app/skills/embedded-hub-picker.tsx, apps/desktop/src/app/skills/index.test.tsx, apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts, apps/desktop/src/components/boot-failure-overlay.test.tsx, apps/desktop/src/components/boot-failure-overlay.tsx, apps/desktop/src/components/send-diagnostics-dialog.tsx, apps/desktop/src/contrib/plugin.ts, apps/desktop/src/i18n/en.ts, apps/desktop/src/i18n/ja.ts, apps/desktop/src/i18n/zh-hant.ts, apps/desktop/src/i18n/zh.ts, apps/desktop/src/plugins/nastech-bots/plugin.js, apps/desktop/src/sdk/index.ts, cli-config.yaml.example, eslint.config.shared.mjs, evals/browser_use/single_run.py, nastech_cli/auth.py, nastech_cli/banner.py, nastech_cli/config_defaults.py, nastech_cli/dashboard_auth/login_page.py, nastech_cli/dashboard_register.py, nastech_cli/debug.py, nastech_cli/diagnostics_upload.py, nastech_cli/fallback_cmd.py, nastech_cli/kanban.py, nastech_cli/main.py, nastech_cli/model_catalog.py, nastech_cli/model_switch.py, nastech_cli/models.py, nastech_cli/nastech_account.py, nastech_cli/nastech_billing.py, nastech_cli/plugins_cmd.py, nastech_cli/portal_cli.py, nastech_cli/providers.py, nastech_cli/proxy/__init__.py, nastech_cli/proxy/adapters/base.py, nastech_cli/proxy/adapters/nastech_portal.py, nastech_cli/setup.py, nastech_cli/setup_whatsapp_cloud.py, nastech_cli/skin_engine.py, nastech_cli/telegram_managed_bot.py, nastech_cli/tools_config.py, nastech_cli/uninstall.py, nastech_cli/update_cmd.py, nastech_cli/web_server.py, nastech_constants.py, package-lock.json, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/plugin.yaml, plugins/kanban/dashboard/dist/index.js, plugins/kanban/systemd/nastech-kanban-dispatcher.service, plugins/model-providers/ai-gateway/__init__.py, plugins/model-providers/fireworks/__init__.py, plugins/model-providers/kimi-coding/__init__.py, plugins/model-providers/nastech/__init__.py, plugins/model-providers/opencode-free/__init__.py, plugins/model-providers/opencode-zen/__init__.py, plugins/nastech-achievements/dashboard/dist/index.js, plugins/platforms/discord/adapter.py, plugins/platforms/email/adapter.py, plugins/platforms/photon/sidecar/package-lock.json, plugins/platforms/slack/adapter.py, run_agent.py, scripts/build_model_catalog.py, scripts/contributor_audit.py, scripts/dev-sandbox.sh, scripts/install.cmd, scripts/install.ps1, scripts/install.sh, scripts/release.py, scripts/whatsapp-bridge/package-lock.json, setup.py, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/references/background-systems.md, skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md, skills/autonomous-ai-agents/nastech-agent/references/configuration.md, skills/autonomous-ai-agents/nastech-agent/references/contributor-guide.md, skills/autonomous-ai-agents/nastech-agent/references/portal-auth-for-third-party-apps.md, skills/autonomous-ai-agents/nastech-agent/references/providers-and-models.md, skills/autonomous-ai-agents/nastech-agent/references/webhooks.md, tests/agent/test_anthropic_adapter.py, tests/agent/test_auxiliary_client.py, tests/agent/test_auxiliary_main_first.py, tests/agent/test_auxiliary_transport_autodetect.py, tests/agent/test_billing_links.py, tests/agent/test_credential_pool.py, tests/agent/test_credits_policy.py, tests/agent/test_error_classifier.py, tests/agent/test_model_metadata.py, tests/agent/test_nastech_credits_gauge.py, tests/agent/test_nastech_oauth_401_guidance.py, tests/agent/test_nastech_portal_anthropic_wire.py, tests/agent/test_phantom_tool_references.py, tests/agent/transports/test_chat_completions.py, tests/cli/test_cli_first_run_setup.py, tests/cli/test_cli_provider_resolution.py, tests/cli/test_show_config_credential.py, tests/docker/test_sqlite_runtime.py, tests/gateway/test_discord_format.py, tests/gateway/test_run_progress_topics.py, tests/gateway/test_status_command.py, tests/gateway/test_usage_command.py, tests/nastech_cli/test_auth_nastech_provider.py, tests/nastech_cli/test_base_url_host_identity.py, tests/nastech_cli/test_dashboard_auth_gate.py, tests/nastech_cli/test_dashboard_register.py, tests/nastech_cli/test_fireworks_provider.py, tests/nastech_cli/test_gateway_restart_loop.py, tests/nastech_cli/test_model_catalog.py, tests/nastech_cli/test_nastech_auth_keepalive.py, tests/nastech_cli/test_nastech_auth_status_cache.py, tests/nastech_cli/test_nastech_inference_url_validation.py, tests/nastech_cli/test_nastech_portal_staging_allowlist.py, tests/nastech_cli/test_nastech_reasoning_metadata.py, tests/nastech_cli/test_proxy.py, tests/nastech_cli/test_reasoning_caps_disk_cache.py, tests/nastech_cli/test_sale_pricing.py, tests/nastech_cli/test_web_oauth_dispatch.py, tests/plugins/dashboard_auth/test_nastech_provider.py, tests/plugins/image_gen/check_parity_vs_main.py, tests/plugins/image_gen/test_openrouter_compat_provider.py, tests/plugins/test_chronos_verify.py, tests/run_agent/test_anthropic_prompt_cache_policy.py, tests/run_agent/test_primary_runtime_restore.py, tests/run_agent/test_provider_attribution_headers.py, tests/run_agent/test_provider_fallback.py, tests/run_agent/test_provider_parity.py, tests/run_agent/test_run_agent.py, tests/run_agent/test_switch_model_reapplies_headers.py, tests/test_install_ps1_uv_powershell_host.py, tests/tools/test_delegate.py, tests/tools/test_managed_media_gateways.py, tests/tools/test_managed_tool_gateway.py, tests/tools/test_strict_provider_selection.py, tests/tools/test_tts_openai_config.py, tests/tools/test_url_safety.py, tests/tools/test_web_tools_config.py, tools/managed_tool_gateway.py, tools/mcp_oauth.py, tools/skills_hub.py, tools/skills_sync_client.py, trajectory_compressor.py, ui-tui/scripts/billing-fixtures.tsx, ui-tui/src/__tests__/subscriptionCommand.test.ts, ui-tui/src/__tests__/subscriptionOverlay.test.tsx, ui-tui/src/app/slash/commands/subscription.ts, ui-tui/src/domain/paths.ts, uv.lock, web/src/components/SidebarFooter.tsx, web/src/pages/DocsPage.tsx, web/src/pages/SystemPage.tsx, website/docs/developer-guide/contributing.md, website/docs/developer-guide/egress-internals.md, website/docs/getting-started/installation.md, website/docs/getting-started/platform-support.md, website/docs/getting-started/quickstart.md, website/docs/getting-started/termux.md, website/docs/guides/manage-nastech-cloud-with-mcp.md, website/docs/guides/run-nastech-with-nastech-portal.md, website/docs/guides/run-nemotron-3-ultra-free.md, website/docs/index.mdx, website/docs/integrations/nastech-portal.md, website/docs/integrations/providers.md, website/docs/reference/cli-commands.md, website/docs/reference/environment-variables.md, website/docs/reference/faq.md, website/docs/reference/model-catalog.md, website/docs/user-guide/desktop.md, website/docs/user-guide/egress/iron-proxy.md, website/docs/user-guide/features/browser.md, website/docs/user-guide/features/image-generation.md, website/docs/user-guide/features/skills.md, website/docs/user-guide/features/subscription-proxy.md, website/docs/user-guide/features/tool-gateway.md, website/docs/user-guide/features/tools.md, website/docs/user-guide/features/tts.md, website/docs/user-guide/features/web-dashboard.md, website/docs/user-guide/features/web-search.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/windows-wsl-quickstart.md, website/docusaurus.config.ts, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/contributing.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/quickstart.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-nastech-with-nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/index.mdx, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/providers.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/faq.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/model-catalog.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/subscription-proxy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tools.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tts.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-native.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-wsl-quickstart.md, website/scripts/generate-llms-txt.py, website/scripts/prebuild.mjs, website/static/api/model-catalog.json, website/static/oauth/client-metadata.json


## Direct upstream tree delta

- complete: +24 ~106 -0 ↪0
- MODIFIED `agent/gemini_native_adapter.py`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/index.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/submit.ts`
- MODIFIED `apps/desktop/src/components/boot-failure-overlay.test.tsx`
- MODIFIED `apps/desktop/src/components/boot-failure-overlay.tsx`
- MODIFIED `apps/desktop/src/lib/voice-client-direct.test.ts`
- MODIFIED `apps/desktop/src/lib/voice-client-direct.ts`
- MODIFIED `cli-config.yaml.example`
- MODIFIED `contributors/emails/Finn763@users.noreply.github.com`
- ADDED `contributors/emails/hjharris1@gmail.com`
- ADDED `contributors/emails/joby@ellingtonlife.com`
- ADDED `contributors/emails/lawrenncecharlotte@gmail.com`
- ADDED `contributors/emails/rodrigo.smscom@gmail.com`
- ADDED `contributors/emails/wansui@bilibili.com`
- MODIFIED `cron/jobs.py`
- MODIFIED `cron/scheduler.py`
- MODIFIED `gateway/display_config.py`
- MODIFIED `gateway/platforms/api_server.py`
- MODIFIED `gateway/platforms/base.py`
- MODIFIED `gateway/platforms/bluebubbles.py`
- MODIFIED `gateway/platforms/msgraph_webhook.py`
- MODIFIED `gateway/platforms/qqbot/adapter.py`
- MODIFIED `gateway/platforms/signal.py`
- MODIFIED `gateway/platforms/webhook.py`
- MODIFIED `gateway/platforms/weixin.py`
- MODIFIED `gateway/platforms/whatsapp_cloud.py`
- MODIFIED `gateway/platforms/yuanbao.py`
- MODIFIED `gateway/restart.py`
- MODIFIED `gateway/run.py`
- MODIFIED `gateway/session.py`
- MODIFIED `gateway/shutdown_forensics.py`
- MODIFIED `gateway/shutdown_watchdog.py`
- MODIFIED `gateway/slash_commands.py`
- MODIFIED `gateway/stream_consumer.py`
- MODIFIED `nastech_cli/active_sessions.py`
- MODIFIED `nastech_cli/config.py`
- MODIFIED `nastech_cli/config_defaults.py`
- MODIFIED `nastech_cli/gateway.py`
- MODIFIED `nastech_cli/inventory.py`
- MODIFIED `nastech_cli/kanban_db.py`
- MODIFIED `nastech_cli/model_switch.py`
- MODIFIED `nastech_cli/plugins.py`
- MODIFIED `nastech_cli/update_cmd.py`
- MODIFIED `nastech_cli/web_routers/sessions.py`
- MODIFIED `nastech_cli/web_server.py`
- MODIFIED `nastech_state.py`
- MODIFIED `nastech_state_common.py`
- MODIFIED `model_tools.py`
- ADDED `optional-skills/web-development/publish-site/SKILL.md`
- MODIFIED `plugins/platforms/a2a/adapter.py`
- MODIFIED `plugins/platforms/buzz/adapter.py`
- MODIFIED `plugins/platforms/dingtalk/adapter.py`
- MODIFIED `plugins/platforms/discord/adapter.py`
- MODIFIED `plugins/platforms/email/adapter.py`
- MODIFIED `plugins/platforms/feishu/adapter.py`
- MODIFIED `plugins/platforms/google_chat/adapter.py`
- MODIFIED `plugins/platforms/homeassistant/adapter.py`
- MODIFIED `plugins/platforms/irc/adapter.py`
- MODIFIED `plugins/platforms/line/adapter.py`
- MODIFIED `plugins/platforms/matrix/adapter.py`
- MODIFIED `plugins/platforms/mattermost/adapter.py`
- MODIFIED `plugins/platforms/ntfy/adapter.py`
- MODIFIED `plugins/platforms/photon/adapter.py`
- MODIFIED `plugins/platforms/raft/adapter.py`
- MODIFIED `plugins/platforms/simplex/adapter.py`
- MODIFIED `plugins/platforms/slack/adapter.py`
- MODIFIED `plugins/platforms/sms/adapter.py`
- MODIFIED `plugins/platforms/teams/adapter.py`
- MODIFIED `plugins/platforms/telegram/adapter.py`
- MODIFIED `plugins/platforms/wecom/adapter.py`
- MODIFIED `plugins/platforms/whatsapp/adapter.py`
- MODIFIED `pyproject.toml`
- MODIFIED `tests/agent/test_gemini_native_adapter.py`
- MODIFIED `tests/cron/test_due_stale_cron_edit.py`
- ADDED `tests/cron/test_scheduler_completion_verification.py`
- MODIFIED `tests/cron/test_sessiondb_init_hang.py`
- ADDED `tests/gateway/test_approval_boundary.py`
- MODIFIED `tests/gateway/test_cron_drain_floor.py`
- MODIFIED `tests/gateway/test_display_config.py`
- MODIFIED `tests/gateway/test_loop_liveness_watchdog.py`
- MODIFIED `tests/gateway/test_per_platform_streaming_defaults.py`
- MODIFIED `tests/gateway/test_platform_base.py`
- ADDED `tests/gateway/test_platform_plugin_handlers.py`
- MODIFIED `tests/gateway/test_session_store_stale_prune.py`
- ADDED `tests/gateway/test_stream_consumer_tool_progress.py`
- ADDED `tests/gateway/test_stream_consumer_wecom_native.py`
- MODIFIED `tests/gateway/test_wecom.py`
- ADDED `tests/gateway/test_wecom_double_send.py`
- ADDED `tests/gateway/test_wecom_per_turn.py`
- ADDED `tests/gateway/test_wecom_stream_dup_fix.py`
- MODIFIED `tests/nastech_cli/test_active_sessions.py`
- MODIFIED `tests/nastech_cli/test_dashboard_auth_gate.py`
- MODIFIED `tests/nastech_cli/test_gateway_service.py`
- MODIFIED `tests/nastech_cli/test_inventory.py`
- MODIFIED `tests/nastech_cli/test_kanban_db.py`
- MODIFIED `tests/nastech_cli/test_model_switch_custom_providers.py`
- MODIFIED `tests/nastech_cli/test_provider_config_validation.py`
- MODIFIED `tests/nastech_cli/test_update_wedged_gateway.py`
- MODIFIED `tests/nastech_cli/test_update_zip_fallback_guards.py`
- MODIFIED `tests/nastech_cli/test_web_server.py`
- ADDED `tests/nastech_state/test_94895_orphan_sweep_cross_backend.py`
- ADDED `tests/nastech_state/test_empty_sweep_archived_transcript_95868.py`
- ADDED `tests/skills/test_publish_site_skill.py`
- MODIFIED `tests/test_journal_mode_config.py`
- ADDED `tests/test_journal_mode_upgrade_warning.py`
- ADDED `tests/test_state_synchronastech_pragma.py`
- MODIFIED `tests/test_tui_gateway_server.py`
- MODIFIED `tests/tools/test_delegate.py`
- MODIFIED `tests/tools/test_delegate_batch_validation.py`
- MODIFIED `tests/tools/test_delegate_control_actions.py`
- MODIFIED `tests/tools/test_delegate_output_schema.py`
- ADDED `tests/tools/test_mcp_stdio_fastfail_reconnect.py`
- ADDED `tests/tools/test_send_message_cross_loop.py`
- ADDED `tests/tui_gateway/test_94895_backend_heartbeat.py`
- ADDED `tests/tui_gateway/test_cross_process_orphan_ownership.py`
- MODIFIED `tools/delegate_tool.py`
- MODIFIED `tools/mcp_tool.py`
- MODIFIED `tools/send_message_tool.py`
- MODIFIED `tui_gateway/entry.py`
- MODIFIED `tui_gateway/server.py`
- MODIFIED `tui_gateway/ws.py`
- MODIFIED `uv.lock`
- MODIFIED `website/docs/developer-guide/plugins/index.md`
- MODIFIED `website/docs/reference/optional-skills-catalog.md`
- MODIFIED `website/docs/user-guide/configuration.md`
- MODIFIED `website/docs/user-guide/docker.md`
- MODIFIED `website/docs/user-guide/features/web-dashboard.md`
- MODIFIED `website/docs/user-guide/messaging/wecom.md`
- ADDED `website/docs/user-guide/skills/optional/web-development/web-development-publish-site.md`
- MODIFIED `website/sidebars.ts`

## Scan

10566 files scanned [audio=5, binary=7, doc=5, font=13, image=92, text=10444]


## Diff

1377 renamed, 0 rewritten, 8789 identical, 61 locked, 0 missing, 34 owned, 251 reconciled


## Fork check (vs nastech-agent)

- 10283 identical, 258 updated (+0/-0 lines), 24 added, 0 missing, 0 fork-local-unpreserved, 0 stale-upstream, 1 locked/binary, 0 collision-safe relocated, 54 preserved fork-local files, 0 violations

- features: fork 51 -> branded 51

Auto-generated by 100Ways.
