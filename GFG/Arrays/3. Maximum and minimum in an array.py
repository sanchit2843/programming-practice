def getMinMax(a, n):
    max = 0
    min = 10 ** 12
    for i in range(n):
        if a[i] > max:
            max = a[i]
        if a[i] < min:
            min = a[i]
    return min, max
