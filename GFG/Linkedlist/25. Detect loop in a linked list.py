class Solution:
    # Function to check if the linked list has a loop.
    def detectLoop(self, head):
        # code here
        slow = head
        fast = head
        if head is None or head.next is None:
            return False
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
