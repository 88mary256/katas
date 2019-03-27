import unittest

from katas.py.expand_number import expanded_form


class TestExpandNumber(unittest.TestCase):
    def test_expanded_form_2_digits(self):
        self.assertEqual(expanded_form(12), '10 + 2')
        self.assertEqual(expanded_form(42), '40 + 2')

    def test_expanded_form_5_digits_with_0(self):
        self.assertEqual(expanded_form(70304), '70000 + 300 + 4')

    def test_expanded_long_number(self):
        self.assertEqual(expanded_form(9000000), '9000000')
        self.assertEqual(expanded_form(605020), '600000 + 5000 + 20')
