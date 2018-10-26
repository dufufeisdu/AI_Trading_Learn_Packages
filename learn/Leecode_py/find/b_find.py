

def b_find(arr, target):
    first = -1
    last = -1
    if not arr:
        return [first, last]
    head = 0
    tail = len(arr) - 1
    # find_pos = -1
    while head <= tail:
        mid = (head + tail) // 2
        if arr[mid] == target:
            first = find_pre_pos(arr, mid)
            last = find_last_pos(arr, mid)
            break
        elif arr[mid] > target:
            tail = mid - 1
        else:
            head = mid + 1
    # pos = find_pos
    # while find_pos > 0 and arr[pos] == target:
    #     first = pos
    #     pos -= 1
    # pos = find_pos
    # while find_pos > 0 and arr[pos] == target:
    #     last = pos
    #     pos += 1

    return [first, last]


def find_pre_pos(arr, pos):
    if pos == 0 or arr[pos] != arr[pos - 1]:
        return pos
    i = 0
    pre_pos = pos
    while pre_pos > 0 and arr[pos] == arr[pre_pos]:
        pre_pos = pos - 2**i
        i += 1
    i -= 1
    return find_pre_pos(arr, pos - 2**(i - 1))


def find_last_pos(arr, pos):
    if pos == len(arr) - 1 or arr[pos] != arr[pos + 1]:
        return pos
    i = 0
    last_pos = pos
    while last_pos < len(arr) and arr[pos] == arr[last_pos]:
        last_pos = pos + 2**i
        i += 1
    i -= 1
    return find_last_pos(arr, pos + 2**(i - 1))


if __name__ == '__main__':
    A = [1, 3, 5, 5, 5, 6, 6, 6, 6, 12]
    print(b_find(A, 12))
