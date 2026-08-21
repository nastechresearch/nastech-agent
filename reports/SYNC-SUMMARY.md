# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 103 commits affecting 1287 files.
- **Source revision:** `40643cbaf9b7`.
- **Previous source revision:** `f43eabee5f36`.

## Technical coverage

- **.dockerignore/:** 1 changed files.
- **.github/:** 5 changed files.
- **agent/:** 7 changed files.
- **apps/:** 80 changed files.
- **cli.py/:** 1 changed files.
- **contributors/:** 6 changed files.
- **cron/:** 2 changed files.
- **docker/:** 3 changed files.
- **gateway/:** 18 changed files.
- **nastech_cli/:** 24 changed files.
- **package-lock.json/:** 1 changed files.
- **plugins/:** 3 changed files.
- **scripts/:** 4 changed files.
- **skills/:** 1 changed files.
- **tests/:** 48 changed files.
- **tools/:** 10 changed files.
- **tui_gateway/:** 2 changed files.
- **web/:** 3 changed files.
- **website/:** 10 changed files.

## Delivered improvements

### New capabilities

- feat(update): structured update receipts + post-update fleet version verification
- feat(bot-mode): durable room identity + full gateway fan-out for group-room sync
- feat(cron): per-job reasoning_effort override in job definitions
- feat(desktop,web): enable the React Compiler in both renderer builds
- feat(opencode): sync Zen/Go catalogs — Ox Alpha stealth model, Grok routing, new free tier
- feat(gateway): GATEWAY_RELAY_ALLOW_DIRECT_PLATFORMS opt-out for relay-exclusive mode
- feat(desktop): a connector consent card that knows nothing about connectors
- feat(desktop): resolve a site's own favicon in the main process
- feat(desktop): let plugins switch the theme, and document the theme surface (#91018)
- feat(desktop): let plugins switch the theme from outside React

### Reliability and fixes

- fix(gateway): scope draft-final finalize skip to fresh persistent sends
- fix(telegram): preserve rich finals after DM drafts
- fix(docker): stage2 API_SERVER_KEY bootstrap no longer depends on .env existing (OOF-285) (#88926)
- fix(update): resolve code identity by reading .git directly — no subprocess
- fix(bot-mode): stabilize sync entry identity across gateway round-trips
- fix(gateway): serialize shared bot room updates
- fix(desktop): hydrate shared bot room previews
- fix(desktop): sync bot room previews through profiles
- fix(cli): read multiplex topology from the default root in enroll warning
- fix(cli): warn when gateway enroll writes relay URLs to a secondary multiplex profile
- fix(gateway): classify relay routing stamps as process-global deployment config
- fix(runtime): per-model api_mode + /v1 healing for custom OpenCode-family providers
- 44 additional reliability and fixes updates are included in this verified snapshot.

### Documentation

- docs(telegram): rich_drafts controls draft rendering, not the draft transport
- docs(bot-mode): group rooms sync across Desktops and gateways
- docs: document the desktop plugin SDK theme surface
- docs: add guide for managing Nastech Cloud via the Portal MCP server

### Improvements

- test(bot-mode): drop unused stub param flagged by eslint
- Merge pull request #69829 from Nastechresearch/docs/nastech-cloud-mcp
- Merge pull request #91237 from Nastechresearch/fix/relay-env-exclusive-messaging
- test(gateway): pin config/registration relay-URL agreement under multiplex scope
- chore: map contributor email for Lesnak1
- test(update): Windows progress self-test survives transient /progress socket stalls
- refactor(cron): keep reasoning_effort off the model-facing cronjob tool schema
- test(cron): scrub tracker references from reasoning-effort test docstring
- test(relay): expiry-notice assertion yields for the fire-and-forget ack task
- fmt(js): `npm run fix` on merge (#91256)
- test(gateway): cover profile-scoped relay stamps, log levels, marker cleanup
- chore: map contributor email for @zhongwater123
- 21 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
