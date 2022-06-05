def multiplyTwoList(head1, head2):
    # Code here
    temp = head1
    num1 = []
    while temp is not None:
        num1.append(str(temp.data))
        temp = temp.next
    num1 = int("".join(num1))

    temp = head2
    num2 = []
    while temp is not None:
        num2.append(str(temp.data))
        temp = temp.next
    num2 = int("".join(num2))

    return num1 * num2 % (10 ** 9 + 7)
