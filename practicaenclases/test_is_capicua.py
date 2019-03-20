from unittest import TestCase


class TestIs_capicua(TestCase):
    def test_is_capicua(self):
        from practicaenclases.Practica import carlosbubbleSort
        arr = [(3, "Richter"), (2, "Hernando"), (1, "Carlos"), (4, "Rodriguez")]
        sortedarr= [(1, "Carlos"), (2, "Hernando"), (3, "Richter"), (4, "Rodriguez")]
        self.assertLessEqual(carlosbubbleSort(arr),sortedarr,"ok")
