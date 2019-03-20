import unittest

from examen.py.collection import *


class TestCollection(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(sortTuples([]), [])
        self.assertEqual(sortTuples([(3.0, "Number1")]), [(3.0, "Number1")])
        self.assertEqual(sortTuples([(3.0, "Number1"), (1.1, "Number 2")]), [(1.1, "Number 2"), (3.0, "Number1")])
        self.assertEqual(
            sortTuples([(3.0, "Number1"), (1.1, "Number 2"), (2.3, "Number 3"), (1.2, "Number 4"), (100, "Number 4")]),
            [(1.1, "Number 2"), (1.2, "Number 4"), (2.3, "Number 3"), (3.0, "Number1"), (100, "Number 4")])
