# Nastech Update Report #1

- upstream sha : `26350357d76e4508c8df9304a3374bdc5a6f6220`
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

- total files : 10707
- renamed     : 1495 (folders and file names)
- text-rewritten : 10609
- locked-copied  : 56
- binary-copied  : 8
- owned assets   : 34 (our logo/banner/mascot override upstream)

## Reconcile

- fixed : 260 files reconciled: .github/workflows/deploy-site.yml, .github/workflows/deploy-site.yml, .github/workflows/skills-index-freshness.yml, .mailmap, CONTRIBUTING.es.md, CONTRIBUTING.md, Dockerfile, README.es.md, README.md, README.ur-pk.md, README.zh-CN.md, SECURITY.es.md, SECURITY.md, agent/agent_runtime_helpers.py, agent/anthropic_adapter.py, agent/anthropic_endpoints.py, agent/auxiliary_client.py, agent/billing_links.py, agent/billing_view.py, agent/chat_completion_helpers.py, agent/conversation_loop.py, agent/credits_tracker.py, agent/model_metadata.py, agent/prompt_builder.py, agent/proxy_sources/iron_proxy.py, agent/subscription_view.py, agent/usage_pricing.py, apps/bootstrap-installer/src-tauri/Cargo.toml, apps/desktop/README.md, apps/desktop/electron/backend-health.test.ts, apps/desktop/electron/backend-health.ts, apps/desktop/electron/connection-config.test.ts, apps/desktop/electron/main.ts, apps/desktop/electron/oauth-partition.test.ts, apps/desktop/electron/remote-lifecycle.ts, apps/desktop/package.json, apps/desktop/src/app/messaging/index.test.tsx, apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx, apps/desktop/src/app/settings/about-settings.tsx, apps/desktop/src/app/settings/billing/api.test.ts, apps/desktop/src/app/settings/billing/dev-fixtures.ts, apps/desktop/src/app/settings/billing/errors.test.ts, apps/desktop/src/app/settings/billing/types.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.ts, apps/desktop/src/app/settings/billing/use-charge-poller.test.ts, apps/desktop/src/app/settings/billing/use-step-up.test.tsx, apps/desktop/src/app/settings/constants.ts, apps/desktop/src/app/settings/gateway-settings.tsx, apps/desktop/src/app/settings/toolset-config-panel.test.tsx, apps/desktop/src/app/skills/embedded-hub-picker.tsx, apps/desktop/src/app/skills/index.test.tsx, apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts, apps/desktop/src/components/boot-failure-overlay.test.tsx, apps/desktop/src/components/boot-failure-overlay.tsx, apps/desktop/src/components/send-diagnostics-dialog.tsx, apps/desktop/src/contrib/plugin.ts, apps/desktop/src/i18n/en.ts, apps/desktop/src/i18n/ja.ts, apps/desktop/src/i18n/zh-hant.ts, apps/desktop/src/i18n/zh.ts, apps/desktop/src/plugins/nastech-bots/skills-hub-picker.test.tsx, apps/desktop/src/plugins/nastech-bots/skills-hub.tsx, apps/desktop/src/sdk/index.ts, cli-config.yaml.example, eslint.config.shared.mjs, evals/browser_use/single_run.py, nastech_cli/auth.py, nastech_cli/banner.py, nastech_cli/config_defaults.py, nastech_cli/dashboard_auth/login_page.py, nastech_cli/dashboard_register.py, nastech_cli/debug.py, nastech_cli/diagnostics_upload.py, nastech_cli/fallback_cmd.py, nastech_cli/kanban.py, nastech_cli/main.py, nastech_cli/model_catalog.py, nastech_cli/model_switch.py, nastech_cli/models.py, nastech_cli/nastech_account.py, nastech_cli/nastech_billing.py, nastech_cli/plugins_cmd.py, nastech_cli/portal_cli.py, nastech_cli/providers.py, nastech_cli/proxy/__init__.py, nastech_cli/proxy/adapters/base.py, nastech_cli/proxy/adapters/nastech_portal.py, nastech_cli/setup.py, nastech_cli/setup_whatsapp_cloud.py, nastech_cli/skin_engine.py, nastech_cli/telegram_managed_bot.py, nastech_cli/tools_config.py, nastech_cli/uninstall.py, nastech_cli/update_cmd.py, nastech_cli/web_server.py, nastech_constants.py, package-lock.json, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/plugin.yaml, plugins/kanban/dashboard/dist/index.js, plugins/kanban/systemd/nastech-kanban-dispatcher.service, plugins/model-providers/ai-gateway/__init__.py, plugins/model-providers/fireworks/__init__.py, plugins/model-providers/kimi-coding/__init__.py, plugins/model-providers/nastech/__init__.py, plugins/model-providers/opencode-free/__init__.py, plugins/model-providers/opencode-zen/__init__.py, plugins/nastech-achievements/dashboard/dist/index.js, plugins/platforms/discord/adapter.py, plugins/platforms/email/adapter.py, plugins/platforms/photon/sidecar/package-lock.json, plugins/platforms/slack/adapter.py, run_agent.py, scripts/build_model_catalog.py, scripts/contributor_audit.py, scripts/dev-sandbox.sh, scripts/install.cmd, scripts/install.ps1, scripts/install.sh, scripts/release.py, scripts/whatsapp-bridge/package-lock.json, setup.py, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/references/background-systems.md, skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md, skills/autonomous-ai-agents/nastech-agent/references/configuration.md, skills/autonomous-ai-agents/nastech-agent/references/contributor-guide.md, skills/autonomous-ai-agents/nastech-agent/references/portal-auth-for-third-party-apps.md, skills/autonomous-ai-agents/nastech-agent/references/providers-and-models.md, skills/autonomous-ai-agents/nastech-agent/references/webhooks.md, tests/agent/test_anthropic_adapter.py, tests/agent/test_auxiliary_client.py, tests/agent/test_auxiliary_main_first.py, tests/agent/test_auxiliary_transport_autodetect.py, tests/agent/test_billing_links.py, tests/agent/test_credential_pool.py, tests/agent/test_credits_policy.py, tests/agent/test_error_classifier.py, tests/agent/test_model_metadata.py, tests/agent/test_nastech_credits_gauge.py, tests/agent/test_nastech_oauth_401_guidance.py, tests/agent/test_nastech_portal_anthropic_wire.py, tests/agent/test_phantom_tool_references.py, tests/agent/transports/test_chat_completions.py, tests/cli/test_cli_first_run_setup.py, tests/cli/test_cli_provider_resolution.py, tests/cli/test_show_config_credential.py, tests/docker/test_sqlite_runtime.py, tests/gateway/test_discord_format.py, tests/gateway/test_run_progress_topics.py, tests/gateway/test_status_command.py, tests/gateway/test_usage_command.py, tests/nastech_cli/test_auth_nastech_provider.py, tests/nastech_cli/test_base_url_host_identity.py, tests/nastech_cli/test_dashboard_auth_gate.py, tests/nastech_cli/test_dashboard_register.py, tests/nastech_cli/test_fireworks_provider.py, tests/nastech_cli/test_gateway_restart_loop.py, tests/nastech_cli/test_model_catalog.py, tests/nastech_cli/test_model_validation.py, tests/nastech_cli/test_nastech_auth_keepalive.py, tests/nastech_cli/test_nastech_auth_status_cache.py, tests/nastech_cli/test_nastech_inference_url_validation.py, tests/nastech_cli/test_nastech_portal_staging_allowlist.py, tests/nastech_cli/test_nastech_reasoning_metadata.py, tests/nastech_cli/test_proxy.py, tests/nastech_cli/test_reasoning_caps_disk_cache.py, tests/nastech_cli/test_sale_pricing.py, tests/nastech_cli/test_web_oauth_dispatch.py, tests/plugins/dashboard_auth/test_nastech_provider.py, tests/plugins/image_gen/check_parity_vs_main.py, tests/plugins/image_gen/test_openrouter_compat_provider.py, tests/plugins/test_chronos_verify.py, tests/run_agent/test_anthropic_prompt_cache_policy.py, tests/run_agent/test_primary_runtime_restore.py, tests/run_agent/test_provider_attribution_headers.py, tests/run_agent/test_provider_fallback.py, tests/run_agent/test_provider_parity.py, tests/run_agent/test_run_agent.py, tests/run_agent/test_switch_model_reapplies_headers.py, tests/test_install_ps1_uv_powershell_host.py, tests/tools/test_delegate.py, tests/tools/test_managed_media_gateways.py, tests/tools/test_managed_tool_gateway.py, tests/tools/test_strict_provider_selection.py, tests/tools/test_tts_openai_config.py, tests/tools/test_url_safety.py, tests/tools/test_web_tools_config.py, tools/managed_tool_gateway.py, tools/mcp_oauth.py, tools/skills_hub.py, tools/skills_sync_client.py, trajectory_compressor.py, ui-tui/scripts/billing-fixtures.tsx, ui-tui/src/__tests__/subscriptionCommand.test.ts, ui-tui/src/__tests__/subscriptionOverlay.test.tsx, ui-tui/src/app/slash/commands/subscription.ts, ui-tui/src/domain/paths.ts, uv.lock, web/src/components/SidebarFooter.tsx, web/src/pages/DocsPage.tsx, web/src/pages/SystemPage.tsx, website/docs/developer-guide/contributing.md, website/docs/developer-guide/egress-internals.md, website/docs/getting-started/installation.md, website/docs/getting-started/platform-support.md, website/docs/getting-started/quickstart.md, website/docs/getting-started/termux.md, website/docs/guides/manage-nastech-cloud-with-mcp.md, website/docs/guides/run-nastech-with-nastech-portal.md, website/docs/guides/run-nemotron-3-ultra-free.md, website/docs/index.mdx, website/docs/integrations/nastech-portal.md, website/docs/integrations/providers.md, website/docs/reference/cli-commands.md, website/docs/reference/environment-variables.md, website/docs/reference/faq.md, website/docs/reference/model-catalog.md, website/docs/user-guide/desktop.md, website/docs/user-guide/egress/iron-proxy.md, website/docs/user-guide/features/browser.md, website/docs/user-guide/features/image-generation.md, website/docs/user-guide/features/skills.md, website/docs/user-guide/features/subscription-proxy.md, website/docs/user-guide/features/tool-gateway.md, website/docs/user-guide/features/tools.md, website/docs/user-guide/features/tts.md, website/docs/user-guide/features/web-dashboard.md, website/docs/user-guide/features/web-search.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/windows-wsl-quickstart.md, website/docusaurus.config.ts, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/contributing.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/quickstart.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-nastech-with-nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/index.mdx, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/providers.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/faq.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/model-catalog.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/subscription-proxy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tools.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tts.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-native.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-wsl-quickstart.md, website/scripts/generate-llms-txt.py, website/scripts/prebuild.mjs, website/static/api/model-catalog.json, website/static/oauth/client-metadata.json


## Direct upstream tree delta

- complete: +45 ~216 -4 ↪0
- MODIFIED `agent/agent_init.py`
- MODIFIED `agent/agent_runtime_helpers.py`
- MODIFIED `agent/anthropic_adapter.py`
- ADDED `agent/anthropic_credentials.py`
- ADDED `agent/anthropic_endpoints.py`
- ADDED `agent/anthropic_message_convert.py`
- MODIFIED `agent/auxiliary_client.py`
- MODIFIED `agent/background_review.py`
- MODIFIED `agent/chat_completion_helpers.py`
- MODIFIED `agent/conversation_compression.py`
- MODIFIED `agent/conversation_loop.py`
- MODIFIED `agent/credential_persistence.py`
- MODIFIED `agent/credential_pool.py`
- ADDED `agent/plan_prompt.py`
- MODIFIED `agent/side_question.py`
- MODIFIED `apps/desktop/electron/main.ts`
- ADDED `apps/desktop/electron/mcp-oauth-callback-ipc.test.ts`
- ADDED `apps/desktop/electron/mcp-oauth-callback-ipc.ts`
- MODIFIED `apps/desktop/electron/preload.ts`
- MODIFIED `apps/desktop/src/api/config.ts`
- MODIFIED `apps/desktop/src/app/chat/composer/status-stack/collapsed-indicator.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/gateway-event/tools.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/index.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/todo-cleanup.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-actions/index.ts`
- ADDED `apps/desktop/src/app/settings/browser-real-profile-panel.test.tsx`
- ADDED `apps/desktop/src/app/settings/browser-real-profile-panel.tsx`
- MODIFIED `apps/desktop/src/app/settings/constants.ts`
- MODIFIED `apps/desktop/src/app/skills/index.tsx`
- MODIFIED `apps/desktop/src/components/chat/status-section.tsx`
- MODIFIED `apps/desktop/src/global.d.ts`
- MODIFIED `apps/desktop/src/i18n/en.ts`
- MODIFIED `apps/desktop/src/i18n/ja.ts`
- MODIFIED `apps/desktop/src/i18n/types.ts`
- MODIFIED `apps/desktop/src/i18n/zh-hant.ts`
- MODIFIED `apps/desktop/src/i18n/zh.ts`
- MODIFIED `apps/desktop/src/lib/chat-messages/types.ts`
- MODIFIED `apps/desktop/src/lib/todos.test.ts`
- MODIFIED `apps/desktop/src/lib/todos.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/mcp-setup.tsx`
- ADDED `apps/desktop/src/plugins/nastech-bots/relay-deliver-budget.test.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/relay.ts`
- MODIFIED `apps/desktop/src/sdk/index.ts`
- MODIFIED `apps/desktop/src/sdk/profile-routing.test.ts`
- MODIFIED `apps/desktop/src/store/todos.test.ts`
- MODIFIED `apps/desktop/src/store/todos.ts`
- MODIFIED `apps/desktop/src/types/nastech.ts`
- MODIFIED `apps/shared/src/json-rpc-gateway.ts`
- MODIFIED `cli-config.yaml.example`
- MODIFIED `cli.py`
- ADDED `contributors/emails/Cheri8014@163.com`
- ADDED `contributors/emails/abtion@outlook.com`
- ADDED `contributors/emails/adamfortuna1324@gmail.com`
- ADDED `contributors/emails/brin@shadewaterlabs.com`
- ADDED `contributors/emails/bsbofmusic@users.noreply.github.com`
- ADDED `contributors/emails/fabiantax@hotmail.com`
- ADDED `contributors/emails/fidiasfeliciano@MacBook-Pro.local`
- ADDED `contributors/emails/icocode@users.noreply.github.com`
- ADDED `contributors/emails/jason@runninwithitmarketing.com`
- ADDED `contributors/emails/salch-cred@users.noreply.github.com`
- ADDED `contributors/emails/yu_zhengbo@foxmail.com`
- ADDED `contributors/emails/zane.chee.2023@scis.smu.edu.sg`
- MODIFIED `cron/jobs.py`
- MODIFIED `cron/scheduler.py`
- MODIFIED `docker/SOUL.md`
- MODIFIED `gateway/relay/adapter.py`
- MODIFIED `gateway/run.py`
- MODIFIED `gateway/slash_commands.py`
- MODIFIED `nastech_cli/auth.py`
- MODIFIED `nastech_cli/browser_connect.py`
- MODIFIED `nastech_cli/cli_commands_mixin.py`
- MODIFIED `nastech_cli/commands.py`
- MODIFIED `nastech_cli/config_defaults.py`
- MODIFIED `nastech_cli/default_soul.py`
- MODIFIED `nastech_cli/loops.py`
- MODIFIED `nastech_cli/main.py`
- MODIFIED `nastech_cli/model_switch.py`
- MODIFIED `nastech_cli/models.py`
- MODIFIED `nastech_cli/skills_hub.py`
- MODIFIED `nastech_cli/tips.py`
- MODIFIED `nastech_cli/web_server.py`
- MODIFIED `nastech_state.py`
- ADDED `optional-skills/creative/impeccable/SKILL.md`
- MODIFIED `optional-skills/software-development/grill-me/SKILL.md`
- MODIFIED `optional-skills/software-development/subagent-driven-development/SKILL.md`
- MODIFIED `plugins/memory/mem0/README.md`
- MODIFIED `plugins/memory/mem0/_backend.py`
- ADDED `plugins/memory/mem0/_openai_llm.py`
- MODIFIED `plugins/memory/mem0/_setup.py`
- MODIFIED `plugins/model-providers/alibaba-coding-plan/__init__.py`
- MODIFIED `plugins/model-providers/alibaba/__init__.py`
- MODIFIED `plugins/model-providers/custom/__init__.py`
- MODIFIED `plugins/platforms/discord/adapter.py`
- MODIFIED `plugins/platforms/telegram/adapter.py`
- ADDED `plugins/platforms/telegram/inline_picker.py`
- MODIFIED `run_agent.py`
- MODIFIED `scripts/install.ps1`
- MODIFIED `scripts/install.sh`
- MODIFIED `skills/autonomous-ai-agents/computer-use/SKILL.md`
- MODIFIED `skills/autonomous-ai-agents/nastech-agent/references/slash-commands.md`
- MODIFIED `skills/research/research-paper-writing/SKILL.md`
- MODIFIED `skills/software-development/nastech-agent-skill-authoring/SKILL.md`
- DELETED `skills/software-development/plan/SKILL.md`
- MODIFIED `skills/software-development/requesting-code-review/SKILL.md`
- MODIFIED `skills/software-development/simplify-code/SKILL.md`
- MODIFIED `skills/software-development/spike/SKILL.md`
- MODIFIED `skills/software-development/systematic-debugging/SKILL.md`
- MODIFIED `skills/software-development/test-driven-development/SKILL.md`
- MODIFIED `tests/agent/test_anthropic_adapter.py`
- ADDED `tests/agent/test_anthropic_borrowed_row_authority.py`
- ADDED `tests/agent/test_anthropic_credential_persist_failure.py`
- MODIFIED `tests/agent/test_anthropic_keychain.py`
- ADDED `tests/agent/test_anthropic_oauth_stress.py`
- ADDED `tests/agent/test_anthropic_spent_rotation_verdict.py`
- MODIFIED `tests/agent/test_anthropic_token_scope_isolation.py`
- MODIFIED `tests/agent/test_auxiliary_client.py`
- MODIFIED `tests/agent/test_compression_rotation_state.py`
- MODIFIED `tests/agent/test_credential_pool.py`
- ADDED `tests/agent/test_credential_pool_anthropic_refresh_race.py`
- MODIFIED `tests/agent/test_credential_pool_oat_authtype.py`
- MODIFIED `tests/agent/test_credential_pool_oauth_writethrough.py`
- MODIFIED `tests/agent/test_curator.py`
- ADDED `tests/agent/test_plan_prompt.py`
- MODIFIED `tests/agent/test_side_question.py`
- MODIFIED `tests/agent/test_skill_todo_retention_parity.py`
- ADDED `tests/agent/test_switch_model_request_overrides.py`
- MODIFIED `tests/agent/transports/test_chat_completions.py`
- MODIFIED `tests/cli/test_cli_background_status_indicator.py`
- MODIFIED `tests/cli/test_cli_browser_connect.py`
- MODIFIED `tests/cli/test_cli_status_bar.py`
- ADDED `tests/cli/test_handoff_slow_dispatch_timeout.py`
- MODIFIED `tests/conftest.py`
- MODIFIED `tests/cron/test_claim_job_for_fire.py`
- ADDED `tests/cron/test_cron_request_overrides.py`
- MODIFIED `tests/cron/test_jobs.py`
- MODIFIED `tests/cron/test_oneshot_dispatch_failure_run_claim.py`
- MODIFIED `tests/cron/test_terminal_job_rearm.py`
- MODIFIED `tests/gateway/relay/test_relay_slack_unfurl.py`
- ADDED `tests/gateway/test_custom_provider_request_overrides.py`
- MODIFIED `tests/gateway/test_gateway_platform_event_hook.py`
- ADDED `tests/gateway/test_model_command_request_overrides.py`
- MODIFIED `tests/gateway/test_telegram_channel_posts.py`
- ADDED `tests/gateway/test_telegram_inline_picker.py`
- MODIFIED `tests/gateway/test_telegram_lazy_install_typehandler.py`
- MODIFIED `tests/gateway/test_telegram_network_reconnect.py`
- MODIFIED `tests/gateway/test_telegram_status_update.py`
- MODIFIED `tests/gateway/test_telegram_thread_fallback.py`
- MODIFIED `tests/gateway/test_telegram_username_chat_id.py`
- ADDED `tests/gateway/test_turn_request_overrides.py`
- MODIFIED `tests/nastech_cli/test_api_key_providers.py`
- ADDED `tests/nastech_cli/test_auth_store_lock_concurrent.py`
- MODIFIED `tests/nastech_cli/test_browser_connect_default_chromium.py`
- MODIFIED `tests/nastech_cli/test_commands.py`
- MODIFIED `tests/nastech_cli/test_config.py`
- MODIFIED `tests/nastech_cli/test_curator_pin_visibility.py`
- MODIFIED `tests/nastech_cli/test_loops.py`
- MODIFIED `tests/nastech_cli/test_model_validation.py`
- MODIFIED `tests/nastech_cli/test_web_oauth_dispatch.py`
- MODIFIED `tests/nastech_cli/test_web_server_cron_profiles.py`
- DELETED `tests/nastech_cli/test_web_server_oauth_write.py`
- MODIFIED `tests/plugins/memory/test_mem0_backend.py`
- ADDED `tests/plugins/memory/test_mem0_backend_integration.py`
- MODIFIED `tests/plugins/memory/test_mem0_setup.py`
- MODIFIED `tests/plugins/model_providers/test_custom_profile.py`
- MODIFIED `tests/providers/test_provider_profiles.py`
- MODIFIED `tests/providers/test_transport_parity.py`
- MODIFIED `tests/run_agent/test_background_review_toolset_restriction.py`
- MODIFIED `tests/run_agent/test_codex_app_server_compaction.py`
- MODIFIED `tests/run_agent/test_primary_runtime_restore.py`
- MODIFIED `tests/run_agent/test_provider_fallback.py`
- MODIFIED `tests/run_agent/test_run_agent.py`
- MODIFIED `tests/test_hermetic_side_effect_guards.py`
- MODIFIED `tests/test_timezone.py`
- MODIFIED `tests/test_tui_gateway_server.py`
- MODIFIED `tests/tools/test_browser_real_profile.py`
- ADDED `tests/tools/test_browser_real_profile_pin.py`
- MODIFIED `tests/tools/test_computer_use_cua_0_10_permissions.py`
- MODIFIED `tests/tools/test_cronjob_tools.py`
- MODIFIED `tests/tools/test_delegate.py`
- ADDED `tests/tools/test_delegate_request_overrides.py`
- MODIFIED `tests/tools/test_setup_mcp_tool.py`
- MODIFIED `tests/tools/test_skill_bundle_provenance.py`
- MODIFIED `tests/tools/test_skill_usage.py`
- MODIFIED `tests/tools/test_skills_hub.py`
- MODIFIED `tests/tools/test_subprocess_stdin_guard.py`
- MODIFIED `tests/tools/test_threat_patterns.py`
- MODIFIED `tests/tools/test_todo_tool.py`
- MODIFIED `tests/tui_gateway/test_loop_command.py`
- ADDED `tests/tui_gateway/test_mcp_oauth_client_callback.py`
- ADDED `tests/tui_gateway/test_todo_state_events.py`
- MODIFIED `tools/browser_tool.py`
- MODIFIED `tools/computer_use/cua_backend.py`
- MODIFIED `tools/cronjob_tools.py`
- MODIFIED `tools/delegate_tool.py`
- MODIFIED `tools/file_tools.py`
- MODIFIED `tools/setup_mcp_tool.py`
- MODIFIED `tools/skill_usage.py`
- MODIFIED `tools/skills_guard.py`
- MODIFIED `tools/skills_hub.py`
- MODIFIED `tools/threat_patterns.py`
- MODIFIED `tools/todo_tool.py`
- MODIFIED `tui_gateway/mcp_oauth_sessions.py`
- MODIFIED `tui_gateway/methods_prompt.py`
- MODIFIED `tui_gateway/methods_session.py`
- MODIFIED `tui_gateway/methods_tools.py`
- MODIFIED `tui_gateway/server.py`
- MODIFIED `ui-tui/README.md`
- MODIFIED `ui-tui/src/__tests__/appChromeStatusRule.test.tsx`
- MODIFIED `ui-tui/src/__tests__/statusRule.test.ts`
- ADDED `ui-tui/src/__tests__/turnControllerTodos.test.ts`
- MODIFIED `ui-tui/src/app/interfaces.ts`
- MODIFIED `ui-tui/src/app/turnController.ts`
- MODIFIED `ui-tui/src/app/uiStore.ts`
- MODIFIED `ui-tui/src/app/useConfigSync.ts`
- MODIFIED `ui-tui/src/components/appChrome.tsx`
- MODIFIED `ui-tui/src/components/appLayout.tsx`
- MODIFIED `ui-tui/src/components/todoPanel.tsx`
- MODIFIED `ui-tui/src/gatewayTypes.ts`
- MODIFIED `ui-tui/src/lib/todo.test.ts`
- MODIFIED `ui-tui/src/lib/todo.ts`
- MODIFIED `ui-tui/src/types.ts`
- MODIFIED `web/src/lib/api.test.ts`
- MODIFIED `web/src/lib/api.ts`
- MODIFIED `website/docs/developer-guide/prompt-assembly.md`
- MODIFIED `website/docs/integrations/providers.md`
- MODIFIED `website/docs/reference/cli-commands.md`
- MODIFIED `website/docs/reference/environment-variables.md`
- MODIFIED `website/docs/reference/optional-skills-catalog.md`
- MODIFIED `website/docs/reference/skills-catalog.md`
- MODIFIED `website/docs/reference/slash-commands.md`
- MODIFIED `website/docs/user-guide/configuration.md`
- MODIFIED `website/docs/user-guide/features/browser.md`
- MODIFIED `website/docs/user-guide/features/computer-use.md`
- MODIFIED `website/docs/user-guide/features/cron.md`
- MODIFIED `website/docs/user-guide/features/curator.md`
- MODIFIED `website/docs/user-guide/features/delegation.md`
- MODIFIED `website/docs/user-guide/features/loops.md`
- MODIFIED `website/docs/user-guide/features/mcp.md`
- MODIFIED `website/docs/user-guide/features/memory.md`
- MODIFIED `website/docs/user-guide/features/personality.md`
- MODIFIED `website/docs/user-guide/features/skills.md`
- MODIFIED `website/docs/user-guide/messaging/telegram.md`
- MODIFIED `website/docs/user-guide/sessions.md`
- MODIFIED `website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-computer-use.md`
- MODIFIED `website/docs/user-guide/skills/bundled/research/research-research-paper-writing.md`
- MODIFIED `website/docs/user-guide/skills/bundled/software-development/software-development-nastech-agent-skill-authoring.md`
- DELETED `website/docs/user-guide/skills/bundled/software-development/software-development-plan.md`
- MODIFIED `website/docs/user-guide/skills/bundled/software-development/software-development-requesting-code-review.md`
- MODIFIED `website/docs/user-guide/skills/bundled/software-development/software-development-simplify-code.md`
- MODIFIED `website/docs/user-guide/skills/bundled/software-development/software-development-spike.md`
- MODIFIED `website/docs/user-guide/skills/bundled/software-development/software-development-systematic-debugging.md`
- MODIFIED `website/docs/user-guide/skills/bundled/software-development/software-development-test-driven-development.md`
- ADDED `website/docs/user-guide/skills/optional/creative/creative-impeccable.md`
- MODIFIED `website/docs/user-guide/skills/optional/software-development/software-development-grill-me.md`
- MODIFIED `website/docs/user-guide/skills/optional/software-development/software-development-subagent-driven-development.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/prompt-assembly.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/skills-catalog.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/slash-commands.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/personality.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/skills.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/research/research-research-paper-writing.md`
- DELETED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/software-development/software-development-plan.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/software-development/software-development-spike.md`
- MODIFIED `website/sidebars.ts`

## Scan

10761 files scanned [audio=5, binary=7, doc=5, font=13, image=92, text=10639]


## Diff

1406 renamed, 0 rewritten, 8952 identical, 61 locked, 0 missing, 34 owned, 254 reconciled


## Fork check (vs nastech-agent)

- 10353 identical, 363 updated (+0/-0 lines), 45 added, 0 missing, 0 fork-local-unpreserved, 0 stale-upstream, 0 locked/binary, 0 collision-safe relocated, 54 preserved fork-local files, 0 violations

- features: fork 51 -> branded 51

Auto-generated by 100Ways.
