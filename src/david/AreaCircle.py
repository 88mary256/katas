import math


def area_of_circle(r):
    if r > 10:
        print ("Area = ", math.pi * r**2)
    else:
        print ("Only number greater than 10")


area_of_circle(18)
