class Exercise2:

    @staticmethod
    def iscapicua(num):
        s = str(num)
        n = len(s)
        if n == 1:
            return True
        i = 0
        r = False
        if n % 2 == 0:
            while i != n/2:
                if s[i] == s[n - 1 - i]:
                    r = True
                else:
                    r = False
                    break
                i += 1
        else:
            while i != (n-1)/2:
               if s[i] == s[n - 1 - i]:
                   r = True
               else:
                    r = False
                    break
               i += 1
        return r

