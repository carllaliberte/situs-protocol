# SITUS Connect

Une prise. Pas un cloud.

OpenAPI : [`connect/openapi.v0.yaml`](connect/openapi.v0.yaml)

## Routes

| Route | Quoi |
|---|---|
| `POST /v0/autoriser` | licence + filtre + douane → décision + quittance si allow |
| `POST /v0/parler` | autoriser puis Ollama local |
| `POST /v0/verifier` | sceau du scan |
| `GET /v0/licence/{empreinte}` | usages + révoque |
| `GET /v0/annuaire/{empreinte}` | fiche publique |
| `GET /v0/douane` | quota du jour |
| `GET /v0/quittance/{id}` | reçu |
| `POST /v0/quittance/verifier` | signature intacte ? |

Jamais le splat. Jamais `owner.txt`. Jamais le texte client dans la quittance.

Famille : [ANNUAIRE.md](ANNUAIRE.md) · [QUITTANCE.md](QUITTANCE.md) · [DOUANE.md](DOUANE.md) · [OLLAMA.md](OLLAMA.md)

```
http://127.0.0.1:8765/v0
```
