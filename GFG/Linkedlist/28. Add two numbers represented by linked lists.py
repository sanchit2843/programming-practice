class Solution:
    # Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list

        temp = first
        num1 = []
        while temp is not None:
            num1.append(str(temp.data))
            temp = temp.next
        num1 = int("".join(num1))

        temp = second
        num2 = []
        while temp is not None:
            num2.append(str(temp.data))
            temp = temp.next
        num2 = int("".join(num2))

        s = str(num1 + num2)

        updated_list = Node(int(s[0]))
        head = updated_list
        for i in s[1:]:
            updated_list.next = Node(int(i))
            updated_list = updated_list.next
        return head
