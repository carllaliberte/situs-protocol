# GitOps SITUS

Git est la source de vérité du **protocole**.  
Actions vérifie que `main` correspond encore à cet état.  
Rien n'est déployé sur un cluster. QUANTUM reste `127.0.0.1`.

```
PR → garde + gitops  → main  → état désiré publié
```

| Dans Git | Hors Git |
|---|---|
| OpenAPI, schémas, INTERDIT, OLLAMA | quantum.db, owner.txt, .spz |
| workflows | Ollama, QRNG |

Pas Argo. Pas Flux. Pas `kubectl apply`.
