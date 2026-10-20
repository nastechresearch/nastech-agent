# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 1075 commits affecting 3305 files.
- **Source revision:** `edeefe514f49`.
- **Previous source revision:** `b3c28838095b`.

## Technical coverage

- **.github/:** 2 changed files.
- **README.md/:** 1 changed files.
- **acp_adapter/:** 29 changed files.
- **agent/:** 81 changed files.
- **apps/:** 850 changed files.
- **cli.py/:** 3 changed files.
- **contributors/:** 23 changed files.
- **cron/:** 1 changed files.
- **evals/:** 1 changed files.
- **gateway/:** 453 changed files.
- **locales/:** 344 changed files.
- **model_tools.py/:** 2 changed files.
- **nastech_cli/:** 496 changed files.
- **nastech_constants.py/:** 1 changed files.
- **nastech_constants_scratch.py/:** 3 changed files.
- **nastech_constants_scratch_stuck.py/:** 2 changed files.
- **nastech_logging.py/:** 3 changed files.
- **nastech_state.py/:** 1 changed files.
- **nastech_state_api_content.py/:** 1 changed files.
- **nastech_state_common.py/:** 7 changed files.
- **nastech_state_compression.py/:** 11 changed files.
- **nastech_state_errors.py/:** 1 changed files.
- **nastech_state_local.py/:** 2 changed files.
- **nastech_state_maintenance.py/:** 4 changed files.
- **nastech_state_messages.py/:** 8 changed files.
- **nastech_state_mutation_branch.py/:** 1 changed files.
- **nastech_state_mutation_chat_pick.py/:** 1 changed files.
- **nastech_state_mutation_guards.py/:** 1 changed files.
- **nastech_state_mutation_prepared.py/:** 3 changed files.
- **nastech_state_mutations.py/:** 8 changed files.
- **nastech_state_portability.py/:** 1 changed files.
- **nastech_state_profile_repair.py/:** 2 changed files.
- **nastech_state_prune_rewrite.py/:** 1 changed files.
- **nastech_state_runtime.py/:** 12 changed files.
- **nastech_state_runtime_workers.py/:** 2 changed files.
- **nastech_state_schema.py/:** 1 changed files.
- **nastech_state_sessions.py/:** 13 changed files.
- **nastech_state_todo.py/:** 1 changed files.
- **nastech_state_usage.py/:** 5 changed files.
- **nastech_state_worker_compression.py/:** 2 changed files.
- **nastech_state_worker_lifecycle.py/:** 2 changed files.
- **plugin-catalog/:** 110 changed files.
- **plugins/:** 37 changed files.
- **pm/:** 1 changed files.
- **pyproject.toml/:** 2 changed files.
- **run_agent.py/:** 12 changed files.
- **scripts/:** 6 changed files.
- **tests/:** 817 changed files.
- **tools/:** 80 changed files.
- **tui_gateway/:** 109 changed files.
- **ui-tui/:** 77 changed files.
- **uv.lock/:** 2 changed files.
- **web/:** 7 changed files.
- **website/:** 127 changed files.

## Delivered improvements

### New capabilities

- feat(plugin-catalog): add nastech-memory-pane plugin
- feat(gateway): ask y/N before a lifecycle verb interrupts live sessions
- feat(mcp): forward MCP notifications/progress as live tool.progress events
- feat(gateway): session.resume carries the session's todo snapshot
- feat(desktop): git-installed plugins get an Update button and a security-scan override dialog
- feat(catalog): featured hero becomes a slider when there are several picks
- feat(desktop): several picked categories show as one shelf each
- feat(desktop): tier filter keeps plugins grouped; every chip on reads as All
- feat(desktop): filter and badge plugins by tier (Official, Verified, Community)
- feat(plugins): portable plugins get the Settings > Plugins form, live
- feat(cli): glyph transcript, status line under the composer, two-line header
- feat(plugins): a re-pin that moves an OAuth entry's authorize host asks first
- 37 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(catalog): update nastech-resetwatch to 0.2.24
- fix(plugin-catalog): update jp-estat to 2cf442a
- fix(plugin-catalog): update jp-kokkai to 7047db9
- fix(website): the featured plugin card shows the summary, not the disclosure
- fix(website): plugin disclosures go at the bottom of the page
- fix(cli): a long one-sentence reasoning is not repeated as a shortened title
- fix(cli): one-sentence reasoning is not repeated as its own summary title
- fix(bedrock): reasoning GPTs replay only the reasoning they stamped on Converse
- fix(bedrock): strip prior reasoning for the gpt-6 family on Converse
- fix(bedrock): never replay another model's sealed reasoning on Converse
- fix(bedrock): recover redacted reasoning in Converse calls
- fix(mcp): rekeyed launch-profile connections keep their owner and tools
- 625 additional reliability and fixes updates are included in this verified snapshot.

### Performance

- perf(agent): a closed agent's message bodies leave the token-estimate memo
- perf(tui_gateway): free a torn-down session's event replay ring
- perf(mem_trim): run gc.collect() on every platform (macOS serve phys_footprint 5m 380.6 -> 368.9 MB)
- perf(state): the ancestor stamp's unset probe reads only the walked rows
- perf(state): the ancestor stamp's fast path follows only compression edges
- perf(state): skip the ancestor stamp walk when no ancestor is unset
- perf(state): stamp compression ancestors at write time, drop list-time walk
- perf(cli): filter the gateway subagent tail once per fetch, not per frame
- perf(cli): release a retired agent off the command path
- perf(state): a display read hashes only rows a removed copy could match
- perf(cli): keep a turn's streamed-delta buffers linear
- perf(gateway): parse a policy's follow flag once, not on every read
- 1 additional performance updates are included in this verified snapshot.

### Documentation

- docs(agent): _trim_process_memory's docstring matches the every-platform gc
- docs(tui_gateway): the teardown finally comment states its one real reason
- docs(mem_trim): module docstring says gc.collect() runs on every platform
- docs(state): an unknown created_source is repaired by the creator upsert
- docs(plugin-catalog): onboarding is curated for official or verified entries
- docs(cli): /queue's shared gateway queue, move refusal, lost-answer note
- docs(tui): say why not_found stays a pre-commit refusal
- docs(plugins): give only the Google client as an example of a plugin OAuth client
- docs(gateway): name the real root-DM transfer hook in run_turn_prepare
- docs(gateway): the parity note for /save names Desktop's client-side write
- docs(gateway): regenerate the command parity table for the Desktop actions
- docs(slash): document /discard and regenerate the Desktop slash registry
- 4 additional documentation updates are included in this verified snapshot.

### Improvements

- plugin-catalog: update nastech-seo to 0.1.1
- chore(catalog): review disclosure for jp-estat
- plugin-catalog: bump loreconvo to 0.10.18
- plugin-catalog: cua-spaces banner
- test(desktop): boot-lifecycle teardown interrupts the live turn it leaves running
- Merge pull request #139467 from IAvecilla/perf/ruamel-yaml-c-parser-py314
- test(e2e): the tmux resize scrollback test follows the glyph CLI layout
- Merge pull request #138820 from Nastechresearch/austin/feat/capabilities-catalog
- test(auth): the Codex opt-out self-heal test never calls the real token endpoint
- plugin-catalog: add cua-spaces (Cua's terminal backend), verified tier
- test(bedrock): pin exact same-model GPT reasoning replay across user turns
- chore(bedrock): fold the two Converse resend arms under the facade's line cap
- 348 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
