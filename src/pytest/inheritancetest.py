import unittest
from inheritance import Pet, Dog


class InheritanceTest(unittest.TestCase):

    def test_inheritance(self):
        self.assertEqual(True, isinstance(Pet, Dog))