"""``nastech debug`` subcommand parser."""

from __future__ import annotations

import argparse
from typing import Callable


def build_debug_parser(subparsers, *, cmd_debug: Callable) -> None:
    """Attach the ``debug`` subcommand to ``subparsers``."""
    debug_parser = subparsers.add_parser(
        "debug", help="Debug tools — upload logs and system info for support",
        description="Debug utilities for Nastech Agent. Use 'nastech debug share' to "
        "upload an allowlisted debug summary (versions, config key names, error "
        "counts; no log text) to a public paste, or 'nastech debug share --nastech' "
        "to send full redacted logs to private Nastech storage.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
Examples:
    nastech debug share              Upload debug report (asks for confirmation)
    nastech debug share --yes        Skip confirmation (for scripts/CI)
    nastech debug share --lines 500  Scan/include more log lines
    nastech debug share --expire 30  Keep dpaste.com fallback pastes for 30 days
    nastech debug share --local      Print report locally (no upload)
    nastech debug share --nastech --no-redact  Send unredacted logs to Nastech storage
    nastech debug share --nastech       Upload to Nastech-internal storage (private)
    nastech debug delete <url>       Delete a previously uploaded paste
""")
    debug_sub = debug_parser.add_subparsers(dest="debug_command")
    share_parser = debug_sub.add_parser(
        "share", help="Upload an allowlisted debug summary to a public paste (full logs: --nastech)")
    share_parser.add_argument(
        "--lines", type=int, default=200,
        help="Log lines per file: scanned for the public summary's error counts, "
            "included verbatim (redacted) with --nastech / --local (default: 200)")
    share_parser.add_argument(
        "--expire", type=int, default=1,
        help="dpaste.com fallback retention in days (minimum 1; default: 1). "
            "paste.rs pastes are always deleted after 6 hours, but if the "
            "upload falls back to dpaste.com the pastes live for this many "
            "days and cannot be deleted.")
    share_parser.add_argument(
        "--local", action="store_true", help="Print the report locally instead of uploading")
    share_parser.add_argument(
        "-y", "--yes", action="store_true",
        help="Skip the confirmation prompt and upload immediately. Required "
            "in non-interactive contexts (scripts/CI); without it, and with "
            "no TTY on stdin, the command refuses rather than upload silently.")
    share_parser.add_argument(
        "--no-redact", action="store_true",
        help="Disable secret redaction of the logs sent with --nastech or printed "
            "with --local (default: redact). The public paste never carries log "
            "text, so this flag cannot put logs there.")
    share_parser.add_argument(
        "--nastech", action="store_true",
        help="Upload the debug bundle to Nastech-internal storage (AWS S3) instead "
            "of a public paste service. The bundle is private — viewable only "
            "by Nastech staff (and allowlisted Discord mods) via a Google-login-"
            "gated viewer — and auto-deletes after 14 days. Still force-redacts "
            "secrets unless --no-redact is also passed.")
    delete_parser = debug_sub.add_parser(
        "delete", help="Delete a paste uploaded by 'nastech debug share'")
    delete_parser.add_argument(
        "urls", nargs="*", default=[],
        help="One or more paste URLs to delete (e.g. https://paste.rs/abc123)")
    debug_parser.set_defaults(func=cmd_debug)
