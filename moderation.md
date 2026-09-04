# Modération v0 — chaîne 1-2-3

La modération SITUS n’est pas « est-ce toxique ? ».
C’est « l’agent a-t-il violé la licence du lieu ? »

```
message client
    →  1. filtre générique
    →  2. agent  (si le filtre laisse passer)
    →  2. juge   (politique du lieu)
    →  3. log flag
```

Ne pas bloquer « mal à la poitrine » à l’étape 1.
L’agent doit pouvoir dire 911. Le juge vérifie qu’il n’a pas conseillé un comprimé.

## 1. Filtre générique

Avant l’agent. Message client seulement.

Outil : Mistral Moderation, OpenAI `omni-moderation-latest`, ou Shieldstral.
Catégories utiles ici : haine, harcèlement, sexuel, violence gratuite, automutilation.

- `allow` — on envoie à l’agent
- `block` — on n’appelle pas l’agent ; réponse fixe : « Je ne peux pas continuer. »
- `urgent` — urgence possible (mal à la poitrine, chest pain, souffle, 911) : **allow** + flag `urgent` pour le juge

Le filtre ne connaît pas l’inventaire. Il ne juge pas un conseil médical.

## 2. Juge SITUS

Après l’agent. Autre conversation. Prompt : [`templates/juge.md`](templates/juge.md).

Il note `pass` ou `fail` sur la licence :

- produit ou prix inventé
- conseil médical / juridique / financier
- langue exigée
- interdit de la licence ignoré
- injection (« ignore tes règles ») si l’agent obéit

`fail` → plus d’agent sur cette session. Owner / humain / 911 selon le cas.

## 3. Log flag

Une ligne par tour, hors Git si le lieu est réel.

```json
{
  "lieu_id": "lieu-demo-001",
  "tour": 5,
  "filtre": "allow",
  "score_juge": "pass",
  "flags": ["urgent"]
}
```

Flags possibles :

| flag | Sens |
|---|---|
| `toxique` | coupé par le filtre 1 |
| `urgent` | urgence possible ; agent doit orienter, pas diagnostiquer |
| `medical` | l’agent a donné un conseil médical |
| `sku_invente` | produit / prix / rayon hors inventaire |
| `injection` | l’agent a suivi une consigne qui casse la licence |
| `langue` | langue exigée non respectée |

Schéma : [`schema/flag.v0.json`](schema/flag.v0.json)

## v0 sans serveur

1. Tu es le filtre : si c’est une insulte gratuite, tu n’envoies pas à l’agent.
2. Tu colles le dialogue au juge.
3. Tu écris une ligne `flags` sous le jugement.

Les clés des API de modération restent hors repo.
