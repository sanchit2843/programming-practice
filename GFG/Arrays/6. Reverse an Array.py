# code
import numpy as np

n = input()
arr = list()
for i in range(int(n)):
    s = input()
    ar = list()
    inp = input().split()
    for j in inp:
        ar.append(int(j))
    arr.append(np.asarray(ar))
