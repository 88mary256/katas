import unittest

from katas.py.roman_numbers import *


class TestExpandNumber(unittest.TestCase):
    def test_from_roman(self):
        self.assertEqual(from_roman("M"), 1000)
        self.assertEqual(from_roman("MDXX"), 1520)
        self.assertEqual(from_roman("MCDXVI"), 1416)
        self.assertEqual(from_roman("MLXV"), 1065)
        self.assertEqual(from_roman("CV"), 105)
        self.assertEqual(from_roman("DCCCXI"), 811)
        self.assertEqual(from_roman("LXXIV"), 74)
        self.assertEqual(from_roman("XXXII"), 32)
        self.assertEqual(from_roman("X"), 10)
        self.assertEqual(from_roman("IV"), 4)
        self.assertEqual(from_roman(None), "None")

    def test_to_roman(self):
        self.assertEqual(to_roman(1000), "M")
        self.assertEqual(to_roman(1520), "MDXX")
        self.assertEqual(to_roman(1416), "MCDXVI")
        self.assertEqual(to_roman(1065), "MLXV")
        self.assertEqual(to_roman(105), "CV")
        self.assertEqual(to_roman(811), "DCCCXI")
        self.assertEqual(to_roman(74), "LXXIV")
        self.assertEqual(to_roman(32), "XXXII")
        self.assertEqual(to_roman(10), "X")
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(0), "None")
        self.assertEqual(to_roman(None), "None")
