class Node:
    def __init__(self, c):
        self.c = c
        self.next = None
        self.prev = None


def string_to_linked_list(s):
    head = Node(s[0])
    cur = head
    for i in range(1, len(s)):
        nxt = Node(s[i])
        cur.next = nxt
        nxt.prev = cur
        cur = nxt

    return head


def linked_list_to_string(head):
    s = ""
    while head is not None:
        s += head.c
        head = head.next

    return s


# this gets TL on test 27 and I have no idea why
def convert_to_good_string(s: str) -> str:
    if len(s) == 0 or len(s) == 1:
        return s
    head = string_to_linked_list(s)
    cur = head
    while cur is not None and cur.next is not None:
        if cur.c != cur.next.c and cur.c.lower() == cur.next.c.lower():
            if cur.prev is None and cur.next.next is None:
                return ""
            else:
                if cur.prev is None:
                    cur.next.next.prev = None
                    cur = cur.next.next
                    head = cur
                elif cur.next.next is None:
                    cur.prev.next = None
                    break
                else:
                    cur.prev.next = cur.next.next
                    cur.next.next.prev = cur.prev
                    cur = cur.prev
        else:
            cur = cur.next
    result = linked_list_to_string(head)

    return result



probably_bad_string = "bB"
print(f"{probably_bad_string}:", convert_to_good_string(probably_bad_string))

probably_bad_string = "cbB"
print(f"{probably_bad_string}:", convert_to_good_string(probably_bad_string))

probably_bad_string = "bBc"
print(f"{probably_bad_string}:", convert_to_good_string(probably_bad_string))

probably_bad_string = "CaAc"
print(f"{probably_bad_string}:", convert_to_good_string(probably_bad_string))

probably_bad_string = "bBaAc"
print(f"{probably_bad_string}:", convert_to_good_string(probably_bad_string))

probably_bad_string = "cbBaA"
print(f"{probably_bad_string}:", convert_to_good_string(probably_bad_string))

probably_bad_string = "cbaAB"
print(f"{probably_bad_string}:", convert_to_good_string(probably_bad_string))

probably_bad_string = "baABc"
print(f"{probably_bad_string}:", convert_to_good_string(probably_bad_string))

probably_bad_string = "bBaAaAaAaAaAaA"
print(f"{probably_bad_string}:", convert_to_good_string(probably_bad_string))

probably_bad_string = "a"
print(f"{probably_bad_string}:", convert_to_good_string(probably_bad_string))
