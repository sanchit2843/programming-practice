def intersetPoint(head1, head2):
    def length(head):
        pnt = head
        count = 0
        while pnt is not None:
            count += 1
            pnt = pnt.next
        return count

    l1 = length(head1)
    l2 = length(head2)
    if l1 > l2:
        pnt1 = head1
        pnt2 = head2
        count = 0
        while count < l1 - l2:
            if pnt1.next == pnt2.next:
                return pnt1.next.data
            pnt1 = pnt1.next
            count += 1
    else:
        pnt1 = head1
        pnt2 = head2
        count = 0
        while count < l2 - l1:
            if pnt1.next == pnt2.next:
                return pnt2.next.data
            pnt2 = pnt2.next
            count += 1
    while pnt1 and pnt2:
        if pnt1.next == pnt2.next:
            return pnt1.next.data
        pnt1 = pnt1.next
        pnt2 = pnt2.next
    return -1
