def sum_to(n):
    sumto=0
    for i in range(1, n+1):
        if sumto < 46:
            sumto += i
    print(sumto)


sum_to(3)
