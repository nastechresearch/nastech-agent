# venv-style activation of the Nastech dev environment for fish.
#
#   source ./activate.fish
#
# The fish counterpart of ./activate: applies the composed pm env to the
# CURRENT shell, with save/restore (`deactivate` undoes exactly what activation
# changed), makes `nastech` a function for this checkout, and prefixes the prompt
# with the worktree name. Scripts and other processes run under
# `scripts/run-in-nastech-env` instead.
#
# Options: `--test-extras a,b` selects the test environment's runtime extras
# (default: [all]).
#
# Composition (setup sync, bootstrap Python, pm env) is shared with ./activate
# through scripts/_activation.sh, so this file only applies its output.

set -l repo (path resolve (path dirname (status filename)))

argparse 'test-extras=' -- $argv
or return 2
set -l test_environment --test-environment
if set -q _flag_test_extras
    set test_environment --test-environment=$_flag_test_extras
end

set -l library '. "$1/scripts/_activation.sh"'
bash -c "$library; nastech_sync \"\$1\" \"\$2\"" _ $repo $test_environment >&2
or begin
    echo 'activate.fish: setup failed; shell environment unchanged' >&2
    return 1
end

# Re-activating deactivates first, as ./activate does.
functions -q deactivate
and deactivate

set -l composed (bash -c "$library; nastech_compose_env \"\$1\" fish" _ $repo)
or begin
    echo 'activate.fish: could not compose the environment (see above)' >&2
    return 1
end

# --- snapshot what we are about to change (deactivate restores this) ---
set -g __nastech_keys (string replace -rf '^set -gx (\S+) .*' '$1' -- $composed)
for name in $__nastech_keys
    if set -q $name
        set -g __nastech_had_$name 1
        set -g __nastech_prior_$name $$name
    end
end
string join \n -- $composed | source

# This checkout, not whichever `nastech` PATH finds. A function beats PATH.
set -g __nastech_worktree $repo
# The branch names the worktree. A checkout cannot share a branch with another.
set -g __nastech_worktree_name (git -C $repo rev-parse --abbrev-ref HEAD 2>/dev/null)
if test -z "$__nastech_worktree_name" -o "$__nastech_worktree_name" = HEAD
    set __nastech_worktree_name (path basename $repo)
end

function __nastech_worktree_here
    set -l top (git rev-parse --show-toplevel 2>/dev/null)
    or return 1
    test (path resolve $top) = (path resolve $__nastech_worktree)
end

function nastech --description 'nastech of the activated checkout'
    if not __nastech_worktree_here
        echo "nastech: $PWD is outside $__nastech_worktree; refusing (the installed command is hidden while this checkout is active)" >&2
        return 1
    end
    set -l python python
    if set -q PYTHON
        set python $PYTHON
    else if test -x $__nastech_worktree/.venv/bin/python
        set python $__nastech_worktree/.venv/bin/python
    else if test -x $__nastech_worktree/venv/bin/python
        set python $__nastech_worktree/venv/bin/python
    end
    pushd $__nastech_worktree >/dev/null
    $python nastech $argv
    set -l code $status
    popd >/dev/null
    return $code
end

functions -c fish_prompt __nastech_saved_fish_prompt
function fish_prompt
    if __nastech_worktree_here
        printf '(%s) ' $__nastech_worktree_name
    end
    __nastech_saved_fish_prompt
end

function deactivate --description 'undo activate.fish'
    for name in $__nastech_keys
        set -l had __nastech_had_$name
        set -l prior __nastech_prior_$name
        if set -q $had
            set -gx $name $$prior
        else
            set -eg $name
        end
        set -eg $had $prior
    end
    functions -e fish_prompt
    functions -c __nastech_saved_fish_prompt fish_prompt
    functions -e __nastech_saved_fish_prompt
    set -eg __nastech_keys __nastech_worktree __nastech_worktree_name
    functions -e deactivate nastech __nastech_worktree_here
end
