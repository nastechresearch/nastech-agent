# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 513 commits affecting 1249 files.
- **Source revision:** `5dd15872a687`.
- **Previous source revision:** `d66341ab2863`.

## Technical coverage

- **.github/:** 10 changed files.
- **acp_adapter/:** 7 changed files.
- **agent/:** 53 changed files.
- **apps/:** 850 changed files.
- **cli-config.yaml.example/:** 2 changed files.
- **cli.py/:** 9 changed files.
- **contributors/:** 33 changed files.
- **cron/:** 30 changed files.
- **evals/:** 12 changed files.
- **flake.lock/:** 1 changed files.
- **flake.nix/:** 1 changed files.
- **gateway/:** 24 changed files.
- **locales/:** 34 changed files.
- **mcp_serve.py/:** 1 changed files.
- **nastech_cli/:** 141 changed files.
- **nastech_state.py/:** 1 changed files.
- **nastech_state_schema.py/:** 2 changed files.
- **nix/:** 5 changed files.
- **optional-skills/:** 7 changed files.
- **package-lock.json/:** 1 changed files.
- **plugins/:** 29 changed files.
- **providers/:** 1 changed files.
- **pyproject.toml/:** 3 changed files.
- **run_agent.py/:** 3 changed files.
- **scripts/:** 3 changed files.
- **skills/:** 4 changed files.
- **tests/:** 277 changed files.
- **tools/:** 81 changed files.
- **tui_gateway/:** 12 changed files.
- **ui-tui/:** 37 changed files.
- **uv.lock/:** 3 changed files.
- **web/:** 19 changed files.
- **website/:** 96 changed files.

## Delivered improvements

### New capabilities

- feat(desktop): agent-applied layout presets — apply_layout joins the desktop_ui toolset
- feat(tui): restore the earlier answer when a batch question is re-visited
- feat(tui): Tab cycles batch clarify questions directly
- feat(cli): batch clarify back-navigation and answer visibility
- feat(desktop): single confirm for the batch clarify card
- feat(cli): compact multi-question clarify panel
- feat(tui): compact multi-question clarify prompt
- feat(desktop): multi-question clarify card with per-question locks
- feat(tui_gateway): batch clarify bridge with per-question locks
- feat(clarify): accept a questions batch in the clarify tool core
- feat(ci): add nix flake check as unrequired job
- feat(nix): home-manager module, shared with the NixOS module
- 80 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix: never evict pinned CIMD sockets from the callback reservation FIFO
- fix(goals): /goal resume actually restarts work after budget exhaustion
- fix(desktop): /goal clear removes the Goal paused card immediately
- fix(desktop): Bots sidebar highlight and Cronjobs tile now follow the chat on screen
- fix(desktop): merge duplicate batch clarify cards
- fix(nix): let the install-method stamp name a home-manager install
- fix(aux): retry once without response_format when a provider rejects it
- fix(aux): translate top-level response_format kwarg on the Anthropic adapter
- fix(aux): translate response_format to output_config.format for anthropic transport
- fix(desktop): hide close affordance on navigation tabs
- fix(gateway): real user text stays clean in the transcript on resume-pending turns (#86580)
- fix(gateway): persist resume recovery notes
- 220 additional reliability and fixes updates are included in this verified snapshot.

### Performance

- perf(desktop): durable transcript-tail cache — bot wakes paint at ~0ms
- perf(desktop): Bot Mode wakes paint-first — transcript paint completes the wake instead of the full runtime boot (#89206 class)
- perf(desktop): stop the translucency slider thrashing the main process
- perf(cron): skip run_claim clear for recurring jobs on dispatch failure

### Documentation

- docs(clarify): advertise the questions batch in the tool description
- docs: describe multi-question clarify batches per surface
- docs: document one-click plugin install links (nastech://plugin/install)
- docs(desktop): state one fallthrough contract at the agent seam
- docs(teams-pipeline): document fetch --organizer-user-id
- docs: escape backslash in cli-symbols glossary so MDX compiles
- docs: add CLI symbols glossary reference page
- docs(relay): clarify timeout payload isolation
- docs(desktop): document the tabbed SESSIONS|BOTS sidebar, Bots-mode-only Cronjobs pane, per-bot Hide/Unhide, and host.paneVisibility (#88788, #88800)
- docs: reflect the unified Gateways page, settings profile scope, plugins cleanup, Bot Mode group rows, and host.openWorkspace
- docs(termux): document community pkg distribution
- docs(sdk): document profiles.list preferred_session_ids lookup
- 9 additional documentation updates are included in this verified snapshot.

### Improvements

- MCP CIMD auth
- fmt(js): `npm run fix` on merge (#89619)
- test(desktop): batch clarify E2E spec and mock trigger
- refactor(ci): hoist docker detect-changes into the .py file
- fmt(js): `npm run fix` on merge (#89580)
- chore: remove case-colliding agent@Agents-Mac-mini.local contributor entries
- test: shrink the goal-DB timing tests to sub-second wall time
- refactor(goals): share one dropped-write warning across managers
- refactor(desktop): wrap the prepareGatewayForAgent signature at the project width
- fmt(js): `npm run fix` on merge (#89501)
- fmt(js): `npm run fix` on merge (#89492)
- fmt(js): `npm run fix` on merge (#89485)
- 152 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
