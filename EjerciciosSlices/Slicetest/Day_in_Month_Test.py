Import
unittest

from EjerciciosSlices.Slicetest import *


class TestMonth(unittest.TestCase):
    def test_month(self):
        self.assertEqual(month("Enero", "Enero"))
        self.assertEqual(month("Febrero", "Febrero"))
        self.assertEqual(month("Marzo", "Marzo"))
        self.assertEqual(month("Abril", "Abril"))
        self.assertEqual(month("Mayo", "Mayo"))
        self.assertEqual(month("Junio", "Junio"))
        self.assertEqual(month("Julio", "Julio"))
        self.assertEqual(month("Agosto", "Agosto"))
        self.assertEqual(month("Septiembre", "Septiembre"))
        self.assertEqual(month("Octubre", "Octubre"))
        self.assertEqual(month("Noviembre", "Noviembre"))
        self.assertEqual(month("Diciembre", "Diciembre"))
