
num= input("Ingrese un numero: ")
cadena = str(num)
indice = -1
iguales = 0
for x in range(0, len(cadena) / 2):
    if cadena[x] == cadena[indice]:
        iguales = iguales + 1
    indice = indice - 1
if iguales == (len(cadena) / 2):
    print ("Es capicuo")
else:
    print ("No es capicuo")

