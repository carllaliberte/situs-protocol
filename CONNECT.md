# SITUS Connect

Une prise. Pas un cloud.

L'entreprise tourne **son** nœud (QUANTUM) ou vérifie hors-ligne.
Carl n'héberge rien. Ce dépôt publie le contrat.

OpenAPI : [`connect/openapi.v0.yaml`](connect/openapi.v0.yaml)

## Trois routes

| Route | Quoi |
|---|---|
| `POST /v0/autoriser` | empreinte + usage → `allow` \| `deny` \| `urgent` |
| `POST /v0/verifier` | carte + sha256 du scan → sceau intact ? |
| `GET /v0/licence/{empreinte}` | usages publics + `revoque` — zéro path, zéro owner |

Jamais le splat. Jamais `owner.txt`. Jamais le dialogue client.

## Brancher (entreprise)

1. Téléphone : Scaniverse + `owner.txt` + `python3 -m quantum situs-auto`
2. Servir **ces trois routes** devant `quantum.db` (loopback ou VPN interne)
3. Un lab appelle `autoriser` avec `usage=train` avant d'entraîner

Si `deny` : le lab n'a pas le droit. Point.

## Base URL

Il n'y en a pas ici. Exemple local :

```
http://127.0.0.1:8765/v0
```

Production = le domaine **de l'entreprise**, pas situs-protocol.org.
