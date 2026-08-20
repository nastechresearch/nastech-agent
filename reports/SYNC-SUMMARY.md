# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 204 commits affecting 1273 files.
- **Source revision:** `6f31cfad7825`.
- **Previous source revision:** `2eb0b3b2c895`.

## Technical coverage

- **.github/:** 2 changed files.
- **AGENTS.md/:** 1 changed files.
- **agent/:** 47 changed files.
- **apps/:** 214 changed files.
- **cli-config.yaml.example/:** 1 changed files.
- **cli.py/:** 10 changed files.
- **contributors/:** 7 changed files.
- **default.tar.gz/:** 1 changed files.
- **docs/:** 18 changed files.
- **gateway/:** 18 changed files.
- **nastech_cli/:** 69 changed files.
- **nastech_state.py/:** 1 changed files.
- **plugins/:** 45 changed files.
- **run_agent.py/:** 2 changed files.
- **scripts/:** 6 changed files.
- **tests/:** 163 changed files.
- **tools/:** 11 changed files.
- **tui_gateway/:** 4 changed files.
- **ui-tui/:** 7 changed files.
- **website/:** 46 changed files.

## Delivered improvements

### New capabilities

- feat(desktop): updating now updates every target — remote backends, other gateways, and the app itself
- feat(desktop): keep midnight, and retint themes that shade their accent
- feat(desktop): an accent picker plugin, off by default
- feat(desktop): glass ships on, tuned per appearance and platform
- feat(desktop): re-seed any theme's accent from one colour
- feat(desktop): ship the GitHub themes, with Nastech blue on top
- feat: keyless web tier becomes a 5-vendor round-robin ring (adds Tavily, Firecrawl, Keenable)
- feat: identical re-calls enter context as reference stubs, not duplicate payloads
- feat(desktop): the composer collapse ladder continues below stacking
- feat: nastech worktree list/prune — attended reclaim for accumulated worktrees and merged branches
- feat: keyless free-tier failover + Tavily/Firecrawl salvage integration
- feat(computer-use): expose screenshots for chat delivery
- 23 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(desktop): remote-gateway desktop stops lying after disconnects — roster survives outages, spawn failures log, host-key change stops the retry wall
- fix(sessions): error paths return non-zero exit codes (delete/rename/prune/import)
- fix(desktop): sort updates.ts imports for perfectionist lint
- fix(backup): friendly error on unwritable output path instead of raw traceback
- fix(config): set coerces negatives/whitespace/null and rejects malformed keys
- fix(sessions): prune/archive spare pinned sessions by default (data loss)
- fix(cli): /undo typo no longer quits the CLI; +3 slash-command papercuts
- fix(cli): worktree lifecycle messages render colors instead of raw ANSI escapes
- fix(desktop): a fresh profile follows the OS, and plugins stay behind the SDK
- fix(desktop): off means off when glass is turned down
- fix(desktop): the finished-session dot follows the theme
- fix(desktop): renamed Bot Mode agents stay @-taggable by their new name
- 87 additional reliability and fixes updates are included in this verified snapshot.

### Documentation

- docs(desktop): troubleshooting entry for SSH host-key-changed latch
- docs(computer-use): document requesting the actual screenshot on chat surfaces
- docs: tool provider selection follows the nastech tools pick (post #90317)
- docs: correct Exa keyless rate-limit characterization
- docs(relay): link supported observability exporters

### Improvements

- fmt(js): `npm run fix` on merge (#90690)
- Merge pull request #90572 from Nastechresearch/feat/keyless-tavily-firecrawl-failover
- test: capture worktree messages through the _cprint route
- fmt(js): `npm run fix` on merge (#90637)
- test: pin ring entry vendor in provider-routing tests (ring rotation made direct-callable mocks stale)
- chore: retrigger CI (zero-job dispatch failure, auto-heal)
- chore: retrigger CI (zero-job dispatch failure, auto-heal)
- Merge remote-tracking branch 'origin/main' into feat/keyless-tavily-firecrawl-failover
- test: vary marathon-turn fixture args — identical calls now legitimately dedupe to stubs
- ci: retrigger after incident window
- refactor(agent): consolidate uncompressed-overflow guard to one warn site + re-arm
- refactor(cli): fold lock-bit review findings - docstrings, dead tilde forms, _lock_twins idiom
- 53 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
