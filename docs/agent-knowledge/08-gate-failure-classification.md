# Release Gate Failure Classification — Durable Knowledge

Scope: permanent operating knowledge for `nastech-agent` contributors and agents triaging a red
rc/release gate. This file tells you **how to classify a failure and which repair is permitted**.
It is a companion to the skills, not a substitute.

> **Skill-first gate (mandatory).** Before triaging any rc/gate/release failure, scan and load the
> `100ways` and `100wayskills` skills, then read `07-100ways-ci-triage.md` and the per-symptom
> files (`01`–`06`) as needed. The safety contract binds the work: review-first, no automatic
> merge/tag/release/deploy. Classify from evidence — never from a red status or a screenshot.

## 1. Evidence first — required for every classification

No failure is classified, and no repair is proposed, until all five evidence items are recorded.
A missing item means "insufficient evidence," not "pick the most likely class."

| # | Evidence | What to capture |
|---|---|---|
| 1 | **Job ID** | Repository, workflow run URL + run ID, job ID, attempt number, job/step names, branch, workflow revision, timestamps. |
| 2 | **Log excerpt** | First non-zero command, exact assertion/traceback, gate JSON, and the retry result if one already happened. Not a paraphrase. |
| 3 | **Artifact** | Run artifact name and path (e.g. `nastech-agent-update`), extracted candidate/fork check slice, or generated gate report that contains the failure. |
| 4 | **Reproduction / validation command** | The exact command that goes red on the symptom and green when fixed, run at the same source SHA in an isolated environment. Use `scripts/run_tests.sh` for `tests/`; never bare `pytest`. |
| 5 | **Fix rationale** | Why the chosen repair addresses the root cause and why it does not weaken a test, gate, completion semantic, or security check. |

Supporting identity to record when relevant: source SHA, candidate digest, review-branch SHA, and
the baseline SHA. See `100wayskills/references/incident-response.md` for the full evidence
checklist and reproduction protocol.

### No attribution hints — absolute rule

Never introduce source/fork attribution, provenance, or "branded from" wording in a triage record,
fix rationale, commit message, PR body, release note, report, or knowledge file. State exactly
what failed, what was validated, and what changed. This is a hard brand-audit requirement, not a
style preference; a single hint is a violation. (Same rule as `07-100ways-ci-triage.md` §5.)

## 2. Classification rubric

Assign exactly one primary class. If a gate is red but no failing test/step in it is genuinely
broken, it is a **cascade** — do not fix the gate, find the upstream cause.

| Class | Signature (what the evidence shows) | Permitted action |
|---|---|---|
| **Deterministic test / contract drift** | Same head, same inputs, always fails; a test/mock/fixture expectation no longer matches the current contract or a deterministic transform. Reproducible on demand. | Fix the code or the test that is actually wrong, narrowly. Add a focused regression test. Do not loosen the assertion to hide a real behavior change. |
| **Harness contention / flake** | Fails once, passes on an unmodified re-run; depends on timing, shared lock, or concurrent state. Pass-on-retry is the tell. | Treat as **blocking**. Harden the harness with evidence (correct probe, quiescence at every mutation boundary, cleanup). Do not paper over with a blind sleep or a retry-to-green. |
| **Product / runtime hang or missing receipt** | The product never reaches completion: a required handoff lock/release never happens, or a completion/metadata receipt is never emitted; the harness times out waiting on it. | Fix the product. Add diagnostics at each component boundary to locate where it stalls. **Never weaken completion semantics** (do not treat "no receipt" as success, skip the wait, or fabricate the receipt). |
| **Timeout budget** | A step does real work but is killed at its wall-clock cap (e.g. SIGKILL at the job limit) with no product defect or stuck state proven. | Raise the budget **only with evidence** (measured duration distribution) and **only within the job cap**. Pair with a harness/progress diagnostic. A larger sleep is not a fix for contention or a hang. |
| **Cascade gate failure** | Gate reports failures but its constituent jobs/tests are individually green at the same SHA, or it fails only because an upstream dependency failed. | Treat as a **symptom**. Do not edit the failing gate. Identify and classify the real upstream cause, then re-run the gate. |

Decision order when classes overlap:

```text
Is the failing gate merely reporting another job's failure?
├─ Yes → Cascade. Classify the real cause; leave the gate alone.
└─ No
   Does it reproduce deterministically with a contract mismatch?
   ├─ Yes → Deterministic drift. Fix code or test, narrowly.
   └─ No
      Did it pass on an unmodified re-run / depend on shared state?
      ├─ Yes → Harness contention. Harden with a correct probe + cleanup; blocking until fixed.
      └─ No
         Did the product fail to reach completion or emit its receipt?
         ├─ Yes → Product/runtime blocker. Fix product + add diagnostics; keep completion strict.
         └─ No
            Was healthy work killed at the wall-clock cap?
            └─ Yes → Timeout budget. Raise only with measured evidence, within the job cap.
```

## 3. Rules that must not be broken

- **Fix root causes; never weaken checks.** Do not disable a test, loosen an assertion, silence a
  scanner, skip a completion wait, or fabricate a receipt to obtain green CI. Fix the cause, add a
  narrowly scoped exception only where the profile explicitly allows it, or stop for human review.
- **A flaky test is a failure until reproduced and stabilized.** Re-run a *proven* flake once, with
  recorded evidence, only where policy supports it — never to manufacture green CI. Preserve the
  `⚠ FLAKY` policy: pass-on-retry is green but flagged, and still a bug to fix.
- **Harden quiescence, don't widen the wait blindly.** A lock race needs a correct, properly
  anchored probe at every mutation boundary, not a longer sleep. See `03-macos-e2e-quiescence.md`.
- **Completion semantics are strict.** If a receipt/handoff is missing, the run is not complete.
  Diagnose where the stall is; do not redefine "done" to make the gate pass.
- **Timeout increases need evidence and a ceiling.** Measure first; raise only within the job cap,
  and add a progress diagnostic so the next stall is classifiable without guessing.
- **Reproduce at the same source SHA in an isolated candidate before changing code.** After a
  repair: focused regression test → full suite → fresh candidate → exact formerly failing test →
  candidate gate + strict brand audit → ZIP audit where packaging applies → protected CI rerun →
  review-only handoff verification.
- **AI may classify, summarize, and propose diagnostics only** — it cannot alter files, authorize
  a retry, or authorize publication. Never merge, tag, release, or deploy automatically.

## 4. Worked examples — rc.7 gate

These are the rc.7 failures mapped to the rubric. Use them as calibration, not as a substitute for
fresh evidence on a new run.

| Failure | Class | Why / permitted repair |
|---|---|---|
| **Python 6/8 mock drift** | **Deterministic** | Six of eight Python tests failed with the same head and inputs, every time, on a stale mock/fixture contract. Reproducible on demand → correct the mocks/expectations to the current contract, add regression coverage. Not a flake, not a product hang. |
| **macOS quiescence contention** | **Harness contention** | Same head passed on an unmodified re-run (HEAD→NEXT update legs); a stale update marker or held checkout lock raced the ref advance/update/desktop launch. Harden with a correctly anchored `wait_for_update_quiescence` at each mutation boundary. See `03-macos-e2e-quiescence.md`. |
| **Windows open-app-update churn** | **Harness contention** | Repeated run-to-run variance around the open-app update path — leftover state/processes between legs. Fix with deterministic harness cleanup/isolation between legs, not a retry or a blanket sleep. |
| **Mode A takeover receipt hang** | **Product/runtime blocker** | The mode-A takeover stalled before emitting its completion/metadata receipt; the harness timed out waiting on a receipt that never came. Add boundary diagnostics to find where the handoff stalls and fix the product. Never skip the wait or synthesize the receipt. See `01-pm-takeover-hang.md`. |
| **crash_cells SIGKILL at 3600s** | **Timeout budget / harness** | Work was still running when the job hit its 3600s wall-clock cap and was SIGKILLed, with no product stall proven. Measure the duration first; raise the budget only with evidence and within the job cap, and add progress logging. Do not mislabel as a product hang or a flake. |
| **Source matrix gate** | **Cascade** | The source-matrix gate was red while its constituent sources/jobs were individually green at the same SHA — it was reporting failures from an upstream dependency. Do not edit the matrix gate; classify and fix the real failing source, then re-run the gate. |

## 5. Safe triage record template

Copy, fill, and attach to the gate/review record. Keep it free of attribution wording.

```text
Gate / job:            <job ID, run URL, attempt, step>
Source SHA:            <sha>   Candidate digest: <digest>
Class:                 <deterministic | harness | product blocker | timeout budget | cascade>

Evidence:
  Log excerpt:         <first non-zero command + exact assertion/traceback/gate JSON>
  Artifact:            <artifact name + path/slice containing the failure>
  Repro command:       <exact command; same SHA; isolated env>
  Retry result:        <pass-on-retry? attempt IDs — evidence for harness class>
  Measured duration:   <only for timeout-budget class>

Root cause (plain language): <what actually failed, distinct from unrelated concerns>

Fix rationale:
  Change:              <narrowest repair>
  Why it fixes cause:  <mechanism>
  Not weakened:        <test/gate/completion semantic/security check preserved — how>

Validation:
  [ ] Focused regression test
  [ ] Full suite / fresh candidate / exact formerly failing test
  [ ] Candidate gate + strict brand audit (+ ZIP audit where packaging applies)
  [ ] Protected CI rerun + review-only handoff verification

Safety boundary: no merge, tag, release, or deployment was performed.
```
