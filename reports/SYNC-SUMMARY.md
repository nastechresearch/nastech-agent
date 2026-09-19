# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 50 commits affecting 2253 files.
- **Source revision:** `8df0a0379378`.
- **Previous source revision:** `03fee43ca344`.

## Technical coverage

- **agent/:** 15 changed files.
- **apps/:** 82 changed files.
- **cli.py/:** 2 changed files.
- **contributors/:** 5 changed files.
- **gateway/:** 30 changed files.
- **nastech_cli/:** 8 changed files.
- **nastech_state.py/:** 1 changed files.
- **nastech_state_profile_repair.py/:** 1 changed files.
- **plugins/:** 5 changed files.
- **scripts/:** 2 changed files.
- **tests/:** 38 changed files.
- **tui_gateway/:** 6 changed files.
- **website/:** 20 changed files.

## Delivered improvements

### New capabilities

- feat(sessions): `nastech sessions repair-profiles` settles crossed-profile durable state
- feat(gateway): route inbound messages to profiles by sender user_id
- feat(gateway): RoutingIdentity — one frozen identity per inbound event

### Reliability and fixes

- fix(gateway): voice input re-routes per speaker through the identity seam
- fix(gateway): canonicalize identity first at every adapter ingress path
- fix(tui_gateway): probe foreign rows by keyset and re-hydrate after a remote compaction
- fix(tui_gateway): next prompt sees turns another surface appended to the session (#42962)
- fix(desktop): create a project from a folder in one step
- fix(agent): judge "wrong script" against the user's own message; one continuation kind per stop
- fix(agent): re-prompt once when a turn that did tool work ends on a collapsed fragment
- fix(shared): a failed gateway dial says which failure it hit
- fix(tui_gateway): the turn-completion trim waits for the other sessions too
- fix(tui_gateway): the periodic memory trim waits until no session is busy or attached
- fix(desktop): profile-only secondaries count their live turn too
- fix(desktop): wake probe counts the foreground turn as in-flight work; sibling pins and prune follow-through
- 14 additional reliability and fixes updates are included in this verified snapshot.

### Documentation

- docs(agent): the finish explainer's terminal set is a sibling heuristic, not the same one
- docs(model_switch): say what the fallback actually relies on

### Improvements

- test(gateway): identity-canonical ingress invariants (#88715 rows A/B) + docs
- refactor(gateway): fold the runner's duplicated identity stamps into one seam
- Revert "feat(catalog): restore website install links to Desktop"
- Revert "docs(catalog): restore native browsing and install guidance"
- Revert "feat(ui): support icon-only segmented controls"
- Revert "feat(desktop): restore native skill and plugin catalogs"
- Revert "feat(desktop): browse catalogs as cards with a saved list option"
- refactor(desktop): folder-derived project name lives in the input only
- test(desktop): cover folder-derived project creation
- chore: map Anton Vykhovanets to @vykhovanets for #68621 salvage
- test(agent): degenerate-final recovery — a collapsed fragment after tool work is re-prompted, not accepted
- chore(contributors): map dankkush (PR #111472 salvage)
- 7 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
