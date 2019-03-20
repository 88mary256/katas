import unittest

from examen.py.heritance.duck import Duck
from examen.py.heritance.flyable import Flyable
from examen.py.heritance.mallar_duck import MallarDuck
from examen.py.heritance.red_duck import RedDuck
from examen.py.heritance.rubber_duck import RubberDuck


class TestDuck(unittest.TestCase):
    def test_duck(self):
        duck = Duck("donald", "duck")
        duck.cuack()
        duck.swim()
        self.assertTrue(isinstance(duck,Duck))


    def test_mallar(self):
        mallar = MallarDuck("mallar 1", "mallar")
        mallar.cuack()
        mallar.swim()
        mallar.fly()
        self.assertTrue(isinstance(mallar,MallarDuck))
        self.assertTrue(isinstance(mallar,Duck))
        self.assertTrue(isinstance(mallar,Flyable))


    def test_red_duck(self):
        red_duck = RedDuck("red 1", "red_duck")
        red_duck.cuack()
        red_duck.swim()
        red_duck.fly()
        red_duck.run()
        self.assertTrue(isinstance(red_duck,RedDuck))
        self.assertTrue(isinstance(red_duck,Duck))
        self.assertTrue(isinstance(red_duck,Flyable))

    def test_rubber_duck(self):
        rubber = RubberDuck("rubber 1", "rubber")
        rubber.cuack()
        rubber.swim()

        self.assertTrue(isinstance(rubber,RubberDuck))
        self.assertTrue(isinstance(rubber,Duck))
        self.assertFalse(isinstance(rubber,RedDuck))
        self.assertFalse(isinstance(rubber,Flyable))