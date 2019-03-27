import unittest

from katas.py.array_ordered import in_asc_order


class TestExpandNumber(unittest.TestCase):
    def test_in_asc_order_form_0_integers(self):
        self.assertEqual(in_asc_order([]), True)

    def test_in_asc_order_form_1_integers(self):
        self.assertEqual(in_asc_order([1]), True)
        self.assertEqual(in_asc_order([8]), True)

    def test_in_asc_order_form_2_integers(self):
        self.assertEqual(in_asc_order([1, 2]), True)
        self.assertEqual(in_asc_order([2, 1]), False)

    def test_in_asc_order_form_3_integers(self):
        self.assertEqual(in_asc_order([1, 2, 3]), True)
        self.assertEqual(in_asc_order([1, 3, 2]), False)

    def test_in_asc_order_complex_case(self):
        self.assertEqual(in_asc_order([1, 4, 13, 97, 508, 1047, 20058]), True)
        self.assertEqual(in_asc_order([56, 98, 123, 67, 742, 1024, 32, 90969]), False)
