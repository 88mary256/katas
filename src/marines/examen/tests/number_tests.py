import unittest

from examen.py.number import *


class TestNumber(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_capicua(self):
        self.assertEqual(capicua(0), True)
        self.assertEqual(capicua(1), True)
        self.assertEqual(capicua(9), True)
        self.assertEqual(capicua(10), False)
        self.assertEqual(capicua(11), True)
        self.assertEqual(capicua(1551), True)
        self.assertEqual(capicua(1552), False)
