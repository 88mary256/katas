
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


def create_dictionary():
    size = raw_input("please set the size of the dictionary: ")
    for index in range(0, int(size)):
        key = raw_input(" str(index + 1): please set the key: ")
        value = raw_input(" str(index + 1): please set the value: ")
        myDictionary[key] = value
    print "keys: ", myDictionary.keys()
    print "values: ", myDictionary.values()
    print "dictionary: ", myDictionary
    return myDictionary


def haskey(key):
    return key in myDictionary


def hasValue(value):
    return value in myDictionary.values()


def circle_functions():
    r = int(raw_input("please set the radio of a circle "))
    print area_of_circle(r)
    print perimeter_of_circle(r)


def ages():
    size = raw_input("how many users are there: ")
    users = []
    for index in range(0, int(size)):
        age = raw_input(str(index) + ": what is the age: ")
        name = raw_input(str(index) + ": what is the name: ")
        users.append(User(name, int(age)))
    all_ages = ""
    for index in range(0, int(size)):
        all_ages += str(get_age_in_days(users[index].age)) + " "
    print all_ages
    all_ages = ""
    for index in range(0, int(size)):
        all_ages += str(get_age_in_hr(users[index].age)) + " "
    print all_ages
    all_ages = ""
    for index in range(0, int(size)):
        all_ages += str(get_age_in_min(users[index].age)) + " "
    print all_ages
    all_ages = ""
    for index in range(0, int(size)):
        what_am_I(users[index].age)


# main
ages()

circle_functions()

create_dictionary()
key = raw_input("please set a key to search")
print "our dictionary has the key? ", haskey(key)
key = raw_input("please set a value to search")
print "our dictionary has the value? ", haskey(key)

load_and_print_array()
