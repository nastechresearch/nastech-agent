# PROBE BRANCH ONLY (wine2e/r6-lock-probe) — never merged.
#
# The #196 arm64 lane showed the hand-off's R6 guard answer "free" one second into a live
# Python holder, then answer "held" on the retry of the same test on the same machine. This
# script puts every probe shape and every handle shape against one known-live holder and
# prints what each of them actually sees, with the Win32 error code.
#
# Run under both hosts: the hand-off runs Windows PowerShell 5.1 (.NET Framework), CI steps
# often run pwsh 7 (.NET Core) — if the two disagree, the host is the variable.
$ErrorActionPreference = 'Stop'

$AddType = @'
using System;
using System.IO;
using System.Runtime.InteropServices;
using System.Text;
using Microsoft.Win32.SafeHandles;

public static class R6Probe {
    [StructLayout(LayoutKind.Sequential)]
    public struct OVERLAPPED {
        public IntPtr Internal; public IntPtr InternalHigh;
        public int Offset; public int OffsetHigh; public IntPtr hEvent;
    }
    [DllImport("kernel32.dll", CharSet=CharSet.Unicode, SetLastError=true)]
    static extern IntPtr CreateFileW(string name, uint access, uint share, IntPtr sa, uint disp, uint flags, IntPtr tpl);
    [DllImport("kernel32.dll", SetLastError=true)]
    static extern bool LockFileEx(IntPtr h, uint flags, uint reserved, uint countLow, uint countHigh, ref OVERLAPPED ov);
    [DllImport("kernel32.dll", SetLastError=true)]
    static extern bool UnlockFileEx(IntPtr h, uint reserved, uint countLow, uint countHigh, ref OVERLAPPED ov);
    [DllImport("kernel32.dll", SetLastError=true)]
    static extern bool CloseHandle(IntPtr h);

    const uint GENERIC_READ = 0x80000000;
    const uint GENERIC_WRITE = 0x40000000;
    const uint SHARE_ALL = 0x00000007;
    const uint OPEN_EXISTING = 3;
    const uint FAIL_IMMEDIATELY = 0x00000001;
    const uint EXCLUSIVE = 0x00000002;
    const long OWNER = 1048576;
    const uint SPAN = 17;

    static OVERLAPPED At(long offset) {
        OVERLAPPED ov = new OVERLAPPED();
        ov.Offset = (int)(offset & 0xFFFFFFFFL);
        ov.OffsetHigh = (int)((offset >> 32) & 0xFFFFFFFFL);
        return ov;
    }

    static string Err(string verdict) {
        int code = Marshal.GetLastWin32Error();
        return verdict + " win32=" + code;
    }

    // .NET FileStream.Lock over the owner byte plus all 16 lease bytes, as marker.ps1 does.
    public static string DotNetLock(string path, bool writable) {
        IntPtr raw = CreateFileW(path, writable ? (GENERIC_READ | GENERIC_WRITE) : GENERIC_READ,
            SHARE_ALL, IntPtr.Zero, OPEN_EXISTING, 0, IntPtr.Zero);
        if (raw == IntPtr.Zero || (long)raw == -1L) return "open-failed " + Err("");
        SafeFileHandle h = new SafeFileHandle(raw, true);
        FileStream fs = null;
        try {
            fs = new FileStream(h, writable ? FileAccess.ReadWrite : FileAccess.Read);
            try {
                fs.Lock(OWNER, (int)SPAN);
                try { fs.Unlock(OWNER, (int)SPAN); } catch {}
                return "free";
            } catch (Exception e) {
                return "held " + e.GetType().Name;
            }
        } catch (Exception e) {
            return "stream-failed " + e.GetType().Name + ": " + e.Message;
        } finally {
            if (fs != null) fs.Dispose();
            else h.Dispose();
        }
    }

    // Raw Win32, both modes, both handle rights — the CRT's msvcrt.locking is an exclusive
    // LockFile, update_lock._try_shared_lock is a shared LockFileEx with FAIL_IMMEDIATELY.
    public static string Win32(string path, bool writable, bool exclusive) {
        IntPtr raw = CreateFileW(path, writable ? (GENERIC_READ | GENERIC_WRITE) : GENERIC_READ,
            SHARE_ALL, IntPtr.Zero, OPEN_EXISTING, 0, IntPtr.Zero);
        if (raw == IntPtr.Zero || (long)raw == -1L) return "open-failed " + Err("");
        try {
            uint flags = FAIL_IMMEDIATELY | (exclusive ? EXCLUSIVE : 0u);
            OVERLAPPED ov = At(OWNER);
            if (LockFileEx(raw, flags, 0, SPAN, 0, ref ov)) {
                UnlockFileEx(raw, 0, SPAN, 0, ref ov);
                return "free";
            }
            return Err("held");
        } catch (Exception e) {
            return "call-failed " + e.GetType().Name;
        } finally {
            CloseHandle(raw);
        }
    }
}
'@

Add-Type -TypeDefinition $AddType -ErrorAction Stop

function Invoke-Probes([string]$LockPath) {
    $script:InstallRoot = Split-Path -Parent $LockPath
    $answers = @()
    for ($i = 0; $i -lt 10; $i++) { $answers += (Test-CheckoutLockHeld) }
    $seen = ($answers | Where-Object { $_ }).Count
    "  marker.ps1 Test-CheckoutLockHeld : $seen/10 held"
    "  dotnet FileStream.Lock  read    : $([R6Probe]::DotNetLock($LockPath, $false))"
    "  dotnet FileStream.Lock  readwri : $([R6Probe]::DotNetLock($LockPath, $true))"
    "  LockFileEx exclusive    read    : $([R6Probe]::Win32($LockPath, $false, $true))"
    "  LockFileEx exclusive    readwri : $([R6Probe]::Win32($LockPath, $true, $true))"
    "  LockFileEx shared       read    : $([R6Probe]::Win32($LockPath, $false, $false))"
    "  LockFileEx shared       readwri : $([R6Probe]::Win32($LockPath, $true, $false))"
    "  python checkout_lock_held       : $(python (Join-Path $env:GITHUB_WORKSPACE 'scripts/desktop-update/r6_py_probe.py') $script:InstallRoot)"
}

# A holder in the commit-outcome test's exact shape: one byte at 1 MiB via msvcrt.locking.
$HolderSrc = @'
import msvcrt, os, sys, time
fd = os.open(sys.argv[1], os.O_RDWR | os.O_CREAT | os.O_BINARY, 0o644)
os.lseek(fd, 1 << 20, os.SEEK_SET)
msvcrt.locking(fd, msvcrt.LK_NBLCK, int(sys.argv[3]))
open(sys.argv[2], 'w', encoding='utf-8').write('locked')
time.sleep(300)
'@
# A real production owner: update_lock._acquire_checkout, which locks the owner byte and
# keeps the fd, exactly as `nastech update` does on a user's machine.
$ProdSrc = @'
import sys, time
sys.path.insert(0, sys.argv[3])
from pathlib import Path
from nastech_cli import update_lock
holder = update_lock._acquire_checkout(Path(sys.argv[1]))
Path(sys.argv[2]).write_text(
    str(update_lock.checkout_lock_path(sys.argv[1])) + ' holder=' + repr(holder), encoding='utf-8')
time.sleep(300)
'@

$root = Join-Path $env:RUNNER_TEMP 'r6-matrix'
if (Test-Path $root) { Remove-Item -Recurse -Force $root }
New-Item -ItemType Directory -Force -Path $root | Out-Null
$holderPy = Join-Path $root 'holder.py'
$prodPy = Join-Path $root 'prod.py'
Set-Content -LiteralPath $holderPy -Value $HolderSrc -Encoding utf8
Set-Content -LiteralPath $prodPy -Value $ProdSrc -Encoding utf8

. (Join-Path $env:GITHUB_WORKSPACE 'scripts/desktop-update/marker.ps1')

"host              = $($PSVersionTable.PSVersion) / $([System.Environment]::Version)"
''
'=== control: the lock file exists, nobody holds it ==='
$lockPath = Join-Path $root '.nastech-update.lock'
Set-Content -LiteralPath $lockPath -Value '' -Encoding ascii
Invoke-Probes $lockPath

''
'=== holder 1: the test shape (msvcrt.locking, 1 byte at 1 MiB) ==='
$ready = Join-Path $root 'ready-1'
$p1 = Start-Process python -ArgumentList $holderPy, $lockPath, $ready, '1' -PassThru -NoNewWindow
for ($i = 0; $i -lt 200 -and -not (Test-Path $ready); $i++) { Start-Sleep -Milliseconds 100 }
if (-not (Test-Path $ready)) { throw 'holder 1 never took the lock' }
Start-Sleep -Seconds 1
"holder alive      = $(-not $p1.HasExited)"
Invoke-Probes $lockPath

''
'=== holder 2: production update_lock._acquire_checkout ==='
if (-not $p1.HasExited) { Stop-Process -Id $p1.Id -Force; $p1.Wait() }
Remove-Item -LiteralPath $ready -Force
$ready2 = Join-Path $root 'ready-2'
$p2 = Start-Process python -ArgumentList $prodPy, $root, $ready2, $env:GITHUB_WORKSPACE -PassThru -NoNewWindow
for ($i = 0; $i -lt 200 -and -not (Test-Path $ready2); $i++) { Start-Sleep -Milliseconds 100 }
if (-not (Test-Path $ready2)) { throw 'holder 2 never reported' }
"production claim  = $(Get-Content -LiteralPath $ready2 -Raw)"
Invoke-Probes (Get-CheckoutLockPath)

''
'=== holder 3: production owner, re-probed after 5 s (does the answer drift?) ==='
Start-Sleep -Seconds 5
Invoke-Probes (Get-CheckoutLockPath)

if (-not $p2.HasExited) { Stop-Process -Id $p2.Id -Force }
