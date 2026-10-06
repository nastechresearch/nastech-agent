---
sidebar_position: 3
title: "Android / Termux"
description: "Install Nastech Agent on Android from its signed Termux APT repository"
---

# Nastech on Android with Termux

:::danger Termux is currently broken
The Termux package does not work right now. A fix is in progress and will
ship soon. Until then, the steps below may fail or install a package that
does not run.
:::

The Termux package runs Nastech on **aarch64 (arm64-v8a)** Android devices.
Two APT channels are published under
`https://nastech-assets.nastech-agent.nastechresearch.workers.dev/releases/termux/<channel>`:

| Channel | APT suite | Contents |
| --- | --- | --- |
| `stable` | `nastech-stable` | Tagged `vMAJOR.MINOR.PATCH` releases that passed the stable release gate |
| `canary` | `nastech-canary` | Prerelease builds from canary tags; versions carry `~canary.<timestamp>` |

The steps below use `stable`. To follow prereleases, replace `stable` with
`canary` and `nastech-stable` with `nastech-canary` in steps 2 and 4. Both
channels are signed with the same key.

The package includes Python, Node.js, npm, uv, ripgrep, ffmpeg, and their runtime libraries.
CI builds the native Python wheels and the TUI before it creates the package.
The device does not compile core dependencies or assemble its base Python
environment during installation. The package uses Python 3.14 with the bionic
interpreter pin; it does not require the same patch version as desktop CPython.
The wheel closure is core plus `acp`, not all desktop extras.

## Install

Use the standard [Termux](https://termux.dev/) application.
The package requires its standard prefix, `/data/data/com.termux/files/usr`.
Other architectures and renamed Termux application packages are not supported.
The wheels target Android API 24 (`android_24_arm64_v8a`).
Do not use the desktop/server `install.sh` or a glibc Linux archive on this target.

1. Install the tools for repository setup:

   ```bash
   pkg install curl gnupg
   ```

2. Download the public key:

   ```bash
   mkdir -p "$PREFIX/etc/apt/keyrings"
   curl -fsSL \
     https://nastech-assets.nastech-agent.nastechresearch.workers.dev/releases/termux/stable/key.asc \
     -o "$PREFIX/etc/apt/keyrings/nastech-agent.asc"
   ```

3. Verify its primary fingerprint:

   ```bash
   gpg --show-keys --with-fingerprint "$PREFIX/etc/apt/keyrings/nastech-agent.asc"
   ```

   The repository key fingerprint is:

   ```text
   C572 B5FD D1A2 9CCF A9A9 12B6 840B 0848 E139 156D
   ```

   If the fingerprint differs, stop. Do not disable signature verification.

4. Add the repository:

   ```bash
   printf '%s\n' \
     "deb [signed-by=$PREFIX/etc/apt/keyrings/nastech-agent.asc] https://nastech-assets.nastech-agent.nastechresearch.workers.dev/releases/termux/stable nastech-stable main" \
     > "$PREFIX/etc/apt/sources.list.d/nastech-agent.list"
   ```

5. Install Nastech:

   ```bash
   pkg update
   pkg install nastech-agent
   ```

6. Configure a provider, then start the TUI:

   ```bash
   nastech setup
   nastech --tui
   ```

The `nastech`, `nastech-agent`, and `nastech-acp` commands use the packaged runtimes.
They do not require Termux's `python` or `nodejs` packages.

## Files and updates

| Contents | Location |
| --- | --- |
| Package files | `$PREFIX/lib/nastech-agent/` |
| Command symlinks | `$PREFIX/bin/nastech`, `$PREFIX/bin/nastech-agent`, `$PREFIX/bin/nastech-acp` |
| Configuration and user data | `~/.nastech/`, or the selected `NASTECH_HOME` |

Update through APT:

```bash
pkg update
pkg upgrade nastech-agent
```

`nastech update` refuses to modify an APT-owned installation.
It prints the package-manager command instead.
Canary versions contain `~canary.<timestamp>` and sort before the corresponding
stable version. Each suite only lists its own channel's packages; to move
between channels, edit the channel path and suite in `nastech-agent.list`, then
`pkg update && pkg upgrade nastech-agent`.

## Gateway

This APT installation does not use systemd, launchd, or Windows Scheduled Tasks.
Run the gateway in a Termux session:

```bash
nastech gateway run
```

For a background process:

```bash
mkdir -p "${NASTECH_HOME:-$HOME/.nastech}/logs"
nohup nastech gateway run >> "${NASTECH_HOME:-$HOME/.nastech}/logs/gateway.log" 2>&1 &
```

:::warning Android process limits
Android can suspend or terminate background Termux processes.
Battery optimization exemptions and `termux-wake-lock` can help, but do not guarantee persistent operation.
:::

## Limits

The package does not include the `nemo-relay` exporter. Its vendored build
toolchain does not support this target.

The package does not include Electron, local Chromium, or desktop computer-use
tools. A local Docker daemon is not part of the Termux environment. Remote
services have their own requirements and connectivity limits.

Phone-native Termux:API microphone and clipboard adapters are not provided by
this package path. The prebuilt CLI/TUI is not proof of local voice or wake-word
support. Optional integrations and third-party plugins can require dependencies
that do not support Android.

Python 3.14 on this target reports `sys.platform == "android"`. A dependency
or skill gated only to `linux` is not automatically available on Android.

## Uninstall

```bash
pkg uninstall nastech-agent
```

APT removes the package and its command symlinks. It preserves your configuration, sessions, skills, and memories.

## Troubleshooting

- **Package not found:** verify the repository entry, then run `pkg update`.
- **Signature error:** verify the public key fingerprint. Do not use an unsigned repository or bypass the error.
- **Missing command:** verify that `$PREFIX/bin` is on `PATH`, or reinstall the package.
- **Missing library or TUI bundle:** report `nastech --version` and the complete error. The core package must not require a local rebuild.
- **Gateway stops with the screen off:** review Android's battery and background-process limits.

For general diagnostics, run `nastech doctor`.
