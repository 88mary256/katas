def dashatize(num):
    if num == None:
        return 'None'
    else:
        if num < 0:
            num = num * -1
        num = str(num)
        char = ""
        i = 0
        while i < len(num):
            if int(num[i]) % 2 == 0:
                if int(num[i - 1]) % 2 == 0:
                    char = char + num[i]
                elif i==0:
                    char = char + num[i]
                else:
                    char = char + '-' + num[i]
            else:
                char = char + '-' + num[i]
            i += 1

        if int(num[0]) % 2 != 0:
            j = len(char)
            return char[1:j]
        else:

            return char


print dashatize(-28229)