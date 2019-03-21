def dashatize(num):
    if num is not None:
        s = str(abs(num))
        n = len(s)-1
        r = s[n] if int(s[n]) % 2 == 0 else "-" + s[n]
        ini = ""
        while n > 1:
            if int(s[n-1]) % 2 != 0:
                r = "-" + s[n-1] + r if r[0] == "-" or r[0] == "" else "-" + s[n-1] + "-" + r
            else:
                r = s[n-1] + r
            n -= 1
        if n > 1:
            ini = s[0] if int(s[0]) % 2 == 0 and r[1] != "-" else s[0] + "-"
        else:
            ini = s[0]
        return s[0] if n == 0 else ini + r
    else:
        return "None"

print dashatize(-28369)
