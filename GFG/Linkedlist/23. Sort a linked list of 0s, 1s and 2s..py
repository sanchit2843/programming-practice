class Solution:
    # Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        # code here
        d = {0: 0, 1: 0, 2: 0}
        pnt = head
        while pnt is not None:
            d[pnt.data] += 1
            pnt = pnt.next
        pnt = head
        for i in range(3):
            for j in range(d[i]):
                pnt.data = i
                pnt = pnt.next
        return head
