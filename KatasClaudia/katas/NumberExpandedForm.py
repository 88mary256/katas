def expanded_form(num):
    result = ""
    comodin = 1
    resto = 0
    while num > 0:
        resto = num % 10
        num = num / 10
        if resto > 0:
            if (len(result) > 0):
                result = str(resto * comodin) + " + " + result
            else:
                result = str(resto * comodin)

        comodin = comodin * 10

    return result


print expanded_form(70304)