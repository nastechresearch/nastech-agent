/**
 * Which persisted keys are machine-level UI preferences (#145213).
 *
 * Only these leave localStorage for the machine's shared store, so native
 * Desktop and every browser that opens this machine's Webapp show the same
 * choices. Scoped families keep their scope inside the key name (a
 * `….profile.<name>` or per-connection suffix): only the location changes.
 *
 * Deliberately NOT here (they stay in this browser/window):
 * - credentials, grants and connection config: gateway registry, custom model
 *   endpoints, plugin decisions and preview-script grants, embed permissions;
 * - per-window or per-device runtime state: layout tree, open tiles and tabs,
 *   last route/session, scroll, zoom, pet and popout geometry, keep-awake;
 * - drafts, queues, journals and caches: composer queue, in-flight turns,
 *   pending/prepared submissions, previews, pricing, backend skin cache, the
 *   "provider configured" onboarding cache (each backend answers that itself);
 * - one-off notices: butterbar, update and real-profile prompts.
 */

const SHARED_KEYS: ReadonlySet<string> = new Set([
  // Appearance.
  'nastech-desktop-theme-v2',
  'nastech-desktop-mode-v1',
  'nastech-desktop-profile-themes-v1',
  'nastech-desktop-profile-modes-v1',
  'nastech-desktop-user-themes-v1',
  'nastech.desktop.backdrop.v1',
  'nastech.desktop.chat-text-scale.v1',
  'nastech.desktop.interfaceMode.v1',
  'nastech.desktop.textDirection',
  'nastech.desktop.translucency.v2',
  'nastech.desktop.user-bubble-transparency.v1',
  // Sessions sidebar and profile rail.
  'nastech.desktop.agentsGroupedByWorkspace',
  'nastech.desktop.profileColors',
  'nastech.desktop.profileOrder',
  'nastech.desktop.profileRailVisible',
  'nastech.desktop.sessionListDensity',
  'nastech.desktop.sessionOrder',
  'nastech.desktop.sessionOrder.manual',
  'nastech.desktop.showAllProfiles',
  'nastech.desktop.sidebarAgentsGrouped.allProfiles',
  'nastech.desktop.sidebarCardRows',
  'nastech.desktop.sidebarGrouping',
  'nastech.desktop.sidebarGrouping.allProfiles',
  'nastech.desktop.sidebarRowMeta',
  'nastech.desktop.sidebarShowAllSessions',
  'nastech.desktop.sidebarShowArchived',
  'nastech.desktop.sidebarSortKey',
  // Status bar.
  'nastech.desktop.statusbarHidden.v2',
  'nastech.desktop.statusbarVisible.v2',
  // Transcript and tools.
  'nastech.desktop.hideThreadTimeline',
  'nastech.desktop.reasoning.collapsedByDefault',
  'nastech.desktop.toolView.hideCodeDiffs',
  'nastech.desktop.toolView.technical',
  // Shell, panes and behaviour.
  'nastech.desktop.alwaysExternalLinks.v1',
  'nastech.desktop.capabilities.catalogCardView',
  'nastech.desktop.composerPopout.enabled',
  'nastech.desktop.composerPopout.gesturesEnabled',
  'nastech.desktop.files.showIgnored',
  'nastech.desktop.keybinds',
  'nastech.desktop.layoutPresets.v2',
  'nastech.desktop.panesFlipped',
  'nastech.desktop.tabStripDefault',
  'nastech.desktop.titlebarAppActions',
  // Guidance: what the user already skipped, saw or dismissed does not come
  // back in every new browser or origin (#145600).
  'nastech-onboarding-skipped-v1',
  'nastech.desktop.tips.last.v1',
  'nastech.desktop.tips.next.v1',
  'nastech.desktop.tips.retired.v1',
  'nastech.desktop.tips.rotation.v1',
  'nastech.desktop.tips.shownAt.v1',
  'nastech.desktop.tours.v1',
  // Sound and media.
  'nastech.desktop.autoSpeakReplies',
  'nastech.desktop.completionSoundVariantId',
  'nastech.desktop.hapticsMuted',
  'nastech.desktop.videoPlaybackSpeed',
  // Model picker.
  'nastech.desktop.collapsed-providers',
  'nastech.desktop.favorite-models',
  // visible-models is a diff against known-models: they only make sense together.
  'nastech.desktop.known-models',
  'nastech.desktop.model-presets',
  'nastech.desktop.visible-models'
])

/** Families whose scope rides in the key suffix (gateway aliases/order/collapsed). */
const SHARED_PREFIXES: readonly string[] = ['nastech.desktop.sidebar.gatewayGroups.v1.']

export function isSharedPreferenceKey(key: string): boolean {
  return SHARED_KEYS.has(key) || SHARED_PREFIXES.some(prefix => key.startsWith(prefix))
}
