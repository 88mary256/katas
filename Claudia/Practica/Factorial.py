def factorial (number):
    resu = 1
    for i in range(number):
        resu = resu * i
        print resu


# Entrada
num= input("Ingrese un numero: ")
# Proceso
factorial(num)
