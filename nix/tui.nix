# Self-contained Nastech TUI, compiled by the same recipe as npm.
{ nastechNpmLib, ... }:
nastechNpmLib.buildNpmPackage {
  dirs = [
    "ui-tui"
    "apps/shared"
    "scripts/build/tui.mjs"
    "scripts/build/freshness.mjs"
    "scripts/build/frontend-common.mjs"
  ];

  doCheck = false;

  buildPhase = ''
    runHook preBuild
    node scripts/build/tui.mjs --source "$PWD" --out "$TMPDIR/tui-product"
    runHook postBuild
  '';

  installPhase = ''
    runHook preInstall
    mkdir -p $out/lib/nastech-tui
    cp -r "$TMPDIR/tui-product/." $out/lib/nastech-tui/
    runHook postInstall
  '';
}
