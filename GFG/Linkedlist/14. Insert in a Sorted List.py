class Solution:
    def sortedInsert(self, head1, key):
        # code here
        # return head of edited linked list
        pnt = head1
        pnt_next = head1.next
        if key <= pnt.data:
            temp = Node(key)
            temp.next = pnt
            head1 = temp
            return head1

        while pnt.next is not None:
            if pnt_next.data == key or pnt_next.data > key and pnt.data < key:
                temp = Node(key)
                pnt.next = temp
                temp.next = pnt_next
                # pnt = pnt_next
                # pnt_next = pnt_next.next
                return head1
            pnt = pnt.next
            pnt_next = pnt_next.next
        if key >= pnt.data:
            temp = Node(key)
            pnt.next = temp
            temp.next = None
        return head1
