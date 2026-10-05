"""A real published launcher driving a disposable CLI, without installing deps."""

from pathlib import Path
import shutil
import sys

from nastech_cli._launchers import mint_launcher


def publish_fixture_launcher(root: Path, main_source: str) -> Path:
    repository = Path(__file__).resolve().parents[1]
    package = root / "nastech_cli"
    package.mkdir(parents=True, exist_ok=True)
    (package / "__init__.py").touch()
    (package / "main.py").write_text(main_source, encoding="utf-8")
    # The application is a stand-in; launcher production and command queries
    # are real. The interpreter is external to the checkout, like PM's store.
    (root / "nastech_bootstrap.py").write_text("", encoding="utf-8")
    (root / "pm").mkdir(exist_ok=True)
    for relative in ("nastech_constants.py", "nastech_cli/_launchers.py", "pm/environments.py"):
        shutil.copyfile(repository / relative, root / relative)
    out = root / ".nastech" / "bin"
    out.mkdir(parents=True)
    launcher = mint_launcher("nastech", root, out, Path(sys.executable), None)
    assert launcher is not None
    assert not (root / "venv").exists()
    return launcher