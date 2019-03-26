class Adding:

    @staticmethod
    def sumto(n):
        sum = 0
        for i in range(1, n+1):
            if sum < 46:
                sum += i
        return sum

