# Nastech Update Report #1

- upstream sha : `fcbd1076a93841fa88855acce810e342a5b78101`
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

- total files : 9976
- renamed     : 1375 (folders and file names)
- text-rewritten : 9876
- locked-copied  : 57
- binary-copied  : 9
- owned assets   : 34 (our logo/banner/mascot override upstream)

## Reconcile

- fixed : 245 files reconciled: .github/workflows/deploy-site.yml, .github/workflows/skills-index-freshness.yml, .mailmap, CONTRIBUTING.es.md, CONTRIBUTING.md, Dockerfile, README.es.md, README.md, README.ur-pk.md, README.zh-CN.md, SECURITY.es.md, SECURITY.md, agent/agent_runtime_helpers.py, agent/anthropic_adapter.py, agent/auxiliary_client.py, agent/billing_links.py, agent/billing_view.py, agent/chat_completion_helpers.py, agent/conversation_loop.py, agent/credits_tracker.py, agent/model_metadata.py, agent/prompt_builder.py, agent/proxy_sources/iron_proxy.py, agent/subscription_view.py, agent/usage_pricing.py, apps/bootstrap-installer/src-tauri/Cargo.toml, apps/desktop/README.md, apps/desktop/electron/connection-config.test.ts, apps/desktop/electron/main.ts, apps/desktop/electron/remote-lifecycle.ts, apps/desktop/package.json, apps/desktop/src/app/messaging/index.test.tsx, apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx, apps/desktop/src/app/settings/about-settings.tsx, apps/desktop/src/app/settings/billing/api.test.ts, apps/desktop/src/app/settings/billing/dev-fixtures.ts, apps/desktop/src/app/settings/billing/errors.test.ts, apps/desktop/src/app/settings/billing/types.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.ts, apps/desktop/src/app/settings/billing/use-charge-poller.test.ts, apps/desktop/src/app/settings/billing/use-step-up.test.tsx, apps/desktop/src/app/settings/constants.ts, apps/desktop/src/app/settings/gateway-settings.tsx, apps/desktop/src/app/settings/toolset-config-panel.test.tsx, apps/desktop/src/app/skills/embedded-hub-picker.tsx, apps/desktop/src/app/skills/index.test.tsx, apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts, apps/desktop/src/contrib/plugin.ts, apps/desktop/src/i18n/en.ts, apps/desktop/src/i18n/ja.ts, apps/desktop/src/i18n/zh-hant.ts, apps/desktop/src/i18n/zh.ts, apps/desktop/src/plugins/nastech-bots/plugin.js, apps/desktop/src/sdk/index.ts, cli-config.yaml.example, eslint.config.shared.mjs, nastech_cli/auth.py, nastech_cli/banner.py, nastech_cli/config_defaults.py, nastech_cli/dashboard_register.py, nastech_cli/diagnostics_upload.py, nastech_cli/fallback_cmd.py, nastech_cli/kanban.py, nastech_cli/main.py, nastech_cli/model_catalog.py, nastech_cli/model_switch.py, nastech_cli/models.py, nastech_cli/nastech_account.py, nastech_cli/nastech_billing.py, nastech_cli/plugins_cmd.py, nastech_cli/portal_cli.py, nastech_cli/providers.py, nastech_cli/proxy/__init__.py, nastech_cli/proxy/adapters/base.py, nastech_cli/proxy/adapters/nastech_portal.py, nastech_cli/setup.py, nastech_cli/setup_whatsapp_cloud.py, nastech_cli/skin_engine.py, nastech_cli/telegram_managed_bot.py, nastech_cli/tools_config.py, nastech_cli/uninstall.py, nastech_cli/update_cmd.py, nastech_cli/web_server.py, nastech_constants.py, package-lock.json, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/plugin.yaml, plugins/kanban/dashboard/dist/index.js, plugins/kanban/systemd/nastech-kanban-dispatcher.service, plugins/model-providers/ai-gateway/__init__.py, plugins/model-providers/fireworks/__init__.py, plugins/model-providers/kimi-coding/__init__.py, plugins/model-providers/nastech/__init__.py, plugins/model-providers/opencode-free/__init__.py, plugins/model-providers/opencode-zen/__init__.py, plugins/nastech-achievements/dashboard/dist/index.js, plugins/platforms/discord/adapter.py, plugins/platforms/email/adapter.py, plugins/platforms/photon/sidecar/package-lock.json, plugins/platforms/slack/adapter.py, run_agent.py, scripts/build_model_catalog.py, scripts/contributor_audit.py, scripts/dev-sandbox.sh, scripts/install.cmd, scripts/install.ps1, scripts/install.sh, scripts/release.py, scripts/whatsapp-bridge/package-lock.json, setup.py, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/references/background-systems.md, skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md, skills/autonomous-ai-agents/nastech-agent/references/configuration.md, skills/autonomous-ai-agents/nastech-agent/references/contributor-guide.md, skills/autonomous-ai-agents/nastech-agent/references/portal-auth-for-third-party-apps.md, skills/autonomous-ai-agents/nastech-agent/references/providers-and-models.md, skills/autonomous-ai-agents/nastech-agent/references/webhooks.md, tests/agent/test_anthropic_adapter.py, tests/agent/test_auxiliary_client.py, tests/agent/test_auxiliary_main_first.py, tests/agent/test_auxiliary_transport_autodetect.py, tests/agent/test_billing_links.py, tests/agent/test_credential_pool.py, tests/agent/test_credits_policy.py, tests/agent/test_error_classifier.py, tests/agent/test_model_metadata.py, tests/agent/test_nastech_credits_gauge.py, tests/agent/test_nastech_oauth_401_guidance.py, tests/agent/test_nastech_portal_anthropic_wire.py, tests/agent/transports/test_chat_completions.py, tests/cli/test_cli_first_run_setup.py, tests/cli/test_cli_provider_resolution.py, tests/cli/test_show_config_credential.py, tests/docker/test_sqlite_runtime.py, tests/gateway/test_discord_format.py, tests/gateway/test_run_progress_topics.py, tests/gateway/test_status_command.py, tests/gateway/test_usage_command.py, tests/nastech_cli/test_auth_nastech_provider.py, tests/nastech_cli/test_base_url_host_identity.py, tests/nastech_cli/test_dashboard_register.py, tests/nastech_cli/test_fireworks_provider.py, tests/nastech_cli/test_gateway_restart_loop.py, tests/nastech_cli/test_model_catalog.py, tests/nastech_cli/test_nastech_auth_keepalive.py, tests/nastech_cli/test_nastech_auth_status_cache.py, tests/nastech_cli/test_nastech_inference_url_validation.py, tests/nastech_cli/test_nastech_portal_staging_allowlist.py, tests/nastech_cli/test_nastech_reasoning_metadata.py, tests/nastech_cli/test_proxy.py, tests/nastech_cli/test_reasoning_caps_disk_cache.py, tests/nastech_cli/test_sale_pricing.py, tests/nastech_cli/test_web_oauth_dispatch.py, tests/plugins/dashboard_auth/test_nastech_provider.py, tests/plugins/image_gen/check_parity_vs_main.py, tests/plugins/image_gen/test_openrouter_compat_provider.py, tests/plugins/test_chronos_verify.py, tests/run_agent/test_anthropic_prompt_cache_policy.py, tests/run_agent/test_primary_runtime_restore.py, tests/run_agent/test_provider_attribution_headers.py, tests/run_agent/test_provider_fallback.py, tests/run_agent/test_provider_parity.py, tests/run_agent/test_run_agent.py, tests/run_agent/test_switch_model_reapplies_headers.py, tests/test_install_ps1_uv_powershell_host.py, tests/tools/test_delegate.py, tests/tools/test_managed_media_gateways.py, tests/tools/test_managed_tool_gateway.py, tests/tools/test_strict_provider_selection.py, tests/tools/test_tts_openai_config.py, tests/tools/test_url_safety.py, tests/tools/test_web_tools_config.py, tools/managed_tool_gateway.py, tools/mcp_oauth.py, tools/skills_hub.py, tools/skills_sync_client.py, trajectory_compressor.py, ui-tui/scripts/billing-fixtures.tsx, ui-tui/src/__tests__/subscriptionCommand.test.ts, ui-tui/src/__tests__/subscriptionOverlay.test.tsx, ui-tui/src/app/slash/commands/subscription.ts, ui-tui/src/domain/paths.ts, uv.lock, web/src/components/SidebarFooter.tsx, web/src/pages/DocsPage.tsx, web/src/pages/SystemPage.tsx, website/docs/developer-guide/contributing.md, website/docs/developer-guide/egress-internals.md, website/docs/getting-started/installation.md, website/docs/getting-started/platform-support.md, website/docs/getting-started/quickstart.md, website/docs/getting-started/termux.md, website/docs/guides/manage-nastech-cloud-with-mcp.md, website/docs/guides/run-nastech-with-nastech-portal.md, website/docs/guides/run-nemotron-3-ultra-free.md, website/docs/index.mdx, website/docs/integrations/nastech-portal.md, website/docs/integrations/providers.md, website/docs/reference/cli-commands.md, website/docs/reference/environment-variables.md, website/docs/reference/faq.md, website/docs/reference/model-catalog.md, website/docs/user-guide/desktop.md, website/docs/user-guide/egress/iron-proxy.md, website/docs/user-guide/features/browser.md, website/docs/user-guide/features/image-generation.md, website/docs/user-guide/features/skills.md, website/docs/user-guide/features/subscription-proxy.md, website/docs/user-guide/features/tool-gateway.md, website/docs/user-guide/features/tools.md, website/docs/user-guide/features/tts.md, website/docs/user-guide/features/web-dashboard.md, website/docs/user-guide/features/web-search.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/windows-wsl-quickstart.md, website/docusaurus.config.ts, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/contributing.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/quickstart.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-nastech-with-nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/index.mdx, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/providers.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/faq.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/model-catalog.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/subscription-proxy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tools.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tts.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-native.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-wsl-quickstart.md, website/scripts/generate-llms-txt.py, website/scripts/prebuild.mjs, website/static/api/model-catalog.json, website/static/oauth/client-metadata.json


## Direct upstream tree delta

- complete: +22 ~114 -0 ↪0
- MODIFIED `.env.example`
- MODIFIED `agent/agent_init.py`
- MODIFIED `agent/agent_runtime_helpers.py`
- MODIFIED `agent/auxiliary_client.py`
- MODIFIED `agent/background_review.py`
- MODIFIED `agent/codex_responses_adapter.py`
- MODIFIED `agent/conversation_loop.py`
- MODIFIED `agent/model_metadata.py`
- MODIFIED `agent/native_compaction.py`
- MODIFIED `agent/prompt_caching.py`
- MODIFIED `agent/reasoning_effort.py`
- MODIFIED `agent/reasoning_timeouts.py`
- ADDED `apps/desktop/e2e/glyph-spinner.spec.ts`
- MODIFIED `apps/desktop/electron/main.ts`
- MODIFIED `apps/desktop/electron/translucency.test.ts`
- MODIFIED `apps/desktop/electron/translucency.ts`
- ADDED `apps/desktop/electron/wsl-path-bridge-gate.test.ts`
- ADDED `apps/desktop/electron/wsl-path-bridge-profile.test.ts`
- MODIFIED `apps/desktop/electron/wsl-path-bridge.test.ts`
- MODIFIED `apps/desktop/electron/wsl-path-bridge.ts`
- MODIFIED `apps/desktop/scripts/run-short-session-hang-repro.mjs`
- ADDED `apps/desktop/src/app/chat/chat-swap-overlay.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/chat-swap-overlay.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/index.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/session-index.test.ts`
- MODIFIED `apps/desktop/src/app/chat/sidebar/session-index.ts`
- MODIFIED `apps/desktop/src/app/gateway/hooks/use-gateway-boot.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/index.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/rewind.test.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/rewind.ts`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/assistant-message.tsx`
- ADDED `apps/desktop/src/components/assistant-ui/thread/inter-agent-collapse.test.tsx`
- ADDED `apps/desktop/src/components/assistant-ui/thread/preview-embeds.test.tsx`
- ADDED `apps/desktop/src/components/assistant-ui/thread/status-invalidation-scope.test.tsx`
- ADDED `apps/desktop/src/components/ui/glyph-spinner.css`
- MODIFIED `apps/desktop/src/components/ui/glyph-spinner.test.tsx`
- MODIFIED `apps/desktop/src/components/ui/glyph-spinner.tsx`
- MODIFIED `apps/desktop/src/global.d.ts`
- MODIFIED `apps/desktop/src/lib/desktop-fs.test.ts`
- MODIFIED `apps/desktop/src/lib/desktop-fs.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/plugin.js`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/group-chat.test.mjs`
- MODIFIED `apps/desktop/src/store/gateway.ts`
- MODIFIED `apps/desktop/src/store/session-pin-sync.test.ts`
- MODIFIED `apps/desktop/src/store/session-pin-sync.ts`
- ADDED `apps/desktop/src/store/session-states-reconnect.test.ts`
- MODIFIED `apps/desktop/src/store/session-states.ts`
- MODIFIED `apps/desktop/src/styles.css`
- ADDED `contributors/emails/paultaki@gmail.com`
- ADDED `contributors/emails/qixuancao36@gmail.com`
- ADDED `contributors/emails/yiyangchaishu@gmail.com`
- MODIFIED `cron/scheduler.py`
- MODIFIED `nastech_cli/__init__.py`
- MODIFIED `nastech_cli/auth.py`
- MODIFIED `nastech_cli/gateway.py`
- MODIFIED `nastech_cli/inventory.py`
- MODIFIED `nastech_cli/main.py`
- MODIFIED `nastech_cli/model_setup_flows.py`
- MODIFIED `nastech_cli/model_switch.py`
- MODIFIED `nastech_cli/models.py`
- MODIFIED `nastech_cli/provider_catalog.py`
- MODIFIED `nastech_cli/providers.py`
- MODIFIED `nastech_cli/runtime_provider.py`
- MODIFIED `nastech_cli/setup.py`
- MODIFIED `nastech_cli/subcommands/update.py`
- MODIFIED `nastech_cli/update_cmd.py`
- ADDED `nastech_cli/update_inventory.py`
- MODIFIED `nastech_cli/update_receipt.py`
- ADDED `plugins/model-providers/opencode-free/__init__.py`
- ADDED `plugins/model-providers/opencode-free/plugin.yaml`
- MODIFIED `plugins/model-providers/opencode-zen/__init__.py`
- MODIFIED `plugins/teams_pipeline/meetings.py`
- MODIFIED `plugins/teams_pipeline/pipeline.py`
- MODIFIED `pyproject.toml`
- MODIFIED `run_agent.py`
- MODIFIED `scripts/desktop-update/windows.ps1`
- ADDED `tests/agent/test_opencode_free_provider.py`
- MODIFIED `tests/agent/test_prompt_caching.py`
- MODIFIED `tests/agent/test_skip_memory_store_65429.py`
- MODIFIED `tests/cron/test_agent_scheduling_gate.py`
- MODIFIED `tests/cron/test_scheduler.py`
- MODIFIED `tests/gateway/test_gateway_platform_event_hook.py`
- MODIFIED `tests/gateway/test_send_image_file.py`
- MODIFIED `tests/gateway/test_send_multiple_images.py`
- MODIFIED `tests/gateway/test_telegram_approval_buttons.py`
- MODIFIED `tests/gateway/test_telegram_clarify_buttons.py`
- MODIFIED `tests/gateway/test_telegram_closewait_limits_31599.py`
- MODIFIED `tests/gateway/test_telegram_conflict.py`
- MODIFIED `tests/gateway/test_telegram_connect.py`
- MODIFIED `tests/gateway/test_telegram_documents.py`
- MODIFIED `tests/gateway/test_telegram_format.py`
- MODIFIED `tests/gateway/test_telegram_init_deadline.py`
- MODIFIED `tests/gateway/test_telegram_max_doc_bytes.py`
- MODIFIED `tests/gateway/test_telegram_media_read_timeout.py`
- MODIFIED `tests/gateway/test_telegram_model_picker.py`
- MODIFIED `tests/gateway/test_telegram_network_reconnect.py`
- MODIFIED `tests/gateway/test_telegram_pending_update_probe.py`
- MODIFIED `tests/gateway/test_telegram_polling_health_confirmation.py`
- MODIFIED `tests/gateway/test_telegram_reply_mode.py`
- MODIFIED `tests/gateway/test_telegram_reply_quote.py`
- MODIFIED `tests/gateway/test_telegram_send_draft_format.py`
- MODIFIED `tests/gateway/test_telegram_send_path_health.py`
- MODIFIED `tests/gateway/test_telegram_slash_confirm.py`
- MODIFIED `tests/gateway/test_telegram_start_polling_timeout.py`
- MODIFIED `tests/gateway/test_telegram_status_indicator.py`
- MODIFIED `tests/gateway/test_telegram_typing_backoff.py`
- MODIFIED `tests/gateway/test_telegram_voice_caption_markdown.py`
- MODIFIED `tests/gateway/test_telegram_voice_duration.py`
- MODIFIED `tests/nastech_cli/test_gateway.py`
- MODIFIED `tests/nastech_cli/test_gateway_proc_fallback.py`
- ADDED `tests/nastech_cli/test_opencode_zen_free_keyless.py`
- MODIFIED `tests/nastech_cli/test_provider_catalog.py`
- MODIFIED `tests/nastech_cli/test_provider_parity.py`
- MODIFIED `tests/nastech_cli/test_runtime_provider_resolution.py`
- MODIFIED `tests/nastech_cli/test_tencent_tokenhub_provider.py`
- ADDED `tests/nastech_cli/test_update_inventory.py`
- ADDED `tests/nastech_cli/test_update_launchd_fleet_restart.py`
- MODIFIED `tests/nastech_cli/test_update_receipt.py`
- MODIFIED `tests/plugins/model_providers/test_opencode_go_profile.py`
- MODIFIED `tests/plugins/test_teams_pipeline_plugin.py`
- MODIFIED `tests/run_agent/test_background_review.py`
- ADDED `tests/run_agent/test_native_compaction_summary_retention.py`
- ADDED `tests/run_agent/test_opencode_free_client_headers.py`
- ADDED `tests/tui_gateway/test_session_profile_db.py`
- MODIFIED `tui_gateway/methods_prompt.py`
- MODIFIED `tui_gateway/methods_tools.py`
- MODIFIED `tui_gateway/server.py`
- MODIFIED `uv.lock`
- MODIFIED `website/docs/developer-guide/cron-internals.md`
- MODIFIED `website/docs/getting-started/updating.md`
- MODIFIED `website/docs/guides/automate-with-cron.md`
- MODIFIED `website/docs/integrations/providers.md`
- MODIFIED `website/docs/reference/cli-commands.md`
- MODIFIED `website/docs/user-guide/configuration.md`
- MODIFIED `website/docs/user-guide/features/fallback-providers.md`
- MODIFIED `website/static/api/model-catalog.json`

## Scan

10030 files scanned [archive=1, audio=5, binary=7, doc=5, font=13, image=93, text=9906]


## Diff

1291 renamed, 0 rewritten, 8348 identical, 63 locked, 0 missing, 34 owned, 240 reconciled


## Fork check (vs nastech-agent)

- 9748 identical, 259 updated (+0/-0 lines), 22 added, 0 missing, 0 fork-local-unpreserved, 0 stale-upstream, 1 locked/binary, 0 collision-safe relocated, 54 preserved fork-local files, 0 violations

- features: fork 51 -> branded 51

Auto-generated by 100Ways.
