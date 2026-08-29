# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 73 commits affecting 1406 files.
- **Source revision:** `360761c8cf50`.
- **Previous source revision:** `1d8946b40b93`.

## Technical coverage

- **.env.example/:** 3 changed files.
- **acp_adapter/:** 1 changed files.
- **agent/:** 25 changed files.
- **apps/:** 14 changed files.
- **cli-config.yaml.example/:** 2 changed files.
- **cli.py/:** 1 changed files.
- **contributors/:** 6 changed files.
- **gateway/:** 18 changed files.
- **locales/:** 34 changed files.
- **nastech_cli/:** 23 changed files.
- **optional-skills/:** 7 changed files.
- **plugins/:** 14 changed files.
- **providers/:** 2 changed files.
- **skills/:** 3 changed files.
- **tests/:** 58 changed files.
- **tools/:** 3 changed files.
- **tui_gateway/:** 1 changed files.
- **ui-tui/:** 5 changed files.
- **website/:** 66 changed files.

## Delivered improvements

### New capabilities

- feat:add hy4-preview model and tokenplan provider
- feat(providers): add Nebius Token Factory provider
- feat(providers): send Nastech-agent User-Agent on Router requests
- feat(providers): add Ramp Router (router.com) provider plugin
- feat: /btw now answers side questions with conversation context; /background renamed to /bg
- feat(todo): nested subtasks via optional parent field
- feat(system_prompt): two-line conversation clock — anchored start + rebuild-day line (salvages #96224) (#97930)
- feat(prompt): default identity rewritten as a behavior spec — sizing rule, named prohibitions, anti-sycophancy, earned depth; exploration-thrift line deliberately removed (models under-explore) (#97926)
- feat(optional-skills): add decision-questionnaire — turn a blocked decision into an async questionnaire
- feat(optional-skills): add setup-wizard-generator — bash wizard for human-only setup steps
- feat(skills): rename grill-me to plan-interrogation, fold in frontier-rounds interview mechanic
- feat(desktop): Download button on preview file cards — save any delivered file via the authenticated backend bridge (works local and remote) (#97816)
- 1 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix: drop duplicate hy4-preview context entry — main's 1_048_576 wins
- fix:update test info
- fix(nebius): route effort through canonical clamp_effort — hand-rolled map inverted the ladder
- fix(nebius): request verbose model metadata
- fix(router): pytest guard on caps warmer + debug log in fail-open efforts lookup
- fix: re-derive the live busy text mode after a non-profile /busy change
- fix(gateway): apply busy mode per profile
- fix: route /insights through /nastech on Slack
- fix: use event.get_command_args() and add persistence tests
- fix: make /busy command available on gateway platforms
- fix(update): ignore unrelated transitional SCM services
- fix: name the preserved snapshot path in the ROLLBACK FAILED payload
- 19 additional reliability and fixes updates are included in this verified snapshot.

### Documentation

- docs: surface Tencent TokenPlan + hy4-preview across provider docs
- docs: surface Nebius Token Factory across user-facing provider docs
- docs: surface Ramp Router across user-facing provider docs
- docs: chat-completions is now a compat shim on Router, not a 404
- docs(commands): clarify busy gateway behavior
- docs: align busy command references
- docs(test): clarify busy scope coverage
- docs(user-stories): drop the Tokyo itinerary entry
- docs(user-stories): add 65 new community stories
- docs: note the MEASURED_1H_PROVIDERS exception in effective_cache_ttl's docstring

### Improvements

- test(nebius): align catalog tests with current fetch_models contract
- test(nebius): expect verbose model catalog URL
- review: host-resolved efforts, ladder-validated ingest, deduped catalog
- Merge pull request #97912 from kshitijk4poor/chore/author-map-provider-salvages
- test: assert /update dispatch via the handler table, not getsource
- refactor(gateway): share plain command dispatch
- test(gateway): verify routed busy persistence
- chore: map abdi.moya@gmail.com -> AxDSan, sam@odio.email -> srosro (attribution for #97875)
- fmt(js): `npm run fix` on merge (#97946)
- refactor(prompt): platform-hint diet — 7 heavies compressed, −657 tok across the map (facts probe-pinned) (#97899)
- chore: map provider-salvage contributor emails to GitHub logins
- fmt(js): `npm run fix` on merge (#97896)
- 7 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
