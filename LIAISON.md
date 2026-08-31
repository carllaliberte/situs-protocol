# Lien SITUS — UNFORGE

Le protocole (ce dépôt) décrit la licence.
Le nœud QUANTUM (`unforge`, privé) tient les fiches.
La carte `*.unforge.json` se vérifie sans le nœud (`unforge-check`).

```
licence SITUS
    → quantum situs-init
scan local (.spz)
    → quantum situs-sceau   # hash + preuve + carte à côté du scan
carte + scan
    → quantum situs-verifier
    → ou : python check.py scan.spz.unforge.json scan.spz
```

Le splat ne va pas sur GitHub. La carte peut voyager.
Si `check` dit `fichier_ok: false`, le scan a bougé.
