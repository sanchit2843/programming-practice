class Solution:
    def addOne(self, head):
        # Returns new head of linked List.
        pnt = head
        if head is None:
            return head
        if head.next is None:
            head.data = head.data + 1
            return head

        while pnt.next is not None:
            pnt_prev = pnt
            pnt = pnt.next
        pnt.data = pnt.data + 1
        return head
