# Release Gate & CI Knowledge Index

Durable operating knowledge for contributors and agents doing CI triage, rc/gate, release,
and fork-sync work on `nastech-agent`. Before any rc, gate, or release work, scan and load the
`100ways` and `100wayskills` skills, then read the relevant file(s) below. These notes are a
companion to the skills, not a substitute for them.

## Files

- [01-pm-takeover-hang.md](01-pm-takeover-hang.md) — Diagnosing the rc.7 PM/historical-updater takeover hang: no successful update-completion receipt.
- [02-windows-e2e-harness.md](02-windows-e2e-harness.md) — Windows install/update E2E harness: quirks and required fixes for reliable CI runs.
- [03-macos-e2e-quiescence.md](03-macos-e2e-quiescence.md) — macOS installer-script E2E HEAD→NEXT lock/quiescence contention flake: symptom, root cause, and ported fix.
- [04-release-versioning-contract.md](04-release-versioning-contract.md) — The release versioning contract: how versions, CalVer dates, and tags are formed and validated.
- [05-rc-lifecycle-and-gate.md](05-rc-lifecycle-and-gate.md) — RC lifecycle and gate rules: claim markers, epoch/tagger checks, draft release bodies, and dispatch discipline.
- [06-desktop-update-receipts.md](06-desktop-update-receipts.md) — Desktop/CLI update completion is receipt-driven: how the E2E observer and product code write and verify receipts.
- [07-100ways-ci-triage.md](07-100ways-ci-triage.md) — 100Ways CI, brand-audit, fork-sync, and release triage via the `100ways`/`100wayskills` skills.
- [08-gate-failure-classification.md](08-gate-failure-classification.md) — Classifying gate failures (fork bug vs upstream vs infrastructure vs flaky) and choosing the narrowest repair.
- [09-v0.23.3-verification-checklist.md](09-v0.23.3-verification-checklist.md) — Verification checklist for the v0.23.3 stable release: API, check-runs, R2 assets, and receipt tags.
