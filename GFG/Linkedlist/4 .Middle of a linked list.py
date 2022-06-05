class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        linked_list_length = self.findlength(head)
        # if linked_list_length%2 == 0:
        #     linked_list_mid = linked_list_length // 2 + 1
        # else:
        linked_list_mid = linked_list_length // 2
        pnt = head
        count = 0
        if pnt.next is None:
            return pnt.data
        while True:
            pnt = pnt.next
            count += 1
            if count == linked_list_mid:
                return pnt.data

    def findlength(self, head):
        pnt = head
        count = 0
        while pnt != None:
            count += 1
            pnt = pnt.next
        return count
        # Code here
        # return the value stored in the middle node
