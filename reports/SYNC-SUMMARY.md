# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 134 commits affecting 1343 files.
- **Source revision:** `f0c0c986c4cb`.
- **Previous source revision:** `f751a8c5467c`.

## Technical coverage

- **.github/:** 2 changed files.
- **agent/:** 7 changed files.
- **apps/:** 316 changed files.
- **contributors/:** 18 changed files.
- **gateway/:** 5 changed files.
- **nastech_cli/:** 22 changed files.
- **plugins/:** 3 changed files.
- **tests/:** 35 changed files.
- **tests-js/:** 5 changed files.
- **tools/:** 4 changed files.
- **tui_gateway/:** 1 changed files.
- **website/:** 5 changed files.

## Delivered improvements

### New capabilities

- feat(openviking): identify Nastech requests
- feat(desktop): add NSScreenCaptureUsageDescription to macOS bundle
- feat(update): unattended-safe cua-driver refresh with fail-fast preflights

### Reliability and fixes

- fix(computer_use): disable embedded daemon overlay
- fix(desktop): clicking a bot no longer burns a model turn on a fake user prompt
- fix(desktop): drop unused registryGatewayWsUrl import left by the header-binding refactor rebase
- fix(desktop): recover remote sessions after gateway restart
- fix(desktop): log when Windows remote SSH skip teardown
- fix(desktop): terminate owned SSH serve backends on quit
- fix(desktop): clarify primary SSH reuse failures
- fix(desktop): reuse migrated primary SSH backend
- fix(desktop): scope registered ssh primary gateway
- fix(desktop): treat ticket 401 as sign-in when native tokens are unreadable
- fix(desktop): refresh remote WebSocket header cache recency
- fix(desktop): bind headers to scoped WebSocket URL
- 86 additional reliability and fixes updates are included in this verified snapshot.

### Documentation

- docs: document the no_overlay auto-detect and new Linux X11 default
- docs(bootstrap): correct marker_owned_by_self justification for current live_marker_owner semantics

### Improvements

- test: pin overlay policy off in embedded-daemon socket/ack contract test
- refactor(cron): halve the cronjob tool schema (2,234 → 1,070 tokens/call) without losing guidance (#95287)
- fmt(js): `npm run fix` on merge (#95365)
- chore: map contributor email for salvaged PR #88544
- refactor(codex): route transports _pair_ids through shared fc_ canonicalization
- refactor(codex): extract shared fc_->call_ canonicalization helper
- test(desktop): pass the pin-write fence into the Show-all order assertion
- test(desktop): lock pin upgrade to server-authoritative pull
- chore: contributor email mappings for salvage class-4
- test(desktop): profile-door dial failure now rejects (post-#81165 contract) — #92265 invariant unchanged
- test(desktop): cover bot reconciliation runtime lifecycle
- fmt(js): `npm run fix` on merge (#95329)
- 19 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
