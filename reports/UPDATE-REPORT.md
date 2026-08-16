# Nastech Update Report #1

- upstream sha : `7095e23eb2066fe9a2f93b99cdbfe0e2b5ece397`
- source       : `https://github.com/NousResearch/hermes-agent.git`
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

- total files : 9408
- renamed     : 1237 (folders and file names)
- text-rewritten : 8669
- locked-copied  : 699
- binary-copied  : 8
- owned assets   : 32 (our logo/banner/mascot override upstream)

## Reconcile

- fixed : 230 files reconciled: .github/workflows/deploy-site.yml, .github/workflows/skills-index-freshness.yml, .mailmap, CONTRIBUTING.es.md, CONTRIBUTING.md, Dockerfile, README.es.md, README.md, README.ur-pk.md, README.zh-CN.md, SECURITY.es.md, SECURITY.md, agent/agent_runtime_helpers.py, agent/anthropic_adapter.py, agent/auxiliary_client.py, agent/billing_links.py, agent/billing_view.py, agent/chat_completion_helpers.py, agent/conversation_loop.py, agent/credits_tracker.py, agent/model_metadata.py, agent/prompt_builder.py, agent/proxy_sources/iron_proxy.py, agent/subscription_view.py, agent/usage_pricing.py, apps/bootstrap-installer/src-tauri/Cargo.toml, apps/desktop/README.md, apps/desktop/electron/connection-config.test.ts, apps/desktop/electron/main.ts, apps/desktop/electron/remote-lifecycle.ts, apps/desktop/package.json, apps/desktop/src/app/messaging/index.test.tsx, apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx, apps/desktop/src/app/settings/billing/api.test.ts, apps/desktop/src/app/settings/billing/dev-fixtures.ts, apps/desktop/src/app/settings/billing/errors.test.ts, apps/desktop/src/app/settings/billing/types.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.ts, apps/desktop/src/app/settings/billing/use-charge-poller.test.ts, apps/desktop/src/app/settings/billing/use-step-up.test.tsx, apps/desktop/src/app/settings/constants.ts, apps/desktop/src/app/settings/gateway-settings.tsx, apps/desktop/src/app/settings/toolset-config-panel.test.tsx, apps/desktop/src/app/skills/embedded-hub-picker.tsx, apps/desktop/src/app/skills/index.test.tsx, apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts, apps/desktop/src/i18n/en.ts, apps/desktop/src/i18n/ja.ts, apps/desktop/src/i18n/zh-hant.ts, apps/desktop/src/i18n/zh.ts, cli-config.yaml.example, eslint.config.shared.mjs, nastech_cli/auth.py, nastech_cli/config_defaults.py, nastech_cli/dashboard_register.py, nastech_cli/diagnostics_upload.py, nastech_cli/fallback_cmd.py, nastech_cli/kanban.py, nastech_cli/main.py, nastech_cli/model_catalog.py, nastech_cli/model_switch.py, nastech_cli/models.py, nastech_cli/nastech_account.py, nastech_cli/nastech_billing.py, nastech_cli/plugins_cmd.py, nastech_cli/portal_cli.py, nastech_cli/providers.py, nastech_cli/proxy/__init__.py, nastech_cli/proxy/adapters/base.py, nastech_cli/proxy/adapters/nastech_portal.py, nastech_cli/setup.py, nastech_cli/setup_whatsapp_cloud.py, nastech_cli/telegram_managed_bot.py, nastech_cli/tools_config.py, nastech_cli/uninstall.py, nastech_cli/update_cmd.py, nastech_cli/web_server.py, nastech_constants.py, package-lock.json, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/plugin.yaml, plugins/kanban/dashboard/dist/index.js, plugins/kanban/systemd/nastech-kanban-dispatcher.service, plugins/model-providers/ai-gateway/__init__.py, plugins/model-providers/fireworks/__init__.py, plugins/model-providers/kimi-coding/__init__.py, plugins/model-providers/nastech/__init__.py, plugins/model-providers/opencode-zen/__init__.py, plugins/nastech-achievements/dashboard/dist/index.js, plugins/platforms/discord/adapter.py, plugins/platforms/email/adapter.py, plugins/platforms/slack/adapter.py, run_agent.py, scripts/build_model_catalog.py, scripts/contributor_audit.py, scripts/dev-sandbox.sh, scripts/install.cmd, scripts/install.ps1, scripts/install.sh, scripts/release.py, setup.py, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/references/background-systems.md, skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md, skills/autonomous-ai-agents/nastech-agent/references/configuration.md, skills/autonomous-ai-agents/nastech-agent/references/contributor-guide.md, skills/autonomous-ai-agents/nastech-agent/references/portal-auth-for-third-party-apps.md, skills/autonomous-ai-agents/nastech-agent/references/providers-and-models.md, skills/autonomous-ai-agents/nastech-agent/references/webhooks.md, tests/agent/test_anthropic_adapter.py, tests/agent/test_auxiliary_client.py, tests/agent/test_auxiliary_main_first.py, tests/agent/test_auxiliary_transport_autodetect.py, tests/agent/test_billing_links.py, tests/agent/test_credential_pool.py, tests/agent/test_credits_policy.py, tests/agent/test_error_classifier.py, tests/agent/test_model_metadata.py, tests/agent/test_nastech_credits_gauge.py, tests/agent/test_nastech_oauth_401_guidance.py, tests/agent/test_nastech_portal_anthropic_wire.py, tests/agent/transports/test_chat_completions.py, tests/cli/test_cli_first_run_setup.py, tests/cli/test_cli_provider_resolution.py, tests/docker/test_sqlite_runtime.py, tests/gateway/test_discord_format.py, tests/gateway/test_run_progress_topics.py, tests/gateway/test_status_command.py, tests/gateway/test_usage_command.py, tests/nastech_cli/test_auth_nastech_provider.py, tests/nastech_cli/test_base_url_host_identity.py, tests/nastech_cli/test_dashboard_register.py, tests/nastech_cli/test_fireworks_provider.py, tests/nastech_cli/test_gateway_restart_loop.py, tests/nastech_cli/test_model_catalog.py, tests/nastech_cli/test_nastech_auth_keepalive.py, tests/nastech_cli/test_nastech_auth_status_cache.py, tests/nastech_cli/test_nastech_inference_url_validation.py, tests/nastech_cli/test_nastech_portal_staging_allowlist.py, tests/nastech_cli/test_proxy.py, tests/nastech_cli/test_sale_pricing.py, tests/nastech_cli/test_web_oauth_dispatch.py, tests/plugins/dashboard_auth/test_nastech_provider.py, tests/plugins/image_gen/check_parity_vs_main.py, tests/plugins/image_gen/test_openrouter_compat_provider.py, tests/plugins/test_chronos_verify.py, tests/run_agent/test_anthropic_prompt_cache_policy.py, tests/run_agent/test_primary_runtime_restore.py, tests/run_agent/test_provider_attribution_headers.py, tests/run_agent/test_provider_fallback.py, tests/run_agent/test_provider_parity.py, tests/run_agent/test_run_agent.py, tests/run_agent/test_switch_model_reapplies_headers.py, tests/test_install_ps1_uv_powershell_host.py, tests/tools/test_delegate.py, tests/tools/test_managed_media_gateways.py, tests/tools/test_managed_tool_gateway.py, tests/tools/test_tts_openai_config.py, tests/tools/test_url_safety.py, tests/tools/test_web_tools_config.py, tools/managed_tool_gateway.py, tools/mcp_oauth.py, tools/skills_hub.py, tools/skills_sync_client.py, trajectory_compressor.py, ui-tui/scripts/billing-fixtures.tsx, ui-tui/src/__tests__/subscriptionCommand.test.ts, ui-tui/src/__tests__/subscriptionOverlay.test.tsx, ui-tui/src/app/slash/commands/subscription.ts, ui-tui/src/domain/paths.ts, uv.lock, web/src/components/SidebarFooter.tsx, web/src/pages/DocsPage.tsx, web/src/pages/SystemPage.tsx, website/docs/developer-guide/contributing.md, website/docs/developer-guide/egress-internals.md, website/docs/getting-started/installation.md, website/docs/getting-started/platform-support.md, website/docs/getting-started/quickstart.md, website/docs/getting-started/termux.md, website/docs/guides/run-nastech-with-nastech-portal.md, website/docs/guides/run-nemotron-3-ultra-free.md, website/docs/index.mdx, website/docs/integrations/nastech-portal.md, website/docs/integrations/providers.md, website/docs/reference/cli-commands.md, website/docs/reference/environment-variables.md, website/docs/reference/faq.md, website/docs/reference/model-catalog.md, website/docs/user-guide/desktop.md, website/docs/user-guide/egress/iron-proxy.md, website/docs/user-guide/features/browser.md, website/docs/user-guide/features/image-generation.md, website/docs/user-guide/features/skills.md, website/docs/user-guide/features/subscription-proxy.md, website/docs/user-guide/features/tool-gateway.md, website/docs/user-guide/features/tools.md, website/docs/user-guide/features/tts.md, website/docs/user-guide/features/web-dashboard.md, website/docs/user-guide/features/web-search.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/windows-wsl-quickstart.md, website/docusaurus.config.ts, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/contributing.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/quickstart.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-nastech-with-nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/index.mdx, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/providers.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/faq.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/model-catalog.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/subscription-proxy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tools.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tts.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-native.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-wsl-quickstart.md, website/scripts/generate-llms-txt.py, website/scripts/prebuild.mjs, website/static/api/model-catalog.json


## Direct upstream tree delta

- complete: +111 ~266 -1 ↪0
- MODIFIED `AGENTS.md`
- MODIFIED `agent/agent_init.py`
- MODIFIED `agent/agent_runtime_helpers.py`
- MODIFIED `agent/background_review.py`
- MODIFIED `agent/chat_completion_helpers.py`
- MODIFIED `agent/context_compressor.py`
- MODIFIED `agent/conversation_compression.py`
- MODIFIED `agent/conversation_loop.py`
- MODIFIED `agent/copilot_acp_client.py`
- MODIFIED `agent/gemini_native_adapter.py`
- MODIFIED `agent/prompt_builder.py`
- ADDED `agent/repetition_guard.py`
- MODIFIED `agent/secret_sources/bitwarden.py`
- MODIFIED `agent/shell_hooks.py`
- MODIFIED `agent/skill_utils.py`
- MODIFIED `agent/system_prompt.py`
- MODIFIED `agent/tool_executor.py`
- MODIFIED `agent/transports/chat_completions.py`
- MODIFIED `agent/transports/codex.py`
- MODIFIED `agent/turn_finalizer.py`
- MODIFIED `agent/verification_evidence.py`
- MODIFIED `apps/desktop/electron/backend-ownership.test.ts`
- MODIFIED `apps/desktop/electron/backend-ownership.ts`
- MODIFIED `apps/desktop/electron/connection-registry.test.ts`
- MODIFIED `apps/desktop/electron/connection-registry.ts`
- ADDED `apps/desktop/electron/gitlock.test.ts`
- ADDED `apps/desktop/electron/gitlock.ts`
- MODIFIED `apps/desktop/electron/main.ts`
- ADDED `apps/desktop/electron/parent-process-identity.test.ts`
- ADDED `apps/desktop/electron/parent-process-identity.ts`
- ADDED `apps/desktop/electron/pool-eviction.test.ts`
- ADDED `apps/desktop/electron/pool-eviction.ts`
- MODIFIED `apps/desktop/electron/preload.ts`
- MODIFIED `apps/desktop/electron/profile-session-routing.test.ts`
- MODIFIED `apps/desktop/electron/profile-session-routing.ts`
- MODIFIED `apps/desktop/electron/venv-blocker-scan.test.ts`
- MODIFIED `apps/desktop/electron/venv-blocker-scan.ts`
- MODIFIED `apps/desktop/src/app/chat/composer/controls.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/controls.tsx`
- ADDED `apps/desktop/src/app/chat/composer/hooks/use-composer-esc-cancel.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/composer/hooks/use-composer-esc-cancel.ts`
- MODIFIED `apps/desktop/src/app/chat/composer/hooks/use-composer-submit.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/index.tsx`
- MODIFIED `apps/desktop/src/app/chat/session-tile-actions.ts`
- MODIFIED `apps/desktop/src/app/chat/session-view.test.ts`
- MODIFIED `apps/desktop/src/app/chat/session-view.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/index.tsx`
- ADDED `apps/desktop/src/app/chat/sidebar/profile-rail-connect.test.tsx`
- ADDED `apps/desktop/src/app/chat/sidebar/profile-scope.test.ts`
- ADDED `apps/desktop/src/app/chat/sidebar/profile-scope.ts`
- MODIFIED `apps/desktop/src/app/chat/sidebar/profile-switcher.tsx`
- ADDED `apps/desktop/src/app/chat/transcript-backfill.test.ts`
- ADDED `apps/desktop/src/app/chat/transcript-backfill.ts`
- MODIFIED `apps/desktop/src/app/command-palette/index.tsx`
- MODIFIED `apps/desktop/src/app/contrib/hooks/use-background-sync.ts`
- MODIFIED `apps/desktop/src/app/contrib/hooks/use-desktop-integrations.ts`
- ADDED `apps/desktop/src/app/contrib/mcp-install-deeplink-dialog.tsx`
- MODIFIED `apps/desktop/src/app/contrib/wiring.tsx`
- MODIFIED `apps/desktop/src/app/gateway/hooks/use-gateway-boot.ts`
- MODIFIED `apps/desktop/src/app/learning/archive-skill-confirm-dialog.tsx`
- MODIFIED `apps/desktop/src/app/master-detail.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/gateway-event.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/index.ts`
- ADDED `apps/desktop/src/app/session/hooks/use-message-stream/provider-wait-event.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/session-info-side-effects.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/utils.test.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-message-stream/utils.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/index.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/index.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/rewind.test.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/rewind.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/submit.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/utils.test.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-prompt-actions/utils.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-actions.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-actions/index.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-actions/resolve-stored-session.test.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-actions/utils.test.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-actions/utils.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-list-actions.test.tsx`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-list-actions.ts`
- MODIFIED `apps/desktop/src/app/session/hooks/use-session-state-cache.ts`
- MODIFIED `apps/desktop/src/app/settings/toolset-config-panel.tsx`
- MODIFIED `apps/desktop/src/app/settings/use-deep-link-highlight.ts`
- MODIFIED `apps/desktop/src/app/shell/model-catalog-menu.tsx`
- ADDED `apps/desktop/src/app/skills/embedded-hub-picker.tsx`
- DELETED `apps/desktop/src/app/skills/hub.tsx`
- MODIFIED `apps/desktop/src/app/skills/index.test.tsx`
- MODIFIED `apps/desktop/src/app/skills/index.tsx`
- MODIFIED `apps/desktop/src/app/skills/mcp-tab.tsx`
- MODIFIED `apps/desktop/src/app/types.ts`
- ADDED `apps/desktop/src/app/updates-overlay.blockers.test.tsx`
- MODIFIED `apps/desktop/src/app/updates-overlay.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/assistant-message.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/status.test.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/thread/status.tsx`
- MODIFIED `apps/desktop/src/global.d.ts`
- MODIFIED `apps/desktop/src/hermes.test.ts`
- MODIFIED `apps/desktop/src/hermes.ts`
- MODIFIED `apps/desktop/src/i18n/ar.ts`
- MODIFIED `apps/desktop/src/i18n/en.ts`
- MODIFIED `apps/desktop/src/i18n/ja.ts`
- MODIFIED `apps/desktop/src/i18n/types.ts`
- MODIFIED `apps/desktop/src/i18n/zh-hant.ts`
- MODIFIED `apps/desktop/src/i18n/zh.ts`
- MODIFIED `apps/desktop/src/lib/chat-messages.ts`
- MODIFIED `apps/desktop/src/lib/chat-runtime.ts`
- MODIFIED `apps/desktop/src/lib/json-rpc-gateway-url-guard.test.ts`
- MODIFIED `apps/desktop/src/lib/keybinds/combo.test.ts`
- MODIFIED `apps/desktop/src/lib/keybinds/combo.ts`
- ADDED `apps/desktop/src/lib/mcp-cost.test.ts`
- ADDED `apps/desktop/src/lib/mcp-cost.ts`
- ADDED `apps/desktop/src/lib/mcp-deeplink.test.ts`
- ADDED `apps/desktop/src/lib/mcp-deeplink.ts`
- ADDED `apps/desktop/src/lib/mcp-import.test.ts`
- ADDED `apps/desktop/src/lib/mcp-import.ts`
- ADDED `apps/desktop/src/lib/mcp-probe-cache.test.ts`
- ADDED `apps/desktop/src/lib/mcp-probe-cache.ts`
- MODIFIED `apps/desktop/src/plugins/example/plugin.tsx`
- ADDED `apps/desktop/src/sdk/host-state.test.ts`
- ADDED `apps/desktop/src/sdk/index.test.ts`
- MODIFIED `apps/desktop/src/sdk/index.ts`
- ADDED `apps/desktop/src/store/gateway-agent-scope.test.ts`
- ADDED `apps/desktop/src/store/gateway-connection-lifecycle.test.ts`
- MODIFIED `apps/desktop/src/store/gateway.ts`
- MODIFIED `apps/desktop/src/store/hub-actions.ts`
- ADDED `apps/desktop/src/store/mcp-deeplink-install.ts`
- ADDED `apps/desktop/src/store/mcp-health.test.ts`
- ADDED `apps/desktop/src/store/mcp-health.ts`
- MODIFIED `apps/desktop/src/store/onboarding.ts`
- ADDED `apps/desktop/src/store/profile-agent-activation.test.ts`
- MODIFIED `apps/desktop/src/store/profile.test.ts`
- MODIFIED `apps/desktop/src/store/profile.ts`
- ADDED `apps/desktop/src/store/provider-wait.ts`
- MODIFIED `apps/desktop/src/store/session-states.ts`
- ADDED `apps/desktop/src/store/transcript-tail.ts`
- MODIFIED `apps/desktop/src/store/updates.test.ts`
- MODIFIED `apps/desktop/src/store/updates.ts`
- MODIFIED `apps/desktop/src/types/hermes.ts`
- MODIFIED `apps/shared/src/index.ts`
- MODIFIED `apps/shared/src/json-rpc-gateway.ts`
- MODIFIED `batch_runner.py`
- MODIFIED `cli-config.yaml.example`
- MODIFIED `cli.py`
- ADDED `contributors/emails/1373636680@qq.com`
- ADDED `contributors/emails/2436887475@qq.com`
- ADDED `contributors/emails/3Nya3@users.noreply.github.com`
- ADDED `contributors/emails/807847218@qq.com`
- ADDED `contributors/emails/Nikola@PlayForm.Cloud`
- ADDED `contributors/emails/cursoragent@cursor.com`
- ADDED `contributors/emails/d@rko.rs`
- ADDED `contributors/emails/dqdung205@gmail.com`
- ADDED `contributors/emails/fukutake@convi.ne.jp`
- ADDED `contributors/emails/junhaowanggg@gmail.com`
- ADDED `contributors/emails/justin@bowes.org`
- ADDED `contributors/emails/lepetitprince716-prog@users.noreply.github.com`
- ADDED `contributors/emails/noreply@anthropic.com`
- ADDED `contributors/emails/ohs2251@naver.com`
- ADDED `contributors/emails/ojassharma16@gmail.com`
- ADDED `contributors/emails/pa.sen@outlook.com`
- ADDED `contributors/emails/professorpalmer9@gmail.com`
- ADDED `contributors/emails/rgerrish@outlook.com`
- ADDED `contributors/emails/uplink.punks-1k@icloud.com`
- ADDED `contributors/emails/yflmq001@users.noreply.github.com`
- MODIFIED `cron/lifecycle_guard.py`
- MODIFIED `cron/scheduler.py`
- MODIFIED `docs/observability/README.md`
- ADDED `evals/compaction/README.md`
- ADDED `evals/compaction/fixtures.py`
- ADDED `evals/compaction/policies.py`
- ADDED `evals/compaction/report.py`
- ADDED `evals/compaction/results/SCORECARD-2026-08-15.md`
- ADDED `evals/compaction/results/codex-arm-2026-08-15/acp.json`
- ADDED `evals/compaction/results/codex-arm-2026-08-15/gui.json`
- ADDED `evals/compaction/results/codex-arm-2026-08-15/prmerge.json`
- ADDED `evals/compaction/results/codex-arm-2026-08-15/sweep.json`
- ADDED `evals/compaction/runner.py`
- ADDED `evals/compaction/scripts/build_html_report.py`
- ADDED `evals/compaction/scripts/codex_arm.py`
- ADDED `evals/compaction/scripts/reconstruct_lineage.py`
- ADDED `evals/compaction/scripts/replay_lineage.py`
- ADDED `evals/compaction/test_region_scoping.py`
- MODIFIED `gateway/platforms/base.py`
- MODIFIED `gateway/platforms/webhook.py`
- MODIFIED `gateway/run.py`
- MODIFIED `gateway/session_state.py`
- MODIFIED `gateway/slash_commands.py`
- MODIFIED `hermes_cli/_early_recovery.py`
- MODIFIED `hermes_cli/_install_repair.py`
- MODIFIED `hermes_cli/_parser.py`
- MODIFIED `hermes_cli/_scan_venv_blockers.py`
- MODIFIED `hermes_cli/_subprocess_compat.py`
- MODIFIED `hermes_cli/auth.py`
- MODIFIED `hermes_cli/backup.py`
- MODIFIED `hermes_cli/banner.py`
- MODIFIED `hermes_cli/claw.py`
- MODIFIED `hermes_cli/config_defaults.py`
- MODIFIED `hermes_cli/dashboard_procs.py`
- MODIFIED `hermes_cli/env_loader.py`
- ADDED `hermes_cli/foreign_sessions.py`
- MODIFIED `hermes_cli/gateway.py`
- MODIFIED `hermes_cli/gateway_windows.py`
- ADDED `hermes_cli/gitlock.py`
- MODIFIED `hermes_cli/inventory.py`
- MODIFIED `hermes_cli/main.py`
- MODIFIED `hermes_cli/mcp_config.py`
- MODIFIED `hermes_cli/model_setup_flows.py`
- MODIFIED `hermes_cli/plugins.py`
- MODIFIED `hermes_cli/prompt_size.py`
- MODIFIED `hermes_cli/pt_input_extras.py`
- MODIFIED `hermes_cli/runtime_provider.py`
- MODIFIED `hermes_cli/sessions_cmd.py`
- MODIFIED `hermes_cli/skills_hub.py`
- MODIFIED `hermes_cli/stderr_timestamp.py`
- ADDED `hermes_cli/terminal_breadcrumbs.py`
- MODIFIED `hermes_cli/tools_config.py`
- MODIFIED `hermes_cli/update_cmd.py`
- MODIFIED `hermes_cli/web_routers/mcp.py`
- MODIFIED `hermes_cli/web_server.py`
- MODIFIED `hermes_state.py`
- MODIFIED `hermes_state_common.py`
- MODIFIED `model_tools.py`
- MODIFIED `plugins/observability/nemo_relay/__init__.py`
- MODIFIED `plugins/platforms/discord/adapter.py`
- MODIFIED `plugins/platforms/telegram/adapter.py`
- MODIFIED `run_agent.py`
- MODIFIED `scripts/desktop-update/posix.sh`
- MODIFIED `scripts/install.sh`
- MODIFIED `skills/autonomous-ai-agents/computer-use/SKILL.md`
- MODIFIED `skills/autonomous-ai-agents/hermes-agent/references/desktop-plugins.md`
- ADDED `tests/agent/test_background_review_usage.py`
- MODIFIED `tests/agent/test_bedrock_interrupt_post_worker.py`
- MODIFIED `tests/agent/test_copilot_acp_client.py`
- MODIFIED `tests/agent/test_gemini_native_adapter.py`
- ADDED `tests/agent/test_hygiene_timeout_cooldown_isolation.py`
- MODIFIED `tests/agent/test_reasoning_stale_timeout_floor.py`
- ADDED `tests/agent/test_repetition_guard.py`
- MODIFIED `tests/agent/test_shell_hooks.py`
- MODIFIED `tests/agent/test_skill_utils.py`
- MODIFIED `tests/agent/test_turn_finalizer_iteration_limit_exit.py`
- MODIFIED `tests/agent/test_verification_evidence.py`
- MODIFIED `tests/agent/transports/test_chat_completions.py`
- MODIFIED `tests/agent/transports/test_codex_transport.py`
- MODIFIED `tests/cli/test_cli_provider_resolution.py`
- MODIFIED `tests/cli/test_exit_watchdog_signal_arm.py`
- ADDED `tests/cli/test_modify_other_keys_aliases.py`
- MODIFIED `tests/cli/test_worktree.py`
- MODIFIED `tests/cron/test_cron_no_agent.py`
- ADDED `tests/cron/test_cron_run_stale_claim_reap_86721.py`
- MODIFIED `tests/cron/test_cron_script.py`
- ADDED `tests/fixtures/session-resume-active-turn.json`
- ADDED `tests/gateway/test_baseexception_turn_notify.py`
- ADDED `tests/gateway/test_discord_split_cap.py`
- ADDED `tests/gateway/test_finalize_session_off_loop.py`
- MODIFIED `tests/gateway/test_hygiene_failure_cooldown_ladder.py`
- ADDED `tests/gateway/test_local_model_connection_reply.py`
- MODIFIED `tests/gateway/test_loop_command.py`
- ADDED `tests/gateway/test_model_command_profile_config.py`
- MODIFIED `tests/gateway/test_session_hygiene.py`
- MODIFIED `tests/gateway/test_status_command.py`
- MODIFIED `tests/gateway/test_telegram_auth_check.py`
- MODIFIED `tests/gateway/test_telegram_reply_mode.py`
- MODIFIED `tests/gateway/test_usage_command.py`
- MODIFIED `tests/gateway/test_webhook_adapter.py`
- ADDED `tests/hermes_cli/test_auth_provider_scope.py`
- MODIFIED `tests/hermes_cli/test_backup.py`
- ADDED `tests/hermes_cli/test_bedrock_mantle_key_env.py`
- ADDED `tests/hermes_cli/test_bounded_probe_run.py`
- ADDED `tests/hermes_cli/test_chat_c_fail_loudly.py`
- MODIFIED `tests/hermes_cli/test_cli_startup_model_cost_guard.py`
- MODIFIED `tests/hermes_cli/test_cmd_update.py`
- MODIFIED `tests/hermes_cli/test_dashboard_admin_endpoints.py`
- MODIFIED `tests/hermes_cli/test_early_recovery.py`
- MODIFIED `tests/hermes_cli/test_env_loader.py`
- ADDED `tests/hermes_cli/test_foreign_sessions.py`
- MODIFIED `tests/hermes_cli/test_gateway.py`
- MODIFIED `tests/hermes_cli/test_gateway_external_supervisor.py`
- ADDED `tests/hermes_cli/test_gateway_foreign_xdg_runtime.py`
- MODIFIED `tests/hermes_cli/test_gateway_restart_loop.py`
- MODIFIED `tests/hermes_cli/test_gateway_service.py`
- MODIFIED `tests/hermes_cli/test_gateway_windows.py`
- ADDED `tests/hermes_cli/test_imagegen_managed_gateway.py`
- MODIFIED `tests/hermes_cli/test_inventory.py`
- MODIFIED `tests/hermes_cli/test_plugins.py`
- ADDED `tests/hermes_cli/test_quarantine_noop_restore.py`
- MODIFIED `tests/hermes_cli/test_runtime_provider_resolution.py`
- MODIFIED `tests/hermes_cli/test_scan_venv_blockers.py`
- MODIFIED `tests/hermes_cli/test_serve_parent_watchdog.py`
- MODIFIED `tests/hermes_cli/test_sessions_delete.py`
- MODIFIED `tests/hermes_cli/test_stderr_timestamp.py`
- ADDED `tests/hermes_cli/test_terminal_breadcrumbs.py`
- MODIFIED `tests/hermes_cli/test_tools_config.py`
- MODIFIED `tests/hermes_cli/test_tui_npm_install.py`
- ADDED `tests/hermes_cli/test_update_secret_import_lock.py`
- MODIFIED `tests/hermes_cli/test_update_self_lock.py`
- MODIFIED `tests/hermes_cli/test_update_stale_dashboard.py`
- MODIFIED `tests/hermes_cli/test_web_server.py`
- MODIFIED `tests/hermes_cli/test_web_server_profile_unification.py`
- MODIFIED `tests/hermes_cli/test_web_ui_build.py`
- MODIFIED `tests/hermes_state/test_aux_usage_accounting.py`
- ADDED `tests/hermes_state/test_session_lifecycle_status.py`
- ADDED `tests/plugins/test_nemo_relay_bounded_marks.py`
- MODIFIED `tests/run_agent/test_agent_guardrails.py`
- MODIFIED `tests/run_agent/test_anthropic_prompt_cache_policy.py`
- MODIFIED `tests/run_agent/test_background_review.py`
- MODIFIED `tests/run_agent/test_background_review_cost_controls.py`
- ADDED `tests/run_agent/test_continuation_repetition_guard.py`
- MODIFIED `tests/run_agent/test_cross_process_turn_lease.py`
- MODIFIED `tests/run_agent/test_run_agent.py`
- MODIFIED `tests/run_agent/test_sequential_tool_timeout.py`
- MODIFIED `tests/run_agent/test_stream_stale_circuit_breaker.py`
- MODIFIED `tests/run_agent/test_tool_call_guardrail_runtime.py`
- MODIFIED `tests/state/test_compression_lineage_guard.py`
- ADDED `tests/test_batch_runner_exit_code.py`
- ADDED `tests/test_compression_watermark_commit.py`
- ADDED `tests/test_gitlock.py`
- MODIFIED `tests/test_hermes_state.py`
- MODIFIED `tests/test_hermes_state_compression_busy_retry.py`
- MODIFIED `tests/test_tui_gateway_queue_on_busy.py`
- MODIFIED `tests/test_tui_gateway_server.py`
- MODIFIED `tests/tools/test_browser_use_cli.py`
- ADDED `tests/tools/test_computer_use_browser_authorization.py`
- MODIFIED `tests/tools/test_computer_use_cua_0_9.py`
- ADDED `tests/tools/test_computer_use_display_count_guard.py`
- ADDED `tests/tools/test_computer_use_empty_discovery_diagnosis.py`
- ADDED `tests/tools/test_computer_use_input_target_guard.py`
- ADDED `tests/tools/test_computer_use_placeholder_ids.py`
- ADDED `tests/tools/test_computer_use_zero_bounds.py`
- MODIFIED `tests/tools/test_mcp_oauth.py`
- MODIFIED `tests/tools/test_mcp_oauth_manager.py`
- MODIFIED `tests/tools/test_mcp_tool.py`
- ADDED `tests/tools/test_single_query_approval_mode.py`
- MODIFIED `tests/tools/test_skill_bundle_provenance.py`
- MODIFIED `tests/tools/test_terminal_hints.py`
- ADDED `tests/tui_gateway/test_image_ref_message.py`
- MODIFIED `tests/tui_gateway/test_protocol.py`
- MODIFIED `tests/tui_gateway/test_session_resume_db_ownership.py`
- MODIFIED `tests/tui_gateway/test_undo_command.py`
- MODIFIED `tools/approval.py`
- MODIFIED `tools/browser_use_cli.py`
- MODIFIED `tools/computer_use/browser_route.py`
- MODIFIED `tools/computer_use/cua_backend.py`
- MODIFIED `tools/computer_use/doctor.py`
- MODIFIED `tools/computer_use/schema.py`
- MODIFIED `tools/computer_use/tool.py`
- MODIFIED `tools/cronjob_tools.py`
- MODIFIED `tools/mcp_oauth.py`
- MODIFIED `tools/mcp_oauth_manager.py`
- MODIFIED `tools/mcp_tool.py`
- MODIFIED `tools/skills_hub.py`
- MODIFIED `tools/terminal_hints.py`
- MODIFIED `tools/terminal_tool.py`
- MODIFIED `tui_gateway/methods_prompt.py`
- MODIFIED `tui_gateway/methods_session.py`
- MODIFIED `tui_gateway/methods_tools.py`
- MODIFIED `tui_gateway/server.py`
- MODIFIED `web/src/lib/api.ts`
- ADDED `web/src/lib/session-prune.test.ts`
- ADDED `web/src/lib/session-prune.ts`
- MODIFIED `web/src/pages/SessionsPage.tsx`
- MODIFIED `website/docs/developer-guide/context-compression-and-caching.md`
- MODIFIED `website/docs/developer-guide/desktop-plugin-sdk.md`
- MODIFIED `website/docs/reference/cli-commands.md`
- MODIFIED `website/docs/reference/mcp-config-reference.md`
- MODIFIED `website/docs/user-guide/configuration.md`
- MODIFIED `website/docs/user-guide/configuring-models.md`
- MODIFIED `website/docs/user-guide/desktop.md`
- MODIFIED `website/docs/user-guide/features/browser.md`
- MODIFIED `website/docs/user-guide/features/computer-use.md`
- MODIFIED `website/docs/user-guide/features/hooks.md`
- MODIFIED `website/docs/user-guide/features/memory.md`
- ADDED `website/docs/user-guide/multi-connection-desktop.md`
- MODIFIED `website/docs/user-guide/multi-profile-gateways.md`
- MODIFIED `website/docs/user-guide/security.md`
- MODIFIED `website/docs/user-guide/sessions.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/context-compression-and-caching.md`
- MODIFIED `website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/configuration.md`
- MODIFIED `website/sidebars.ts`

## Scan

9470 files scanned [audio=5, binary=7, doc=5, font=13, image=91, text=9349]


## Diff

1161 renamed, 0 rewritten, 7286 identical, 702 locked, 0 missing, 32 owned, 227 reconciled


## Fork check (vs nastech-agent)

- 8985 identical, 372 updated (+0/-0 lines), 111 added, 0 missing, 0 fork-local-unpreserved, 0 stale-upstream, 2 locked/binary, 62 preserved fork-local files, 0 violations

- features: fork 51 -> branded 51

Auto-generated by 100Ways.
