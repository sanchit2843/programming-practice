class Solution:
    # Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        prev = None
        if head is None or head.next is None:
            return head
        while head is not None:
            front = Node(head.data)
            front.next = prev
            prev = front
            head = head.next
        return front
