import unittest
from inascorder import Excercise4

class orderTest(unittest.TestCase):


    def test_ascorder(self):
        numbers = [(2.9, 'Number1'), (3.0, 'number2'), (2.5, 'number3')]
        self.assertEqual([(2.5, 'number3'), (2.9, 'Number1'), (3.0, 'number2')], Excercise4.sortnumbers(numbers))