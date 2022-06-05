def flatten(root):
    # Your code here
    def sortedMerge(head1, head2):
        # code here
        if head2 is None:
            return head1
        if head1 is None:
            return head2
        temp = Node(0)
        res = temp
        a = head1
        b = head2
        while a is not None and b is not None:
            if a.data < b.data:
                temp.bottom = a
                a = a.bottom
                temp = temp.bottom
            else:
                temp.bottom = b
                b = b.bottom
                temp = temp.bottom
        temp.bottom = a if a is not None else b
        return res.bottom

    pnt = root
    merged_list = pnt
    pnt = pnt.next
    while pnt is not None:
        merged_list = sortedMerge(merged_list, pnt)
        pnt = pnt.next
    return merged_list
