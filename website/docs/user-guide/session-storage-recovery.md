---
title: "Session Storage Recovery"
description: "What to do when Nastech says another process holds an old copy of the session database's write-ahead log, and what the files beside state.db are"
---

# Session storage recovery

Nastech keeps every conversation in one SQLite file per profile, `state.db`, with two
sidecar files SQLite manages itself: `state.db-wal` (the write-ahead log) and `state.db-shm`.
Several Nastech processes can share that file safely — the gateway, the Desktop app, the
dashboard, cron, and CLI commands all write through SQLite's own locking.

One thing is not safe: **rewriting the store while another process is writing to it**.
When that happens, the processes still holding the *old* copy of the log stop writing on
purpose and every turn answers with a message like:

> another Nastech process still holds an old copy of the session database's write-ahead log,
> so Nastech stopped writing to keep the file safe …

This page is the guide that message links to. Nothing is lost when you see it; the
refusal exists precisely so nothing gets lost.

## The fix in three steps

1. **Quit every Nastech process on that profile.** Desktop app, gateway, dashboard, cron:

   ```bash
   nastech gateway stop          # add -p <profile> for a named profile
   ```

   then quit the Desktop app from its menu and stop any dashboard (`nastech dashboard --stop`)
   or custom service you run. Restarting *one* of them is not enough — a single process left
   holding the old log keeps every new one refusing.

2. **Ask doctor who is still holding the log.**

   ```bash
   nastech doctor                # add -p <profile> for a named profile
   ```

   While anything still holds the retired log, doctor prints each holder as
   `PID N (command)` with the same remedy, and skips its health probes and any `--fix` work
   so it cannot become another writer. Stop the listed processes and run it again until the
   line is gone.

3. **Start Nastech again** (one process first — the gateway or the Desktop app) and send your
   message once more. Your conversation resumes from where it stopped.

## Do not

- **Do not run `nastech doctor --fix` while the processes are running.** Doctor refuses the
  checkpoint while it can see a process holding the retired log, but on a host where it cannot
  inspect processes the fix path is exactly the second writer that caused the problem.
- **Do not delete `state.db-wal` or `state.db-shm`.** The log holds committed conversations
  that are not yet in `state.db`. Deleting it is the one action that turns a refusal into
  real data loss.
- **Do not copy `state.db` alone.** The three files are one image. Use a snapshot
  (`nastech backup`) or `nastech sessions recover`, never `cp state.db somewhere/`.
- **Do not ask the agent to fix it.** The agent's own session is in the same store; it will
  hit the same refusal.

## Maintenance commands refuse while someone is writing

`nastech sessions optimize`, `nastech sessions optimize-storage` and `nastech sessions prune`
rewrite the store (VACUUM, a full-text index rebuild, bulk deletes). Running one of them under
a live gateway is how a fleet of agents ends up in the refusal above, so they now check first
and refuse while another process holds the database:

```text
Refusing `nastech sessions optimize-storage`: another process is using ~/.nastech/state.db.
  PID 41230 (nastech gateway run): state.db, state.db-shm, state.db-wal
  PID 41355 (nastech serve --profile work): state.db-wal
Rewriting the database under a live writer is how every agent ends up refusing turns with the
retired state.db-wal error. Nothing is lost.
Stop them first (`nastech gateway stop`, quit the Desktop app, pause cron), then re-run.
Override with --force if you accept the risk.
```

`--dry-run` previews are never blocked. `--force` runs anyway — use it only when you know
the listed processes are idle (a reader you started yourself, for example). The same check
runs when you type `sessions optimize` in the Desktop console.

## Files you may find beside `state.db`

| File or directory | What it is | What to do |
|---|---|---|
| `state.db-wal`, `state.db-shm` | SQLite's live write-ahead log and its shared-memory index. A large `-wal` is normal while the gateway or Desktop is running. | Leave them alone. They shrink on their own at the next checkpoint. |
| `state.db.retired-wal-<timestamp>-<pid>/` | A capture Nastech made of the log copy a process was still holding when it refused to write, plus a `manifest.json` describing it. Forensic evidence, not a backup you restore blindly. | Keep it. If conversations from just before the incident are missing after recovery, attach the directory to a bug report; a maintainer can tell from `manifest.json` whether those frames belong on top of the current file. |
| `state.db.pre-update-emergency-<timestamp>.bak` | A snapshot the Desktop updater takes before it touches the store. | Keep it until you have used the updated app for a while. Restore only with every Nastech process stopped: `nastech sessions recover --source <file> --inspect-only` first. |
| `state.db.corrupt.<timestamp>.bak`, `*.malformed-backup` | Copies of a file Nastech found damaged before it repaired or quarantined it. | Do not restore them over `state.db` — they are the same damage. Keep for a report; safe to delete once you are back to normal. |
| `state-snapshots/` | Quick snapshots `nastech update` and `nastech backup` take. | Restore with every Nastech process stopped; see [`nastech backup`](../reference/cli-commands.md#nastech-backup). |

## When the three steps do not work

If every Nastech process is stopped, `nastech doctor` no longer lists a holder, and the
gateway still refuses to write when you start it, the file itself may be damaged. Stop
everything again and inspect without writing:

```bash
nastech sessions recover --source ~/.nastech/state.db --inspect-only
```

`--inspect-only` never modifies the file. If it reports the store as recoverable, follow the
command it prints, or restore the newest snapshot from `state-snapshots/`. The mechanics
behind all of this are in the developer guide:
[State DB recovery](../developer-guide/state-db-recovery.md) and
[Session storage](../developer-guide/session-storage.md).
