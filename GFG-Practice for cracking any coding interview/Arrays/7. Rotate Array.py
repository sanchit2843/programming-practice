for i in range(int(input())):
    p, q = map(int, input().split())
    arr = list(map(int, input().split()))[:p]
    print(" ".join(list(map(str, arr[q:] + arr[:q]))))
