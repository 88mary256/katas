
import unittest
from Katas.py.reverse_even_words import reverse_alternate

class TestReverse_alternate(unittest.TestCase):

    def test_reverse_alternate_3_words(self):
        self.assertEqual(reverse_alternate("Did it work?"), "Did ti work?")
        self.assertEqual(reverse_alternate("Have a beer"), "Have a beer")
        self.assertEqual(reverse_alternate('This is a   test   '), 'This si a tset')

    def test_reverse_alternate_many_words(self):
        self.assertEqual(reverse_alternate("I really hope it works this time..."),
                         "I yllaer hope ti works siht time...")
        self.assertEqual(reverse_alternate("Reverse this string, please!"), "Reverse siht string, !esaelp")

    def test_reverse_alternate_empty(self):
        self.assertEqual(reverse_alternate(""), "")
