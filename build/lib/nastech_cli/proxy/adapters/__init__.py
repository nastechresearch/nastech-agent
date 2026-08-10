"""Upstream adapter registry for the local proxy server.

Each adapter wraps a provider's OAuth state and exposes a uniform interface
the proxy server can use to forward requests with a freshly-minted bearer
token. See :class:`UpstreamAdapter` for the contract.
"""

from typing import Dict, Type

from nastech_cli.proxy.adapters.base import UpstreamAdapter
from nastech_cli.proxy.adapters.nastech_portal import NastechPortalAdapter
from nastech_cli.proxy.adapters.xai import XAIGrokAdapter

# Registry of available adapter classes keyed by provider name as used on
# the ``nastech proxy start --provider <name>`` CLI flag.
ADAPTERS: Dict[str, Type[UpstreamAdapter]] = {
    "nastech": NastechPortalAdapter,
    "xai": XAIGrokAdapter,
}


def get_adapter(name: str) -> UpstreamAdapter:
    """Instantiate an adapter by provider name.

    Raises:
        ValueError: if ``name`` is not a registered adapter.
    """
    key = (name or "").strip().lower()
    if key not in ADAPTERS:
        available = ", ".join(sorted(ADAPTERS)) or "(none)"
        raise ValueError(
            f"Unknown proxy upstream provider: {name!r}. Available: {available}"
        )
    return ADAPTERS[key]()


__all__ = ["UpstreamAdapter", "ADAPTERS", "get_adapter"]
