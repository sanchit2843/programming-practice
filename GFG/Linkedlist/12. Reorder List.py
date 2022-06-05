def reorderList(self):
    if self.head == None or self.head.next == None:
        return
    # write code to reorder Nodes of Linked_List
    def getLength(head):
        pnt = head
        count = 0
        while pnt is not None:
            count += 1
            pnt = pnt.next
        return count

    def reverseList(head):
        # Code here
        prev = None
        if head is None or head.next is None:
            return head
        while head is not None:
            front = node(head.data)
            front.next = prev
            prev = front
            head = head.next
        return front

    linked_list_length = getLength(self.head)
    # get head to mid point of list
    count = 0
    mid_pnt = self.head
    while count != linked_list_length // 2:
        mid_pnt = mid_pnt.next
        count += 1
    temp = mid_pnt
    mid_pnt = mid_pnt.next
    temp.next = None
    front_list = self.head

    reversed_mid_list = reverseList(mid_pnt)

    count = 0
    while front_list is not None and reversed_mid_list is not None:
        count += 1
        temp = front_list.next
        front_list.next = reversed_mid_list
        front_list = front_list.next
        reversed_mid_list = reversed_mid_list.next
        front_list.next = temp
        front_list = front_list.next
    if reversed_mid_list is not None:
        front_list.next = reversed_mid_list

    return self.head
