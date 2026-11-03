#!/data/data/com.termux/files/usr/bin/bash
# Verify the signed repository with the same non-root APT used on a phone.
set -euo pipefail
export PREFIX=/data/data/com.termux/files/usr
export PATH="$PREFIX/bin:$PATH"
suite="${1:?APT suite required}"
expected="${2:?expected package version required}"
# The feed is published FLAT as the assets of one fixed-tag release (a release
# asset name cannot hold '/'), which is why the source line below carries no
# suite or component and no `by-hash`: apt reads <repository>/./InRelease and
# <repository>/./Packages.gz.  See scripts/termux/release_apt.py for the layout
# and the measurements behind it.  The default is what a phone is told to use.
repository="${3:-https://github.com/nastechresearch/nastech-agent/releases/download/termux-repo}"
ctmp=/tmp  # no-tmp: ok — where the caller mounts validate_installed.py inside this container
work="$(mktemp -d "$PREFIX/tmp/nastech-apt-proof.XXXXXX")"
trap 'rm -rf "$work"' EXIT
mkdir -p "$work/lists/partial" "$work/archives/partial"
# The feed directory is mounted read-only at /apt by every caller, so the suite
# that was staged is checked against the suite that is published: a channel wired
# to the wrong feed would otherwise install over another channel's packages.
grep -qx "Suite: $suite" /apt/Release
printf 'deb [signed-by=/apt/key.asc] %s ./\n' "$repository" > "$work/sources.list"
apt_options=(
    -o "Dir::Etc::sourcelist=$work/sources.list"
    -o "Dir::Etc::sourceparts=-"
    -o "Dir::State::lists=$work/lists"
    -o "Dir::Cache::archives=$work/archives"
    -o "DPkg::Options::=--force-not-root"
    -o "DPkg::Options::=--force-script-chrootless"
)
mkdir -p "$work/state"
printf 'user data survives package replacement\n' > "$work/state/sentinel"
export NASTECH_HOME="$work/state"
if [ -f /previous.deb ]; then
    dpkg --force-not-root --force-script-chrootless --install /previous.deb
    previous="$(dpkg-query -W -f='${Version}' nastech-agent)"
    dpkg --compare-versions "$expected" gt "$previous"
fi
apt-get "${apt_options[@]}" update
apt-get "${apt_options[@]}" --yes install nastech-agent
actual="$(dpkg-query -W -f='${Version}' nastech-agent)"
[ "$actual" = "$expected" ]
[ "$(cat "$work/state/sentinel")" = 'user data survives package replacement' ]
root="$PREFIX/lib/nastech-agent"
export LD_LIBRARY_PATH="$root/tools/python$PREFIX/lib:$root/tools/node$PREFIX/lib:$root/tools/ffmpeg$PREFIX/lib:$root/runtime-libs/lib:$PREFIX/lib"
export PYTHONPATH="$root/app"
"$root/venv/bin/python" "$ctmp/validate_installed.py"
printf 'SIGNED_APT_INSTALL_OK %s\n' "$actual"
if [ -f /previous.deb ]; then
    printf 'SIGNED_APT_UPGRADE_OK %s -> %s\n' "$previous" "$actual"
fi
