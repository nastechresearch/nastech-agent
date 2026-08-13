#!/bin/sh
# shellcheck shell=sh
# /opt/nastech/docker/main-wrapper.sh — wraps the container's CMD with
# the same argument-routing logic the pre-s6 entrypoint.sh used. Runs
# as /init's "main program" (Docker CMD) so it inherits stdin/stdout/
# stderr from the container. The non-PID-1 entrypoint fallback also
# execs this script directly after running the stage2 bootstrap.
#
# Env note: /init scrubs env before invoking CMD, so when this wrapper
# is launched through the supervised path it must rehydrate via
# with-contenv before touching NASTECH_HOME / PATH. On the non-PID-1
# fallback path the Dockerfile env is still intact, so we skip the
# re-exec and continue directly.
#
# Routing:
#   no args                       → exec `nastech` (the default)
#   first arg is an executable    → exec it directly (sleep, bash, sh, …)
#   first arg is anything else    → exec `nastech <args>` (subcommand passthrough)
#
# Drop to nastech via s6-setuidgid, but skip it when already non-root.
set -e

if [ -z "${NASTECH_MAIN_WRAPPER_ENV_READY:-}" ] && \
   [ -z "${NASTECH_HOME:-}" ] && \
   [ -x /command/with-contenv ]; then
    export NASTECH_MAIN_WRAPPER_ENV_READY=1
    exec /command/with-contenv sh "$0" "$@"
fi
unset NASTECH_MAIN_WRAPPER_ENV_READY

drop() { [ "$(id -u)" = 0 ] && set -- s6-setuidgid nastech "$@"; exec "$@"; }

# --- Reject the unsupported `docker run --user <uid>:<gid>` start ---
# Mirror the guard in stage2-hook.sh (cont-init). This is the surface the
# user actually sees in `docker run` output: when the container is pinned to
# an arbitrary non-root, non-nastech UID, the bootstrap was skipped and the
# baked image dirs (owned by the nastech build UID) are unwritable, so fail
# fast here with actionable guidance rather than crashing on `cd`/EACCES
# further down. See stage2-hook.sh for the full rationale.
cur_uid="$(id -u)"
if [ "$cur_uid" != 0 ] && [ "$cur_uid" != "$(id -u nastech)" ]; then
    cat >&2 <<EOF
[nastech] ERROR: container started with --user $cur_uid (an arbitrary, non-nastech UID) — not supported.

To make container-written files match your HOST user, don't use --user.
Start as root (the default) and pass your host UID/GID instead:

    docker run -e NASTECH_UID=\$(id -u) -e NASTECH_GID=\$(id -g) ...

NAS users (Synology / unRAID / UGOS) can use the PUID/PGID aliases:

    docker run -e PUID=\$(id -u) -e PGID=\$(id -g) ...

The image remaps the nastech user to that UID/GID at boot and chowns the data
volume, so files land owned by your host user — the same outcome --user gave,
without breaking the s6 supervision tree.
EOF
    exit 1
fi

# HOME comes through with-contenv as /root (the /init context). Override
# to the nastech user's home before dropping privileges so libraries that
# resolve paths via $HOME (e.g. discord lockfile under XDG_STATE_HOME)
# don't try to write to /root.
export HOME=/opt/data

# Save the Docker -w (or default) working directory before init
# scripts cd to /opt/data, so the container starts in the
# directory the user requested.
_nastech_orig_cwd="${NASTECH_ORIG_CWD:-$PWD}"

cd /opt/data
# shellcheck disable=SC1091
. /opt/nastech/.venv/bin/activate

# Restore the original working directory before handing off to
# the user's command so `nastech chat` starts in the Docker -w
# directory, not /opt/data.
cd "$_nastech_orig_cwd"

if [ $# -eq 0 ]; then
    drop nastech
fi

if command -v "$1" >/dev/null 2>&1; then
    # Bare executable — pass through directly.
    drop "$@"
fi

# Nastech subcommand pass-through.
drop nastech "$@"
