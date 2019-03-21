def expanded_form(num):
    n = len(str(num))
    r = ""
    for i, single in enumerate(str(num)):
        if single == "0":
            continue
        aux = str(int(single) * (10 ** (n - 1 - i)))
        r += " + " + aux if i > 0 else aux
    return r


print expanded_form(7025)
