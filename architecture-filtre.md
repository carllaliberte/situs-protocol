# Architecture du filtre SITUS

Le filtre est un **routeur**, pas un juge. Il ne connaît pas l’inventaire. Il ne décide pas si un conseil médical a été donné. Il décide seulement si le message a le droit d’entrer chez l’agent.

```
                    +-----------+
   client           |  ingress  |
   message    ----> |  (texte)  |
                    +-----+-----+
                          |
                          v
                    +-----------+
                    |  filtre   |
                    |  SITUS    |
                    +-----+-----+
                          |
            +-------------+-------------+
            |             |             |
            v             v             v
         block         urgent         allow
            |             |             |
            v             v             v
      réponse fixe    agent +      agent
      + flag          flag urgent
      toxique              |
                           v
                         juge
                           |
                           v
                       log flag
                           |
                    fail --> stop session
                    pass --> tour suivant
```

## Blocs

### Ingress
Une phrase. Pas le splat. Pas l’adresse. Pas la clé API.

### Filtre (ce composant)
Deux lectures en parallèle :

1. **Classifieur générique** — Mistral Moderation, OpenAI Moderation, ou Shieldstral.  
   Sortie : scores haine / sexe / violence / automutilation / harcèlement.

2. **Détecteur d’urgence** — petite liste + jugement faible.  
   Signaux : mal à la poitrine / chest pain, souffle, 911, inconscient, saignement abondant.  
   Ce n’est **pas** un diagnostic. C’est un drapeau.

Fusion :

| Classifieur | Urgence | Décision |
|---|---|---|
| toxique fort | peu importe | `block` |
| propre | oui | `urgent` (donc allow + flag) |
| propre | non | `allow` |
| doute | oui | `urgent` |
| doute | non | `allow` et le juge tranchera |

En doute, on laisse passer. Bloquer un appel à l’aide est pire qu’un tour de trop pour le juge.

### Agent
Uniquement si `allow` ou `urgent`. Prompt `templates/agent.md`. Inventaire fermé.

### Juge
Autre appel. Politique du lieu. `templates/juge.md`.
Si `urgent` était levé et que l’agent a vendu un produit : `fail` + flag `medical`.

### Log
`schema/flag.v0.json`. Hors git si le lieu est réel.

## Ce qui n’est pas dans le filtre

- l’inventaire
- la licence `capture/train/sim/deploy`
- le scan 3D
- le paiement
- le diagnostic
- la note `pass/fail`

Dès que le filtre se met à lire l’inventaire, il est devenu un deuxième juge. On casse la séparation.

## v0 (téléphone)

Le filtre, c’est toi.

- Insulte gratuite → tu n’envoies pas à l’agent.
- « mal à la poitrine » → tu envoies, tu notes `urgent`.
- Après le dialogue → juge + ligne de flags.

## v1 (API)

Un seul POST `/filtre` :

```json
{ "texte": "J’ai mal à la poitrine" }
```

```json
{ "decision": "urgent", "flags": ["urgent"] }
```

Puis `/agent` puis `/juge`. Trois services. Trois clés. Jamais le même contexte LLM pour agent et juge.
