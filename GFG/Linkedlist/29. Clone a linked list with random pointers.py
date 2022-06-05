class Solution:
    # Function to clone a linked list with next and random pointer.
    def copyList(self, head):
        # code here
        if head is None or head.next is None:
            return head
        head_copy = Node(head.data)

        pnt = head.next
        pnt2 = head_copy

        pairs = []
        count = 0
        while pnt is not None:
            pnt2.next = Node(pnt.data)
            pnt = pnt.next
            pnt2 = pnt2.next

        pnt = head
        while pnt is not None:
            if pnt.arb is not None:
                pnt_ = head
                count1 = 0
                while pnt.arb != pnt_ or pnt_ is None:
                    pnt_ = pnt_.next
                    count1 += 1
                pairs.append((count, count1))
            count += 1
            pnt = pnt.next

        for i in pairs:
            p1, p2 = i
            pnt_1 = head_copy
            count = 0
            while count != p1:
                pnt_1 = pnt_1.next
                count += 1
            pnt_2 = head_copy
            count = 0
            while count != p2:
                pnt_2 = pnt_2.next
                count += 1
            pnt_1.arb = pnt_2
        return head_copy
