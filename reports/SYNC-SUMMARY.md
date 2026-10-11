# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 332 commits affecting 2904 files.
- **Source revision:** `cca83848ec79`.
- **Previous source revision:** `73162b00eefd`.

## Technical coverage

- **.github/:** 7 changed files.
- **CONTRIBUTING.es.md/:** 3 changed files.
- **CONTRIBUTING.md/:** 3 changed files.
- **Dockerfile/:** 1 changed files.
- **acp_adapter/:** 3 changed files.
- **agent/:** 235 changed files.
- **apps/:** 129 changed files.
- **batch_runner.py/:** 1 changed files.
- **cli.py/:** 2 changed files.
- **contributors/:** 22 changed files.
- **cron/:** 14 changed files.
- **evals/:** 47 changed files.
- **gateway/:** 118 changed files.
- **justfile/:** 1 changed files.
- **lefthook.yml/:** 4 changed files.
- **locales/:** 4 changed files.
- **mcp_serve.py/:** 1 changed files.
- **nastech_bootstrap.py/:** 1 changed files.
- **nastech_cli/:** 316 changed files.
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
- **plugins/:** 124 changed files.
- **pm/:** 24 changed files.
- **providers/:** 1 changed files.
- **pyproject.toml/:** 1 changed files.
- **registration_lifecycle.py/:** 1 changed files.
- **ruff.pre-commit.toml/:** 2 changed files.
- **ruff.strict.toml/:** 9 changed files.
- **ruff.toml/:** 4 changed files.
- **run_agent.py/:** 2 changed files.
- **scripts/:** 56 changed files.
- **skills/:** 22 changed files.
- **tests/:** 983 changed files.
- **tools/:** 146 changed files.
- **trajectory_compressor.py/:** 4 changed files.
- **tui_gateway/:** 24 changed files.
- **utils.py/:** 2 changed files.
- **uv.lock/:** 2 changed files.
- **website/:** 81 changed files.

## Delivered improvements

### New capabilities

- feat(evals): reasoning-replay consumption harness
- feat(desktop): plugins run built-in app actions (ctx.runAction)
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
- 21 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(update): the main channel follows the git branch without reading an R2 record
- fix(evals): reasoning-replay treats Anthropic refusals like xAI 403s
- fix(evals): reasoning-replay harness measures opaque carriers reliably
- fix: Alibaba's content guardrail ends the turn instead of a 4-minute retry loop
- fix: /steer, /branch and compaction accounting keep reasoning intact
- fix: encrypted reasoning items are never deleted from retained history
- fix: Bedrock Converse reasoning survives a reload from state.db
- fix: Gemini/Copilot signatures survive reloads; an error body can't switch off DeepSeek replay
- fix: compaction salvage no longer strips reasoning from retained turns
- fix: OpenAI and xAI models keep reasoning across turns and through compaction
- fix: Gemini and Copilot keep their reasoning carriers across turns
- fix(anthropic): Haiku 5.5 thinks adaptively
- 94 additional reliability and fixes updates are included in this verified snapshot.

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

- chore(memory): holographic leaves core for its community catalog plugin (re-land #136424)
- chore(health): waive pre-existing broad excepts in the restored holographic provider
- Revert "chore(memory): holographic leaves core for its community catalog plugin"
- refactor(evals): split reasoning-replay summarize into per-cell helpers
- chore(memory): holographic leaves core for its community catalog plugin
- test: LSP hard-kill test no longer races its own cleanup
- refactor: move the Codex recovery rungs out of turn_recovery
- refactor: move the stream tool-call accumulator out of the chat-completions facade
- Revert "contributors: drop internal comment line"
- contributors: drop internal comment line
- chore: map contributor email for jcperdomoybarra
- chore(catalog): merge-side review chores for browser-toggle (sweep 1011)
- 169 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
