# Release Versioning Contract — Durable Knowledge

Durable operating knowledge for `nastech-agent` contributors and agents touching release
versioning, published-release identity, or their contract tests. This is the companion to the
`100ways` and `100wayskills` skills — load both with the `skill` tool before any rc, gate,
versioning, or release work. This file records the rc.7 Python 6/8 failure, its root cause in a
drifted test mock, the exact fix, the verification evidence, and the guardrails that prevent a
recurrence.

> **Skill-first gate (mandatory).** Scan and load `100ways` and `100wayskills` first. Their
> safety contract binds the work: review-first, no automatic merge/tag/release/deploy. Do not
> weaken a test to make a failing job green — fix the root cause or stop for human review.

## 1. Incident record — rc.7 Python 6/8 failure

- **Line:** rc.7 (the active v0.23.3 candidate line; see
  [05-rc-lifecycle-and-gate.md](05-rc-lifecycle-and-gate.md)).
- **Failing lane:** Python **6/8**.
- **Jobs:** `136797100587` (**attempt 2**) and `136825542115` (**attempt 3**).
- **Symptom:** `tests/scripts/test_release_version_from_ref.py` failed on both attempts. Two
  separate attempts reproducing the same failure ruled out a one-off flake: this was a real
  contract mismatch between the test and the implementation, not noise.
- **Classification:** contract-test/mock drift (a test bug), not a product defect in the
  versioning implementation. The implementation behavior was correct; the mock no longer
  modeled the tool call the implementation actually makes.

## 2. Root cause — the mock drifted from `published_release_identity`

The failing tests exercise `scripts/releases/versioning.py::published_release_identity`.
The implementation's `gh` call contract is:

- It invokes `gh api --paginate repos/{repository}/releases?per_page=100` (the `--paginate` flag
  and `per_page=100` are part of the call, not optional decoration).
- It decodes the result with a `json.JSONDecoder().raw_decode` loop over the raw stdout. There is
  **no `--slurp`** flag and no newline-delimited-JSON (ndjson) post-processing: with `--paginate`,
  each API page is its own JSON array, so the raw stdout is a sequence of concatenated JSON
  documents.
- It keeps only published stable releases — rows with `draft is False` and `prerelease is False`
  and a parseable `vX.Y.Z` tag — and selects the newest one (ranked by semantic version via
  `cmp_to_key(compare)`), then resolves its commit with a separate `gh api ... --jq .sha` call.

The old mock did not match this contract: it keyed the fake `run` on the non-paginate argv shape
and returned ndjson (`--slurp`-style) output. As a result the versioning code received data in a
form it never receives in production, and the assertions failed.

## 3. The fix

Update the mock in `tests/scripts/test_release_version_from_ref.py` so it mirrors the real
implementation:

- **Accept the `--paginate` call:** match on `argv[:3] == ["gh", "api", "--paginate"]` (instead
  of the old non-paginate shape).
- **Return a single JSON document:** `return json.dumps(releases)` — i.e. one JSON array, not
  `--slurp` ndjson / newline-separated records. The `raw_decode` loop handles a single page just
  as it handles many.
- Keep the separate `--jq .sha` branch intact and the existing assertions unchanged: drafts,
  prereleases, and CalVer labels are still filtered out, and the newest published stable release
  still wins.

Representative fixed mock shape:

```python
def run(argv):
    if argv[:3] == ["gh", "api", "--paginate"]:
        return json.dumps(releases)
    assert argv[:2] == ["gh", "api"] and argv[3:] == ["--jq", ".sha"]
    return { ... commits/vX.Y.Z: sha ... }[argv[2]]
```

This is a test-only change. No production behavior in `scripts/releases/versioning.py` was
altered — the implementation was already correct.

## 4. Verification evidence

Recorded after applying the fix:

```bash
PYTHONPATH=. uv run --no-sync pytest -q tests/scripts/test_release_version_from_ref.py
# 34 passed

# Related release tests (broader set): 160 passed
```

- `tests/scripts/test_release_version_from_ref.py` — **34 passed**.
- Related release tests — **160 passed**.

Both Python job failures above were traced to the same mock drift; aligning the mock to the
`--paginate` + plain-JSON contract cleared them on re-run. A green local run is necessary but
not sufficient for release claims — the gate must also be green with fresh evidence (see
[05-rc-lifecycle-and-gate.md](05-rc-lifecycle-and-gate.md) §3).

## 5. Guardrails — do not break this contract again

- **Update contract tests and mocks together.** When changing versioning / release-identity
  behavior, update `scripts/releases/versioning.py` and its contract tests
  (`tests/scripts/test_release_version_from_ref.py`) in the same change. A mock that drifts from
  the real `gh` argv/JSON shape will produce false CI failures that masquerade as flakes.
- **Mock what the implementation actually calls.** `--paginate` plus plain JSON arrays
  (`json.dumps(...)`) is the contract. Do not reintroduce `--slurp`/ndjson mocks or key the fake
  `run` on the old argv shape. If the implementation changes its call, change the mock in lockstep.
- **Never weaken assertions.** Do not relax a failing test to "green" it, skip it, or delete the
  draft/prerelease/newest-wins checks. Reproduce the failure, fix the root cause, and keep the
  behavioral contract intact. A "fix" that destroys what the test secures is rejected.
- **No attribution hints — absolute rule.** Never introduce source/fork attribution,
  provenance, or "branded from" wording in code, comments, tests, docstrings, commit messages,
  PR titles/bodies, release notes, knowledge files, or summaries. State only what changed and
  what was validated. A single hint is a brand-audit violation, not a style preference.

## 6. Cross-references

- [README.md](README.md) — knowledge index and skill-first entry point.
- [05-rc-lifecycle-and-gate.md](05-rc-lifecycle-and-gate.md) — rc history, cut discipline,
  verification discipline, and the no-attribution rule.
- [07-100ways-ci-triage.md](07-100ways-ci-triage.md) — CI triage via `100ways`/`100wayskills`.
- [08-gate-failure-classification.md](08-gate-failure-classification.md) — classifying a gate
  failure as fork bug vs upstream vs infrastructure vs flaky.
