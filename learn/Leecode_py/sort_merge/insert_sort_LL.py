from LinkedList import LinkedList, create_linkedList_from_array
import math


def insertion_sort_LL(LL):
    if not LL:
        return None
    p = LL
    dummy = LinkedList(-math.inf)
    dummy.next = LL
    while p.next:
        q = dummy
        while not (q is p):
            if p.next.value < q.next.value:
                v = p.next
                p.next = v.next
                v.next = q.next
                q.next = v
                break
            q = q.next
        else:
            p = p.next

    return dummy.next


if __name__ == '__main__':
    A = [3, 2, 1, 7, 4, 5, 6, 9, 0]
    A = create_linkedList_from_array(A)
    print(A)
    print(insertion_sort_LL(A))
