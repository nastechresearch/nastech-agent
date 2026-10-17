# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 148 commits affecting 3225 files.
- **Source revision:** `e6f57427c198`.
- **Previous source revision:** `18c525b669b6`.

## Technical coverage

- **.github/:** 1 changed files.
- **agent/:** 37 changed files.
- **apps/:** 60 changed files.
- **contributors/:** 1 changed files.
- **gateway/:** 128 changed files.
- **locales/:** 19 changed files.
- **nastech_cli/:** 16 changed files.
- **nastech_logging.py/:** 1 changed files.
- **nastech_state_local_lineage.py/:** 4 changed files.
- **nastech_state_local_migration.py/:** 1 changed files.
- **nastech_state_messages.py/:** 1 changed files.
- **nastech_state_mutation_retirement.py/:** 9 changed files.
- **nastech_state_mutations.py/:** 1 changed files.
- **nastech_state_portability.py/:** 1 changed files.
- **nastech_state_runtime.py/:** 4 changed files.
- **nastech_state_sessions.py/:** 1 changed files.
- **nastech_state_terminal.py/:** 4 changed files.
- **plugins/:** 3 changed files.
- **scripts/:** 2 changed files.
- **tests/:** 151 changed files.
- **tests-js/:** 1 changed files.
- **tools/:** 5 changed files.
- **tui_gateway/:** 10 changed files.
- **ui-tui/:** 4 changed files.
- **website/:** 5 changed files.

## Delivered improvements

### New capabilities

- feat(gateway): steer and edit a canonical queued prompt from Desktop

### Reliability and fixes

- fix(desktop-build): `npm run builder -- --win --x64` can stage its per-target native deps
- fix(desktop): a zero request timeout is no deadline on the canonical socket
- fix(gateway): a pre-upgrade session whose custom endpoint moved resumes on the profile route
- fix(desktop): show the lost-turn card and Discard without expanding the queue
- fix(desktop): show a queued prompt returned from a steer in its FIFO place
- fix(gateway): refuse a cancel that races a queued steer instead of reporting success
- fix(gateway): a late queued steer goes back to its queue, never into a follow-up
- fix(gateway): settle a queued steer by its admission, not by searching its text
- fix(gateway): offer queued-row Steer/Edit on Desktop chats migrated from main
- fix(desktop): an unconfirmed queued-row edit keeps its identity and retries it
- fix(desktop): a queued-row Save reply settles only its own save and keeps newer text
- fix(gateway): list a steer in transfer as `steering` so a returned prompt keeps its card
- 88 additional reliability and fixes updates are included in this verified snapshot.

### Performance

- perf(gateway): check a local receipt's entry once when nothing was adopted
- perf(memory): resolve the bound profile key and the tool-call signature once per manager
- perf(gateway): scan API tombstones only for a client Idempotency-Key

### Documentation

- docs(gateway): name the usage_frame view's two exceptions to the embedded ticker
- docs(api-server): say how an Idempotency-Key conflict arrives per mode
- docs(api-server): list the Idempotency-Key conflict fields per endpoint
- docs(api-server): what an Idempotency-Key covers after a session delete
- docs(state): note that load_result decodes the parsed row in place
- docs(gateway): a legacy custom_providers entry is named by its display name
- docs(memory): say why a claim's weakref callback checks it is still the entry's reference

### Improvements

- Merge pull request #140701 from Nastechresearch/fix/pkg9-windows-live
- Merge pull request #140700 from Nastechresearch/fix/pkg9-desktop-reconnect
- Merge pull request #140699 from Nastechresearch/fix/pkg9-stored-endpoint
- test(e2e): new_machine's base_ref no longer shadows the machine root
- test(desktop-e2e): Desktop attaches to a local gateway that was already running, on Windows
- test(e2e): upgrading a pre-runtime Windows install over its running gateway, elevated and not
- test(desktop): E2E guard for turn state after a lost connection
- test(gateway): drop the removed ticker from the held-writer test's docstring
- refactor(gateway): one requeue statement, one cancel statement, one exact-retry check
- test(gateway): queued-control tests wait on events, not the clock
- test(desktop): say the gateway-frame fixture pins the reader, not the producer
- chore(contributors): map herovivian@gmail.com to herovivian-collab
- 25 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
