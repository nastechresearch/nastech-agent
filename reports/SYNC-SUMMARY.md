# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 86 commits affecting 1201 files.
- **Source revision:** `d66341ab2863`.
- **Previous source revision:** `7095e23eb206`.

## Technical coverage

- **.gitignore/:** 1 changed files.
- **agent/:** 15 changed files.
- **apps/:** 212 changed files.
- **cli-config.yaml.example/:** 1 changed files.
- **contributors/:** 5 changed files.
- **gateway/:** 7 changed files.
- **hermes_cli/:** 26 changed files.
- **hermes_state.py/:** 4 changed files.
- **plugins/:** 1 changed files.
- **pyproject.toml/:** 1 changed files.
- **run_agent.py/:** 4 changed files.
- **scripts/:** 3 changed files.
- **skills/:** 2 changed files.
- **tests/:** 60 changed files.
- **tools/:** 23 changed files.
- **tui_gateway/:** 4 changed files.
- **ui-tui/:** 13 changed files.
- **uv.lock/:** 1 changed files.
- **website/:** 16 changed files.

## Delivered improvements

### New capabilities

- feat(delegation): record model/provider in live-transcript manifest (#telemetry)
- feat(desktop): carry remote gateway headers through the connections registry, test probes, and Settings UI
- feat(desktop): support remote gateway headers
- feat(desktop): add status bar reconnect for offline gateways
- feat(state): support the context-manager protocol on SessionDB
- feat: raise Codex OAuth context to 900K for gpt-5.6 family and gpt-5.4 (subscription 1M rollout)
- feat: sync bundled Bot Mode with multi-source roster (Nastech-Bot-Mode#68)
- feat(agent): one-time protocol upgrade for legacy Bot Chat sessions
- feat(agent): capability-refresh + timeless prompts for eternal Bot Chat sessions
- feat(agent): core Bot Mode teammate protocol — stable-tier prompt section
- feat(desktop): bundle Bot Mode (nastech-bots) as a built-in, default-on plugin
- feat(desktop): expose connection-aware plugin routing
- 2 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(status): strict writer-identity ownership for aggregated platform entries (OOF-3)
- fix(status): freshness-filter aggregated per-profile platform entries (OOF-3)
- fix(status): aggregate independent per-profile gateway failures; harden key filter (OOF-3)
- fix(gateway): surface multiplex profile failures (OOF-3)
- fix(gateway): attribute scoped credential lock conflicts to the owning profile (OOF-3)
- fix(desktop): self-heal dropped SSH/HTTP registered remote connections
- fix(gateway): scope slash.exec's skill-command check to the session's profile
- fix(skills): rescan skill commands cache when active profile changes
- fix(gateway): accept CJK full-width punctuation as MEDIA path terminators
- fix(gateway): ignore invalid managed Node directories
- fix(state): avoid overlapping context manager change
- fix(state): release abandoned session database handles
- 42 additional reliability and fixes updates are included in this verified snapshot.

### Documentation

- docs(computer-use): note driver contract auto-repair at update and runtime

### Improvements

- chore: map contributor email for tigercraft4 (PR #74468 salvage)
- fmt(js): `npm run fix` on merge (#88079)
- chore: map contributor email for attribution audit
- fmt(js): `npm run fix` on merge (#88016)
- test(desktop): steer suite drives the real redirectPrompt path; hydration fixture carries durable row shape
- test(desktop): harden steer-order suite against fake-timer id collisions
- test(desktop): pin steered-turn transcript order end-to-end
- fmt(js): `npm run fix` on merge (#88014)
- chore: add contributor email mapping for addelh
- fmt(js): `npm run fix` on merge (#87880)
- chore: map contributor email for xkam7ar
- Revert "fix(agent): harden canonical tool call deduplication"
- 5 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
