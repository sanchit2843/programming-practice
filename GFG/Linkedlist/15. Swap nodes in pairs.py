class Solution:
    def pairWiseSwap(self, head):
        newNode = Node(0)
        newNode.next, head = head, newNode
        prev = head
        curr = head.next
        while curr and curr.next:
            temp = curr.next
            curr.next = temp.next
            temp.next = curr
            prev.next = temp
            prev = curr
            curr = curr.next
        head = head.next
        return head
