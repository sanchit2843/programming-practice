class Solution:
    def reverse(self, head, k):
        # Code here
        if k == 1:
            return head

        def reverse_list(head):
            prev = None
            if head is None or head.next is None:
                return head
            while head is not None:
                front = Node(head.data)
                front.next = prev
                prev = front
                head = head.next
            return front

        partial_lists = []
        count = 0
        pnt = head
        pnt_front = head
        while pnt.next is not None:
            if count == k - 1:
                temp = pnt.next
                pnt.next = None
                partial_lists.append(reverse_list(pnt_front))
                pnt = temp
                pnt_front = temp
                count = 0
            else:
                count += 1
                pnt = pnt.next
        partial_lists.append(reverse_list(pnt_front))
        head = partial_lists[0]
        for i in range(len(partial_lists) - 1):
            p1 = partial_lists[i]
            while p1.next is not None:
                p1 = p1.next
            p1.next = partial_lists[i + 1]
        return head
