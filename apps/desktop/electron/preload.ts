import { contextBridge, ipcRenderer, webFrame, webUtils } from 'electron'

// Which translucency the OS can back. Asked synchronously because the renderer
// needs it before its first paint, and answered by main because deciding it
// needs `os.release()` — a sandboxed preload may only require electron, events,
// timers and url, so importing node:os here throws before contextBridge runs
// and takes the ENTIRE bridge down with it (window.nastechDesktop undefined =>
// "Desktop IPC bridge is unavailable"). No reply means no glass, which degrades
// to an ordinary opaque window rather than a page thinned over nothing.
const translucencySupport = ipcRenderer.sendSync('nastech:translucency:support')

contextBridge.exposeInMainWorld('nastechDesktop', {
  glassSupported: translucencySupport?.glass === true,
  translucencySupported: translucencySupport?.translucency === true,
  getConnection: profile => ipcRenderer.invoke('nastech:connection', profile),
  // Registry-scoped backend resolution: { connectionId, profile } → descriptor.
  getConnectionFor: payload => ipcRenderer.invoke('nastech:connection:for', payload),
  getProfileRoutes: profiles => ipcRenderer.invoke('nastech:plugin-profile-routes', profiles),
  revalidateConnection: () => ipcRenderer.invoke('nastech:connection:revalidate'),
  touchBackend: profile => ipcRenderer.invoke('nastech:backend:touch', profile),
  getGatewayWsUrl: profile => ipcRenderer.invoke('nastech:gateway:ws-url', profile),
  // Registry-scoped fresh WS URL: { connectionId, profile } → result shape of
  // getGatewayWsUrl, minted against that connection's backend.
  getGatewayWsUrlFor: payload => ipcRenderer.invoke('nastech:gateway:ws-url-for', payload),
  // Union agent roster across every registered connection.
  getAgentRoster: () => ipcRenderer.invoke('nastech:agents:roster'),
  openSessionWindow: (sessionId, opts) => ipcRenderer.invoke('nastech:window:openSession', sessionId, opts),
  openSessionInTerminal: (sessionId, opts) => ipcRenderer.invoke('nastech:window:openInTerminal', sessionId, opts),
  openWindow: () => ipcRenderer.invoke('nastech:window:openInstance'),
  claimAmbientCue: key => ipcRenderer.invoke('nastech:ambient:claim', key),
  wakeIndicator: {
    getState: () => ipcRenderer.invoke('nastech:wake-indicator:get'),
    setState: state => ipcRenderer.send('nastech:wake-indicator:set', state),
    onState: callback => {
      const listener = (_event, state) => callback(state)
      ipcRenderer.on('nastech:wake-indicator:state', listener)

      return () => ipcRenderer.removeListener('nastech:wake-indicator:state', listener)
    }
  },
  petOverlay: {
    // Main renderer → main process: window lifecycle + drag. `request` is
    // `{ bounds, screen }`; resolves with the screen bounds it actually used.
    open: request => ipcRenderer.invoke('nastech:pet-overlay:open', request),
    close: () => ipcRenderer.invoke('nastech:pet-overlay:close'),
    setBounds: bounds => ipcRenderer.send('nastech:pet-overlay:set-bounds', bounds),
    setIgnoreMouse: ignore => ipcRenderer.send('nastech:pet-overlay:ignore-mouse', ignore),
    // Flip the overlay focusable (and focus it) while the composer needs keys.
    setFocusable: focusable => ipcRenderer.send('nastech:pet-overlay:set-focusable', focusable),
    // Main renderer → overlay (forwarded by main): push the latest pet state.
    pushState: payload => ipcRenderer.send('nastech:pet-overlay:state', payload),
    // Overlay → main renderer (forwarded by main): pop back in / composer submit.
    control: payload => ipcRenderer.send('nastech:pet-overlay:control', payload),
    // Overlay subscribes to state pushes.
    onState: callback => {
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on('nastech:pet-overlay:state', listener)

      return () => ipcRenderer.removeListener('nastech:pet-overlay:state', listener)
    },
    // Main renderer subscribes to overlay control messages.
    onControl: callback => {
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on('nastech:pet-overlay:control', listener)

      return () => ipcRenderer.removeListener('nastech:pet-overlay:control', listener)
    }
  },
  // HUD mode: the chrome-free floating chat. A full app renderer (own gateway)
  // sized as a floating bar, so it mounts the real composer. Main owns the
  // window; `onChanged` keeps every window's toggle truthful.
  hud: {
    open: request => ipcRenderer.invoke('nastech:hud:open', request),
    close: () => ipcRenderer.invoke('nastech:hud:close'),
    setIgnoreMouse: ignore => ipcRenderer.send('nastech:hud:ignore-mouse', ignore),
    moveBy: delta => ipcRenderer.send('nastech:hud:move-by', delta),
    setBounds: bounds => ipcRenderer.send('nastech:hud:set-bounds', bounds),
    // Whether the band covers the window below the bar. Main pairs it with the
    // user's translucency setting to decide the native frost (macOS vibrancy /
    // Windows 11 DWM backdrop) — see hudFrostFor.
    setFrost: showing => ipcRenderer.invoke('nastech:hud:frost', showing),
    // The HUD tells main which session it is on; main hands that back to the
    // app window when the HUD closes, so the app can re-home onto it.
    setSession: sessionId => ipcRenderer.send('nastech:hud:session', sessionId),
    onGoto: callback => {
      const listener = (_event, sessionId) => callback(sessionId)
      ipcRenderer.on('nastech:hud:goto', listener)

      return () => ipcRenderer.removeListener('nastech:hud:goto', listener)
    },
    onChanged: callback => {
      const listener = (_event, state) => callback(state)
      ipcRenderer.on('nastech:hud:changed', listener)

      return () => ipcRenderer.removeListener('nastech:hud:changed', listener)
    },
    // Linux only, and silent elsewhere: where the cursor is, in page
    // coordinates, or null when it has left the window. Stands in for the
    // mousemove that `setIgnoreMouseEvents(true, { forward: true })` delivers on
    // macOS and Windows but not here.
    onCursor: callback => {
      const listener = (_event, point) => callback(point)
      ipcRenderer.on('nastech:hud:cursor', listener)

      return () => ipcRenderer.removeListener('nastech:hud:cursor', listener)
    }
  },
  // Quick Entry: the global-hotkey mini composer window. Main owns the OS
  // shortcut + the persisted preference; the quick window only captures text
  // and hands it back, and the primary renderer submits it through the normal
  // prompt path.
  quickEntry: {
    getSettings: () => ipcRenderer.invoke('nastech:quick-entry:settings:get'),
    setSettings: patch => ipcRenderer.invoke('nastech:quick-entry:settings:set', patch),
    submit: payload => ipcRenderer.send('nastech:quick-entry:submit', payload),
    dismiss: () => ipcRenderer.send('nastech:quick-entry:dismiss'),
    // Primary renderer → main → quick window: gateway connection state + the
    // recent-session options the target picker offers. Main caches the latest
    // payload so a freshly spawned quick window starts from truth.
    pushState: payload => ipcRenderer.send('nastech:quick-entry:state', payload),
    // Quick window subscribes to those pushes.
    onState: callback => {
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on('nastech:quick-entry:state', listener)

      return () => ipcRenderer.removeListener('nastech:quick-entry:state', listener)
    },
    // Main → primary renderer: a submit captured by the quick window.
    onSubmit: callback => {
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on('nastech:quick-entry:submit', listener)

      return () => ipcRenderer.removeListener('nastech:quick-entry:submit', listener)
    },
    // Main → quick window: you were just summoned (reset draft + refocus).
    onShown: callback => {
      const listener = () => callback()
      ipcRenderer.on('nastech:quick-entry:shown', listener)

      return () => ipcRenderer.removeListener('nastech:quick-entry:shown', listener)
    }
  },
  getBootProgress: () => ipcRenderer.invoke('nastech:boot-progress:get'),
  getConnectionConfig: profile => ipcRenderer.invoke('nastech:connection-config:get', profile),
  saveConnectionConfig: payload => ipcRenderer.invoke('nastech:connection-config:save', payload),
  applyConnectionConfig: payload => ipcRenderer.invoke('nastech:connection-config:apply', payload),
  testConnectionConfig: payload => ipcRenderer.invoke('nastech:connection-config:test', payload),
  // v2 multi-connection registry: named agent sources (local / remote / cloud / ssh).
  connections: {
    list: () => ipcRenderer.invoke('nastech:connections:list'),
    save: payload => ipcRenderer.invoke('nastech:connections:save', payload),
    remove: id => ipcRenderer.invoke('nastech:connections:remove', id),
    setPrimary: id => ipcRenderer.invoke('nastech:connections:set-primary', id),
    setLaunchMode: mode => ipcRenderer.invoke('nastech:connections:set-launch-mode', mode),
    setLastUsed: id => ipcRenderer.invoke('nastech:connections:set-last-used', id),
    test: id => ipcRenderer.invoke('nastech:connections:test', id),
    // Fan out `nastech update` to every eligible registered connection.
    // Optional excludeIds skips rows the caller updates through another path.
    updateAll: options => ipcRenderer.invoke('nastech:connections:update-all', options),
    // Registry lifecycle push (main → renderer): a connection was removed or
    // materially edited, so secondaries scoped to it must be disposed (and,
    // for edits, re-dialed at the new target).
    onChanged: callback => {
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on('nastech:connections:changed', listener)

      return () => ipcRenderer.removeListener('nastech:connections:changed', listener)
    }
  },
  sshConfigHosts: () => ipcRenderer.invoke('nastech:ssh-config:hosts'),
  sshResolveHost: host => ipcRenderer.invoke('nastech:ssh-config:resolve', host),
  probeConnectionConfig: remoteUrl => ipcRenderer.invoke('nastech:connection-config:probe', remoteUrl),
  oauthLoginConnectionConfig: remoteUrl => ipcRenderer.invoke('nastech:connection-config:oauth-login', remoteUrl),
  oauthLogoutConnectionConfig: remoteUrl => ipcRenderer.invoke('nastech:connection-config:oauth-logout', remoteUrl),
  // Nastech Cloud: one portal login powers discovery + silent per-agent sign-in
  // (cloud-auto-discovery Phase 3).
  cloud: {
    status: () => ipcRenderer.invoke('nastech:cloud:status'),
    login: () => ipcRenderer.invoke('nastech:cloud:login'),
    logout: () => ipcRenderer.invoke('nastech:cloud:logout'),
    discover: org => ipcRenderer.invoke('nastech:cloud:discover', org),
    agentSignIn: dashboardUrl => ipcRenderer.invoke('nastech:cloud:agent-sign-in', dashboardUrl)
  },
  profile: {
    get: () => ipcRenderer.invoke('nastech:profile:get'),
    set: name => ipcRenderer.invoke('nastech:profile:set', name)
  },
  api: request => ipcRenderer.invoke('nastech:api', request),
  notify: payload => ipcRenderer.invoke('nastech:notify', payload),
  requestMicrophoneAccess: () => ipcRenderer.invoke('nastech:requestMicrophoneAccess'),
  readWindowBelow: () => ipcRenderer.invoke('nastech:window:readBelow'),
  readFileDataUrl: filePath => ipcRenderer.invoke('nastech:readFileDataUrl', filePath),
  readFileDataUrlForAttach: filePath => ipcRenderer.invoke('nastech:readFileDataUrlForAttach', filePath),
  dataUrlReadMax: {
    get: () => ipcRenderer.invoke('nastech:data-url-read-max:get'),
    set: maxMb => ipcRenderer.invoke('nastech:data-url-read-max:set', maxMb)
  },
  readFileText: filePath => ipcRenderer.invoke('nastech:readFileText', filePath),
  selectPaths: options => ipcRenderer.invoke('nastech:selectPaths', options),
  selectSavePath: options => ipcRenderer.invoke('nastech:selectSavePath', options),
  writeClipboard: text => ipcRenderer.invoke('nastech:writeClipboard', text),
  readClipboard: () => ipcRenderer.invoke('nastech:readClipboard'),
  saveGatewayFile: payload => ipcRenderer.invoke('nastech:saveGatewayFile', payload),
  saveImageFromUrl: url => ipcRenderer.invoke('nastech:saveImageFromUrl', url),
  contextMenuEdit: command => ipcRenderer.invoke('nastech:context-menu:edit', command),
  contextMenuCopyImage: () => ipcRenderer.invoke('nastech:context-menu:copy-image'),
  contextMenuSpellcheck: action => ipcRenderer.invoke('nastech:context-menu:spellcheck', action),
  contextMenuGuestAddWord: payload => ipcRenderer.invoke('nastech:context-menu:guest-add-word', payload),
  onContextMenuSpellcheck: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('nastech:context-menu-spellcheck', listener)

    return () => ipcRenderer.removeListener('nastech:context-menu-spellcheck', listener)
  },
  saveImageBuffer: (data, ext) => ipcRenderer.invoke('nastech:saveImageBuffer', { data, ext }),
  saveClipboardImage: () => ipcRenderer.invoke('nastech:saveClipboardImage'),
  getPathForFile: file => {
    try {
      return webUtils.getPathForFile(file) || ''
    } catch {
      return ''
    }
  },
  normalizePreviewTarget: (target, baseDir) => ipcRenderer.invoke('nastech:normalizePreviewTarget', target, baseDir),
  watchPreviewFile: url => ipcRenderer.invoke('nastech:watchPreviewFile', url),
  watchDirectory: dir => ipcRenderer.invoke('nastech:watchDirectory', dir),
  stopPreviewFileWatch: id => ipcRenderer.invoke('nastech:stopPreviewFileWatch', id),
  setActiveWork: payload => ipcRenderer.send('nastech:active-work', payload),
  setTitleBarTheme: payload => ipcRenderer.send('nastech:titlebar-theme', payload),
  setNativeTheme: mode => ipcRenderer.send('nastech:native-theme', mode),
  setTranslucency: payload => ipcRenderer.send('nastech:translucency', payload),
  setKeepAwake: on => ipcRenderer.send('nastech:keep-awake', on),
  setDisableF12: blocked => ipcRenderer.send('nastech:devtools:disable-f12', blocked),
  setPreviewShortcutActive: active => ipcRenderer.send('nastech:previewShortcutActive', Boolean(active)),
  openExternal: url => ipcRenderer.invoke('nastech:openExternal', url),
  openPreviewInBrowser: url => ipcRenderer.invoke('nastech:openPreviewInBrowser', url),
  reachPreviewUrl: url => ipcRenderer.invoke('nastech:preview:reach', url),
  fetchLinkTitle: url => ipcRenderer.invoke('nastech:fetchLinkTitle', url),
  sanitizeWorkspaceCwd: cwd => ipcRenderer.invoke('nastech:workspace:sanitize', cwd),
  settings: {
    getDefaultProjectDir: () => ipcRenderer.invoke('nastech:setting:defaultProjectDir:get'),
    setDefaultProjectDir: dir => ipcRenderer.invoke('nastech:setting:defaultProjectDir:set', dir),
    pickDefaultProjectDir: () => ipcRenderer.invoke('nastech:setting:defaultProjectDir:pick')
  },
  zoom: {
    // Current zoom of this window, as { level, percent }.
    get: () => ipcRenderer.invoke('nastech:zoom:get'),
    // Synchronous zoom factor (1 = 100%). Coordinate math needs it in the
    // same tick as the event it converts, so no IPC round-trip here.
    factor: () => webFrame.getZoomFactor(),
    setPercent: percent => ipcRenderer.send('nastech:zoom:set-percent', percent),
    // Fires on every zoom change, including the Ctrl/Cmd +/-/0 shortcuts,
    // so the settings UI can stay in sync with the keyboard.
    onChanged: callback => {
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on('nastech:zoom:changed', listener)

      return () => ipcRenderer.removeListener('nastech:zoom:changed', listener)
    }
  },
  revealLogs: () => ipcRenderer.invoke('nastech:logs:reveal'),
  getRecentLogs: () => ipcRenderer.invoke('nastech:logs:recent'),
  // Fire-and-forget: persists a renderer error-boundary catch (with component
  // stack) to desktop.log so crashes survive the window (#79428).
  reportRendererError: report => ipcRenderer.send('nastech:logs:renderer-error', report),
  readDir: dirPath => ipcRenderer.invoke('nastech:fs:readDir', dirPath),
  gitRoot: startPath => ipcRenderer.invoke('nastech:fs:gitRoot', startPath),
  revealPath: targetPath => ipcRenderer.invoke('nastech:fs:reveal', targetPath),
  openDir: dirPath => ipcRenderer.invoke('nastech:fs:openDir', dirPath),
  desktopPluginsRoot: () => ipcRenderer.invoke('nastech:fs:desktopPluginsRoot'),
  agentPluginsRoot: () => ipcRenderer.invoke('nastech:fs:agentPluginsRoot'),
  renamePath: (targetPath, newName) => ipcRenderer.invoke('nastech:fs:rename', targetPath, newName),
  writeTextFile: (filePath, content) => ipcRenderer.invoke('nastech:fs:writeText', filePath, content),
  trashPath: targetPath => ipcRenderer.invoke('nastech:fs:trash', targetPath),
  git: {
    worktreeList: repoPath => ipcRenderer.invoke('nastech:git:worktreeList', repoPath),
    worktreeAdd: (repoPath, options) => ipcRenderer.invoke('nastech:git:worktreeAdd', repoPath, options),
    worktreeRemove: (repoPath, worktreePath, options) =>
      ipcRenderer.invoke('nastech:git:worktreeRemove', repoPath, worktreePath, options),
    branchSwitch: (repoPath, branch) => ipcRenderer.invoke('nastech:git:branchSwitch', repoPath, branch),
    branchList: repoPath => ipcRenderer.invoke('nastech:git:branchList', repoPath),
    baseBranchList: repoPath => ipcRenderer.invoke('nastech:git:baseBranchList', repoPath),
    repoStatus: repoPath => ipcRenderer.invoke('nastech:git:repoStatus', repoPath),
    fileDiff: (repoPath, filePath) => ipcRenderer.invoke('nastech:git:fileDiff', repoPath, filePath),
    scanRepos: (roots, options) => ipcRenderer.invoke('nastech:git:scanRepos', roots, options),
    review: {
      list: (repoPath, scope, baseRef) => ipcRenderer.invoke('nastech:git:review:list', repoPath, scope, baseRef),
      diff: (repoPath, filePath, scope, baseRef, staged) =>
        ipcRenderer.invoke('nastech:git:review:diff', repoPath, filePath, scope, baseRef, staged),
      stage: (repoPath, filePath) => ipcRenderer.invoke('nastech:git:review:stage', repoPath, filePath),
      unstage: (repoPath, filePath) => ipcRenderer.invoke('nastech:git:review:unstage', repoPath, filePath),
      revert: (repoPath, filePath) => ipcRenderer.invoke('nastech:git:review:revert', repoPath, filePath),
      revParse: (repoPath, ref) => ipcRenderer.invoke('nastech:git:review:revParse', repoPath, ref),
      commit: (repoPath, message, push) => ipcRenderer.invoke('nastech:git:review:commit', repoPath, message, push),
      commitContext: repoPath => ipcRenderer.invoke('nastech:git:review:commitContext', repoPath),
      push: repoPath => ipcRenderer.invoke('nastech:git:review:push', repoPath),
      shipInfo: repoPath => ipcRenderer.invoke('nastech:git:review:shipInfo', repoPath),
      prList: (repoPath, branches, numbers) =>
        ipcRenderer.invoke('nastech:git:review:prList', repoPath, branches, numbers),
      fetchPrComment: (repoPath, url) => ipcRenderer.invoke('nastech:git:review:fetchPrComment', repoPath, url),
      createPr: repoPath => ipcRenderer.invoke('nastech:git:review:createPr', repoPath)
    }
  },
  terminal: {
    cwd: id => ipcRenderer.invoke('nastech:terminal:cwd', id),
    dispose: id => ipcRenderer.invoke('nastech:terminal:dispose', id),
    resize: (id, size) => ipcRenderer.invoke('nastech:terminal:resize', id, size),
    start: options => ipcRenderer.invoke('nastech:terminal:start', options),
    write: (id, data) => ipcRenderer.invoke('nastech:terminal:write', id, data),
    onData: (id, callback) => {
      const channel = `nastech:terminal:${id}:data`
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on(channel, listener)

      return () => ipcRenderer.removeListener(channel, listener)
    },
    onExit: (id, callback) => {
      const channel = `nastech:terminal:${id}:exit`
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on(channel, listener)

      return () => ipcRenderer.removeListener(channel, listener)
    }
  },
  onClosePreviewRequested: callback => {
    const listener = () => callback()
    ipcRenderer.on('nastech:close-preview-requested', listener)

    return () => ipcRenderer.removeListener('nastech:close-preview-requested', listener)
  },
  onPreviewNav: callback => {
    const listener = (_event, command) => callback(command)
    ipcRenderer.on('nastech:preview-nav', listener)

    return () => ipcRenderer.removeListener('nastech:preview-nav', listener)
  },
  onOpenFolderRequested: callback => {
    const listener = () => callback()
    ipcRenderer.on('nastech:open-folder-requested', listener)

    return () => ipcRenderer.removeListener('nastech:open-folder-requested', listener)
  },
  onOpenUpdatesRequested: callback => {
    const listener = () => callback()
    ipcRenderer.on('nastech:open-updates', listener)

    return () => ipcRenderer.removeListener('nastech:open-updates', listener)
  },
  onDeepLink: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('nastech:deep-link', listener)

    return () => ipcRenderer.removeListener('nastech:deep-link', listener)
  },
  signalDeepLinkReady: () => ipcRenderer.invoke('nastech:deep-link-ready'),
  probePluginRepo: payload => ipcRenderer.invoke('nastech:plugin:probe', payload),
  installDesktopPlugin: payload => ipcRenderer.invoke('nastech:plugin:installDesktop', payload),
  onWindowStateChanged: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('nastech:window-state-changed', listener)

    return () => ipcRenderer.removeListener('nastech:window-state-changed', listener)
  },
  onFocusSession: callback => {
    const listener = (_event, sessionId) => callback(sessionId)
    ipcRenderer.on('nastech:focus-session', listener)

    return () => ipcRenderer.removeListener('nastech:focus-session', listener)
  },
  onNotificationAction: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('nastech:notification-action', listener)

    return () => ipcRenderer.removeListener('nastech:notification-action', listener)
  },
  onNotificationActivate: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('nastech:notification-activate', listener)

    return () => ipcRenderer.removeListener('nastech:notification-activate', listener)
  },
  onPreviewFileChanged: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('nastech:preview-file-changed', listener)

    return () => ipcRenderer.removeListener('nastech:preview-file-changed', listener)
  },
  onBackendExit: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('nastech:backend-exit', listener)

    return () => ipcRenderer.removeListener('nastech:backend-exit', listener)
  },
  // Soft gateway-mode apply finished tearing down the primary backend. Renderer
  // should wipe session lists + re-dial without a window reload.
  onConnectionApplied: callback => {
    const listener = () => callback()
    ipcRenderer.on('nastech:connection:applied', listener)

    return () => ipcRenderer.removeListener('nastech:connection:applied', listener)
  },
  onPowerResume: callback => {
    const listener = () => callback()
    ipcRenderer.on('nastech:power-resume', listener)

    return () => ipcRenderer.removeListener('nastech:power-resume', listener)
  },
  // AC ↔ battery transitions; renderers slow their backstop polls on battery.
  getOnBattery: () => ipcRenderer.invoke('nastech:power-battery:get'),
  onBatteryChanged: callback => {
    const listener = (_event, onBattery) => callback(Boolean(onBattery))
    ipcRenderer.on('nastech:power-battery', listener)

    return () => ipcRenderer.removeListener('nastech:power-battery', listener)
  },
  onBootProgress: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('nastech:boot-progress', listener)

    return () => ipcRenderer.removeListener('nastech:boot-progress', listener)
  },
  // First-launch bootstrap progress -- emitted by the install.ps1 stage
  // runner in main.ts (apps/desktop/electron/bootstrap-runner.ts).
  // Renderer's install overlay subscribes to live events and queries the
  // current snapshot via getBootstrapState() to recover after a devtools
  // reload mid-bootstrap.
  getBootstrapState: () => ipcRenderer.invoke('nastech:bootstrap:get'),
  continueBootstrapLocal: () => ipcRenderer.invoke('nastech:bootstrap:continue-local'),
  resetBootstrap: () => ipcRenderer.invoke('nastech:bootstrap:reset'),
  repairBootstrap: () => ipcRenderer.invoke('nastech:bootstrap:repair'),
  cancelBootstrap: () => ipcRenderer.invoke('nastech:bootstrap:cancel'),
  onBootstrapEvent: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('nastech:bootstrap:event', listener)

    return () => ipcRenderer.removeListener('nastech:bootstrap:event', listener)
  },
  getVersion: () => ipcRenderer.invoke('nastech:version'),
  getRemoteDisplayReason: () => ipcRenderer.invoke('nastech:get-remote-display-reason'),
  uninstall: {
    summary: () => ipcRenderer.invoke('nastech:uninstall:summary'),
    run: mode => ipcRenderer.invoke('nastech:uninstall:run', { mode })
  },
  updates: {
    check: () => ipcRenderer.invoke('nastech:updates:check'),
    apply: opts => ipcRenderer.invoke('nastech:updates:apply', opts),
    getBranch: () => ipcRenderer.invoke('nastech:updates:branch:get'),
    setBranch: name => ipcRenderer.invoke('nastech:updates:branch:set', name),
    onProgress: callback => {
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on('nastech:updates:progress', listener)

      return () => ipcRenderer.removeListener('nastech:updates:progress', listener)
    }
  },
  themes: {
    fetchMarketplace: id => ipcRenderer.invoke('nastech:vscode-theme:fetch', id),
    searchMarketplace: query => ipcRenderer.invoke('nastech:vscode-theme:search', query)
  },
  // Find-in-page (Ctrl/Cmd+F): delegates to Electron's
  // webContents.findInPage on the IPC sender's window so a Cmd+F pressed
  // in a secondary session window searches THAT window, not the primary.
  // `onFoundInPage` returns the unsubscribe fn; the renderer wires it via
  // `initFindInPageListener` in store/find-in-page.ts and tears it down
  // when the FindBar unmounts.
  findInPage: (query, options) => ipcRenderer.invoke('nastech:find-in-page', query, options),
  stopFindInPage: () => ipcRenderer.invoke('nastech:stop-find-in-page'),
  onFoundInPage: callback => {
    const listener = (_event, result) => callback(result)
    ipcRenderer.on('nastech:found-in-page', listener)

    return () => ipcRenderer.removeListener('nastech:found-in-page', listener)
  },
  // Main-process `before-input-event` forwards Ctrl/Cmd+F here so renderer
  // can open the FindBar even when the GTK compositor has already grabbed
  // the chord at the windowing layer (#81727).
  onOpenFindBarRequested: callback => {
    const listener = () => callback()
    ipcRenderer.on('nastech:open-find-bar', listener)

    return () => ipcRenderer.removeListener('nastech:open-find-bar', listener)
  }
})
