"""Security boundary tests for dashboard MCP catalog credential writes."""

from __future__ import annotations

import os
from pathlib import Path

import pytest
import yaml
from fastapi.testclient import TestClient

from nastech_cli.web_server import _SESSION_TOKEN, app


HEADERS = {"X-Nastech-Session-Token": _SESSION_TOKEN}


@pytest.fixture
def catalog_env(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, _isolate_nastech_home):
    """Install one synthetic API-key catalog entry in the isolated test home."""
    from nastech_constants import get_nastech_home
    from nastech_cli.config import invalidate_env_cache

    catalog = tmp_path / "optional-mcps"
    entry_dir = catalog / "demo"
    entry_dir.mkdir(parents=True)
    (entry_dir / "manifest.yaml").write_text(
        yaml.safe_dump(
            {
                "manifest_version": 1,
                "name": "demo",
                "description": "Synthetic dashboard boundary fixture",
                "source": "https://example.test/demo",
                "transport": {
                    "type": "stdio",
                    "command": "demo-mcp",
                },
                "auth": {
                    "type": "api_key",
                    "env": [
                        {
                            "name": "DEMO_API_KEY",
                            "prompt": "Demo API key",
                            "secret": True,
                        }
                    ],
                },
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setenv("NASTECH_OPTIONAL_MCPS", str(catalog))
    invalidate_env_cache()
    return get_nastech_home()


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client


def test_catalog_rejects_undeclared_key_before_any_write_or_install(
    client: TestClient,
    catalog_env: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    import nastech_cli.mcp_catalog as mcp_catalog

    installs: list[str] = []
    monkeypatch.setattr(
        mcp_catalog,
        "install_entry",
        lambda entry, enable=True: installs.append(entry.name),
    )

    response = client.post(
        "/api/mcp/catalog/install",
        headers=HEADERS,
        json={
            "name": "demo",
            "env": {
                "DEMO_API_KEY": "valid-demo-value",
                "UNRELATED_SETTING": "must-not-land",
            },
        },
    )

    assert response.status_code == 400
    detail = response.json()["detail"]
    assert "UNRELATED_SETTING" in detail
    assert "valid-demo-value" not in detail
    assert "must-not-land" not in detail
    assert installs == []
    env_path = catalog_env / ".env"
    assert not env_path.exists() or env_path.read_text(encoding="utf-8") == ""


def test_catalog_cannot_declare_reserved_control_key(
    client: TestClient,
    catalog_env: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    import nastech_cli.mcp_catalog as mcp_catalog

    catalog_root = Path(os.environ["NASTECH_OPTIONAL_MCPS"])
    manifest_path = catalog_root / "demo" / "manifest.yaml"
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    manifest["auth"]["env"].append(
        {
            "name": "NASTECH_YOLO_MODE",
            "prompt": "Unsafe control",
            "secret": False,
        }
    )
    manifest_path.write_text(yaml.safe_dump(manifest), encoding="utf-8")

    installs: list[str] = []
    monkeypatch.setattr(
        mcp_catalog,
        "install_entry",
        lambda entry, enable=True: installs.append(entry.name),
    )

    response = client.post(
        "/api/mcp/catalog/install",
        headers=HEADERS,
        json={"name": "demo", "env": {"NASTECH_YOLO_MODE": "1"}},
    )

    assert response.status_code == 400
    assert "denylist" in response.json()["detail"]
    assert installs == []
    env_path = catalog_env / ".env"
    assert not env_path.exists() or "NASTECH_YOLO_MODE" not in env_path.read_text(
        encoding="utf-8"
    )


def test_catalog_accepts_declared_credential(
    client: TestClient,
    catalog_env: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    import nastech_cli.mcp_catalog as mcp_catalog

    installs: list[str] = []
    monkeypatch.setattr(
        mcp_catalog,
        "install_entry",
        lambda entry, enable=True: installs.append(entry.name),
    )

    response = client.post(
        "/api/mcp/catalog/install",
        headers=HEADERS,
        json={"name": "demo", "env": {"DEMO_API_KEY": "valid-demo-value"}},
    )

    assert response.status_code == 200
    assert installs == ["demo"]
    assert "DEMO_API_KEY=valid-demo-value" in (
        catalog_env / ".env"
    ).read_text(encoding="utf-8")


@pytest.mark.parametrize(
    "protected_key",
    [
        "NASTECH_YOLO_MODE",
        "NASTECH_OPTIONAL_MCPS",
        "NASTECH_COPILOT_ACP_COMMAND",
        "NASTECH_COPILOT_ACP_ARGS",
    ],
)
def test_generic_env_endpoint_rejects_protected_key(
    client: TestClient,
    catalog_env: Path,
    protected_key: str,
):
    response = client.put(
        "/api/env",
        headers=HEADERS,
        json={"key": protected_key, "value": "must-not-land"},
    )

    assert response.status_code == 400
    env_path = catalog_env / ".env"
    assert not env_path.exists() or protected_key not in env_path.read_text(
        encoding="utf-8"
    )


def test_process_supplied_catalog_root_remains_supported(catalog_env: Path):
    from nastech_cli.mcp_catalog import get_entry

    assert get_entry("demo") is not None


def test_rejected_copilot_controls_do_not_change_live_resolvers(
    client: TestClient,
    catalog_env: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    from agent.copilot_acp_client import _resolve_args, _resolve_command

    monkeypatch.setenv("NASTECH_COPILOT_ACP_COMMAND", "/opt/trusted/copilot")
    monkeypatch.setenv("NASTECH_COPILOT_ACP_ARGS", "--acp --stdio")
    expected_command = _resolve_command()
    expected_args = _resolve_args()

    attempts = {
        "NASTECH_COPILOT_ACP_COMMAND": "/tmp/attacker-command",
        "NASTECH_COPILOT_ACP_ARGS": "--malicious-transport",
    }
    for key, value in attempts.items():
        response = client.put(
            "/api/env",
            headers=HEADERS,
            json={"key": key, "value": value},
        )
        assert response.status_code == 400

    assert _resolve_command() == expected_command
    assert _resolve_args() == expected_args
    env_path = catalog_env / ".env"
    if env_path.exists():
        env_text = env_path.read_text(encoding="utf-8")
        assert "/tmp/attacker-command" not in env_text
        assert "--malicious-transport" not in env_text


def test_preexisting_copilot_controls_remain_usable(
    catalog_env: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    from agent.copilot_acp_client import _resolve_args, _resolve_command
    from nastech_cli.env_loader import load_nastech_dotenv

    monkeypatch.setenv("NASTECH_COPILOT_ACP_COMMAND", "parent-placeholder")
    monkeypatch.setenv("NASTECH_COPILOT_ACP_ARGS", "--parent-placeholder")
    (catalog_env / ".env").write_text(
        "NASTECH_COPILOT_ACP_COMMAND=/opt/operator/copilot\n"
        "NASTECH_COPILOT_ACP_ARGS=--acp --stdio --operator-mode\n",
        encoding="utf-8",
    )

    load_nastech_dotenv(
        nastech_home=catalog_env,
        load_external_secrets=False,
    )

    assert _resolve_command() == "/opt/operator/copilot"
    assert _resolve_args() == ["--acp", "--stdio", "--operator-mode"]
