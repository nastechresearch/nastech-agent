# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 107 commits affecting 3317 files.
- **Source revision:** `ebc9960b9d42`.
- **Previous source revision:** `369cc6b07f26`.

## Technical coverage

- **.github/:** 9 changed files.
- **.npmrc/:** 2 changed files.
- **agent/:** 16 changed files.
- **apps/:** 58 changed files.
- **cron/:** 1 changed files.
- **gateway/:** 5 changed files.
- **locales/:** 19 changed files.
- **mcp_serve.py/:** 1 changed files.
- **nastech_cli/:** 27 changed files.
- **nastech_state_dbfile.py/:** 3 changed files.
- **nastech_state_fts.py/:** 4 changed files.
- **nastech_state_messages.py/:** 1 changed files.
- **nastech_state_repair.py/:** 1 changed files.
- **nastech_state_runtime.py/:** 1 changed files.
- **nastech_state_schema.py/:** 4 changed files.
- **nastech_state_search.py/:** 3 changed files.
- **package-lock.json/:** 14 changed files.
- **package.json/:** 4 changed files.
- **plugin-catalog/:** 12 changed files.
- **plugins/:** 2 changed files.
- **pm/:** 5 changed files.
- **pyproject.toml/:** 3 changed files.
- **scripts/:** 3 changed files.
- **skills/:** 1 changed files.
- **tests/:** 76 changed files.
- **tests-js/:** 4 changed files.
- **tools/:** 30 changed files.
- **uv.lock/:** 4 changed files.
- **web/:** 6 changed files.
- **website/:** 42 changed files.

## Delivered improvements

### New capabilities

- feat(pm): pm update --skip-target leaves a target's pins alone
- feat(mcp): declared per-tool costs and a per-chat spend limit for MCP servers
- feat(data-use): route connector results that need no-training to qualifying Nastech endpoints

### Reliability and fixes

- fix(terminal): background launches on env-backed backends honour workdir
- fix(terminal): report a failed sandbox background launch as an error
- fix(update): diagnose a damaged checkout from the checkout, not the stderr
- fix(update): only local git's own 'not a git repository' reads as a damaged checkout
- fix(update): a damaged .git no longer strands paused gateways
- fix(deps): bump webpack-dev-middleware 7.4.5 → 7.4.6 (high, GHSA-g84c-rxfj-3j2c)
- fix(deps): bump simple-git 3.36.0 → 4.0.2 (critical, GHSA-x6jw-m9v5-85vh)
- fix(deps): bump katex 0.16.47 → 0.18.4 (low, GHSA-238p-pmpm-9mq7)
- fix(deps): bump postcss-selector-parser → 7.1.6 (medium, GHSA-rj75-hqrm-r3gf)
- fix(deps): bump oauthlib 3.3.1 → 4.0.0 (medium, GHSA-xpv3-w29h-x7cv)
- fix(deps): bump tinypool 1.1.1 → 2.2.0 (critical, GHSA-85c8-ppgw-ccpr)
- fix(pm): name the URL when an update pin fails with an HTTP error
- 44 additional reliability and fixes updates are included in this verified snapshot.

### Documentation

- docs(update): repairing a checkout whose .git git rejects
- docs(mcp): tool costs and per-chat spend limits for MCP servers and portable packages

### Improvements

- plugin-catalog: re-pin agent-importers to 6108b7b (OpenClaw migration moved in)
- Merge pull request #142799 from Nastechresearch/deps/webpack-dev-middleware-7.4.6
- refactor(mcp): Nastech as an MCP server leaves core for the mcp-serve plugin
- test(e2e): damaged .git on Windows — paused gateway returns, installer repairs
- Merge pull request #142783 from Nastechresearch/deps/simple-git-4.0.2
- Merge pull request #142781 from Nastechresearch/deps/katex-0.18.4
- Merge pull request #142758 from Nastechresearch/deps/postcss-selector-parser-7.1.6
- chore(catalog): re-pin meshy to 6108b7b4 (in-place animations, image saving)
- Merge pull request #142753 from Nastechresearch/deps/tinypool-2.2.0
- Merge pull request #142754 from Nastechresearch/deps/oauthlib-4.0.0
- Merge pull request #142707 from Nastechresearch/deps/nanoid-3.3.20
- Merge pull request #142705 from Nastechresearch/deps/sanitize-html-2.18.1
- 34 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** fresh-direct-clone at ebc9960b9d42, fetched 2026-10-22T00:26:34+00:00
- **Publication gate:** PASS - cleared for human review only
- **Tree parity:** 20691/20691 files verified byte-faithful after branding; no outstanding differences
- **Branding:** 20691 files branded, 20506 rewritten, 0 errors
- **Fork consistency:** 0 inconsistency violations, 49 fork-owned files carried forward
- **Upstream change evidence:** added 24, deleted 16, modified 193, renamed 0

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
