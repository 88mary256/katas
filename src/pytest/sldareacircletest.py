import unittest
from areacircle import Area


class OperationsTest(unittest.TestCase):

    def test_areacircle(self):
        self.assertEqual("Only number greater than 10", Area.area_of_circle(10))
        self.assertEqual("Only number greater than 10", Area.area_of_circle(9))
        self.assertEqual(380.132711084365, Area.area_of_circle(11))