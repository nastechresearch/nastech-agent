import { type MutableRefObject, useCallback, useRef, useState } from 'react'

import { setTerminalFontFamilyFromConfig } from '@/app/right-sidebar/terminal/terminal-font'
import { BUILTIN_PERSONALITIES, normalizePersonalityValue, personalityNamesFromConfig } from '@/lib/chat-runtime'
import { normalize } from '@/lib/text'
import { getNastechConfig, getNastechConfigDefaults } from '@/nastech'
import { setDisplayTimestampsFromConfig } from '@/store/display-timestamps'
import {
  getComposerSelectionGeneration,
  getCurrentModelSource,
  setAvailablePersonalities,
  setCurrentFastMode,
  setCurrentPersonality,
  setCurrentReasoningEffort,
  setCurrentServiceTier,
  setDefaultReasoningEffort,
  setIntroPersonality
} from '@/store/session'
import {
  applyAutoSpeakFromConfig,
  applyThinkingSoundFromConfig,
  applyVoiceStopPhraseFromConfig
} from '@/store/voice-prefs'

const DEFAULT_VOICE_SECONDS = 120
const FAST_TIERS = new Set(['fast', 'priority', 'on'])

function recordingLimit(value: unknown) {
  return typeof value === 'number' && Number.isFinite(value) && value > 0 ? value : DEFAULT_VOICE_SECONDS
}

/** config.yaml hands back whatever the user wrote — `reasoning_effort: false`
 *  (or `off`/`no`, which YAML also parses to boolean false) means thinking
 *  disabled, and a bare boolean must not throw on `.trim()`. */
function normalizeConfigEffort(value: unknown): string {
  if (value === false) {
    return 'none'
  }

  if (typeof value !== 'string') {
    return ''
  }

  const effort = normalize(value)

  return effort === 'false' || effort === 'disabled' ? 'none' : effort
}

interface NastechConfigOptions {
  activeSessionIdRef: MutableRefObject<string | null>
}

export function useNastechConfig({ activeSessionIdRef }: NastechConfigOptions) {
  const [voiceMaxRecordingSeconds, setVoiceMaxRecordingSeconds] = useState(DEFAULT_VOICE_SECONDS)
  const [sttEnabled, setSttEnabled] = useState(true)
  const profileRefreshEpochRef = useRef(0)

  const refreshNastechConfig = useCallback(
    async (force = false) => {
      if (force) {
        profileRefreshEpochRef.current += 1
      }

      const profileRefreshEpoch = profileRefreshEpochRef.current
      const selectionGeneration = getComposerSelectionGeneration()

      try {
        const [config, defaults] = await Promise.all([getNastechConfig(), getNastechConfigDefaults().catch(() => ({}))])

        if (profileRefreshEpochRef.current !== profileRefreshEpoch) {
          return
        }

        const personality = normalizePersonalityValue(
          typeof config.display?.personality === 'string' ? config.display.personality : ''
        )

        setIntroPersonality(personality)
        // Active sessions keep their per-session value; standalone falls back to config.
        setCurrentPersonality(prev => (activeSessionIdRef.current ? prev || personality : personality))
        setAvailablePersonalities([
          ...new Set([
            'none',
            ...BUILTIN_PERSONALITIES,
            ...personalityNamesFromConfig(defaults),
            ...personalityNamesFromConfig(config)
          ])
        ])

        const reasoning = normalizeConfigEffort(config.agent?.reasoning_effort)
        const tier = (config.agent?.service_tier ?? '').trim()

        // Publish the profile default regardless of whether the composer is
        // reseeded below: picker rows and preset application resolve "the
        // default" from here, so a manual model pick must not leave them
        // rendering/applying Nastech' built-in medium over the user's config.
        setDefaultReasoningEffort(reasoning)

        const shouldSeedComposer =
          !activeSessionIdRef.current &&
          getComposerSelectionGeneration() === selectionGeneration &&
          (force || getCurrentModelSource() !== 'manual')

        if (shouldSeedComposer) {
          setCurrentReasoningEffort(reasoning)
          setCurrentFastMode(FAST_TIERS.has(tier.toLowerCase()))
        }

        setCurrentServiceTier(prev => (activeSessionIdRef.current ? prev : tier))

        setVoiceMaxRecordingSeconds(recordingLimit(config.voice?.max_recording_seconds))
        setSttEnabled(config.stt?.enabled !== false)
        setDisplayTimestampsFromConfig(config.display?.timestamps)
        setTerminalFontFamilyFromConfig(config.terminal?.font_family)
        applyAutoSpeakFromConfig(config)
        applyVoiceStopPhraseFromConfig(config)
        applyThinkingSoundFromConfig(config)
      } catch {
        // Config is nice-to-have; chat still works without it.
      }
    },
    [activeSessionIdRef]
  )

  return { refreshNastechConfig, sttEnabled, voiceMaxRecordingSeconds }
}
