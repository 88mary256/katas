import unittest
from palindromo import Exercise5

class OperationsTest(unittest.TestCase):


    def test_palindromo(self):
        self.assertEqual(True, Exercise5.ispalindromo("arenera"))
        self.assertEqual(True, Exercise5.ispalindromo("oso"))
        self.assertEqual(False, Exercise5.ispalindromo("itisnot"))
        self.assertEqual(False, Exercise5.ispalindromo("upps"))