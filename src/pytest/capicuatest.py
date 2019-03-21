import unittest
from capicua import Exercise2

class OperationsTest(unittest.TestCase):


    def test_capicua(self):
        self.assertEqual(True, Exercise2.iscapicua(2992))
        self.assertEqual(True, Exercise2.iscapicua(24142))
        self.assertEqual(True, Exercise2.iscapicua(1))
        self.assertEqual(False, Exercise2.iscapicua(123))
        self.assertEqual(False, Exercise2.iscapicua(1234))