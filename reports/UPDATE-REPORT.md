# Nastech Update Report #1

- upstream sha : `7cd91114b462b7af76e558cc4e97f82201d2e884`
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

- total files : 11040
- renamed     : 1538 (folders and file names)
- text-rewritten : 10942
- locked-copied  : 56
- binary-copied  : 8
- owned assets   : 34 (our logo/banner/mascot override upstream)

## Reconcile

- fixed : 261 files reconciled: .github/workflows/deploy-site.yml, .github/workflows/deploy-site.yml, .github/workflows/skills-index-freshness.yml, .mailmap, CONTRIBUTING.es.md, CONTRIBUTING.md, Dockerfile, README.es.md, README.md, README.ur-pk.md, README.zh-CN.md, SECURITY.es.md, SECURITY.md, agent/agent_runtime_helpers.py, agent/anthropic_adapter.py, agent/anthropic_endpoints.py, agent/auxiliary_client.py, agent/billing_links.py, agent/billing_view.py, agent/chat_completion_helpers.py, agent/conversation_loop.py, agent/credits_tracker.py, agent/model_metadata.py, agent/prompt_builder.py, agent/proxy_sources/iron_proxy.py, agent/subscription_view.py, agent/usage_pricing.py, apps/bootstrap-installer/src-tauri/Cargo.toml, apps/desktop/README.md, apps/desktop/electron/backend-health.test.ts, apps/desktop/electron/backend-health.ts, apps/desktop/electron/connection-config.test.ts, apps/desktop/electron/main.ts, apps/desktop/electron/oauth-partition.test.ts, apps/desktop/electron/remote-lifecycle.ts, apps/desktop/package.json, apps/desktop/src/app/messaging/index.test.tsx, apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx, apps/desktop/src/app/settings/about-settings.tsx, apps/desktop/src/app/settings/billing/api.test.ts, apps/desktop/src/app/settings/billing/dev-fixtures.ts, apps/desktop/src/app/settings/billing/errors.test.ts, apps/desktop/src/app/settings/billing/types.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.ts, apps/desktop/src/app/settings/billing/use-charge-poller.test.ts, apps/desktop/src/app/settings/billing/use-step-up.test.tsx, apps/desktop/src/app/settings/constants.ts, apps/desktop/src/app/settings/gateway-settings.tsx, apps/desktop/src/app/settings/toolset-config-panel.test.tsx, apps/desktop/src/app/skills/embedded-hub-picker.tsx, apps/desktop/src/app/skills/index.test.tsx, apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts, apps/desktop/src/components/boot-failure-overlay.test.tsx, apps/desktop/src/components/boot-failure-overlay.tsx, apps/desktop/src/components/send-diagnostics-dialog.tsx, apps/desktop/src/contrib/plugin.ts, apps/desktop/src/i18n/en.ts, apps/desktop/src/i18n/ja.ts, apps/desktop/src/i18n/ru.ts, apps/desktop/src/i18n/zh-hant.ts, apps/desktop/src/i18n/zh.ts, apps/desktop/src/plugins/nastech-bots/skills-hub-picker.test.tsx, apps/desktop/src/plugins/nastech-bots/skills-hub.tsx, apps/desktop/src/sdk/index.ts, cli-config.yaml.example, eslint.config.shared.mjs, evals/browser_use/single_run.py, nastech_cli/auth.py, nastech_cli/banner.py, nastech_cli/config_defaults.py, nastech_cli/dashboard_auth/login_page.py, nastech_cli/dashboard_register.py, nastech_cli/debug.py, nastech_cli/diagnostics_upload.py, nastech_cli/fallback_cmd.py, nastech_cli/kanban.py, nastech_cli/main.py, nastech_cli/model_catalog.py, nastech_cli/model_switch.py, nastech_cli/models.py, nastech_cli/nastech_account.py, nastech_cli/nastech_billing.py, nastech_cli/plugins_cmd.py, nastech_cli/portal_cli.py, nastech_cli/providers.py, nastech_cli/proxy/__init__.py, nastech_cli/proxy/adapters/base.py, nastech_cli/proxy/adapters/nastech_portal.py, nastech_cli/setup.py, nastech_cli/setup_whatsapp_cloud.py, nastech_cli/skin_engine.py, nastech_cli/telegram_managed_bot.py, nastech_cli/tools_config.py, nastech_cli/uninstall.py, nastech_cli/update_cmd.py, nastech_cli/web_server.py, nastech_constants.py, package-lock.json, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/plugin.yaml, plugins/kanban/dashboard/dist/index.js, plugins/kanban/systemd/nastech-kanban-dispatcher.service, plugins/model-providers/ai-gateway/__init__.py, plugins/model-providers/fireworks/__init__.py, plugins/model-providers/kimi-coding/__init__.py, plugins/model-providers/nastech/__init__.py, plugins/model-providers/opencode-free/__init__.py, plugins/model-providers/opencode-zen/__init__.py, plugins/nastech-achievements/dashboard/dist/index.js, plugins/platforms/discord/adapter.py, plugins/platforms/email/adapter.py, plugins/platforms/photon/sidecar/package-lock.json, plugins/platforms/slack/adapter.py, run_agent.py, scripts/build_model_catalog.py, scripts/contributor_audit.py, scripts/dev-sandbox.sh, scripts/install.cmd, scripts/install.ps1, scripts/install.sh, scripts/release.py, scripts/whatsapp-bridge/package-lock.json, setup.py, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/references/background-systems.md, skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md, skills/autonomous-ai-agents/nastech-agent/references/configuration.md, skills/autonomous-ai-agents/nastech-agent/references/contributor-guide.md, skills/autonomous-ai-agents/nastech-agent/references/portal-auth-for-third-party-apps.md, skills/autonomous-ai-agents/nastech-agent/references/providers-and-models.md, skills/autonomous-ai-agents/nastech-agent/references/webhooks.md, tests/agent/test_anthropic_adapter.py, tests/agent/test_auxiliary_client.py, tests/agent/test_auxiliary_main_first.py, tests/agent/test_auxiliary_transport_autodetect.py, tests/agent/test_billing_links.py, tests/agent/test_credential_pool.py, tests/agent/test_credits_policy.py, tests/agent/test_error_classifier.py, tests/agent/test_model_metadata.py, tests/agent/test_nastech_credits_gauge.py, tests/agent/test_nastech_oauth_401_guidance.py, tests/agent/test_nastech_portal_anthropic_wire.py, tests/agent/test_phantom_tool_references.py, tests/agent/transports/test_chat_completions.py, tests/cli/test_cli_first_run_setup.py, tests/cli/test_cli_provider_resolution.py, tests/cli/test_show_config_credential.py, tests/docker/test_sqlite_runtime.py, tests/gateway/test_discord_format.py, tests/gateway/test_run_progress_topics.py, tests/gateway/test_status_command.py, tests/gateway/test_usage_command.py, tests/nastech_cli/test_auth_nastech_provider.py, tests/nastech_cli/test_base_url_host_identity.py, tests/nastech_cli/test_dashboard_auth_gate.py, tests/nastech_cli/test_dashboard_register.py, tests/nastech_cli/test_fireworks_provider.py, tests/nastech_cli/test_gateway_restart_loop.py, tests/nastech_cli/test_model_catalog.py, tests/nastech_cli/test_model_validation.py, tests/nastech_cli/test_nastech_auth_keepalive.py, tests/nastech_cli/test_nastech_auth_status_cache.py, tests/nastech_cli/test_nastech_inference_url_validation.py, tests/nastech_cli/test_nastech_portal_staging_allowlist.py, tests/nastech_cli/test_nastech_reasoning_metadata.py, tests/nastech_cli/test_proxy.py, tests/nastech_cli/test_reasoning_caps_disk_cache.py, tests/nastech_cli/test_sale_pricing.py, tests/nastech_cli/test_web_oauth_dispatch.py, tests/plugins/dashboard_auth/test_nastech_provider.py, tests/plugins/image_gen/check_parity_vs_main.py, tests/plugins/image_gen/test_openrouter_compat_provider.py, tests/plugins/test_chronos_verify.py, tests/run_agent/test_anthropic_prompt_cache_policy.py, tests/run_agent/test_primary_runtime_restore.py, tests/run_agent/test_provider_attribution_headers.py, tests/run_agent/test_provider_fallback.py, tests/run_agent/test_provider_parity.py, tests/run_agent/test_run_agent.py, tests/run_agent/test_switch_model_reapplies_headers.py, tests/test_install_ps1_uv_powershell_host.py, tests/tools/test_delegate.py, tests/tools/test_managed_media_gateways.py, tests/tools/test_managed_tool_gateway.py, tests/tools/test_strict_provider_selection.py, tests/tools/test_tts_openai_config.py, tests/tools/test_url_safety.py, tests/tools/test_web_tools_config.py, tools/managed_tool_gateway.py, tools/mcp_oauth.py, tools/skills_hub.py, tools/skills_sync_client.py, trajectory_compressor.py, ui-tui/scripts/billing-fixtures.tsx, ui-tui/src/__tests__/subscriptionCommand.test.ts, ui-tui/src/__tests__/subscriptionOverlay.test.tsx, ui-tui/src/app/slash/commands/subscription.ts, ui-tui/src/domain/paths.ts, uv.lock, web/src/components/SidebarFooter.tsx, web/src/pages/DocsPage.tsx, web/src/pages/SystemPage.tsx, website/docs/developer-guide/contributing.md, website/docs/developer-guide/egress-internals.md, website/docs/getting-started/installation.md, website/docs/getting-started/platform-support.md, website/docs/getting-started/quickstart.md, website/docs/getting-started/termux.md, website/docs/guides/manage-nastech-cloud-with-mcp.md, website/docs/guides/run-nastech-with-nastech-portal.md, website/docs/guides/run-nemotron-3-ultra-free.md, website/docs/index.mdx, website/docs/integrations/nastech-portal.md, website/docs/integrations/providers.md, website/docs/reference/cli-commands.md, website/docs/reference/environment-variables.md, website/docs/reference/faq.md, website/docs/reference/model-catalog.md, website/docs/user-guide/desktop.md, website/docs/user-guide/egress/iron-proxy.md, website/docs/user-guide/features/browser.md, website/docs/user-guide/features/image-generation.md, website/docs/user-guide/features/skills.md, website/docs/user-guide/features/subscription-proxy.md, website/docs/user-guide/features/tool-gateway.md, website/docs/user-guide/features/tools.md, website/docs/user-guide/features/tts.md, website/docs/user-guide/features/web-dashboard.md, website/docs/user-guide/features/web-search.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/windows-wsl-quickstart.md, website/docusaurus.config.ts, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/contributing.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/quickstart.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-nastech-with-nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/index.mdx, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/providers.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/faq.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/model-catalog.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/subscription-proxy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tools.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tts.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-native.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-wsl-quickstart.md, website/scripts/generate-llms-txt.py, website/scripts/prebuild.mjs, website/static/api/model-catalog.json, website/static/oauth/client-metadata.json


## Direct upstream tree delta

- complete: +38 ~186 -1 ↪0
- MODIFIED `agent/anthropic_adapter.py`
- MODIFIED `agent/auxiliary_client.py`
- MODIFIED `agent/background_review.py`
- MODIFIED `agent/bedrock_adapter.py`
- MODIFIED `agent/chat_completion_helpers.py`
- MODIFIED `agent/conversation_compression.py`
- MODIFIED `agent/conversation_loop.py`
- MODIFIED `agent/credential_pool.py`
- MODIFIED `agent/prompt_builder.py`
- MODIFIED `agent/skill_utils.py`
- MODIFIED `agent/transports/anthropic.py`
- MODIFIED `agent/transports/bedrock.py`
- MODIFIED `agent/transports/chat_completions.py`
- MODIFIED `agent/transports/codex.py`
- MODIFIED `agent/transports/types.py`
- MODIFIED `agent/web_search_provider.py`
- MODIFIED `agent/web_search_registry.py`
- MODIFIED `apps/desktop/electron/backend-ready.test.ts`
- MODIFIED `apps/desktop/electron/backend-ready.ts`
- MODIFIED `apps/desktop/electron/main.ts`
- ADDED `apps/desktop/electron/profile-migration.test.ts`
- ADDED `apps/desktop/electron/profile-migration.ts`
- MODIFIED `apps/desktop/src/i18n/ar.ts`
- MODIFIED `apps/desktop/src/i18n/catalog.ts`
- MODIFIED `apps/desktop/src/i18n/en.ts`
- MODIFIED `apps/desktop/src/i18n/ja.ts`
- MODIFIED `apps/desktop/src/i18n/languages.test.ts`
- MODIFIED `apps/desktop/src/i18n/languages.ts`
- ADDED `apps/desktop/src/i18n/ru.ts`
- MODIFIED `apps/desktop/src/i18n/types.ts`
- MODIFIED `apps/desktop/src/i18n/zh-hant.ts`
- MODIFIED `apps/desktop/src/i18n/zh.ts`
- MODIFIED `apps/desktop/src/store/onboarding.test.ts`
- MODIFIED `apps/desktop/src/store/onboarding.ts`
- DELETED `contributors/emails/agent@Agents-Mac-mini.local`
- ADDED `contributors/emails/nastech@ecl.400iso.net`
- ADDED `contributors/emails/jon@cromulent.dk`
- ADDED `contributors/emails/user55596@protonmail.com`
- MODIFIED `cron/jobs.py`
- MODIFIED `cron/scheduler.py`
- MODIFIED `evals/browser_use/single_run.py`
- MODIFIED `gateway/channel_directory.py`
- MODIFIED `gateway/mirror.py`
- MODIFIED `gateway/run.py`
- MODIFIED `gateway/session.py`
- MODIFIED `gateway/shutdown_flush.py`
- MODIFIED `gateway/slash_commands.py`
- MODIFIED `gateway/stream_consumer.py`
- MODIFIED `gateway/wake.py`
- MODIFIED `nastech_cli/auth.py`
- MODIFIED `nastech_cli/backup.py`
- MODIFIED `nastech_cli/config.py`
- MODIFIED `nastech_cli/config_defaults.py`
- MODIFIED `nastech_cli/cron.py`
- MODIFIED `nastech_cli/dashboard_procs.py`
- MODIFIED `nastech_cli/dump.py`
- MODIFIED `nastech_cli/gateway_windows.py`
- MODIFIED `nastech_cli/hooks.py`
- MODIFIED `nastech_cli/main.py`
- MODIFIED `nastech_cli/model_setup_flows.py`
- MODIFIED `nastech_cli/nastech_subscription.py`
- MODIFIED `nastech_cli/proxy/server.py`
- ADDED `nastech_cli/proxy/sse_done.py`
- MODIFIED `nastech_cli/runtime_provider.py`
- MODIFIED `nastech_cli/setup.py`
- MODIFIED `nastech_cli/status.py`
- MODIFIED `nastech_cli/tools_config.py`
- ADDED `nastech_cli/update_abort_recovery.py`
- MODIFIED `nastech_cli/update_cmd.py`
- MODIFIED `nastech_cli/update_inventory.py`
- MODIFIED `nastech_cli/update_receipt.py`
- MODIFIED `nastech_cli/update_restart_recovery.py`
- MODIFIED `nastech_state.py`
- MODIFIED `nastech_state_common.py`
- ADDED `nastech_state_registry.py`
- MODIFIED `mcp_serve.py`
- MODIFIED `plugins/platforms/discord/adapter.py`
- MODIFIED `plugins/platforms/telegram/adapter.py`
- MODIFIED `plugins/web/brave_free/provider.py`
- MODIFIED `plugins/web/searxng/__init__.py`
- ADDED `plugins/web/tavily/__init__.py`
- ADDED `plugins/web/tavily/plugin.yaml`
- ADDED `plugins/web/tavily/provider.py`
- MODIFIED `plugins/web/xai/provider.py`
- MODIFIED `run_agent.py`
- MODIFIED `scripts/desktop-update/posix.sh`
- MODIFIED `scripts/install.ps1`
- MODIFIED `tests/agent/test_anthropic_mcp_prefix_strip.py`
- MODIFIED `tests/agent/test_auxiliary_client.py`
- MODIFIED `tests/agent/test_auxiliary_named_custom_providers.py`
- MODIFIED `tests/agent/test_bedrock_adapter.py`
- ADDED `tests/agent/test_bedrock_transport_replay.py`
- MODIFIED `tests/agent/test_credential_pool_provider_boundary.py`
- ADDED `tests/agent/test_openrouter_silent_default_purge.py`
- MODIFIED `tests/agent/test_trace_upload.py`
- MODIFIED `tests/agent/transports/test_chat_completions.py`
- MODIFIED `tests/conftest.py`
- MODIFIED `tests/cron/test_cleanup_timeout.py`
- MODIFIED `tests/cron/test_cron_drift_alert_once.py`
- MODIFIED `tests/cron/test_cron_incidents.py`
- MODIFIED `tests/cron/test_cron_provider_pin.py`
- MODIFIED `tests/cron/test_cron_request_overrides.py`
- ADDED `tests/cron/test_dispatch_lateness_stamp.py`
- MODIFIED `tests/cron/test_preflight_config.py`
- MODIFIED `tests/cron/test_scheduler.py`
- MODIFIED `tests/cron/test_scheduler_cron_session_isolation.py`
- MODIFIED `tests/cron/test_script_claim_heartbeat.py`
- MODIFIED `tests/cron/test_sessiondb_init_hang.py`
- MODIFIED `tests/gateway/test_73771_media_resend_dedup.py`
- MODIFIED `tests/gateway/test_background_process_notifications.py`
- MODIFIED `tests/gateway/test_goal_continuation_drain.py`
- MODIFIED `tests/gateway/test_goal_max_turns_config.py`
- MODIFIED `tests/gateway/test_goal_resume_restart.py`
- MODIFIED `tests/gateway/test_hosted_room_gateway_lifecycle.py`
- MODIFIED `tests/gateway/test_loop_command.py`
- MODIFIED `tests/gateway/test_mirror.py`
- MODIFIED `tests/gateway/test_pending_drain_no_recursion.py`
- MODIFIED `tests/gateway/test_pending_drain_race.py`
- MODIFIED `tests/gateway/test_session_db_recovery.py`
- MODIFIED `tests/gateway/test_shutdown_flush.py`
- ADDED `tests/gateway/test_silent_partial_delivery_95382.py`
- MODIFIED `tests/gateway/test_stale_finalize_suppression.py`
- ADDED `tests/gateway/test_telegram_connect_success_visibility.py`
- MODIFIED `tests/gateway/test_wake_delivery.py`
- MODIFIED `tests/nastech_cli/test_anthropic_oauth_routes_to_messages_api.py`
- MODIFIED `tests/nastech_cli/test_backup.py`
- MODIFIED `tests/nastech_cli/test_config.py`
- ADDED `tests/nastech_cli/test_config_guard_surfaces.py`
- ADDED `tests/nastech_cli/test_cron_dispatch_visibility.py`
- MODIFIED `tests/nastech_cli/test_dump_env_visibility.py`
- ADDED `tests/nastech_cli/test_gateway_start_attestation.py`
- MODIFIED `tests/nastech_cli/test_kanban_init_lock_bounded.py`
- ADDED `tests/nastech_cli/test_keyed_provider_credential_pool.py`
- ADDED `tests/nastech_cli/test_noninteractive_config_guard.py`
- MODIFIED `tests/nastech_cli/test_nastech_subscription.py`
- MODIFIED `tests/nastech_cli/test_plugins.py`
- MODIFIED `tests/nastech_cli/test_proxy.py`
- ADDED `tests/nastech_cli/test_resolve_provider_corrupt_config.py`
- ADDED `tests/nastech_cli/test_restore_own_holder_guard.py`
- MODIFIED `tests/nastech_cli/test_runtime_provider_resolution.py`
- MODIFIED `tests/nastech_cli/test_serve_runtime_inventory.py`
- ADDED `tests/nastech_cli/test_sse_done.py`
- MODIFIED `tests/nastech_cli/test_status.py`
- MODIFIED `tests/nastech_cli/test_tools_config.py`
- MODIFIED `tests/nastech_cli/test_update_autostash.py`
- MODIFIED `tests/nastech_cli/test_update_config_migration_on_current_checkout.py`
- ADDED `tests/nastech_cli/test_update_cron_deadlock_guard.py`
- MODIFIED `tests/nastech_cli/test_update_current_node_repair.py`
- ADDED `tests/nastech_cli/test_update_handoff_desktop_rebuild.py`
- MODIFIED `tests/nastech_cli/test_update_receipt.py`
- MODIFIED `tests/nastech_cli/test_update_restart_recovery.py`
- ADDED `tests/nastech_cli/test_update_serve_generation_recovery.py`
- MODIFIED `tests/nastech_cli/test_update_sqlite_remediation.py`
- MODIFIED `tests/nastech_cli/test_update_stale_dashboard.py`
- ADDED `tests/nastech_state/test_shared_session_db_registry.py`
- MODIFIED `tests/nastech_state/test_state_db_file_identity.py`
- ADDED `tests/install_ps1_fake_uv.py`
- MODIFIED `tests/plugins/web/test_web_search_provider_plugins.py`
- MODIFIED `tests/run_agent/test_background_review.py`
- MODIFIED `tests/run_agent/test_exit_cleanup_interrupt.py`
- ADDED `tests/run_agent/test_first_chunk_at_hook.py`
- ADDED `tests/run_agent/test_in_place_commit_rollback_99477.py`
- MODIFIED `tests/run_agent/test_partial_stream_finish_reason.py`
- MODIFIED `tests/run_agent/test_primary_runtime_restore.py`
- MODIFIED `tests/run_agent/test_token_persistence_non_cli.py`
- MODIFIED `tests/state/test_fts_rebuild_admission.py`
- ADDED `tests/test_desktop_update_tcc_heal.py`
- ADDED `tests/test_install_ps1_managed_python_provenance.py`
- MODIFIED `tests/test_install_ps1_native_stderr_eap.py`
- MODIFIED `tests/test_install_ps1_venv_process_tree.py`
- MODIFIED `tests/test_install_ps1_venv_recreate_safety.py`
- MODIFIED `tests/test_managed_runtime_resolution.py`
- MODIFIED `tests/test_tui_gateway_server.py`
- MODIFIED `tests/tools/conftest.py`
- MODIFIED `tests/tools/test_browser_lightpanda.py`
- MODIFIED `tests/tools/test_browser_orphan_reaper.py`
- ADDED `tests/tools/test_removed_backend_migration.py`
- MODIFIED `tests/tools/test_session_search.py`
- ADDED `tests/tools/test_skill_create_dir.py`
- MODIFIED `tests/tools/test_web_keyless_fallback.py`
- MODIFIED `tests/tools/test_web_tools_config.py`
- ADDED `tests/tools/test_web_tools_tavily.py`
- MODIFIED `tests/tui_gateway/test_hosted_room_driver_runtime.py`
- MODIFIED `tests/tui_gateway/test_session_db_ownership_teardown.py`
- MODIFIED `tests/tui_gateway/test_session_resume_db_ownership.py`
- MODIFIED `tools/browser_tool.py`
- MODIFIED `tools/delegate_tool.py`
- MODIFIED `tools/react_to_message_tool.py`
- MODIFIED `tools/session_search_tool.py`
- MODIFIED `tools/skill_manager_tool.py`
- MODIFIED `tools/tool_backend_helpers.py`
- MODIFIED `tools/url_safety.py`
- MODIFIED `tools/web_tools.py`
- MODIFIED `tui_gateway/compute_host.py`
- MODIFIED `tui_gateway/methods_profiles.py`
- MODIFIED `tui_gateway/methods_session.py`
- MODIFIED `tui_gateway/server.py`
- ADDED `web/src/components/OAuthLoginModal.test.tsx`
- MODIFIED `web/src/components/OAuthLoginModal.tsx`
- MODIFIED `web/src/i18n/af.ts`
- MODIFIED `web/src/i18n/de.ts`
- MODIFIED `web/src/i18n/en.ts`
- MODIFIED `web/src/i18n/es.ts`
- MODIFIED `web/src/i18n/fr.ts`
- MODIFIED `web/src/i18n/ga.ts`
- MODIFIED `web/src/i18n/hu.ts`
- MODIFIED `web/src/i18n/it.ts`
- MODIFIED `web/src/i18n/ja.ts`
- MODIFIED `web/src/i18n/ko.ts`
- MODIFIED `web/src/i18n/pt.ts`
- MODIFIED `web/src/i18n/ru.ts`
- MODIFIED `web/src/i18n/tr.ts`
- MODIFIED `web/src/i18n/types.ts`
- MODIFIED `web/src/i18n/uk.ts`
- MODIFIED `web/src/i18n/zh-hant.ts`
- MODIFIED `web/src/i18n/zh.ts`
- MODIFIED `website/docs/developer-guide/web-search-provider-plugin.md`
- MODIFIED `website/docs/integrations/index.md`
- MODIFIED `website/docs/reference/environment-variables.md`
- MODIFIED `website/docs/reference/tools-reference.md`
- MODIFIED `website/docs/user-guide/configuration.md`
- MODIFIED `website/docs/user-guide/desktop.md`
- MODIFIED `website/docs/user-guide/features/skills.md`
- MODIFIED `website/docs/user-guide/features/web-dashboard.md`
- MODIFIED `website/docs/user-guide/features/web-search.md`

## Scan

11096 files scanned [audio=5, binary=7, doc=5, font=13, image=92, text=10974]


## Diff

1449 renamed, 0 rewritten, 9241 identical, 61 locked, 0 missing, 34 owned, 255 reconciled


## Fork check (vs nastech-agent)

- 10716 identical, 341 updated (+0/-0 lines), 39 added, 0 missing, 0 fork-local-unpreserved, 0 stale-upstream, 0 locked/binary, 0 collision-safe relocated, 56 preserved fork-local files, 0 violations

- features: fork 51 -> branded 51

Auto-generated by 100Ways.
