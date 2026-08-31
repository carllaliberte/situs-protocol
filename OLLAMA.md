# Ollama dans SITUS

Ollama tourne **chez l'entreprise**, `127.0.0.1:11434`.  
Pas dans ce repo. Pas dans GitHub Actions. Pas chez Carl.

## Ordre

```
filtre SITUS  →  allow|urgent  →  agent Ollama  →  juge Ollama
                 deny|block    →  silence
```

Deux modèles. Deux rôles.

```bash
export FILON_URL=http://127.0.0.1:11434
export FILON_MODELE=qwen3.5:4b
export FILON_JUGE=qwen3.5:4b          # idéal : autre tag
ollama pull "$FILON_MODELE"
python3 -m quantum filon-etat
python3 -m quantum situs-tour --lieu QT-LX-… --texte "où est le café"
```

## Connect

`POST /v0/parler` = `autoriser` puis, si allow/urgent, le tour Filon.
`deny` n'envoie rien à Ollama.

Jamais le splat. Jamais `owner.txt`. Jamais un client cloud.
