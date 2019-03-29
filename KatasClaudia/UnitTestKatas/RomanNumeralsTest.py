import unittest




class RomanNumerals(unittest.TestCase):
    def test_RomanNumeral(self):
        self.assert_equals(RomanNum(10), 'X');
        self.assert_equals(RomanNum(15), '40 + 2');
        self.assert_equals(RomanNum(70304), '70000 + 300 + 4');