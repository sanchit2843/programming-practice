class Solution:
    # Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        # remove the loop without losing any nodes
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                cur = head
                while cur != slow:
                    cur = cur.next
                    slow = slow.next

                temp = cur
                while temp.next != cur:
                    temp = temp.next
                temp.next = None
                break
        return head
