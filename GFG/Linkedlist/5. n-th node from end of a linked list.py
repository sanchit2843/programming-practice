def getNthFromLast(head, n):
    # code here
    def getlength(head):
        pnt = head
        count = 0
        while pnt is not None:
            count += 1
            pnt = pnt.next
        return count

    length = getlength(head)
    if n > length:
        return -1
    node_to_check = length - n
    pnt = head
    count = 0
    while pnt is not None:

        if count == node_to_check:
            return pnt.data
        count += 1
        pnt = pnt.next
