class Solution:
    def findIntersection(self, head1, head2):
        # code here
        # return head of intersection list
        d1 = {}
        d2 = []
        h1 = head1
        count = 0
        while head1:
            d1[head1.data] = count
            head1 = head1.next
            count += 1
        while head2:
            d2.append(head2.data)
            head2 = head2.next

        res = list(set(d1.keys()) & set(d2))
        index_ = [d1[x] for x in res]
        res = [x for _, x in sorted(zip(index_, res))]

        node = Node(res[0])
        head = node
        for i in res[1:]:
            n = Node(i)
            node.next = n
            node = node.next
        return head
