import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from situs_filtre.router import URGENT_PATTERNS, route


def test_allow_rayon():
    r = route("Vous avez-tu du tylenol ?")
    assert r["decision"] == "allow"
    assert r["flags"] == []


def test_urgent_poitrine():
    r = route("J’ai mal à la poitrine, je respire mal.")
    assert r["decision"] == "urgent"
    assert "urgent" in r["flags"]


def test_medical_porte_urgent():
    r = route("J'ai mal à la poitrine")
    assert r["decision"] == "urgent"
    assert r["decision"] != "allow"
    assert r["decision"] != "block"
    assert "urgent" in r["flags"]


def test_poitrine_seul_pas_urgent():
    assert "poitrine" not in URGENT_PATTERNS
    r = route("poitrine")
    assert r["decision"] == "allow"
    assert "urgent" not in r["flags"]
    produit = route("avez-vous une crème poitrine")
    assert produit["decision"] == "allow"
    assert "urgent" not in produit["flags"]


def test_chest_pain_urgent():
    r = route("I have chest pain")
    assert r["decision"] == "urgent"
    assert "urgent" in r["flags"]


def test_heures_ouverture_pas_crash_medical():
    r = route("Quelle est l'heure d'ouverture ?")
    assert r["decision"] == "allow"
    assert r["flags"] == []


def test_urgent_911():
    r = route("Je fais le 911 là.")
    assert r["decision"] == "urgent"


def test_block_si_flagged():
    r = route("n’importe quoi", flagged=True)
    assert r["decision"] == "block"
    assert "toxique" in r["flags"]


def test_toxique_gagne_sur_urgence():
    r = route("mal à la poitrine", flagged=True)
    assert r["decision"] == "block"


def test_score_haut():
    r = route("bonjour", scores={"hate": 0.91})
    assert r["decision"] == "block"


def test_score_bas_allow():
    r = route("bonjour", scores={"hate": 0.1})
    assert r["decision"] == "allow"
