# Sécurité

## Signaler une faille

N’ouvre **pas** une issue publique si ça expose :

- un lieu réel, une adresse, un scan
- un consentement, une identité
- un moyen de contourner une licence SITUS
- des identifiants, clés, tokens

Utilise plutôt le [signalement privé de GitHub](https://github.com/carllaliberte/situs-protocol/security/advisories/new) (Security Advisories).

Délai visé : accusé de réception sous 7 jours.

Les questions de spec non sensibles : issues publiques.

## Périmètre v0

v0 n’a pas de serveur, pas de wallet, pas de smart contract. La surface, c’est :

1. les gabarits et prompts (injection, juge complaisant)
2. le registre fichier (licence falsifiée, hash inventé)
3. les scans et preuves laissés au mauvais endroit (Git, Drive public)

## Règles non négociables

- Aucun scan, photo de façade, numéro civique ou consentement nominatif dans ce repo.
- L’agent et le juge sont deux conversations séparées. L’agent ne se note pas.
- Une licence sans owner identifiable n’est pas une licence.
- Un hash de scan sans fichier sous le contrôle de l’owner n’est pas une preuve.
- `train` et `deploy` restent décochés tant que l’owner n’a pas accepté **ces** usages.

## Durcissements v0.1 (nœud QUANTUM)

1. Carte exportée : pas de `chemin_origine`. `nom` + `sha256` + `octets` seulement.
2. `SCORE: fail` ferme la session du lieu.
3. `FILON_JUGE` ≠ `FILON_MODELE`.
4. `inventaire_sha256` dans la fiche et dans `objet`.
5. `revoque_at` : le vérifieur refuse. Champ hors empreinte — la source de vérité reste le nœud.
6. `owner.txt` obligatoire à l’init. Hash seulement en base. Fichier gitignoré.

## Menaces v0

| Menace | Quoi faire |
|---|---|
| Prompt injection | Inventaire fermé + juge séparé + fail si l’agent obéit |
| Faux owner | `owner.txt` + preuve de lieu (hors git) |
| Scan d’un lieu sans licence | Ne pas produire la copie. C’est le primitive. |
| Fuite du splat / du path home | `.gitignore` + carte sans chemin |
| Juge = même poids que l’agent | `FILON_JUGE` |
| Carte révoquée rééditée | `quantum.db` gagne sur le JSON |

## Quand on ajoutera de la chain

Avant tout contrat on-chain : revue des clés admin, pas de mint ouvert, pas de clé dans le repo, politique de révocation. v0 n’a pas ce périmètre.

## Dépendances

Scaniverse, Le Chat, Gemini, Grok, Drive, Ollama : outils tiers. Leur sécurité n’est pas SITUS. Ne colle pas de secrets dans les prompts.
