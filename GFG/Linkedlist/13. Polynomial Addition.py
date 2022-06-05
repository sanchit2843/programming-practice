class Solution:
    # return a linked list denoting the sum with decreasing value of power
    def addPolynomial(self, poly1, poly2):
        h1 = poly1
        h2 = poly2
        new_node = node(1, 1)
        new_node_head = new_node
        while h1 is not None and h2 is not None:
            if h1.power == h2.power:
                temp = node(h1.coef + h2.coef, h1.power)
                new_node_head.next = temp
                new_node_head = new_node_head.next
                h1 = h1.next
                h2 = h2.next
            elif h1.power > h2.power:
                temp = node(h1.coef, h1.power)
                new_node_head.next = temp
                new_node_head = new_node_head.next
                h1 = h1.next
            else:
                temp = node(h2.coef, h2.power)
                new_node_head.next = temp
                new_node_head = new_node_head.next
                h2 = h2.next
        if h1 is None:
            while h2:
                temp = node(h2.coef, h2.power)
                new_node_head.next = temp
                new_node_head = new_node_head.next
                h2 = h2.next
        elif h2 is None:
            while h1:
                temp = node(h1.coef, h1.power)
                new_node_head.next = temp
                new_node_head = new_node_head.next
                h1 = h1.next

        return new_node.next
