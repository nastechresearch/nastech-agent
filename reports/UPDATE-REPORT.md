# Nastech Update Report #1

- upstream sha : `cc75e8f4021f7efab99158f57601be4d691a6da9`
- source       : `/home/runner/work/100Ways/100Ways/upstream-agent`
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

- total files : 17848
- renamed     : 3016 (folders and file names)
- text-rewritten : 17669
- locked-copied  : 139
- binary-copied  : 8
- owned assets   : 34 (our logo/banner/mascot override upstream)

## Reconcile

- fixed : 398 files reconciled: .env.example, .github/workflows/deploy-site.yml, .github/workflows/deploy-site.yml, .github/workflows/install-e2e-macos-run.yml, .github/workflows/install-e2e-windows-run.yml, .github/workflows/skills-index-freshness.yml, .mailmap, AGENTS.md, CONTRIBUTING.es.md, CONTRIBUTING.md, Dockerfile, README.es.md, README.md, README.ur-pk.md, README.zh-CN.md, SECURITY.es.md, SECURITY.md, agent/agent_runtime_helpers.py, agent/anthropic_adapter.py, agent/anthropic_endpoints.py, agent/auxiliary_client.py, agent/billing_links.py, agent/billing_view.py, agent/chat_completion_helpers.py, agent/conversation_compression.py, agent/conversation_loop.py, agent/model_metadata.py, agent/prompt_builder.py, agent/proxy_sources/iron_proxy.py, agent/reasoning_params.py, agent/subscription_view.py, agent/turn_recovery.py, agent/usage_pricing.py, apps/bootstrap-installer/src-tauri/Cargo.toml, apps/desktop/README.md, apps/desktop/electron-builder.config.cjs, apps/desktop/electron/backend-health.test.ts, apps/desktop/electron/backend-health.ts, apps/desktop/electron/challenge-window.test.ts, apps/desktop/electron/cloud-session-recovery.test.ts, apps/desktop/electron/connection-config.test.ts, apps/desktop/electron/hub-iframe-policy.ts, apps/desktop/electron/oauth-partition.test.ts, apps/desktop/electron/portal-session.ts, apps/desktop/electron/remote-lifecycle.ts, apps/desktop/electron/remote-oauth-ticket.test.ts, apps/desktop/electron/updater/checkout-source.test.ts, apps/desktop/electron/window-open-policy.test.ts, apps/desktop/src/app/capabilities/index.test.tsx, apps/desktop/src/app/capabilities/plugins/plugins-tab.test.tsx, apps/desktop/src/app/capabilities/skills/embedded-hub-picker.tsx, apps/desktop/src/app/chat/sidebar/section-states.tsx, apps/desktop/src/app/messaging/index.test.tsx, apps/desktop/src/app/pet-generate/components/generate-unavailable.tsx, apps/desktop/src/app/settings/billing/api.test.ts, apps/desktop/src/app/settings/billing/dev-fixtures.ts, apps/desktop/src/app/settings/billing/errors.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.test.ts, apps/desktop/src/app/settings/billing/use-billing-state.ts, apps/desktop/src/app/settings/billing/use-charge-poller.test.ts, apps/desktop/src/app/settings/billing/use-step-up.test.tsx, apps/desktop/src/app/settings/constants.ts, apps/desktop/src/app/settings/gateway-settings.test.tsx, apps/desktop/src/app/settings/gateway-settings.tsx, apps/desktop/src/app/settings/toolset-config-panel.test.tsx, apps/desktop/src/components/assistant-ui/tool/fallback-model.test.ts, apps/desktop/src/components/boot-failure-overlay.test.tsx, apps/desktop/src/components/boot-failure-overlay.tsx, apps/desktop/src/components/send-diagnostics-dialog.tsx, apps/desktop/src/components/update-status.tsx, apps/desktop/src/contrib/plugin.ts, apps/desktop/src/i18n/de.ts, apps/desktop/src/i18n/en.ts, apps/desktop/src/i18n/es.ts, apps/desktop/src/i18n/fr.ts, apps/desktop/src/i18n/ja.ts, apps/desktop/src/i18n/ru.ts, apps/desktop/src/i18n/zh-hant_settings.ts, apps/desktop/src/i18n/zh.ts, apps/desktop/src/lib/docs.ts, apps/desktop/src/lib/plugin-catalog.ts, apps/desktop/src/plugins/nastech-bots/skills-hub-picker.test.tsx, apps/desktop/src/plugins/nastech-bots/skills-hub.tsx, apps/desktop/src/sdk/index.ts, apps/desktop/src/store/free-tier-challenge.test.ts, apps/desktop/src/store/shared-metrics.ts, cli-config.yaml.example, eslint.config.shared.mjs, evals/auth_pool_controls.py, evals/browser_use/single_run.py, evals/postmortem/live_ab/auth_stampede.py, evals/postmortem/live_ab/cache_concurrency_probe.py, evals/postmortem/review_probes/cache_estimator_probe.py, evals/postmortem/review_probes/credential_identity_probe.py, nastech_cli/anon_auth.py, nastech_cli/anon_auth.py, nastech_cli/anon_sign_in.py, nastech_cli/auth.py, nastech_cli/auth_codex.py, nastech_cli/auth_constants.py, nastech_cli/auth_error_copy.py, nastech_cli/auth_nastech.py, nastech_cli/banner.py, nastech_cli/config_defaults.py, nastech_cli/dashboard_auth/login_page.py, nastech_cli/dashboard_register.py, nastech_cli/debug.py, nastech_cli/diagnostics_upload.py, nastech_cli/fallback_cmd.py, nastech_cli/kanban_parser.py, nastech_cli/main.py, nastech_cli/main_dashboard.py, nastech_cli/main_desktop.py, nastech_cli/model_catalog.py, nastech_cli/model_setup_flows_common.py, nastech_cli/models.py, nastech_cli/models_pricing.py, nastech_cli/nastech_account.py, nastech_cli/nastech_account.py, nastech_cli/nastech_billing.py, nastech_cli/observability/shared_metrics_consent.py, nastech_cli/observability/shared_metrics_send_config.py, nastech_cli/plugin_catalog.py, nastech_cli/plugins_cmd.py, nastech_cli/portal_cli.py, nastech_cli/providers.py, nastech_cli/proxy/adapters/base.py, nastech_cli/proxy/adapters/nastech_portal.py, nastech_cli/setup.py, nastech_cli/setup_platforms.py, nastech_cli/setup_quick.py, nastech_cli/setup_whatsapp_cloud.py, nastech_cli/skin_engine.py, nastech_cli/source_releases.py, nastech_cli/steward.py, nastech_cli/subcommands/egress.py, nastech_cli/subcommands/fallback.py, nastech_cli/subcommands/secrets.py, nastech_cli/subcommands/worktree.py, nastech_cli/telegram_managed_bot.py, nastech_cli/tools_config.py, nastech_cli/uninstall.py, nastech_cli/update_cmd.py, nastech_cli/update_cmd_maint.py, nastech_cli/update_cmd_zip.py, nastech_cli/web_routers/status.py, nastech_cli/web_server_messaging.py, nastech_cli/web_server_oauth.py, nastech_constants.py, nastech_state_errors.py, optional-skills/productivity/memento-flashcards/SKILL.md, package-lock.json, plugin-catalog/README.md, plugins/dashboard_auth/nastech/__init__.py, plugins/dashboard_auth/nastech/plugin.yaml, plugins/kanban/dashboard/dist/index.js, plugins/kanban/systemd/nastech-kanban-dispatcher.service, plugins/model-providers/ai-gateway/__init__.py, plugins/model-providers/fireworks/__init__.py, plugins/model-providers/kimi-coding/__init__.py, plugins/model-providers/nastech/__init__.py, plugins/model-providers/opencode-zen/__init__.py, plugins/model-providers/solstice/auth.py, plugins/nastech-achievements/dashboard/dist/index.js, plugins/platforms/discord/adapter.py, plugins/platforms/discord/onboarding.py, plugins/platforms/email/adapter.py, plugins/platforms/photon/sidecar/package-lock.json, plugins/platforms/slack/adapter.py, plugins/web/perplexity/provider.py, pm/artifact-mirror.json, pm/uv.lock, scripts/build_model_catalog.py, scripts/contributor_audit.py, scripts/e2e_shared_metrics_staging.py, scripts/install.cmd, scripts/install.ps1, scripts/install.sh, scripts/release.py, scripts/releases/authors_legacy.py, scripts/releases/r2.py, scripts/sandbox/generate-e2e-matrix.mjs, scripts/termux/stage_apt_repo.py, scripts/whatsapp-bridge/package-lock.json, setup.py, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/SKILL.md, skills/autonomous-ai-agents/nastech-agent/references/background-systems.md, skills/autonomous-ai-agents/nastech-agent/references/cli-reference.md, skills/autonomous-ai-agents/nastech-agent/references/configuration.md, skills/autonomous-ai-agents/nastech-agent/references/contributor-guide.md, skills/autonomous-ai-agents/nastech-agent/references/portal-auth-for-third-party-apps.md, skills/autonomous-ai-agents/nastech-agent/references/providers-and-models.md, skills/autonomous-ai-agents/nastech-agent/references/webhooks.md, skills/media/youtube-content/SKILL.md, skills/software-development/python-debugpy/SKILL.md, tests/agent/test_anthropic_adapter.py, tests/agent/test_anthropic_preserved_thinking_replay.py, tests/agent/test_anthropic_prompt_cache_policy.py, tests/agent/test_auxiliary_auth_rung_fallthrough.py, tests/agent/test_auxiliary_client.py, tests/agent/test_auxiliary_client_nastech_401_cache_key.py, tests/agent/test_auxiliary_main_first.py, tests/agent/test_auxiliary_transport_autodetect.py, tests/agent/test_billing_links.py, tests/agent/test_credential_pool.py, tests/agent/test_credential_pool_nastech_refresh_stampede.py, tests/agent/test_credits_cold_start.py, tests/agent/test_credits_policy.py, tests/agent/test_deepseek_anthropic_thinking.py, tests/agent/test_error_classifier.py, tests/agent/test_error_classifier_observed.py, tests/agent/test_fast_mode_auto.py, tests/agent/test_model_metadata.py, tests/agent/test_nastech_credits_gauge.py, tests/agent/test_nastech_key_pre_expiry_adoption.py, tests/agent/test_nastech_portal_anthropic_wire.py, tests/agent/test_nastech_rate_guard.py, tests/agent/test_nastech_welcome_client_contract.py, tests/agent/test_nastech_wire_auto.py, tests/agent/test_nonretryable_result_carries_verdict.py, tests/agent/test_primary_runtime_restore.py, tests/agent/test_provider_attribution_headers.py, tests/agent/test_provider_fallback.py, tests/agent/test_provider_history_parity.py, tests/agent/test_provider_parity.py, tests/agent/test_run_agent.py, tests/agent/test_switch_model_reapplies_headers.py, tests/agent/test_turn_usage_log_line.py, tests/agent/test_welcome_error_identity.py, tests/agent/test_welcome_tier_recovery.py, tests/agent/transports/test_chat_completions.py, tests/agent/transports/test_chat_completions_reasoning_details_replay.py, tests/agent/transports/test_provider_wire_snapshot.py, tests/compat/old_updater_dependencies.py, tests/docker/test_sqlite_runtime.py, tests/e2e/core/live/_helpers.py, tests/e2e/core/providers/test_catalog_oauth.py, tests/e2e/core/providers/test_chat_reasoning_variants.py, tests/e2e/core/providers/test_fallback_providers.py, tests/e2e/core/upgrade/network/_seed.py, tests/e2e/core/upgrade/network/test_proxy_only_egress.py, tests/e2e/core/upgrade/network/test_release_channel_records.py, tests/fakes/providers/chat_variants.py, tests/fixtures/provider_wire_snapshot.json, tests/gateway/test_discord_format.py, tests/gateway/test_free_tier_startup_notice.py, tests/gateway/test_housekeeping_profile_scope.py, tests/gateway/test_internal_event_pin_wiring.py, tests/gateway/test_model_switch_persistence.py, tests/gateway/test_run_progress_topics.py, tests/gateway/test_session_model_override_persistence.py, tests/gateway/test_startup_warmup_profile_scope.py, tests/gateway/test_status_command.py, tests/gateway/test_status_free_tier_line.py, tests/gateway/test_telegram_mention_context.py, tests/gateway/test_usage_command.py, tests/install/macos-desktop-e2e.sh, tests/install/windows-e2e.ps1, tests/nastech_cli/anon_portal.py, tests/nastech_cli/test_anon_auth_core.py, tests/nastech_cli/test_anon_failure_modes.py, tests/nastech_cli/test_anon_failure_modes.py, tests/nastech_cli/test_anon_first_notice.py, tests/nastech_cli/test_anon_picker.py, tests/nastech_cli/test_anon_surfaces.py, tests/nastech_cli/test_anon_upgrade.py, tests/nastech_cli/test_auth_nastech_provider.py, tests/nastech_cli/test_base_url_host_identity.py, tests/nastech_cli/test_cli_first_run_setup.py, tests/nastech_cli/test_cli_init.py, tests/nastech_cli/test_cli_provider_resolution.py, tests/nastech_cli/test_dashboard_register.py, tests/nastech_cli/test_fireworks_provider.py, tests/nastech_cli/test_local_abandoned_requests.py, tests/nastech_cli/test_local_quickstart.py, tests/nastech_cli/test_model_catalog.py, tests/nastech_cli/test_model_validation.py, tests/nastech_cli/test_nastech_anthropic_wire_default.py, tests/nastech_cli/test_nastech_auth_keepalive.py, tests/nastech_cli/test_nastech_auth_status_cache.py, tests/nastech_cli/test_nastech_inference_url_validation.py, tests/nastech_cli/test_nastech_nonproduction_inference_host.py, tests/nastech_cli/test_nastech_nonproduction_inference_host.py, tests/nastech_cli/test_nastech_portal_staging_allowlist.py, tests/nastech_cli/test_nastech_reasoning_metadata.py, tests/nastech_cli/test_proxy.py, tests/nastech_cli/test_reasoning_caps_disk_cache.py, tests/nastech_cli/test_sale_pricing.py, tests/nastech_cli/test_show_config_credential.py, tests/nastech_cli/test_source_channel_integration.py, tests/nastech_cli/test_source_check.py, tests/nastech_cli/test_update_target_identity.py, tests/nastech_cli/test_web_oauth_dispatch.py, tests/plugins/dashboard_auth/test_nastech_provider.py, tests/plugins/image_gen/check_parity_vs_main.py, tests/plugins/image_gen/test_openrouter_compat_provider.py, tests/plugins/test_chronos_verify.py, tests/scripts/test_release_build_commit.py, tests/scripts/test_release_r2.py, tests/scripts/test_release_r2.py, tests/scripts/test_stage_apt_repo.py, tests/scripts/test_upload_summary.py, tests/tools/test_delegate.py, tests/tools/test_managed_media_gateways.py, tests/tools/test_managed_tool_gateway.py, tests/tools/test_stage2_hook_nastech_routing_env.py, tests/tools/test_strict_provider_selection.py, tests/tools/test_tts_openai_config.py, tests/tools/test_url_safety.py, tests/tools/test_web_tools_config.py, tests/tools/test_web_tools_perplexity.py, tests/tui_gateway/test_free_tier_rpc.py, tests/tui_gateway/test_resume_switched_provider_endpoint.py, tools/managed_gateway_auth.py, tools/managed_tool_gateway.py, tools/mcp_oauth.py, tools/skills_hub_search.py, trajectory_compressor.py, ui-tui/scripts/billing-fixtures.tsx, ui-tui/src/__tests__/subscriptionCommand.test.ts, ui-tui/src/__tests__/subscriptionOverlay.test.tsx, ui-tui/src/app/slash/commands/subscription.ts, ui-tui/src/domain/paths.ts, uv.lock, web/src/components/SharedMetricsConsentBanner.tsx, web/src/components/SidebarFooter.tsx, web/src/pages/DocsPage.tsx, web/src/pages/PluginsPage.tsx, web/src/pages/SystemPage.tsx, website/README.md, website/docs/developer-guide/egress-internals.md, website/docs/developer-guide/stable-releases.md, website/docs/getting-started/installation.md, website/docs/getting-started/platform-support.md, website/docs/getting-started/quickstart.md, website/docs/getting-started/termux.md, website/docs/guides/manage-nastech-cloud-with-mcp.md, website/docs/guides/run-nastech-with-nastech-portal.md, website/docs/guides/run-nemotron-3-ultra-free.md, website/docs/index.mdx, website/docs/integrations/nastech-portal.md, website/docs/integrations/providers.md, website/docs/reference/cli-commands.md, website/docs/reference/environment-variables.md, website/docs/reference/faq.md, website/docs/reference/model-catalog.md, website/docs/user-guide/desktop.md, website/docs/user-guide/egress/iron-proxy.md, website/docs/user-guide/features/browser.md, website/docs/user-guide/features/image-generation.md, website/docs/user-guide/features/plugin-catalog.md, website/docs/user-guide/features/skills.md, website/docs/user-guide/features/subscription-proxy.md, website/docs/user-guide/features/tool-gateway.md, website/docs/user-guide/features/tools.md, website/docs/user-guide/features/tts.md, website/docs/user-guide/features/web-dashboard.md, website/docs/user-guide/features/web-search.md, website/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/docs/user-guide/skills/bundled/media/media-youtube-content.md, website/docs/user-guide/skills/bundled/software-development/software-development-python-debugpy.md, website/docs/user-guide/skills/optional/productivity/productivity-memento-flashcards.md, website/docs/user-guide/windows-native.md, website/docs/user-guide/windows-wsl-quickstart.md, website/docusaurus.config.ts, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/developer-guide/plugins/index.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/quickstart.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/termux.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-nastech-with-nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/index.mdx, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nastech-portal.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/providers.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/cli-commands.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/environment-variables.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/faq.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/reference/model-catalog.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/browser.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/image-generation.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/subscription-proxy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tool-gateway.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tools.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/tts.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/web-search.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-nastech-agent.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/media/media-youtube-content.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/bundled/software-development/software-development-python-debugpy.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/skills/optional/productivity/productivity-memento-flashcards.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-native.md, website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/windows-wsl-quickstart.md, website/scripts/fetch-plugin-stars.py, website/scripts/generate-llms-txt.py, website/scripts/prebuild.mjs, website/src/pages/plugins/index.tsx, website/src/pages/skills/index.tsx, website/static/api/model-catalog.json, website/static/oauth/client-metadata.json


## Direct upstream tree delta

- complete: +20 ~116 -0 ↪0
- MODIFIED `agent/turn_facade_lease.py`
- MODIFIED `agent/usage_pricing.py`
- MODIFIED `apps/desktop/DESIGN.md`
- MODIFIED `apps/desktop/e2e/fixtures.ts`
- MODIFIED `apps/desktop/electron/desktop-installation.test.ts`
- MODIFIED `apps/desktop/electron/desktop-installation.ts`
- MODIFIED `apps/desktop/electron/desktop-uninstall-ipc.test.ts`
- MODIFIED `apps/desktop/electron/entry.ts`
- MODIFIED `apps/desktop/electron/handoff-result-producer.test.ts`
- MODIFIED `apps/desktop/electron/handoff-result.test.ts`
- MODIFIED `apps/desktop/electron/handoff-result.ts`
- MODIFIED `apps/desktop/electron/host-backend-singleton-orphan-reap.test.ts`
- MODIFIED `apps/desktop/electron/link-title-window.test.ts`
- MODIFIED `apps/desktop/electron/link-title-window.ts`
- MODIFIED `apps/desktop/electron/main.ts`
- ADDED `apps/desktop/electron/remote-lifecycle-profile-missing.test.ts`
- MODIFIED `apps/desktop/electron/remote-lifecycle.ts`
- MODIFIED `apps/desktop/electron/remote-update-marker-programs.test.ts`
- MODIFIED `apps/desktop/electron/update-marker-corpus.test.ts`
- MODIFIED `apps/desktop/electron/update-marker-gate.test.ts`
- MODIFIED `apps/desktop/electron/update-marker-gate.ts`
- MODIFIED `apps/desktop/electron/update-marker-readonly.test.ts`
- MODIFIED `apps/desktop/electron/update-marker.test.ts`
- MODIFIED `apps/desktop/electron/updater/checkout-handoff.test.ts`
- MODIFIED `apps/desktop/electron/updater/marker-helper.test.ts`
- MODIFIED `apps/desktop/electron/updater/marker-helper.ts`
- MODIFIED `apps/desktop/electron/windows-remote-lifecycle.test.ts`
- MODIFIED `apps/desktop/electron/windows-remote-lifecycle.ts`
- MODIFIED `apps/desktop/electron/zoom.test.ts`
- MODIFIED `apps/desktop/electron/zoom.ts`
- MODIFIED `apps/desktop/src/api/messaging.ts`
- MODIFIED `apps/desktop/src/api/system.ts`
- MODIFIED `apps/desktop/src/app/chat/composer/hooks/use-composer-draft.ts`
- MODIFIED `apps/desktop/src/app/chat/composer/hooks/use-voice-recorder.ts`
- MODIFIED `apps/desktop/src/app/chat/sidebar/project-dialog.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/projects/project-menu.test.tsx`
- MODIFIED `apps/desktop/src/app/chat/sidebar/projects/project-menu.tsx`
- MODIFIED `apps/desktop/src/app/contrib/wiring-background-queue-drain.test.tsx`
- MODIFIED `apps/desktop/src/app/cron/index.test.tsx`
- MODIFIED `apps/desktop/src/app/cron/index.tsx`
- MODIFIED `apps/desktop/src/app/open-session.test.ts`
- MODIFIED `apps/desktop/src/app/settings/constants.ts`
- MODIFIED `apps/desktop/src/app/settings/model-settings.test.tsx`
- MODIFIED `apps/desktop/src/app/settings/model-settings.tsx`
- MODIFIED `apps/desktop/src/app/settings/uninstall-section.test.tsx`
- MODIFIED `apps/desktop/src/app/shell/butterbar.tsx`
- MODIFIED `apps/desktop/src/app/shell/model-catalog-menu.test.tsx`
- MODIFIED `apps/desktop/src/app/shell/model-catalog-menu.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/catalog-advanced-dialog.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/catalog-install-tool.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/markdown-text.media-md.test.tsx`
- MODIFIED `apps/desktop/src/components/assistant-ui/markdown-text.tsx`
- MODIFIED `apps/desktop/src/components/pane-shell/tree/renderer/tree-split.test.tsx`
- ADDED `apps/desktop/src/hooks/use-media-image.frames.test.tsx`
- MODIFIED `apps/desktop/src/i18n/ar_common.ts`
- MODIFIED `apps/desktop/src/i18n/de.ts`
- ADDED `apps/desktop/src/i18n/de_projects.ts`
- MODIFIED `apps/desktop/src/i18n/en.ts`
- ADDED `apps/desktop/src/i18n/en_projects.ts`
- MODIFIED `apps/desktop/src/i18n/en_shared_metrics.ts`
- MODIFIED `apps/desktop/src/i18n/es.ts`
- ADDED `apps/desktop/src/i18n/es_projects.ts`
- MODIFIED `apps/desktop/src/i18n/fr.ts`
- ADDED `apps/desktop/src/i18n/fr_projects.ts`
- MODIFIED `apps/desktop/src/i18n/ja.ts`
- ADDED `apps/desktop/src/i18n/ja_projects.ts`
- MODIFIED `apps/desktop/src/i18n/ru.ts`
- ADDED `apps/desktop/src/i18n/ru_projects.ts`
- MODIFIED `apps/desktop/src/i18n/types.ts`
- ADDED `apps/desktop/src/i18n/types_projects.ts`
- MODIFIED `apps/desktop/src/i18n/zh-hant.ts`
- MODIFIED `apps/desktop/src/i18n/zh.ts`
- ADDED `apps/desktop/src/i18n/zh_projects.ts`
- MODIFIED `apps/desktop/src/i18n/zh_shared_metrics.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/group-chat-view-members.test.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/group-round-prompt.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/group-rounds.test.ts`
- MODIFIED `apps/desktop/src/plugins/nastech-bots/group-turns.ts`
- MODIFIED `apps/desktop/src/store/butterbar.ts`
- MODIFIED `apps/desktop/src/store/free-tier-challenge.test.ts`
- MODIFIED `apps/desktop/src/store/free-tier-challenge.ts`
- MODIFIED `apps/desktop/src/store/layout-dismissed-projects.test.ts`
- MODIFIED `apps/desktop/src/store/layout.ts`
- MODIFIED `apps/desktop/src/store/projects.ts`
- MODIFIED `apps/desktop/src/store/session-states.test.ts`
- MODIFIED `apps/desktop/src/store/zoom.ts`
- MODIFIED `apps/desktop/src/styles.css`
- MODIFIED `gateway/run.py`
- MODIFIED `nastech_cli/auth.py`
- ADDED `nastech_cli/auth_external_process.py`
- MODIFIED `nastech_cli/dashboard_auth/routes.py`
- MODIFIED `nastech_cli/kanban_boards.py`
- MODIFIED `nastech_cli/kanban_db.py`
- ADDED `nastech_cli/kanban_db_boards.py`
- MODIFIED `nastech_cli/kanban_db_connect.py`
- MODIFIED `nastech_cli/model_switch_providers.py`
- MODIFIED `nastech_cli/models.py`
- MODIFIED `nastech_cli/models_catalog_static.py`
- MODIFIED `nastech_cli/source_build.py`
- ADDED `nastech_cli/web_build_limits.py`
- MODIFIED `nastech_state_compression.py`
- MODIFIED `nastech_state_search.py`
- MODIFIED `locales/_keys.desktop.json`
- MODIFIED `plugin-catalog/claude-subscription-directsdk.yaml`
- MODIFIED `plugin-catalog/nastech-monitoring-dashboard.yaml`
- MODIFIED `plugins/kanban/dashboard/plugin_api.py`
- MODIFIED `scripts/build/web.mjs`
- MODIFIED `scripts/ci/classify_changes.py`
- MODIFIED `tests/agent/test_turn_facade_lease.py`
- MODIFIED `tests/agent/test_usage_pricing.py`
- MODIFIED `tests/agent/transports/test_chat_completions.py`
- ADDED `tests/agent/transports/test_profile_hook_keyword_compat.py`
- MODIFIED `tests/fixtures/resolution_allowlist.json`
- MODIFIED `tests/gateway/test_windows_venv_import_guard.py`
- MODIFIED `tests/nastech_cli/test_api_key_providers.py`
- ADDED `tests/nastech_cli/test_bare_custom_picker_row.py`
- MODIFIED `tests/nastech_cli/test_dashboard_auth_middleware.py`
- MODIFIED `tests/nastech_cli/test_external_process_auth_status.py`
- MODIFIED `tests/nastech_cli/test_kanban_boards.py`
- MODIFIED `tests/nastech_cli/test_kanban_core_functionality.py`
- MODIFIED `tests/nastech_cli/test_models_relay_base_url.py`
- ADDED `tests/nastech_cli/test_web_build_limits.py`
- ADDED `tests/nastech_state/test_fts_rebuild_corruption_class.py`
- MODIFIED `tests/plugins/test_kanban_board_lifecycle_api.py`
- MODIFIED `tests/plugins/test_kanban_dashboard_plugin.py`
- ADDED `tests/tools/test_browser_windows_headless.py`
- MODIFIED `tools/browser_tool_lightpanda_fallback.py`
- MODIFIED `tools/browser_tool_session.py`
- ADDED `web/src/components/AuthWidget.test.tsx`
- MODIFIED `web/src/components/AuthWidget.tsx`
- ADDED `web/src/components/auth-widget-visibility.ts`
- MODIFIED `web/src/lib/api.test.ts`
- MODIFIED `web/src/lib/api.ts`
- MODIFIED `web/src/pages/SessionsPage.tsx`
- MODIFIED `website/docs/user-guide/features/web-dashboard.md`
- MODIFIED `website/static/api/model-catalog.json`

## Scan

17908 files scanned [audio=5, binary=8, doc=4, font=13, image=174, text=17704]


## Diff

2883 renamed, 0 rewritten, 14405 identical, 141 locked, 0 missing, 32 owned, 387 reconciled


## Fork check (vs nastech-agent)

- 17772 identical, 116 updated (+0/-0 lines), 20 added, 0 missing, 0 fork-local-unpreserved, 0 stale-upstream, 0 locked/binary, 0 collision-safe relocated, 60 preserved fork-local files, 0 violations

- features: fork 56 -> branded 56

Auto-generated by 100Ways.
