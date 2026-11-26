import type { ApprovalCopy } from './types_approval'

export const frApproval: Partial<ApprovalCopy> = {
  gatewayDisconnected: "La Gateway Nastech n'est pas connectée",
  sendFailed: "Impossible d'envoyer la réponse d'approbation",
  reconnect: 'Se reconnecter',
  timedOutSystemLine:
    "Le délai d'approbation a expiré — la commande n'a pas été exécutée. Demandez à Nastech de réessayer ou augmentez la limite dans Paramètres → Sécurité → Délai d'approbation.",
  openSafetySettings: 'Ouvrir les paramètres de sécurité',
  run: 'Exécuter',
  command: 'Commande',
  moreOptions: "Plus d'options d'approbation",
  allowSession: 'Autoriser cette session',
  alwaysAllowMenu: 'Toujours autoriser…',
  jumpToApproval: 'Approbation requise',
  reject: 'Rejeter',
  alwaysTitle: 'Toujours autoriser cette commande ?',
  alwaysDescription: pattern =>
    `Cela ajoute le motif « ${pattern} » à votre liste d'autorisation permanente (~/.nastech/config.yaml). Nastech ne redemandera plus pour ce type de commande — que ce soit dans cette session ou dans une session future.`,
  alwaysAllow: 'Toujours autoriser',
  deny: 'Refuser',
  allow: 'Autoriser',
  allowHint: 'Jusqu’à la désactivation du bac à sable',
  denyReason: 'Motif du refus',
  denyReasonPlaceholder: 'Dites à Nastech pourquoi (facultatif)',
  access: {
    title: 'Accès au dossier',
    readOnly: 'Lecture seule',
    readWrite: 'Lecture et écriture',
    timedOut: folder =>
      `Le délai de la demande a expiré — l'accès au dossier ${folder} n'a pas été accordé. Demandez à Nastech de réessayer.`,
    alwaysTitle: 'Toujours autoriser ce dossier ?',
    alwaysDescription: 'Le dossier est ajouté au bac à sable de ce profil. Nastech ne le redemandera dans aucun chat.'
  },
  network: {
    title: 'Accès au site',
    timedOut: site =>
      `Le délai de la demande a expiré — l'accès à ${site} n'a pas été accordé. Demandez à Nastech de réessayer.`,
    alwaysTitle: 'Toujours autoriser ce site ?',
    alwaysDescription: 'Le site est ajouté aux sites autorisés de ce profil. Nastech ne le redemandera dans aucun chat.'
  }
}
