def load_integer_array():
    size = raw_input("please set the size of the array: ")
    print(size)
    myArray = []
    for index in range(0, int(size)):
        number = raw_input("please set the " + str(index + 1) + " value of the array: ")
        myArray.append(number)
    return myArray


def print_array(myArray):
    print myArray


def load_and_print_array():
    myArray = load_integer_array()
    print_array(myArray)


load_and_print_array()
