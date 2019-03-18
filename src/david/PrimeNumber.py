def primenumber():
    numbers = [8, 7, 11, 15]
    for val in numbers:
        isprimo = True
        if val % 2 == 0 or val % 3 == 0 or val <= 1:
            print("It is not prime number", val)
            continue
        for i in range(4, val):
            if val % i == 0:
                isprimo = False
        if isprimo: print ("It is prime number", val)
        else: print("It is not prime number", val)
        continue
primenumber()