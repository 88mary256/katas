from unittest import TestCase


class TestFactorial(TestCase):
    def test_factorial(self):
        from practicaenclases.Practica import factorial
        self.assertEqual(factorial(5),120,"ok")


    def test_factorial_zero(self):
        from practicaenclases.Practica import factorial
        self.assertEqual(factorial(0),None,"ok")
