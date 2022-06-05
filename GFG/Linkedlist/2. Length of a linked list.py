class Solution:

    # Function to count nodes of a linked list.
    def getCount(self, head_node):
        # code here
        count = 0
        pnt = head_node
        while pnt != None:
            count += 1
            pnt = pnt.next
        return count
