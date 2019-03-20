class Exercise1:

    @staticmethod
    def factorial(num):
        r = num
        if num < 2:
            return 1
        else:
            while num > 1:
                r = r * (num - 1)
                num -= 1
        return r
