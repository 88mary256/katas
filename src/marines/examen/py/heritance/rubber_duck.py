from examen.py.heritance.duck import Duck


class RubberDuck(Duck):
    def __init__(self, name, type):
        self.name = name
        self.type = type


    def cuack(self):
        print "(%s) squish" % self.name
