from examen.py.heritance.duck import Duck
from examen.py.heritance.flyable import Flyable


class MallarDuck(Duck, Flyable):
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def fly(self):
        print "I(%s) can fly" % self.name
