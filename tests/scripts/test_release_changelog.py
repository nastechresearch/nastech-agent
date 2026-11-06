"""The generated changelog is bounded by construction, for any range size.

A fork's first SemVer release can span tens of thousands of commits (this one:
~19,952 since the v0.21.5 seed). GitHub refuses a release body over
GITHUB_BODY_LIMIT characters, so the enumerated entries, the rendered line
length, and the contributor list are all capped, and a capped body declares
how many commits were omitted with a link to the full comparison. A small
range renders exactly as it always did — the cap must never distort it.
"""
import re


def _commit(index, subject, *, category="features", author="@dev", pr=None):
    sha = f"{index:040x}"
    return {
        "sha": sha, "short_sha": sha[:8], "author_name": "Dev", "author_email": "dev@example.test",
        "subject": f"{subject} (#{pr})" if pr else subject,
        "category": category, "github_author": author, "coauthors": [],
    }


def _listed_entries(body):
    """The rendered commit-entry lines: bullets that carry a link."""
    return [line for line in body.splitlines() if line.startswith("- ") and "](" in line]


def test_no_changelog_keeps_the_frame_without_commit_sections():
    from scripts import release

    commits = [{
        "sha": "a" * 40, "short_sha": "a" * 8, "author_name": "Dev", "author_email": "dev@example.test",
        "subject": "feat: something (#5)", "category": "features", "github_author": "@dev", "coauthors": [],
    }]

    body = release.generate_changelog(commits, "rc.1-v1.2.4", "1.2.4", repo_url="https://github.com/o/r",
                                      prev_tag="v1.2.3", no_changelog=True)

    assert "Something" not in body and "@dev" not in body
    assert "<!-- NASTECH_BUILDS_TABLE -->" in body
    assert "https://github.com/o/r/compare/v1.2.3...rc.1-v1.2.4" in body


def test_a_huge_range_yields_a_body_that_fits_github_and_declares_the_rest():
    """The bug: an unbounded commit list grows the draft body past GitHub's limit.

    The first real release of this fork ranges over ~19,952 commits; the
    generated body must fit GitHub's limit for ANY range, list only commits
    that are in the range, and state exactly how many it left out with a
    working comparison link.
    """
    from scripts import release
    from scripts.releases.draft_warning import draft_body
    from scripts.releases.entrypoint import GITHUB_BODY_LIMIT

    total = 5000
    # Newest first, like git log; long subjects make the raw render oversized.
    commits = [_commit(i, f"Sync upstream batch c{i:05d} " + "x" * 2000, pr=i)
               for i in range(total)]

    notes = release.generate_changelog(commits, "rc.1-v0.22.0", "0.22.0",
                                       repo_url="https://github.com/o/r", prev_tag="v0.21.5")
    body = draft_body(version="0.22.0", attempt_ref="rc.1-v0.22.0", notes=notes)

    assert len(body) <= GITHUB_BODY_LIMIT
    listed = len(_listed_entries(body))
    assert 0 < listed < total

    # The body states how many commits were omitted, and the number is true.
    claimed = re.search(r"([\d,]+) older commits are omitted", body)
    assert claimed, "a capped changelog must say how many commits it left out"
    assert int(claimed.group(1).replace(",", "")) == total - listed

    # The complete history stays reachable through the comparison link.
    assert "https://github.com/o/r/compare/v0.21.5...rc.1-v0.22.0" in body

    # Truthfulness: only the newest commits are enumerated; nothing outside
    # the listed window is claimed.
    assert f"c{0:05d}" in body and f"c{listed - 1:05d}" in body
    assert f"c{listed:05d}" not in body


def test_a_small_range_renders_in_full_exactly_as_before():
    """No regression for normal releases: every entry, PR/commit links, author
    attribution, and a contributor count over the whole (uncapped) range."""
    from scripts import release

    commits = [
        _commit(1, "New session resume", pr=5, author="@ada"),
        _commit(2, "Crash on empty history", category="fixes", author="@bo"),
        _commit(3, "Tune worker pool", category="chore", author="@teknium1"),
    ]

    body = release.generate_changelog(commits, "rc.1-v1.2.4", "1.2.4",
                                      repo_url="https://github.com/o/r", prev_tag="v1.2.3")

    # clean_subject strips conventional prefixes but keeps inline refs; the
    # attribution style is: subject, PR link, author.
    assert "- New session resume (#5) ([#5](https://github.com/o/r/pull/5)) — @ada" in body
    assert "- Crash on empty history " \
           f"([`{commits[1]['short_sha']}`](https://github.com/o/r/commit/{commits[1]['sha']})) — @bo" in body
    assert "- Tune worker pool " \
           f"([`{commits[2]['short_sha']}`](https://github.com/o/r/commit/{commits[2]['sha']}))" in body
    assert "commits are omitted" not in body
    assert "…and" not in body
    assert "- @ada (1 commit)" in body and "- @bo (1 commit)" in body
    assert "**Full Changelog**: [v1.2.3...rc.1-v1.2.4](https://github.com/o/r/compare/" \
           "v1.2.3...rc.1-v1.2.4)" in body


def test_a_single_monster_subject_is_truncated_with_a_marker_not_dropped():
    """Even one commit whose subject alone exceeds the body limit yields a
    body that fits, and the entry stays visible (ellipsis-marked)."""
    from scripts import release
    from scripts.releases.draft_warning import draft_body
    from scripts.releases.entrypoint import GITHUB_BODY_LIMIT

    commits = [_commit(1, "Sync upstream mega " + "x" * 200_000, author="@ada")]

    notes = release.generate_changelog(commits, "rc.1-v0.22.0", "0.22.0",
                                       repo_url="https://github.com/o/r", prev_tag="v0.21.5")
    body = draft_body(version="0.22.0", attempt_ref="rc.1-v0.22.0", notes=notes)

    assert len(body) <= GITHUB_BODY_LIMIT
    assert "Sync upstream mega" in body, "the entry must not be dropped silently"
    assert any("…" in line for line in _listed_entries(body)), "truncation must be visible"
