"""CLI entry point for the nastech-agent ACP adapter.

Loads ``~/.nastech/.env``, routes logging to stderr (stdout is reserved for ACP
JSON-RPC), and starts the ACP agent server.

Usage::

    python -m acp_adapter.entry   # or: nastech acp / nastech-acp
"""

# IMPORTANT: nastech_bootstrap must be the very first import — UTF-8 stdio
# on Windows.  No-op on POSIX.  See nastech_bootstrap.py for full rationale.
try:
    import nastech_bootstrap  # noqa: F401
except ModuleNotFoundError as exc:
    # Partial ``nastech update`` (git-reset landed, ``uv pip install -e .`` did not).
    if exc.name != "nastech_bootstrap":
        raise  # the bootstrap exists but cannot load: skipping it would skip PM activation
else:
    # Stop a ``utils/``/``proxy/``/``ui/`` package in the launch cwd from shadowing Nastech modules.
    nastech_bootstrap.harden_import_path()

# `nastech-acp` runs without nastech_cli.main: repair a `nastech update` killed mid-pull here, before
# importing anything else from the checkout (a no-op under `nastech acp`, which already did).
from nastech_cli import _early_recovery

if _early_recovery.restore_interrupted_pull():
    _early_recovery.relaunch_after_restore()

import argparse
import asyncio
import logging
import os
import sys
from pathlib import Path
from nastech_constants import get_nastech_home


# Liveness-probe methods outside the ACP schema. The router correctly answers JSON-RPC -32601
# (clients treat that as "agent alive"), but the dispatching supervisor task also logs
# ``"Background task failed"`` with a traceback every probe. Keep the response; silence the noise.
_BENIGN_PROBE_METHODS = frozenset({"ping", "health", "healthcheck"})


class _BenignProbeMethodFilter(logging.Filter):
    """Suppress acp 'Background task failed' tracebacks caused by unknown liveness-probe methods
    (e.g. ``ping``); every other background-task error, incl. method_not_found for non-probe
    methods, stays visible."""

    def filter(self, record: logging.LogRecord) -> bool:
        if record.getMessage() != "Background task failed" or not record.exc_info:
            return True
        # Lazy import keeps this module importable without ``agent-client-protocol``.
        try:
            from acp.exceptions import RequestError
        except ImportError:
            return True
        exc = record.exc_info[1]
        if not isinstance(exc, RequestError) or getattr(exc, "code", None) != -32601:
            return True
        data = getattr(exc, "data", None)
        return not (isinstance(data, dict) and data.get("method") in _BENIGN_PROBE_METHODS)


def _setup_logging() -> None:
    """Route all logging to stderr so stdout stays clean for ACP stdio."""
    from agent.redact import RedactingFormatter

    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(RedactingFormatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s",
                                            datefmt="%Y-%m-%d %H:%M:%S"))
    handler.addFilter(_BenignProbeMethodFilter())
    root = logging.getLogger()
    root.handlers.clear()
    root.addHandler(handler)
    root.setLevel(logging.INFO)
    for noisy in ("httpx", "httpcore", "openai"):
        logging.getLogger(noisy).setLevel(logging.WARNING)


def _load_env() -> None:
    """Load .env from NASTECH_HOME (default ``~/.nastech``)."""
    from nastech_cli.env_loader import load_nastech_dotenv

    nastech_home = get_nastech_home()
    loaded = load_nastech_dotenv(nastech_home=nastech_home)
    log = logging.getLogger(__name__)
    for env_file in loaded or ():
        log.info("Loaded env from %s", env_file)
    if not loaded:
        log.info("No .env found at %s, using system env", nastech_home / ".env")


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="nastech-acp", description="Run Nastech Agent as an ACP stdio server.")
    parser.add_argument("--version", action="store_true", help="Print Nastech version and exit")
    parser.add_argument("--check", action="store_true", help="Verify ACP dependencies and adapter imports, then exit")
    parser.add_argument("--setup", action="store_true",
                        help="Run interactive Nastech provider/model setup for ACP terminal auth")
    parser.add_argument("--setup-browser", action="store_true",
                        help="Prepare PM's pinned browser tools and Chromium.")
    parser.add_argument("--yes", "-y", action="store_true", dest="assume_yes",
                        help="Accept setup prompts.")
    return parser.parse_args(argv)


def _print_version() -> None:
    from nastech_cli.version_info import get_version_info

    print(get_version_info().derived_version)


def _run_check() -> None:
    import acp  # noqa: F401
    from acp_adapter.server import NastechACPAgent  # noqa: F401

    print("Nastech ACP check OK")


def _run_setup() -> None:
    from nastech_cli.main import main as nastech_main

    old_argv = sys.argv[:]
    try:
        sys.argv = [old_argv[0] if old_argv else "nastech", "model"]
        nastech_main()
    finally:
        sys.argv = old_argv

    # Terminal auth is the first-run UX for registry installs, so offer the browser-tools
    # install here. Skip silently without a TTY.
    if not sys.stdin.isatty():
        return
    try:
        reply = input("\nInstall browser tools? Downloads the pinned browser and "
                      "Chromium through PM. [y/N] ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        return
    if reply in {"y", "yes"}:
        _run_setup_browser(assume_yes=False)


def _run_setup_browser(assume_yes: bool = False) -> int:
    """The setup command is an explicit request for PM's browser closure."""
    import pm

    try:
        pm.ensure("agent-browser", explicit=True)
    except (pm.InstallError, OSError) as exc:
        print(f"Browser setup failed: {exc}", file=sys.stderr)
        return 1
    return 0


def _warm_memory_provider_import(logger: logging.Logger) -> None:
    """Import ``memory.provider``'s module + numpy (no provider instance) before the ACP threads start."""
    from plugins.memory import import_memory_provider_module

    if not import_memory_provider_module():
        logger.debug("memory provider not warmed (none configured or import failed; agent init reports that)")


def main(argv: list[str] | None = None) -> None:
    """Entry point: load env, configure logging, run the ACP agent."""
    args = _parse_args(argv)
    for flag, action in (("version", _print_version), ("check", _run_check), ("setup", _run_setup)):
        if getattr(args, flag):
            return action()
    if args.setup_browser:
        if rc := _run_setup_browser(assume_yes=args.assume_yes):
            sys.exit(rc)
        return

    _setup_logging()
    _load_env()

    logger = logging.getLogger(__name__)
    logger.info("Starting nastech-agent ACP adapter")

    # Ensure the project root is on sys.path so ``from run_agent import AIAgent`` works
    project_root = str(Path(__file__).resolve().parent.parent)
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    # One TLS authority: trust the OS store before any outbound call (bare
    # requests/urllib included) resolves a CA bundle — see agent/ssl_verify.py.
    # This console script bypasses nastech_cli.main, which does the same.
    from agent.ssl_verify import install_truststore

    install_truststore()

    import acp
    from .server import NastechACPAgent

    # Windows: import the configured memory provider (and numpy) on the main thread before
    # the MCP-discovery and ACP stdin-reader threads start (nastech_cli's ~150 ms
    # plugin-discovery thread is the only one already running). A first-time
    # native-extension import (numpy via holographic / mnemosyne / hindsight) racing another
    # thread's import chain deadlocked in create_module and session/new never answered
    # (#58083). After this the off-loop agent build finds the modules in sys.modules.
    if sys.platform == "win32":
        _warm_memory_provider_import(logger)

    # MCP discovery from config.yaml runs in a background daemon thread so the ACP server is
    # responsive immediately (blocking here cost 2-5 s); per-session MCP servers registered via
    # asyncio.to_thread are unaffected. Metadata-only hosts can opt out of the global startup.
    # Previously this blocked asyncio.run() for 2-5 s. (ACP also registers per-session MCP servers
    # dynamically via asyncio.to_thread inside the event loop; that path is unaffected.)  Moved from
    # model_tools.py module scope to avoid freezing the gateway's loop on lazy import (#16856).
    if os.environ.get("NASTECH_ACP_SKIP_CONFIGURED_MCP", "").strip() != "1":
        try:
            from nastech_cli.mcp_startup import start_background_mcp_discovery

            start_background_mcp_discovery(logger=logger, thread_name="acp-mcp-discovery")
        except Exception:
            logger.debug("MCP tool discovery failed at ACP startup", exc_info=True)

    agent = NastechACPAgent()
    try:
        asyncio.run(acp.run_agent(agent, use_unstable_protocol=True))
    except KeyboardInterrupt:
        logger.info("Shutting down (KeyboardInterrupt)")
    except Exception:
        logger.exception("ACP agent crashed")
        sys.exit(1)
    finally:
        # The stdio client that drove these conversations is gone. Without an
        # ended_at writer here, source='acp' rows stay open forever and the
        # ended-session guard keeps prune/archive away from them (#118216). A
        # later load/resume reopens the row (acp_adapter.session._restore).
        agent.session_manager.end_all_sessions()


if __name__ == "__main__":
    main()
