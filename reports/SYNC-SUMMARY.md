# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 78 commits affecting 1449 files.
- **Source revision:** `7cd91114b462`.
- **Previous source revision:** `5a8e8a6b8748`.

## Technical coverage

- **agent/:** 27 changed files.
- **apps/:** 26 changed files.
- **contributors/:** 4 changed files.
- **cron/:** 3 changed files.
- **evals/:** 1 changed files.
- **gateway/:** 11 changed files.
- **mcp_serve.py/:** 1 changed files.
- **nastech_cli/:** 46 changed files.
- **nastech_state.py/:** 3 changed files.
- **nastech_state_common.py/:** 1 changed files.
- **nastech_state_registry.py/:** 2 changed files.
- **plugins/:** 9 changed files.
- **run_agent.py/:** 1 changed files.
- **scripts/:** 4 changed files.
- **tests/:** 127 changed files.
- **tools/:** 11 changed files.
- **tui_gateway/:** 5 changed files.
- **web/:** 19 changed files.
- **website/:** 12 changed files.

## Delivered improvements

### New capabilities

- feat(web): add Tavily web search and extract provider
- feat(desktop): add Russian (ru) locale
- feat(skills): render the configured create dir in every instruction that names the path
- feat(skills): skills.create_dir routes agent-created skills to a configured directory

### Reliability and fixes

- fix(web): drop tavily from the removed-backend registry after the restore
- fix(tavily): update Tavily provider documentation
- fix(tui-gateway): gate the ws-orphan interrupt of running turns on activity staleness
- fix(state): break provably-orphaned repair/FTS-rebuild locks left by dead holders (#100108)
- fix(state): stop the on-write identity probe cancelling our own POSIX locks (#100368)
- fix(gateway): gate record-less visible-text match on _already_sent
- fix(gateway): judge delivery success against final content, not flag trust (#95382, #98552)
- fix(web): stale removed-backend config warns at startup and errors by name
- fix(agent): accept marker-only finish_reason after stream supersession
- fix(auth): compare pool-identity callers against all candidate keys
- fix(auth): look up keyed custom providers by durable pool slug
- fix(proxy): harden SSE DONE tracker — spec multi-line data joins, truthy lastOne, EOF-write guard
- 38 additional reliability and fixes updates are included in this verified snapshot.

### Improvements

- test(gateway): pre-warm the goals SessionDB cache in async goal tests
- test: managed-runtime source scan survives a vanishing sdist dir (TOCTOU)
- test(gateway): widen pending-drain chain wait budget (4s -> 20s)
- test: raise tight wall-clock bounds that flaked on loaded CI runners
- test(auth): cover keyed providers.<key> credential-pool lookup
- test(proxy): cover multi-line SSE data joins, truthy lastOne, EOF-without-blank-line dispatch
- fmt(js): `npm run fix` on merge (#100517)
- style(desktop): satisfy eslint and prettier in profile migration
- test(desktop): cover active-profile migration helpers
- refactor(desktop): extract pure active-profile migration helpers
- test(installer): cover managed Python timeout
- chore: map contributor email for #100352 salvage
- 12 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
