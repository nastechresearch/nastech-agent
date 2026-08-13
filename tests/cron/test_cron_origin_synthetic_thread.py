"""Cron origin capture: Slack per-message session-key threads are not routing.

Bug report (relay-fronted Slack, thread-per-message mode): creating a cron job
from a top-level Slack DM message persisted the creation message's own id as
``origin.thread_id`` — the relay adapter stamps ``source.thread_id = message_id``
on every top-level Slack message purely for SESSION KEYING (native SlackAdapter
parity: ``thread_ts = event.thread_ts or ts``). Every subsequent cron delivery
then landed inside the ephemeral thread spawned around the creation message
instead of the top-level conversation / configured home.

The stamp is recognizable at capture time: a Slack session whose thread id
equals the triggering message's own id is a synthetic per-message key, not a
durable thread. A genuine in-thread creation has thread_id == the parent
thread's id != the triggering message's own id, and must keep its thread.
"""

from unittest.mock import patch

from tools.cronjob_tools import _origin_from_env


def _session_env(env: dict):
    """Patch gateway.session_context.get_session_env with a dict lookup."""
    return patch(
        "gateway.session_context.get_session_env",
        side_effect=lambda name, default="": env.get(name, default),
    )


class TestSlackSyntheticThreadCapture:
    def test_synthetic_slack_thread_not_captured(self):
        """thread_id == message_id on Slack = per-message session key: drop it."""
        env = {
            "NASTECH_SESSION_PLATFORM": "slack",
            "NASTECH_SESSION_CHAT_ID": "D0BJTDCSR7C",
            "NASTECH_SESSION_THREAD_ID": "1755043010.123456",
            "NASTECH_SESSION_MESSAGE_ID": "1755043010.123456",
        }
        with _session_env(env):
            origin = _origin_from_env()
        assert origin is not None
        assert origin["platform"] == "slack"
        assert origin["chat_id"] == "D0BJTDCSR7C"
        assert origin["thread_id"] is None

    def test_genuine_slack_thread_preserved(self):
        """A real in-thread creation (thread != own message id) keeps its thread."""
        env = {
            "NASTECH_SESSION_PLATFORM": "slack",
            "NASTECH_SESSION_CHAT_ID": "C0AGENERAL",
            "NASTECH_SESSION_THREAD_ID": "1755040000.000100",
            "NASTECH_SESSION_MESSAGE_ID": "1755043010.123456",
        }
        with _session_env(env):
            origin = _origin_from_env()
        assert origin is not None
        assert origin["thread_id"] == "1755040000.000100"

    def test_non_slack_platform_thread_untouched(self):
        """Telegram forum topics legitimately reuse ids; the rule is Slack-scoped."""
        env = {
            "NASTECH_SESSION_PLATFORM": "telegram",
            "NASTECH_SESSION_CHAT_ID": "-1003941067111",
            "NASTECH_SESSION_THREAD_ID": "2203",
            "NASTECH_SESSION_MESSAGE_ID": "2203",
        }
        with _session_env(env):
            origin = _origin_from_env()
        assert origin is not None
        assert origin["thread_id"] == "2203"

    def test_slack_no_message_id_keeps_thread(self):
        """Without a message id to compare, never guess: keep the thread."""
        env = {
            "NASTECH_SESSION_PLATFORM": "slack",
            "NASTECH_SESSION_CHAT_ID": "D0BJTDCSR7C",
            "NASTECH_SESSION_THREAD_ID": "1755040000.000100",
        }
        with _session_env(env):
            origin = _origin_from_env()
        assert origin is not None
        assert origin["thread_id"] == "1755040000.000100"
