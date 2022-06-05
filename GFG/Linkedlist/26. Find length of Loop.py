def countNodesinLoop(head):
    # Your code here
    fast = head
    slow = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            count = 1
            slow = slow.next
            while slow != fast:
                count += 1
                slow = slow.next
            return count
    return 0
