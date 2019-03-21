class Pet:
    @classmethod
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    @classmethod
    def ows(self):
        return self.name + " belongs to " + self.owner


class Dog(Pet):

    @classmethod
    def __init__(self, name, owner, family):
        Pet.__init__(self, name, owner)
        self.familyname = family

    @classmethod
    def getdog(self):
        return self.ows() + ", It is " + self.familyname + " family's pet"


p = Pet("Santa's Little Helper", "Bart")
d = Dog("Santa's Little Helper", "Bart", "Simpson")

print(p.ows())
print(d.getdog())