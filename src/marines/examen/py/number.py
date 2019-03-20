def factorial(num):
    if (num == 0 or num == 1):
        return 1
    fact = 1
    for index in range(2,num+1):
        fact *= index
    return fact