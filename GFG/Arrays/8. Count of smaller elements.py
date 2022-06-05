def countOfElements(a, n, x):
    count = 0
    for i in range(n):
        if a[i] <= x:
            count += 1
    return count
