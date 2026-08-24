from pathlib import Path


def test_windows_native_install_path_docs_match_installer() -> None:
    doc = Path("website/docs/user-guide/windows-native.md").read_text()
    install = Path("scripts/install.ps1").read_text()

    # The launchers live in the managed binary dir OUTSIDE the git checkout
    # (NASTECH_HOME\bin, next to the managed uv) — NOT the whole venv\Scripts
    # (which would shadow the user's python, #83797) and NOT a dir inside
    # the checkout (which `nastech update`'s autostash swept off disk).
    assert "%LOCALAPPDATA%\\nastech\\bin" in doc
    assert (
        "Get-Command nastech        # should print "
        "C:\\Users\\<you>\\AppData\\Local\\nastech\\bin\\nastech.exe"
    ) in doc
    # Installer exposes $NastechHome\bin, and must copy the launchers into it.
    assert '$nastechBin = "$NastechHome\\bin"' in install
    assert "nastech.exe" in install and "nastech-acp.exe" in install
    # Guard against regressions to either legacy layout.
    assert '$nastechBin = "$InstallDir\\venv\\Scripts"' not in install
    assert '$nastechBin = "$InstallDir\\bin"' not in install
