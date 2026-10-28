"""Évaluer une transcription ASR à partir d'une référence, avec JiWER.

Usage:
  python calcul_wer.py examples/reference.txt examples/hypothese_asr.txt

Les fichiers d'exemple sont entièrement fictifs.
"""
import argparse
import re
from pathlib import Path
from jiwer import process_words


def nettoyer(texte: str) -> str:
    """Minuscules, suppression de la ponctuation et espaces normalisés."""
    texte = texte.lower()
    texte = re.sub(r"[^\w\s]", " ", texte)
    return re.sub(r"\s+", " ", texte).strip()


def lire_fichier(chemin: Path) -> str:
    return chemin.read_text(encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Calcul du WER d'une transcription automatique")
    parser.add_argument("reference", type=Path, help="Transcription de référence")
    parser.add_argument("hypothese", type=Path, help="Transcription ASR à évaluer")
    args = parser.parse_args()

    reference = nettoyer(lire_fichier(args.reference))
    hypothese = nettoyer(lire_fichier(args.hypothese))
    if not reference:
        parser.error("La transcription de référence est vide après nettoyage.")

    resultat = process_words(reference, hypothese)
    print(f"WER : {resultat.wer * 100:.2f} %")
    print(f"Substitutions : {resultat.substitutions}")
    print(f"Suppressions : {resultat.deletions}")
    print(f"Insertions : {resultat.insertions}")


if __name__ == "__main__":
    main()
