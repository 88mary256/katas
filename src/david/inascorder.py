def in_asc_order(arr):
    r = True
    n = len(arr)
    while n != 1 and r == True:
        if arr[n-2] > arr[n-1]:
            r = False
        n -= 1
    return r


array = [3, 2]
print in_asc_order(array)
