def dashatize(num):
    if (num != None):
        str_num = str(num * -1) if (num < 0) else str(num)
        size = len(str_num)
        if (size > 1):
            result = str_num[0] + ("-" if (int(str_num[0]) % 2 == 1) else "")
            for i in range(1, size - 1):
                digit = str_num[i]
                result += ("-" + digit + "-") if (int(digit) % 2 == 1) else digit
            digit = str_num[size - 1]

            result += ("-" + digit) if (int(digit) % 2 == 1) else digit
            return result.replace("--", "-")
        else:
            return str_num
    return "None"


'''
clever
def dashatize(num):
    # get 'em
    if num == None:
        return "None"
    num = num*-1 if (num < 0) else num
    return "-".join(list(filter(None, re.split("(1|3|5|7|9)", str(num)))))
'''
