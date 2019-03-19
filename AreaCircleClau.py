# Write a function area_of_circle(r) which returns the area of a circle of radius r only
# if the radius value is greater of 10.
def calculo (radio):
    area = 3.1415 * radio * radio
    return area


def  mayor(radio):
    print radio
    if radio > 10:
        return calculo(int(radio))
    else:
        print ("Su Radio es menor a 10, no podemos calcular el Area")


#Entrada
radio = input ("Ingrese el radio del circulo: ")
#Proceso
area = mayor(radio)

# Salida
print "El Area del circulo es: ", area