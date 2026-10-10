# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 207 commits affecting 2905 files.
- **Source revision:** `f925b01791fe`.
- **Previous source revision:** `73162b00eefd`.

## Technical coverage

- **.github/:** 4 changed files.
- **Dockerfile/:** 1 changed files.
- **acp_adapter/:** 3 changed files.
- **agent/:** 161 changed files.
- **apps/:** 77 changed files.
- **cli.py/:** 1 changed files.
- **contributors/:** 16 changed files.
- **cron/:** 13 changed files.
- **evals/:** 5 changed files.
- **gateway/:** 104 changed files.
- **locales/:** 3 changed files.
- **mcp_serve.py/:** 1 changed files.
- **nastech_bootstrap.py/:** 1 changed files.
- **nastech_cli/:** 218 changed files.
- **nastech_constants.py/:** 1 changed files.
- **nastech_logging.py/:** 1 changed files.
- **nastech_platform/:** 3 changed files.
- **nastech_startup_watchdog.py/:** 2 changed files.
- **nastech_state.py/:** 2 changed files.
- **nastech_state_common.py/:** 1 changed files.
- **nastech_state_dbfile.py/:** 1 changed files.
- **nastech_state_errors.py/:** 1 changed files.
- **nastech_state_guard.py/:** 1 changed files.
- **nastech_state_maintenance.py/:** 2 changed files.
- **nastech_state_portability.py/:** 1 changed files.
- **nastech_state_readpool.py/:** 2 changed files.
- **nastech_state_registry.py/:** 1 changed files.
- **nastech_state_repair.py/:** 1 changed files.
- **nastech_state_schema.py/:** 1 changed files.
- **nastech_state_search.py/:** 1 changed files.
- **nastech_state_sessions.py/:** 1 changed files.
- **optional-skills/:** 15 changed files.
- **package.json/:** 1 changed files.
- **plugin-catalog/:** 81 changed files.
- **plugins/:** 81 changed files.
- **pm/:** 16 changed files.
- **providers/:** 1 changed files.
- **pyproject.toml/:** 1 changed files.
- **registration_lifecycle.py/:** 1 changed files.
- **ruff.strict.toml/:** 5 changed files.
- **run_agent.py/:** 2 changed files.
- **scripts/:** 26 changed files.
- **skills/:** 9 changed files.
- **tests/:** 372 changed files.
- **tools/:** 120 changed files.
- **trajectory_compressor.py/:** 3 changed files.
- **tui_gateway/:** 22 changed files.
- **utils.py/:** 2 changed files.
- **uv.lock/:** 2 changed files.
- **website/:** 49 changed files.

## Delivered improvements

### New capabilities

- feat(relay): emit compaction marks from the compression attempt record
- feat(plugin-catalog): add jp-edinet
- feat(plugin-catalog): add nastech-adaptive-effort plugin
- feat(plugin-catalog): add beam plugin
- feat(plugin-catalog): repin radio-dm-gateway to f3f8049 after the repository rename
- feat(plugin-catalog): remove old meshtastic-gateway file name
- feat(plugin-catalog): rename meshtastic-gateway to radio-dm-gateway
- feat(plugin-catalog): add meshtastic-gateway
- feat(plugin-catalog): bump command-ledger to 1.1.0
- feat(plugin-catalog): bump approval-ledger to 1.1.0
- feat(plugin-catalog): memory-shield 1.1.2 (review fixes)
- feat(plugin-catalog): memory-shield 1.1.1 (bounded hook scan)
- 12 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(relay): stop waiting on Relay after one stalled compaction mark
- fix(relay): bound compaction marks and skip unused prune estimates
- fix(relay): mark a micro-compaction in a rotated child on the turn it ran in
- fix(relay): keep the empty_transcript class on its attempt mark
- fix(relay): record why an overflow compaction ran in overflow_reason
- fix(relay): mark a second rotating compaction on the turn it ran in
- fix(relay): align the nastech.compaction v1 contract with what Nastech emits
- fix(relay): emit no compaction mark from an uninstrumented turn or a detached fork
- fix(compression): report committed effects without leaking metric state
- fix(compression): log one attempt record when an engine returns an empty transcript
- fix(compression): keep a late-unwinding attempt's own id, session and trigger
- fix(compression): log one attempt record when the Codex route raises
- 58 additional reliability and fixes updates are included in this verified snapshot.

### Documentation

- docs(relay): document the summarizer fields as free-form identifiers
- docs(relay): list the gateway reset after compression exhaustion as unmarked
- docs(update): CLI reference names stable as the default and --set-channel main as the way back
- docs(skills): note inline-shell scoping for nested, external_dirs and unreadable-lock cases
- docs(telemetry): v4 takes additive values in place after its stable release
- docs(image_gen): state the fallback rule as no server accepted the request
- docs(tool-gateway): attribute the 429 retries to the gateway
- docs(loops): soften backend-lifetime wording

### Improvements

- test(relay): make stalled mark assertion scheduler independent
- test(relay): publish one attempt mark when the Codex route raises
- test(relay): call a failed summary attempt failed, not aborted
- test(compression): cover the attempt record of a rotating session-backed commit
- test(compression): prove each automatic call site passes its trigger label
- refactor(compression): move attempt telemetry helpers and the Codex route into siblings
- chore(plugin-catalog): claude-code-theme requires Nastech 0.21.6 (registerSettingsPage)
- plugin-catalog: add claude-code-theme
- chore: map obierlaire contributor email
- chore(plugin-catalog): lowrouter disclosure uses the catalog's 'Disclosure —' form
- plugin-catalog: add lowrouter
- chore(plugin-catalog): crew 0.8.1, re-pin to e698850
- 93 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
