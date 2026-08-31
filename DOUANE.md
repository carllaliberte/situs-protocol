# Douane

Quota par lab, usage et jour UTC.

Défaut v0 : **20** tours `sim` / jour / lab / empreinte.  
`capture` / `train` / `deploy` : 20 aussi, sauf plafond posé sur le nœud.

```
consomme >= plafond  →  deny + flag quota
```

Compteur dans `quantum.db`. Jamais dans Git.
Schéma : [`schema/douane.v0.json`](schema/douane.v0.json)
