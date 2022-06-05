def searchEle(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return True
    return False
    # Code here


# fucntion must return true if
# insertion is successful or else
# return false
def insertEle(a, y, yi):
    if yi > len(a):
        return False
    else:
        b = a[yi:]
        a[yi] = y
        a.append(y)
        a[yi + 1 :] = b
        return True
    # Code here


# fucntion must return true if
# deletion is successful or else
# return false
def deleteEle(a, z):
    # Code here
    for i in range(len(a)):
        if a[i] == z:
            del a[i]
            return True
    return True
