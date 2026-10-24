# nix/devShell.nix — Dev shell that delegates setup to each package
#
# Each npm workspace package exposes passthru.packageJsonPath (e.g.
# "ui-tui/package.json").  This file collects them all and passes the
# list to mkNpmDevShellHook, which stamps all package.jsons at once,
# then runs a single `npm i --package-lock-only` if any changed and
# `npm ci` if the lockfile changed.
{ ... }:
{
  perSystem =
    { pkgs, lib, self', ... }:
    let
      packages = builtins.attrValues self'.packages;
      nastechNpmLib = self'.packages.default.passthru.nastechNpmLib;

      # Collect all packageJsonPath values from npm workspace packages.
      npmPackageJsonPaths = builtins.filter (p: p != null) (
        map (p: p.passthru.packageJsonPath or null) packages
      );

      nastechAgentDevShellHook = self'.packages.default.passthru.devShellHook;
    in
    {
      devShells.default = pkgs.mkShell {
        packages = with pkgs; [
          (pkgs.runCommand "nastech" { } ''
            mkdir -p $out/bin
            install -Dm755 ${../nastech} $out/bin/nastech
          '')
          self'.packages.sandbox
        ]
        # Wayland-only: cage and ghostty pull alsa-lib, which does not
        # evaluate on darwin.
        ++ lib.optionals pkgs.stdenv.hostPlatform.isLinux [
          # Headless Wayland compositor for E2E tests (test:e2e:visual).
          # cage renders a single client with no window management, so
          # the Electron window opens at a fixed size without tiling.
          # libglvnd provides libEGL.so.1 that cage needs on NixOS.
          cage
          libglvnd
          # Graphical terminal + Wayland screenshot client for CLI/TUI UI
          # evidence. `cage -- ghostty ...` keeps captures off the user's
          # live compositor; grim runs inside that isolated client session.
          ghostty
          grim
        ]
        ++ self'.packages.default.passthru.devDeps;
        shellHook = ''
          # The editable venv's .pth resolves the checkout through this.
          export NASTECH_PYTHON_SRC_ROOT=$(git rev-parse --show-toplevel)

          ${nastechAgentDevShellHook}
          ${nastechNpmLib.mkNpmDevShellHook npmPackageJsonPaths}

          # Force Node to use Nix's playwright-test binary instead of node_modules/.bin
          export PATH="${pkgs.playwright-test}/bin:$PATH"

          # The lock's interpreter is python-build-standalone, whose OpenSSL has
          # no compiled-in NixOS trust store; point it at the CA bundle so
          # urllib/httpx/requests verify certificates like the nixpkgs one.
          export SSL_CERT_FILE="${pkgs.cacert}/etc/ssl/certs/ca-bundle.crt"
          export NIX_SSL_CERT_FILE="$SSL_CERT_FILE"

          echo "Nastech Agent dev shell in $NASTECH_PYTHON_SRC_ROOT"
          echo "Ready. Run 'nastech' or 'sandbox nastech' to start."
        '';
      };
    };
}
