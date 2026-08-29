# Nastech Update Report #1

- upstream sha : `360761c8cf50bf1222e89bb53433323e571cbaf1`
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

- total files : 10666
- renamed     : 1494 (folders and file names)
- text-rewritten : 10568
- locked-copied  : 56
- binary-copied  : 8
- owned assets   : 34 (our logo/banner/mascot override upstream)

## Reconcile

- fixed : 258 files reconciled: .github/workflows/deploy-site.yml, .github/workflows/deploy-site.yml, .github/workflows/skills-index-freshness.yml, .mailmap, CONTRIBUTING.es.md, CONTRIBUTING.md, Dockerfile, README.es.md, README.md, README.ur-pk.md, README.zh-CN.md, SECURITY.es.md, SECURITY.md, agent/agent_runtime_helpers.py, agent/anthropic_adapter.py, agent/auxiliary_client.py, agent/billing_links.py, agent/billing_view.py, agent/chat_completion_helpers.py, agent/conversation_loop.py, agent/credits_tracker.py, agent/model_metadata.py, agent/prompt_builder.py, agent/proxy_sources/iron_proxy.py, agent/subscription_view.py, agent/usage_pricing.py, apps/bootstrap-installer/src-tauri/Cargo.toml, apps/desktop/README.md, apps/desktop/electron/backend-health.test.ts, apps/desktop/electron/backend-health.ts, apps/desktop/electron/connection-config.test.ts, apps/desktop/electron/main.ts, apps/desktop/electron/oauth-partition.test.ts, apps/desktop/electron/remote-lifecycle.ts, apps/desktop/package.json, apps/desktop/src/app/messaging/index.test.tsx, apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx, apps/desktop/src/app/settings/about-settings.tsx, apps/desktop/src/app/settings/billing/api.test.ts, apps/desktop/src/app/settings/billing/dev-fixtures.ts, apps/desktop/src/app/settings/billing/errors.test.ts, apps/desktop/src/app/settings/billing/types.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.ts, apps/desktop/src/app/settings/billing/use-charge-poller.test.ts, apps/desktop/src/app/settings/billing/use-step-up.test.tsx, apps/desktop/src/app/settings/constants.ts, apps/desktop/src/app/settings/gateway-settings.tsx, apps/desktop/src/app/settings/toolset-config-panel.test.tsx, apps/desktop/src/app/skills/embedded-hub-picker.tsx, apps/desktop/src/app/skills/index.test.tsx, apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts, apps/desktop/src/components/boot-failure-overlay.test.tsx, apps/desktop/src/components/boot-failure-overlay.tsx, apps/desktop/src/components/send-diagnostics-dialog.tsx, apps/desktop/src/contrib/plugin.ts, apps/desktop/src/i18n/en.ts, apps/desktop/src/i18n/ja.ts, apps/desktop/src/i18n/zh-hant.ts, apps/desktop/src/i18n/zh.ts, apps/desktop/src/plugins/nastech-bots/skills-hub-picker.test.tsx, apps/desktop/src/plugins/nastech-bots/skills-hub.tsx, apps/desktop/src/sdk/index.ts, cli-config.yaml.example, eslint.config.shared.mjs, evals/browser_use/single_run.py, nastech_cli/auth.py, nastech_cli/banner.py, nastech_cli/config_defaults.py, nastech_cli/dashboard_auth/login_page.py, nastech_cli/dashboard_register.py, nastech_cli/debug.py, nastech_cli/diagnostics_upload.py, nastech_cli/fallback_cmd.py, nastech_cli/kanban.py, nastech_cli/main.py, nastech_cli/model_catalog.py, nastech_cli/model_switch.py, nastech_cli/models.py, nastech_cli/nastech_account.py, nastech_cli/nastech_billing.py, nastech_cli/plugins_cmd.py, nastech_cli/portal_cli.py, nastech_cli/providers.py, nastech_cli/proxy/__init__.py, nastech_cli/proxy/adapters/base.py, nastech_cli/proxy/adapters/nastech_portal.py, nastech_cli/setup.py, nastech_cli/setup_whatsapp_cloud.py, nastech_cli/skin_engine.py, nastech_cli/telegram_managed_bot.py, nastech_cli/tools_config.py, nastech_cli/uninstall.py, nastech_cli/update_cmd.py, nastech_cli/web_server.py, nastech_constants.py, package-lock.json, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/plugin.yaml, plugins/kanban/dashboard/dist/index.js, plugins/kanban/systemd/nastech-kanban-dispatcher.service, plugins/model-providers/ai-gateway/__init__.py, plugins/model-providers/fireworks/__init__.py, plugins/model-providers/kimi-coding/__init__.py, plugins/model-providers/nastech/__init__.py, plugins/model-providers/opencode-free/__init__.py, plugins/model-providers/opencode-zen/__init__.py, plugins/nastech-achievements/dashboard/dist/index.js, plugins/platforms/discord/adapter.py, plugins/platforms/email/adapter.py, plugins/platforms/photon/sidecar/package-lock.json, plugins/platforms/slack/adapter.py, run_agent.py, scripts/build_model_catalog.py, scripts/contributor_audit.py, scripts/dev-sandbox.sh, scripts/install.cmd, scripts/install.ps1, scripts/install.sh, scripts/release.py, scripts/whatsapp-bridge/package-lock.json, setup.py, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/references/background-systems.md, skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md, skills/autonomous-ai-agents/nastech-agent/references/configuration.md, skills/autonomous-ai-agents/nastech-agent/references/contributor-guide.md, skills/autonomous-ai-agents/nastech-agent/references/portal-auth-for-third-party-apps.md, skills/autonomous-ai-agents/nastech-agent/references/providers-and-models.md, skills/autonomous-ai-agents/nastech-agent/references/webhooks.md, tests/agent/test_anthropic_adapter.py, tests/agent/test_auxiliary_client.py, tests/agent/test_auxiliary_main_first.py, tests/agent/test_auxiliary_transport_autodetect.py, tests/agent/test_billing_links.py, tests/agent/test_credential_pool.py, tests/agent/test_credits_policy.py, tests/agent/test_error_classifier.py, tests/agent/test_model_metadata.py, tests/agent/test_nastech_credits_gauge.py, tests/agent/test_nastech_oauth_401_guidance.py, tests/agent/test_nastech_portal_anthropic_wire.py, tests/agent/test_phantom_tool_references.py, tests/agent/transports/test_chat_completions.py, tests/cli/test_cli_first_run_setup.py, tests/cli/test_cli_provider_resolution.py, tests/cli/test_show_config_credential.py, tests/docker/test_sqlite_runtime.py, tests/gateway/test_discord_format.py, tests/gateway/test_run_progress_topics.py, tests/gateway/test_status_command.py, tests/gateway/test_usage_command.py, tests/nastech_cli/test_auth_nastech_provider.py, tests/nastech_cli/test_base_url_host_identity.py, tests/nastech_cli/test_dashboard_auth_gate.py, tests/nastech_cli/test_dashboard_register.py, tests/nastech_cli/test_fireworks_provider.py, tests/nastech_cli/test_gateway_restart_loop.py, tests/nastech_cli/test_model_catalog.py, tests/nastech_cli/test_nastech_auth_keepalive.py, tests/nastech_cli/test_nastech_auth_status_cache.py, tests/nastech_cli/test_nastech_inference_url_validation.py, tests/nastech_cli/test_nastech_portal_staging_allowlist.py, tests/nastech_cli/test_nastech_reasoning_metadata.py, tests/nastech_cli/test_proxy.py, tests/nastech_cli/test_reasoning_caps_disk_cache.py, tests/nastech_cli/test_sale_pricing.py, tests/nastech_cli/test_web_oauth_dispatch.py, tests/plugins/dashboard_auth/test_nastech_provider.py, tests/plugins/image_gen/check_parity_vs_main.py, tests/plugins/image_gen/test_openrouter_compat_provider.py, tests/plugins/test_chronos_verify.py, tests/run_agent/test_anthropic_prompt_cache_policy.py, tests/run_agent/test_primary_runtime_restore.py, tests/run_agent/test_provider_attribution_headers.py, tests/run_agent/test_provider_fallback.py, tests/run_agent/test_provider_parity.py, tests/run_agent/test_run_agent.py, tests/run_agent/test_switch_model_reapplies_headers.py, tests/test_install_ps1_uv_powershell_host.py, tests/tools/test_delegate.py, tests/tools/test_managed_media_gateways.py, tests/tools/test_managed_tool_gateway.py, tests/tools/test_strict_provider_selection.py, tests/tools/test_tts_openai_config.py, tests/tools/test_url_safety.py, tests/tools/test_web_tools_config.py, tools/managed_tool_gateway.py, tools/mcp_oauth.py, tools/skills_hub.py, tools/skills_sync_client.py, trajectory_compressor.py, ui-tui/scripts/billing-fixtures.tsx, ui-tui/src/__tests__/subscriptionCommand.test.ts, ui-tui/src/__tests__/subscriptionOverlay.test.tsx, ui-tui/src/app/slash/commands/subscription.ts, ui-tui/src/domain/paths.ts, uv.lock, web/src/components/SidebarFooter.tsx, web/src/pages/DocsPage.tsx, web/src/pages/SystemPage.tsx, website/docs/developer-guide/contributing.md, website/docs/developer-guide/egress-internals.md, website/docs/getting-started/installation.md, website/docs/getting-started/platform-support.md, website/docs/getting-started/quickstart.md, website/docs/getting-started/termux.md, website/docs/guides/manage-nastech-cloud-with-mcp.md, website/docs/guides/run-nastech-with-nastech-portal.md, website/docs/guides/run-nemotron-3-ultra-free.md, website/docs/index.mdx, website/docs/integrations/nastech-portal.md, website/docs/integrations/providers.md, website/docs/reference/cli-commands.md, website/docs/reference/environment-variables.md, website/docs/reference/faq.md, website/docs/reference/model-catalog.md, website/docs/user-guide/desktop.md, website/docs/user-guide/egress/iron-proxy.md, website/docs/user-guide/features/browser.md, website/docs/user-guide/features/image-generation.md, website/docs/user-guide/features/skills.md, website/docs/user-guide/features/subscription-proxy.md, website/docs/user-guide/features/tool-gateway.md, website/docs/user-guide/features/tools.md, website/docs/user-guide/features/tts.md, website/docs/user-guide/features/web-dashboard.md, website/docs/user-guide/features/web-search.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/windows-wsl-quickstart.md, website/docusaurus.config.ts, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/contributing.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/quickstart.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-nastech-with-nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/index.mdx, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/providers.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/faq.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/model-catalog.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/subscription-proxy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tools.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tts.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-native.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-wsl-quickstart.md, website/scripts/generate-llms-txt.py, website/scripts/prebuild.mjs, website/static/api/model-catalog.json, website/static/oauth/client-metadata.json


## Direct upstream tree delta

- complete: +28 ~132 -0 ↪0
- MODIFIED `.env.example`
- MODIFIED `acp_adapter/tools.py`
- MODIFIED `agent/auxiliary_client.py`
- MODIFIED `agent/chat_completion_helpers.py`
- MODIFIED `agent/model_metadata.py`
- MODIFIED `agent/prompt_builder.py`
- MODIFIED `agent/prompt_caching.py`
- MODIFIED `agent/reasoning_effort.py`
- MODIFIED `agent/session_activity.py`
- ADDED `agent/side_question.py`
- MODIFIED `agent/system_prompt.py`
- MODIFIED `agent/transports/codex.py`
- MODIFIED `agent/vertex_adapter.py`
- MODIFIED `apps/desktop/src/app/chat/composer/status-stack/status-row.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/inline-preview-directive.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/markdown-text.media-md.test.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/markdown-text.tsx`
- MODIFIED `apps/desktop/src/components/chat/preview-attachment.tsx`
- MODIFIED `apps/desktop/src/components/ui/pane-tab.test.tsx`
- MODIFIED `apps/desktop/src/components/ui/pane-tab.tsx`
- MODIFIED `apps/desktop/src/lib/desktop-slash-commands.test.ts`
- MODIFIED `apps/desktop/src/lib/todos.test.ts`
- MODIFIED `apps/desktop/src/lib/todos.ts`
- MODIFIED `apps/desktop/src/store/composer-status.ts`
- MODIFIED `cli-config.yaml.example`
- MODIFIED `cli.py`
- ADDED `contributors/emails/1littlecoder@gmail.com`
- ADDED `contributors/emails/jack@powries.com`
- ADDED `contributors/emails/neel.patel@ramp.com`
- ADDED `contributors/emails/neel49@users.noreply.github.com`
- ADDED `contributors/emails/rafael.zendron22@gmail.com`
- ADDED `contributors/emails/sam@odio.email`
- MODIFIED `gateway/platforms/base.py`
- MODIFIED `gateway/platforms/yuanbao.py`
- MODIFIED `gateway/relay/command_manifest.py`
- MODIFIED `gateway/run.py`
- MODIFIED `gateway/slash_commands.py`
- MODIFIED `nastech_cli/auth.py`
- MODIFIED `nastech_cli/cli_commands_mixin.py`
- MODIFIED `nastech_cli/commands.py`
- MODIFIED `nastech_cli/config_defaults.py`
- MODIFIED `nastech_cli/doctor.py`
- MODIFIED `nastech_cli/gateway.py`
- MODIFIED `nastech_cli/main.py`
- MODIFIED `nastech_cli/model_normalize.py`
- MODIFIED `nastech_cli/models.py`
- MODIFIED `nastech_cli/providers.py`
- MODIFIED `nastech_cli/runtime_provider.py`
- MODIFIED `nastech_cli/setup.py`
- MODIFIED `nastech_cli/tips.py`
- MODIFIED `locales/af.yaml`
- MODIFIED `locales/ar.yaml`
- MODIFIED `locales/de.yaml`
- MODIFIED `locales/en.yaml`
- MODIFIED `locales/es.yaml`
- MODIFIED `locales/fr.yaml`
- MODIFIED `locales/ga.yaml`
- MODIFIED `locales/hu.yaml`
- MODIFIED `locales/it.yaml`
- MODIFIED `locales/ja.yaml`
- MODIFIED `locales/ko.yaml`
- MODIFIED `locales/pt.yaml`
- MODIFIED `locales/ru.yaml`
- MODIFIED `locales/tr.yaml`
- MODIFIED `locales/uk.yaml`
- MODIFIED `locales/zh-hant.yaml`
- MODIFIED `locales/zh.yaml`
- ADDED `optional-skills/devops/setup-wizard-generator/SKILL.md`
- ADDED `optional-skills/devops/setup-wizard-generator/templates/template.sh`
- ADDED `optional-skills/productivity/decision-questionnaire/SKILL.md`
- ADDED `optional-skills/software-development/grill-me/SKILL.md`
- ADDED `plugins/model-providers/nebius-token-factory/__init__.py`
- ADDED `plugins/model-providers/nebius-token-factory/plugin.yaml`
- ADDED `plugins/model-providers/router/__init__.py`
- ADDED `plugins/model-providers/router/plugin.yaml`
- MODIFIED `plugins/platforms/discord/adapter.py`
- MODIFIED `plugins/platforms/feishu/adapter.py`
- MODIFIED `plugins/platforms/telegram/adapter.py`
- MODIFIED `providers/README.md`
- MODIFIED `providers/base.py`
- MODIFIED `skills/autonomous-ai-agents/nastech-agent/references/slash-commands.md`
- MODIFIED `tests/agent/test_ghost_skill_pruning.py`
- MODIFIED `tests/agent/test_opencode_free_provider.py`
- MODIFIED `tests/agent/test_prompt_builder.py`
- MODIFIED `tests/agent/test_prompt_caching.py`
- ADDED `tests/agent/test_side_question.py`
- MODIFIED `tests/agent/test_skills_guidance_content_filter.py`
- MODIFIED `tests/agent/test_system_prompt.py`
- MODIFIED `tests/agent/test_vertex_adapter.py`
- ADDED `tests/agent/transports/test_router_codex_efforts.py`
- MODIFIED `tests/cli/test_cli_approval_ui.py`
- MODIFIED `tests/cli/test_cli_background_busy_path.py`
- MODIFIED `tests/gateway/test_background_command.py`
- ADDED `tests/gateway/test_busy_command.py`
- MODIFIED `tests/gateway/test_command_bypass_active_session.py`
- MODIFIED `tests/gateway/test_discord_slash_auth.py`
- MODIFIED `tests/gateway/test_gateway_command_dispatch_minimal.py`
- MODIFIED `tests/gateway/test_multiplex_background_task_scope.py`
- MODIFIED `tests/gateway/test_multiplex_busy_input_mode.py`
- MODIFIED `tests/gateway/test_session_hygiene.py`
- MODIFIED `tests/gateway/test_slash_access_dispatch.py`
- MODIFIED `tests/gateway/test_tts_media_routing.py`
- MODIFIED `tests/gateway/test_update_command.py`
- ADDED `tests/gateway/test_voice_transcode.py`
- MODIFIED `tests/nastech_cli/test_busy_policy_invariants.py`
- MODIFIED `tests/nastech_cli/test_commands.py`
- MODIFIED `tests/nastech_cli/test_gateway.py`
- ADDED `tests/nastech_cli/test_nebius_token_factory_provider.py`
- ADDED `tests/nastech_cli/test_opencode_free_live_catalog.py`
- MODIFIED `tests/nastech_cli/test_opencode_zen_free_keyless.py`
- ADDED `tests/nastech_cli/test_router_provider.py`
- MODIFIED `tests/nastech_cli/test_tencent_tokenhub_provider.py`
- MODIFIED `tests/providers/test_plugin_discovery.py`
- MODIFIED `tests/run_agent/test_steer.py`
- MODIFIED `tests/run_agent/test_streaming.py`
- ADDED `tests/skills/test_decision_questionnaire_skill.py`
- ADDED `tests/skills/test_setup_wizard_generator_skill.py`
- MODIFIED `tests/tools/test_skill_manage_batch.py`
- ADDED `tests/tools/test_todo_nested.py`
- MODIFIED `tools/skill_manager_tool.py`
- MODIFIED `tools/todo_tool.py`
- MODIFIED `tui_gateway/methods_prompt.py`
- MODIFIED `ui-tui/src/__tests__/slashParity.test.ts`
- MODIFIED `ui-tui/src/app/createGatewayEventHandler.ts`
- MODIFIED `ui-tui/src/app/slash/commands/session.ts`
- MODIFIED `ui-tui/src/gatewayTypes.ts`
- MODIFIED `website/docs/developer-guide/adding-providers.md`
- MODIFIED `website/docs/getting-started/quickstart.md`
- MODIFIED `website/docs/integrations/providers.md`
- MODIFIED `website/docs/reference/cli-commands.md`
- MODIFIED `website/docs/reference/cli-symbols.md`
- MODIFIED `website/docs/reference/environment-variables.md`
- MODIFIED `website/docs/reference/optional-skills-catalog.md`
- MODIFIED `website/docs/reference/slash-commands.md`
- MODIFIED `website/docs/reference/tools-reference.md`
- MODIFIED `website/docs/user-guide/cli.md`
- MODIFIED `website/docs/user-guide/configuration.md`
- MODIFIED `website/docs/user-guide/features/fallback-providers.md`
- MODIFIED `website/docs/user-guide/messaging/discord.md`
- MODIFIED `website/docs/user-guide/messaging/index.md`
- MODIFIED `website/docs/user-guide/messaging/matrix.md`
- MODIFIED `website/docs/user-guide/messaging/slack.md`
- MODIFIED `website/docs/user-guide/messaging/telegram.md`
- MODIFIED `website/docs/user-guide/messaging/yuanbao.md`
- ADDED `website/docs/user-guide/skills/optional/devops/devops-setup-wizard-generator.md`
- ADDED `website/docs/user-guide/skills/optional/productivity/productivity-decision-questionnaire.md`
- ADDED `website/docs/user-guide/skills/optional/software-development/software-development-grill-me.md`
- MODIFIED `website/docs/user-guide/tui.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/slash-commands.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/cli.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/messaging/discord.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/messaging/index.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/messaging/slack.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/messaging/telegram.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/messaging/yuanbao.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/tui.md`
- MODIFIED `website/sidebars.ts`
- MODIFIED `website/src/data/userStories.json`

## Scan

10720 files scanned [audio=5, binary=7, doc=5, font=13, image=92, text=10598]


## Diff

1406 renamed, 0 rewritten, 8913 identical, 61 locked, 0 missing, 34 owned, 252 reconciled


## Fork check (vs nastech-agent)

- 10403 identical, 289 updated (+0/-0 lines), 28 added, 0 missing, 0 fork-local-unpreserved, 0 stale-upstream, 0 locked/binary, 0 collision-safe relocated, 54 preserved fork-local files, 0 violations

- features: fork 51 -> branded 51

Auto-generated by 100Ways.
