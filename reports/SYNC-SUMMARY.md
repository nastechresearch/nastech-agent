# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 65 commits affecting 1346 files.
- **Source revision:** `86ae906e88b2`.
- **Previous source revision:** `f0c0c986c4cb`.

## Technical coverage

- **.mailmap/:** 1 changed files.
- **agent/:** 3 changed files.
- **apps/:** 119 changed files.
- **contributors/:** 9 changed files.
- **cron/:** 4 changed files.
- **gateway/:** 4 changed files.
- **locales/:** 17 changed files.
- **nastech_cli/:** 9 changed files.
- **nastech_state.py/:** 1 changed files.
- **skills/:** 1 changed files.
- **tests/:** 32 changed files.
- **tools/:** 12 changed files.
- **tui_gateway/:** 1 changed files.
- **website/:** 2 changed files.

## Delivered improvements

### New capabilities

- feat(cron): import-error cron failures now name gateway code skew and the one-command fix (#95294 part 3)

### Reliability and fixes

- fix(desktop): skip macOS TCC-protected media dirs in git repo scan
- fix(terminal): tolerate macOS TCC PermissionError in _safe_getcwd
- fix(computer_use): pitch background-FIRST (not background-only) in schema, prompt block, and skill
- fix(desktop): single-owner backend dial claim in Electron main (#90812)
- fix(desktop): revalidate pooled remote/SSH backends on power resume (#93910)
- fix(gateway): redeliver transient failures after reconnect
- fix(desktop): poll-guard reset is fire-and-forget off the redial path
- fix(desktop): isolate the poll-guard reset import + sort-imports lint
- fix(desktop): republish the connections registry to renderers after every successful save (#95393)
- fix(desktop): release reconnect-orphaned warm transcripts once their authoritative state settles
- fix(desktop): harden the dead-session poll guard per #94950 review
- fix(desktop): stop the status-stack poll storming a dead session with 4001s
- 29 additional reliability and fixes updates are included in this verified snapshot.

### Documentation

- docs(cron): describe widened continuable scope (origin fallback + explicit opt-in)

### Improvements

- fmt(js): `npm run fix` on merge (#95511)
- chore: map contributor email for wiseconnex
- test: loosen frozen bare-verdict dict in cua_0_9 sibling test to decision contract
- refactor(computer_use): diet schema + delete prompt block (~1.4K tok/call); remove max_elements, ladder moves to response verdicts
- test(gateway): prove delivered rows are never reclaimed by the reconnect sweep
- chore: map justinjohnson25600 and BrunoBza contributor emails
- refactor(checkpoints): call the size-cap predicate instead of restating it
- chore: map contributor email for notkisk
- Merge pull request #95477 from kshitijk4poor/chore/mailmap-kshitijk4poor
- chore: mailmap kshitijkapoorr@gmail.com to kshitijk4poor's canonical noreply
- test: assert omitted attach_to_session stays absent from formatted list output
- chore: map kshitijkapoorr@gmail.com to kshitijk4poor in contributors/emails
- 10 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
