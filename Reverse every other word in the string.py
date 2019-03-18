def reverse_alternate(string):
    Result=""
    lista = string.split()
    i=0
    while i<len(lista):
        if i%2==0:
            Result=Result+lista[i]+' '
        else:
            j=len(lista[i])-1
            gato=''
            while j>=0:
                gato=gato+lista[i][j]
                j-=1
            Result = Result + gato + ' '
        i=i+1

    return Result

    #return lista
b= reverse_alternate("perro del mal: carlos?")
print b
'''print b[0]
print b[1]
print b[2]
print len(b)
print range(len(b))
'''