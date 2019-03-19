# katas


#Unit test sample
#operations.py
class Operations:

    def add(self, a, b):
        return a + b

    @staticmethod
    def divition(a, b):
        return a // b

    def multiply(self, a, b):
        return a * b


#operations_test.py
import unittest
from operations import Operations


class OperationsTest(unittest.TestCase):

    def setUp(self):
        self.op = Operations()

    def test_add(self):
        self.assertEqual(10, self.op.add(7, 3))
        self.assertEqual(10, self.op.add(5, 5))
        self.assertEqual(10, self.op.add(4, 6))
        self.assertEqual(10, self.op.add(15, -5))

    def test_multiply(self):
        self.assertEqual(-2, self.op.multiply(-2, 1))

    def test_divition(self):
        self.assertEqual(1, Operations.divition(2, 2))
