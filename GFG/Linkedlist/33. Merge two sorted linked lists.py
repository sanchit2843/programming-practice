def sortedMerge(head1, head2):
    # code here

    if head2 is None:
        return head1
    if head1 is None:
        return head2
    temp = Node(0)
    res = temp
    a = head1
    b = head2
    while a is not None and b is not None:
        if a.data < b.data:
            temp.next = a
            a = a.next
            temp = temp.next
        else:
            temp.next = b
            b = b.next
            temp = temp.next
    temp.next = a if a is not None else b
    return res.next
