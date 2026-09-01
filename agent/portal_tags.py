"""Centralized Nastech Portal request tags.

Every Nastech request that hits the Nastech Portal — main agent loop, auxiliary
client (compression / titles / vision / web_extract / session_search / etc.),
and any future code path — must carry the same product-attribution tags so
Nastech can attribute usage to Nastech Agent and bucket it by client release.

Tag shape (sent in OpenAI-compatible ``extra_body['tags']``):

    [
        "product=nastech-agent",
        "client=nastech-client-v<__version__>",
    ]

The version is sourced live from ``nastech_cli.__version__`` so it auto-aligns
to whatever release is installed; the release script
(``scripts/release.py``) regex-bumps that single string, and every Portal
request picks up the new tag on the next process start.

Why one helper instead of inlining the literal at each site:
* Four call sites (main loop profile, aux client, run_agent compression
  fallback, web_tools fallback) used to drift apart — see PR #24194 which
  only got the aux site, leaving the main loop sending a different tag set.
* Tests should assert the same tag list everywhere; centralizing makes that
  assertion a one-liner against this module.

Do NOT pre-compute these as module-level constants in the consumers. The
version can change at runtime (editable installs, hot-reload tooling), and
``nastech_cli.__version__`` is the canonical source of truth.
"""

from __future__ import annotations

from contextvars import ContextVar
from typing import List, Optional

# ── Ambient conversation context ─────────────────────────────────────────────
#
# The main agent loop knows its ``session_id``; the dozens of auxiliary call
# sites (compression, title generation, vision, web_extract, session_search,
# MoA reference/aggregator slots, curator, kanban helpers, ...) do not — they
# funnel through ``agent.auxiliary_client.call_llm`` which has no session
# handle. Rather than threading a ``session_id`` parameter through every one
# of those call sites (and every future one), the agent loop publishes the
# active conversation id here and ``nastech_portal_tags()`` picks it up as a
# fallback whenever no explicit ``session_id`` is passed.
#
# ContextVar (not a module global) so concurrent agents in one process —
# gateway sessions, delegate_task subagents, batch runners — never see each
# other's conversation id. Worker threads spawned via
# ``tools.thread_context.propagate_context_to_thread`` (background review,
# MoA fan-out, tool executor) inherit it through the copied Context; bare
# threads (title generator) capture it explicitly at spawn time.
_conversation_id: ContextVar[Optional[str]] = ContextVar(
    "nastech_portal_conversation_id", default=None
)


# ── Ambient routing/affinity scope ───────────────────────────────────────────
#
# Separate from the conversation id above, which is an ATTRIBUTION value: it
# names the conversation a request belongs to and is sent to the Portal as
# ``conversation=<id>``. The affinity scope is a ROUTING value — OpenRouter's
# sticky ``session_id``, Nastech Portal's sticky key and xAI's ``x-grok-conv-id``
# use it to pin one conversation to one backend/prompt cache.
#
# The two agree for every host that keeps one session id per conversation, so
# the providers historically read the attribution id for both. They diverge
# for a host that mints one physical session per RESPONSE: attribution still
# resolves per row, while routing must follow the key the host declared for
# the whole chat (``agent.prompt_cache_scope.declared_conversation_scope``,
# issue #96811). Only that declared value is published here — unset means
# "no declaration", and consumers fall back to the conversation id exactly as
# before, so delegate trees keep sharing their parent's sticky key.
_affinity_scope: ContextVar[Optional[str]] = ContextVar(
    "nastech_affinity_scope", default=None
)


def set_affinity_scope(scope: Optional[str]):
    """Publish the declared routing/affinity scope for this turn.

    Returns the ContextVar token; pair with :func:`reset_affinity_scope`.
    """
    return _affinity_scope.set(scope or None)


def reset_affinity_scope(token) -> None:
    """Restore the previous affinity scope (pair with ``set_affinity_scope``)."""
    try:
        _affinity_scope.reset(token)
    except Exception:
        _affinity_scope.set(None)


def get_affinity_scope() -> Optional[str]:
    """Return the declared routing/affinity scope, or ``None`` when unset."""
    return _affinity_scope.get()


def set_conversation_context(conversation_id: Optional[str]):
    """Publish the active conversation id for ambient Portal tagging.

    Called by the agent loop at turn entry with the conversation's stable
    id (the session-lineage ROOT id, so the tag survives context-compression
    session rotation). Pass ``None`` to clear. Returns the ContextVar token
    so callers can ``reset_conversation_context(token)`` on turn exit.
    """
    return _conversation_id.set(conversation_id or None)


def reset_conversation_context(token) -> None:
    """Restore the previous conversation context (pair with ``set_...``)."""
    try:
        _conversation_id.reset(token)
    except Exception:
        # Token from another Context (e.g. reset on a different thread) —
        # fall back to clearing rather than raising in cleanup paths.
        _conversation_id.set(None)


def get_conversation_context() -> Optional[str]:
    """Return the ambient conversation id, or ``None`` when unset."""
    return _conversation_id.get()


def _nastech_version() -> str:
    """Return the current Nastech release version, e.g. ``"0.13.0"``.

    Falls back to ``"unknown"`` if ``nastech_cli`` cannot be imported (should
    never happen in a real install — guarded for defensive testing).
    """
    try:
        from nastech_cli import __version__
        return __version__
    except Exception:
        return "unknown"


def nastech_client_tag() -> str:
    """Return the ``client=...`` tag for Nastech Portal requests.

    Format: ``client=nastech-client-v<MAJOR>.<MINOR>.<PATCH>``.
    """
    return f"client=nastech-client-v{_nastech_version()}"


def conversation_tag(session_id: str) -> str:
    """Return the ``conversation=...`` tag for a Nastech session/conversation.

    Format: ``conversation=<session_id>``. ``session_id`` is the canonical
    Nastech conversation identifier (``AIAgent.session_id``) — the same value
    used for ``~/.nastech/sessions/`` storage, session logs, and lineage.

    Unlike the product/client tags this is high-cardinality (one value per
    conversation), so it is only appended when a session id is actually
    available — never as part of the always-on base tag set.
    """
    return f"conversation={session_id}"


def nastech_portal_tags(session_id: str | None = None) -> List[str]:
    """Return the canonical list of Nastech Portal product tags.

    Always returns a fresh list so callers can mutate it freely
    (e.g. ``merged_extra.setdefault("tags", []).extend(nastech_portal_tags())``).

    When ``session_id`` is provided, a ``conversation=<session_id>`` tag is
    appended so Portal usage can be attributed to a specific Nastech
    conversation. When it is omitted, the ambient conversation context
    (``set_conversation_context``, published by the agent loop at turn
    entry) is used instead — this is how auxiliary calls (compression,
    titles, vision, MoA slots, ...) inherit the conversation tag without
    per-call-site plumbing. Callers outside any conversation (e.g. the
    auxiliary client's import-time base tags) get the canonical two-tag set.
    """
    tags = ["product=nastech-agent", nastech_client_tag()]
    # Ambient context first: the agent loop publishes the lineage ROOT id
    # (stable across context-compression rotation and delegate subagent
    # trees), which is the better conversation key than a per-segment
    # session_id passed explicitly. The explicit argument remains as a
    # fallback for callers running outside any agent turn.
    effective = get_conversation_context() or session_id
    if effective:
        tags.append(conversation_tag(effective))
    return tags
