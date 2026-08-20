# Nastech Update Report #1

- upstream sha : `044acf2bf700b8452e903f035406091146eb0245`
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

- total files : 9919
- renamed     : 1362 (folders and file names)
- text-rewritten : 9819
- locked-copied  : 57
- binary-copied  : 9
- owned assets   : 34 (our logo/banner/mascot override upstream)

## Reconcile

- fixed : 243 files reconciled: .github/workflows/deploy-site.yml, .github/workflows/skills-index-freshness.yml, .mailmap, CONTRIBUTING.es.md, CONTRIBUTING.md, Dockerfile, README.es.md, README.md, README.ur-pk.md, README.zh-CN.md, SECURITY.es.md, SECURITY.md, agent/agent_runtime_helpers.py, agent/anthropic_adapter.py, agent/auxiliary_client.py, agent/billing_links.py, agent/billing_view.py, agent/chat_completion_helpers.py, agent/conversation_loop.py, agent/credits_tracker.py, agent/model_metadata.py, agent/prompt_builder.py, agent/proxy_sources/iron_proxy.py, agent/subscription_view.py, agent/usage_pricing.py, apps/bootstrap-installer/src-tauri/Cargo.toml, apps/desktop/README.md, apps/desktop/electron/connection-config.test.ts, apps/desktop/electron/main.ts, apps/desktop/electron/remote-lifecycle.ts, apps/desktop/package.json, apps/desktop/src/app/messaging/index.test.tsx, apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx, apps/desktop/src/app/settings/about-settings.tsx, apps/desktop/src/app/settings/billing/api.test.ts, apps/desktop/src/app/settings/billing/dev-fixtures.ts, apps/desktop/src/app/settings/billing/errors.test.ts, apps/desktop/src/app/settings/billing/types.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.ts, apps/desktop/src/app/settings/billing/use-charge-poller.test.ts, apps/desktop/src/app/settings/billing/use-step-up.test.tsx, apps/desktop/src/app/settings/constants.ts, apps/desktop/src/app/settings/gateway-settings.tsx, apps/desktop/src/app/settings/toolset-config-panel.test.tsx, apps/desktop/src/app/skills/embedded-hub-picker.tsx, apps/desktop/src/app/skills/index.test.tsx, apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts, apps/desktop/src/contrib/plugin.ts, apps/desktop/src/i18n/en.ts, apps/desktop/src/i18n/ja.ts, apps/desktop/src/i18n/zh-hant.ts, apps/desktop/src/i18n/zh.ts, apps/desktop/src/plugins/nastech-bots/plugin.js, apps/desktop/src/sdk/index.ts, cli-config.yaml.example, eslint.config.shared.mjs, nastech_cli/auth.py, nastech_cli/banner.py, nastech_cli/config_defaults.py, nastech_cli/dashboard_register.py, nastech_cli/diagnostics_upload.py, nastech_cli/fallback_cmd.py, nastech_cli/kanban.py, nastech_cli/main.py, nastech_cli/model_catalog.py, nastech_cli/model_switch.py, nastech_cli/models.py, nastech_cli/nastech_account.py, nastech_cli/nastech_billing.py, nastech_cli/plugins_cmd.py, nastech_cli/portal_cli.py, nastech_cli/providers.py, nastech_cli/proxy/__init__.py, nastech_cli/proxy/adapters/base.py, nastech_cli/proxy/adapters/nastech_portal.py, nastech_cli/setup.py, nastech_cli/setup_whatsapp_cloud.py, nastech_cli/skin_engine.py, nastech_cli/telegram_managed_bot.py, nastech_cli/tools_config.py, nastech_cli/uninstall.py, nastech_cli/update_cmd.py, nastech_cli/web_server.py, nastech_constants.py, package-lock.json, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/plugin.yaml, plugins/kanban/dashboard/dist/index.js, plugins/kanban/systemd/nastech-kanban-dispatcher.service, plugins/model-providers/ai-gateway/__init__.py, plugins/model-providers/fireworks/__init__.py, plugins/model-providers/kimi-coding/__init__.py, plugins/model-providers/nastech/__init__.py, plugins/model-providers/opencode-zen/__init__.py, plugins/nastech-achievements/dashboard/dist/index.js, plugins/platforms/discord/adapter.py, plugins/platforms/email/adapter.py, plugins/platforms/photon/sidecar/package-lock.json, plugins/platforms/slack/adapter.py, run_agent.py, scripts/build_model_catalog.py, scripts/contributor_audit.py, scripts/dev-sandbox.sh, scripts/install.cmd, scripts/install.ps1, scripts/install.sh, scripts/release.py, scripts/whatsapp-bridge/package-lock.json, setup.py, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/references/background-systems.md, skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md, skills/autonomous-ai-agents/nastech-agent/references/configuration.md, skills/autonomous-ai-agents/nastech-agent/references/contributor-guide.md, skills/autonomous-ai-agents/nastech-agent/references/portal-auth-for-third-party-apps.md, skills/autonomous-ai-agents/nastech-agent/references/providers-and-models.md, skills/autonomous-ai-agents/nastech-agent/references/webhooks.md, tests/agent/test_anthropic_adapter.py, tests/agent/test_auxiliary_client.py, tests/agent/test_auxiliary_main_first.py, tests/agent/test_auxiliary_transport_autodetect.py, tests/agent/test_billing_links.py, tests/agent/test_credential_pool.py, tests/agent/test_credits_policy.py, tests/agent/test_error_classifier.py, tests/agent/test_model_metadata.py, tests/agent/test_nastech_credits_gauge.py, tests/agent/test_nastech_oauth_401_guidance.py, tests/agent/test_nastech_portal_anthropic_wire.py, tests/agent/transports/test_chat_completions.py, tests/cli/test_cli_first_run_setup.py, tests/cli/test_cli_provider_resolution.py, tests/cli/test_show_config_credential.py, tests/docker/test_sqlite_runtime.py, tests/gateway/test_discord_format.py, tests/gateway/test_run_progress_topics.py, tests/gateway/test_status_command.py, tests/gateway/test_usage_command.py, tests/nastech_cli/test_auth_nastech_provider.py, tests/nastech_cli/test_base_url_host_identity.py, tests/nastech_cli/test_dashboard_register.py, tests/nastech_cli/test_fireworks_provider.py, tests/nastech_cli/test_gateway_restart_loop.py, tests/nastech_cli/test_model_catalog.py, tests/nastech_cli/test_nastech_auth_keepalive.py, tests/nastech_cli/test_nastech_auth_status_cache.py, tests/nastech_cli/test_nastech_inference_url_validation.py, tests/nastech_cli/test_nastech_portal_staging_allowlist.py, tests/nastech_cli/test_nastech_reasoning_metadata.py, tests/nastech_cli/test_proxy.py, tests/nastech_cli/test_reasoning_caps_disk_cache.py, tests/nastech_cli/test_sale_pricing.py, tests/nastech_cli/test_web_oauth_dispatch.py, tests/plugins/dashboard_auth/test_nastech_provider.py, tests/plugins/image_gen/check_parity_vs_main.py, tests/plugins/image_gen/test_openrouter_compat_provider.py, tests/plugins/test_chronos_verify.py, tests/run_agent/test_anthropic_prompt_cache_policy.py, tests/run_agent/test_primary_runtime_restore.py, tests/run_agent/test_provider_attribution_headers.py, tests/run_agent/test_provider_fallback.py, tests/run_agent/test_provider_parity.py, tests/run_agent/test_run_agent.py, tests/run_agent/test_switch_model_reapplies_headers.py, tests/test_install_ps1_uv_powershell_host.py, tests/tools/test_delegate.py, tests/tools/test_managed_media_gateways.py, tests/tools/test_managed_tool_gateway.py, tests/tools/test_strict_provider_selection.py, tests/tools/test_tts_openai_config.py, tests/tools/test_url_safety.py, tests/tools/test_web_tools_config.py, tools/managed_tool_gateway.py, tools/mcp_oauth.py, tools/skills_hub.py, tools/skills_sync_client.py, trajectory_compressor.py, ui-tui/scripts/billing-fixtures.tsx, ui-tui/src/__tests__/subscriptionCommand.test.ts, ui-tui/src/__tests__/subscriptionOverlay.test.tsx, ui-tui/src/app/slash/commands/subscription.ts, ui-tui/src/domain/paths.ts, uv.lock, web/src/components/SidebarFooter.tsx, web/src/pages/DocsPage.tsx, web/src/pages/SystemPage.tsx, website/docs/developer-guide/contributing.md, website/docs/developer-guide/egress-internals.md, website/docs/getting-started/installation.md, website/docs/getting-started/platform-support.md, website/docs/getting-started/quickstart.md, website/docs/getting-started/termux.md, website/docs/guides/run-nastech-with-nastech-portal.md, website/docs/guides/run-nemotron-3-ultra-free.md, website/docs/index.mdx, website/docs/integrations/nastech-portal.md, website/docs/integrations/providers.md, website/docs/reference/cli-commands.md, website/docs/reference/environment-variables.md, website/docs/reference/faq.md, website/docs/reference/model-catalog.md, website/docs/user-guide/desktop.md, website/docs/user-guide/egress/iron-proxy.md, website/docs/user-guide/features/browser.md, website/docs/user-guide/features/image-generation.md, website/docs/user-guide/features/skills.md, website/docs/user-guide/features/subscription-proxy.md, website/docs/user-guide/features/tool-gateway.md, website/docs/user-guide/features/tools.md, website/docs/user-guide/features/tts.md, website/docs/user-guide/features/web-dashboard.md, website/docs/user-guide/features/web-search.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/windows-wsl-quickstart.md, website/docusaurus.config.ts, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/contributing.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/quickstart.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-nastech-with-nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/index.mdx, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/providers.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/faq.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/model-catalog.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/subscription-proxy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tools.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tts.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-native.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-wsl-quickstart.md, website/scripts/generate-llms-txt.py, website/scripts/prebuild.mjs, website/static/api/model-catalog.json, website/static/oauth/client-metadata.json


## Direct upstream tree delta

- complete: +35 ~77 -5 ↪0
- MODIFIED `CONTRIBUTING.es.md`
- MODIFIED `CONTRIBUTING.md`
- MODIFIED `SECURITY.es.md`
- MODIFIED `SECURITY.md`
- MODIFIED `agent/agent_init.py`
- MODIFIED `agent/agent_runtime_helpers.py`
- MODIFIED `agent/tool_executor.py`
- MODIFIED `apps/desktop/electron/backend-ownership.test.ts`
- MODIFIED `apps/desktop/electron/backend-ownership.ts`
- MODIFIED `apps/desktop/electron/main.ts`
- MODIFIED `apps/desktop/electron/parent-process-identity.test.ts`
- MODIFIED `apps/desktop/electron/parent-process-identity.ts`
- ADDED `apps/desktop/src/app/chat/right-rail/preview-act.test.ts`
- ADDED `apps/desktop/src/app/chat/right-rail/preview-act.ts`
- ADDED `apps/desktop/src/app/chat/right-rail/preview-drive.ts`
- ADDED `apps/desktop/src/app/chat/right-rail/preview-input.ts`
- ADDED `apps/desktop/src/app/chat/right-rail/preview-mind.ts`
- MODIFIED `apps/desktop/src/app/chat/right-rail/preview-nav.ts`
- ADDED `apps/desktop/src/app/chat/right-rail/preview-nudge.ts`
- MODIFIED `apps/desktop/src/app/chat/right-rail/preview-pane.tsx`
- MODIFIED `apps/desktop/src/app/chat/right-rail/preview-reader.ts`
- ADDED `apps/desktop/src/app/chat/right-rail/preview-script-runner.ts`
- DELETED `apps/desktop/src/app/chat/right-rail/preview-tour-runner.ts`
- MODIFIED `apps/desktop/src/app/chat/right-rail/preview-tour.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/gateway-event/desktop-bridge.ts`
- MODIFIED `apps/desktop/src/lib/chat-messages/types.ts`
- ADDED `apps/desktop/src/lib/preview-act/act-in-page.test.ts`
- ADDED `apps/desktop/src/lib/preview-act/act-in-page.ts`
- ADDED `apps/desktop/src/lib/preview-act/identity.ts`
- ADDED `apps/desktop/src/lib/preview-act/naming.test.ts`
- ADDED `apps/desktop/src/lib/preview-act/naming.ts`
- ADDED `apps/desktop/src/lib/preview-act/types.ts`
- ADDED `apps/desktop/src/lib/preview-act/visibility.ts`
- ADDED `apps/desktop/src/lib/preview-act/watch-in-page.test.ts`
- ADDED `apps/desktop/src/lib/preview-act/watch-in-page.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/plugin.js`
- ADDED `apps/desktop/src/plugins/nastech-bots/tests/canonical-chat-adopt-before-mint.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/group-chat.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/hide-bot-chats.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/roster-preview.test.mjs`
- DELETED `apps/desktop/src/plugins/nastech-bots/tests/session-workspace.test.mjs`
- MODIFIED `cli.py`
- ADDED `contributors/emails/fattchris@users.noreply.github.com`
- MODIFIED `cron/scheduler.py`
- MODIFIED `docs/relay-connector-contract.md`
- MODIFIED `gateway/mirror.py`
- MODIFIED `gateway/relay/adapter.py`
- MODIFIED `gateway/relay/descriptor.py`
- MODIFIED `gateway/run.py`
- MODIFIED `nastech_cli/_startup_fast.py`
- MODIFIED `nastech_cli/commands.py`
- MODIFIED `nastech_cli/config.py`
- MODIFIED `nastech_cli/config_defaults.py`
- MODIFIED `nastech_cli/console_engine.py`
- MODIFIED `nastech_cli/main.py`
- ADDED `nastech_cli/process_identity.py`
- MODIFIED `nastech_cli/subcommands/update.py`
- DELETED `nastech_cli/subcommands/version.py`
- MODIFIED `nastech_cli/tips.py`
- MODIFIED `nastech_cli/update_cmd.py`
- MODIFIED `nastech_cli/web_server.py`
- MODIFIED `nix/checks.nix`
- MODIFIED `run_agent.py`
- MODIFIED `scripts/desktop-update/posix.sh`
- MODIFIED `scripts/desktop-update/windows.ps1`
- MODIFIED `tests/cli/test_cli_init.py`
- MODIFIED `tests/cli/test_cli_status_command.py`
- ADDED `tests/cli/test_command_palette.py`
- ADDED `tests/cli/test_model_picker_filter.py`
- DELETED `tests/cli/test_surrogate_sanitization.py`
- ADDED `tests/cron/test_cron_thread_seed_dm_keying.py`
- MODIFIED `tests/cron/test_scheduler.py`
- MODIFIED `tests/gateway/test_scale_to_zero_watcher.py`
- ADDED `tests/nastech_cli/test_composer_placeholder.py`
- MODIFIED `tests/nastech_cli/test_pre_command_hook.py`
- ADDED `tests/nastech_cli/test_process_identity.py`
- ADDED `tests/nastech_cli/test_resolve_turn_limit.py`
- MODIFIED `tests/nastech_cli/test_startup_plugin_gating.py`
- MODIFIED `tests/nastech_cli/test_subcommands_batch.py`
- MODIFIED `tests/nastech_cli/test_update_autostash.py`
- ADDED `tests/nastech_cli/test_update_fetch_failure_classifier.py`
- ADDED `tests/nastech_cli/test_update_handoff_backend_reap.py`
- MODIFIED `tests/nastech_cli/test_update_shim_self_lock.py`
- ADDED `tests/nastech_cli/test_update_stale_module_purge.py`
- ADDED `tests/relay/test_relay_format_hints.py`
- ADDED `tests/relay/test_relay_inchannel_continuable.py`
- MODIFIED `tests/run_agent/test_run_agent.py`
- MODIFIED `tests/test_desktop_update_shim_progress.py`
- ADDED `tests/tools/test_annotate_preview_tool.py`
- ADDED `tests/tools/test_drive_preview_tool.py`
- ADDED `tests/tools/test_web_keyless_rescue.py`
- DELETED `tests/tools/test_website_policy.py`
- MODIFIED `tests/tui_gateway/test_gui_surface_toolsets.py`
- ADDED `tools/annotate_preview_tool.py`
- MODIFIED `tools/cronjob_tools.py`
- ADDED `tools/drive_preview_tool.py`
- MODIFIED `tools/web_tools.py`
- MODIFIED `toolsets.py`
- MODIFIED `tui_gateway/methods_prompt.py`
- MODIFIED `tui_gateway/methods_session.py`
- MODIFIED `tui_gateway/server.py`
- MODIFIED `website/docs/developer-guide/contributing.md`
- MODIFIED `website/docs/getting-started/nix-setup.md`
- MODIFIED `website/docs/getting-started/termux.md`
- MODIFIED `website/docs/getting-started/updating.md`
- MODIFIED `website/docs/reference/cli-commands.md`
- MODIFIED `website/docs/reference/slash-commands.md`
- MODIFIED `website/docs/reference/tools-reference.md`
- MODIFIED `website/docs/reference/toolsets-reference.md`
- MODIFIED `website/docs/user-guide/bot-mode.md`
- MODIFIED `website/docs/user-guide/configuration.md`
- MODIFIED `website/docs/user-guide/features/web-search.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/contributing.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/nix-setup.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/updating.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md`

## Scan

9973 files scanned [archive=1, audio=5, binary=7, doc=5, font=13, image=93, text=9849]


## Diff

1279 renamed, 0 rewritten, 8305 identical, 63 locked, 0 missing, 34 owned, 238 reconciled


## Fork check (vs nastech-agent)

- 9710 identical, 228 updated (+0/-0 lines), 35 added, 0 missing, 0 fork-local-unpreserved, 0 stale-upstream, 0 locked/binary, 0 collision-safe relocated, 54 preserved fork-local files, 0 violations

- features: fork 51 -> branded 51

Auto-generated by 100Ways.
