def primenumber(numbers):
    for val in numbers:
        isprime = True
        if val % 2 == 0 or val % 3 == 0 or val <= 1:
            print("It is not prime number", val)
            continue
        for i in range(4, val):
            if val % i == 0:
                isprime = False
        print ("It is prime number", val) if isprime else ("It is not prime number", val)
        continue


primenumber([8, 7, 11, 15])
