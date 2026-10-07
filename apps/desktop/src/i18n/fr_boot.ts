import type { TranslationOverrides } from './define-locale'

// The boot screen's copy (including the update-hold screen), composed by fr.ts.
export const frBoot = {
  boot: {
    ready: 'Nastech Desktop est prêt',
    desktopBootFailedWithMessage: message => `Échec du démarrage : ${message}`,
    steps: {
      connectingGateway: 'Connexion au gateway desktop',
      loadingSettings: 'Chargement des paramètres Nastech',
      loadingSessions: 'Chargement des sessions récentes',
      retryingRemoteBackend: 'Reconnexion au backend Nastech distant…',
      startingDesktopConnection: 'Démarrage de la connexion desktop',
      startingNastechDesktop: 'Démarrage de Nastech Desktop…'
    },
    errors: {
      backgroundExited: "Le processus en arrière-plan de Nastech s'est arrêté.",
      backgroundExitedDuringStartup: "Le processus en arrière-plan de Nastech s'est arrêté pendant le démarrage.",
      backendStopped: 'Backend arrêté',
      restartNastech: 'Redémarrer Nastech',
      openLogs: 'Ouvrir les journaux',
      desktopBootFailed: 'Échec du démarrage',
      gatewayConnectionLost: 'Connexion au gateway perdue',
      gatewayConnectionLostDetail:
        'Nouvelle tentative en arrière-plan. Vous pouvez continuer à lire et rédiger — ouvrez les paramètres du gateway si le problème persiste.',
      reconnectNow: 'Se reconnecter maintenant',
      connectionSettings: 'Paramètres de connexion',
      gatewaySignInRequired: 'Connexion au gateway requise',
      gatewaySignInRequiredDetail:
        'Reconnectez-vous pour rétablir la connexion. Vos conversations et paramètres sont en sécurité.',
      signInAgain: 'Se reconnecter',
      ipcBridgeUnavailable: 'Le pont IPC du desktop est indisponible.'
    },
    causes: {
      exitedEarly: "Le service en arrière-plan de Nastech s'est arrêté juste après son démarrage.",
      timedOut: "Le service en arrière-plan de Nastech n'a pas répondu à temps.",
      permission: "Nastech n'a pas pu écrire dans son dossier de données (problème d'autorisation).",
      diskFull: "Le disque est plein ; Nastech n'a donc pas pu démarrer.",
      portInUse: 'Un autre programme utilise le port réseau nécessaire à Nastech.',
      installMissing:
        "Une partie de l'installation de Nastech est manquante. Choisissez Réparer l'installation pour la restaurer."
    },
    failure: {
      title: "Nastech n'a pas pu démarrer",
      description:
        "Le gateway en arrière-plan n'a pas pu se lancer. Essayez l'une des étapes de récupération ci-dessous. Rien ici ne supprime vos conversations ou paramètres.",
      details: 'Détails',
      remoteTitle: 'Connexion au gateway distante requise',
      remoteDescription:
        'Votre session de gateway distante a expiré. Connectez-vous à nouveau pour vous reconnecter. Rien ici ne supprime vos conversations ou paramètres.',
      retry: 'Réessayer',
      repairInstall: "Réparer l'installation",
      useLocalGateway: 'Utiliser le gateway local',
      gatewaySettings: 'Paramètres du gateway',
      back: 'Retour',
      openLogs: 'Ouvrir les journaux',
      repairHint: "La réparation relance l'installateur et peut prendre quelques minutes sur une machine neuve.",
      remoteSignInHint: signInLabel =>
        `Déconnecte la session navigateur distante enregistrée, puis ouvre ${signInLabel}. Utilisez le gateway local pour passer au backend intégré.`,
      signOutAndSignIn: 'Se déconnecter et se reconnecter',
      remoteFailureHint:
        "Vérifiez l'URL du gateway et la connexion dans les paramètres du gateway, ou passez au gateway local.",
      cloudDownTitle: "L'agent Nastech Cloud est indisponible",
      cloudDownDescription:
        "L'agent cloud géré par Nastech auquel ce gateway se connecte renvoie une erreur serveur. Il ne peut pas être redémarré depuis ici — vérifiez son état, passez au gateway local ou contactez l'assistance.",
      cloudDownHint:
        "Les boutons ci-dessous ouvrent le portail Nastech, pour consulter et contrôler l'instance, ainsi que notre Discord pour obtenir de l'aide.",
      cloudDownCheckPortal: "Vérifier l'état sur le portail",
      cloudDownDiscord: "Obtenir de l'aide sur Discord",
      hideRecentLogs: 'Masquer les journaux récents',
      showRecentLogs: 'Afficher les journaux récents',
      signedInTitle: 'Connecté',
      signedInMessage: 'Reconnexion au gateway distante…',
      signInIncompleteTitle: 'Connexion incomplète',
      signInIncompleteMessage: "La fenêtre de connexion s'est fermée avant la fin de l'authentification.",
      signInFailed: 'Échec de la connexion',
      signInToRemoteGateway: 'Se connecter au gateway distante',
      signInWithProvider: provider => `Se connecter avec ${provider}`,
      identityProvider: "votre fournisseur d'identité"
    },
    updateHold: {
      title: 'Une mise à jour précédente bloque encore Nastech',
      titleUnverified: 'Nastech ne peut pas confirmer la fin de la dernière mise à jour',
      description:
        "Nastech attend avant de démarrer pour ne pas charger des fichiers qu'une mise à jour modifie peut-être encore. Il démarre tout seul dès que le blocage cesse.",
      heldByProcess: pid =>
        `La mise à jour (processus ${pid}) s'est terminée, mais un processus qu'elle a lancé bloque encore l'installation de Nastech.`,
      heldUnknown:
        "Une mise à jour s'est terminée, mais un processus qu'elle a lancé bloque encore l'installation de Nastech.",
      unverified:
        "L'assistant de mise à jour n'a pas pu vérifier qui détient l'installation de Nastech. Nastech continue de vérifier.",
      since: time => `En attente depuis ${time}`,
      lastChecked: time => `Dernière vérification ${time}`,
      recoveryHint:
        "Cela se règle généralement en quelques minutes. Sinon : quittez Nastech, arrêtez les processus git ou nastech restants (ou redémarrez l'ordinateur), puis rouvrez Nastech.",
      checkAgain: 'Vérifier à nouveau',
      quit: 'Quitter Nastech',
      openLogs: 'Ouvrir les journaux',
      startAnyway: 'Démarrer quand même…',
      confirmTitle: 'Démarrer Nastech alors que la mise à jour le bloque encore ?',
      confirmBody:
        'Le processus de mise à jour restant modifie peut-être encore les fichiers de Nastech. Démarrer maintenant peut charger une installation à moitié mise à jour, qui risque de ne pas fonctionner avant une nouvelle mise à jour. Nastech consigne ce choix dans son journal et laisse le marqueur de mise à jour en place.',
      confirmKeepWaiting: 'Continuer à attendre',
      confirmStart: 'Démarrer quand même',
      startAnywayRefused:
        "Ce qui bloque l'installation a changé avant que Nastech puisse démarrer. Vérifiez et réessayez."
    }
  }
} satisfies Pick<TranslationOverrides, 'boot'>
