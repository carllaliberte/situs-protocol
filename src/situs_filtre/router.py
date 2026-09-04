"""Routeur du filtre SITUS.

Décide seulement si le message entre chez l'agent.
Ne lit pas l'inventaire. Ne note pas pass/fail.
"""

from __future__ import annotations

import re
from typing import Iterable

DECISIONS = ("allow", "block", "urgent")

URGENT_PATTERNS = (
    r"\b911\b",
    r"mal \w* ?\u00e0 la poitrine",
    r"mal \w* ?a la poitrine",
    r"douleur \w* ?\u00e0 la poitrine",
    r"douleur \w* ?a la poitrine",
    r"chest pain",
    r"pain in (?:the )?chest",
    r"heart[- ]?attack",
    r"manque[r]? d['’]?air",
    r"respire mal",
    r"souffle (court|coupé)",
    r"\binconscient",
    r"ne r[eé]pond plus",
    r"saign(?:e|ement) (?:beaucoup|abondant)",
    r"crise cardiaque",
    r"infarctus",
    r"avc\b",
    r"stroke\b",
    r"je vais mourir",
)

TOXIC_KEYS = (
    "hate",
    "harassment",
    "sexual",
    "violence",
    "self-harm",
    "self_harm",
    "hate_and_discrimination",
    "violence_and_threats",
)

_URGENT_RE = [re.compile(p, re.IGNORECASE) for p in URGENT_PATTERNS]


def _norm(texte: str) -> str:
    return (texte or "").strip()


def est_urgent(texte: str) -> bool:
    t = _norm(texte)
    if not t:
        return False
    return any(rx.search(t) for rx in _URGENT_RE)


def est_toxique(
    scores: dict | None,
    flagged: bool | None = None,
    seuil: float = 0.8,
) -> bool:
    if flagged is True:
        return True
    if not scores:
        return False
    for key, raw in scores.items():
        if key.lower() not in TOXIC_KEYS and key.lower() not in {
            k.replace("-", "_") for k in TOXIC_KEYS
        }:
            continue
        try:
            val = float(raw)
        except (TypeError, ValueError):
            continue
        if val >= seuil:
            return True
    return False


def route(
    texte: str,
    scores: dict | None = None,
    flagged: bool | None = None,
    seuil: float = 0.8,
) -> dict:
    """Fusion classifieur + urgence.

    scores / flagged viennent d'une API de modération optionnelle.
    Sans API, seul le détecteur d'urgence tourne : jamais block.
    """
    t = _norm(texte)
    urgent = est_urgent(t)
    toxique = est_toxique(scores, flagged=flagged, seuil=seuil)

    flags: list[str] = []

    if toxique:
        flags.append("toxique")
        # Table d'archi : toxique fort gagne, même si urgence.
        return {"decision": "block", "filtre": "block", "flags": flags}

    if urgent:
        flags.append("urgent")
        return {"decision": "urgent", "filtre": "urgent", "flags": flags}

    return {"decision": "allow", "filtre": "allow", "flags": flags}


def route_lot(messages: Iterable[str], **kwargs) -> list[dict]:
    return [route(m, **kwargs) for m in messages]
