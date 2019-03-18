def function1():
    size = raw_input("please set the size of the array: ")
    print(size)
    myArray = []
    for index in range(0, int(size)):
        number = raw_input("please set the " + str(index + 1) + " value of the array: ")
        myArray.append(number)
    return myArray


def function2(myArray):
    print myArray

def function3():
    myArray = function1()
    function2(myArray)

function3()