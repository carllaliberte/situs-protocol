# Bots SITUS

Aucun bot n'est owner. Aucun bot ne scelle un lieu réel. Aucun bot n'ouvre QUANTUM.

## GitHub Actions

| Workflow | Déclencheur Git |
|---|---|
| `garde` | push `main`, PR |
| `filtre` | push `main`, PR |

## Grok — quoi sonne où

| Bot | Git | Notif |
|---|---|---|
| `situs-ci-casse` | `garde` fail | app + mail |
| `unforge-ci-casse` | `rigueur` fail | app + mail |
| `unforge-check-ci-casse` | `check` fail | app + mail |
| `situs-garde-secrets` | lundi 09:45 | app + mail |
| `github-revue-hebdo` | lundi 09:30 | app + mail |
| `situs-push` | push main proto | app seulement |
| `situs-pr` | PR proto | app seulement |
| `unforge-situs-push` | push main nœud | app seulement |
| `unforge-pr` | PR nœud | app seulement |
| `unforge-check-pr` | PR check | app seulement |

CI cassée = mail. Push quotidien = pas de mail.

## Cloche GitHub (toi, 30 s)

L'intégration n'a pas le droit `notifications`. À faire une fois :

1. [situs-protocol Watch](https://github.com/carllaliberte/situs-protocol) → All activity
2. [unforge Watch](https://github.com/carllaliberte/unforge) → All activity
3. [unforge-check Watch](https://github.com/carllaliberte/unforge-check) → All activity
4. GitHub → Settings → Notifications → Actions : e-mail si **failed** seulement

Reconnecter le connecteur GitHub avec le droit notifications si tu veux que Grok lise la cloche.
