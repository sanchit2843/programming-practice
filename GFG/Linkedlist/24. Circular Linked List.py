def isCircular(head):
    # Code here
    slow = head.next

    while slow:
        if slow == head:
            return 1
        slow = slow.next

    return 0
