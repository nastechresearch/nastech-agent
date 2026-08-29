import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'

import { registry } from '@/contrib/registry'

import { allPaneIds, group, split } from './model'
import {
  $hiddenStripTabs,
  $hiddenTreePanes,
  $layoutTree,
  closeAllTreeTabs,
  hideOnlyZoneTabs,
  isHideOnlyPane,
  revealTreePane,
  setStripTabHidden,
  setTreeGroupTabStrip,
  tabStripVisibleForGroup,
  treeTabCloseTargets
} from './store'

vi.mock('@/store/notifications', () => ({ notify: vi.fn() }))

import { notify } from '@/store/notifications'

const disposers: (() => void)[] = []

function registerPane(id: string, data: Record<string, unknown>) {
  disposers.push(registry.register({ area: 'panes', data, id, render: () => null, title: id }))
}

/** The SESSIONS | BOTS shape: both hide-only chrome tabs stacked in one zone. */
function sessionsBotsTree() {
  registerPane('sessions', { placement: 'left', hideOnly: true })
  registerPane('nastech-bots:pane', { placement: 'left', hideOnly: true })
  registerPane('workspace', { placement: 'main', uncloseable: true })
  $layoutTree.set(
    split('row', [
      group(['sessions', 'nastech-bots:pane'], { active: 'sessions', id: 'g-side' }),
      group(['workspace'], { active: 'workspace', id: 'g-main' })
    ])
  )
}

beforeEach(() => {
  window.localStorage.clear()
  $hiddenStripTabs.set(new Set())
  $hiddenTreePanes.set(new Set())
  vi.mocked(notify).mockReset()
})

afterEach(() => {
  disposers.splice(0).forEach(dispose => dispose())
})

describe('hide-only strip tabs', () => {
  it('hides and shows a chrome tab, keeping the pane in the tree', () => {
    sessionsBotsTree()

    expect(setStripTabHidden('nastech-bots:pane', true)).toBe(true)
    expect($hiddenTreePanes.get()).toContain('nastech-bots:pane')
    expect($hiddenStripTabs.get()).toContain('nastech-bots:pane')
    // Hidden, not dismissed: the pane stays in the layout tree.
    expect(allPaneIds($layoutTree.get()!)).toContain('nastech-bots:pane')

    expect(setStripTabHidden('nastech-bots:pane', false)).toBe(true)
    expect($hiddenTreePanes.get()).not.toContain('nastech-bots:pane')
    expect($hiddenStripTabs.get()).not.toContain('nastech-bots:pane')
  })

  it('refuses to hide the zone last visible tab', () => {
    sessionsBotsTree()
    setStripTabHidden('nastech-bots:pane', true)

    // Sessions is now the only visible tab in the zone — the hide is refused
    // and the user is told, so the zone can never become an empty dead strip.
    expect(setStripTabHidden('sessions', true)).toBe(false)
    expect($hiddenTreePanes.get()).not.toContain('sessions')
    expect(vi.mocked(notify)).toHaveBeenCalledTimes(1)
  })

  it('persists hides and clears them on reveal', () => {
    sessionsBotsTree()
    setStripTabHidden('nastech-bots:pane', true)

    const persisted = JSON.parse(window.localStorage.getItem('nastech.desktop.hiddenStripTabs.v1') ?? '[]')

    expect(persisted).toContain('nastech-bots:pane')

    // Reveal intent (⌘K toggle on, a programmatic reveal) beats the hide —
    // including the persisted record, so the tab can't pop back hidden on the
    // next launch while visibly on screen now.
    revealTreePane('nastech-bots:pane')
    expect($hiddenTreePanes.get()).not.toContain('nastech-bots:pane')
    expect(window.localStorage.getItem('nastech.desktop.hiddenStripTabs.v1')).toBeNull()
  })

  it('lists the zone hide-only tabs with live hidden state for the menu', () => {
    sessionsBotsTree()
    setStripTabHidden('nastech-bots:pane', true)

    expect(hideOnlyZoneTabs('g-side')).toEqual([
      { hidden: false, id: 'sessions', title: 'sessions' },
      { hidden: true, id: 'nastech-bots:pane', title: 'nastech-bots:pane' }
    ])
    expect(hideOnlyZoneTabs('g-main')).toEqual([])
  })

  it('refuses to hide the strip that is the only handle for hide-only tabs', () => {
    sessionsBotsTree()
    setTreeGroupTabStrip('g-side', 'never')

    const side = $layoutTree.get()
    const group = side && side.type === 'split' ? side.children[0] : side

    expect(group && group.type === 'group' ? tabStripVisibleForGroup(group) : false).toBe(true)
  })

  it('excludes hide-only tabs from every close verb', () => {
    registerPane('sessions', { placement: 'left', hideOnly: true })
    registerPane('nastech-bots:pane', { placement: 'left', hideOnly: true })
    registerPane('session-tile:x', { placement: 'main' })
    $layoutTree.set(group(['sessions', 'nastech-bots:pane', 'session-tile:x'], { active: 'sessions', id: 'g-mixed' }))

    expect(isHideOnlyPane('sessions')).toBe(true)
    // Close-others measured from the tile must not sweep standing chrome.
    expect(treeTabCloseTargets('session-tile:x')).toEqual({ all: 1, others: 0, right: 0 })
    // Close-all leaves both chrome tabs in the tree.
    closeAllTreeTabs('sessions')
    expect(allPaneIds($layoutTree.get()!)).toContain('sessions')
    expect(allPaneIds($layoutTree.get()!)).toContain('nastech-bots:pane')
    expect(allPaneIds($layoutTree.get()!)).not.toContain('session-tile:x')
  })
})
