class Solution:
    def divide(self, N, head):
        # code here
        even_head = None
        odd_head = None
        last_even = None
        last_odd = None

        curr = head
        while curr is not None:
            if curr.data % 2 == 0:
                if even_head is None:
                    even_head = last_even = curr
                else:
                    last_even.next = curr
                    last_even = last_even.next
            else:
                if odd_head is None:
                    odd_head = last_odd = curr
                else:
                    last_odd.next = curr
                    last_odd = last_odd.next
            curr = curr.next
        if even_head is not None:
            head = even_head
        if last_even is not None:
            last_even.next = odd_head
        if last_odd is not None:
            last_odd.next = None
        return head
