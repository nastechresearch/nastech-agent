# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 337 commits affecting 2898 files.
- **Source revision:** `73162b00eefd`.
- **Previous source revision:** `0240fa4a8412`.

## Technical coverage

- **.github/:** 10 changed files.
- **acp_adapter/:** 8 changed files.
- **agent/:** 273 changed files.
- **apps/:** 51 changed files.
- **batch_runner.py/:** 2 changed files.
- **cli-config.yaml.example/:** 1 changed files.
- **cli.py/:** 4 changed files.
- **contributors/:** 19 changed files.
- **cron/:** 26 changed files.
- **evals/:** 42 changed files.
- **gateway/:** 116 changed files.
- **lefthook.yml/:** 1 changed files.
- **mcp_serve.py/:** 1 changed files.
- **mini_swe_runner.py/:** 2 changed files.
- **model_tools.py/:** 1 changed files.
- **nastech_cli/:** 346 changed files.
- **nastech_logging.py/:** 1 changed files.
- **nastech_platform/:** 2 changed files.
- **nastech_startup_watchdog.py/:** 1 changed files.
- **nastech_state.py/:** 2 changed files.
- **nastech_state_compression.py/:** 2 changed files.
- **nastech_state_coverage.py/:** 2 changed files.
- **nastech_state_dbfile.py/:** 1 changed files.
- **nastech_state_gateway.py/:** 2 changed files.
- **nastech_state_health.py/:** 1 changed files.
- **nastech_state_holders.py/:** 1 changed files.
- **nastech_state_identity.py/:** 1 changed files.
- **nastech_state_lockguard.py/:** 1 changed files.
- **nastech_state_lockowners.py/:** 1 changed files.
- **nastech_state_maintenance.py/:** 2 changed files.
- **nastech_state_messages.py/:** 2 changed files.
- **nastech_state_portability.py/:** 4 changed files.
- **nastech_state_profile_repair.py/:** 1 changed files.
- **nastech_state_registry.py/:** 1 changed files.
- **nastech_state_repair.py/:** 1 changed files.
- **nastech_state_rewind.py/:** 1 changed files.
- **nastech_state_schema.py/:** 1 changed files.
- **nastech_state_search.py/:** 2 changed files.
- **nastech_state_sessions.py/:** 2 changed files.
- **nastech_state_telegram.py/:** 1 changed files.
- **nastech_state_titles.py/:** 1 changed files.
- **nastech_state_tool_retries.py/:** 1 changed files.
- **nastech_state_usage.py/:** 2 changed files.
- **nastech_state_wal.py/:** 1 changed files.
- **nastech_time.py/:** 1 changed files.
- **optional-skills/:** 52 changed files.
- **package-lock.json/:** 1 changed files.
- **package.json/:** 2 changed files.
- **plugin-catalog/:** 236 changed files.
- **plugins/:** 131 changed files.
- **pm/:** 8 changed files.
- **ruff.strict.toml/:** 11 changed files.
- **run_agent.py/:** 3 changed files.
- **scripts/:** 58 changed files.
- **skills/:** 18 changed files.
- **tests/:** 1688 changed files.
- **tests-js/:** 5 changed files.
- **tools/:** 272 changed files.
- **toolset_distributions.py/:** 1 changed files.
- **toolsets.py/:** 3 changed files.
- **trajectory_compressor.py/:** 2 changed files.
- **tui_gateway/:** 31 changed files.
- **ui-tui/:** 3 changed files.
- **website/:** 43 changed files.

## Delivered improvements

### New capabilities

- feat(desktop): plugin SDK pet bubble (ctx.pet.say)
- feat(plugin-catalog): bump nastech-pickup to 0.2.0
- feat(plugin-catalog): add redline plugin
- feat(catalog): refresh OpenViking pin and honor display titles
- feat(catalog): list nastech-openwhispr (community, voice)
- feat(plugin-catalog): add print-job-watch
- feat(catalog): bump nastech-pokemon to v0.7.0
- feat(plugin-catalog): bump error-ledger to 1.2.0
- feat(plugin-catalog): nastech-dreaming 2.2.0 (final)
- feat(plugin-catalog): nastech-dreaming 2.2.0 — trust_feedback
- feat(plugin-catalog): nastech-dreaming 2.2.0 (final sha)
- feat(plugin-catalog): nastech-dreaming 2.2.0
- 26 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(update): a Desktop-only Node dependency failure no longer blocks the TUI and web UI
- fix(memory): keep a runaway-recall ceiling when prefetch spilling is off
- fix(memory): make external prefetch spilling opt-in
- fix(gateway): ignore other Unix users' gateway processes in the process scan
- fix(plugins): a linked plugins/<name> slot reads "already installed", not a bad manifest
- fix(memory): a failed agent-start provider install is not retried by every process start
- fix(tts): a failed synthesis no longer deletes an existing file
- fix(memory): detect providers past the first 8 KB of __init__.py
- fix(browser): end timeout=None captured waits when the supervisor loop closes
- fix(browser): fence captured CDP dispatch and retain late replies
- fix(mcp): a failed OAuth catalog install from a card or the agent says why, instead of `exception`
- fix(plugin-catalog): bump web-search-plus to 4.3.5
- 42 additional reliability and fixes updates are included in this verified snapshot.

### Performance

- perf(update): the product tail trusts the npm closure the PM step just verified
- perf(install): a pinned install checks out only the pin, not the branch tip first
- perf(desktop): skip restaging native inputs whose receipt still matches
- perf(desktop): cache the React Compiler pass by content, so an update recompiles only the files it changed
- perf(desktop): reuse the compiled renderer when only the install stamp changed
- perf(install): a pinned install.ps1 clone checks out only the pin, before it publishes

### Documentation

- docs(catalog): clarify OpenViking managed cloud setup
- docs(catalog): simplify OpenViking description and refresh guide
- docs(gateway): a service definition belongs to the home it pins
- docs(plugin-catalog): update Ace Data Cloud installation guide
- docs(catalog): pin kanban-gantt 1.4.2 and add its catalogue card
- docs(plugin-catalog): bump SHA to b77f5df (canonical externalSideEffects)
- docs(plugin-catalog): bump SHA to b9a8067 with full supersession history
- docs(plugin-catalog): note the pending doctor namespace fix

### Improvements

- test(gateway): process scan skips other uids' gateways unless root
- refactor(desktop): move plugin-contract type re-exports out of the SDK barrel
- catalog: add dashboard-auth-feishu
- chore(catalog): merge-side review chores for enchanted-composer (sweep 1009)
- catalog: re-pin Enchanted Composer after review
- catalog: add Enchanted Composer
- chore: map contributor email for silentpr0
- chore(catalog): merge-side review chores for redline (sweep 1009)
- plugin-catalog: redline re-pin to 6fbb0f9 (review fixes)
- chore: map contributor email for hellohanchen
- chore(catalog): merge-side review chores for huddo (sweep 1009)
- plugin-catalog: huddo 0.7.1 (re-pin to a86d3aa)
- 219 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
