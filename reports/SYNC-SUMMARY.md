# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 256 commits affecting 3236 files.
- **Source revision:** `b3c28838095b`.
- **Previous source revision:** `18c525b669b6`.

## Technical coverage

- **.github/:** 1 changed files.
- **agent/:** 42 changed files.
- **apps/:** 60 changed files.
- **cli-config.yaml.example/:** 2 changed files.
- **cli.py/:** 4 changed files.
- **contributors/:** 10 changed files.
- **cron/:** 1 changed files.
- **gateway/:** 153 changed files.
- **locales/:** 87 changed files.
- **nastech_cli/:** 65 changed files.
- **nastech_logging.py/:** 1 changed files.
- **nastech_state_gateway.py/:** 4 changed files.
- **nastech_state_local_lineage.py/:** 4 changed files.
- **nastech_state_local_migration.py/:** 1 changed files.
- **nastech_state_messages.py/:** 1 changed files.
- **nastech_state_mutation_retirement.py/:** 17 changed files.
- **nastech_state_mutations.py/:** 1 changed files.
- **nastech_state_portability.py/:** 1 changed files.
- **nastech_state_runtime.py/:** 4 changed files.
- **nastech_state_sessions.py/:** 1 changed files.
- **nastech_state_terminal.py/:** 4 changed files.
- **plugin-catalog/:** 54 changed files.
- **plugins/:** 38 changed files.
- **scripts/:** 2 changed files.
- **tests/:** 197 changed files.
- **tests-js/:** 1 changed files.
- **tools/:** 12 changed files.
- **tui_gateway/:** 10 changed files.
- **ui-tui/:** 4 changed files.
- **website/:** 19 changed files.

## Delivered improvements

### New capabilities

- feat(plugin-catalog): add scalekit (#140032)
- feat(plugin-catalog): add offpeak-bekci — Ollama Cloud off-peak window + approval-gated work queue
- feat(catalog): add Tsubasa model-provider plugin
- feat(plugin-catalog): add the edit-ledger catalog card
- feat(plugin-catalog): add edit-ledger
- feat(plugin-catalog): add the interim-ledger catalog card
- feat(plugin-catalog): add interim-ledger
- feat(plugin-catalog): add gadget (Nastech Gadget hardware platform)
- feat(plugin-catalog): add nastech-whatsapp-voice plugin
- feat(plugin-catalog): add nastech-lang-it-full — Italian Desktop language pack
- feat: archive stale dirty worktrees before removing them, sweep every repo, ask on dirty exit
- feat(plugins): document and allowlist the platform-plugin public surface
- 5 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(plugin-catalog): re-pin nastech-whatsapp-voice to e472a47
- fix(gateway): answer a storage error in a moved chain's pre-bind with a 503
- fix(gateway): fence a route whose retirement value is not valid JSON
- fix(gateway): strip a retired route from sessions.json when it is retired
- fix(gateway): keep an earlier release's unscoped retirement marker unscoped when retiring again
- fix(gateway): refuse a moved chain before a streamed response starts
- fix(gateway): keep a secondary's delete fence past the retry horizon
- fix(gateway): let a pruned secondary's shared routing fence age out by itself
- fix(gateway): keep a retired route out of the sessions.json mirror
- fix(gateway): refuse a chain successor whose walk lost a fence before its bind
- fix(gateway): key session retirement by profile in the shared routing index
- fix(state): let a swept caller-named API session id age out
- 119 additional reliability and fixes updates are included in this verified snapshot.

### Performance

- perf(gateway): check a local receipt's entry once when nothing was adopted
- perf(memory): resolve the bound profile key and the tool-call signature once per manager
- perf(gateway): scan API tombstones only for a client Idempotency-Key

### Documentation

- docs(plugin-catalog): expose Ace media service names in search
- docs(catalog): disclose Tsubasa region and tool limits
- docs(catalog): add Antenna banner image
- docs(weixin): the connector docstring names both no-bundle cases
- docs(auth): say when the credential context falls back to the platform store
- docs: keep the catalog rules block identical to plugin-catalog/README.md
- docs(gateway): name the usage_frame view's two exceptions to the embedded ticker
- docs(api-server): say how an Idempotency-Key conflict arrives per mode
- docs(api-server): list the Idempotency-Key conflict fields per endpoint
- docs(api-server): what an Idempotency-Key covers after a session delete
- docs(state): note that load_result decodes the parsed row in place
- docs(gateway): a legacy custom_providers entry is named by its display name
- 1 additional documentation updates are included in this verified snapshot.

### Improvements

- chore: map contributor email for saif-at-scalekit
- chore(catalog): raise scalekit requires_nastech to >=0.20.0 (agent.secret_scope)
- chore(catalog): drop local-copy comments from offpeak-bekci entry
- chore: map contributor email for onkanat
- chore(catalog): review disclosure for offpeak-bekci
- plugin-catalog: offpeak-bekci English-first text + dil setting; re-pin to 0.1.4 (7b9a1c4)
- katalog: offpeak-bekci 0.1.2 pini (a3427af) — ozet/sayaç düzeltmesi
- plugin-catalog: offpeak-bekci pin ve surum 0.1.1'e tazelendi
- plugin-catalog: pin the chip screenshot to the entry's commit
- chore: map contributor email for cenab
- chore(catalog): review disclosure for tsubasa
- plugin-catalog: nastech-teammates 1.0.0
- 80 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
