# Behavioral test for install.ps1's dedicated Nastech launcher directory.
#
# Run: powershell.exe -NoProfile -File scripts/ci/test_install_ps1_cli_launchers.ps1
#
# The test lifts the real Install-NastechCommandLaunchers function from the
# PowerShell AST and executes it against a temporary install tree. It never
# reads or changes the user's PATH.

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$installPs1 = Join-Path (Join-Path $PSScriptRoot '..') 'install.ps1' | Resolve-Path
$ast = [System.Management.Automation.Language.Parser]::ParseFile(
    $installPs1, [ref]$null, [ref]$null)

$fn = $ast.Find({
    param($n)
    $n -is [System.Management.Automation.Language.FunctionDefinitionAst] -and
    $n.Name -eq 'Install-NastechCommandLaunchers'
}, $true)

if (-not $fn) {
    throw "Install-NastechCommandLaunchers not found in $installPs1"
}

Invoke-Expression $fn.Extent.Text

$tempBase = [System.IO.Path]::GetFullPath([System.IO.Path]::GetTempPath())
$caseRoot = [System.IO.Path]::GetFullPath((Join-Path $tempBase (
    'nastech-cli-launcher-test-' + [guid]::NewGuid().ToString('N')
)))
if (-not $caseRoot.StartsWith($tempBase, [System.StringComparison]::OrdinalIgnoreCase)) {
    throw "Refusing to create test directory outside the system temp directory: $caseRoot"
}

$script:Failures = 0

function Assert-True {
    param([bool]$Condition, [string]$Name)
    if ($Condition) {
        Write-Host "  PASS  $Name"
    } else {
        Write-Host "  FAIL  $Name"
        $script:Failures++
    }
}

function Assert-BytesEqual {
    param([byte[]]$Expected, [byte[]]$Actual, [string]$Name)
    $same = $Expected.Length -eq $Actual.Length
    if ($same) {
        for ($i = 0; $i -lt $Expected.Length; $i++) {
            if ($Expected[$i] -ne $Actual[$i]) {
                $same = $false
                break
            }
        }
    }
    Assert-True $same $Name
}

try {
    New-Item -ItemType Directory -Force -Path $caseRoot | Out-Null

    $missingThrew = $false
    try {
        Install-NastechCommandLaunchers -Root $caseRoot | Out-Null
    } catch {
        $missingThrew = $_.Exception.Message -like '*required launcher not found*'
    }
    Assert-True $missingThrew 'missing nastech.exe fails the launcher stage'
    Assert-True (-not (Test-Path -LiteralPath (Join-Path $caseRoot 'bin'))) `
        'failure does not create an empty PATH directory'

    $scriptsDir = Join-Path $caseRoot 'venv\Scripts'
    New-Item -ItemType Directory -Force -Path $scriptsDir | Out-Null
    $nastechV1 = [byte[]](77, 90, 1)
    $nastechV2 = [byte[]](77, 90, 2)
    $acp = [byte[]](77, 90, 3)
    [System.IO.File]::WriteAllBytes((Join-Path $scriptsDir 'nastech.exe'), $nastechV1)

    $binDir = Install-NastechCommandLaunchers -Root $caseRoot
    Assert-BytesEqual $nastechV1 `
        ([System.IO.File]::ReadAllBytes((Join-Path $binDir 'nastech.exe'))) `
        'required launcher is copied into the dedicated bin directory'
    Assert-True (-not (Test-Path -LiteralPath (Join-Path $binDir 'nastech-acp.exe'))) `
        'optional ACP launcher may be absent'

    [System.IO.File]::WriteAllBytes((Join-Path $scriptsDir 'nastech.exe'), $nastechV2)
    [System.IO.File]::WriteAllBytes((Join-Path $scriptsDir 'nastech-acp.exe'), $acp)
    Install-NastechCommandLaunchers -Root $caseRoot | Out-Null
    Assert-BytesEqual $nastechV2 `
        ([System.IO.File]::ReadAllBytes((Join-Path $binDir 'nastech.exe'))) `
        'installer refreshes an existing Nastech launcher'
    Assert-BytesEqual $acp `
        ([System.IO.File]::ReadAllBytes((Join-Path $binDir 'nastech-acp.exe'))) `
        'installer copies the optional ACP launcher when present'
} finally {
    if (Test-Path -LiteralPath $caseRoot) {
        $resolvedCase = [System.IO.Path]::GetFullPath($caseRoot)
        if (-not $resolvedCase.StartsWith($tempBase, [System.StringComparison]::OrdinalIgnoreCase)) {
            throw "Refusing to remove test directory outside the system temp directory: $resolvedCase"
        }
        Remove-Item -LiteralPath $resolvedCase -Recurse -Force
    }
}

if ($script:Failures -gt 0) {
    Write-Host ""
    Write-Host "$script:Failures assertion(s) failed"
    exit 1
}

Write-Host ""
Write-Host "all assertions passed"
