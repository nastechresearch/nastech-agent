"""Cheap source-driver checks: real shells, disposable installs, no installer."""
import hashlib
import json
import os
from pathlib import Path
import runpy
import shutil
import subprocess
import sys
import sysconfig

import pytest


ASSETS = Path(__file__).resolve().parents[1] / "install/e2e-assets"


@pytest.mark.platforms("posix")
def test_shell_selects_the_installed_command_not_the_phase_or_path(tmp_path):
    root = tmp_path / "installed source"
    legacy = root / "venv/bin/nastech"
    published = root / ".nastech/bin/nastech"
    for command, label in ((legacy, "legacy"), (published, "published")):
        command.parent.mkdir(parents=True)
        command.write_text(f'#!/bin/sh\nprintf "{label}:%s\\n" "$*"\n', encoding="utf-8")
        command.chmod(0o755)
    env = dict(os.environ, INSTALL_DIR=str(root), ASSETS=str(ASSETS), HOME=str(tmp_path))
    result = subprocess.run(["bash", "-euc", '''
source "$ASSETS/source-driver.sh"
command=$(source_nastech "$INSTALL_DIR")
"$command" 'literal argument'
rm "$INSTALL_DIR/venv/bin/nastech"
test "$(source_nastech "$INSTALL_DIR")" = "$command"
printf '#!/bin/sh\nexit 23\n' > "$command"
"$command" || test "$?" = 23
rm "$command"
if source_nastech "$INSTALL_DIR"; then exit 91; fi
printf '#!/bin/sh\nprintf legacy\n' > "$INSTALL_DIR/venv/bin/nastech"
chmod +x "$INSTALL_DIR/venv/bin/nastech"
"$(source_nastech "$INSTALL_DIR")"
# A PM checkout cannot hide missing publication behind its old venv.
mkdir -p "$INSTALL_DIR/pm"
printf '{}' > "$INSTALL_DIR/pm/lock.json"
if source_nastech "$INSTALL_DIR"; then exit 92; fi
'''], env=env, cwd=tmp_path, capture_output=True, text=True, timeout=30, check=False)
    assert result.returncode == 0, result.stdout + result.stderr
    assert result.stdout.splitlines() == ["published:literal argument", "legacy"]


@pytest.mark.platforms("posix")
def test_installer_marker_is_the_only_dirty_state_a_driver_accepts(tmp_path):
    root = tmp_path / "installed source"
    root.mkdir()
    git = ["git", "-C", str(root), "-c", "user.name=t", "-c", "user.email=t@t"]
    subprocess.run([*git, "init", "-q"], check=True)
    (root / "tracked").write_text("v1\n", encoding="utf-8")
    subprocess.run([*git, "add", "tracked"], check=True)
    subprocess.run([*git, "commit", "-qm", "base"], check=True)
    (root / ".install_method").write_text("git\n", encoding="utf-8")
    env = dict(os.environ, INSTALL_DIR=str(root), ASSETS=str(ASSETS), HOME=str(tmp_path))

    def accept():
        return subprocess.run(["bash", "-euc", 'source "$ASSETS/source-driver.sh"; accept_installer_marker "$INSTALL_DIR"'],
                              env=env, capture_output=True, text=True, timeout=30, check=False)

    assert accept().returncode == 0
    assert (root / ".install_method").read_text(encoding="utf-8") == "git\n"
    assert subprocess.run([*git, "status", "--porcelain", "--untracked-files=all"],
                          capture_output=True, text=True, check=True).stdout == ""
    (root / "tracked").write_text("edited\n", encoding="utf-8")
    refused = accept()
    assert refused.returncode != 0 and "M tracked" in refused.stderr


@pytest.mark.platforms("windows", "posix")
def test_powershell_selects_exact_exe_or_cmd_and_legacy_fallback(tmp_path):
    # These are file-selection rules, not Windows execution emulation. Run
    # them in real PowerShell on any host that supplies it (native CI included).
    path = os.pathsep.join(p for p in os.get_exec_path() if ".nastech" not in Path(p).parts)
    pwsh = shutil.which("pwsh", path=path) or shutil.which("powershell", path=path)
    if not pwsh:
        if os.name == "nt":
            pytest.fail("native Windows acceptance requires PowerShell")
        pytest.skip("PowerShell is not available on this host")
    root = tmp_path / "installed source"
    root.mkdir()
    harness = tmp_path / "probe.ps1"
    harness.write_text('''$ErrorActionPreference = 'Stop'
. (Join-Path $env:ASSETS 'source-driver.ps1')
$root = $env:INSTALL_DIR
$legacy = Join-Path $root 'venv/Scripts/nastech.exe'
$exe = Join-Path $root '.nastech/bin/nastech.exe'
$cmd = Join-Path $root '.nastech/bin/nastech.cmd'
New-Item -ItemType Directory -Path (Split-Path $legacy), (Split-Path $exe) -Force | Out-Null
Set-Content $legacy 'legacy'
if ((Get-SourceNastech $root) -ne $legacy) { throw 'legacy fallback' }
Set-Content $cmd 'cmd'
if ((Get-SourceNastech $root) -ne $cmd) { throw 'published cmd' }
Set-Content $exe 'exe'
if ((Get-SourceNastech $root) -ne $exe) { throw 'exe precedence' }
Remove-Item $legacy
if ((Get-SourceNastech $root) -ne $exe) { throw 'requires legacy venv' }
Remove-Item $exe, $cmd
$refused = $false
try { Get-SourceNastech $root } catch { $refused = $true }
if (-not $refused) { throw 'missing command accepted' }
Set-Content $legacy 'stale legacy'
New-Item -ItemType Directory -Path (Join-Path $root 'pm') | Out-Null
Set-Content (Join-Path $root 'pm/lock.json') '{}'
$refused = $false
try { Get-SourceNastech $root } catch { $refused = $true }
if (-not $refused) { throw 'missing PM launcher accepted' }
Write-Output 'selection verified'
''', encoding="utf-8")
    result = subprocess.run([pwsh, "-NoProfile", "-NonInteractive", "-File", str(harness)],
                            env=dict(os.environ, INSTALL_DIR=str(root), ASSETS=str(ASSETS), HOME=str(tmp_path)),
                            cwd=tmp_path, capture_output=True, text=True, timeout=30, check=False)
    assert result.returncode == 0, result.stdout + result.stderr
    assert result.stdout.strip() == "selection verified"


def test_observer_preserves_no_desktop_and_refuses_incomplete_app(tmp_path):
    verify = runpy.run_path(str(ASSETS / "source_driver.py"))["verify_products"]
    root = tmp_path / "source"
    root.mkdir()
    verify(root, "absent")
    assert list(root.iterdir()) == []
    with pytest.raises(RuntimeError, match="desktop"):
        verify(root, "present")
    release = root / "apps/desktop/release/linux-unpacked"
    release.mkdir(parents=True)
    (release / "nastech").write_bytes(b"incomplete fixture")
    with pytest.raises(RuntimeError, match="desktop"):
        verify(root, "absent")
    with pytest.raises(RuntimeError, match="desktop"):
        verify(root, "present")
    assert (release / "nastech").read_bytes() == b"incomplete fixture"


@pytest.mark.platforms("posix")
@pytest.mark.parametrize("fault,error", [
    ("uv-lock", "dependency generation is not current"),
    ("no-desktop", "dependency generation is not current"),
    ("foreign-launcher", "belongs to another installation"),
    ("missing-launcher", ""),
    ("incomplete", "incomplete"),
    ("web-changed", "web output"), ("web-missing", "web output"),
])
def test_pm_observer_accepts_ready_fixture_and_leaves_failed_fixture_untouched(tmp_path, fault, error):
    # This exercises the complete observer process, not a whole install. The
    # fixture borrows prepared test dependencies and records real PM input
    # stamps / compiler receipts. It never resolves or acquires a package.
    repo = ASSETS.parents[2]
    root = tmp_path / "source"
    for directory in ("pm", "nastech_cli"):
        shutil.copytree(repo / directory, root / directory, ignore=shutil.ignore_patterns("__pycache__"))
    shutil.copy2(repo / "nastech_constants.py", root / "nastech_constants.py")
    (root / "nastech_bootstrap.py").write_text("raise RuntimeError('bootstrap must not run')", encoding="utf-8")
    (root / "uv.lock").write_text("fixture locked graph", encoding="utf-8")
    home = tmp_path / "home"
    store = tmp_path / "store"
    env = dict(os.environ, HOME=str(home), NASTECH_HOME=str(home), NASTECH_RUNTIME_DIR=str(store),
               PYTHONDONTWRITEBYTECODE="1", NASTECH_DISABLE_LAZY_INSTALLS="1")
    env.pop("NASTECH_INSTALL_ROOT", None)
    path = os.pathsep.join(p for p in os.get_exec_path() if ".nastech" not in Path(p).parts)
    node = shutil.which("node", path=path)
    assert node
    setup = '''import sys
from pathlib import Path
root, store, node, deps = map(Path, sys.argv[1:])
sys.path.insert(0, str(root))
from pm.lock import Facts, Lockfile
from pm.packages import Venv
from pm.environments import install_state_dir, runtime_facts_path, site_packages
from nastech_cli._launchers import ensure_install_launchers
lock = Lockfile(root / 'pm/lock.json')
lock.set_pin('node', 'fixture', {})
lock.save()
for name, executable in [('python', Path(sys.executable)), ('node', node)]:
    binary = store / name / 'bin' / ('python3' if name == 'python' else name)
    binary.parent.mkdir(parents=True)
    binary.symlink_to(executable)
    Facts(store / 'facts.json').record(name, 'fixture', name, {}, store)
selected = install_state_dir(root) / 'environments/fixture/venv'
selected.mkdir(parents=True)
(selected / 'pyvenv.cfg').write_text('home = fixture')
site = site_packages(selected)
site.parent.mkdir(parents=True)
site.symlink_to(deps, target_is_directory=True)
Facts(runtime_facts_path(root)).record_state('venv', Venv(root).expected_stamp([]), [], environment=selected)
ensure_install_launchers(root, root / '.nastech/bin')
'''
    subprocess.run([sys.executable, "-I", "-B", "-c", setup, str(root), str(store), node,
                    sysconfig.get_path("purelib")], env=env, cwd=tmp_path, check=True, timeout=60)
    build = root / "scripts/build"
    build.mkdir(parents=True)
    for name in ("freshness.mjs", "frontend-common.mjs"):
        shutil.copy2(repo / "scripts/build" / name, build / name)
    record = '''import { mkdirSync, writeFileSync } from 'node:fs';
import { buildInputs, recordProduct } from './scripts/build/freshness.mjs';
const source = process.cwd();
for (const [product, out] of [['tui', 'ui-tui/dist'], ['web', 'nastech_cli/web_dist'], ['desktop', 'apps/desktop/release/linux-unpacked/resources/app.asar.unpacked/dist']]) {
  mkdirSync(out, { recursive: true }); writeFileSync(out + '/index.html', 'fixture product');
  recordProduct({source, product, out, inputs: buildInputs(source, product)});
}
'''
    subprocess.run([node, "--input-type=module", "-e", record], cwd=root, env=env, check=True, timeout=30)
    (root / "apps/desktop/release/linux-unpacked/nastech").write_bytes(b"fixture executable")
    command = [sys.executable, "-B", str(ASSETS / "source_driver.py"), "--root", str(root),
               "--launcher", str(root / ".nastech/bin/nastech"), "--desktop", "present"]
    if fault == "no-desktop":
        shutil.rmtree(root / "apps/desktop")
        command[-1] = "absent"
    # The passive query must not write even import caches: -I ignores the
    # environment's bytecode switch, so the published query enforces it.
    def snapshot():
        return {p: (hashlib.sha256(p.read_bytes()).hexdigest(), p.stat().st_mtime_ns) for tree in (root, home, store)
                for p in tree.rglob("*") if p.is_file()}
    before = snapshot()
    result = subprocess.run(command, env=env, cwd=tmp_path, capture_output=True, text=True, timeout=60, check=False)
    assert result.returncode == 0, result.stdout + result.stderr
    assert snapshot() == before
    if fault in {"uv-lock", "no-desktop"}:
        (root / "uv.lock").write_text("changed graph without preparation", encoding="utf-8")
    elif fault == "foreign-launcher":
        foreign = tmp_path / "foreign"
        shutil.copytree(root, foreign)
        from nastech_cli._launchers import mint_launcher
        launcher = mint_launcher("nastech", foreign, root / ".nastech/bin", Path(sys.executable), None)
        assert launcher is not None
    elif fault == "missing-launcher":
        (root / ".nastech/bin/nastech").unlink()
    elif fault == "incomplete":
        (root / ".update-incomplete").write_text("incomplete", encoding="utf-8")
    else:
        damaged = root / "nastech_cli/web_dist/index.html"
        if fault == "web-missing":
            damaged.unlink()
        else:
            damaged.write_bytes(b"damaged")
    before = snapshot()
    result = subprocess.run(command, env=env, cwd=tmp_path, capture_output=True, text=True, timeout=60, check=False)
    assert result.returncode != 0
    assert error in result.stderr
    assert "bootstrap must not run" not in result.stderr
    assert snapshot() == before