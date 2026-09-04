"""Le filtre public : PYTHONPATH=src python3 -m situs_filtre.cli"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = [sys.executable, "-m", "situs_filtre.cli"]
ENV = {**os.environ, "PYTHONPATH": str(ROOT / "src")}


def _cli(message: str) -> dict:
    proc = subprocess.run(
        CLI + [message],
        cwd=ROOT,
        env=ENV,
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr
    return json.loads(proc.stdout)


def test_cli_medical_urgent():
    r = _cli("J'ai mal à la poitrine")
    assert r["decision"] == "urgent"
    assert r["decision"] != "allow"
    assert r["decision"] != "block"
    assert "urgent" in r["flags"]


def test_cli_poitrine_seul_pas_urgent():
    r = _cli("poitrine")
    assert r["decision"] == "allow"
    assert "urgent" not in r["flags"]


def test_cli_heures_pas_crash_medical():
    r = _cli("Quelle est l'heure d'ouverture ?")
    assert r["decision"] == "allow"
    assert "urgent" not in r["flags"]
