def getNth(head, k):
    # Code here
    pnt = head
    while pnt != None:
        k -= 1
        if k == 0:
            return pnt.data
        pnt = pnt.next
