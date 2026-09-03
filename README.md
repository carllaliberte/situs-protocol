# SITUS Protocol

**Une servitude pour machines.**

SITUS nomme **où**. Un lieu réel n’entre dans une copie 3D, un entraînement ou un déploiement d’agent **que** s’il existe une licence. Ce rail ne collapse pas MODE.

Ce dépôt est la version 0. Elle tient dans un téléphone. Zéro token. Zéro serveur payant.

**Open source (MIT).** Le protocole reste public. Voir [OPEN_SOURCE.md](OPEN_SOURCE.md), [COPYRIGHT.md](COPYRIGHT.md) et [SECURITY.md](SECURITY.md).

## Primitive

```
licence active  →  copie 3D + agent + test
licence absente →  pas de copie propre
```

Quatre usages, **séparés** — un usage n’en ouvre pas un autre :

| Code | Droit |
|---|---|
| `capture` | Scanner / filmer le lieu |
| `train` | S’en servir pour entraîner un modèle |
| `sim` | Y faire courir un agent dans le 3D |
| `deploy` | Y envoyer un robot ou un agent live |

## Physique / droits

- Un lieu n’est pas un qubit. On ne mint pas `quantique`.
- Ne pas coller HORIZON sur SITUS Connect pour prétendre qu’un endroit est quantique.
- La carte JSON / licence n’est pas un sceau QUANTUM. QUANTUM signe plus tard. Les clés restent hors Git.
- SITUS n’est pas FIGURE, UNFORGE, QUELLE, TÉMOIN, BRUIT, ni HORIZON. Ici : **où**.

## Vérifié vs assumé

| Vérifié (v0 tient ça) | Assumé (v0 ne tient pas ça) |
|---|---|
| Licence présente ou absente | Qu’un lieu est un qubit |
| Les 4 usages, un par un | Qu’un usage en ouvre un autre |
| Le filtre sort urgent sur le médical | Qu’un modèle a « scellé » le lieu |
| Hash du scan (fichier hors Git) | Qu’une fiche JSON remplace QUANTUM |
| L’exemple public est **fictif** | Qu’un commerce réel est dans ce repo |

Le juge filtre. La copie propre n’existe pas sans licence. Le jugement, c’est Carl.

## v0 au cellulaire — 3 commandes

```bash
PYTHONPATH=src python3 -m situs_filtre.cli "Quelle est l'heure d'ouverture ?"
PYTHONPATH=src python3 -m situs_filtre.cli "J'ai mal à la poitrine"
sha256sum examples/pharmacie-fictive/licence.md
```

Médical → `urgent`, pas allow. Urgent n’est pas block. Si « J'ai mal à la poitrine » sort allow, le système est cassé. Les heures d’ouverture restent allow.

## Rituel 45 minutes (en dessous)

1. Copier [`templates/licence.md`](templates/licence.md)
2. Obtenir le consentement écrit de l’owner (texto suffit)
3. Scanner avec [Scaniverse](https://scaniverse.com) (gratuit, sur l’appareil)
4. Remplir [`templates/inventaire.md`](templates/inventaire.md)
5. Coller [`templates/agent.md`](templates/agent.md) dans Mistral Le Chat, Gemini ou Grok
6. Jouer les 10 questions de [`templates/scenario.md`](templates/scenario.md)
7. Coller le dialogue dans [`templates/juge.md`](templates/juge.md) — **autre conversation**
8. Ranger le tout comme dans [`examples/pharmacie-fictive/`](examples/pharmacie-fictive/)

## Famille

| Rail | Question |
|---|---|
| [FIGURE](https://github.com/carllaliberte/figure-protocol) | qui |
| [SITUS](https://github.com/carllaliberte/situs-protocol) | où |
| [UNFORGE](https://github.com/carllaliberte/unforge-check) | quoi |
| [QUELLE](https://github.com/carllaliberte/quelle) | d'où le bit |
| [TÉMOIN](https://github.com/carllaliberte/temoin-protocol) | avec quelle force |
| [HORIZON](https://github.com/carllaliberte/horizon-protocol) | jusqu'à quand le sceau tient |

MIT (protocoles) · Apache-2.0 (œil UNFORGE). QUANTUM signe plus tard. Les clés restent hors Git. Cette carte n’est pas ce sceau.

## API

Contrat d’appel (agent + juge, deux conversations) : [`api.md`](api.md).

Pas de serveur SITUS en v0. Tu branches un LLM. Les clés restent hors repo.

## Ce qui va sur GitHub / ce qui reste privé

| Public (ce repo) | Privé (ton téléphone / Drive) |
|---|---|
| Gabarits, prompts, schéma | Scan `.spz` / `.ply` d’un vrai lieu |
| Exemple **fictif** | Photos de façade, numéro civique |
| Méthode de hash | Consentement nominatif |
| Rubrique du juge | Dialogues avec de vrais clients |

Ne commite jamais un scan d’un commerce sans licence **et** sans anonymisation. C’est exactement ce que SITUS interdit. Hash seulement.

## Schéma d’une fiche lieu

Voir [`schema/lieu.v0.json`](schema/lieu.v0.json).

```bash
sha256sum scan.spz
```

## Ce que v0 n’est pas

- pas une blockchain
- pas un metaverse
- pas un token
- pas un L1
- pas un avis juridique
- pas un réseau quantique simulé
- pas un qubit (un lieu n’en est pas un)
- pas FIGURE, UNFORGE, QUELLE, TÉMOIN, BRUIT, HORIZON

La chain, plus tard, ne fait qu’ancrer ce dossier. Elle ne le crée pas.

## Droits et sécurité

- Auteur du protocole : Carl Laliberté, © 2026, MIT — [COPYRIGHT.md](COPYRIGHT.md)
- Les lieux réels et leurs scans restent à leurs owners
- Signalement privé : [SECURITY.md](SECURITY.md)
