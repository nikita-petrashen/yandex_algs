class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def create_linked_list(rang):
    head = Node(1)
    cur = head
    for i in range(2, rang+1):
        nxt = Node(i)
        cur.next = nxt
        cur = nxt

    return head


def print_linked_list(head):
    s = ""
    cur = head
    while cur is not None:
        s += f"{cur.value} -> "
        cur = cur.next

    s += "None"

    print(s)


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


head = create_linked_list(5)
print_linked_list(head)
print("2 : 4")
print_linked_list(Reverse(head, 2, 4))

head = create_linked_list(5)
print("1 : 4")
print_linked_list(Reverse(head, 1, 4))

head = create_linked_list(5)
print("2 : 5")
print_linked_list(Reverse(head, 2, 5))

head = create_linked_list(5)
print("4 : 4")
print_linked_list(Reverse(head, 4, 4))

head = create_linked_list(5)
print("1 : 5")
print_linked_list(Reverse(head, 1, 5))

head = create_linked_list(5)
print("-1 : 6")
print_linked_list(Reverse(head, -1, 6))




