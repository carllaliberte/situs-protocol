# Ancre

Le dossier est scellé chez toi. L'ancre, c'est une tx **ailleurs** qui répète l'empreinte.

```
python3 -m quantum situs-ancrer --preuve scan.spz.unforge.json
# → empreinte + payload SITUS1<64 hex>

# tu stamps (OpenTimestamps, OP_RETURN, calldata)
# puis :
python3 -m quantum situs-ancre --lieu QT-LX-... --empreinte <64hex> --txid <id> --chain ots
```

On poste 32 octets. Jamais le splat, jamais owner.txt, jamais l'adresse.

`revoque` plus tard = une deuxième tx sur la même empreinte. Le JSON local peut mentir. Le registre public, non.
