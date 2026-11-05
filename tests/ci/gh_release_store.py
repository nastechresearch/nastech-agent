"""A file-backed stand-in for the GitHub release-asset API, run through a `gh` shim.

`tests/ci` executes real workflow steps in a subprocess, so the fake release store
has to be reachable the way the product reaches it: as a `gh` on `PATH` (see
`scripts/releases/gh_transport.py`, whose only subprocess surface is `gh api`).
This module is that command. It keeps its state in a directory so the test that
seeds a staged asset and the test that asserts what was fetched are looking at the
same store, across the process boundary.

The routes implemented are exactly the ones the transport uses -- nothing else
answers. A route the transport starts calling without a test noticing fails here,
rather than silently returning an empty listing.
"""
from __future__ import annotations

import json
import os
import re
import shlex
import sys
from pathlib import Path
from urllib.parse import unquote

from scripts.releases.gh_transport import asset_name, key_for_asset, release_tag_for

STATE = "GH_FAKE_RELEASE_STORE"
_REPO_ROOT = Path(__file__).resolve().parents[2]


def install_shim(helper: Path) -> Path:
    """Put a `gh` on `PATH` that answers from the store named by `$GH_FAKE_RELEASE_STORE`.

    A workflow step reaches the store by running `gh`, so that is the seam a test
    has to occupy; the shim re-enters this module with the interpreter that owns
    the state directory, which is why it is a launcher rather than a patched
    function.
    """
    helper.mkdir(parents=True, exist_ok=True)
    launcher = helper / "gh"
    launcher.write_text(
        # The re-entered process is outside pytest's import path, and it must read the
        # product's own key routing to place an asset where the product looks for it.
        f'#!/bin/sh\nPYTHONPATH={shlex.quote(str(_REPO_ROOT))}'
        '${PYTHONPATH:+:$PYTHONPATH}\nexport PYTHONPATH\n'
        f'exec {shlex.quote(sys.executable)} '
        f'{shlex.quote(str(Path(__file__).resolve()))} "$@"\n',
        encoding="utf-8", newline="\n")
    launcher.chmod(0o755)
    return helper


class ReleaseStore:
    """The release-asset endpoints `gh_transport` uses, kept in a directory."""

    def __init__(self, root: Path):
        self.root = root
        self.state_path = root / "state.json"
        self.payload_dir = root / "payloads"
        self.payload_dir.mkdir(parents=True, exist_ok=True)

    def _load(self) -> dict:
        if self.state_path.exists():
            return json.loads(self.state_path.read_text(encoding="utf-8-sig"))
        return {"releases": {}, "assets": {}, "next_id": 1, "calls": []}

    def _save(self, state: dict) -> None:
        self.state_path.write_text(json.dumps(state, sort_keys=True) + "\n", encoding="utf-8")

    def env(self) -> dict:
        """The variables a job carries to reach this store: the pin and the job's own token.

        No storage credential is among them, which is the point -- a release store
        is addressed with the identity the runner already has.
        """
        return {STATE: str(self.root), "RELEASE_HANDOFF_STORE": "github",
                "GH_TOKEN": "inert-test-token", "GITHUB_REPOSITORY": "o/r"}

    def seed(self, key: str, body: bytes) -> None:
        """Put bytes at an object key, as a build job that already staged them would.

        The key is placed the way the product places it -- which release carries it
        and what the asset is called both come from `gh_transport`, so a test that
        seeds a key and a leg that fetches it cannot drift apart.  The release a key
        is seeded on is a draft, because that is the only state this plane stages
        into, and it is why finding one's release needs the list route.
        """
        state = self._load()
        tag = release_tag_for(key)
        release = state["releases"].setdefault(tag, {"id": self._new_id(state), "draft": True})
        asset_id = self._new_id(state)
        state["assets"][str(asset_id)] = {
            "name": asset_name(key), "release": release["id"], "size": len(body),
            "payload": self._put_payload(asset_id, body),
        }
        self._save(state)

    def keys(self) -> list[str]:
        """Every object key currently staged, in the store's own key language."""
        return sorted(key_for_asset(str(asset["name"])) for asset in self._load()["assets"].values())

    def calls(self) -> list[list[str]]:
        return self._load()["calls"]

    def _new_id(self, state: dict) -> int:
        state["next_id"] += 1
        return state["next_id"] - 1

    def _put_payload(self, asset_id: int, body: bytes) -> str:
        name = f"{asset_id}.bin"
        (self.payload_dir / name).write_bytes(body)
        return name

    def _read_payload(self, asset: dict) -> bytes:
        return (self.payload_dir / asset["payload"]).read_bytes()

    def run(self, argv: list[str]) -> int:
        """`gh api <route> [args…]` -> the reply the release API would give."""
        state = self._load()
        state["calls"].append(list(argv))
        route = argv[1] if argv and argv[0] == "api" else argv[0]
        fields = [argv[index + 1] for index, arg in enumerate(argv) if arg in ("-f", "-F")]
        code = self._dispatch(state, route, fields, argv, self._method(argv))
        self._save(state)
        return code

    @staticmethod
    def _method(argv: list[str]) -> str:
        """The verb `gh api` will send, which is not always the one the caller meant.

        A field or an input body turns the call into a POST even when nothing asked
        for one, and GitHub answers a write to a read-only route with a 404 -- so a
        transport that paginates with `-f per_page=100` and no explicit verb loses
        the release it was looking for and opens another.
        """
        for flag in ("-X", "--method"):
            if flag in argv:
                return argv[argv.index(flag) + 1].upper()
        return "POST" if any(arg in ("-f", "-F", "--input") for arg in argv) else "GET"

    def _dispatch(self, state: dict, route: str, fields: list[str], argv: list[str],
                  method: str) -> int:
        path, _, query = route.partition("?")
        if m := _match(path, r"repos/[^/]+/[^/]+/releases/tags/(.+)"):
            if method != "GET":
                return self._not_found(path)
            tag = unquote(m.group(1))
            release = state["releases"].get(tag)
            if release is None or release["draft"]:
                return self._not_found(tag)
            return self._json({"id": release["id"]})
        if _match(path, r"repos/[^/]+/[^/]+/releases"):
            if method == "POST":
                tag = next(field.split("=", 1)[1] for field in fields
                           if field.startswith("tag_name="))
                release = state["releases"].get(tag) or {"id": self._new_id(state), "draft": True}
                state["releases"][tag] = release
                return self._json({"id": release["id"], "draft": release["draft"]})
            if method != "GET":
                return self._not_found(path)
            # The paginated list is the route that can see a draft, so it is how the
            # product finds the release a key belongs to when the tag lookup misses.
            rows = [{"id": release["id"], "tag_name": tag}
                    for tag, release in state["releases"].items()]
            size = int(next((field.split("=")[1] for field in fields
                             if field.startswith("per_page=")), 30))
            page = int(next((field.split("=")[1] for field in fields
                             if field.startswith("page=")), 1))
            return self._json(rows[(page - 1) * size:page * size])
        if m := _match(path, r"repos/[^/]+/[^/]+/releases/(\d+)/assets"):
            release_id = int(m.group(1))
            if method == "POST":
                body = Path(argv[argv.index("--input") + 1]).read_bytes()
                asset_id = self._new_id(state)
                state["assets"][str(asset_id)] = {
                    "name": unquote(query.partition("name=")[2]), "release": release_id,
                    "size": len(body), "payload": self._put_payload(asset_id, body),
                }
                return self._json({"id": asset_id, "name": state["assets"][str(asset_id)]["name"],
                                   "size": len(body)})
            if method != "GET":
                return self._not_found(path)
            rows = [self._row(asset_id, asset)
                    for asset_id, asset in state["assets"].items()
                    if asset["release"] == release_id]
            page = int(next((field.split("=")[1] for field in fields
                             if field.startswith("page=")), 1))
            return self._json(rows[(page - 1) * 100:page * 100])
        if m := _match(path, r"repos/[^/]+/[^/]+/releases/assets/(\d+)"):
            asset_id = m.group(1)
            if method == "DELETE":
                state["assets"].pop(asset_id, None)
                return self._json({})
            if method != "GET":
                return self._not_found(path)
            if asset_id not in state["assets"]:
                return self._not_found(f"asset {asset_id}")
            sys.stdout.buffer.write(self._read_payload(state["assets"][asset_id]))
            sys.stdout.buffer.flush()
            return 0
        print(f"unhandled gh api route: {route}", file=sys.stderr)
        return 2

    @staticmethod
    def _row(asset_id: str, asset: dict) -> dict:
        return {"id": int(asset_id), "name": asset["name"], "size": asset["size"]}

    @staticmethod
    def _json(payload) -> int:
        print(json.dumps(payload))
        return 0

    @staticmethod
    def _not_found(target: str) -> int:
        print(f"gh: HTTP 404: Not Found ({target})", file=sys.stderr)
        return 1


def _match(route: str, pattern: str):
    return re.fullmatch(pattern, route)


def main(argv: list[str]) -> int:
    assert argv and argv[0] == "api", f"the fake gh only answers `gh api`: {argv}"
    root = os.environ.get(STATE)
    assert root, f"{STATE} must name the directory holding the fake store"
    return ReleaseStore(Path(root)).run(argv[1:])


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
