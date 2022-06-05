def removeDuplicates(head):
    # code here
    pnt = head
    pnt1 = pnt.next
    while pnt1 is not None:
        if pnt.data == pnt1.data:
            pnt1 = pnt1.next
        else:
            pnt.next = pnt1
            pnt = pnt1
            pnt1 = pnt1.next
    pnt.next = pnt1
    return head
