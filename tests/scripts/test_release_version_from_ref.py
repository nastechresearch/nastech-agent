"""A ref names a version, and the next version is derived, never read from the tree.

Derivation reads the published stable head, or the seeded line before one exists.
Attempt refs number attempts within a version and never move the line.
"""
import json
import math
import subprocess

import pytest

from scripts.releases.versioning import derive_next_version, next_attempt, tag_record, version_from_tag


def test_final_tag_is_its_version():
    assert version_from_tag("v0.21.5") == "0.21.5"


@pytest.mark.parametrize("ref", [
    "v0.21.5-rc",
    "v0.21.4+canary.20260922T001400Z",
    "v2026.9.21",
    "canary-0.21.4+canary.20260922T001400Z",
    "v0.0.7+channel.20260922T001400Z.98765",
    "v0.0.0+commit.20260922T001400Z.98766",
])
def test_non_final_refs_are_not_versions(ref):
    assert version_from_tag(ref) is None


def test_attempt_ref_carries_version_and_attempt():
    from scripts.releases.versioning import parse_attempt_ref

    assert parse_attempt_ref("rc.1-v0.21.5") == ("0.21.5", 1)
    assert parse_attempt_ref("rc.12-v1.0.0") == ("1.0.0", 12)


def test_marker_ref_names_the_attempt_it_clears():
    from scripts.releases.versioning import parse_marker_ref

    assert parse_marker_ref("abandoned-rc.1-v0.21.5") == ("0.21.5", 1)
    assert parse_marker_ref("rc.1-v0.21.5") is None


@pytest.mark.parametrize("ref", [
    "v0.21.5-rc", "v0.21.5-rc.1", "rc.01-v0.21.5", "rc.0-v0.21.5",
    "rc.1-v2026.9.21", "v0.21.5", "abandoned-rc.1-v0.21.5",
    "rc.1-v0.21.5+canary.20260922T001400Z", "rc.1-v0.21", "rc.-v0.21.5",
])
def test_attempt_ref_rejects_other_shapes(ref):
    from scripts.releases.versioning import parse_attempt_ref

    assert parse_attempt_ref(ref) is None


def test_attempt_and_marker_refs_round_trip():
    from scripts.releases.versioning import attempt_ref, marker_ref, parse_attempt_ref, parse_marker_ref

    assert parse_attempt_ref(attempt_ref("0.21.5", 3)) == ("0.21.5", 3)
    assert parse_marker_ref(marker_ref("0.21.5", 3)) == ("0.21.5", 3)


@pytest.mark.parametrize("version, attempt", [("2026.9.21", 1), ("0.21.5", 0), ("0.21", 1)])
def test_attempt_ref_refuses_what_it_could_not_parse(version, attempt):
    from scripts.releases.versioning import attempt_ref

    with pytest.raises(ValueError):
        attempt_ref(version, attempt)


def test_next_attempt_counts_cleared_attempts_and_skips_other_shapes():
    refs = ["rc.1-v0.21.5", "abandoned-rc.1-v0.21.5", "rc.2-v0.21.6",
            "v0.21.5-rc", "v2026.9.21", "abandoned-rc.4-v0.21.5"]
    assert next_attempt("0.21.5", refs) == 2
    assert next_attempt("0.21.6", refs) == 3
    assert next_attempt("0.21.7", refs) == 1


def test_canary_compares_equal_to_its_stable():
    from scripts.releases.semver import compare, is_canary_version
    assert is_canary_version("0.21.4+canary.20260922T001400Z")
    assert compare("0.21.4+canary.20260922T001400Z", "0.21.4") == 0


def test_empty_head_seeds_the_line():
    """Before the first published release, the line continues from the seed.

    Asserted against the seed instead of its number: the seed names the newest
    upstream stable the tree carries, so it moves with every sync and a literal
    here would go red on each one.
    """
    from scripts.releases.versioning import BUMPS, SEED

    for bump in BUMPS:
        assert derive_next_version(published=None, bump=bump) == derive_next_version(
            published=SEED, bump=bump)


def test_published_head_spends_its_version():
    assert derive_next_version(published="0.21.5", bump="patch") == "0.21.6"


def test_canary_base_comes_from_the_validated_protected_stable_head():
    from scripts.releases.versioning import published_stable_version

    class Reader:
        def __init__(self, base, repository):
            assert base == "https://assets.example"
            assert repository == "example/nastech-agent"

        def resolve(self, name):
            assert name == "stable"
            return type("Resolution", (), {
                "terminal": {"policy": "stable-release"},
                "manifest": {"request": {"version": "0.21.7", "commit": "a" * 40}},
            })()

    assert published_stable_version(
        "example/nastech-agent", base_url="https://assets.example", reader_type=Reader,
        run=lambda argv: "[[]]",
    ) == "0.21.7"


def test_a_newer_published_release_outranks_the_protected_head():
    """A release that skipped bundles never moves the R2 head, but it still spends its version."""
    from scripts.releases.versioning import published_stable_identity

    class Reader:
        def __init__(self, base, repository):
            pass

        def resolve(self, name):
            return type("Resolution", (), {
                "terminal": {"policy": "stable-release"},
                "manifest": {"request": {"version": "0.21.7", "commit": "a" * 40}},
            })()

    releases = [
        {"tag_name": "v0.21.8", "draft": False, "prerelease": False},
        # Drafts, prereleases and CalVer labels are not published stable releases.
        {"tag_name": "v0.21.9", "draft": True, "prerelease": False},
        {"tag_name": "v0.21.8+canary.20260924T000000Z", "draft": False, "prerelease": True},
        {"tag_name": "v2026.9.24", "draft": False, "prerelease": False},
    ]

    def run(argv):
        if argv[:4] == ["gh", "api", "--paginate", "--slurp"]:
            return json.dumps([releases])
        assert argv[:2] == ["gh", "api"] and argv[3:] == ["--jq", ".sha"]
        return {"repos/example/nastech-agent/commits/v0.21.8": "b" * 40,
                "repos/example/nastech-agent/commits/v0.21.6": "c" * 40}[argv[2]]

    assert published_stable_identity(
        "example/nastech-agent", base_url="https://assets.example", reader_type=Reader, run=run,
    ) == ("0.21.8", "b" * 40)
    releases[0]["tag_name"] = "v0.21.6"
    assert published_stable_identity(
        "example/nastech-agent", base_url="https://assets.example", reader_type=Reader, run=run,
    ) == ("0.21.7", "a" * 40)


def test_the_version_read_retries_only_the_shared_rate_limit():
    """Canary run 42049972593 died on one 403 from the installation budget every
    concurrent check shares: a queue position, not an answer about versions."""
    from scripts.releases.versioning import _gh

    attempts = []

    def run(argv, **kwargs):
        attempts.append(argv)
        if len(attempts) < 3:
            return subprocess.CompletedProcess(
                argv, 1, "", "gh: API rate limit exceeded for installation (HTTP 403)")
        return subprocess.CompletedProcess(argv, 0, "[]", "")

    assert _gh(["gh", "api", "repos/example/nastech-agent/releases"],
               run=run, sleep=lambda _s: None) == "[]"
    assert len(attempts) == 3


def test_a_real_answer_fails_once_and_keeps_ghs_message(capsys):
    from scripts.releases.versioning import _gh

    attempts = []

    def run(argv, **kwargs):
        attempts.append(argv)
        return subprocess.CompletedProcess(argv, 1, "", "gh: Not Found (HTTP 404)")

    with pytest.raises(subprocess.CalledProcessError):
        _gh(["gh", "api", "repos/example/nastech-agent/releases"], run=run, sleep=lambda _s: None)
    assert len(attempts) == 1
    assert "Not Found" in capsys.readouterr().err


def test_the_version_read_gives_every_gh_child_a_deadline():
    """A child that never answers must not hold the release forever, on any attempt."""
    from scripts.releases.versioning import _gh

    seen = []

    def run(argv, **kwargs):
        seen.append(kwargs.get("timeout"))
        if len(seen) < 2:
            return subprocess.CompletedProcess(
                argv, 1, "", "gh: API rate limit exceeded (HTTP 403)")
        return subprocess.CompletedProcess(argv, 0, "[]", "")

    assert _gh(["gh", "api", "repos/example/nastech-agent/releases"],
               run=run, sleep=lambda _s: None) == "[]"
    assert len(seen) == 2
    assert all(isinstance(t, (int, float)) and math.isfinite(t) and t > 0 for t in seen)


def test_a_hung_gh_child_surfaces_its_deadline_on_the_first_attempt():
    """A hang is not a queue position: it propagates, never retried as a rate limit."""
    from scripts.releases.versioning import _gh

    attempts = []

    def run(argv, **kwargs):
        attempts.append(kwargs["timeout"])
        raise subprocess.TimeoutExpired(argv, kwargs["timeout"])

    with pytest.raises(subprocess.TimeoutExpired) as excinfo:
        _gh(["gh", "api", "repos/example/nastech-agent/releases"], run=run, sleep=lambda _s: None)
    assert len(attempts) == 1
    assert excinfo.value.timeout == attempts[0]


def test_outstanding_attempts_is_the_one_shared_predicate():
    from scripts.releases.versioning import outstanding_attempts

    refs = ["rc.1-v0.21.5", "abandoned-rc.1-v0.21.5", "rc.2-v0.21.5",
            "rc.1-v0.21.6", "v0.21.5", "rc.1-v0.21.7"]
    published = {"0.21.6", "0.21.7"}

    def is_published(version):
        return version in published

    assert outstanding_attempts(refs, is_published) == [("0.21.5", 2, "rc.2-v0.21.5")]


def test_tag_record_reads_the_record_a_signature_is_appended_to():
    """git keeps a tag signature inside the message body, so ``%(contents)`` is
    the record followed by the armor. The record is what precedes it."""
    record = {"attempt": 19, "autopublish": False, "claimEpoch": 1790701941,
              "commit": "3" * 40, "schema": 1, "skipBundles": False, "skipTests": True,
              "version": "0.21.5"}
    record_text = json.dumps(record, sort_keys=True, separators=(",", ":"))

    assert tag_record(record_text) == record
    for armor in ("-----BEGIN SSH SIGNATURE-----", "-----BEGIN PGP SIGNATURE-----"):
        assert tag_record(f"{record_text}\n{armor}\nAAAA\n") == record


def test_tag_record_refuses_a_message_that_is_not_a_record():
    with pytest.raises(json.JSONDecodeError):
        tag_record("not a record\n-----BEGIN SSH SIGNATURE-----\nAAAA\n")
