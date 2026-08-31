# Annuaire SITUS

Un lab découvre un lieu **sans** entrer dans le nœud.

L'annuaire ne contient que : empreinte, usages, `revoque`, langue.  
Jamais un path, un owner, un splat, un dialogue.

```
annuaire public  →  lab lit l'empreinte
                 →  lab appelle Connect CHEZ l'owner
                 →  allow | deny
```

Fiche : [`schema/entree.v0.json`](schema/entree.v0.json)  
Exemple : [`examples/pharmacie-fictive/entree.json`](examples/pharmacie-fictive/entree.json)

Pas un DNS mondial. Pas un cloud Carl. Une page Git que l'owner met à jour.
