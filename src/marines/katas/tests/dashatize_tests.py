import unittest

from katas.py.dashatize import dashatize


class TestExpandNumber(unittest.TestCase):
    def test_dashatize_start_end_with_par(self):
        self.assertEqual(dashatize(274), "2-7-4", "Should return 2-7-4")

    def test_dashatize_start_end_with_impar(self):
        self.assertEqual(dashatize(5311), "5-3-1-1", "Should return 5-3-1-1")

    def test_dashatize_two_par_together(self):
        self.assertEqual(dashatize(86320), "86-3-20", "Should return 86-3-20")
        self.assertEqual(dashatize(974302), "9-7-4-3-02", "Should return 9-7-4-3-02")

    def test_dashatize_special_cases(self):
        self.assertEqual(dashatize(None), "None", "Should return None")
        self.assertEqual(dashatize(0), "0", "Should return 0")
        self.assertEqual(dashatize(-1), "1", "Should return 1")
        self.assertEqual(dashatize(-28369), "28-3-6-9", "Should return 28-3-6-9")
