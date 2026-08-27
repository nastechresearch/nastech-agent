# Nastech Update Report #1

- upstream sha : `790e1eb6bd576261e6b9e70fcfe4fbdf17f866bb`
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

- total files : 10435
- renamed     : 1447 (folders and file names)
- text-rewritten : 10337
- locked-copied  : 56
- binary-copied  : 8
- owned assets   : 34 (our logo/banner/mascot override upstream)

## Reconcile

- fixed : 256 files reconciled: .github/workflows/deploy-site.yml, .github/workflows/deploy-site.yml, .github/workflows/skills-index-freshness.yml, .mailmap, CONTRIBUTING.es.md, CONTRIBUTING.md, Dockerfile, README.es.md, README.md, README.ur-pk.md, README.zh-CN.md, SECURITY.es.md, SECURITY.md, agent/agent_runtime_helpers.py, agent/anthropic_adapter.py, agent/auxiliary_client.py, agent/billing_links.py, agent/billing_view.py, agent/chat_completion_helpers.py, agent/conversation_loop.py, agent/credits_tracker.py, agent/model_metadata.py, agent/prompt_builder.py, agent/proxy_sources/iron_proxy.py, agent/subscription_view.py, agent/usage_pricing.py, apps/bootstrap-installer/src-tauri/Cargo.toml, apps/desktop/README.md, apps/desktop/electron/backend-health.test.ts, apps/desktop/electron/backend-health.ts, apps/desktop/electron/connection-config.test.ts, apps/desktop/electron/main.ts, apps/desktop/electron/oauth-partition.test.ts, apps/desktop/electron/remote-lifecycle.ts, apps/desktop/package.json, apps/desktop/src/app/messaging/index.test.tsx, apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx, apps/desktop/src/app/settings/about-settings.tsx, apps/desktop/src/app/settings/billing/api.test.ts, apps/desktop/src/app/settings/billing/dev-fixtures.ts, apps/desktop/src/app/settings/billing/errors.test.ts, apps/desktop/src/app/settings/billing/types.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.ts, apps/desktop/src/app/settings/billing/use-charge-poller.test.ts, apps/desktop/src/app/settings/billing/use-step-up.test.tsx, apps/desktop/src/app/settings/constants.ts, apps/desktop/src/app/settings/gateway-settings.tsx, apps/desktop/src/app/settings/toolset-config-panel.test.tsx, apps/desktop/src/app/skills/embedded-hub-picker.tsx, apps/desktop/src/app/skills/index.test.tsx, apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts, apps/desktop/src/components/boot-failure-overlay.test.tsx, apps/desktop/src/components/boot-failure-overlay.tsx, apps/desktop/src/components/send-diagnostics-dialog.tsx, apps/desktop/src/contrib/plugin.ts, apps/desktop/src/i18n/en.ts, apps/desktop/src/i18n/ja.ts, apps/desktop/src/i18n/zh-hant.ts, apps/desktop/src/i18n/zh.ts, apps/desktop/src/plugins/nastech-bots/plugin.js, apps/desktop/src/sdk/index.ts, cli-config.yaml.example, eslint.config.shared.mjs, nastech_cli/auth.py, nastech_cli/banner.py, nastech_cli/config_defaults.py, nastech_cli/dashboard_auth/login_page.py, nastech_cli/dashboard_register.py, nastech_cli/debug.py, nastech_cli/diagnostics_upload.py, nastech_cli/fallback_cmd.py, nastech_cli/kanban.py, nastech_cli/main.py, nastech_cli/model_catalog.py, nastech_cli/model_switch.py, nastech_cli/models.py, nastech_cli/nastech_account.py, nastech_cli/nastech_billing.py, nastech_cli/plugins_cmd.py, nastech_cli/portal_cli.py, nastech_cli/providers.py, nastech_cli/proxy/__init__.py, nastech_cli/proxy/adapters/base.py, nastech_cli/proxy/adapters/nastech_portal.py, nastech_cli/setup.py, nastech_cli/setup_whatsapp_cloud.py, nastech_cli/skin_engine.py, nastech_cli/telegram_managed_bot.py, nastech_cli/tools_config.py, nastech_cli/uninstall.py, nastech_cli/update_cmd.py, nastech_cli/web_server.py, nastech_constants.py, package-lock.json, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/plugin.yaml, plugins/kanban/dashboard/dist/index.js, plugins/kanban/systemd/nastech-kanban-dispatcher.service, plugins/model-providers/ai-gateway/__init__.py, plugins/model-providers/fireworks/__init__.py, plugins/model-providers/kimi-coding/__init__.py, plugins/model-providers/nastech/__init__.py, plugins/model-providers/opencode-free/__init__.py, plugins/model-providers/opencode-zen/__init__.py, plugins/nastech-achievements/dashboard/dist/index.js, plugins/platforms/discord/adapter.py, plugins/platforms/email/adapter.py, plugins/platforms/photon/sidecar/package-lock.json, plugins/platforms/slack/adapter.py, run_agent.py, scripts/build_model_catalog.py, scripts/contributor_audit.py, scripts/dev-sandbox.sh, scripts/install.cmd, scripts/install.ps1, scripts/install.sh, scripts/release.py, scripts/whatsapp-bridge/package-lock.json, setup.py, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/references/background-systems.md, skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md, skills/autonomous-ai-agents/nastech-agent/references/configuration.md, skills/autonomous-ai-agents/nastech-agent/references/contributor-guide.md, skills/autonomous-ai-agents/nastech-agent/references/portal-auth-for-third-party-apps.md, skills/autonomous-ai-agents/nastech-agent/references/providers-and-models.md, skills/autonomous-ai-agents/nastech-agent/references/webhooks.md, tests/agent/test_anthropic_adapter.py, tests/agent/test_auxiliary_client.py, tests/agent/test_auxiliary_main_first.py, tests/agent/test_auxiliary_transport_autodetect.py, tests/agent/test_billing_links.py, tests/agent/test_credential_pool.py, tests/agent/test_credits_policy.py, tests/agent/test_error_classifier.py, tests/agent/test_model_metadata.py, tests/agent/test_nastech_credits_gauge.py, tests/agent/test_nastech_oauth_401_guidance.py, tests/agent/test_nastech_portal_anthropic_wire.py, tests/agent/test_phantom_tool_references.py, tests/agent/transports/test_chat_completions.py, tests/cli/test_cli_first_run_setup.py, tests/cli/test_cli_provider_resolution.py, tests/cli/test_show_config_credential.py, tests/docker/test_sqlite_runtime.py, tests/gateway/test_discord_format.py, tests/gateway/test_run_progress_topics.py, tests/gateway/test_status_command.py, tests/gateway/test_usage_command.py, tests/nastech_cli/test_auth_nastech_provider.py, tests/nastech_cli/test_base_url_host_identity.py, tests/nastech_cli/test_dashboard_auth_gate.py, tests/nastech_cli/test_dashboard_register.py, tests/nastech_cli/test_fireworks_provider.py, tests/nastech_cli/test_gateway_restart_loop.py, tests/nastech_cli/test_model_catalog.py, tests/nastech_cli/test_nastech_auth_keepalive.py, tests/nastech_cli/test_nastech_auth_status_cache.py, tests/nastech_cli/test_nastech_inference_url_validation.py, tests/nastech_cli/test_nastech_portal_staging_allowlist.py, tests/nastech_cli/test_nastech_reasoning_metadata.py, tests/nastech_cli/test_proxy.py, tests/nastech_cli/test_reasoning_caps_disk_cache.py, tests/nastech_cli/test_sale_pricing.py, tests/nastech_cli/test_web_oauth_dispatch.py, tests/plugins/dashboard_auth/test_nastech_provider.py, tests/plugins/image_gen/check_parity_vs_main.py, tests/plugins/image_gen/test_openrouter_compat_provider.py, tests/plugins/test_chronos_verify.py, tests/run_agent/test_anthropic_prompt_cache_policy.py, tests/run_agent/test_primary_runtime_restore.py, tests/run_agent/test_provider_attribution_headers.py, tests/run_agent/test_provider_fallback.py, tests/run_agent/test_provider_parity.py, tests/run_agent/test_run_agent.py, tests/run_agent/test_switch_model_reapplies_headers.py, tests/test_install_ps1_uv_powershell_host.py, tests/tools/test_delegate.py, tests/tools/test_managed_media_gateways.py, tests/tools/test_managed_tool_gateway.py, tests/tools/test_strict_provider_selection.py, tests/tools/test_tts_openai_config.py, tests/tools/test_url_safety.py, tests/tools/test_web_tools_config.py, tools/managed_tool_gateway.py, tools/mcp_oauth.py, tools/skills_hub.py, tools/skills_sync_client.py, trajectory_compressor.py, ui-tui/scripts/billing-fixtures.tsx, ui-tui/src/__tests__/subscriptionCommand.test.ts, ui-tui/src/__tests__/subscriptionOverlay.test.tsx, ui-tui/src/app/slash/commands/subscription.ts, ui-tui/src/domain/paths.ts, uv.lock, web/src/components/SidebarFooter.tsx, web/src/pages/DocsPage.tsx, web/src/pages/SystemPage.tsx, website/docs/developer-guide/contributing.md, website/docs/developer-guide/egress-internals.md, website/docs/getting-started/installation.md, website/docs/getting-started/platform-support.md, website/docs/getting-started/quickstart.md, website/docs/getting-started/termux.md, website/docs/guides/manage-nastech-cloud-with-mcp.md, website/docs/guides/run-nastech-with-nastech-portal.md, website/docs/guides/run-nemotron-3-ultra-free.md, website/docs/index.mdx, website/docs/integrations/nastech-portal.md, website/docs/integrations/providers.md, website/docs/reference/cli-commands.md, website/docs/reference/environment-variables.md, website/docs/reference/faq.md, website/docs/reference/model-catalog.md, website/docs/user-guide/desktop.md, website/docs/user-guide/egress/iron-proxy.md, website/docs/user-guide/features/browser.md, website/docs/user-guide/features/image-generation.md, website/docs/user-guide/features/skills.md, website/docs/user-guide/features/subscription-proxy.md, website/docs/user-guide/features/tool-gateway.md, website/docs/user-guide/features/tools.md, website/docs/user-guide/features/tts.md, website/docs/user-guide/features/web-dashboard.md, website/docs/user-guide/features/web-search.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/windows-wsl-quickstart.md, website/docusaurus.config.ts, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/contributing.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/quickstart.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-nastech-with-nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/index.mdx, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/providers.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/faq.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/model-catalog.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/subscription-proxy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tools.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tts.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-native.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-wsl-quickstart.md, website/scripts/generate-llms-txt.py, website/scripts/prebuild.mjs, website/static/api/model-catalog.json, website/static/oauth/client-metadata.json


## Direct upstream tree delta

- complete: +60 ~182 -4 ↪0
- MODIFIED `Dockerfile`
- ADDED `agent/acp_openai_bridge.py`
- MODIFIED `agent/agent_init.py`
- MODIFIED `agent/background_review.py`
- MODIFIED `agent/context_compressor.py`
- MODIFIED `agent/conversation_loop.py`
- MODIFIED `agent/copilot_acp_client.py`
- MODIFIED `agent/deadline.py`
- ADDED `agent/provider_projection.py`
- MODIFIED `apps/bootstrap-installer/src-tauri/Cargo.toml`
- MODIFIED `apps/bootstrap-installer/src-tauri/src/update.rs`
- ADDED `apps/desktop/e2e/fleet-profile-rail.spec.ts`
- ADDED `apps/desktop/e2e/group-to-local-bot-handoff.spec.ts`
- ADDED `apps/desktop/electron/app-icon.test.ts`
- ADDED `apps/desktop/electron/app-icon.ts`
- MODIFIED `apps/desktop/electron/connection-registry.test.ts`
- MODIFIED `apps/desktop/electron/connection-registry.ts`
- MODIFIED `apps/desktop/electron/desktop-remote-route.test.ts`
- MODIFIED `apps/desktop/electron/desktop-remote-route.ts`
- MODIFIED `apps/desktop/electron/main.ts`
- ADDED `apps/desktop/electron/oauth-partition.test.ts`
- ADDED `apps/desktop/electron/oauth-partition.ts`
- MODIFIED `apps/desktop/electron/remote-lifecycle.test.ts`
- MODIFIED `apps/desktop/electron/remote-lifecycle.ts`
- ADDED `apps/desktop/electron/renderer-load-error-page.test.ts`
- ADDED `apps/desktop/electron/renderer-load-error-page.ts`
- MODIFIED `apps/desktop/electron/window-renderer-lifecycle.test.ts`
- MODIFIED `apps/desktop/electron/window-renderer-lifecycle.ts`
- MODIFIED `apps/desktop/src/api/profiles.ts`
- MODIFIED `apps/desktop/src/app/chat/chat-swap-overlay.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/attachments.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/index.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/index.tsx`
- MODIFIED `apps/desktop/src/app/chat/session-tile-actions.ts`
- ADDED `apps/desktop/src/app/chat/sidebar/connection-glyph.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/connection-switcher.tsx`
- ADDED `apps/desktop/src/app/chat/sidebar/fleet-rail.test.ts`
- ADDED `apps/desktop/src/app/chat/sidebar/fleet-rail.ts`
- MODIFIED `apps/desktop/src/app/chat/sidebar/index.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/profile-rail-connect.test.tsx`
- ADDED `apps/desktop/src/app/chat/sidebar/profile-rail-fleet.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/profile-switcher.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/projects/workspace-groups.test.ts`
- MODIFIED `apps/desktop/src/app/chat/sidebar/projects/workspace-groups.ts`
- MODIFIED `apps/desktop/src/app/chat/sidebar/session-actions-menu.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/session-actions-menu.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/sessions-section.tsx`
- ADDED `apps/desktop/src/app/chat/sidebar/use-fleet-roster.ts`
- MODIFIED `apps/desktop/src/app/chat/sidebar/virtual-session-list.tsx`
- MODIFIED `apps/desktop/src/app/contrib/hooks/use-background-sync.test.ts`
- MODIFIED `apps/desktop/src/app/contrib/hooks/use-background-sync.ts`
- MODIFIED `apps/desktop/src/app/contrib/hooks/use-session-tile-delegate.ts`
- MODIFIED `apps/desktop/src/app/contrib/session-rpc-dispatcher.test.ts`
- MODIFIED `apps/desktop/src/app/contrib/session-rpc-dispatcher.ts`
- MODIFIED `apps/desktop/src/app/contrib/wiring.tsx`
- MODIFIED `apps/desktop/src/app/gateway/hooks/use-gateway-boot.test.tsx`
- MODIFIED `apps/desktop/src/app/gateway/hooks/use-gateway-boot.ts`
- MODIFIED `apps/desktop/src/app/profiles/delete-profile-dialog.tsx`
- MODIFIED `apps/desktop/src/app/profiles/rename-profile-dialog.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/gateway-event/session-info.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-model-controls.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-model-controls.ts`
- MODIFIED `apps/desktop/src/components/assistant-ui/clarify-tool.test.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/clarify-tool.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/markdown-text.artifacts.test.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/message-parts.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/streaming.test.tsx`
- MODIFIED `apps/desktop/src/components/pane-shell/tree/renderer/tree-group.tsx`
- ADDED `apps/desktop/src/hover-variant.test.ts`
- MODIFIED `apps/desktop/src/i18n/ar.ts`
- MODIFIED `apps/desktop/src/i18n/en.ts`
- MODIFIED `apps/desktop/src/i18n/ja.ts`
- MODIFIED `apps/desktop/src/i18n/types.ts`
- MODIFIED `apps/desktop/src/i18n/zh-hant.ts`
- MODIFIED `apps/desktop/src/i18n/zh.ts`
- DELETED `apps/desktop/src/plugins/accent/plugin.js`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/plugin.js`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/active-now-strip.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/bots-home.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/canonical-chat-creation.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/canonical-chat-registry.test.mjs`
- ADDED `apps/desktop/src/plugins/nastech-bots/tests/group-to-local-bot-handoff.test.mjs`
- ADDED `apps/desktop/src/plugins/nastech-bots/tests/legacy-member-normalize.test.mjs`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/tests/remote-routing-races.test.mjs`
- DELETED `apps/desktop/src/plugins/kanban/plugin.js`
- MODIFIED `apps/desktop/src/sdk/index.ts`
- MODIFIED `apps/desktop/src/sdk/profile-routing.test.ts`
- MODIFIED `apps/desktop/src/store/connections.test.ts`
- MODIFIED `apps/desktop/src/store/connections.ts`
- MODIFIED `apps/desktop/src/store/cron-model-impact.test.ts`
- MODIFIED `apps/desktop/src/store/cron-model-impact.ts`
- ADDED `apps/desktop/src/store/fleet-roster.ts`
- MODIFIED `apps/desktop/src/store/gateway-connection-scope.test.ts`
- MODIFIED `apps/desktop/src/store/gateway.test.ts`
- MODIFIED `apps/desktop/src/store/gateway.ts`
- MODIFIED `apps/desktop/src/store/onboarding.ts`
- MODIFIED `apps/desktop/src/store/profile.ts`
- MODIFIED `apps/desktop/src/store/session-states.test.ts`
- MODIFIED `apps/desktop/src/store/session-states.ts`
- MODIFIED `apps/desktop/src/store/session.test.ts`
- MODIFIED `apps/desktop/src/store/session.ts`
- MODIFIED `apps/desktop/src/styles.css`
- MODIFIED `apps/desktop/src/types/nastech.ts`
- ADDED `contributors/emails/Finn763@users.noreply.github.com`
- ADDED `contributors/emails/alex.gazzillo@gmail.com`
- ADDED `contributors/emails/alexander.prendota@gmail.com`
- ADDED `contributors/emails/caseyrussell1976@gmail.com`
- ADDED `contributors/emails/epeterpanz@gmail.com`
- ADDED `contributors/emails/etzelvon@users.noreply.github.com`
- ADDED `contributors/emails/nastech@lift-off.co.uk`
- ADDED `contributors/emails/laroberts@hchb.com`
- ADDED `contributors/emails/takealook97@naver.com`
- MODIFIED `docs/kanban/multi-gateway.md`
- ADDED `evals/session_search_schema/README.md`
- ADDED `evals/session_search_schema/fixtures.py`
- ADDED `evals/session_search_schema/report.py`
- ADDED `evals/session_search_schema/results/pr95570/openai_gpt-5.6-luna.jsonl`
- ADDED `evals/session_search_schema/results/pr95570/openai_gpt-5.6-terra.jsonl`
- ADDED `evals/session_search_schema/results/pr95570/qwen_qwen3-coder-30b-a3b-instruct.jsonl`
- ADDED `evals/session_search_schema/runner.py`
- ADDED `evals/session_search_schema/tasks.py`
- MODIFIED `gateway/control_socket.py`
- MODIFIED `gateway/kanban_watchers.py`
- MODIFIED `gateway/run.py`
- MODIFIED `gateway/scale_to_zero.py`
- MODIFIED `gateway/slash_commands.py`
- MODIFIED `gateway/status.py`
- MODIFIED `nastech_cli/backup.py`
- MODIFIED `nastech_cli/banner.py`
- MODIFIED `nastech_cli/cli_commands_mixin.py`
- MODIFIED `nastech_cli/config.py`
- MODIFIED `nastech_cli/config_defaults.py`
- MODIFIED `nastech_cli/dashboard_procs.py`
- MODIFIED `nastech_cli/doctor.py`
- MODIFIED `nastech_cli/gateway.py`
- MODIFIED `nastech_cli/gitlock.py`
- ADDED `nastech_cli/image_provenance.py`
- DELETED `nastech_cli/macos_tcc_anchor.py`
- MODIFIED `nastech_cli/main.py`
- MODIFIED `nastech_cli/memory_setup.py`
- MODIFIED `nastech_cli/models.py`
- MODIFIED `nastech_cli/process_identity.py`
- MODIFIED `nastech_cli/setup.py`
- MODIFIED `nastech_cli/update_cmd.py`
- ADDED `nastech_cli/update_contract.py`
- MODIFIED `nastech_cli/update_inventory.py`
- MODIFIED `nastech_cli/update_receipt.py`
- ADDED `nastech_cli/update_restart_recovery.py`
- MODIFIED `nastech_cli/web_routers/mcp.py`
- MODIFIED `nastech_cli/web_server.py`
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
- MODIFIED `package-lock.json`
- MODIFIED `package.json`
- MODIFIED `plugins/memory/supermemory/__init__.py`
- MODIFIED `plugins/platforms/slack/adapter.py`
- MODIFIED `plugins/video_gen/fal/__init__.py`
- ADDED `tests/agent/test_acp_openai_bridge.py`
- ADDED `tests/agent/test_acp_provider_rails.py`
- ADDED `tests/agent/test_background_review_tool_call_guard.py`
- MODIFIED `tests/agent/test_compression_small_ctx_threshold_floor.py`
- MODIFIED `tests/agent/test_context_compressor.py`
- MODIFIED `tests/agent/test_context_compressor_summary_continuity.py`
- MODIFIED `tests/agent/test_deadline.py`
- ADDED `tests/agent/test_provider_projection.py`
- ADDED `tests/desktop/test_bots_chat_live_append.py`
- ADDED `tests/desktop/test_bots_chat_stream_rekey.py`
- ADDED `tests/gateway/test_control_socket_pause.py`
- ADDED `tests/gateway/test_kanban_changes_requested_notifier.py`
- MODIFIED `tests/gateway/test_kanban_notifier.py`
- MODIFIED `tests/gateway/test_scale_to_zero_watcher.py`
- MODIFIED `tests/gateway/test_slack.py`
- MODIFIED `tests/gateway/test_slack_mention.py`
- ADDED `tests/gateway/test_slack_unfurl_duplicate_turn.py`
- MODIFIED `tests/gateway/test_status.py`
- MODIFIED `tests/nastech_cli/test_backup.py`
- MODIFIED `tests/nastech_cli/test_cmd_update_apt.py`
- MODIFIED `tests/nastech_cli/test_cmd_update_docker.py`
- MODIFIED `tests/nastech_cli/test_config.py`
- MODIFIED `tests/nastech_cli/test_dashboard_lifecycle_flags.py`
- MODIFIED `tests/nastech_cli/test_fleet_matrix_down_state.py`
- MODIFIED `tests/nastech_cli/test_gateway.py`
- ADDED `tests/nastech_cli/test_gitlock_tmp_packs.py`
- ADDED `tests/nastech_cli/test_macos_fda_guidance.py`
- DELETED `tests/nastech_cli/test_macos_tcc_anchor.py`
- ADDED `tests/nastech_cli/test_mcp_catalog_env_boundary.py`
- MODIFIED `tests/nastech_cli/test_memory_setup.py`
- ADDED `tests/nastech_cli/test_memory_setup_env_denylist.py`
- MODIFIED `tests/nastech_cli/test_restart_plan_reconciliation.py`
- ADDED `tests/nastech_cli/test_serve_runtime_inventory.py`
- MODIFIED `tests/nastech_cli/test_ssh_ownership_endpoint.py`
- ADDED `tests/nastech_cli/test_tcc_anchor_revert.py`
- MODIFIED `tests/nastech_cli/test_update_cold_start_gateway_liveness.py`
- MODIFIED `tests/nastech_cli/test_update_concurrent_quarantine.py`
- ADDED `tests/nastech_cli/test_update_contract.py`
- MODIFIED `tests/nastech_cli/test_update_fleet_check_fail_closed.py`
- MODIFIED `tests/nastech_cli/test_update_receipt.py`
- ADDED `tests/nastech_cli/test_update_restart_recovery.py`
- MODIFIED `tests/nastech_cli/test_update_stale_dashboard.py`
- ADDED `tests/nastech_cli/test_update_state_autorestore.py`
- MODIFIED `tests/nastech_cli/test_web_server.py`
- MODIFIED `tests/nastech_cli/test_windows_gateway_cold_start_desktop_lifecycle.py`
- ADDED `tests/nastech_cli/test_windows_update_restart_reconciliation.py`
- MODIFIED `tests/run_agent/test_compression_persistence.py`
- MODIFIED `tests/tools/test_checkpoint_manager.py`
- MODIFIED `tests/tools/test_clarify_tool.py`
- ADDED `tests/tools/test_macos_protected_search.py`
- MODIFIED `tests/tools/test_mcp_parked_self_probe.py`
- MODIFIED `tests/tools/test_mcp_reconnect_log_hygiene.py`
- MODIFIED `tests/tools/test_mcp_reconnect_retry_reset.py`
- MODIFIED `tests/tools/test_mcp_tool.py`
- ADDED `tests/tui_gateway/test_deferred_model_switch_confirm.py`
- MODIFIED `tools/checkpoint_manager.py`
- MODIFIED `tools/clarify_tool.py`
- MODIFIED `tools/environments/base.py`
- MODIFIED `tools/environments/local.py`
- MODIFIED `tools/file_operations.py`
- MODIFIED `tools/file_tools.py`
- MODIFIED `tools/mcp_tool.py`
- MODIFIED `tools/session_search_tool.py`
- MODIFIED `tools/skill_manager_tool.py`
- MODIFIED `tui_gateway/server.py`
- MODIFIED `website/docs/developer-guide/context-compression-and-caching.md`
- MODIFIED `website/docs/getting-started/updating.md`
- MODIFIED `website/docs/reference/cli-commands.md`
- MODIFIED `website/docs/reference/slash-commands.md`
- MODIFIED `website/docs/user-guide/configuration.md`
- MODIFIED `website/docs/user-guide/desktop.md`
- MODIFIED `website/docs/user-guide/features/kanban.md`
- MODIFIED `website/docs/user-guide/multi-connection-desktop.md`
- MODIFIED `website/static/api/model-catalog.json`

## Scan

10489 files scanned [audio=5, binary=7, doc=5, font=13, image=92, text=10367]


## Diff

1360 renamed, 0 rewritten, 8730 identical, 61 locked, 0 missing, 34 owned, 250 reconciled


## Fork check (vs nastech-agent)

- 10116 identical, 312 updated (+0/-0 lines), 60 added, 0 missing, 0 fork-local-unpreserved, 0 stale-upstream, 1 locked/binary, 0 collision-safe relocated, 54 preserved fork-local files, 0 violations

- features: fork 51 -> branded 51

Auto-generated by 100Ways.
