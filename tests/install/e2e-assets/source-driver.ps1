# Dot-source only. Prefer the published command; never rescue a broken one
# through PATH, the user's shared bin, or an obsolete checkout venv.
function Get-SourceNastech([string]$Root) {
    foreach ($name in @('nastech.exe', 'nastech.cmd')) {
        $command = Join-Path $Root ".nastech/bin/$name"
        if (Test-Path -LiteralPath $command) {
            if (-not (Test-Path -LiteralPath $command -PathType Leaf)) {
                throw "Invalid published launcher: $command"
            }
            return $command
        }
    }
    if (Test-Path -LiteralPath (Join-Path $Root 'pm/lock.json')) {
        throw "Missing published launcher under $Root/.nastech/bin"
    }
    $legacy = Join-Path $Root 'venv/Scripts/nastech.exe'
    if (Test-Path -LiteralPath $legacy -PathType Leaf) { return $legacy }
    throw "No installed Nastech command under $Root"
}

# Hand out a command to DRIVE the next ordinary startup, even when the
# published launcher is not there yet.
#
# A pre-handoff release cannot flip during `nastech update` -- there is no
# retired-hook seam on its update path to reach, so the update ends with the
# tree at HEAD and no `.nastech/bin/*`. The NEXT ordinary startup is what
# completes it: nastech_bootstrap calls prepare_launch() before importing
# anything, which syncs PM, publishes the launchers and re-execs.
#
# Deliberately NOT used for `--version` probes: those stay under
# NASTECH_DISABLE_LAZY_INSTALLS so a probe can never complete an unfinished
# update. Only a real startup may heal.
function Get-SourceNastechForStartup([string]$Root) {
    foreach ($name in @('nastech.exe', 'nastech.cmd')) {
        $published = Join-Path $Root ".nastech/bin/$name"
        if (Test-Path -LiteralPath $published -PathType Leaf) { return $published }
    }
    $legacy = Join-Path $Root 'venv/Scripts/nastech.exe'
    if (Test-Path -LiteralPath $legacy -PathType Leaf) { return $legacy }
    throw "No installed Nastech command to start under $Root"
}
