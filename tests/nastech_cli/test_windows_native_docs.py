from pathlib import Path


def test_windows_native_install_path_docs_match_installer() -> None:
    doc = Path("website/docs/user-guide/windows-native.md").read_text()
    install = Path("scripts/install.ps1").read_text()

    # The launchers live in a dedicated bin/ dir on PATH — NOT the whole
    # venv\Scripts (which would shadow the user's python, #83797).
    assert "%LOCALAPPDATA%\\nastech\\nastech-agent\\bin" in doc
    assert (
        "Get-Command nastech        # should print "
        "C:\\Users\\<you>\\AppData\\Local\\nastech\\nastech-agent\\bin\\nastech.exe"
    ) in doc
    # Installer exposes $InstallDir\bin, and must copy the launchers into it.
    assert '$nastechBin = "$InstallDir\\bin"' in install
    assert "nastech.exe" in install and "nastech-acp.exe" in install
    # Guard against a regression back to putting venv\Scripts on PATH.
    assert '$nastechBin = "$InstallDir\\venv\\Scripts"' not in install
