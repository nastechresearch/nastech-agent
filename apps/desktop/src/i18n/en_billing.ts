import type { BillingTranslations } from './types_billing'

// Out-of-credits overlay copy (Nastech vs. third-party providers), spread into en.ts.
export const enBilling: BillingTranslations = {
  billingBlock: {
    titleNastech: 'Out of Nastech credits',
    titleProvider: provider => `Out of credits — ${provider}`,
    fallbackMessage: 'Your account is out of credits. Add credits to keep going.',
    openBilling: 'Open billing',
    addCredits: 'Add credits',
    dismiss: 'Dismiss'
  }
}
