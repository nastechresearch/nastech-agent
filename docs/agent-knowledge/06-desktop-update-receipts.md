# Desktop / CLI Update Completion Is Receipt-Driven — Durable Knowledge

Scope: permanent operating knowledge for `nastech-agent` contributors and agents debugging
desktop or CLI update handoffs, especially the source E2E path that clicks the real
Settings → About → "Update now". Source of truth is the code in this checkout; the relevant
entry points are:

- `tests/install/e2e-assets/launch-from-spec.mjs` — the source desktop update driver.
- `tests/install/e2e-assets/source-update-observer.mjs` — `observeSourceUpdate()`, the
  completion predicate.
- `nastech_cli/update_receipt.py`, `update_handoff.py`, `update_lock.py`, `update_stage.py`
  — the product side that writes receipts and the in-progress marker.

> **Skill-first gate (mandatory).** Before diagnosing any update failure, scan and load the
> matching skill — `systematic-debugging` for evidence-first root-cause work, and `100ways`
> / `100wayskills` when the failure is on a CI gate or rc/release-candidate cut. Fix root
> causes; never weaken an assertion, gate, or semantic to get a green result. Do not diagnose
> from a red status or screenshot alone.

## 1. What actually constitutes completion

`launch-from-spec.mjs` does **not** treat a reset checkout as a successful update. Its own
header states the contract (lines 19–24): click Update now, then require a new successful
handoff result **or** source-update receipt, the expected checkout, and marker removal.
`source-update-observer.mjs` opens with the same rule: *"A checkout reset is the start of
preparation, not its completion."*

`observeSourceUpdate({ home, resultPath, expectSha })` snapshots the candidate files before
the click and, on each poll, requires **all** of the following:

1. **A new success result file or receipt** — content must differ from the pre-click snapshot
   (a stale file is ignored, and the relaunched app may unlink the result file as soon as it
   boots, so reads tolerate `ENOENT`):
   - `--result` file (`.nastech-update-result.json`): `ok === true` **and**
     `exit_code == null || exit_code === 0`, otherwise it throws `update handoff failed`.
   - a receipt in `<home>/logs/update_receipts/update_*.json` with `finished_at`:
     `outcome === 'success'` (otherwise it throws `source update failed`) **and**, when
     `expectSha` is set, `post_update.sha === expectSha`.
2. **Expected HEAD** — when `--expect-sha` is set, the driver's `headSha()` (real git via
   `NASTECH_E2E_REAL_GIT`, read at the gate, not a bare `git` on PATH) must equal `expectSha`.
   A receipt's `post_update.sha` alone does not cover the live checkout; both are checked.
3. **No in-progress marker** — `<home>/.nastech-update-in-progress` must not exist.

A checkout reset by itself satisfies none of this. No driver-assisted relaunch, force-kill,
or rebuild may turn an unfinished update into a passing one; the Playwright close event is
unreliable across the handoff, so neither Playwright events nor a driver-forced action count
as product completion signals. Receipts are written to the **ROOT** home's
`logs/update_receipts/` (`get_default_nastech_root()`), never a sticky profile's home.

## 2. Mode A failure signature — do not weaken the assertion

**Signature:** after clicking Update now and polling to `--timeout-ms` (default 900000 ms /
15 min), the driver throws:

```
Error: no successful update completion receipt; leaving the install untouched
```

This is the terminal `throw` in the poll loop of `launch-from-spec.mjs` (line 274). It means
the product never produced a *new* ok=true result or a successful receipt with the expected
SHA, the HEAD never reached `expectSha`, or the in-progress marker was never removed — before
the deadline.

**Recorded observation (rc.7):** the `desktop-update-handoff.log` showed the takeover handoff
begin and then go silent; no success receipt followed. Orphan processes were killed at
timeout by the harness, not by a product completion. Treat this as a real product/handoff
failure to root-cause — **do not relax `observeSourceUpdate`, extend the poll into a pass,
force a relaunch, force-kill to manufacture a clean close, or otherwise weaken the assertion
to make the lane green.** The driver deliberately closes with *"update completed without
driver-assisted recovery"* and refuses to force-close a window that will not close
(`"app did not close after completion; no force-kill attempted"`).

Per `nastech_cli/AGENTS.md`, the update pipeline is transactional
(`plan → snapshot → apply → restart-per-kind → verify → report`); `update_handoff.py` and
`update_serve_obligations.py` are a **frozen compat surface** (`tests/compat/old_updater_surface.json`)
because removing a name bricks releases mid-update. The failure is in that handoff chain or
its environment — not in the observer's strictness.

## 3. Diagnosis — what to inspect, in order

Follow systematic-debugging Phase 1: read the exact error, gather evidence at every component
boundary, then form ranked hypotheses. Evidence sources for an update failure:

| Source | Where | What it proves |
|---|---|---|
| `desktop-update-handoff.log` | `<NASTECH_HOME>/logs/desktop-update-handoff.log` | Staged handoff progress; the terminal `rc=0` / "completed at command boundary" record; where silence begins (takeover, child stage, rebuild). UTF-8 BOM — read with `encoding='utf-8-sig'`. |
| `update_receipts/` | ROOT `<home>/logs/update_receipts/update_*.json` | Whether a receipt was finalized: `outcome`, `finished_at`, `post_update.sha`, skip reasons. Keep the last 20. |
| `.nastech-update-result.json` | `<NASTECH_HOME>/` (the `--result` path) | Handoff result from the relaunched app: `ok`, `exit_code`. Consumed/unlinked on boot. |
| `.nastech-update-in-progress` | ROOT `<home>/` | Live claim marker. Its continued presence blocks completion; check for live vs dead/stale claims before clearing anything. |
| Agent / desktop `errors` logs | `<NASTECH_HOME>/logs/` (agent + desktop error logs) | Product-side exceptions during apply/restart/verify that stopped before a receipt was written. |
| Job artifacts | CI run artifacts (handoff log copies, screenshots, `manual-update.json`, OLD/NEW chat output) | The exact run's captured state at timeout, including `${spec}.timeout.png` and window dumps. |

Notes that prevent misdiagnosis:

- The driver writes `manual-update.json` and exits 42 when the UI reports a manual-update
  path — that is an intentional branch, not the Mode A signature.
- A `git rev-parse HEAD` that returns `''` (e.g. a fresh-machine leg with git off PATH) is a
  driver-environment fault, not a product receipt failure; the driver uses
  `NASTECH_E2E_REAL_GIT` for this reason.
- The observer changes only when a file's content actually changes; a pre-existing successful
  receipt from an earlier run is not completion for this click.

## 4. No attribution hints — absolute rule

Never introduce source/fork attribution, provenance, or "branded from" wording — in code,
comments, docstrings, commit messages, PR titles/bodies, release notes, generated reports,
summaries, or skill/knowledge files. State exactly what changed and what was validated,
nothing about an upstream brand or fork relationship. This is a hard brand-audit requirement,
not a style preference; a single hint is a violation. (Mirrors `07-100ways-ci-triage.md` §5.)

## 5. Safe triage summary template

```text
Surface: desktop (source) / CLI update
Result file: present|absent, ok=?, exit_code=? (new vs stale)
Receipt: outcome=?, finished_at=?, post_update.sha=? vs expectSha=?
HEAD: <sha> vs expectSha <sha>
Marker: .nastech-update-in-progress present|absent
Handoff log last stage: <stage>; silence after: <stage>
Classification: product/handoff defect | env (git/PATH) | manual-update(42) | flaky
Safety boundary: no assertion weakened, no forced relaunch/kill, install left untouched.
```
