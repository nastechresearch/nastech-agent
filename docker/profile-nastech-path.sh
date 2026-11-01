# shellcheck shell=sh
# Installed as /etc/profile.d/nastech.sh. Debian's /etc/profile resets PATH for
# every login shell (`bash -l`, `docker exec <c> bash -l`, ssh, the terminal
# tool's background `bash -lic`), dropping the image's ENV PATH dirs, so bare
# `nastech` exits 127 there. Put them back in the ENV PATH order; dirs a login
# PATH already lists keep their position.
for __nastech_p in /opt/data/.local/bin /opt/nastech/.venv/bin /opt/nastech/bin; do
    case ":$PATH:" in
        *":$__nastech_p:"*) ;;
        *) PATH="$__nastech_p:$PATH" ;;
    esac
done
unset __nastech_p
export PATH
