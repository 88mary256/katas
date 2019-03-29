def reverse_alternate(string):
    words = string.split(" ")
    result = ""

    for i in range(len(words)):
        word = words[i]
        if (word):
            result += (word if ((i % 2) == 0) else word[::-1]) + " "
    return result.strip()


palabra = raw_input("Ingrese una palabra: ")
reverse_alternate(palabra)
