class Solution:
    def display(self, node):
        # code here
        pnt = node
        while pnt != None:
            print(pnt.data, end=" ")
            pnt = pnt.next
