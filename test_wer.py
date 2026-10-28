"""Tests automatisés sur des données entièrement fictives."""
import unittest
from pathlib import Path
from jiwer import process_words
from calcul_wer import nettoyer

BASE = Path(__file__).resolve().parent

class TestWER(unittest.TestCase):
    def test_normalisation(self):
        self.assertEqual(nettoyer("Bonjour, LE monde !"), "bonjour le monde")

    def test_exemple_fictif(self):
        reference = nettoyer((BASE / "examples/reference.txt").read_text(encoding="utf-8"))
        hypothese = nettoyer((BASE / "examples/hypothese_asr.txt").read_text(encoding="utf-8"))
        result = process_words(reference, hypothese)
        self.assertEqual(result.substitutions, 1)
        self.assertEqual(result.deletions, 1)
        self.assertEqual(result.insertions, 0)
        self.assertAlmostEqual(result.wer, 2 / 17)

if __name__ == "__main__":
    unittest.main()
