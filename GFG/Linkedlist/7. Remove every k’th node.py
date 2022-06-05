def deleteK(head, k):
    # code here
    pos = 1
    prev = head
    if k == 1:
        return None
    if k == 0:
        return head
    while prev is not None and prev.next is not None:
        if (pos + 1) % k == 0:
            prev.next = prev.next.next
            pos += 1
        prev = prev.next
        pos += 1
    return head
