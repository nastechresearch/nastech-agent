# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 96 commits affecting 1335 files.
- **Source revision:** `4c1f53be10d0`.
- **Previous source revision:** `057dcdf236f8`.

## Technical coverage

- **agent/:** 25 changed files.
- **apps/:** 149 changed files.
- **cli-config.yaml.example/:** 1 changed files.
- **cli.py/:** 1 changed files.
- **contributors/:** 5 changed files.
- **cron/:** 2 changed files.
- **gateway/:** 9 changed files.
- **nastech_cli/:** 20 changed files.
- **nastech_constants.py/:** 2 changed files.
- **plugins/:** 10 changed files.
- **run_agent.py/:** 3 changed files.
- **tests/:** 61 changed files.
- **tools/:** 28 changed files.
- **tui_gateway/:** 7 changed files.
- **ui-tui/:** 2 changed files.
- **web/:** 1 changed files.
- **website/:** 27 changed files.

## Delivered improvements

### New capabilities

- feat(gateway): warn when a Docker sandbox MEDIA path fails translation
- feat(browser): make snapshot threshold configurable
- feat: browser snapshots drop LLM summarization — truncate-and-store like web_extract; auxiliary.web_extract slot removed
- feat(terminal): pluggable terminal environment backends via plugin registry
- feat(desktop): add Settings toggle for vibe hearts
- feat(tui-gateway): seq-stamped event replay for lossless desktop reconnect
- feat(desktop): let the in-app browser hold more than one tab
- feat(desktop): make Cmd/Ctrl+L focus the composer from anywhere

### Reliability and fixes

- fix(approval): machine-readable outcome parity on the gateway tails + sudo human-wait exclusion (#85125 2e)
- fix(gateway): widen computer-use media path repair to sibling surfaces
- fix(curator): tell the background reviewer to read before it writes
- fix(background-review): teach review prompts the enforced read-before-write handshake
- fix: follow-up for salvaged PR #93985 — cache key, snapshot, dead code
- fix(memory): keep OpenViking identity operations consistent
- fix(memory): scope OpenViking user cache to connection
- fix(memory): emit explicit-uid OpenViking URIs resolved from system status
- fix(memory): migrate OpenViking URIs to the viking://~ home alias
- fix(skills): preserve review marks across contexts
- fix(gateway): resolve session-scoped Docker sandboxes for MEDIA delivery (#93950)
- fix(fallback): surface provider transitions and primary recovery
- 39 additional reliability and fixes updates are included in this verified snapshot.

### Documentation

- docs(gemini): update to use latest gemini models
- docs: note httpcore pin dependency in _enable_happy_eyeballs
- docs: add operator remediation for install dirs locked to 0700 by older images
- docs: update secure_parent_dir docstring and caller comments for the install-tree exclusion

### Improvements

- Merge pull request #94568 from kshitijk4poor/fix/85125-2e-approval-outcome-parity-v2
- Merge pull request #94536 from kshitijk4poor/salvage/94439-computer-use-media-path
- refactor(gateway): retire private repair alias per replay_cleanup precedent
- chore: map contributor email for salvage attribution
- refactor(gateway): unify computer-use repair call sites after review
- chore: map contributor email for salvage attribution
- test(curator): assert the instruction through the delivered prompt, not the source
- test(gateway): accept session_key kwarg in media resend dedup stubs
- test(telegram): cover send() waiting for reconnect after a network blip
- test(teams): cover connect when the namespace exists but App is unbound
- test(desktop): stop the syntax-diff mock factory from leaking unhandled rejections (#94415)
- test: opted-out profile seeding now exercises the essential-only sync subprocess
- 21 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
