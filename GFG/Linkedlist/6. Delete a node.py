def delNode(head, k):
    # Code here
    prev = head
    count = 1
    linked_list_length = 0
    while prev is not None:
        linked_list_length += 1
        prev = prev.next
    prev = head
    if prev.next == None:
        return head
    if count == k:
        head = prev.next
        return head

    while count <= k - 1:

        if count == k - 1:
            if count == linked_list_length - 1:
                prev.next = None
                return head
            else:
                prev.next = prev.next.next
        prev = prev.next
        count += 1
    return head
