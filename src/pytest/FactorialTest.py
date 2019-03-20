import unittest
from factorial import Exercise1

class OperationsTest(unittest.TestCase):


    def test_factorial(self):
        self.assertEqual(1, Exercise1.factorial(1))
        self.assertEqual(1, Exercise1.factorial(0))
        self.assertEqual(1307674368000, Exercise1.factorial(15))