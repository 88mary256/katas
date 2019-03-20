print "-----------1-------------------"
print "Create 1 script to determine is a number is odd or even (use single line statement if applies)"

some_value = 11
if (some_value % 2) == 0:
    print str(some_value) + " is a EVEN value"

else:
    print str(some_value) + " is a ODD value"

print "----------------2--------------"
print "According a list of values between a Min and Max range, identify if the number is prime or not."


def is_prime(number):
    i = 1
    contadorPrimos = 0
    while i <= number:
        if number % i == 0:
            contadorPrimos += 1
        i += 1

    return contadorPrimos == 2

List = [2, 5, 7, 11, 13, 8]

for val in List:
    flag = is_prime(val)
    print str(flag) + " is prime"
    '''if flag == True:
        print str(flag) + " is prime"

    else:
        print str(flag) + " isn't prime"

'''


    def carlosbubbleSort(arr):
        n = len(arr)

        # Traverse through all array elements
        for i in range(n):

            # Last i elements are already in place
            for j in range(0, n - i - 1):

                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j][0] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]


    arr = [64, 34, 25, 12, 22, 11, 90]
    carlosbubbleSort(arr)

    print ("Sorted array is:")
    for i in range(len(arr)):
        print ("%d" % arr[i]),
