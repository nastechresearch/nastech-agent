"""config.yaml sessions.* bridges for the search-index knobs (config-authoritative).

Salvaged from PR #65544 (adapted: agent.fts_v2_read → sessions.cjk_fts).
"""

from __future__ import annotations

import os
from pathlib import Path

import nastech_yaml as yaml

import gateway.run as gateway_run


def _write_home(tmp_path: Path, sessions_cfg: dict, env_text: str = "") -> Path:
    nastech_home = tmp_path / ".nastech"
    nastech_home.mkdir()
    (nastech_home / "config.yaml").write_text(
        yaml.safe_dump({"sessions": sessions_cfg}), encoding="utf-8"
    )
    (nastech_home / ".env").write_text(env_text, encoding="utf-8")
    return nastech_home


def test_cjk_fts_bridged_from_config(tmp_path, monkeypatch):
    home = _write_home(tmp_path, {"cjk_fts": False})
    monkeypatch.setattr(gateway_run, "_nastech_home", home)
    monkeypatch.setenv("NASTECH_CJK_FTS", "1")
    gateway_run._reload_runtime_env_preserving_config_authority()
    assert os.environ["NASTECH_CJK_FTS"] == "False"


