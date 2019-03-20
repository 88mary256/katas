from unittest import TestCase


class TestIs_palindromo(TestCase):
    def test_is_palindromo(self):
        from practicaenclases.Practica import is_palindromo
        self.assertEqual(is_palindromo("anitalavalatina"), "la cadena es palindromo", "ok")
        self.assertEqual(is_palindromo("oso"), "la cadena es palindromo", "ok")
        self.assertEqual(is_palindromo("gato"), "la cadena no es palindromo", "ok")
