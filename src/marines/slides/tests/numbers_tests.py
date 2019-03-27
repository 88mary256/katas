import unittest

from slides.py.numbers import *


class TestNumbers(unittest.TestCase):
    def test_isOdd(self):
        self.assertEqual(isOdd(2), True)
        self.assertEqual(isOdd(3), False)

    def test_isEven(self):
        self.assertEqual(isEven(2), False)
        self.assertEqual(isEven(3), True)

    def test_primeList(self):
        self.assertEqual(primeList(1, 21), [1, 2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(primeList(5, 21), [5, 7, 11, 13, 17, 19])

    def test_area_of_circle(self):
        self.assertEqual(area_of_circle(1), "not supported")
        self.assertEqual(area_of_circle(5), "not supported")
        self.assertEqual(area_of_circle(10), "not supported")
        self.assertEqual(area_of_circle(11), 380.1336)
        self.assertEqual(area_of_circle(15), 706.86)

    def sum_to(self):
        self.assertEqual(sum_to(3), 6)
        self.assertEqual(sum_to(10), 55)
