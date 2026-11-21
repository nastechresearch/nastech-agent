# 100Ways CI / Release / Fork-Sync Triage — Durable Knowledge

Scope: permanent operating knowledge for `nastech-agent` contributors and agents doing CI,
release, or fork-sync work. Source of truth is the two installed skills — load them with the
`skill` tool before acting:

- `100ways` — manages `nastechresearch/100Ways` CI/CD, the NasTech→Hermes fork-sync pipeline,
  and the brand-audit system.
- `100wayskills` — the canonical package for the NasTech-agent profile: candidate gates,
  strict brand audit, reconciliation playbook, incident response, review-only handoff,
  and manual release.

> **Skill-first gate (mandatory).** Before any CI triage, release preparation/cut, or
> fork-sync work, scan and load `100ways` and `100wayskills`. Their safety contract binds
> the work: review-first, no automatic merge/tag/release/deploy. Do not diagnose from a
> red status or screenshot alone.

## 1. Awareness: when these skills apply

Use them when:

- Main CI on `nastechresearch/100Ways` is broken (cascade repair, trigger logic, forkcheck).
- A brand audit (hermes/nous reference scan) is failing.
- Fork-sync pipeline gates are failing, or a branded candidate must be validated/handed off.
- Preparing a release (manual `PREVIEW` → protected `PUBLISH`) for nastech-agent.
- Triaging an rc/release-candidate gate failure on `nastechresearch/nastech-agent`.

If `100wayskills` is published, install it from `nastechresearch/100wayskills` before
diagnosing (the `100ways` skill gives the exact clone/copy/test recipe). Its
`references/incident-response.md` decision tree is authoritative for "fork bug vs upstream
bug" and "patch the candidate, the test, or the workflow".

## 2. NasTech-agent profile (from `100wayskills/references/nastech-agent-profile.md`)

| Role | Value |
|---|---|
| Automation | `nastechresearch/100Ways` |
| Downstream | `nastechresearch/nastech-agent` |
| Direct upstream | `NousResearch/hermes-agent` |
| Review branch | `100WAYS` (dedicated, review-only) |
| Protected downstream base | `main` |
| Candidate release policy | **Review only; no automatic merge, tag, release, or deployment** |
| Candidate test entry point | `scripts/run_tests.sh` in the built candidate |
| Local transformation tests | `PYTHONPATH=<100Ways-root> python3 -m pytest -q` |

### Strict brand exception profile

The candidate must contain **no upstream-brand references** except these exact allowances
(scan path names, text, generated reports, manifests, summaries, and final ZIP entries):

| Allowed reference | Allowed location | Notes |
|---|---|---|
| `hermes-parser`, `hermes-estree` | root `package-lock.json` | dependency-only |
| `@nous-research/image-size` | `website/package-lock.json`, `website/.npmrc` | dependency-only |
| `Powered by NousResearch` | `reports/SYNC-SUMMARY.md` | exact phrase only |
| Contributor names | `contributors/names/` | identity metadata only |

Contributor **email** paths and contents are NOT exempt. Preserve case-colliding email
records exactly once through collision-safe path mapping; never drop records due to
case-insensitive filesystem collisions. `contributors/emails/*` are immutable credit records:
do NOT rename, flag in brand audits, or subject to case-collision checks.

Identity requirements: CLI banner renders `NASTECH AGENT` + approved `𓄃` symbol; no inherited
ASCII/block art or skin-provided upstream identity; owned assets listed in
`config/owned-assets/manifest.json`; generated reports regenerated (never reuse stale
`reports/` from a prior review branch).

### Non-negotiable safety contract (summary)

1. Fetch upstream directly; record exact SHA. No cached source as proof of freshness.
2. Build candidates in isolated workspaces; never edit downstream `main` to validate.
3. Deterministic, path-scoped transformations only — no broad destructive replacement.
4. Run targeted tests, full transformation suite, and affected candidate tests before pushing.
5. Integrity/branding/security/provenance/candidate-test/ZIP/conformance failures are hard stops.
6. **A flaky test is a failure until reproduced and stabilized; do not retry merely for green CI.**
7. AI may classify/summarize/propose diagnostics only — it cannot alter files, authorize a
   retry, or authorize publication.
8. Update only the configured review branch after every gate passes.
9. **Never merge a PR, tag, release, or deploy automatically. These are human actions.**
10. No secrets, tokens, private chat IDs, or credentials in skill files, reports, logs,
    commit messages, or release notes.

## 3. RC gate-failure triage

### 3.1 Evidence first

Fetch the run and jobs before forming a hypothesis. Capture: repository, run URL/ID, job and
step names, branch, workflow revision, timestamps, source SHA, candidate digest, review-branch
SHA, first non-zero command, exact assertion/traceback, gate JSON, and whether a retry already
occurred. Never act on an incomplete error screenshot.

### 3.2 Classify every failure

Classify with evidence into one of these classes, then act accordingly:

| Class | Evidence | Action |
|---|---|---|
| **Deterministic / transformation-induced mismatch** | Upstream passes; candidate differs after a deterministic rename/rewrite (e.g. fixed-width credential display where a branded token grew). | Narrow reconciliation per `reconciliation-playbook.md`; add focused regression test; do not change production semantics or expose longer secrets. |
| **Product / candidate regression** | Candidate behavior is wrong independently of test wording. | Repair source transformation or candidate code narrowly; add regression test. |
| **Flaky test** | Fails once, passes retry, or depends on order/time/state. | Treat as **blocking**; stabilize test/environment. Re-run a *proven* flake **once**, with recorded evidence, and only if the policy supports it — never to manufacture green CI. |
| **Environmental / dependency-runtime mismatch** | Lockfile, Node/Python/npm/uv versions, or runner state differ. | Match declared engines and locked environment first; fix isolation. |
| **Workflow / artifact defect** | CI-only file layout, permissions, artifact, or path issue (e.g. branded zip ships without `.git/`, breaking `git check-ignore` rc=128). | Validate with local artifact simulation; narrow workflow repair (e.g. `git init` in extraction). |
| **Human-only gate** | Required label, approval, or security-sensitive workflow review. | Explain the exact human action; do not self-approve or add `ci-reviewed` labels automatically. |

Root-cause decision tree (`references/incident-response.md`):

```text
Does the exact upstream test pass?
├─ No → upstream issue or environmental mismatch; record and decide under policy.
└─ Yes
   Does the transformed candidate reproduce the failure?
   ├─ No → CI state/order/environment issue; stabilize test isolation.
   └─ Yes
      Is the transformed production behavior incorrect?
      ├─ Yes → repair transform/candidate production behavior narrowly.
      └─ No → repair only the transformed expectation / semantic artifact.
```

### 3.3 Rules that must not be broken

- **Fix root causes; never weaken tests, checks, gates, or semantics without evidence.**
  Do not disable a check, loosen an assertion, or silence a scanner to obtain green CI.
  Fix the candidate transform, add a narrowly approved exception, or stop for human review.
- Reproduce in a local isolated candidate at the same upstream SHA before changing code.
- After a repair: focused regression test → full 100Ways suite → fresh candidate from direct
  source → exact formerly failing candidate test → candidate gate + strict brand audit →
  ZIP audit where packaging applies → protected CI rerun → review-only handoff verification.
- If a defect is upstream-caused (fresh upstream commits, 100Ways `main` static), do **not**
  open a fix branch on the fork — it will conflict with the next weekly sync. Wait for sync
  or update the rebranding logic instead.
- `gh run view <job> --log` may return empty for forkcheck slices; use the jobs-logs API below.

## 4. Useful commands

```bash
# Human-readable run overview (nastech-agent runs)
gh run view <run> -R nastechresearch/nastech-agent

# Enumerate jobs for a specific attempt, paged
gh api "repos/nastechresearch/nastech-agent/actions/runs/<run>/attempts/<n>/jobs?per_page=100&page=<p>"

# Fetch a job's full log (bare API path returns the complete log)
gh api "repos/nastechresearch/nastech-agent/actions/jobs/<job-id>/logs"

# 100Ways equivalents
gh run list --repo nastechresearch/100Ways --branch main
gh api "repos/nastechresearch/100Ways/actions/jobs/<job-id>/logs"
gh pr list --repo nastechresearch/100Ways --state all --limit 20 \
  --json number,title,state,headRefName,createdAt,mergedAt,closedAt
```

**API 502 / transient errors:** retry; if large paginated job lists keep failing, use the
`per_page=50` paging workaround and walk pages, instead of assuming zero jobs. Do not treat a
502 as a product failure or as evidence for weakening a gate.

**Forkcheck slices:** the failing test runs against the extracted branded candidate zip, not
`origin/main`. Download artifact `nastech-agent-update`, extract `nastech-agent/tests/...`,
and find the `FAILED tests/...::test_name` source there. The candidate tree's `.gitignore`
and source are what get tested.

## 5. No attribution hints — absolute rule

Never introduce source/fork attribution, provenance, or "branded from" wording — in code,
comments, docstrings, commit messages, PR titles/bodies, release notes, generated reports,
summaries, or skill/knowledge files. Professional release notes state exactly what changed
and what was validated, nothing about the upstream brand or the fork relationship. This is a
hard brand-audit requirement, not a style preference; a single hint is a violation.

## 6. Review handoff & release boundaries

Review-only handoff (dedicated branch `100WAYS`, PR base `main`, PR state `OPEN`):

- Source CI conclusion `success`; candidate tests / conformance / ZIP audit / post-test receipt all PASS.
- Head equals the dedicated review branch; base is protected `main`.
- **No action merged the PR, created a tag, published a release, or deployed a service.**
- Downstream checks and any human-only labels reported precisely.
- CI-sensitive changes (workflows, composite actions, release actions, permissions, runners,
  artifact paths, arbitrary execution) require a human reviewer with the four questions in
  `references/ci-and-review-handoff.md`.

Release is a separate human decision: merge reviewed note/workflow changes → manual `PREVIEW`
on `main` → inspect artifact → protected `PUBLISH` only after approval. A successful candidate
sync or merge does **not** authorize a release. For GitHub Pages docs staged at `_site/docs`,
use `url: 'https://nastechresearch.github.io'` and `baseUrl: '/nastech-agent/docs/'`.

## 7. Safe status template

```text
Source: <upstream SHA>
Candidate: <candidate digest>
CI: PASS / FAIL — <run URL>
Review PR: <URL>, <branch> → <base>
Brand audit: <allowed counts>, <zero or N violations>
Classification: <deterministic | flaky | product blocker | environmental | human-only>
Remaining action: <human review/check>
Safety boundary: no merge, tag, release, or deployment was performed.
```
