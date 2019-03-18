'''a = 33
b = 200
if b > a: print (str(b) +"is greater than "+str(a))

some_value = 1
if some_value:
   print "Got a true expression value"
   print(some_value)
else:
   print "Got a false expression value"
   print(some_value)
'''

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



'''
genre = ['pop', 'rock', 'jazz']
# iterate over the list using index
for i in range(len(genre)):	
   print("I like", genre[i])
'''

