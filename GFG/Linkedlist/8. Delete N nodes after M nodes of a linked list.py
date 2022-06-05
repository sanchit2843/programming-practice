class Solution:
    def skipMdeleteN(self, head, M, N):
        # Code here
        curr = head

        # The main loop that traverses through the
        # whole list
        while curr:
            # Skip M nodes
            for count in range(1, M):
                if curr is None:
                    return
                curr = curr.next

            if curr is None:
                return

            # Start from next node and delete N nodes
            t = curr.next
            for count in range(1, N + 1):
                if t is None:
                    break
                t = t.next

            # Link the previous list with remaining nodes
            curr.next = t
            # Set Current pointer for next iteration
            curr = t
        return head

    def getLength(self, head):
        pnt = head
        count = 0
        while pnt is not None:
            count += 1
            pnt = pnt.next
        return count
