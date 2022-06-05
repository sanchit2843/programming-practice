class Solution:
    def isPalindrome(self, head):
        # code here
        def reverse_list(head):
            if head is None or head.next is None:
                return head
            prev = None
            while head is not None:
                front = Node(head.data)
                front.next = prev
                prev = front
                head = head.next
            return front

        reversed_list = reverse_list(head)
        while head is not None:
            if head.data != reversed_list.data:
                return False
            reversed_list = reversed_list.next
            head = head.next
        return True
