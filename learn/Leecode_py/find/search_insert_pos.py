def search_insert_pos(ls, target):
    if not ls:
        return 0
    head = 0
    tail = len(ls)
    while tail >= head:
        mid = (head + tail) // 2
        if mid >= tail:
            return mid
        if ls[mid] == target:
            return mid
        elif ls[mid] > target:
            mid -= 1
            tail = mid
        else:
            mid += 1
            head = mid
    return mid


if __name__ == '__main__':
    A = [1, 3, 5, 7, 9, 11, 12]
    print(search_insert_pos(A, 13))
