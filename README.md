# SITUS Protocol

**Une servitude pour machines.**

SITUS est un registre de droits spatiaux pour l’IA : un lieu réel n’entre dans un jumeau 3D, un entraînement ou un déploiement d’agent **que** s’il existe une licence.

Ce dépôt est la version 0. Elle tient dans un téléphone. Zéro token. Zéro serveur payant.

## Primitive

```
licence active  →  copie 3D + agent + test
licence absente →  pas de copie propre
```

Quatre usages, séparés :

| Code | Droit |
|---|---|
| `capture` | Scanner / filmer le lieu |
| `train` | S’en servir pour entraîner un modèle |
| `sim` | Y faire courir un agent dans le 3D |
| `deploy` | Y envoyer un robot ou un agent live |

## Monter v0 en 45 minutes

1. Copier [`templates/licence.md`](templates/licence.md)
2. Obtenir le consentement écrit de l’owner (texto suffit)
3. Scanner avec [Scaniverse](https://scaniverse.com) (gratuit, sur l’appareil)
4. Remplir [`templates/inventaire.md`](templates/inventaire.md)
5. Coller [`templates/agent.md`](templates/agent.md) dans Mistral Le Chat, Gemini ou Grok
6. Jouer les 10 questions de [`templates/scenario.md`](templates/scenario.md)
7. Coller le dialogue dans [`templates/juge.md`](templates/juge.md) — **autre conversation**
8. Ranger le tout comme dans [`examples/pharmacie-fictive/`](examples/pharmacie-fictive/)

Si le juge échoue la question médicale, le système marche.

## Ce qui va sur GitHub / ce qui reste privé

| Public (ce repo) | Privé (ton téléphone / Drive) |
|---|---|
| Gabarits, prompts, schéma | Scan `.spz` / `.ply` d’un vrai lieu |
| Exemple **fictif** | Photos de façade, numéro civique |
| Méthode de hash | Consentement nominatif |
| Rubrique du juge | Dialogues avec des clients réels |

Ne commite jamais un scan d’un commerce sans licence **et** sans anonymisation. C’est exactement ce que SITUS interdit.

## Schéma d’une fiche lieu

Voir [`schema/lieu.v0.json`](schema/lieu.v0.json).

Le hash du scan remplace le fichier 3D dans le registre public :

```bash
# sur ordi, ou via une app de hash
sha256sum scan.spz
```

## Ce que v0 n’est pas

- pas une blockchain
- pas un metaverse
- pas un token
- pas un avis juridique

La chain, plus tard, ne fait qu’ancrer ce dossier. Elle ne le crée pas.

## Licence du dépôt

MIT. Les gabarits sont réutilisables. Les lieux réels restent la propriété de leurs owners.
