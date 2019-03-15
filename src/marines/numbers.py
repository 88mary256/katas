def isOdd(number):
    return number % 2 == 0


def isEven(number):
    return number % 2 == 1


def isPrime(number):
    for i in range(2, number):
        if(number % i == 0):
            return False
    return True

def primeList(init,end):
    primes = []
    for number in range(init,end +1):
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
    for i in range(1, n+1):
        sum += i
    return sum

print "---- IS ODD OR EVEN ----"

print 2, "isOdd?", isOdd(2)
print 2, "isEven?", isEven(2)

print 3, "isOdd?",isOdd(3)
print 3, "isEven?",isEven(3)

print "---- PRIMES LIST ----"
print primeList(1, 21)

print "---- AREA o ----"
print area_of_circle(1)
print area_of_circle(5)
print area_of_circle(10)
print area_of_circle(11)
print area_of_circle(15)

print "---- sum ----"
print sum_to(3)
print sum_to(10)

