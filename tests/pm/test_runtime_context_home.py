"""Context-only homes use the same dependency state as their own process."""

from pm import environments as runtime_paths
from pm.publication import PluginSelection
from nastech_cli.runtime_state import recover_publication, runtime_lock
from nastech_constants import reset_nastech_home_override, set_nastech_home_override
from pm import paths, plugins_state


def test_context_home_publication_recovers_from_its_own_process(tmp_path, monkeypatch):
    process_home = tmp_path / "process-home"
    context_home = tmp_path / "context-home"
    context_home.mkdir()
    project = tmp_path / "repo"
    project.mkdir()
    config = context_home / "config.yaml"
    original = b"plugins:\n  enabled: [old]\n"
    config.write_bytes(original)
    monkeypatch.setenv("NASTECH_HOME", str(process_home))
    monkeypatch.setattr(paths, "repo_root", lambda: project)
    process_state = runtime_paths.install_state_dir(project)
    token = set_nastech_home_override(context_home)
    try:
        context_state = runtime_paths.install_state_dir(project)
        assert context_state != process_state
        assert plugins_state.enabled_plugins_ordered() == {
            context_home / "plugins": ["old"],
        }
        with runtime_lock(project):
            PluginSelection({"home": str(config.parent), "enabled": ["new"], "disabled": []}).publish(project)
        assert config.read_bytes() != original
    finally:
        reset_nastech_home_override(token)

    assert not process_state.exists()
    monkeypatch.setenv("NASTECH_HOME", str(context_home))
    assert runtime_paths.install_state_dir(project) == context_state
    with runtime_lock(project):
        recover_publication(project)
    assert config.read_bytes() == original
    assert not (context_state / "publication.json").exists()


def test_named_context_profile_shares_its_install_root(tmp_path, monkeypatch):
    home = tmp_path / "home"
    profile = home / "profiles" / "worker"
    profile.mkdir(parents=True)
    monkeypatch.setenv("NASTECH_HOME", str(home))
    project = tmp_path / "repo"
    state = runtime_paths.install_state_dir(project)
    token = set_nastech_home_override(profile)
    try:
        assert runtime_paths.install_state_dir(project) == state
    finally:
        reset_nastech_home_override(token)
