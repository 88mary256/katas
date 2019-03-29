# According a list of values between a Min and Max range, identify if the number is prime or not.
# Funciones
def es_primo(num):
    cont = 0
    i = 1
    while i<= num:
        if num % i == 0:
            cont = cont + 1
        i = i+1
    return cont
def crear_lista(num):

    lista = []
    i = 2
    while i <= num:
        lista.append(i)
        i = i+1
    return lista
def get_primo (lista) :
    primos = []
    for num in lista:
        verificado = es_primo(num)
        if verificado == 2 :
            primos.append(num)
    return primos

#Entrada
num = input ("Ingrese un numero natural: ")
#Proceso
lista = crear_lista(num)
primos = get_primo(lista)

# Salida
print "Los numeros primos entre 1 y ", num, "son: ", primos