import unittest

from katas.NumberExpandedForm import expanded_form


class TestExpandNumber(unittest.TestCase):
    def test_expandfrom(self):
        self.assert_equals(expanded_form(12), '10 + 2');
        self.assert_equals(expanded_form(42), '40 + 2');
        self.assert_equals(expanded_form(70304), '70000 + 300 + 4');