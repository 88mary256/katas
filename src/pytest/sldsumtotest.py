import unittest
from sum_to import Adding


class OperationsTest(unittest.TestCase):

    def test_sumto(self):
        self.assertEqual(55, Adding.sumto(10))
        self.assertEqual(45, Adding.sumto(9))
        self.assertEqual(55, Adding.sumto(11))