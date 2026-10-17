import type { Usage } from '@nastech/shared/gateway-events'

export { usageFromTick } from '@nastech/shared/usage-tick'

export const ZERO: Usage = { calls: 0, input: 0, output: 0, total: 0 }
