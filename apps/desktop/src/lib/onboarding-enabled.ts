export function isOnboardingEnabled(): boolean {
  return window.nastechDesktop?.guestOnboardingEnabled === true
}
