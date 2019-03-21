from unittest import TestCase


class TestIs_capicua(TestCase):
    def test_is_capicua(self):
        from practicaenclases.Practica import is_capicua
        self.assertEqual(is_capicua(121), "el numero es capicua", "ok")
        self.assertEqual(is_capicua(1231), "el numero no es capicua", "ok")
        self.assertEqual(is_capicua(1221), "el numero es capicua", "ok")
        self.assertEqual(is_capicua(1), "el numero es capicua", "ok")
        self.assertEqual(is_capicua(55), "el numero es capicua", "ok")
