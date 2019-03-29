import unittest

from examen.py.my_string import palindromo


class TestMyString(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(palindromo(""), True)
        self.assertEqual(palindromo(None), False)
        self.assertEqual(palindromo("abba"), True)
        self.assertEqual(palindromo("casa"), False)
