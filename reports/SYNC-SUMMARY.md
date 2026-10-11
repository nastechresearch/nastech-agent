# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 305 commits affecting 2904 files.
- **Source revision:** `c57331677d7f`.
- **Previous source revision:** `73162b00eefd`.

## Technical coverage

- **.github/:** 7 changed files.
- **Dockerfile/:** 1 changed files.
- **acp_adapter/:** 3 changed files.
- **agent/:** 183 changed files.
- **apps/:** 122 changed files.
- **batch_runner.py/:** 1 changed files.
- **cli.py/:** 2 changed files.
- **contributors/:** 22 changed files.
- **cron/:** 14 changed files.
- **evals/:** 42 changed files.
- **gateway/:** 115 changed files.
- **justfile/:** 1 changed files.
- **lefthook.yml/:** 4 changed files.
- **locales/:** 4 changed files.
- **mcp_serve.py/:** 1 changed files.
- **nastech_bootstrap.py/:** 1 changed files.
- **nastech_cli/:** 301 changed files.
- **nastech_constants.py/:** 2 changed files.
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
- **nastech_yaml.py/:** 1 changed files.
- **optional-skills/:** 22 changed files.
- **package-lock.json/:** 2 changed files.
- **package.json/:** 3 changed files.
- **plugin-catalog/:** 124 changed files.
- **plugins/:** 96 changed files.
- **pm/:** 24 changed files.
- **providers/:** 1 changed files.
- **pyproject.toml/:** 1 changed files.
- **registration_lifecycle.py/:** 1 changed files.
- **ruff.pre-commit.toml/:** 2 changed files.
- **ruff.strict.toml/:** 9 changed files.
- **ruff.toml/:** 4 changed files.
- **run_agent.py/:** 2 changed files.
- **scripts/:** 56 changed files.
- **skills/:** 21 changed files.
- **tests/:** 920 changed files.
- **tools/:** 146 changed files.
- **trajectory_compressor.py/:** 4 changed files.
- **tui_gateway/:** 24 changed files.
- **utils.py/:** 2 changed files.
- **uv.lock/:** 2 changed files.
- **website/:** 64 changed files.

## Delivered improvements

### New capabilities

- feat(plugin-catalog): bump stream-speed to 1.2.0
- feat(plugin-catalog): bump aux-ledger to 1.2.0
- feat(plugin-catalog): add Model Router v0.4.1
- feat(plugin-catalog): add jp-kokkai
- feat(plugin-catalog): add doc-markdown
- feat(desktop): version details name the update channel; the overlay links to change it
- feat(plugins): core-made Codex requests so plugins never hold the token
- feat(relay): emit compaction marks from the compression attempt record
- feat(plugin-catalog): add jp-edinet
- feat(plugin-catalog): add nastech-adaptive-effort plugin
- feat(plugin-catalog): add beam plugin
- feat(plugin-catalog): repin radio-dm-gateway to f3f8049 after the repository rename
- 19 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(plugin-catalog): nastech-lang-vi requires_nastech >=0.21.6, not the unreleased 0.22
- fix(plugin-catalog): bump web-search-plus to 5.0.1
- fix(plugin-catalog): bump nastech-field-notes to 1.2.4
- fix(plugin-catalog): update jp-egov-law to 765ec57
- fix(desktop): Change only where Settings can switch; name the release only on an explicit not-ahead
- fix: add tsx to linted extensions
- fix(checkpoints): avoid history queries in the footprint notice
- fix(install): name the marker owner as the Desktop hand-off pid
- fix(update): stable lookup failures travel as exceptions and name the quota the failed request spent
- fix(update): the stable lookup sends the user's GitHub token and names a rate limit as one
- fix(compression): a refused candidate's attempt record claims no effect
- fix(compression): keep a running attempt's record when an overlapping call stops at a gate
- 77 additional reliability and fixes updates are included in this verified snapshot.

### Documentation

- docs(catalog): pin kanban-gantt 1.5.0
- docs(plugin-catalog): qualify qdrant verbose-log claim (md_search echoes the query)
- docs: official plugin links point at nastech-official-plugins
- docs(plugin-catalog): rule 11 — credentials come through Nastech, never from files
- docs(relay): document the summarizer fields as free-form identifiers
- docs(relay): list the gateway reset after compression exhaustion as unmarked
- docs(update): CLI reference names stable as the default and --set-channel main as the way back
- docs(skills): note inline-shell scoping for nested, external_dirs and unreadable-lock cases
- docs(telemetry): v4 takes additive values in place after its stable release
- docs(image_gen): state the fallback rule as no server accepted the request
- docs(tool-gateway): attribute the 429 retries to the gateway
- docs(loops): soften backend-lifetime wording

### Improvements

- Revert "contributors: drop internal comment line"
- contributors: drop internal comment line
- chore: map contributor email for jcperdomoybarra
- chore(catalog): merge-side review chores for browser-toggle (sweep 1011)
- plugin-catalog: bump browser-toggle pin (README + screenshot)
- plugin-catalog: add browser-toggle
- chore(catalog): merge-side review chores for nastech-taskbar-badge (sweep 1011)
- plugin-catalog: add nastech-taskbar-badge
- chore(catalog): merge-side review chores for nastech-lang-it (sweep 1011)
- Add plugin catalog entry: nastech-lang-it (Italian language pack)
- chore(plugin-catalog): bump Gmail to v1.0.17
- chore(plugin-catalog): update Gmail to v1.0.16
- 161 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
