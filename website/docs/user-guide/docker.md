---
sidebar_position: 7
title: "Nastech Docker Setup"
description: "Running Nastech Agent in Docker and using Docker as a terminal backend"
---

# Nastech Docker Setup

There are two distinct ways Docker intersects with Nastech Agent:

1. **Running Nastech IN Docker** — the agent itself runs inside a container (this page's primary focus)
2. **Docker as a terminal backend** — the agent runs on your host but executes every command inside a single, persistent Docker sandbox container that survives across tool calls, `/new`, and subagents for the life of the Nastech process (see [Configuration → Docker Backend](./configuration.md#docker-backend))

This page covers option 1. The container stores all user data (config, API keys, sessions, skills, memories) in a single directory mounted from the host at `/opt/data`. The image itself is stateless and can be upgraded by pulling a new version without losing any configuration.

## Quick start

If this is your first time running Nastech Agent, create a data directory on the host and start the container interactively to run the setup wizard:

:::caution Avoid browser-based VPS consoles for the install commands
Some VPS providers (Hetzner Cloud, and several others) offer a browser-based
console for managing hosts. These consoles transmit special characters
incorrectly — `:` may arrive as `;`, `@` may be mis-rendered, and non-English
keyboard layouts fare worse — which silently corrupts `docker run` arguments
like `-v ~/.nastech:/opt/data`, `-e KEY=value`, and pasted API keys / tokens.

**Connect over SSH instead** (`ssh root@<host>`) for copy-paste-safe command
entry. If you must use the browser console, type the commands manually
instead of pasting, and double-check every `:`, `@`, `=`, and `/` in the
result before hitting Enter.
:::

```sh
mkdir -p ~/.nastech
docker run -it --rm \
  -v ~/.nastech:/opt/data \
  nastechresearch/nastech-agent setup
```

This drops you into the setup wizard, which will prompt you for your API keys and write them to `~/.nastech/.env`. You only need to do this once. It is highly recommended to set up a chat system for the gateway to work with at this point.

:::tip
Inside the container, run `nastech setup --portal` once — the refresh token persists in the mounted `~/.nastech` volume. See [Nastech Portal](/integrations/nastech-portal).
:::

## Running in gateway mode

Once configured, run the container in the background as a persistent gateway (Telegram, Discord, Slack, WhatsApp, etc.):

```sh
docker run -d \
  --name nastech \
  --restart unless-stopped \
  -v ~/.nastech:/opt/data \
  -p 8642:8642 \
  nastechresearch/nastech-agent gateway run
```

Port 8642 exposes the gateway's [OpenAI-compatible API server](./features/api-server.md) and health endpoint. It's optional if you only use chat platforms (Telegram, Discord, etc.), but required if you want the dashboard or external tools to reach the gateway.

:::tip Gateway runs supervised
Inside the official Docker image, `gateway run` is **automatically supervised by s6-overlay**: if the gateway process crashes it's restarted within a couple of seconds without losing the container, and the dashboard (when `NASTECH_DASHBOARD=1` is set) is supervised alongside it. The `gateway run` CMD process itself is a `sleep infinity` heartbeat that keeps the container alive while s6 manages the actual gateway process — so `docker stop` still shuts everything down cleanly, but `docker logs` shows the supervised gateway's output.

You'll see a one-line breadcrumb in `docker logs` confirming the upgrade. To opt out — and get the historical "gateway is the container's main process, container exit = gateway exit" semantics — pass `--no-supervise` or set `NASTECH_GATEWAY_NO_SUPERVISE=1`. The opt-out is useful for CI smoke tests that want the container to exit with the gateway's status code; for production deployments the supervised default is strictly better.

This behavior applies to the s6-based image only. Earlier (tini-based) images still run `gateway run` as the foreground main process.
:::

:::note Where gateway logs go
See the [Where the logs go](#where-the-logs-go) section below for the full routing map (per-profile gateways, dashboard, boot reconciler, container-wide `docker logs`).
:::

:::note Tool-loop hard stops for unattended gateways
The `tool_loop_guardrails.hard_stop_enabled` setting defaults to `false`, which is reasonable for interactive CLI and TUI sessions where a person can see repeated tool-call warnings. In unattended gateway or server deployments, warnings alone may not stop an agent that gets stuck in a repeated tool-call loop. Operators who want circuit-breaker behavior should explicitly enable hard stops in the profile's `config.yaml`:

```yaml
tool_loop_guardrails:
  hard_stop_enabled: true
  hard_stop_after:
    exact_failure: 5
    idempotent_no_progress: 5
```
:::

Note: the API server is gated on `API_SERVER_ENABLED=true`. To expose it beyond `127.0.0.1` inside the container, also set `API_SERVER_HOST=0.0.0.0` and an `API_SERVER_KEY` (minimum 8 characters — generate one with `openssl rand -hex 32`). Example:

```sh
docker run -d \
  --name nastech \
  --restart unless-stopped \
  -v ~/.nastech:/opt/data \
  -p 8642:8642 \
  -e API_SERVER_ENABLED=true \
  -e API_SERVER_HOST=0.0.0.0 \
  -e API_SERVER_KEY="$(openssl rand -hex 32)" \
  -e API_SERVER_CORS_ORIGINS='*' \
  nastechresearch/nastech-agent gateway run
```

Opening any port on an internet facing machine is a security risk. You should not do it unless you understand the risks.

## Running the dashboard

The built-in web dashboard runs as a supervised s6-rc service alongside the gateway in the same container. Set `NASTECH_DASHBOARD=1` to bring it up:

```sh
docker run -d \
  --name nastech \
  --restart unless-stopped \
  -v ~/.nastech:/opt/data \
  -p 8642:8642 \
  -p 9119:9119 \
  -e NASTECH_DASHBOARD=1 \
  nastechresearch/nastech-agent gateway run
```

The dashboard is supervised by s6 — if it crashes, `s6-supervise` restarts it automatically after a short backoff. Dashboard stdout/stderr is forwarded to `docker logs <container>` (no prefix; the gateway's own output now lives in a per-profile s6-log file — see [Where the logs go](#where-the-logs-go) below — so the two streams don't clash).

| Environment variable | Description | Default |
|---------------------|-------------|---------|
| `NASTECH_DASHBOARD` | Set to `1` (or `true` / `yes`) to enable the supervised dashboard service | *(unset — service is registered but stays down)* |
| `NASTECH_DASHBOARD_HOST` | Bind address for the dashboard HTTP server | `0.0.0.0` |
| `NASTECH_DASHBOARD_PORT` | Port for the dashboard HTTP server | `9119` |
| `NASTECH_DASHBOARD_INSECURE` | **Deprecated / no-op.** Formerly bypassed the auth gate; as of the June 2026 hardening it no longer disables authentication. A non-loopback bind always requires an auth provider | *(ignored — configure a provider instead)* |

The dashboard inside the container defaults to binding `0.0.0.0` — without it, the published `-p 9119:9119` port would not be reachable from the host. To restrict the bind to container loopback (for sidecar / reverse-proxy setups), set `NASTECH_DASHBOARD_HOST=127.0.0.1`.

The dashboard's auth gate engages automatically when both of the following are true:

1. The bind host is non-loopback (e.g. the default `0.0.0.0` inside the container), **and**
2. A `DashboardAuthProvider` plugin is registered.

There are three bundled ways to satisfy the second condition:

- **Username/password** — the simplest for a self-hosted / on-prem / homelab container on a trusted network or behind a VPN: set `NASTECH_DASHBOARD_BASIC_AUTH_USERNAME` + `NASTECH_DASHBOARD_BASIC_AUTH_PASSWORD` (and `NASTECH_DASHBOARD_BASIC_AUTH_SECRET` for restart-stable sessions). Not suitable for direct public-internet exposure.
- **OAuth (Nastech Portal)** — for hosted/public deploys: the `dashboard_auth/nastech` provider activates whenever `NASTECH_DASHBOARD_OAUTH_CLIENT_ID` is set.
- **Self-hosted OIDC** — to authenticate against your own identity provider via standard OpenID Connect: the `dashboard_auth/self_hosted` provider activates when `NASTECH_DASHBOARD_OIDC_ISSUER` + `NASTECH_DASHBOARD_OIDC_CLIENT_ID` are set.

Whichever you choose, the gate redirects callers to a login page before they can reach any protected route. See [Web Dashboard → Authentication](features/web-dashboard.md#authentication-gated-mode) for all three providers.

If no provider is registered and the bind is non-loopback, the dashboard **fails closed at startup** with a specific error pointing at the missing env var. There is no longer an escape hatch that serves the dashboard unauthenticated on a public bind: `NASTECH_DASHBOARD_INSECURE=1` is now a deprecated no-op (it logs a warning and is ignored). Configure a provider, or bind `NASTECH_DASHBOARD_HOST=127.0.0.1` and reach the dashboard over an SSH tunnel / Tailscale instead.

:::warning Why `--insecure` was removed
An unauthenticated public dashboard was the entry point for the June 2026 MCP-config persistence campaign: internet scanners reached exposed dashboards (and OpenAI API servers) and drove the agent into planting an SSH-key backdoor. The auth gate is now mandatory on every non-loopback bind. For a trusted-LAN / homelab box, the bundled username/password provider (`NASTECH_DASHBOARD_BASIC_AUTH_USERNAME` + `_PASSWORD`) is the zero-infra way to satisfy it.
:::

Running the dashboard as a separate container **is** supported when that container shares the host PID and network namespace (e.g. `network_mode: host`, as the repo's own `docker-compose.yml` does — see its `dashboard` service). Its gateway-liveness detection requires a shared PID namespace with the gateway process, so the limitation only applies to dashboards run in isolated bridge-network containers without a shared PID namespace.

## Running interactively (CLI chat)

To open an interactive chat session against a running data directory:

```sh
docker run -it --rm \
  -v ~/.nastech:/opt/data \
  nastechresearch/nastech-agent
```

Or if you have already opened a terminal in your running container (via Docker Desktop for instance), just run:

```sh
/opt/nastech/.venv/bin/nastech
```

## Persistent volumes

The `/opt/data` volume is the single source of truth for all Nastech state. It maps to your host's `~/.nastech/` directory and contains:

| Path | Contents |
|------|----------|
| `.env` | API keys and secrets |
| `config.yaml` | All Nastech configuration |
| `SOUL.md` | Agent personality/identity |
| `sessions/` | Conversation history |
| `memories/` | Persistent memory store |
| `skills/` | Installed skills |
| `home/` | Per-profile HOME for Nastech tool subprocesses (`git`, `ssh`, `gh`, `npm`, and skill CLIs) |
| `cron/` | Scheduled job definitions |
| `hooks/` | Event hooks |
| `logs/` | Runtime logs |
| `skins/` | Custom CLI skins |

### Immutable install tree

In hosted and published Docker images, `/opt/nastech` is the installed application tree. It is root-owned and read-only to the runtime `nastech` user, so agent turns, gateway sessions, dashboard actions, and normal `docker exec nastech nastech ...` commands cannot edit the core source, bundled `.venv`, `node_modules`, or TUI bundle in place.

All mutable Nastech state belongs under `/opt/data`: config, `.env`, profiles, skills, memories, sessions, logs, dashboard uploads, plugins, and other user-managed files. The image also disables runtime `.pyc` writes and Nastech lazy dependency installs into `/opt/nastech`; optional platform dependencies needed by the published image should be baked into the image or installed through a new image build.

On hosted/published images, agent self-improvement is scoped to skills, memory, plugins, and config under `/opt/data`. The installed core source under `/opt/nastech` is immutable; core changes are made via PRs to the repo and shipped by updating the image, not by live-editing the running install.

If an operator needs to repair or inspect files outside `/opt/data`, use a root shell intentionally. The `nastech` shim normally drops `docker exec nastech nastech ...` back to the runtime user; set `NASTECH_DOCKER_EXEC_AS_ROOT=1` for a one-off root invocation when you explicitly need root semantics.

Skill CLIs that store credentials under `~` must be initialized against the subprocess HOME, not just the data-volume root. For example, the [xurl skill](./skills/bundled/social-media/social-media-xurl.md) stores OAuth state in `~/.xurl`; in the official Docker layout, Nastech tool calls read that as `/opt/data/home/.xurl`, so run manual xurl auth with `HOME=/opt/data/home` and verify with `HOME=/opt/data/home xurl auth status`.

:::warning
Never run two Nastech **gateway** containers against the same data directory simultaneously — session files and memory stores are not designed for concurrent write access.
:::

## Multi-profile support

Nastech supports [multiple profiles](../reference/profile-commands.md) — separate `~/.nastech/` subdirectories that let you run independent agents (different SOUL, skills, memory, sessions, credentials) from a single installation. **Inside the official Docker image, the s6 supervision tree treats each profile as a first-class supervised service**, so the recommended deployment is **one container hosting all profiles**.

Each profile created with `nastech profile create <name>` gets:

- A dedicated s6 service slot at `/run/service/gateway-<name>/`, registered dynamically by the runtime — no container rebuild required.
- Auto-restart on crash, backoff-managed by `s6-supervise`.
- Per-profile rotated logs at `${NASTECH_HOME}/logs/gateways/<name>/current` (10 archives × 1 MB each).
- State persistence across container restarts: the boot-time reconciler reads `gateway_state.json` from each profile directory and brings the slot back up only for profiles whose last recorded state was `running`. Only a gateway you explicitly stopped (`nastech gateway stop`) stays down across a restart — a container restart, image upgrade, or unexpected exit leaves the recorded state as `running`, so the gateway auto-starts on the next boot.

The lifecycle commands you'd run on the host work the same way from inside the container:

```sh
# Create a profile — registers the gateway-<name> s6 slot.
docker exec nastech nastech profile create coder

# Start / stop / restart — dispatches s6-svc; the gateway lifecycle survives docker restart.
docker exec nastech nastech -p coder gateway start
docker exec nastech nastech -p coder gateway stop
docker exec nastech nastech -p coder gateway restart

# Status — reports `Manager: s6 (container supervisor)` inside the container.
docker exec nastech nastech -p coder gateway status

# Remove a profile — tears down the s6 slot too.
docker exec nastech nastech profile delete coder
```

Under the hood, `nastech gateway start/stop/restart` inside the container is intercepted and routed to `s6-svc` against the right service directory; you don't need to learn the s6 commands directly. For raw supervisor state, use `/command/s6-svstat /run/service/gateway-<name>` (note `/command/` is on PATH only for processes spawned by the supervision tree — when calling from `docker exec`, pass the absolute path).

### Reaching more than one profile from outside the container

Two different surfaces reach a profile's gateway from outside, and they behave differently — don't conflate them:

**Nastech Desktop (and the web dashboard).** The Desktop app's **Remote Gateway** connection talks to a `nastech dashboard` backend (default **port 9119**, enabled by `NASTECH_DASHBOARD=1`) — *not* the OpenAI API server. One dashboard backend serves **every** co-located profile: the app's profile switcher sends the target profile with each request and the backend opens that profile's `NASTECH_HOME` on disk. So you do **not** need a second port — or a second connection — per profile for Desktop; one `:9119` connection covers them all through the switcher.

**OpenAI-compatible API clients (Open WebUI, LobeChat, `/v1/...`).** These talk to each profile's **API server**, which binds **port 8642 for every profile** (resolved from `API_SERVER_PORT` / `platforms.api_server.extra.port` — there is no auto-allocation and no `config.yaml`/`gateway.port` key). If you want a client to reach a *specific* second profile, give that profile a distinct `API_SERVER_PORT` in **its own** `.env`, otherwise its gateway tries to bind 8642 too and conflicts with the default profile:

```sh
# Create the profile (registers its gateway-<name> s6 slot)
docker exec nastech nastech profile create work

# Point its API server at a free port (write to the profile's own .env)
cat >> /opt/data/profiles/work/.env <<'EOF'
API_SERVER_ENABLED=true
API_SERVER_PORT=8643
EOF

docker exec nastech nastech -p work gateway restart
```

Keep `API_SERVER_PORT` in each profile's **own** `.env`, never in the container-wide `environment:` block — a global value would force every profile onto the same port and they would collide. With bridge networking, publish the extra port in `docker-compose.yml` (`- "8643:8643"`); with `network_mode: host` it is already reachable on the host. The default profile's 8642 connection is untouched.

### Why one container with many profiles, not many containers

Before the s6 migration, "one container per profile" was the recommended pattern because there was no in-container supervisor to manage multiple gateways. With s6 as PID 1, that's no longer necessary, and the single-container layout is simpler in almost every dimension:

| | One container, many profiles | One container per profile |
|---|---|---|
| Disk overhead | One image, one bundled venv, one Playwright cache | N images / N caches |
| Memory overhead | Shared Python interpreter cache, shared node_modules | Duplicated per container |
| Profile creation | `docker exec ... nastech profile create <name>` (seconds) | New `docker run` invocation + port allocation + bind-mount config |
| Per-profile crash recovery | `s6-supervise` auto-restart | Docker's `--restart unless-stopped` (slower, kills sibling work) |
| Logs | Per-profile rotated file via `s6-log`, plus container-boot audit log | `docker logs <name>` per container — no built-in rotation |
| Backup | One `~/.nastech` directory | N directories to coordinate |

The default profile (`default`) is always registered on first boot, so a fresh container ships with one supervised gateway out of the box. Additional profiles are pure runtime adds.

### When you DO want a separate container

Profile-in-container is the default. Run a separate container per profile only when you have a specific reason:

- **Resource isolation per workload** — e.g. a runaway browser-tool session in profile A shouldn't be able to OOM profile B. Containers give you `--memory` / `--cpus` per profile.
- **Independent image pinning** — different upstream image tags per workload.
- **Network segmentation** — distinct Docker networks per profile (e.g. one customer-facing, one internal).
- **Compliance / blast radius** — distinct credentials never share an OS-level process tree.

In those cases, declare one service per profile with distinct `container_name`, `volumes`, and `ports`:

```yaml
services:
  nastech-work:
    image: nastechresearch/nastech-agent:latest
    container_name: nastech-work
    restart: unless-stopped
    command: gateway run
    ports:
      - "8642:8642"
    volumes:
      - ~/.nastech-work:/opt/data

  nastech-personal:
    image: nastechresearch/nastech-agent:latest
    container_name: nastech-personal
    restart: unless-stopped
    command: gateway run
    ports:
      - "8643:8642"
    volumes:
      - ~/.nastech-personal:/opt/data
```

The warning from [Persistent volumes](#persistent-volumes) still applies: never point two containers at the same `~/.nastech` directory simultaneously. The s6 supervisor inside each container manages its own profile set; cross-container sharing of a data volume corrupts session files and memory stores.

## Where the logs go

The s6 container has four distinct log surfaces, and "why isn't my gateway showing anything in `docker logs`" is a common surprise. Cheatsheet:

| Source | Where it lands | How to read it |
|---|---|---|
| **Per-profile gateway** (`nastech gateway run` and per-profile gateways under s6) | Tee'd to two places: `docker logs <container>` (real time, no extra prefix) **and** `${NASTECH_HOME}/logs/gateways/<profile>/current` (rotated, ISO-8601 timestamped, 10 archives × 1 MB each) | `docker logs -f nastech` or `tail -F ~/.nastech/logs/gateways/default/current` on the host |
| **Dashboard** (when `NASTECH_DASHBOARD=1`) | `docker logs <container>` (no prefix) | `docker logs -f nastech` — interleaved with gateway lines |
| **Boot reconciler** (records which profile gateways were restored on each container start) | `${NASTECH_HOME}/logs/container-boot.log` (append-only audit log) | `tail -F ~/.nastech/logs/container-boot.log` |
| **Generic Nastech logs** (`agent.log`, `errors.log`) | `${NASTECH_HOME}/logs/` (profile-aware) | `docker exec nastech nastech logs --follow [--level WARNING] [--session <id>]` |

Two practical consequences worth knowing:

- The file copy at `logs/gateways/<profile>/current` is what survives container restarts. `docker logs` only retains output from the current container's lifetime (and is wiped on `docker rm`); the rotated files persist on the bind-mounted volume.
- The boot reconciler's audit line shape is `<iso-timestamp> profile=<name> prior_state=<state> action=<registered|started>`, so a quick `grep profile=coder ~/.nastech/logs/container-boot.log` reveals when a given profile was last restored and whether s6 auto-started it.

## Environment variable forwarding

API keys are read from `/opt/data/.env` inside the container. You can also pass environment variables directly:

```sh
docker run -it --rm \
  -v ~/.nastech:/opt/data \
  -e ANTHROPIC_API_KEY="sk-ant-..." \
  -e OPENAI_API_KEY="sk-..." \
  nastechresearch/nastech-agent
```

Direct `-e` flags override values from `.env`. This is useful for CI/CD or secrets-manager integrations where you don't want keys on disk.

:::note Looking for Docker as the **terminal backend**?
This page covers running Nastech itself inside Docker. If you want Nastech to execute the agent's `terminal` / `execute_code` calls inside a Docker sandbox container (one long-lived container shared across Nastech processes — see issue #20561), that's a separate config block — `terminal.backend: docker` plus `terminal.docker_image`, `terminal.docker_volumes`, `terminal.docker_forward_env`, `terminal.docker_env`, `terminal.docker_run_as_host_user`, `terminal.docker_extra_args`, `terminal.docker_persist_across_processes`, and `terminal.docker_orphan_reaper`. See [Configuration → Docker Backend](configuration.md#docker-backend) for the full set including container-lifecycle rules.
:::

## Docker Compose example

For persistent deployment with both the gateway and dashboard, a `docker-compose.yaml` is convenient:

```yaml
services:
  nastech:
    image: nastechresearch/nastech-agent:latest
    container_name: nastech
    restart: unless-stopped
    command: gateway run
    ports:
      - "8642:8642"   # gateway API
      - "9119:9119"   # dashboard (only reached when NASTECH_DASHBOARD=1)
    volumes:
      - ~/.nastech:/opt/data
    environment:
      - NASTECH_DASHBOARD=1
      # Uncomment to forward specific env vars instead of using .env file:
      # - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      # - OPENAI_API_KEY=${OPENAI_API_KEY}
      # - TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}
    deploy:
      resources:
        limits:
          memory: 4G
          cpus: "2.0"
```

Start with `docker compose up -d` and view logs with `docker compose logs -f`. The supervised gateway's stdout is also tee'd to `${NASTECH_HOME}/logs/gateways/<profile>/current` on the volume — see [Where the logs go](#where-the-logs-go) for the full routing map.

## Optional: Linux desktop audio bridge

Voice mode in Docker needs two separate things to work: Nastech must be allowed to probe audio devices inside the container, and the container must be able to reach your host audio server. The setup below covers the host audio plumbing for Linux desktops that expose a PulseAudio-compatible socket, including many PipeWire setups.

:::caution
This is a Linux desktop workaround, not a general Docker Desktop feature. It is useful when you already have host audio working and want CLI voice mode inside the Nastech container. If Nastech still reports `Running inside Docker container -- no audio devices`, use a build that includes Docker audio probing support for `PULSE_SERVER` / `PIPEWIRE_REMOTE`.
:::

First, create an ALSA config next to your Compose file:

```conf title="asound.conf"
pcm.!default {
    type pulse
    hint {
        show on
        description "Default ALSA Output (PulseAudio)"
    }
}

pcm.pulse {
    type pulse
}

ctl.!default {
    type pulse
}
```

Then build a small derived image with the ALSA PulseAudio plugin installed:

```dockerfile title="Dockerfile.audio"
FROM nastechresearch/nastech-agent:latest

USER root
RUN apt-get update \
    && apt-get install -y --no-install-recommends libasound2-plugins \
    && rm -rf /var/lib/apt/lists/*
```

Use that image in Compose and pass through the host user's PulseAudio socket and cookie:

```yaml
services:
  nastech:
    build:
      context: .
      dockerfile: Dockerfile.audio
    image: nastech-agent-audio
    container_name: nastech
    restart: unless-stopped
    command: gateway run
    volumes:
      - ~/.nastech:/opt/data
      - /run/user/${NASTECH_UID}/pulse:/run/user/${NASTECH_UID}/pulse
      - ~/.config/pulse/cookie:/tmp/pulse-cookie:ro
      - ./asound.conf:/etc/asound.conf:ro
    environment:
      - NASTECH_UID=${NASTECH_UID}
      - NASTECH_GID=${NASTECH_GID}
      - XDG_RUNTIME_DIR=/run/user/${NASTECH_UID}
      - PULSE_SERVER=unix:/run/user/${NASTECH_UID}/pulse/native
      - PULSE_COOKIE=/tmp/pulse-cookie
```

Start it with your host UID/GID so the container process can access the per-user audio socket:

```sh
export NASTECH_UID="$(id -u)"
export NASTECH_GID="$(id -g)"
docker compose up -d --build
```

To verify what PortAudio sees inside the container:

```sh
docker exec nastech /opt/nastech/.venv/bin/python -c "import sounddevice as sd; print(sd.query_devices())"
```

## Resource limits

The Nastech container needs moderate resources. Recommended minimums:

| Resource | Minimum | Recommended |
|----------|---------|-------------|
| Memory | 1 GB | 2–4 GB |
| CPU | 1 core | 2 cores |
| Disk (data volume) | 500 MB | 2+ GB (grows with sessions/skills) |

Browser automation (Playwright/Chromium) is the most memory-hungry feature. If you don't need browser tools, 1 GB is sufficient. With browser tools active, allocate at least 2 GB.

Set limits in Docker:

```sh
docker run -d \
  --name nastech \
  --restart unless-stopped \
  --memory=4g --cpus=2 \
  -v ~/.nastech:/opt/data \
  nastechresearch/nastech-agent gateway run
```

## What the Dockerfile does

The official image is based on `debian:13.4` and includes:

- Python 3.13 with dependencies synced from the lockfile via `uv sync --frozen --no-install-project` for the baked extras (`all`, `messaging`, Anthropic/Bedrock/Azure identity, Hindsight, Matrix), followed by a no-dependency editable install of Nastech itself.
- Node.js 26 + npm (for browser automation, WhatsApp bridge, TUI/Desktop bundles, and workspace build tooling)
- Playwright with Chromium (`npx playwright install --with-deps chromium --only-shell`)
- ripgrep, ffmpeg, git, and `xz-utils` as system utilities
- **`docker-cli`** — so agents running inside the container can drive the host's Docker daemon (bind-mount `/var/run/docker.sock` to opt in) for `docker build`, `docker run`, container inspection, etc.
- **`openssh-client`** — enables the [SSH terminal backend](/user-guide/configuration#ssh-backend) from inside the container. The SSH backend shells out to the system `ssh` binary; without this, it failed silently in containerized installs.
- The WhatsApp bridge (`scripts/whatsapp-bridge/`)
- **[`s6-overlay`](https://github.com/just-containers/s6-overlay) v3** as PID 1 (replaces the older `tini`) — supervises the dashboard and per-profile gateways with auto-restart on crash, reaps zombie subprocesses, and forwards signals.

The image treats `/opt/nastech` as an immutable install tree at runtime. Optional Python extras, Node workspaces, and TUI assets that must be available inside Docker need to be baked during the image build; runtime lazy installs are disabled so supervised gateways and `docker exec nastech …` commands do not try to write dependency artifacts back into the read-only source tree.

The container's `ENTRYPOINT` is a small dispatcher (`docker/entrypoint-dispatch.sh`). When the container owns PID 1 (normal Docker / Podman), it exec's s6-overlay's `/init` and you get the full supervision tree described below. When a platform wraps the image entrypoint under its own PID-1 init (Fly.io Machines, `docker run --init`, some Nomad/Kubernetes setups), `/init` would abort with `s6-overlay-suexec: fatal: can only run as pid 1` — so the dispatcher instead runs the stage2 bootstrap directly and exec's the main wrapper without s6. On that fallback path the requested command still runs, but supervised services (dashboard, per-profile gateways) are unavailable.

On the PID-1 path, `/init`:
1. Runs `/etc/cont-init.d/01-nastech-setup` (= `docker/stage2-hook.sh`) as root: optional UID/GID remap, fixes volume ownership, seeds `.env` / `config.yaml` / `SOUL.md` on first boot, runs non-interactive config-schema migrations unless `NASTECH_SKIP_CONFIG_MIGRATION=1`, syncs bundled skills.
2. Runs `/etc/cont-init.d/02-reconcile-profiles` (= `nastech_cli.container_boot`): walks `$NASTECH_HOME/profiles/<name>/`, recreates the per-profile gateway s6 service slot under `/run/service/gateway-<profile>/`, and auto-starts only those whose last recorded state was `running` (see [Per-profile gateway supervision](#per-profile-gateway-supervision)).
3. Starts the static `main-nastech` and `dashboard` s6-rc services.
4. Exec's the container's CMD as the main program (`/opt/nastech/docker/main-wrapper.sh`), which routes the arguments the user passed to `docker run`:
   - no args → `nastech` (the default)
   - first arg is an executable on PATH (e.g. `sleep`, `bash`) → exec it directly
   - anything else → `nastech <args>` (subcommand passthrough)
   The container exits when this main program exits, with its exit code.

:::warning Breaking change vs. pre-s6 images
The container ENTRYPOINT is now the `entrypoint-dispatch.sh` dispatcher (which delegates to s6-overlay's `/init` under PID 1), not `/usr/bin/tini`. All five documented `docker run` invocation patterns (no args, `chat -q "…"`, `sleep infinity`, `bash`, `--tui`) behave identically to the tini-based image. If you have a downstream wrapper that depended on tini-specific signal behavior or hard-coded `/usr/bin/tini --` invocation, pin to the previous image tag.
:::

:::warning Privilege model
Do not override the image entrypoint unless you keep `/init` (or, equivalently, the legacy `docker/entrypoint.sh` shim that forwards to the stage2 hook) in the command chain. s6-overlay's `/init` runs as root so it can chown the volume on first boot, then drops to the `nastech` user via `s6-setuidgid` for every supervised service AND for the main program. Starting `nastech gateway run` as root inside the official image is refused by default because it can leave root-owned files in `/opt/data` and break later dashboard or gateway starts. Set `NASTECH_ALLOW_ROOT_GATEWAY=1` only when you intentionally accept that risk.
:::

### `docker exec` automatically drops to the `nastech` user

`docker exec nastech <cmd>` defaults to running as root inside the container, but the image ships a thin shim at `/opt/nastech/bin/nastech` (earliest on PATH) that detects root callers and transparently re-execs through `s6-setuidgid nastech`. So `docker exec nastech login`, `docker exec nastech profile create …`, `docker exec nastech setup`, etc. all write files owned by UID 10000 — i.e. readable by the supervised gateway — with no extra `--user` flag needed. Non-root callers (the supervised processes themselves, `docker exec --user nastech`, kanban subagents inside the container) hit a short-circuit that exec's the venv binary directly, so there's no overhead on the hot paths.

If you specifically need a `docker exec` that retains root semantics (diagnostic sessions, inspecting root-only state, files outside `/opt/data` that root happens to own), opt out per invocation:

```sh
docker exec -e NASTECH_DOCKER_EXEC_AS_ROOT=1 nastech <cmd>
```

The shim accepts `1` / `true` / `yes` (case-insensitive). Anything else — including typos like `=0` — falls through to the drop, so silent opt-outs aren't possible. If `s6-setuidgid` isn't available (custom builds that stripped s6-overlay), the shim refuses to run as root and exits 126 instead, surfacing the broken privilege model loudly rather than regressing to the historical footgun where `docker exec nastech login` would write `auth.json` as `root:root` and break the supervised gateway's auth on every chat platform message.

### Per-profile gateway supervision

Each profile created with `nastech profile create <name>` automatically gets an s6-supervised gateway service registered at `/run/service/gateway-<name>/`, with state-persistent auto-restart across container restarts. See [Multi-profile support](#multi-profile-support) above for the user-facing workflow and the lifecycle commands.

**Supervision benefits over the pre-s6 image:**

- Gateway crashes are auto-restarted by `s6-supervise` after a ~1s backoff.
- Dashboard, when enabled with `NASTECH_DASHBOARD=1`, is supervised on the same supervision tree and gets the same auto-restart treatment.
- `docker restart`, image upgrades (`docker compose up -d --force-recreate`), and unexpected exits preserve running gateways: the cont-init reconciler reads `$NASTECH_HOME/profiles/<name>/gateway_state.json` and brings the slot back up if the last recorded state was `running`. Only an explicit `nastech gateway stop` records `stopped` and keeps the gateway down across the restart; the container/s6 SIGTERM sent on a restart or upgrade is treated as "still running" and auto-starts.
- Per-profile gateway logs persist under `$NASTECH_HOME/logs/gateways/<profile>/current` (rotated by `s6-log`), and the reconciler's actions are appended to `$NASTECH_HOME/logs/container-boot.log` per boot. See [Where the logs go](#where-the-logs-go) for the full routing map.

`nastech status` inside the container reports `Manager: s6 (container supervisor)`. Use `/command/s6-svstat /run/service/gateway-<name>` for the raw supervisor view (note `/command/` is on PATH for supervision-tree processes only; pass the absolute path when calling from `docker exec`).

## Upgrading

Pull the latest image and recreate the container. Your data directory is
preserved, and the container runs non-interactive config-schema migrations
against the mounted `$NASTECH_HOME/config.yaml` before starting the gateway.
When a migration is needed, Nastech writes timestamped backups next to
`config.yaml` and `.env` first.

```sh
docker pull nastechresearch/nastech-agent:latest
docker rm -f nastech
docker run -d \
  --name nastech \
  --restart unless-stopped \
  -v ~/.nastech:/opt/data \
  nastechresearch/nastech-agent gateway run
```

Or with Docker Compose:

```sh
docker compose pull
docker compose up -d
```

Set `NASTECH_SKIP_CONFIG_MIGRATION=1` only if you need to inspect or migrate the
persisted config manually before letting the new image rewrite it.

## Skills and credential files

When using Docker as the execution environment (not the methods above, but when the agent runs commands inside a Docker sandbox — see [Configuration → Docker Backend](./configuration.md#docker-backend)), Nastech reuses a single long-lived container for all tool calls and automatically bind-mounts the skills directory (`~/.nastech/skills/`) and any credential files declared by skills into that container as read-only volumes. Skill scripts, templates, and references are available inside the sandbox without manual configuration, and because the container persists for the life of the Nastech process, any dependencies you install or files you write stay around for the next tool call.

The same syncing happens for SSH and Modal backends — skills and credential files are uploaded via rsync or the Modal mount API before each command.

## Installing more tools in the container

The official image ships with a curated set of utilities (see [What the Dockerfile does](#what-the-dockerfile-does)), but not every tool an agent might want is preinstalled. There are five recommended approaches, in increasing order of effort and durability.

### npm or Python tools — use `npx` or `uvx`

For any tool published to npm or PyPI, instruct Nastech to run it via `npx` (npm) or `uvx` (Python) and to remember that command in its persistent memory. If the tool needs a config file or credentials, instruct it to drop those under `/opt/data` (e.g. `/opt/data/<tool>/config.yaml`).

Dependencies are fetched on demand and cached for the life of the container. Configuration written under `/opt/data` survives container restarts because it lives on the bind-mounted host directory. The package cache itself is rebuilt after a `docker rm`, but `npx` and `uvx` re-fetch transparently the next time the tool runs.

### Other tools (apt packages, binaries) — install and remember

For anything outside npm or PyPI — `apt` packages, prebuilt binaries, language runtimes not already in the image — instruct Nastech how to install it (e.g. `apt-get update && apt-get install -y <package>`) and tell it to remember the install command. The tool persists for the rest of the container's lifetime, and Nastech will re-run the install command after a container restart when it next needs the tool.

This is a good fit for tools that are quick to install and used occasionally. For tools used constantly, prefer the next approach.

### Durable installs — build a derived image

When a tool must be available immediately on every container start with no re-install delay, build a new image that inherits from `nastechresearch/nastech-agent` and installs the tool in a layer:

```dockerfile
FROM nastechresearch/nastech-agent:latest

USER root
RUN apt-get update \
    && apt-get install -y --no-install-recommends <your-package> \
    && rm -rf /var/lib/apt/lists/*
USER nastech
```

Build it and use it in place of the official image:

```sh
docker build -t my-nastech:latest .
docker run -d \
  --name nastech \
  --restart unless-stopped \
  -v ~/.nastech:/opt/data \
  -p 8642:8642 \
  my-nastech:latest gateway run
```

The entrypoint script and `/opt/data` semantics are inherited unchanged, so the rest of this page still applies. Remember to rebuild the image when pulling a newer upstream `nastechresearch/nastech-agent`.

### Complex tools or multi-service stacks — run a sidecar container

For tools that bring their own service (a database, a web server, a queue, a headless browser farm) or that are too heavy to live inside the Nastech container, run them as a separate container on a shared Docker network. Nastech reaches the sidecar by container name, the same way it reaches a local inference server (see [Connecting to local inference servers](#connecting-to-local-inference-servers-vllm-ollama-etc)).

```yaml
services:
  nastech:
    image: nastechresearch/nastech-agent:latest
    container_name: nastech
    restart: unless-stopped
    command: gateway run
    ports:
      - "8642:8642"
    volumes:
      - ~/.nastech:/opt/data
    networks:
      - nastech-net

  my-tool:
    image: example/my-tool:latest
    container_name: my-tool
    restart: unless-stopped
    networks:
      - nastech-net

networks:
  nastech-net:
    driver: bridge
```

From inside the Nastech container, the sidecar is reachable at `http://my-tool:<port>` (or whatever protocol it serves). This pattern keeps each service's lifecycle, resource limits, and upgrade cadence independent, and avoids bloating the Nastech image with dependencies that are only needed by one tool.

### Broadly useful tools — open an issue or pull request

If a tool is likely to be useful to most Nastech Agent users, consider contributing it upstream rather than carrying it in a private derived image. Open an issue or pull request on the [nastech-agent repository](https://github.com/NastechResearch/nastech-agent) describing the tool and its use case. Tools that get bundled into the official image benefit every user and avoid the maintenance overhead of a downstream fork.

## Connecting to local inference servers (vLLM, Ollama, etc.)

When running Nastech in Docker and your inference server (vLLM, Ollama, text-generation-inference, etc.) is also running on the host or in another container, networking requires extra attention.

### Docker Compose (recommended)

Put both services on the same Docker network. This is the most reliable approach:

```yaml
services:
  vllm:
    image: vllm/vllm-openai:latest
    container_name: vllm
    command: >
      --model Qwen/Qwen2.5-7B-Instruct
      --served-model-name my-model
      --host 0.0.0.0
      --port 8000
    ports:
      - "8000:8000"
    networks:
      - nastech-net
    deploy:
      resources:
        reservations:
          devices:
            - capabilities: [gpu]

  nastech:
    image: nastechresearch/nastech-agent:latest
    container_name: nastech
    restart: unless-stopped
    command: gateway run
    ports:
      - "8642:8642"
    volumes:
      - ~/.nastech:/opt/data
    networks:
      - nastech-net

networks:
  nastech-net:
    driver: bridge
```

Then in your `~/.nastech/config.yaml`, use the **container name** as the hostname:

```yaml
model:
  provider: custom
  model: my-model
  base_url: http://vllm:8000/v1
  api_key: "none"
```

:::tip Key points
- Use the **container name** (`vllm`) as the hostname — not `localhost` or `127.0.0.1`, which refer to the Nastech container itself.
- The `model` value must match the `--served-model-name` you passed to vLLM.
- Set `api_key` to any non-empty string (vLLM requires the header but doesn't validate it by default).
- Do **not** include a trailing slash in `base_url`.
:::

### Standalone Docker run (no Compose)

If your inference server runs directly on the host (not in Docker), use `host.docker.internal` on macOS/Windows, or `--network host` on Linux:

**macOS / Windows:**

```sh
docker run -d \
  --name nastech \
  -v ~/.nastech:/opt/data \
  -p 8642:8642 \
  nastechresearch/nastech-agent gateway run
```

```yaml
# config.yaml
model:
  provider: custom
  model: my-model
  base_url: http://host.docker.internal:8000/v1
  api_key: "none"
```

**Linux (host networking):**

```sh
docker run -d \
  --name nastech \
  --network host \
  -v ~/.nastech:/opt/data \
  nastechresearch/nastech-agent gateway run
```

```yaml
# config.yaml
model:
  provider: custom
  model: my-model
  base_url: http://127.0.0.1:8000/v1
  api_key: "none"
```

:::warning With `--network host`, the `-p` flag is ignored — all container ports are directly exposed on the host.
:::

### Verifying connectivity

From inside the Nastech container, confirm the inference server is reachable:

```sh
docker exec nastech curl -s http://vllm:8000/v1/models
```

You should see a JSON response listing your served model. If this fails, check:

1. Both containers are on the same Docker network (`docker network inspect nastech-net`)
2. The inference server is listening on `0.0.0.0`, not `127.0.0.1`
3. The port number matches

### Ollama

Ollama works the same way. If Ollama runs on the host, use `host.docker.internal:11434` (macOS/Windows) or `127.0.0.1:11434` (Linux with `--network host`). If Ollama runs in its own container on the same Docker network:

```yaml
model:
  provider: custom
  model: llama3
  base_url: http://ollama:11434/v1
  api_key: "none"
```

## Troubleshooting

### Container exits immediately

Check logs: `docker logs nastech`. Common causes:
- Missing or invalid `.env` file — run interactively first to complete setup
- Port conflicts if running with exposed ports

### "Permission denied" errors

The container's stage2 hook drops privileges to the non-root `nastech` user (UID 10000) via `s6-setuidgid` inside each supervised service. If your host `~/.nastech/` is owned by a different UID, set `NASTECH_UID`/`NASTECH_GID` — or their `PUID`/`PGID` aliases, for parity with LinuxServer.io and NAS images — to match your host user, or ensure the data directory is writable:

```sh
chmod -R 755 ~/.nastech
```

On a NAS (UGOS, Synology, unRAID) the data directory is typically a **bind mount** owned by a host UID the container cannot `chown`. Set `PUID`/`PGID` (or `NASTECH_UID`/`NASTECH_GID`) to that host user so the runtime runs as the owner of the mount rather than UID 10000:

```sh
docker run -d \
  --name nastech \
  -e PUID=1000 -e PGID=10 \
  -v /volume1/docker/nastech:/opt/data \
  nastechresearch/nastech-agent gateway run
```

`docker exec nastech <cmd>` automatically drops to UID 10000 too — see [`docker exec` automatically drops to the `nastech` user](#docker-exec-automatically-drops-to-the-nastech-user) for details and the per-invocation opt-out.

### "Permission denied" on every `docker exec` (install dir locked to 0700)

Images built before late August 2026 had a bug where writing a credential file directly under `/opt/nastech` restricted that directory to `0700`, locking the `nastech` user (UID 10000) out of the install tree. Every new `docker exec` then fails with `Permission denied`.

Pulling a newer image and recreating the container fixes it permanently (the install dir ships as `0755` and current releases no longer restrict it). If you need to recover a running container in place without recreating it:

```sh
docker exec -u root nastech chmod 0755 /opt/nastech
```

### Browser tools not working

Playwright needs shared memory. Add `--shm-size=1g` to your Docker run command:

```sh
docker run -d \
  --name nastech \
  --shm-size=1g \
  -v ~/.nastech:/opt/data \
  nastechresearch/nastech-agent gateway run
```

### Gateway not reconnecting after network issues

The `--restart unless-stopped` flag handles most transient failures. If the gateway is stuck, restart the container:

```sh
docker restart nastech
```

### Checking container health

```sh
docker logs --tail 50 nastech          # Recent logs
docker run -it --rm nastechresearch/nastech-agent:latest version     # Verify version
docker stats nastech                    # Resource usage
```
