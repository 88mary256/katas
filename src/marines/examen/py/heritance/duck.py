class Duck:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def cuack(self):
        print "(%s) cuack" % self.name

    def swim(self):
        print "I(%s) can swiming" % self.name
