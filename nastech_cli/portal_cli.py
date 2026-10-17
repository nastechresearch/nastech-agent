"""``nastech portal`` — the human-readable entry point for Nastech Portal."""
from __future__ import annotations

import sys
import webbrowser

from nastech_cli.colors import Colors, color
from nastech_cli.config import load_config

# Post-brand reconciliation: FAIL-CLOSED API defaults.  Nastech
# operates no portal/inference/welcome API, and a GitHub Pages subdomain can
# never complete TLS (the certificate carries only `*.github.io`, one label),
# so the literal this replaces is an origin nobody can reach.  The default is
# therefore read from the environment; when the variable is absent the value
# names an RFC 2606 `.invalid` origin instead, which no resolver can answer, so
# the dead origin is never used and a request fails at DNS with the variable to
# set visible in the host name.
#
# That value must stay safe to STRINGIFY, format and strip: real consumers
# build their authorize/token/JWKS URLs from these constants while they
# register, and a default whose ``str()`` raised disabled the whole
# dashboard-auth provider rather than failing one request
# (nastech-agent#157, 2026-10-17).
import os as _nastech_endpoint_env


def _nastech_endpoint_default(env: str, constant: str, dead_default: str):
    """Operator-configured endpoint, else an unconfigured, unresolvable origin.

    ``constant`` is carried so a generated call site records which branded
    default it replaced.
    """
    configured = _nastech_endpoint_env.environ.get(env, "").strip().rstrip("/")
    if configured:
        return configured
    path = dead_default.split("://", 1)[-1].partition("/")[2]
    label = env.lower().replace("_", "-") or "endpoint"
    return _NastechUnconfiguredEndpoint(
        f"https://{label}.invalid" + (f"/{path}" if path else "")
    )


class _NastechUnconfiguredEndpoint(str):
    """Unconfigured endpoint: a real string, at a host that can never resolve.

    Falsy, so ``value or fallback`` keeps working; never raising, because
    logging and URL construction stringify the default while a provider is
    registering; and unresolvable, so nothing is ever sent to a host that
    cannot answer instead of the branded dead origin.
    """

    def __bool__(self):
        return False


DEFAULT_PORTAL_URL = _nastech_endpoint_default(
    env='PORTAL_URL',
    constant='DEFAULT_PORTAL_URL',
    dead_default='https://portal.nastechresearch.github.io',
)
SUBSCRIPTION_URL = "https://portal.nastechresearch.github.io/manage-subscription"
DOCS_URL = "https://nastechresearch.github.io/nastech-agent/docs/user-guide/features/tool-gateway"
# Static `portal tools` catalog — the partners Tool Gateway routes to today: (key, label, partner).
_CATALOG = [
    ("web", "Web search & extract", "Nastech-managed"),
    ("image_gen", "Image generation", "FAL"),
    ("tts", "Text-to-speech", "OpenAI TTS"),
    ("browser", "Browser automation", "Browser Use"),
    ("modal", "Cloud terminal", "Modal"),
]


def _feature_state(feat, *, via_nastech: str) -> str:
    """Routing column shared by `portal info` and `portal tools`."""
    if feat.managed_by_nastech:
        return color(via_nastech, Colors.GREEN)
    if feat.active:
        return feat.current_provider or "active"
    return color("not configured", Colors.DIM)


def _heading(title: str) -> None:
    print()
    print(color(f"  {title}", Colors.MAGENTA))
    print(color("  " + "─" * len(title), Colors.MAGENTA))


def _cmd_status(args) -> int:
    """Show Portal auth + Tool Gateway routing summary."""
    from nastech_cli.auth import get_nastech_auth_status_local
    from nastech_cli.nastech_subscription import get_nastech_subscription_features

    config = load_config() or {}
    try:
        auth = get_nastech_auth_status_local() or {}  # refresh-free snapshot
    except Exception:
        auth = {}
    logged_in = bool(auth.get("logged_in"))
    free_tier = bool(auth.get("free_tier"))
    _heading("Nastech Portal")
    if free_tier:
        from nastech_cli.anon_auth import FREE_TIER_LABEL, GUEST_MODEL, UPGRADE_HINT
        print(f"  Auth:    {color(f'{FREE_TIER_LABEL} · {GUEST_MODEL}', Colors.GREEN)}")
        print(f"           {UPGRADE_HINT}")
        if auth.get("inference_base_url"):
            print(f"  API:     {auth['inference_base_url']}")
    elif logged_in:
        print(f"  Auth:    {color('✓ logged in', Colors.GREEN)}")
        print(f"  Portal:  {auth.get('portal_base_url') or DEFAULT_PORTAL_URL}")
        if auth.get("inference_base_url"):
            print(f"  API:     {auth['inference_base_url']}")
    else:
        print(f"  Auth:    {color('not logged in', Colors.YELLOW)}")
        print(f"  Sign up: {SUBSCRIPTION_URL}")
        print("  Login:   nastech portal")

    # Provider selection (independent of auth)
    model_cfg = config.get("model") if isinstance(config.get("model"), dict) else {}
    provider = str(model_cfg.get("provider") or "").strip().lower()
    if provider == "nastech":
        print(f"  Model:   {color('✓ using Nastech as inference provider', Colors.GREEN)}")
    elif provider:
        print(f"  Model:   currently {provider} (switch with `nastech model`)")

    _heading("Tool Gateway")
    try:
        features = get_nastech_subscription_features(config)
    except Exception:
        print("  (could not resolve subscription state)")
        return 0
    rows = [(feat.label, _feature_state(feat, via_nastech="via Nastech Portal")) for feat in features.items()]
    width = max((len(r[0]) for r in rows), default=0)
    for label, state in rows:
        print(f"  {label:<{width}}   {state}")
    if not logged_in:
        print()
        print(color(f"  Docs: {DOCS_URL}", Colors.DIM))
    return 0


def _cmd_open(args) -> int:
    """Open the Portal subscription page in the default browser."""
    print(f"Opening {SUBSCRIPTION_URL}")
    try:
        opened = webbrowser.open(SUBSCRIPTION_URL)
    except Exception:
        opened = False
    if opened:
        return 0
    print()
    print("Could not launch a browser. Visit the URL above manually.")
    return 1


def _cmd_tools(args) -> int:
    """List the Tool Gateway catalog + current routing."""
    from nastech_cli.nastech_subscription import get_nastech_subscription_features, managed_image_partner

    config = load_config() or {}
    try:
        features = get_nastech_subscription_features(config)
    except Exception:
        print("Could not resolve Tool Gateway state.", file=sys.stderr)
        return 1

    _heading("Tool Gateway catalog")
    if not features.nastech_auth_present:
        print(color("  Not logged into Nastech Portal — sign in with `nastech portal`.", Colors.YELLOW))
        print()

    label_width = max(len(label) for _, label, _ in _CATALOG)
    for key, label, partner in _CATALOG:
        if key == "image_gen":
            partner = managed_image_partner(config) or partner
        feat = features.features.get(key)
        state = color("unknown", Colors.DIM) if feat is None else _feature_state(feat, via_nastech="✓ via Nastech Portal")
        print(f"  {label:<{label_width}}  partner: {partner:<14} {state}")

    print()
    print(color(f"  Manage your subscription: {SUBSCRIPTION_URL}", Colors.DIM))
    print(color(f"  Docs: {DOCS_URL}", Colors.DIM))
    return 0


def _cmd_login(args) -> int:
    """One-shot Nastech Portal onboarding (login + model + provider + tools).

    Reuses the exact wiring behind ``nastech setup --portal`` so the commands stay in lockstep.
    """
    from nastech_cli.setup import _run_portal_one_shot

    config = load_config() or {}
    try:
        _run_portal_one_shot(config)
    except (KeyboardInterrupt, EOFError):
        print()
        print("Portal setup cancelled.")
        return 1
    return 0


# Default (None/"") is the one-shot onboarding (alias for `nastech auth add nastech --type oauth` /
# `nastech setup --portal`). `status` kept as a back-compat alias for `info`.
_SUBCOMMANDS = {
    None: _cmd_login,
    "": _cmd_login,
    "login": _cmd_login,
    "info": _cmd_status,
    "status": _cmd_status,
    "open": _cmd_open,
    "tools": _cmd_tools,
}


def portal_command(args) -> int:
    """Top-level dispatch for `nastech portal <subcommand>`."""
    sub = getattr(args, "portal_command", None)
    handler = _SUBCOMMANDS.get(sub)
    if handler is not None:
        return handler(args)
    print(f"Unknown portal subcommand: {sub}", file=sys.stderr)
    print("Run `nastech portal -h` for usage.", file=sys.stderr)
    return 1


def add_parser(subparsers) -> None:
    """Register `nastech portal` on the given argparse subparsers object."""
    portal_parser = subparsers.add_parser(
        "portal",
        help="Set up Nastech Portal (login, model pick, Tool Gateway); see also `portal info`",
        description=(
            "Run `nastech portal` with no subcommand to log in to Nastech Portal "
            "and set it up — pick a model, set Nastech as your provider, and offer "
            "the Tool Gateway (the human-readable alias for `nastech auth add "
            "nastech --type oauth`, identical to `nastech setup --portal`). "
            "Subcommands: login (default), info, open, tools."
        ),
    )
    portal_sub = portal_parser.add_subparsers(dest="portal_command")

    # `status` is a hidden (no help) back-compat alias; registration order = `nastech portal -h` order.
    for name, help_text in (
        ("login", "Log in to Nastech Portal + set it up (default; one-shot onboarding)"),
        ("info", "Show Portal auth + Tool Gateway routing summary"),
        ("status", None),
        ("open", "Open the Portal subscription page in your default browser"),
        ("tools", "List Tool Gateway tools and which are routed via Nastech"),
    ):
        portal_sub.add_parser(name, **({} if help_text is None else {"help": help_text}))

    portal_parser.set_defaults(func=portal_command)
