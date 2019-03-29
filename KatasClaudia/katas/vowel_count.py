def count_Vowel(line):
    if (line == None or len(line) < 1):
        return 0
    return len(''.join(c for c in line.lower() if c in ['a', 'e', 'i', 'o', 'u']))

palabra = raw_input("Ingrese una palabra: ")
count_Vowel(palabra)