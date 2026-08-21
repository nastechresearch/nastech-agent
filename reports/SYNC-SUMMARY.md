# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 55 commits affecting 1291 files.
- **Source revision:** `fcbd1076a938`.
- **Previous source revision:** `40643cbaf9b7`.

## Technical coverage

- **.env.example/:** 2 changed files.
- **agent/:** 20 changed files.
- **apps/:** 58 changed files.
- **contributors/:** 3 changed files.
- **cron/:** 2 changed files.
- **nastech_cli/:** 34 changed files.
- **plugins/:** 9 changed files.
- **pyproject.toml/:** 1 changed files.
- **run_agent.py/:** 2 changed files.
- **scripts/:** 1 changed files.
- **tests/:** 62 changed files.
- **tui_gateway/:** 3 changed files.
- **uv.lock/:** 1 changed files.
- **website/:** 11 changed files.

## Delivered improvements

### New capabilities

- feat: keyless providers count as authenticated everywhere — opencode-free appears in /model and desktop pickers with zero setup
- feat(update): nastech update --plan — read-only fleet inventory + plan phase in every update
- feat(cron): cron agents now run with memory enabled like every other agent
- feat: keyless flag on the provider catalog — GUI contract tests exempt anonymous providers
- feat: opencode-free is fully keyless — no env var, no account, anonymous wire
- feat(providers): add OpenCode Free provider with keyed auth and opencode User-Agent
- feat: stealth/ox-alpha free model in the OpenRouter catalog

### Reliability and fixes

- fix(native_compaction): preserve compression summary messages during pre-checkpoint pruning
- fix: catalog drift sync — dead free slugs out, live OpenRouter free models in, ox-alpha-free on Go
- fix(bot-mode): durableGroupChatRooms drops tombstones and roomId on the remote-merge persist path
- fix(desktop): order-independent selection guard, layer-hint scoping, honest compositor receipt
- fix: lazy session-states import is best-effort under partial module mocks
- fix: break session-states import cycle via lazy import in reconnectSecondary
- fix(desktop): stale running arcs clear on gateway reconnect (#53902, #73082)
- fix: delist UA-gated free models from opencode-free — big-pickle and mimo-v2.5-free 429 every non-opencode client
- fix(update): restart all macOS launchd gateways on nastech update
- fix(update): every begun update receipt is now persisted — command-boundary finalization
- fix: foreground priority for background review cancel timeout
- fix(agent): synchronize background review cancellation
- 14 additional reliability and fixes updates are included in this verified snapshot.

### Performance

- perf(desktop): harden the spinner strip and tighten status invalidation
- perf(desktop): composite-clean spinner strip, selection guard, swap-overlay ticker
- perf(desktop): compositor-only glyph spinner (no per-tick DOM mutation)
- perf(desktop): move settled-preview derivation off the message root
- perf(desktop): finish scoping streaming-status invalidation (data-streaming leaf, root isRunning)
- perf(desktop): scope streaming-status invalidation below message root
- perf(desktop): idle renderers stop burning CPU on infinite CSS animations (#53902, #73082)

### Documentation

- docs: opencode-free in provider choice lists (cli-commands, aux providers, fallback table)

### Improvements

- chore: release v0.20.5 (2026.8.19)
- test(desktop): exercise the spinner CSS and the invalidation scope for real
- Merge pull request #91401 from kshitijk4poor/refactor/dedupe-telegram-mock
- refactor: remove 27 duplicate _ensure_telegram_mock() copies from gateway tests
- chore: map contributor email for paultaki
- test(gateway): re-pin _get_service_pids tests to the label-derived locate + prefix-scan union
- refactor: use request_hard_interrupt for review cancellation
- chore: add qixuancao to AUTHOR_MAP
- refactor(agent): simplify background review run state
- chore: map contributor email for vinsew
- test(prompt_caching): home empty-tools fallback test in TestPromptCachePlan
- refactor(prompt_caching): shallow strip copy, exact-count guards, dedupe idempotency tests
- 2 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
