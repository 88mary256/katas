newArray = []
def arrayN():
    nElements = input("Introduce lenght of new array")
    try:
        n = int(nElements)
        if n > 0:
            while n != 0:
                element = input("Introduce a new value")
                newArray.append(element)
                n -= 1
        else:
            print ("Number must be greater than zero")

    except ValueError:
        print("Not a valid integer input")
    return newArray


def functionReceptor(newArray):
    print (" ".join(str(x) for x in newArray))


arrayN()
functionReceptor(newArray)
