from node import Node

def Reverse(head: Node, left: int, right: int) -> Node:
    if left == right:
        return head
    left = 1 if left < 1 else left
    to_reverse = []
    cur = head
    left_prev = None
    right_next = None
    while cur:
        if cur.value == left - 1:
            left_prev = cur
        elif left <= cur.value <= right:
            to_reverse.append(cur)
        elif cur.value == right + 1:
            right_next = cur
        cur = cur.next

    i = len(to_reverse) - 1
    while i > 0:
        to_reverse[i].next = to_reverse[i-1]
        i -= 1

    if left_prev is None and right_next is None:
        to_reverse[0].next = None
        head.val = to_reverse[-1].val
        head.next = to_reverse[-1].next
        return to_reverse[-1]

    if left_prev is None:
        to_reverse[0].next = right_next
        return to_reverse[-1]

    if right_next is None:
        left_prev.next = to_reverse[-1]
        to_reverse[0].next = None
        return head

    if left_prev is not None and right_next is not None:
        left_prev.next = to_reverse[-1]
        to_reverse[0].next = right_next
        return head