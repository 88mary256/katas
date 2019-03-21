def sumto(n):
    sum=0
    for i in range(1, n+1):
        if sum < 46:
            sum += i
    print(sum)


sumto(3)
