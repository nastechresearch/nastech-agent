# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 97 commits affecting 2877 files.
- **Source revision:** `7dab93b06e2b`.
- **Previous source revision:** `a3ed4a173070`.

## Technical coverage

- **agent/:** 44 changed files.
- **apps/:** 15 changed files.
- **contributors/:** 1 changed files.
- **cron/:** 12 changed files.
- **gateway/:** 2 changed files.
- **locales/:** 1 changed files.
- **nastech_cli/:** 39 changed files.
- **plugin-catalog/:** 7 changed files.
- **pm/:** 4 changed files.
- **scripts/:** 2 changed files.
- **tests/:** 78 changed files.
- **tools/:** 6 changed files.
- **web/:** 11 changed files.
- **website/:** 11 changed files.

## Delivered improvements

### New capabilities

- feat(telemetry): updates that stop before applying say why
- feat(plugin-catalog): add nastech-field-notes — pitfalls and local core patches

### Reliability and fixes

- fix(mcp): reject fabricated DCR for providers without RFC 7591 registration (#78190)
- fix(kanban): only sweep a parent workspace once the parent itself is terminal
- fix(pm): an interrupted orphan reclaim leaves a dir the next pass still finds
- fix(pm): orphan reclaim runs on every prune pass and keeps checkouts it cannot see
- fix(pm): reclaim dependency state of deleted checkouts (pm gc + startup worktree prune)
- fix(desktop): hide unknown cloud agent status
- fix(web): scope structured reasoning UI to assistant messages
- fix(update): review the macOS lock scan's lsof/ps lookups; keep it stdlib-only
- fix(update): the macOS lock scan finds ps when the launcher's PATH has none
- fix(update): on macOS only a git working in this checkout keeps a dead index.lock
- fix(update): the start-of-update index.lock reclaim never takes a live git's lock
- fix(update): only a killed update's index.lock is reclaimed at once
- 37 additional reliability and fixes updates are included in this verified snapshot.

### Documentation

- docs(telemetry): how update dashboards count a partial run
- docs(agent): say skipped-result content uses str.replace for {name}
- docs: stop presenting Desktop Light as a shipped download

### Improvements

- test(desktop): cover empty cloud agent status
- refactor(web): move session source config to SessionsPage_sources sibling; satisfy code-health ratchet
- test(web): behaviour coverage for structured reasoning transcript rendering
- Fix reasoning markup rendering in dashboard
- test(ci): the CI replay does not run Git Bash under x64 emulation on Windows arm64
- test(ci): the CI replay names a silent step's exit code
- chore(desktop): refresh locales/_keys.desktop.json for cron.queuedRun
- refactor(desktop-i18n): move billingBlock copy into en_billing sibling
- test: detached-writer custody tests read a pid from a beat that can never be empty
- test(e2e/desktop): give the build-fail updater its manual-outcome grace before asserting it exited
- test(desktop-update): a hand-off log read racing Add-Content retries, not fails
- test(telemetry): pre-apply exit classes, parked parity, receipt-less refusals; docs + smoke
- 31 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
