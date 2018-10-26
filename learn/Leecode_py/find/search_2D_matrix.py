from search_insert_pos import search_insert_pos
from b_find import b_find


def search_2D_matrixI(mx, target):
    ls = [i[0] for i in mx]
    index = search_insert_pos(ls, target)
    if index < len(mx):
        has_element = b_find(mx[index], target)
        if has_element != -1:
            return True
    else:
        return False
    return False


def search_2D_matrixII(mx, target):
    m = len(mx)
    n = len(mx[0])
    head = 0
    tail = m * n - 1
    while head <= tail:
        mid = (head + tail) // 2
        i, j = divmod(mid, n)
        if mx[i][j] == target:
            return True
        elif mx[i][j] > target:
            tail = mid - 1
        else:
            head = mid + 1
    return False
