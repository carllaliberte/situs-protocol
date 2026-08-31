# Discord ← GitHub

Pas de bot Discord dans QUANTUM. Un webhook, secret, **échec seulement**.

## Toi (2 min)

1. Serveur Discord → Paramètres → Intégrations → Webhooks → Nouveau
2. Canal `#situs-alerte` (crée-le). Copie l'URL.
3. GitHub → chaque repo → Settings → Secrets → Actions → `DISCORD_WEBHOOK`
   - [situs-protocol](https://github.com/carllaliberte/situs-protocol/settings/secrets/actions)
   - [unforge](https://github.com/carllaliberte/unforge/settings/secrets/actions)
   - [unforge-check](https://github.com/carllaliberte/unforge-check/settings/secrets/actions)
4. Relance `garde` (Actions → Run workflow) pour tester. Un échec volontaire ping. Un vert se tait.

N'ajoute pas `/github` à l'URL.
Ne colle jamais le webhook dans un fichier.

## Autre voie (events Git, pas CI)

Discord → Intégrations → GitHub : relie le compte, choisis le canal, coche Issues / PR. Ça ne remplace pas le secret CI.
