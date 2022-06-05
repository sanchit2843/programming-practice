def union(head1, head2):
    # code here
    # return head of resultant linkedlist
    d1 = []
    d2 = []
    while head1:
        d1.append(head1.data)
        head1 = head1.next
    while head2:
        d2.append(head2.data)
        head2 = head2.next
    res = list(set(d1) | set(d2))
    res = sorted(res)
    node = Node(res[0])
    head = node
    for i in res[1:]:
        n = Node(i)
        node.next = n
        node = node.next
    return head
