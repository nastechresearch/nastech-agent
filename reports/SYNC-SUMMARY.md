# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 9138 commits affecting 2205 files.
- **Source revision:** `debfc7420b61`.
- **Previous source revision:** `3ea71a47b3f8`.

## Technical coverage

- **.dockerignore/:** 1 changed files.
- **.env.example/:** 2 changed files.
- **.github/:** 132 changed files.
- **.gitignore/:** 18 changed files.
- **AGENTS.md/:** 7 changed files.
- **COMPAT_MANIFEST.md/:** 6 changed files.
- **CONTRIBUTING.es.md/:** 1 changed files.
- **CONTRIBUTING.md/:** 7 changed files.
- **Dockerfile/:** 1 changed files.
- **MagicMock/:** 168 changed files.
- **acp_adapter/:** 116 changed files.
- **agent/:** 2956 changed files.
- **apps/:** 4343 changed files.
- **batch_runner.py/:** 8 changed files.
- **cli-config.yaml.example/:** 19 changed files.
- **cli.py/:** 100 changed files.
- **compat_manifest.json/:** 4 changed files.
- **contributors/:** 271 changed files.
- **cron/:** 317 changed files.
- **datagen-config-examples/:** 5 changed files.
- **docker/:** 3 changed files.
- **docs/:** 17 changed files.
- **evals/:** 233 changed files.
- **gateway/:** 2228 changed files.
- **locales/:** 68 changed files.
- **mcp-research-data/:** 5 changed files.
- **mcp_serve.py/:** 7 changed files.
- **mini_swe_runner.py/:** 3 changed files.
- **model_tools.py/:** 27 changed files.
- **model_tools_connectors.py/:** 1 changed files.
- **nastech_bootstrap.py/:** 1 changed files.
- **nastech_cli/:** 4982 changed files.
- **nastech_constants.py/:** 29 changed files.
- **nastech_logging.py/:** 14 changed files.
- **nastech_startup_watchdog.py/:** 5 changed files.
- **nastech_state.py/:** 73 changed files.
- **nastech_state_common.py/:** 38 changed files.
- **nastech_state_compression.py/:** 24 changed files.
- **nastech_state_dbfile.py/:** 27 changed files.
- **nastech_state_errors.py/:** 5 changed files.
- **nastech_state_fts.py/:** 7 changed files.
- **nastech_state_gateway.py/:** 15 changed files.
- **nastech_state_guard.py/:** 4 changed files.
- **nastech_state_holders.py/:** 4 changed files.
- **nastech_state_ids.py/:** 1 changed files.
- **nastech_state_lockguard.py/:** 4 changed files.
- **nastech_state_maintenance.py/:** 17 changed files.
- **nastech_state_messages.py/:** 42 changed files.
- **nastech_state_portability.py/:** 22 changed files.
- **nastech_state_readpool.py/:** 8 changed files.
- **nastech_state_registry.py/:** 12 changed files.
- **nastech_state_repair.py/:** 17 changed files.
- **nastech_state_rewind.py/:** 3 changed files.
- **nastech_state_schema.py/:** 34 changed files.
- **nastech_state_search.py/:** 35 changed files.
- **nastech_state_sessions.py/:** 29 changed files.
- **nastech_state_telegram.py/:** 9 changed files.
- **nastech_state_timeline.py/:** 1 changed files.
- **nastech_state_titles.py/:** 13 changed files.
- **nastech_state_usage.py/:** 16 changed files.
- **nastech_state_user_copy.py/:** 3 changed files.
- **nastech_state_wal.py/:** 15 changed files.
- **nastech_time.py/:** 4 changed files.
- **nastech_wisdom/:** 108 changed files.
- **nix/:** 4 changed files.
- **optional-mcps/:** 18 changed files.
- **optional-skills/:** 137 changed files.
- **package-lock.json/:** 11 changed files.
- **plugin-catalog/:** 169 changed files.
- **plugins/:** 1750 changed files.
- **prompts/:** 6 changed files.
- **providers/:** 9 changed files.
- **pyproject.toml/:** 15 changed files.
- **r318C_fuzz_new.json/:** 2 changed files.
- **registration_lifecycle.py/:** 2 changed files.
- **run_agent.py/:** 57 changed files.
- **scripts/:** 140 changed files.
- **setup-nastech.sh/:** 1 changed files.
- **setup.py/:** 2 changed files.
- **skills/:** 29 changed files.
- **tests/:** 7412 changed files.
- **tests-js/:** 17 changed files.
- **tools/:** 3335 changed files.
- **toolset_distributions.py/:** 6 changed files.
- **toolsets.py/:** 25 changed files.
- **trajectory_compressor.py/:** 3 changed files.
- **tui_gateway/:** 1021 changed files.
- **ui-tui/:** 241 changed files.
- **utils.py/:** 13 changed files.
- **uv.lock/:** 9 changed files.
- **web/:** 213 changed files.
- **website/:** 1173 changed files.

## Delivered improvements

### New capabilities

- feat(providers): remove the keyless opencode-free tier
- feat(memory): a configured provider that left core is installed from the catalog automatically
- feat(notifications): opt-in suppression of user-channel warning notifications
- feat(plugins validate): --install-deps installs the declaration before the capability probe
- feat(desktop): per-project toggle for gitignored files in the file tree (#101065)
- feat(vision): vision.embed_target_bytes replaces the hardcoded 256 KB native embed budget
- feat(desktop): add rebindable sidebar grouping cycle
- feat(plugins validate): fail trees with nothing to load; check dependency declarations
- feat(plugins): install declared Python dependencies and re-apply them after nastech update
- feat(lazy_deps): install_specs takes constraints and dry_run
- feat(desktop): auto-grow the Bot group composer for long prompts
- feat(bot-mode): render room @mentions as inline references and add Reply to @bot
- 266 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(models): restore _OPENCODE_FREE_EXCLUDED_MODELS used by the Zen/Go live pickers
- fix(gateway): a /stop in a thread stops every run of that thread
- fix(desktop): compare the moved agent's legacy URL with the shared gateway normaliser
- fix(desktop): let the Reconnect action redial a rejected active gateway
- fix(cron): move FIRE_CLAIM_TTL_SECONDS to the same leaf as the skew bound
- fix(cron): isolate fire claim skew constant
- fix(desktop): retain auth rejection across socket cleanup
- fix(desktop): stop reconnecting rejected gateway sessions
- fix(desktop): recover Cloud connections after team changes
- fix(desktop): support Privy and NAS portal sessions in Cloud sign-in
- fix(gateway): match the chat id as text so ids containing ':' survive
- fix(gateway): chat-scope match must not alias a chat_id or a reply thread
- 2868 additional reliability and fixes updates are included in this verified snapshot.

### Security and hardening

- security(state): harden async_delegation's direct state.db writer
- security: make state databases and snapshots owner-only
- security(gateway): re-resolve hooks directory per call to fix profile isolation

### Performance

- perf(desktop): reasoning-block seam check reads two chars, not two string copies
- perf(agent): size outbound image payloads by data length, not by re-serializing them
- perf(aux): bound the anonymous Nastech cooldown marker instead of skipping it
- perf(desktop): reduce Windows startup I/O and blocking checks
- perf(desktop): virtualize the timeline and bound history jumps
- perf(sessions): index prompts without hydrating full transcripts
- perf(desktop): observe live workspace frame pacing without synthetic sessions
- perf(desktop): defer closed action menus until their content mounts
- perf(desktop): keep relational style invalidation out of unrelated panes
- perf(agent): keep bulk chat-completions payloads out of the SDK request transform
- perf(desktop): resolve the renderer bundle once per window, not twice
- perf(plugins): scan each plugin's source for removed imports once per process, not once per profile
- 18 additional performance updates are included in this verified snapshot.

### Documentation

- docs: the first-run guard no longer counts a keyless provider
- docs: correct the free-tier narrative the removal left behind
- docs: drop opencode-free references (provider removed)
- docs: setup UX a standalone memory provider keeps; catalog migration note for users
- docs(bedrock): specify persisted URL for cache invalidation
- docs(discord): drop a stray conflict marker left by the #114356 salvage resolution
- docs(discord): clarify deployed bot handoff behavior and verify ingress
- docs: note the Windows file-lock retry in the desktop stage-and-swap description
- docs: call out the client.capabilities fail-closed gate as breaking for third-party WS clients
- docs(i18n): zh-Hans mirrors of the vision.embed_target_bytes / max_calls_per_image sections
- docs(vision): document vision.embed_target_bytes and vision.max_calls_per_image
- docs(cron): permanent-error parks block the job; reconnecting notice is once per outage
- 223 additional documentation updates are included in this verified snapshot.

### Improvements

- refactor(providers): finish the keyless cleanup
- test(providers): guard the removed-provider migration hint
- refactor(providers): drop the now-dead keyless provider plumbing
- chore(contributors): map DECRUX9812 for credit on the opencode-free removal salvage
- refactor(desktop): let the foreground rearm own the reauth clear
- test(desktop): keep the secured-prefix and legacy Privy cookie names under contract
- refactor(cron): probe name covers both bounds; delattr fails loudly; one-line facade import
- test(cron): stale-facade probe strips both fire-claim constants and reaches the TTL path
- chore(contributors): map konit.block@protonmail.com to @KoNit-K
- test(desktop): launch the portal-session Electron fixture without the sandbox and surface its stderr
- refactor(desktop): extract portal session window driver
- test(gateway): pin the /stop chat-scope contract and its bounds
- 5700 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
