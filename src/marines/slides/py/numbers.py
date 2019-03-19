def isOdd(number):
    return number % 2 == 0


def isEven(number):
    return number % 2 == 1


def isPrime(number):
    for i in range(2, number):
        if (number % i == 0):
            return False
    return True


def primeList(init, end):
    primes = []
    for number in range(init, end + 1):
        if (isPrime(number)):
            primes.append(number)
    return primes


def area_of_circle(r):
    if (r > 10):
        return r * r * 3.1416
    else:
        return "not supported"


def sum_to(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum
