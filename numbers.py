def binary (n):
    a = 1
    b= 5
    cont = 0
    flipflop = True
    while cont < n :
        if flipflop :
            print a
            a = a+1
        else :
            print b
            b = b-1
        flipflop = not flipflop
        cont += 1

n = input ("Por favor ingresar un numero :" )
binary(int(n))
