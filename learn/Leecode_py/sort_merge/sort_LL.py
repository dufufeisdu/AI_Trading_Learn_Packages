from LinkedList import LinkedList, create_linkedList_from_array
import math

# incorrect


def merge_sort_LL(LL):
    if not LL or not LL.next:
        return LL
    first = LL
    second = LL

    while first.next and first.next.next:
        first = first.next.next
        second = second.next
    first = second.next
    second.next = None
    second = first
    first = LL
    left = merge_sort_LL(first)
    right = merge_sort_LL(second)
    return merge(left, right)


def merge(left, right):
    if not right:
        return left
    dummy = LinkedList(-1)
    p = dummy
    while left and right:
        if left.value > right.value:
            p.next = right
            right = right.next
            p = p.next
        else:
            p.next = left
            left = left.next
            p = p.next
    if left:
        p.next = left
    if right:
        p.next = right

    return dummy.next

# def sort_LL(LL):
#     # merge sort
#     if not LL or LL.next == None:
#         return LL
#     # dummy = LinkedList(-math.inf)
#     # dummy.next = LL
#     LL_len = LL.get_len()
#     times = math.ceil(math.log2(LL_len))

#     while times:
#         i = 1
#         p = LL
#         while p:
#             p, q, rest = split_LL(p, i**2)
#             p, end = merge_lr(p, q)
#             end.next = rest
#             p = rest
#         i += 1
#         times -= 1
#     return LL


# def split_LL(start, step):
#     a = 0
#     p = start
#     while step != a:
#         p = p.next
#         a += 1
#     a = 0
#     q = p.next
#     p.next = None
#     while step != a:
#         q = q.next
#         a += 1
#     rest = q.next
#     q.next = None
#     return start, q, rest


# def merge_lr(left, right):
#     dummy = LinkedList(-math.inf)
#     p = dummy
#     while left and right:
#         if left.value > right.value:
#             p.next = left
#             left = left.next

#         else:
#             p.next = right
#             right = right.next
#         p = p.next

#     while left:
#         p.next = left
#         left = left.next
#         p = p.next
#     while right:
#         p.next = right
#         right = right.next
#         p = p.next
#     return dummy.next, p

if __name__ == '__main__':
    A = [3, 2, 1, 7, 4, 5, 6, 9, 0]
    A = create_linkedList_from_array(A)
    print(A)
    print(merge_sort_LL(A))
