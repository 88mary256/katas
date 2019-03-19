import unittest

from slides.py.time import *


class TestTime(unittest.TestCase):
    def test_days_in_month(self):
        self.assertEqual(days_in_month("January"), 31)
        self.assertEqual(days_in_month("February"), 28)
        self.assertEqual(days_in_month("November"), 30)
