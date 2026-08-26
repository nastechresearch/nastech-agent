# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 88 commits affecting 1339 files.
- **Source revision:** `f751a8c5467c`.
- **Previous source revision:** `4c1f53be10d0`.

## Technical coverage

- **agent/:** 19 changed files.
- **apps/:** 81 changed files.
- **cli-config.yaml.example/:** 4 changed files.
- **cli.py/:** 2 changed files.
- **contributors/:** 6 changed files.
- **cron/:** 2 changed files.
- **gateway/:** 8 changed files.
- **nastech_cli/:** 33 changed files.
- **nastech_state.py/:** 1 changed files.
- **nastech_state_common.py/:** 1 changed files.
- **optional-mcps/:** 101 changed files.
- **plugins/:** 3 changed files.
- **pyproject.toml/:** 1 changed files.
- **run_agent.py/:** 2 changed files.
- **scripts/:** 5 changed files.
- **skills/:** 1 changed files.
- **tests/:** 64 changed files.
- **tools/:** 24 changed files.
- **toolsets.py/:** 1 changed files.
- **tui_gateway/:** 1 changed files.
- **uv.lock/:** 1 changed files.
- **website/:** 26 changed files.

## Delivered improvements

### New capabilities

- feat(tool-search): multi-query search, batched describe, Snowball stemming
- feat(desktop): add --setup-tcc-identity to keep macOS TCC grants across rebuilds
- feat(desktop): hide the docked Browser tab while it is popped out
- feat(desktop): give the in-app Browser its own OS window
- feat(mcp-catalog): add Grafana Cloud MCP server
- feat(desktop): open a Browser tab in the default browser from its context menu
- feat(desktop): let a pane prefix the zone tab menu
- feat(desktop): OS-keychain encryption for stored secrets is now opt-in — no more macOS Keychain password prompt on every launch
- feat(cron): acked failure signatures stop re-pinging — durable incidents + ack CLI (salvage #94692) (#95017)
- feat(web): cache_exempt_hosts — always-live fetches for staging/tunnel sites
- feat(web): TTL result caching for web_search + web_extract
- feat(mcp): add 18 more live-verified remote MCPs from the final sweep
- 9 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(update): also defer the missing-binary CUA install on Windows
- fix(update): defer interactive CUA installs on Windows
- fix(livetest): render multi-query bridge calls
- fix(tool-describe): separate missing and direct names
- fix(tool-search): preserve exact and per-query ranking semantics
- fix(desktop): keep the Cronjobs pane subscribed to roster hydration
- fix(nastech-bots): stop New Cronjob dialog crash when the owner is a roster object
- fix(desktop): stop the edit composer's timers from outliving it
- fix(desktop): copy unsafe RPC rejections instead of mutating name
- fix(desktop): coerce bot RPC rejections for React 19 error formatting
- fix(desktop): scope Cronjobs pane to the roster-clicked bot when the focused session has no owner (#94516)
- fix(desktop): make --setup-tcc-identity produce a VALID signing identity on modern macOS
- 29 additional reliability and fixes updates are included in this verified snapshot.

### Performance

- perf(tool-search): cache stems and bound result metadata

### Documentation

- docs(desktop): name the timer drain in the effect that performs it
- docs(browser): call Browserbase the alternative
- docs(browser): put Browser Use Cloud first
- docs(skill): troubleshoot stale web_extract pages — cache carveouts + cache_exempt_hosts
- docs(memory): document the pre-compress checkpoint contract

### Improvements

- test(tool-search): make salvage-seam tests order- and stem-robust
- test(tool-search): kill the shared-stemmer mutant with cache-missing input
- test(tool-search): exercise stemmer in parallel
- refactor(tool-search): keep batch caps internal
- fmt(js): `npm run fix` on merge (#95114)
- test: pin CreateRoutineDialog owner-object label resolution (follow-up for salvaged #93572)
- chore: map contributor email
- style(desktop): sort secret-storage-policy import per perfectionist lint
- Merge pull request #90129 from rroverin/fix/nvidia-nim-tool-message-name-field
- refactor(prompt): remove the ~1.2K-token Nastech Subscription block from the system prompt (#95005)
- chore: map contributor email for attribution gate
- test(mcp-catalog): actually exercise the exfil-shaped-manifest rejection
- 8 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
