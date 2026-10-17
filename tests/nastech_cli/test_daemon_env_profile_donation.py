"""A named-profile client that auto-starts the host daemon never donates its own dotenv to it (N43)."""
import json
import os
from pathlib import Path
import sys
import time

import pytest


@pytest.mark.platforms("linux")
@pytest.mark.spawns_gateway_lookalike  # stub interpreter records env then exits; reaped below
def test_host_daemon_does_not_inherit_named_profile_dotenv(tmp_path, monkeypatch):
    from nastech_cli import gateway_runtime_start as start
    from nastech_cli.env_loader import load_nastech_dotenv
    root = tmp_path / 'root'
    work = root / 'profiles' / 'work'
    work.mkdir(parents=True, mode=0o700)
    (root / '.env').write_text('OPENROUTER_API_KEY=root-key\n', encoding='utf-8')
    (work / '.env').write_text('TELEGRAM_BOT_TOKEN=work-bot-token\nOPENROUTER_API_KEY=work-key\n'
                               'NASTECH_LANGUAGE=fr\n', encoding='utf-8')
    for key in ('TELEGRAM_BOT_TOKEN', 'OPENROUTER_API_KEY', 'NASTECH_LANGUAGE'):
        monkeypatch.delenv(key, raising=False)
    # The `nastech -p work` client: its process home is the profile and its .env is in os.environ.
    monkeypatch.setenv('NASTECH_HOME', str(work))
    load_nastech_dotenv(nastech_home=work)
    assert os.environ['TELEGRAM_BOT_TOKEN'] == 'work-bot-token'
    monkeypatch.setenv('SHELL_INJECTED_SETTING', 'kept')
    witness = tmp_path / 'env.json'
    executable = tmp_path / 'owned-interpreter'
    names = ['TELEGRAM_BOT_TOKEN', 'OPENROUTER_API_KEY', 'NASTECH_LANGUAGE', 'NASTECH_HOME', 'SHELL_INJECTED_SETTING']
    executable.write_text(
        '#!' + sys.executable + '\nimport json, os\n'
        + f'open({str(witness)!r}, "w").write(json.dumps('
        + '{k: os.environ.get(k) for k in ' + repr(names) + '}))\n', encoding='utf-8')
    executable.chmod(0o700)
    monkeypatch.setattr(sys, 'executable', str(executable))
    child = start.spawn_unmanaged_gateway(root, deadline=time.monotonic() + 5)
    try:
        assert child.wait(timeout=10) == 0
    finally:
        if child.poll() is None:
            child.kill()
            child.wait(timeout=5)
    seen = json.loads(Path(witness).read_text())
    assert seen == {'TELEGRAM_BOT_TOKEN': None, 'OPENROUTER_API_KEY': 'root-key', 'NASTECH_LANGUAGE': None,
                    'NASTECH_HOME': str(root.resolve()), 'SHELL_INJECTED_SETTING': 'kept'}
