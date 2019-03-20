import unittest

from katas.py.vowel_count import getCount


class TestExpandNumber(unittest.TestCase):
    def test_reverse_alternate_3_words(self):
        self.assertEqual(getCount("abracadabra"), 5)
        self.assertEqual(getCount("abcee"), 3)
