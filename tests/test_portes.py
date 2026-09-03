"""Portes publiques : copie, exemple fictif, pas de sceau QUANTUM."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXEMPLE = ROOT / "examples" / "pharmacie-fictive"

# Aiguilles construites : la copie publique ne doit pas les contenir.
_IMAGINE = "Imag" + "ine"
_FORMALLY_VERIFIED = "formally" + " " + "verified"
_QUANTUM_SEAL_EN = "QUANTUM" + " " + "seal"

SKIP_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".spz", ".ply"}
SKIP_DIRS = {".git", ".pytest_cache", "__pycache__", ".mypy_cache"}


def _tracked_text_files() -> list[Path]:
    proc = subprocess.run(
        ["git", "ls-files"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    out: list[Path] = []
    for line in proc.stdout.splitlines():
        p = ROOT / line
        if not p.is_file():
            continue
        if p.suffix.lower() in SKIP_SUFFIXES:
            continue
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        out.append(p)
    return out


def _read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def test_readme_porte_usages_et_licence():
    text = _read(ROOT / "README.md")
    for usage in ("capture", "train", "sim", "deploy"):
        assert f"`{usage}`" in text
    assert "licence active" in text
    assert "pas de copie propre" in text
    assert "python3 -m situs_filtre.cli" in text
    assert "J'ai mal à la poitrine" in text
    assert "heure d'ouverture" in text
    assert "qubit" in text
    assert "n’est pas un sceau QUANTUM" in text or "n'est pas un sceau QUANTUM" in text
    assert "Le filtre sort urgent sur le médical" in text
    assert "Médical → `urgent`" in text
    assert "pas allow" in text
    assert "Urgent n’est pas block" in text or "Urgent n'est pas block" in text
    assert "heures d’ouverture restent allow" in text or "heures d'ouverture restent allow" in text
    medical_lines = [
        line
        for line in text.splitlines()
        if "médical" in line.lower() or "poitrine" in line.lower()
    ]
    assert medical_lines, "porte médicale absente"
    assert all("refusée" not in line for line in medical_lines)


def test_readme_rituel_45_minutes():
    text = _read(ROOT / "README.md")
    assert "Rituel 45 minutes" in text
    assert "templates/licence.md" in text
    assert "templates/inventaire.md" in text
    assert "templates/agent.md" in text
    assert "templates/scenario.md" in text
    assert "templates/juge.md" in text
    assert "examples/pharmacie-fictive/" in text


def test_copie_sans_imagine():
    hits = []
    for p in _tracked_text_files():
        if _IMAGINE in _read(p):
            hits.append(str(p.relative_to(ROOT)))
    assert hits == [], f"mot interdit dans {hits}"


def test_copie_sans_formally_verified():
    hits = []
    needle = _FORMALLY_VERIFIED
    for p in _tracked_text_files():
        if needle in _read(p).lower():
            hits.append(str(p.relative_to(ROOT)))
    assert hits == [], f"locution interdite dans {hits}"


def test_pas_de_sceau_quantum_sur_la_carte():
    needle = "sceau" + " " + "quantum"
    hits = []
    for p in _tracked_text_files():
        rel = str(p.relative_to(ROOT))
        if rel.startswith("tests/"):
            continue
        text = _read(p)
        if _QUANTUM_SEAL_EN.lower() in text.lower():
            hits.append(rel)
        for raw in text.splitlines():
            line = raw.strip().lower()
            if needle not in line:
                continue
            if any(
                neg in line
                for neg in (
                    "n'est pas",
                    "n’est pas",
                    "pas un sceau",
                    "pas de sceau",
                    "pas ce sceau",
                    "pas le sceau",
                )
            ):
                continue
            hits.append(f"{rel}: {raw.strip()}")
    assert hits == [], f"sceau réclamé dans {hits}"


def test_exemple_reste_fictif():
    assert EXEMPLE.is_dir()
    readme = _read(EXEMPLE / "README.md").lower()
    assert "fictif" in readme
    assert "aucun scan réel" in readme or "ne pas traiter comme un vrai commerce" in readme

    licence = _read(EXEMPLE / "licence.md")
    assert "[redacted]" in licence.lower() or "redacted" in licence.lower()
    assert "pas de scan" in licence.lower()

    session = json.loads(_read(EXEMPLE / "connect-session.json"))
    assert session.get("fictif") is True
    assert "civique" in session.get("lieu_public", "").lower()

    entree = json.loads(_read(EXEMPLE / "entree.json"))
    assert "fictive" in entree.get("nom_public", "").lower()
    assert set(entree["empreinte"]) == {"a"}


def test_aucun_scan_reel_versionne():
    proc = subprocess.run(
        ["git", "ls-files"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    forbidden = [
        line
        for line in proc.stdout.splitlines()
        if line.lower().endswith((".spz", ".ply"))
        or line.endswith("owner.txt")
        or line.endswith("quantum.db")
    ]
    assert forbidden == [], f"fichier interdit versionné: {forbidden}"
