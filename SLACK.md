# Slack ← GitHub

Pas de Slack dans QUANTUM. Un incoming webhook, secret, **échec seulement**.

## Toi (2 min)

1. [Incoming Webhooks](https://api.slack.com/messaging/webhooks) → Add to Slack → canal `#situs-alerte`
2. Copie l'URL `hooks.slack.com/services/...`
3. GitHub → Settings → Secrets → Actions → `SLACK_WEBHOOK`
   - [situs-protocol](https://github.com/carllaliberte/situs-protocol/settings/secrets/actions)
   - [unforge](https://github.com/carllaliberte/unforge/settings/secrets/actions)
   - [unforge-check](https://github.com/carllaliberte/unforge-check/settings/secrets/actions)
4. Relance `garde`. Vert = silence. Rouge = un message.

Ne commite jamais l'URL.

## App officielle (events, pas CI)

[GitHub pour Slack](https://slack.github.com) : `/github subscribe carllaliberte/situs-protocol` dans le canal.
Coche `fails` seulement si tu ne veux pas le bruit des pushes.
