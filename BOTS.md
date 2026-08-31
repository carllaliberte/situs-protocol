# Bots SITUS

Aucun bot n'est owner. Aucun bot ne scelle un lieu réel. Aucun bot n'ouvre QUANTUM.

## GitHub Actions

| Workflow | Déclencheur Git |
|---|---|
| `garde` | push `main`, PR |

## Grok

| Bot | Déclencheur Git |
|---|---|
| `situs-push` | push `main` situs-protocol |
| `situs-pr` | PR ouverte situs-protocol |
| `situs-ci-casse` | workflow `garde` = failure |
| `situs-garde-secrets` | cron lundi (pas Git) |
| `unforge-situs-push` | push `main` unforge |
| `unforge-pr` | PR ouverte unforge |
| `unforge-ci-casse` | workflow `rigueur` = failure |
| `unforge-check-ci-casse` | workflow `check` = failure |
| `unforge-check-pr` | PR ouverte unforge-check |
| `github-revue-hebdo` | cron lundi |

Carl seulement : `owner.txt`, Scaniverse, bloc OTS, révoquer un lieu.
