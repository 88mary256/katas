import math


class Area:

    @staticmethod
    def area_of_circle(r):
        if r > 10:
            return math.pi * r**2
        else:
            return "Only number greater than 10"

