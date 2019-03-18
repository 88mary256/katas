def occurrencies(string):
    n = len(string)-1
    alphabet = {}
    strg = string.lower()
    print strg
    while n != 0:
        if strg[n] != " ":
            if strg[n] in alphabet:
                alphabet[strg[n]] += 1
            else:
                alphabet[strg[n]] = 1
        n -= 1
    return alphabet
list = occurrencies("ThiS is String with Upper and lower case Letters")
print list
