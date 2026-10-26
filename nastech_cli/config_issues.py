"""The issue record config validation emits (``nastech config check``, doctor, startup warnings).

Its own module so the facade (``nastech_cli.config``) and its check siblings share it without
a facade import from the siblings."""

from dataclasses import dataclass


@dataclass
class ConfigIssue:
    """A detected config structure problem."""
    severity: str  # "error", "warning"
    message: str
    hint: str


def _issue(issues: list[ConfigIssue], severity: str, message: str, hint: str) -> None:
    issues.append(ConfigIssue(severity, message, hint))
