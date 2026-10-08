# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 57 commits affecting 2883 files.
- **Source revision:** `cc75e8f4021f`.
- **Previous source revision:** `7dab93b06e2b`.

## Technical coverage

- **agent/:** 4 changed files.
- **apps/:** 117 changed files.
- **gateway/:** 1 changed files.
- **locales/:** 1 changed files.
- **nastech_cli/:** 17 changed files.
- **nastech_state_compression.py/:** 1 changed files.
- **nastech_state_search.py/:** 5 changed files.
- **plugin-catalog/:** 2 changed files.
- **plugins/:** 2 changed files.
- **scripts/:** 2 changed files.
- **tests/:** 30 changed files.
- **tools/:** 2 changed files.
- **web/:** 7 changed files.
- **website/:** 2 changed files.

## Delivered improvements

### New capabilities

- feat(models): add anthropic/claude-haiku-5.5 to OpenRouter and Nastech Portal catalogs (#134759)

### Reliability and fixes

- fix(ci): route web_build_limits.py to the update e2e lanes
- fix(agent): bound lease lock tolerance by the row's committed expiry
- fix(agent): stop a locked lease refresh once its lifetime runs out
- fix(agent): do not interrupt a turn when lease refresh hits a SQLite lock
- fix(kanban): dashboard rejects stale archived/deleted board slugs
- fix(kanban): connect()/init_db() refuse to recreate dead boards
- fix(kanban): board identity requires board.json; archive leaves a tombstone
- fix(gateway): stop _ensure_windows_gateway_venv_imports leaking PYTHONPATH into global environment
- fix(desktop): the link-title window cannot become visible
- fix(browser): pin local Chromium headless on Windows
- fix(web): bound the dashboard build's CPU and heap (#63338)
- fix(dashboard): hide AuthWidget on 401 via ApiError status
- 20 additional reliability and fixes updates are included in this verified snapshot.

### Documentation

- docs(web): note the dashboard build's resource caps (#63338)

### Improvements

- chore(plugin-catalog): bump nastech-monitoring-dashboard to e4825262
- test(agent): release the lease-test lock on a refusal signal, not a timer
- refactor(kanban): split board metadata/lifecycle into kanban_db_boards; fix ratchet findings
- test(gateway): venv import setup must not leak PYTHONPATH into global environ (#57467)
- test(desktop): fold the MEDIA pdf card case into the existing media suite
- test(desktop): pin the preview height clamp's viewport growth and ceiling
- chore(plugin-catalog): pin claude-subscription-directsdk to 4bc79c7 (Haiku 5.5) (#134749)
- fmt(js): `npm run fix` on merge (#134737)
- style(desktop): sort the projects-sibling imports per perfectionist
- refactor(desktop): move sidebar projects copy into per-locale siblings for #73091
- test(desktop): store-level dismiss/restore round-trip for auto projects
- chore(desktop): regenerate locales/_keys.desktop.json for undo-hide keys
- 11 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
