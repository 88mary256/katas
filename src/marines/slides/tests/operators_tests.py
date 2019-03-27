import unittest

from slides.py.operators import *


class TestOperators(unittest.TestCase):
    def test_perform_operation(self):
        self.assertEqual(perform_and_print_operation("*", "5", "6"), 30)
        self.assertEqual(perform_and_print_operation("+", "2", "5"), 7)
        self.assertEqual(perform_and_print_operation("-", "2", "5"), -3)
        self.assertEqual(perform_and_print_operation("*", "2", "5"), 10)
        self.assertEqual(perform_and_print_operation("/", "2", "5"), 0)
        self.assertEqual(perform_and_print_operation("%", "5", "2"), 1)
        self.assertEqual(perform_and_print_operation("/", "5", "2"), 2)
        self.assertEqual(perform_and_print_operation("//", "-11", "3"), -4)
        self.assertEqual(perform_and_print_operation("//", "9", "2"), 4)
        self.assertEqual(perform_and_print_operation("**", "5", "2"), 25)
        self.assertEqual(perform_and_print_operation("==", "5", "2"), False)
        self.assertEqual(perform_and_print_operation("!=", "5", "2"), True)
        self.assertEqual(perform_and_print_operation("<", "5", "2"), False)
        self.assertEqual(perform_and_print_operation(">", "5", "2"), True)
        self.assertEqual(perform_and_print_operation("<=", "5", "2"), False)
        self.assertEqual(perform_and_print_operation(">=", "5", "2"), True)
