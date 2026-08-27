# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 144 commits affecting 1360 files.
- **Source revision:** `790e1eb6bd57`.
- **Previous source revision:** `86ae906e88b2`.

## Technical coverage

- **Dockerfile/:** 1 changed files.
- **agent/:** 12 changed files.
- **apps/:** 170 changed files.
- **contributors/:** 9 changed files.
- **docs/:** 1 changed files.
- **evals/:** 8 changed files.
- **gateway/:** 14 changed files.
- **locales/:** 51 changed files.
- **nastech_cli/:** 63 changed files.
- **package-lock.json/:** 1 changed files.
- **package.json/:** 1 changed files.
- **plugins/:** 8 changed files.
- **tests/:** 84 changed files.
- **tools/:** 12 changed files.
- **tui_gateway/:** 1 changed files.
- **website/:** 15 changed files.

## Delivered improvements

### New capabilities

- feat: MiniMax H3 Max joins the FAL video picker (t2v + i2v)
- feat(update): image/package-managed installs refuse in-place updates through one shared gate (#91277 Phase 3)
- feat(update): bake authoritative image provenance into the Docker image
- feat(kanban): carry the review handoff summary into the wake turn
- feat(agent): fold an agent-as-provider's own tool work back into the turn
- feat(gateway): updaters pause gateways over the control socket instead of tree-killing them (#92091 step 2)
- feat(desktop): fleet profile rail — every registered gateway's agents on one strip
- feat(update): network-bound serve backends survive nastech update on their recorded endpoints (#63206)
- feat(models): add z-ai/glm-5.3-flash to OpenRouter and Nastech Portal catalogs
- feat(compression): lean tail retention is the default — compaction keeps 10-25K verbatim, not 100-240K
- feat(macos): one-switch Full Disk Access guidance in doctor and setup
- feat(deadline): SuspectableBackend protocol — mark timed-out backends suspect

### Reliability and fixes

- fix(update): pause SCM-supervised Windows gateway services before venv mutation
- fix(update): conservative outcomes + serve-ledger coverage for fresh restart recovery
- fix(update): persist fresh recovery outcome
- fix(update): persist per-profile recovery outcomes
- fix(update): verify fresh restart recovery results
- fix(update): recover aborted gateway restart in a fresh process
- fix(update): sweep aborted-fetch tmp_pack debris before it corrupts the pack directory (#93732)
- fix(deps): bump the nanoid@^3 override past GHSA-2v37-7h3g-55p8 (#91931)
- fix(cli): note pre_restart_pids' per-PID data model gap, pin the matching-start_time path
- fix(cli): guard the post-update fleet check against PID reuse
- fix(update): feed Windows gateway relaunch outcome into fleet reconciliation
- fix: harden claim-release guard for bare test doubles; repoint source-pinning test at the impl
- 72 additional reliability and fixes updates are included in this verified snapshot.

### Documentation

- docs: image provenance marker and the shared refusal gate (#91277 Phase 3)
- docs: serve/dashboard backends in the update flow, --plan, and --status (#63206)
- docs: /snapshot restore live-safety behavior

### Improvements

- refactor(clarify): schema diet + single questions[] interface (880 → 335 tok/call, −62%) (#95907)
- fmt(js): `npm run fix` on merge (#95924)
- chore: map contributor emails
- refactor(skills): skill_manage 924 → 518 tok/call — dedup diet, retire 'edit', unadvertise curator-only absorbed_into (#95697)
- fmt(js): `npm run fix` on merge (#95861)
- fmt(js): `npm run fix` on merge (#95858)
- desktop: remove js vestiges
- test: re-pin refusal exit codes and gate patch points to the shared contract
- Merge pull request #91716 from Nastechresearch/fix/scale-to-zero-no-pointless-quiesce
- chore: map contributor email for salvage of #88470
- refactor(acp): share one OpenAI bridge between the ACP clients
- chore: contributor mappings for #95633/#95652 salvage
- 33 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
