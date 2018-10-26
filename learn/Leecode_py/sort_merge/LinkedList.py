class LinkedList():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        p = self
        s = ''
        while p:
            s += " "
            s += str(p.value)
            p = p.next
        return s

    def get_len(self):
        i = 0
        p = self
        while p:
            i += 1
            p = p.next
        return i


def create_linkedList_from_array(ls):
    dummy = LinkedList(0)
    p = dummy
    for value in ls:
        node = LinkedList(value)
        p.next = node
        p = p.next

    return dummy.next
