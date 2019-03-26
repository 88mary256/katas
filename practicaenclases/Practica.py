print "--------------1----------------------"


def factorial(num):
    if num > 0:
        i = 1
        Result = 1
        while i <= num:
            Result = Result * i
            i += 1
        return Result


print "--------------2----------------------"


def is_capicua(num):
    num = str(num)
    chain = ""
    j = len(num) - 1
    while j >= 0:
        chain = chain + num[j]
        j -= 1
    if chain == num:
        return "el numero es capicua"
    else:
        return "el numero no es capicua"


print "--------------3----------------------"

def carlosbubbleSort(arr):
    n = len(arr)


    for i in range(n):


        for j in range(0, n-i-1):

            if arr[j][0] > arr[j+1][0] :
                arr[j], arr[j+1] = arr[j+1], arr[j]


print "--------------5----------------------"


def is_palindromo(string):

    chain = ""
    j = len(string) - 1
    while j >= 0:
        chain = chain + string[j]
        j -= 1
    if chain == string:
        return "la cadena es palindromo"
    else:
        return "la cadena no es palindromo"





print "--------------6----------------------"

class Persona():

    def __init__(self, identificacion, nombre, apellido):
        self.identificacion = identificacion
        self.nombre = nombre
        self.apellido = apellido
    def __str__(self):
        return " %s: %s, %s" % (str(self.identificacion), self.apellido, self.nombre)


class AlumnoJALA(Persona):
    def __init__(self, identificacion, nombre, apellido, codigoAlumno):

        Persona.__init__(self, identificacion, nombre, apellido)

        self.codigoAlumno = codigoAlumno


