# Nastech Update Report #1

- upstream sha : `40643cbaf9b767af146694131ffb8f8160f25e1c`
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

- total files : 9954
- renamed     : 1371 (folders and file names)
- text-rewritten : 9854
- locked-copied  : 57
- binary-copied  : 9
- owned assets   : 34 (our logo/banner/mascot override upstream)

## Reconcile

- fixed : 244 files reconciled: .github/workflows/deploy-site.yml, .github/workflows/skills-index-freshness.yml, .mailmap, CONTRIBUTING.es.md, CONTRIBUTING.md, Dockerfile, README.es.md, README.md, README.ur-pk.md, README.zh-CN.md, SECURITY.es.md, SECURITY.md, agent/agent_runtime_helpers.py, agent/anthropic_adapter.py, agent/auxiliary_client.py, agent/billing_links.py, agent/billing_view.py, agent/chat_completion_helpers.py, agent/conversation_loop.py, agent/credits_tracker.py, agent/model_metadata.py, agent/prompt_builder.py, agent/proxy_sources/iron_proxy.py, agent/subscription_view.py, agent/usage_pricing.py, apps/bootstrap-installer/src-tauri/Cargo.toml, apps/desktop/README.md, apps/desktop/electron/connection-config.test.ts, apps/desktop/electron/main.ts, apps/desktop/electron/remote-lifecycle.ts, apps/desktop/package.json, apps/desktop/src/app/messaging/index.test.tsx, apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx, apps/desktop/src/app/settings/about-settings.tsx, apps/desktop/src/app/settings/billing/api.test.ts, apps/desktop/src/app/settings/billing/dev-fixtures.ts, apps/desktop/src/app/settings/billing/errors.test.ts, apps/desktop/src/app/settings/billing/types.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.ts, apps/desktop/src/app/settings/billing/use-charge-poller.test.ts, apps/desktop/src/app/settings/billing/use-step-up.test.tsx, apps/desktop/src/app/settings/constants.ts, apps/desktop/src/app/settings/gateway-settings.tsx, apps/desktop/src/app/settings/toolset-config-panel.test.tsx, apps/desktop/src/app/skills/embedded-hub-picker.tsx, apps/desktop/src/app/skills/index.test.tsx, apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts, apps/desktop/src/contrib/plugin.ts, apps/desktop/src/i18n/en.ts, apps/desktop/src/i18n/ja.ts, apps/desktop/src/i18n/zh-hant.ts, apps/desktop/src/i18n/zh.ts, apps/desktop/src/plugins/nastech-bots/plugin.js, apps/desktop/src/sdk/index.ts, cli-config.yaml.example, eslint.config.shared.mjs, nastech_cli/auth.py, nastech_cli/banner.py, nastech_cli/config_defaults.py, nastech_cli/dashboard_register.py, nastech_cli/diagnostics_upload.py, nastech_cli/fallback_cmd.py, nastech_cli/kanban.py, nastech_cli/main.py, nastech_cli/model_catalog.py, nastech_cli/model_switch.py, nastech_cli/models.py, nastech_cli/nastech_account.py, nastech_cli/nastech_billing.py, nastech_cli/plugins_cmd.py, nastech_cli/portal_cli.py, nastech_cli/providers.py, nastech_cli/proxy/__init__.py, nastech_cli/proxy/adapters/base.py, nastech_cli/proxy/adapters/nastech_portal.py, nastech_cli/setup.py, nastech_cli/setup_whatsapp_cloud.py, nastech_cli/skin_engine.py, nastech_cli/telegram_managed_bot.py, nastech_cli/tools_config.py, nastech_cli/uninstall.py, nastech_cli/update_cmd.py, nastech_cli/web_server.py, nastech_constants.py, package-lock.json, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/plugin.yaml, plugins/kanban/dashboard/dist/index.js, plugins/kanban/systemd/nastech-kanban-dispatcher.service, plugins/model-providers/ai-gateway/__init__.py, plugins/model-providers/fireworks/__init__.py, plugins/model-providers/kimi-coding/__init__.py, plugins/model-providers/nastech/__init__.py, plugins/model-providers/opencode-zen/__init__.py, plugins/nastech-achievements/dashboard/dist/index.js, plugins/platforms/discord/adapter.py, plugins/platforms/email/adapter.py, plugins/platforms/photon/sidecar/package-lock.json, plugins/platforms/slack/adapter.py, run_agent.py, scripts/build_model_catalog.py, scripts/contributor_audit.py, scripts/dev-sandbox.sh, scripts/install.cmd, scripts/install.ps1, scripts/install.sh, scripts/release.py, scripts/whatsapp-bridge/package-lock.json, setup.py, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/references/background-systems.md, skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md, skills/autonomous-ai-agents/nastech-agent/references/configuration.md, skills/autonomous-ai-agents/nastech-agent/references/contributor-guide.md, skills/autonomous-ai-agents/nastech-agent/references/portal-auth-for-third-party-apps.md, skills/autonomous-ai-agents/nastech-agent/references/providers-and-models.md, skills/autonomous-ai-agents/nastech-agent/references/webhooks.md, tests/agent/test_anthropic_adapter.py, tests/agent/test_auxiliary_client.py, tests/agent/test_auxiliary_main_first.py, tests/agent/test_auxiliary_transport_autodetect.py, tests/agent/test_billing_links.py, tests/agent/test_credential_pool.py, tests/agent/test_credits_policy.py, tests/agent/test_error_classifier.py, tests/agent/test_model_metadata.py, tests/agent/test_nastech_credits_gauge.py, tests/agent/test_nastech_oauth_401_guidance.py, tests/agent/test_nastech_portal_anthropic_wire.py, tests/agent/transports/test_chat_completions.py, tests/cli/test_cli_first_run_setup.py, tests/cli/test_cli_provider_resolution.py, tests/cli/test_show_config_credential.py, tests/docker/test_sqlite_runtime.py, tests/gateway/test_discord_format.py, tests/gateway/test_run_progress_topics.py, tests/gateway/test_status_command.py, tests/gateway/test_usage_command.py, tests/nastech_cli/test_auth_nastech_provider.py, tests/nastech_cli/test_base_url_host_identity.py, tests/nastech_cli/test_dashboard_register.py, tests/nastech_cli/test_fireworks_provider.py, tests/nastech_cli/test_gateway_restart_loop.py, tests/nastech_cli/test_model_catalog.py, tests/nastech_cli/test_nastech_auth_keepalive.py, tests/nastech_cli/test_nastech_auth_status_cache.py, tests/nastech_cli/test_nastech_inference_url_validation.py, tests/nastech_cli/test_nastech_portal_staging_allowlist.py, tests/nastech_cli/test_nastech_reasoning_metadata.py, tests/nastech_cli/test_proxy.py, tests/nastech_cli/test_reasoning_caps_disk_cache.py, tests/nastech_cli/test_sale_pricing.py, tests/nastech_cli/test_web_oauth_dispatch.py, tests/plugins/dashboard_auth/test_nastech_provider.py, tests/plugins/image_gen/check_parity_vs_main.py, tests/plugins/image_gen/test_openrouter_compat_provider.py, tests/plugins/test_chronos_verify.py, tests/run_agent/test_anthropic_prompt_cache_policy.py, tests/run_agent/test_primary_runtime_restore.py, tests/run_agent/test_provider_attribution_headers.py, tests/run_agent/test_provider_fallback.py, tests/run_agent/test_provider_parity.py, tests/run_agent/test_run_agent.py, tests/run_agent/test_switch_model_reapplies_headers.py, tests/test_install_ps1_uv_powershell_host.py, tests/tools/test_delegate.py, tests/tools/test_managed_media_gateways.py, tests/tools/test_managed_tool_gateway.py, tests/tools/test_strict_provider_selection.py, tests/tools/test_tts_openai_config.py, tests/tools/test_url_safety.py, tests/tools/test_web_tools_config.py, tools/managed_tool_gateway.py, tools/mcp_oauth.py, tools/skills_hub.py, tools/skills_sync_client.py, trajectory_compressor.py, ui-tui/scripts/billing-fixtures.tsx, ui-tui/src/__tests__/subscriptionCommand.test.ts, ui-tui/src/__tests__/subscriptionOverlay.test.tsx, ui-tui/src/app/slash/commands/subscription.ts, ui-tui/src/domain/paths.ts, uv.lock, web/src/components/SidebarFooter.tsx, web/src/pages/DocsPage.tsx, web/src/pages/SystemPage.tsx, website/docs/developer-guide/contributing.md, website/docs/developer-guide/egress-internals.md, website/docs/getting-started/installation.md, website/docs/getting-started/platform-support.md, website/docs/getting-started/quickstart.md, website/docs/getting-started/termux.md, website/docs/guides/manage-nastech-cloud-with-mcp.md, website/docs/guides/run-nastech-with-nastech-portal.md, website/docs/guides/run-nemotron-3-ultra-free.md, website/docs/index.mdx, website/docs/integrations/nastech-portal.md, website/docs/integrations/providers.md, website/docs/reference/cli-commands.md, website/docs/reference/environment-variables.md, website/docs/reference/faq.md, website/docs/reference/model-catalog.md, website/docs/user-guide/desktop.md, website/docs/user-guide/egress/iron-proxy.md, website/docs/user-guide/features/browser.md, website/docs/user-guide/features/image-generation.md, website/docs/user-guide/features/skills.md, website/docs/user-guide/features/subscription-proxy.md, website/docs/user-guide/features/tool-gateway.md, website/docs/user-guide/features/tools.md, website/docs/user-guide/features/tts.md, website/docs/user-guide/features/web-dashboard.md, website/docs/user-guide/features/web-search.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/windows-wsl-quickstart.md, website/docusaurus.config.ts, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/contributing.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/quickstart.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-nastech-with-nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/index.mdx, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/providers.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/faq.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/model-catalog.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/subscription-proxy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tools.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tts.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-native.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-wsl-quickstart.md, website/scripts/generate-llms-txt.py, website/scripts/prebuild.mjs, website/static/api/model-catalog.json, website/static/oauth/client-metadata.json


## Direct upstream tree delta

- complete: +35 ~102 -0 ↪0
- MODIFIED `.dockerignore`
- MODIFIED `.github/actions/detect-changes/action.yml`
- MODIFIED `.github/workflows/ci.yaml`
- ADDED `.github/workflows/rust-tests.yml`
- MODIFIED `agent/agent_init.py`
- MODIFIED `agent/agent_runtime_helpers.py`
- MODIFIED `agent/anthropic_adapter.py`
- MODIFIED `agent/model_metadata.py`
- MODIFIED `agent/secret_scope.py`
- MODIFIED `agent/transports/codex.py`
- MODIFIED `apps/bootstrap-installer/src-tauri/src/powershell.rs`
- MODIFIED `apps/bootstrap-installer/src-tauri/src/update.rs`
- ADDED `apps/desktop/electron/favicon.test.ts`
- ADDED `apps/desktop/electron/favicon.ts`
- MODIFIED `apps/desktop/electron/main.ts`
- MODIFIED `apps/desktop/electron/preload.ts`
- ADDED `apps/desktop/electron/update-handoff-marker.test.ts`
- MODIFIED `apps/desktop/electron/update-marker.test.ts`
- MODIFIED `apps/desktop/electron/update-marker.ts`
- MODIFIED `apps/desktop/package.json`
- MODIFIED `apps/desktop/src/app/chat/composer/hooks/use-at-completions-contrib.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/hooks/use-at-completions.ts`
- MODIFIED `apps/desktop/src/app/chat/sidebar/chrome.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/cron-jobs-section.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/load-more-row.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/projects/workspace-header.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/section-states.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/session-row.tsx`
- MODIFIED `apps/desktop/src/app/messaging/platform-icon.tsx`
- MODIFIED `apps/desktop/src/app/skills/mcp-tab.tsx`
- ADDED `apps/desktop/src/components/ui/avatar-chip.test.tsx`
- ADDED `apps/desktop/src/components/ui/avatar-chip.tsx`
- ADDED `apps/desktop/src/components/ui/connector-card.test.tsx`
- ADDED `apps/desktop/src/components/ui/connector-card.tsx`
- ADDED `apps/desktop/src/components/ui/connector-logo.tsx`
- ADDED `apps/desktop/src/components/ui/favicon.tsx`
- MODIFIED `apps/desktop/src/global.d.ts`
- MODIFIED `apps/desktop/src/i18n/plugin-i18n.ts`
- MODIFIED `apps/desktop/src/lib/external-link.test.tsx`
- MODIFIED `apps/desktop/src/lib/external-link.tsx`
- MODIFIED `apps/desktop/src/lib/mcp-brands.tsx`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/plugin.js`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/group-chat.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/group-mention-composer.test.mjs`
- ADDED `apps/desktop/src/plugins/nastech-bots/tests/group-room-ux.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/legacy-sdk-compat.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/mention-completions.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/mention-handoff-quoting.test.mjs`
- ADDED `apps/desktop/src/plugins/nastech-bots/tests/mention-roster-cache-key.test.mjs`
- MODIFIED `apps/desktop/src/sdk/index.ts`
- MODIFIED `apps/desktop/src/themes/index.ts`
- ADDED `apps/desktop/src/themes/request.test.tsx`
- ADDED `apps/desktop/src/themes/request.ts`
- MODIFIED `apps/desktop/vite.config.ts`
- MODIFIED `cli.py`
- ADDED `contributors/emails/805041391@qq.com`
- ADDED `contributors/emails/Lesnak1@users.noreply.github.com`
- ADDED `contributors/emails/atesabdulkadir@outlook.com.tr`
- ADDED `contributors/emails/bkashjee@gmail.com`
- ADDED `contributors/emails/yuyigeng97@gmail.com`
- ADDED `contributors/emails/zhaomengfan44@sina.com`
- MODIFIED `cron/jobs.py`
- MODIFIED `cron/scheduler.py`
- MODIFIED `docker/stage2-hook.sh`
- MODIFIED `gateway/config.py`
- MODIFIED `gateway/relay/adapter.py`
- MODIFIED `gateway/run.py`
- MODIFIED `gateway/scale_to_zero.py`
- MODIFIED `gateway/status.py`
- MODIFIED `gateway/stream_consumer.py`
- MODIFIED `nastech_cli/build_info.py`
- MODIFIED `nastech_cli/config_defaults.py`
- MODIFIED `nastech_cli/cron.py`
- MODIFIED `nastech_cli/gateway_enroll.py`
- MODIFIED `nastech_cli/goals.py`
- MODIFIED `nastech_cli/model_normalize.py`
- MODIFIED `nastech_cli/model_switch.py`
- MODIFIED `nastech_cli/models.py`
- MODIFIED `nastech_cli/runtime_provider.py`
- MODIFIED `nastech_cli/setup.py`
- MODIFIED `nastech_cli/subcommands/cron.py`
- MODIFIED `nastech_cli/update_cmd.py`
- ADDED `nastech_cli/update_receipt.py`
- MODIFIED `package-lock.json`
- MODIFIED `plugins/model-providers/opencode-zen/__init__.py`
- MODIFIED `plugins/platforms/telegram/adapter.py`
- MODIFIED `scripts/ci/classify_changes.py`
- MODIFIED `scripts/desktop-update/posix.sh`
- MODIFIED `scripts/desktop-update/windows.ps1`
- MODIFIED `skills/autonomous-ai-agents/nastech-agent/references/desktop-plugins.md`
- ADDED `tests/agent/test_anthropic_thinking_disable.py`
- MODIFIED `tests/agent/test_builtin_memory_disabled_surface.py`
- MODIFIED `tests/agent/test_secret_scope.py`
- MODIFIED `tests/agent/transports/test_codex_transport.py`
- MODIFIED `tests/ci/test_classify_changes.py`
- ADDED `tests/cron/test_cron_reasoning_effort.py`
- MODIFIED `tests/gateway/relay/test_relay_interactive.py`
- MODIFIED `tests/gateway/relay/test_relay_registration.py`
- ADDED `tests/gateway/test_approval_send_timeout_ambiguity.py`
- ADDED `tests/gateway/test_clarify_send_timeout_ambiguity.py`
- MODIFIED `tests/gateway/test_config.py`
- MODIFIED `tests/gateway/test_scale_to_zero.py`
- MODIFIED `tests/gateway/test_scale_to_zero_watcher.py`
- MODIFIED `tests/gateway/test_telegram_rich_messages.py`
- ADDED `tests/nastech_cli/test_custom_opencode_family_runtime.py`
- ADDED `tests/nastech_cli/test_gateway_enroll_multiplex_warning.py`
- ADDED `tests/nastech_cli/test_goal_judge_timeout_config.py`
- MODIFIED `tests/nastech_cli/test_model_validation.py`
- MODIFIED `tests/nastech_cli/test_service_manager.py`
- ADDED `tests/nastech_cli/test_update_receipt.py`
- ADDED `tests/nastech_cli/test_update_skip_unchanged_editable_install.py`
- MODIFIED `tests/relay/test_relay_format_hints.py`
- ADDED `tests/relay/test_relay_prompt_ack_stream_isolation.py`
- MODIFIED `tests/run_agent/test_run_agent.py`
- ADDED `tests/test_desktop_update_windows_pipe_drain.py`
- MODIFIED `tests/test_desktop_update_windows_progress.py`
- MODIFIED `tests/test_desktop_update_windows_python_handoff.py`
- ADDED `tests/tools/test_stage2_hook_api_server_keygen.py`
- MODIFIED `tests/tools/test_write_approval.py`
- ADDED `tests/tui_gateway/test_profiles_ui_meta_cas.py`
- MODIFIED `tools/approval.py`
- MODIFIED `tools/cronjob_tools.py`
- MODIFIED `tools/memory_tool.py`
- MODIFIED `tools/registry.py`
- MODIFIED `tui_gateway/methods_profiles.py`
- MODIFIED `tui_gateway/server.py`
- MODIFIED `web/package.json`
- MODIFIED `web/vite.config.ts`
- MODIFIED `web/vitest.config.ts`
- MODIFIED `website/docs/developer-guide/desktop-plugin-sdk.md`
- ADDED `website/docs/guides/manage-nastech-cloud-with-mcp.md`
- MODIFIED `website/docs/reference/cli-commands.md`
- MODIFIED `website/docs/user-guide/bot-mode.md`
- MODIFIED `website/docs/user-guide/features/cron.md`
- MODIFIED `website/docs/user-guide/features/memory.md`
- MODIFIED `website/docs/user-guide/messaging/telegram.md`
- MODIFIED `website/sidebars.ts`

## Scan

10008 files scanned [archive=1, audio=5, binary=7, doc=5, font=13, image=93, text=9884]


## Diff

1287 renamed, 0 rewritten, 8331 identical, 63 locked, 0 missing, 34 owned, 239 reconciled


## Fork check (vs nastech-agent)

- 9717 identical, 249 updated (+0/-0 lines), 35 added, 0 missing, 0 fork-local-unpreserved, 0 stale-upstream, 7 locked/binary, 0 collision-safe relocated, 54 preserved fork-local files, 0 violations

- features: fork 51 -> branded 51

Auto-generated by 100Ways.
