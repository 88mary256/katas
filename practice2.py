print "-----------1-------------------"
print "Create 1 script to determine is a number is odd or even (use single line statement if applies)"

some_value = 11
if (some_value%2)==0:
   print str(some_value)+" is a EVEN value"

else:
   print str(some_value)+" is a ODD value"

print "----------------2--------------"
print "According a list of values between a Min and Max range, identify if the number is prime or not."

def is_prime(number):
    i=1
    contadorPrimos=0
    while(i<=number):
        if(number%i==0):
            contadorPrimos += 1
        i+=1

    if (contadorPrimos == 2):
        return True
    else:
        return False

List = [2, 5, 13, 22,50, 100]

for val in List:
    flag = is_prime(val)
    if (flag == True):
        print str(flag) + " is prime"

    else:
        print str(flag) + " isn't prime"




def area_of_circle(r):
    if(r>10):
        area=3.14159*r**2
    else:
        print "the radio es less than 10"
        return 0
    return area

r1=area_of_circle(12)
print "el radio es " + str(r1)

print "--------------------------------------"

def sum_to(n):
    if(n<35):
        sum = 0
        counter = 1
        while(counter <= n):
            sum = sum + counter
            counter = counter + 1
        return sum
    else:
        print "n exceeds 35"
    return 0

n1=sum_to(10)
print "the sum is " + str(n1)

print "--------------------------------------"
def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def days_in_month(month, year):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if month == 2:
        if leap_year(year):
            return 29
        return 28
    return 30

print(days_in_month(2, 2021))