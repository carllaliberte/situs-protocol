# Clôture

SITUS licencie l'espace. La clôture éteint un usage à une heure.

```
dans la fenêtre  →  allow possible
hors fenêtre     →  deny + flag cloture
```

Vit sur la fiche lieu, pas dans le LLM.

```
ouvre: "08:30"
ferme: "21:00"
tz: "America/Toronto"
usages: ["deploy", "sim"]
```

`capture` et `train` peuvent rester 24 h. Un scan de nuit est parfois le seul moment.
`deploy` et `sim` meurent à `ferme`.

Révoquer une clôture = une nouvelle fiche. Pas un adjectif dans le prompt.

Sans objet `cloture` : pas de borne. C'est correct. Ce n'est pas 24 h déguisé.

## Interdit

- « Presque fermé ».
- UTC sans fuseau.
- Faire porter l'horaire par l'agent.
- Token d'heure, L1, cloud d'horaires.

Schéma : [`schema/cloture.v0.json`](schema/cloture.v0.json) — aussi sur [`schema/lieu.v0.json`](schema/lieu.v0.json).
