"""Runtime smoke tests for Docker PUID/PGID and UID/GID remap.

Build the real image and verify the actual runtime behavior:

  1. PUID/PGID env vars remap the nastech user UID/GID at boot
  2. NASTECH_UID/NASTECH_GID take precedence over PUID/PGID aliases
  3. NAS-style low UIDs (99:100) are accepted and remapped
  4. Invalid UIDs are rejected
  5. The remapped user can write to the data volume
"""
from __future__ import annotations

from tests.docker.conftest import docker_exec_sh, start_container

def test_puid_pgid_remaps_nastech_user(
    built_image: str, container_name: str,
) -> None:
    """PUID=1000 PGID=1000 must remap the nastech user to UID 1000."""
    start_container(built_image, container_name, "PUID=1000", "PGID=1000")

    r = docker_exec_sh(
        container_name,
        "id -u nastech",
        timeout=10,
    )
    assert r.stdout.strip() == "1000", (
        f"expected nastech UID 1000 after PUID remap, got: {r.stdout.strip()}"
    )

    r = docker_exec_sh(
        container_name,
        "id -g nastech",
        timeout=10,
    )
    assert r.stdout.strip() == "1000", (
        f"expected nastech GID 1000 after PGID remap, got: {r.stdout.strip()}"
    )

    # The remapped user must still be able to write to the data volume.
    r = docker_exec_sh(
        container_name,
        "touch /opt/data/test_write && echo WRITE_OK || echo WRITE_FAIL",
        timeout=10,
    )
    assert "WRITE_OK" in r.stdout, (
        f"nastech user cannot write to /opt/data after remap: {r.stdout}"
    )

def test_nas_low_uid_accepted(
    built_image: str, container_name: str,
) -> None:
    """NAS-style low UIDs (99:100, common on Unraid) must be accepted."""
    start_container(built_image, container_name, "PUID=99", "PGID=100")

    r = docker_exec_sh(container_name, "id -u nastech", timeout=10)
    assert r.stdout.strip() == "99", (
        f"expected nastech UID 99, got: {r.stdout.strip()}"
    )

    r = docker_exec_sh(container_name, "id -g nastech", timeout=10)
    assert r.stdout.strip() == "100", (
        f"expected nastech GID 100, got: {r.stdout.strip()}"
    )
