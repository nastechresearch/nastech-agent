"""persistence.sqlite._schema and _schema_ddl stand alone: the DDL carries the table text the updater and gateway downgrade guards look for, and importing both modules loads none of the ``nastech_state`` store or mixin modules.
"""

import subprocess
import sys
from pathlib import Path

from nastech_cli.update_downgrade_guard import _RUNTIME_SCHEMA_MARKER
from persistence.sqlite import _schema, _schema_ddl


def test_downgrade_guard_marker_present():
    # The updater and gateway downgrade guards recognise a tree with the runtime ledger by this statement.
    assert _RUNTIME_SCHEMA_MARKER in _schema_ddl.SCHEMA_SQL


def test_imports_no_legacy_store_or_mixin_module():
    probe = (
        "import sys, persistence.sqlite._schema, persistence.sqlite._schema_ddl\n"
        "mixins = ('nastech_state', 'nastech_state_schema', 'nastech_state_fts', 'nastech_state_search',"
        " 'nastech_state_titles', 'nastech_state_gateway', 'nastech_state_sessions', 'nastech_state_messages')\n"
        "print(sorted(m for m in mixins if m in sys.modules))\n"
    )
    root = Path(_schema.__file__).resolve().parents[2]
    result = subprocess.run([sys.executable, "-c", probe], cwd=root, capture_output=True, text=True, check=True)
    assert result.stdout.strip() == "[]"
