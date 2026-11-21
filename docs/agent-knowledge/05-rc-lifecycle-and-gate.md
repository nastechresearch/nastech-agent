# RC Lifecycle and Gate — Durable Knowledge

Durable operating knowledge for `nastech-agent` contributors and agents doing release-candidate
(rc) cuts, gate triage, or stable-publication work. This is the companion to the `100ways` and
`100wayskills` skills — load both with the `skill` tool before any rc, gate, or release work.
This file records the v0.23.3 rc history and the hard rules for cutting, verifying, and never
prematurely declaring a release successful.

> **Skill-first gate (mandatory).** Scan and load `100ways` and `100wayskills` first. Their
> safety contract binds the work: review-first, no automatic merge/tag/release/deploy. Treat
> integrity, branding, provenance, candidate-test, ZIP-audit, and conformance failures as hard
> stops; a flaky test is a failure until reproduced and stabilized.

## 1. Stable target and rc history (incident record)

- **Stable target:** `v0.23.3`.
- **Attempts rc.1 through rc.6:** all **abandoned**. Do not resurrect, re-point, or reuse any
  of their claim markers, tags, or draft releases as the basis for the stable cut.
- **rc.7 (active):** cut from `main` at **9efde6c474** (the head that includes merged **PR #237**).
  It is the current candidate line; all earlier rc markers are stale.
- **Gate snapshot at time of fix:** gate run **44873305395**, **attempt 3**, was still
  **in progress**. It carried **5 known failures** plus **1 active, OS-specific Windows job**
  whose result had not landed yet. This is a point-in-time observation, not a final verdict —
  it must never be reported as a passing or published release.

Guardrails for this record:

- A gate still in progress with known failures is **not** green. An active Windows-only job
  means the run is incomplete; OS-specific legs cannot be assumed to pass.
- Do not claim the stable release exists until §3 verification is satisfied with fresh
  evidence. "rc.7 was cut" and "gate was dispatched" are process facts, not success facts.

## 2. Cut discipline — abandon and cut commands

Always abandon the stale claim and **cut from a fixed `main` head**. Never reuse a stale rc
claim marker or re-point an old draft to a new commit.

```bash
# 1. Abandon the stale release claim for this version.
python3 scripts/release.py abandon --version 0.23.3 --remote origin

# 2. Cut a fresh claim from the fixed main head (the validated, merged commit).
#    --autopublish marks the intended publication path; the publish itself remains
#    a human/authorized action per the safety contract.
python3 scripts/release.py release --commit <fixed-main> --autopublish --remote origin
```

Rules that must not be broken:

- **`<fixed-main>` must be the verified, fixed `main` commit** — for v0.23.3 that is the
  rc.7 head `9efde6c474` (PR #237). Cutting from an older head silently reverts newer fixes.
- **Never reuse a stale rc claim.** Abandon first; do not edit an abandoned claim's epoch,
  re-tag it, or re-point its draft. A fresh cut mints a fresh claim on the chosen head.
- Never cut from a candidate/review branch to validate — build candidates in isolated
  workspaces; do not edit downstream `main` while validating.
- The release script is a tool, not authority. Running `--autopublish` does not by itself
  grant permission to publish; see §4.

## 3. Verification discipline — evidence, not assumption

Report a stable release as published **only** from API / check-runs / state checks. A green
terminal line, a screenshot, a dispatched gate, or a draft release is not evidence.

Required evidence, all fetched fresh:

1. **Release exists and is truly stable:**
   `gh release view v0.23.3` must resolve. Confirm via API that it is **published**,
   **non-draft** (`draft: false`) and **non-prerelease** (`prerelease: false`).
2. **Builds and assets:** confirm the release shows a **builds table** and **R2-backed
   assets** (artifacts reachable and returning 200), not just a notes body.
3. **Checks:** confirm **check-runs are green** for the published head — every required
   job concluding `success`, including the OS-specific Windows leg that was still active
   in the §1 snapshot.

```bash
# Release exists, and is non-draft / non-prerelease / published.
gh release view v0.23.3 -R nastechresearch/nastech-agent
gh api repos/nastechresearch/nastech-agent/releases/tags/v0.23.3 \
  --jq '{tag_name, draft, prerelease, published_at, assets: [.assets[].name]}'

# Check-runs for the published head (all required conclusions must be success).
gh api "repos/nastechresearch/nastech-agent/commits/<published-sha>/check-runs?per_page=100" \
  --jq '.check_runs[] | {name, status, conclusion}'
```

**Never report success without this evidence.** If any check is pending, failing, missing,
or the release is still draft/prerelease, report the precise state and the exact remaining
human action. Do not infer a pass from a partial run or from a prior attempt's green jobs.

## 4. Policy and safety contract

- **No automatic merge, tag, release, or deploy without appropriate authority.** These are
  human actions. AI may classify, summarize, and propose diagnostics only — it cannot
  authorize a retry, a merge, a tag, a publication, or a deployment.
- Follow the `100wayskills` safety contract in full (see also
  [07-100ways-ci-triage.md](07-100ways-ci-triage.md)): direct-fetch provenance, isolated
  candidates, deterministic path-scoped transforms, hard-stop gates, and review-only handoff
  to the dedicated branch.
- A successful candidate sync, gate, or PR merge does **not** authorize a release. Release is
  a separate human decision: reviewed changes → manual `PREVIEW` on `main` → inspect artifact
  → protected `PUBLISH` only after approval.
- Do not disable tests, checks, gates, or scanners to obtain a green run. Fix the root cause
  or stop for human review.

## 5. No attribution hints — absolute rule

Never introduce source/fork attribution, provenance, or "branded from" wording — in code,
comments, docstrings, commit messages, PR titles/bodies, release notes, generated reports,
summaries, or skill/knowledge files. Professional release notes state exactly what changed
and what was validated, nothing about an upstream or fork relationship. This is a hard
brand-audit requirement, not a style preference; a single hint is a violation.

## 6. Safe status template

```text
Stable target: v0.23.3
Candidate head: 9efde6c474 (PR #237)
RC line: rc.7 (rc.1–rc.6 abandoned)
Gate run: 44873305395 attempt 3 — <IN PROGRESS | PASS | FAIL>
Failures: <N known>; OS-specific jobs: <state of Windows leg>
Release: gh release view v0.23.3 — <exists | missing>; draft=<bool> prerelease=<bool>
Assets: builds table <present | absent>; R2 assets <200 | missing>
Check-runs: <all success | pending/failing — name each>
Classification: <process fact | verified success | blocker>
Remaining action: <exact human action, if any>
Safety boundary: no merge, tag, release, or deployment was performed.
```
