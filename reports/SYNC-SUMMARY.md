# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 63 commits affecting 2249 files.
- **Source revision:** `03fee43ca344`.
- **Previous source revision:** `a51143fbbe6d`.

## Technical coverage

- **acp_adapter/:** 1 changed files.
- **agent/:** 17 changed files.
- **apps/:** 29 changed files.
- **cli.py/:** 1 changed files.
- **contributors/:** 7 changed files.
- **cron/:** 2 changed files.
- **gateway/:** 2 changed files.
- **nastech_cli/:** 13 changed files.
- **plugin-catalog/:** 24 changed files.
- **plugins/:** 8 changed files.
- **scripts/:** 1 changed files.
- **tests/:** 30 changed files.
- **tools/:** 3 changed files.
- **tui_gateway/:** 1 changed files.
- **website/:** 14 changed files.

## Delivered improvements

### New capabilities

- feat(auth): opt out of borrowing Codex CLI / Claude Code logins (auth.adopt_external_logins)
- feat(plugins): pin nastech-talk catalog entry to v0.19.2
- feat(plugin-catalog): add Nastech Talk
- feat(plugin-catalog): add Prism provider
- feat(catalog): add Search1API plugin
- feat(catalog): add pinned artifact-relay plugin
- feat(plugin-catalog): add nastech-security-audit
- feat(catalog): add OpenAlex research tools

### Reliability and fixes

- fix(agent): refuse stale singleton adoption over rotated manual:device_code entries (#106705)
- fix(auth): isolate Codex singleton sync by principal
- fix(agent): terminal copy for the new role_alternation failure reason
- fix: MoA aggregator merges adjacent same-role messages only for destinations that reject them
- fix(desktop): restore the unsent composer draft when a session is gone
- fix(desktop): /reasoning hide|show gates Thinking blocks immediately
- fix(desktop): count the head entries the group-chat mirror drops
- fix(desktop): mark truncated group-chat sync payloads
- fix(desktop): mark the truncated head of a bot group-chat turn delta
- fix: /stop halts background subagents and returns their partial results as interrupted completions
- fix(kanban): dispatcher blocks a card on the first terminal provider error
- fix(kanban): worker exits EX_CONFIG on a terminal provider error
- 18 additional reliability and fixes updates are included in this verified snapshot.

### Documentation

- docs: relative link to the borrowed-logins section (route-style links fail the docs check)

### Improvements

- chore: map contributor email for @Caelier (#100423 salvage)
- test: two invariant tests for Codex singleton adoption, replacing the salvaged suites
- test(desktop): pin the omitted-head marker on the real group turn path
- plugin-catalog: nastech-talk disclosure line for the Codex realtime lane + contributor map
- plugin-catalog: bump nastech-talk pin to v0.21.0, add voice category
- catalog: pin nastech-talk to v0.19.1 (read-only Codex lane)
- chore: map contributor email for @TheStreamCode
- catalog: bump nastech-muse-code to e335011 (review fixes)
- catalog: bump nastech-muse-code to 22298cb (poll-tolerant device login)
- catalog: bump nastech-muse-code to v0.2.0 (own device login, no omp)
- catalog: add nastech-muse-code (Muse Spark via Muse Code subscription)
- chore: map contributor email for @Shotflame
- 12 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
