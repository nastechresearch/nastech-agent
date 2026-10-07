# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 859 commits affecting 2875 files.
- **Source revision:** `a3ed4a173070`.
- **Previous source revision:** `e97923c38acb`.

## Technical coverage

- **.github/:** 14 changed files.
- **.gitignore/:** 1 changed files.
- **CONTRIBUTING.es.md/:** 2 changed files.
- **CONTRIBUTING.md/:** 2 changed files.
- **agent/:** 77 changed files.
- **apps/:** 503 changed files.
- **cli-config.yaml.example/:** 3 changed files.
- **cli.py/:** 1 changed files.
- **contributors/:** 20 changed files.
- **cron/:** 77 changed files.
- **evals/:** 5 changed files.
- **gateway/:** 79 changed files.
- **locales/:** 110 changed files.
- **model_tools.py/:** 1 changed files.
- **nastech_bootstrap.py/:** 3 changed files.
- **nastech_cli/:** 492 changed files.
- **nastech_constants.py/:** 1 changed files.
- **nastech_constants_scratch.py/:** 3 changed files.
- **nastech_platform/:** 4 changed files.
- **nastech_state.py/:** 2 changed files.
- **nastech_state_messages.py/:** 1 changed files.
- **nastech_state_portability.py/:** 1 changed files.
- **nastech_state_sessions.py/:** 1 changed files.
- **nastech_state_usage.py/:** 1 changed files.
- **nix/:** 3 changed files.
- **optional-skills/:** 10 changed files.
- **plugin-catalog/:** 62 changed files.
- **plugins/:** 54 changed files.
- **pm/:** 22 changed files.
- **pyproject.toml/:** 1 changed files.
- **run_agent.py/:** 1 changed files.
- **scripts/:** 106 changed files.
- **skills/:** 3 changed files.
- **tests/:** 761 changed files.
- **tests-js/:** 1 changed files.
- **tools/:** 87 changed files.
- **toolsets.py/:** 2 changed files.
- **tui_gateway/:** 37 changed files.
- **ui-tui/:** 20 changed files.
- **uv.lock/:** 1 changed files.
- **web/:** 48 changed files.
- **website/:** 82 changed files.

## Delivered improvements

### New capabilities

- feat(plugin-catalog): add switchbot-control
- feat(plugins): a portable package can ask Nastech to gate its MCP server
- feat(catalog): add Kinprove genealogy research recipes
- feat(catalog): pin Jot 0.2.0 with current screenshots
- feat(catalog): add Jot notes for Nastech Desktop
- feat(plugin-catalog): add gbrain-pointer (community GBrain memory provider)
- feat(plugin-catalog): add alice-voice plugin
- feat(plugin-catalog): add pastdotdev memory provider
- feat(plugin-catalog): add klipper-print-watch
- feat(plugin-catalog): stalkchain banner and update
- feat(plugin-catalog): bump stream-speed to 1.1.0
- feat(plugin-catalog): bump aux-ledger to 1.1.0
- 36 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(update): skip the restore import check only for non-runtime files
- fix(update): a stash with no Python is never rejected by the import probe (#130101)
- fix: POSIX update pause drains turns first and survives a killed update cleanly
- fix(update): a replayed gateway gets its own profile's environment, not the updater's
- fix(gateway): decode the re-entered .cmd launcher directly; keep the base64 form untouched in the test
- fix(gateway): a gateway re-entered through a dependency-syncing launcher is a gateway
- fix(update): adopt a serving gateway through the canonical identity reader
- fix(update): the POSIX gateway pause never blocks an update
- fix(update): Windows keeps resuming after the fleet restart, never twice
- fix(update): a terminal-launched gateway is paused instead of mistaken for a supervised one
- fix(update): adopt a paused gateway's home only through its runtime lock, never a process scan
- fix(update): pause POSIX gateways before the first checkout move, restart them after deps
- 501 additional reliability and fixes updates are included in this verified snapshot.

### Performance

- perf(cron): skip the skipped-run count in `cron list`
- perf(cron): let a failed scan save count as the degraded tick's probe

### Documentation

- docs(plugin-catalog): show the official Ace Data Cloud logo
- docs(cron): name nastech_bootstrap as the pre-ack relaunch in the worker docstrings
- docs(kanban): document archived as a manual-move source in the workflow contract
- docs(cron): store gauges are host-wide; notices use the owning profile's language
- docs(cron): note that a gateway restart mid-outage drops the one-shot carve-out
- docs(cron): document the unwritable-store headline, notices and fix steps
- docs(cron): say occurrences.py also holds the catch-up counter marker
- docs: crash-cell oracle, strict acceptance and derived update routing
- docs: crash-cell matrix for source updates
- docs(stt): xAI STT model pin wording + auto-detect format note
- docs(stt): clarify xAI model default
- docs(telemetry): the send explainer and Desktop consent window name the fresh-install note
- 2 additional documentation updates are included in this verified snapshot.

### Improvements

- chore(catalog): review disclosure for switchbot-control
- chore(plugin-catalog): bump switchbot-control to bb68cb4
- chore: map contributor email for lazyants
- chore: map contributor email for praggybuilds
- chore(catalog): review disclosure for gbrain-pointer
- Re-pin agora to v2.0.10
- chore(catalog): review disclosure for alice-voice
- chore(plugin-catalog): bump pinned-folders entry sha to v0.1.4
- chore(catalog): review disclosure for kimchi-acp-provider
- catalog: pin kimchi-nastech@d6ffe628 — make --yolo opt-in per review
- catalog: add kimchi-acp-provider (Kimchi harness over ACP stdio)
- chore(catalog): pastdotdev disclosure form + contributor map for Kiloris
- 270 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
