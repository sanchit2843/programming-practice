class Solution:
    # Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        d = {}
        pnt = head
        while pnt is not None:
            if pnt.data in d.keys():
                d[pnt.data] += 1
            else:
                d[pnt.data] = 1
            pnt = pnt.next
        pnt = head
        pnt1 = head.next
        while pnt1 is not None:
            if d[pnt1.data] > 1:
                d[pnt1.data] -= 1
                pnt.next = pnt1.next
                pnt1 = pnt1.next

            else:
                pnt = pnt1
                pnt1 = pnt1.next

        return head
