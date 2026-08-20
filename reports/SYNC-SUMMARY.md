# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 65 commits affecting 1279 files.
- **Source revision:** `044acf2bf700`.
- **Previous source revision:** `6f31cfad7825`.

## Technical coverage

- **CONTRIBUTING.es.md/:** 1 changed files.
- **CONTRIBUTING.md/:** 1 changed files.
- **SECURITY.es.md/:** 1 changed files.
- **SECURITY.md/:** 1 changed files.
- **agent/:** 4 changed files.
- **apps/:** 56 changed files.
- **cli.py/:** 5 changed files.
- **contributors/:** 1 changed files.
- **cron/:** 13 changed files.
- **docs/:** 1 changed files.
- **gateway/:** 13 changed files.
- **nastech_cli/:** 25 changed files.
- **nix/:** 1 changed files.
- **run_agent.py/:** 2 changed files.
- **scripts/:** 2 changed files.
- **tests/:** 41 changed files.
- **tools/:** 7 changed files.
- **toolsets.py/:** 1 changed files.
- **tui_gateway/:** 4 changed files.
- **website/:** 21 changed files.

## Delivered improvements

### New capabilities

- feat: desktop updates no longer re-apply local source edits (--keep-stash)
- feat(config): default agent.max_turns to unlimited; accept inf/infinity/null spellings
- feat(config): resolve_turn_limit — first-class 'none'/'unlimited' for agent.max_turns
- feat(process): positive process identity — spawn tags, machine spawn ledger, Windows job-object self-attach
- feat(cli): declutter /help + Ctrl+P command palette (C-04/C-05)
- feat(cli): /status shows reasoning, approval mode, and context usage (C-02)
- feat(cli): rotating task-oriented composer placeholder (C-09)
- feat(cli): type-to-fuzzy-filter the /model picker model list
- feat(desktop): durable element handles, and a delta instead of the whole page
- feat(desktop): an overlay that shows what the agent is doing to the page
- feat(desktop): drive the preview with real input, not synthetic events
- feat(tools): drive_preview and annotate_preview — the agent can use the page it opened
- 4 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(update): gateway auto-restart no longer dies on stale cached modules after the pull
- fix(resolve_turn_limit): gateway bridge null handling, TUI resolver, docs
- fix: keyless rescue no longer re-fetches policy-blocked URLs
- fix(bot-mode): group-chat command approvals surface in the room too — same hidden-session class
- fix(bot-mode): group-chat members' clarify questions surface in the room and are answerable (#90694)
- fix(update): fail closed when the hand-off shim check cannot run
- fix(update): reap leaked serve backends during a GUI hand-off instead of dead-ending the venv sync (Windows)
- fix(desktop): corrupt backend-ownership.json no longer erases records of live backends (#89298)
- fix(bot-mode): disband dialog no longer points at the removed session browser
- fix(bot-mode): canonical-chat adoption survives busy profiles via exact-title lookup
- fix(update): hand off only the dependency sync, not the whole update (#90240)
- fix(cron): stamp persisted origin scope_id onto origin-matching delivery metadata
- 13 additional reliability and fixes updates are included in this verified snapshot.

### Documentation

- docs(bot-mode): drop the removed per-bot Sessions browser from the Bots-pane list
- docs(cron): document the in_channel carve-out on the mirror opt-in
- docs(relay): document the two new descriptor capability bits in the contract §2 table

### Improvements

- chore(tests): remove two flaky test files that tax CI
- test: shim-progress fake nastech answers the --keep-stash --help probe
- test(desktop): parent watchdog env now carries NASTECH_SPAWN — update exact-shape assertions
- Merge pull request #90038 from victor-kyriazakos/feat/relay-slack-parity
- test: pre-command hook stubs accept show_help(arg) after /help filter change
- chore: nudge PR head sync (empty)
- Merge branch 'main' into feat/relay-slack-parity
- test(cron): native scalar-fallback test asserts the live delivery actually ran
- test(cron): pin the auto-mocked D6 accessor; prove the native scalar fallback with a real adapter shape
- Merge pull request #90197 from Nastechresearch/bb/preview-act
- refactor(desktop): give the act engine's pure logic real modules
- test(relay): rename misnamed precedence test; document the flat-key fallback nuance
- 9 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
