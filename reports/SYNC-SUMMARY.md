# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 103 commits affecting 1370 files.
- **Source revision:** `ef46ec03e114`.
- **Previous source revision:** `790e1eb6bd57`.

## Technical coverage

- **.github/:** 9 changed files.
- **agent/:** 5 changed files.
- **apps/:** 115 changed files.
- **cli-config.yaml.example/:** 1 changed files.
- **contributors/:** 4 changed files.
- **gateway/:** 7 changed files.
- **nastech_cli/:** 41 changed files.
- **plugins/:** 4 changed files.
- **scripts/:** 7 changed files.
- **tests/:** 81 changed files.
- **tools/:** 20 changed files.
- **tui_gateway/:** 19 changed files.
- **website/:** 7 changed files.

## Delivered improvements

### New capabilities

- feat(relay): stamp slack unfurl_links/unfurl_media onto outbound frame metadata (gateway-directed)
- feat(slack): add link unfurl controls
- feat(desktop): Managed updates section drives per-connection SSH updates
- feat(browser): close-with-approval flow for Windows real-profile (toggle arms, agent asks, blocked if still locked) [proof do-not-merge]
- feat(browser): consented auto-close of a running browser for Windows real-profile [proof workflow do-not-merge]
- feat(browser): real-profile browsing via agent-browser copy + browser-use CDP
- feat(browser): consent-gated real default-Chromium profile for local browsing + local_browser arg
- feat(desktop): wire managed SSH update engine into main process
- feat(desktop): managed SSH remote update engine — extracted from #93042
- feat(chat-plane): trace_id + turn telemetry, transient-delta split, seq-namespace epoch
- feat(gateway): slim WS-only server — remove FastAPI/uvicorn from desktop boot path

### Reliability and fixes

- fix(mcp): un-invert the stdio children liveness check (#94335)
- fix(nastech_cli): surface fail-closed config write refusals cleanly
- fix(nastech_cli): stop config set/unset from wiping user overrides on invalid YAML
- fix(compression): preserve terminal lifecycle for lock skips
- fix(compression): suppress duplicate completion notices
- fix(config): preserve lossy decimal values as strings
- fix(relay): fall back to descriptor platform for unfurl stamping
- fix(slack): coerce string unfurl knobs on the native plane
- fix(relay): coerce string unfurl knobs and disable Slack draft streaming
- fix(slack): preserve unfurl controls during streaming
- fix(slack): honor unfurl controls for media captions
- fix(relay): restore voice-note STT — wire media[] MIMEs, message_type "voice", and a User-Agent for CDN downloads (#95274)
- 45 additional reliability and fixes updates are included in this verified snapshot.

### Documentation

- docs(slack): note caption ordering and streaming fallback for unfurl knobs

### Improvements

- test(mcp): absorb watcher-consumer and fail-open liveness cases from #94521/#94661
- chore: map paulapsp157@gmail.com -> Aoshi-Dev (PR #96003 salvage)
- test(nastech_cli): make test_default_path pass on native Windows
- test(nastech_cli): align malformed YAML set/unset expectations with RuntimeError
- refactor(compression): fold review follow-ups on #71488 salvage
- test(compression): cover failed in-place split status
- Merge pull request #96118 from kshitijk4poor/revert/94245
- Revert "Merge pull request #94245 from kshitijk4poor/feat/gw-event-replay"
- Merge pull request #94245 from kshitijk4poor/feat/gw-event-replay
- test(relay): cover media-lane unfurl stamping and descriptor fallback
- chore(contributors): map potatosaladx@gmail.com to potatosalad (attribution for salvaged #79436/#81128 commits)
- test(slack): cover default and split unfurl behavior
- 22 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
