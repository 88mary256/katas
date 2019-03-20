def expanded_form(num):
    str_num = str(num)
    size = len(str_num)
    if (num > 0):
        result = str_num[0].ljust(size, "0")
        for i in range(1, size):
            digit = str_num[i]
            if (int(digit) > 0):
                result += " + " + digit.ljust(size - i, "0")
        return result
    return "0"


def expanded_number(num):
    str_num = str(num)
    size = len(str_num)
    if (num > 0):
        result = []
        result.append(int(str_num[0].ljust(size, "0")))
        for i in range(1, size):
            digit = str_num[i]
            if (int(digit) > 0):
                result.append(int(digit.ljust(size - i, "0")))
        result.reverse()
        return result
    return [0]