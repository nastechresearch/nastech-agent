# Nastech Update Report #1

- upstream sha : `f751a8c5467c41500e505d90cb0eb8b70929080f`
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

- total files : 10308
- renamed     : 1426 (folders and file names)
- text-rewritten : 10210
- locked-copied  : 56
- binary-copied  : 8
- owned assets   : 34 (our logo/banner/mascot override upstream)

## Reconcile

- fixed : 255 files reconciled: .github/workflows/deploy-site.yml, .github/workflows/deploy-site.yml, .github/workflows/skills-index-freshness.yml, .mailmap, CONTRIBUTING.es.md, CONTRIBUTING.md, Dockerfile, README.es.md, README.md, README.ur-pk.md, README.zh-CN.md, SECURITY.es.md, SECURITY.md, agent/agent_runtime_helpers.py, agent/anthropic_adapter.py, agent/auxiliary_client.py, agent/billing_links.py, agent/billing_view.py, agent/chat_completion_helpers.py, agent/conversation_loop.py, agent/credits_tracker.py, agent/model_metadata.py, agent/prompt_builder.py, agent/proxy_sources/iron_proxy.py, agent/subscription_view.py, agent/usage_pricing.py, apps/bootstrap-installer/src-tauri/Cargo.toml, apps/desktop/README.md, apps/desktop/electron/backend-health.test.ts, apps/desktop/electron/backend-health.ts, apps/desktop/electron/connection-config.test.ts, apps/desktop/electron/main.ts, apps/desktop/electron/remote-lifecycle.ts, apps/desktop/package.json, apps/desktop/src/app/messaging/index.test.tsx, apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx, apps/desktop/src/app/settings/about-settings.tsx, apps/desktop/src/app/settings/billing/api.test.ts, apps/desktop/src/app/settings/billing/dev-fixtures.ts, apps/desktop/src/app/settings/billing/errors.test.ts, apps/desktop/src/app/settings/billing/types.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.ts, apps/desktop/src/app/settings/billing/use-charge-poller.test.ts, apps/desktop/src/app/settings/billing/use-step-up.test.tsx, apps/desktop/src/app/settings/constants.ts, apps/desktop/src/app/settings/gateway-settings.tsx, apps/desktop/src/app/settings/toolset-config-panel.test.tsx, apps/desktop/src/app/skills/embedded-hub-picker.tsx, apps/desktop/src/app/skills/index.test.tsx, apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts, apps/desktop/src/components/boot-failure-overlay.test.tsx, apps/desktop/src/components/boot-failure-overlay.tsx, apps/desktop/src/components/send-diagnostics-dialog.tsx, apps/desktop/src/contrib/plugin.ts, apps/desktop/src/i18n/en.ts, apps/desktop/src/i18n/ja.ts, apps/desktop/src/i18n/zh-hant.ts, apps/desktop/src/i18n/zh.ts, apps/desktop/src/plugins/nastech-bots/plugin.js, apps/desktop/src/sdk/index.ts, cli-config.yaml.example, eslint.config.shared.mjs, nastech_cli/auth.py, nastech_cli/banner.py, nastech_cli/config_defaults.py, nastech_cli/dashboard_auth/login_page.py, nastech_cli/dashboard_register.py, nastech_cli/debug.py, nastech_cli/diagnostics_upload.py, nastech_cli/fallback_cmd.py, nastech_cli/kanban.py, nastech_cli/main.py, nastech_cli/model_catalog.py, nastech_cli/model_switch.py, nastech_cli/models.py, nastech_cli/nastech_account.py, nastech_cli/nastech_billing.py, nastech_cli/plugins_cmd.py, nastech_cli/portal_cli.py, nastech_cli/providers.py, nastech_cli/proxy/__init__.py, nastech_cli/proxy/adapters/base.py, nastech_cli/proxy/adapters/nastech_portal.py, nastech_cli/setup.py, nastech_cli/setup_whatsapp_cloud.py, nastech_cli/skin_engine.py, nastech_cli/telegram_managed_bot.py, nastech_cli/tools_config.py, nastech_cli/uninstall.py, nastech_cli/update_cmd.py, nastech_cli/web_server.py, nastech_constants.py, package-lock.json, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/plugin.yaml, plugins/kanban/dashboard/dist/index.js, plugins/kanban/systemd/nastech-kanban-dispatcher.service, plugins/model-providers/ai-gateway/__init__.py, plugins/model-providers/fireworks/__init__.py, plugins/model-providers/kimi-coding/__init__.py, plugins/model-providers/nastech/__init__.py, plugins/model-providers/opencode-free/__init__.py, plugins/model-providers/opencode-zen/__init__.py, plugins/nastech-achievements/dashboard/dist/index.js, plugins/platforms/discord/adapter.py, plugins/platforms/email/adapter.py, plugins/platforms/photon/sidecar/package-lock.json, plugins/platforms/slack/adapter.py, run_agent.py, scripts/build_model_catalog.py, scripts/contributor_audit.py, scripts/dev-sandbox.sh, scripts/install.cmd, scripts/install.ps1, scripts/install.sh, scripts/release.py, scripts/whatsapp-bridge/package-lock.json, setup.py, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/references/background-systems.md, skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md, skills/autonomous-ai-agents/nastech-agent/references/configuration.md, skills/autonomous-ai-agents/nastech-agent/references/contributor-guide.md, skills/autonomous-ai-agents/nastech-agent/references/portal-auth-for-third-party-apps.md, skills/autonomous-ai-agents/nastech-agent/references/providers-and-models.md, skills/autonomous-ai-agents/nastech-agent/references/webhooks.md, tests/agent/test_anthropic_adapter.py, tests/agent/test_auxiliary_client.py, tests/agent/test_auxiliary_main_first.py, tests/agent/test_auxiliary_transport_autodetect.py, tests/agent/test_billing_links.py, tests/agent/test_credential_pool.py, tests/agent/test_credits_policy.py, tests/agent/test_error_classifier.py, tests/agent/test_model_metadata.py, tests/agent/test_nastech_credits_gauge.py, tests/agent/test_nastech_oauth_401_guidance.py, tests/agent/test_nastech_portal_anthropic_wire.py, tests/agent/test_phantom_tool_references.py, tests/agent/transports/test_chat_completions.py, tests/cli/test_cli_first_run_setup.py, tests/cli/test_cli_provider_resolution.py, tests/cli/test_show_config_credential.py, tests/docker/test_sqlite_runtime.py, tests/gateway/test_discord_format.py, tests/gateway/test_run_progress_topics.py, tests/gateway/test_status_command.py, tests/gateway/test_usage_command.py, tests/nastech_cli/test_auth_nastech_provider.py, tests/nastech_cli/test_base_url_host_identity.py, tests/nastech_cli/test_dashboard_auth_gate.py, tests/nastech_cli/test_dashboard_register.py, tests/nastech_cli/test_fireworks_provider.py, tests/nastech_cli/test_gateway_restart_loop.py, tests/nastech_cli/test_model_catalog.py, tests/nastech_cli/test_nastech_auth_keepalive.py, tests/nastech_cli/test_nastech_auth_status_cache.py, tests/nastech_cli/test_nastech_inference_url_validation.py, tests/nastech_cli/test_nastech_portal_staging_allowlist.py, tests/nastech_cli/test_nastech_reasoning_metadata.py, tests/nastech_cli/test_proxy.py, tests/nastech_cli/test_reasoning_caps_disk_cache.py, tests/nastech_cli/test_sale_pricing.py, tests/nastech_cli/test_web_oauth_dispatch.py, tests/plugins/dashboard_auth/test_nastech_provider.py, tests/plugins/image_gen/check_parity_vs_main.py, tests/plugins/image_gen/test_openrouter_compat_provider.py, tests/plugins/test_chronos_verify.py, tests/run_agent/test_anthropic_prompt_cache_policy.py, tests/run_agent/test_primary_runtime_restore.py, tests/run_agent/test_provider_attribution_headers.py, tests/run_agent/test_provider_fallback.py, tests/run_agent/test_provider_parity.py, tests/run_agent/test_run_agent.py, tests/run_agent/test_switch_model_reapplies_headers.py, tests/test_install_ps1_uv_powershell_host.py, tests/tools/test_delegate.py, tests/tools/test_managed_media_gateways.py, tests/tools/test_managed_tool_gateway.py, tests/tools/test_strict_provider_selection.py, tests/tools/test_tts_openai_config.py, tests/tools/test_url_safety.py, tests/tools/test_web_tools_config.py, tools/managed_tool_gateway.py, tools/mcp_oauth.py, tools/skills_hub.py, tools/skills_sync_client.py, trajectory_compressor.py, ui-tui/scripts/billing-fixtures.tsx, ui-tui/src/__tests__/subscriptionCommand.test.ts, ui-tui/src/__tests__/subscriptionOverlay.test.tsx, ui-tui/src/app/slash/commands/subscription.ts, ui-tui/src/domain/paths.ts, uv.lock, web/src/components/SidebarFooter.tsx, web/src/pages/DocsPage.tsx, web/src/pages/SystemPage.tsx, website/docs/developer-guide/contributing.md, website/docs/developer-guide/egress-internals.md, website/docs/getting-started/installation.md, website/docs/getting-started/platform-support.md, website/docs/getting-started/quickstart.md, website/docs/getting-started/termux.md, website/docs/guides/manage-nastech-cloud-with-mcp.md, website/docs/guides/run-nastech-with-nastech-portal.md, website/docs/guides/run-nemotron-3-ultra-free.md, website/docs/index.mdx, website/docs/integrations/nastech-portal.md, website/docs/integrations/providers.md, website/docs/reference/cli-commands.md, website/docs/reference/environment-variables.md, website/docs/reference/faq.md, website/docs/reference/model-catalog.md, website/docs/user-guide/desktop.md, website/docs/user-guide/egress/iron-proxy.md, website/docs/user-guide/features/browser.md, website/docs/user-guide/features/image-generation.md, website/docs/user-guide/features/skills.md, website/docs/user-guide/features/subscription-proxy.md, website/docs/user-guide/features/tool-gateway.md, website/docs/user-guide/features/tools.md, website/docs/user-guide/features/tts.md, website/docs/user-guide/features/web-dashboard.md, website/docs/user-guide/features/web-search.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/windows-wsl-quickstart.md, website/docusaurus.config.ts, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/contributing.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/quickstart.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-nastech-with-nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/index.mdx, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/providers.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/faq.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/model-catalog.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/subscription-proxy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tools.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tts.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-native.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-wsl-quickstart.md, website/scripts/generate-llms-txt.py, website/scripts/prebuild.mjs, website/static/api/model-catalog.json, website/static/oauth/client-metadata.json


## Direct upstream tree delta

- complete: +68 ~137 -2 ↪0
- MODIFIED `agent/agent_init.py`
- MODIFIED `agent/codex_runtime.py`
- MODIFIED `agent/conversation_compression.py`
- MODIFIED `agent/memory_manager.py`
- MODIFIED `agent/memory_provider.py`
- MODIFIED `agent/monitoring/cron_health.py`
- MODIFIED `agent/native_compaction.py`
- MODIFIED `agent/prompt_builder.py`
- MODIFIED `agent/system_prompt.py`
- MODIFIED `agent/tool_dispatch_helpers.py`
- MODIFIED `agent/tool_guardrails.py`
- MODIFIED `agent/turn_finalizer.py`
- MODIFIED `apps/desktop/e2e/at-rest-connection-token.spec.ts`
- ADDED `apps/desktop/electron/browser-windows.test.ts`
- ADDED `apps/desktop/electron/browser-windows.ts`
- MODIFIED `apps/desktop/electron/connection-config.test.ts`
- MODIFIED `apps/desktop/electron/connection-config.ts`
- MODIFIED `apps/desktop/electron/main.ts`
- MODIFIED `apps/desktop/electron/preload.ts`
- ADDED `apps/desktop/electron/secret-storage-policy.test.ts`
- ADDED `apps/desktop/electron/secret-storage-policy.ts`
- MODIFIED `apps/desktop/src/api/sessions.ts`
- MODIFIED `apps/desktop/src/app/artifacts/artifact-utils.ts`
- ADDED `apps/desktop/src/app/chat/browser-popout-shell.tsx`
- MODIFIED `apps/desktop/src/app/chat/pane-mirror.ts`
- MODIFIED `apps/desktop/src/app/chat/preview-tile.test.ts`
- MODIFIED `apps/desktop/src/app/chat/preview-tile.tsx`
- MODIFIED `apps/desktop/src/app/chat/right-rail/preview-browser-bar.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/right-rail/preview-browser-bar.tsx`
- MODIFIED `apps/desktop/src/app/chat/right-rail/preview-pane.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/session-actions-menu.test.tsx`
- MODIFIED `apps/desktop/src/app/contrib/controller.tsx`
- MODIFIED `apps/desktop/src/app/contrib/hooks/use-desktop-integrations.ts`
- MODIFIED `apps/desktop/src/app/contrib/wiring.tsx`
- MODIFIED `apps/desktop/src/app/settings/gateway-settings.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/user-edit-composer.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/user-message-edit.test.tsx`
- MODIFIED `apps/desktop/src/components/pane-shell/tree/renderer/track-model.ts`
- MODIFIED `apps/desktop/src/components/pane-shell/tree/renderer/tree-group.tsx`
- MODIFIED `apps/desktop/src/components/pane-shell/tree/store.ts`
- MODIFIED `apps/desktop/src/global.d.ts`
- MODIFIED `apps/desktop/src/nastech.test.ts`
- MODIFIED `apps/desktop/src/i18n/ar.ts`
- MODIFIED `apps/desktop/src/i18n/en.ts`
- MODIFIED `apps/desktop/src/i18n/ja.ts`
- MODIFIED `apps/desktop/src/i18n/types.ts`
- MODIFIED `apps/desktop/src/i18n/zh-hant.ts`
- MODIFIED `apps/desktop/src/i18n/zh.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/plugin.js`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/focused-bot-highlight.test.mjs`
- ADDED `apps/desktop/src/plugins/nastech-bots/tests/routines-dialog-owner-label.test.mjs`
- ADDED `apps/desktop/src/plugins/nastech-bots/tests/routines-pane-owner.test.mjs`
- ADDED `apps/desktop/src/plugins/nastech-bots/tests/routines-rpc-error.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/routines-selected-bot.test.mjs`
- MODIFIED `apps/desktop/src/store/preview.test.ts`
- MODIFIED `apps/desktop/src/store/preview.ts`
- MODIFIED `apps/desktop/src/store/session-states.ts`
- MODIFIED `apps/desktop/src/store/session-unread.ts`
- MODIFIED `apps/desktop/src/store/translucency.ts`
- MODIFIED `apps/desktop/src/store/windows.test.ts`
- MODIFIED `apps/desktop/src/store/windows.ts`
- MODIFIED `cli-config.yaml.example`
- MODIFIED `cli.py`
- ADDED `contributors/emails/joshuadavidfairbank@gmail.com`
- ADDED `contributors/emails/krzysztof.radzikowski@gmail.com`
- ADDED `contributors/emails/mail@cedric-ziel.com`
- ADDED `contributors/emails/mamagnus00@gmail.com`
- ADDED `contributors/emails/qazasdsdqaza@users.noreply.github.com`
- ADDED `contributors/emails/rroveri@nvidia.com`
- ADDED `cron/incidents.py`
- MODIFIED `cron/scheduler.py`
- MODIFIED `gateway/platforms/base.py`
- MODIFIED `gateway/run.py`
- MODIFIED `gateway/slash_commands.py`
- MODIFIED `nastech_cli/config.py`
- MODIFIED `nastech_cli/config_defaults.py`
- MODIFIED `nastech_cli/config_migrations.py`
- MODIFIED `nastech_cli/cron.py`
- MODIFIED `nastech_cli/main.py`
- MODIFIED `nastech_cli/mcp_catalog.py`
- MODIFIED `nastech_cli/mcp_config.py`
- MODIFIED `nastech_cli/subcommands/cron.py`
- MODIFIED `nastech_cli/subcommands/gui.py`
- MODIFIED `nastech_cli/tools_config.py`
- MODIFIED `nastech_cli/update_cmd.py`
- MODIFIED `nastech_state.py`
- MODIFIED `nastech_state_common.py`
- ADDED `optional-mcps/algolia/manifest.yaml`
- ADDED `optional-mcps/alltrails/manifest.yaml`
- ADDED `optional-mcps/amplitude/manifest.yaml`
- MODIFIED `optional-mcps/atlassian/manifest.yaml`
- ADDED `optional-mcps/attio/manifest.yaml`
- ADDED `optional-mcps/aws-knowledge/manifest.yaml`
- ADDED `optional-mcps/betterstack/manifest.yaml`
- ADDED `optional-mcps/buildkite/manifest.yaml`
- ADDED `optional-mcps/calendly/manifest.yaml`
- ADDED `optional-mcps/canva/manifest.yaml`
- ADDED `optional-mcps/circleci/manifest.yaml`
- ADDED `optional-mcps/clickup/manifest.yaml`
- ADDED `optional-mcps/close/manifest.yaml`
- ADDED `optional-mcps/cloudflare/manifest.yaml`
- ADDED `optional-mcps/cloudinary/manifest.yaml`
- ADDED `optional-mcps/context7/manifest.yaml`
- ADDED `optional-mcps/craft/manifest.yaml`
- ADDED `optional-mcps/deepwiki/manifest.yaml`
- ADDED `optional-mcps/dropbox/manifest.yaml`
- ADDED `optional-mcps/fireflies/manifest.yaml`
- ADDED `optional-mcps/gamma/manifest.yaml`
- ADDED `optional-mcps/gitlab/manifest.yaml`
- ADDED `optional-mcps/globalping/manifest.yaml`
- ADDED `optional-mcps/grafana/manifest.yaml`
- ADDED `optional-mcps/indeed/manifest.yaml`
- ADDED `optional-mcps/kiwi/manifest.yaml`
- ADDED `optional-mcps/klaviyo/manifest.yaml`
- ADDED `optional-mcps/microsoft-learn/manifest.yaml`
- ADDED `optional-mcps/miro/manifest.yaml`
- ADDED `optional-mcps/mixpanel/manifest.yaml`
- ADDED `optional-mcps/monday/manifest.yaml`
- ADDED `optional-mcps/motherduck/manifest.yaml`
- ADDED `optional-mcps/neon/manifest.yaml`
- ADDED `optional-mcps/plaid/manifest.yaml`
- ADDED `optional-mcps/postman/manifest.yaml`
- ADDED `optional-mcps/prisma-postgres/manifest.yaml`
- ADDED `optional-mcps/railway/manifest.yaml`
- ADDED `optional-mcps/robinhood/manifest.yaml`
- ADDED `optional-mcps/semgrep/manifest.yaml`
- ADDED `optional-mcps/strava/manifest.yaml`
- ADDED `optional-mcps/todoist/manifest.yaml`
- ADDED `optional-mcps/trivago/manifest.yaml`
- ADDED `optional-mcps/twelve-data/manifest.yaml`
- ADDED `optional-mcps/twilio-docs/manifest.yaml`
- ADDED `optional-mcps/wolfram/manifest.yaml`
- ADDED `optional-mcps/wordpress-com/manifest.yaml`
- MODIFIED `plugins/model-providers/nvidia/__init__.py`
- MODIFIED `plugins/teams_pipeline/meetings.py`
- MODIFIED `pyproject.toml`
- MODIFIED `run_agent.py`
- MODIFIED `scripts/analyze_livetest.py`
- MODIFIED `scripts/tool_search_livetest.py`
- MODIFIED `scripts/tool_search_livetest_ue_disc.py`
- MODIFIED `scripts/tool_search_livetest_ue_hard.py`
- MODIFIED `skills/autonomous-ai-agents/nastech-agent/references/troubleshooting.md`
- MODIFIED `tests/agent/test_platform_hint_desktop.py`
- ADDED `tests/agent/test_pre_compress_checkpoint_contract.py`
- MODIFIED `tests/agent/test_profile_home_override_precedence.py`
- MODIFIED `tests/agent/test_prompt_builder.py`
- MODIFIED `tests/agent/test_stall_guards.py`
- MODIFIED `tests/agent/test_system_prompt.py`
- ADDED `tests/cron/test_cron_incidents.py`
- MODIFIED `tests/gateway/test_platform_base.py`
- MODIFIED `tests/nastech_cli/test_gui_command.py`
- MODIFIED `tests/nastech_cli/test_install_cua_driver.py`
- MODIFIED `tests/nastech_cli/test_mcp_catalog.py`
- MODIFIED `tests/nastech_cli/test_relay_plugin_cutover.py`
- MODIFIED `tests/nastech_cli/test_set_config_value.py`
- MODIFIED `tests/nastech_cli/test_tools_config.py`
- MODIFIED `tests/nastech_cli/test_tui_npm_install.py`
- MODIFIED `tests/nastech_cli/test_update_concurrent_quarantine.py`
- MODIFIED `tests/nastech_cli/test_update_launchd_restart_verification.py`
- ADDED `tests/nastech_cli/test_update_launchd_unloaded_gateway.py`
- MODIFIED `tests/nastech_cli/test_venv_holder_windows_live.py`
- MODIFIED `tests/plugins/test_a2a_schema_registration.py`
- MODIFIED `tests/plugins/test_teams_pipeline_meetings.py`
- MODIFIED `tests/providers/test_e2e_wiring.py`
- MODIFIED `tests/providers/test_provider_profiles.py`
- MODIFIED `tests/run_agent/test_pre_compress_memory_context.py`
- MODIFIED `tests/run_agent/test_run_agent.py`
- MODIFIED `tests/test_tui_gateway_server.py`
- MODIFIED `tests/tools/conftest.py`
- ADDED `tests/tools/test_computer_use_fullscreen_capture.py`
- ADDED `tests/tools/test_deferral_fixes.py`
- MODIFIED `tests/tools/test_docker_environment.py`
- DELETED `tests/tools/test_flux3_video_tool.py`
- MODIFIED `tests/tools/test_managed_tool_gateway.py`
- MODIFIED `tests/tools/test_mcp_tool.py`
- MODIFIED `tests/tools/test_microsoft_graph_client.py`
- MODIFIED `tests/tools/test_shared_container_task_id.py`
- MODIFIED `tests/tools/test_tool_search.py`
- ADDED `tests/tools/test_tool_search_multiquery.py`
- ADDED `tests/tools/test_web_result_cache.py`
- MODIFIED `tools/computer_use/backend.py`
- MODIFIED `tools/computer_use/cua_backend.py`
- MODIFIED `tools/computer_use/schema.py`
- MODIFIED `tools/computer_use/tool.py`
- MODIFIED `tools/environments/docker.py`
- DELETED `tools/flux3_video_tool.py`
- MODIFIED `tools/mcp_tool.py`
- MODIFIED `tools/microsoft_graph_client.py`
- MODIFIED `tools/terminal_tool.py`
- MODIFIED `tools/tool_search.py`
- ADDED `tools/web_result_cache.py`
- MODIFIED `tools/web_tools.py`
- MODIFIED `toolsets.py`
- MODIFIED `tui_gateway/server.py`
- MODIFIED `uv.lock`
- MODIFIED `website/docs/developer-guide/memory-provider-plugin.md`
- MODIFIED `website/docs/guides/desktop-native-signin.md`
- MODIFIED `website/docs/integrations/index.md`
- MODIFIED `website/docs/user-guide/configuration.md`
- MODIFIED `website/docs/user-guide/desktop.md`
- MODIFIED `website/docs/user-guide/features/browser.md`
- MODIFIED `website/docs/user-guide/features/computer-use.md`
- MODIFIED `website/docs/user-guide/features/cron.md`
- MODIFIED `website/docs/user-guide/features/mcp.md`
- MODIFIED `website/docs/user-guide/features/tool-search.md`
- MODIFIED `website/docs/user-guide/features/web-search.md`
- MODIFIED `website/docs/user-guide/multi-connection-desktop.md`

## Scan

10362 files scanned [audio=5, binary=7, doc=5, font=13, image=92, text=10240]


## Diff

1339 renamed, 0 rewritten, 8625 identical, 61 locked, 0 missing, 34 owned, 249 reconciled


## Fork check (vs nastech-agent)

- 10009 identical, 284 updated (+0/-0 lines), 68 added, 0 missing, 0 fork-local-unpreserved, 0 stale-upstream, 1 locked/binary, 0 collision-safe relocated, 54 preserved fork-local files, 0 violations

- features: fork 51 -> branded 51

Auto-generated by 100Ways.
