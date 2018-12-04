# init a path [0,0....],same lenth as arr
# for each element in the arr:
#  update the path's correspondent element with +1
#  until reach the last element
# return the last element in path


def jump_gameII(arr):
    end = len(arr)
    if not end:
        return -1
    if end == 1:
        return 0

    path = [0 for i in range(end)]

    for idx, ele in enumerate(arr):
        left = idx
        right = idx + ele
        if right >= end:
            return path[left] + 1
        for i in range(left, right + 1):
            if path[i] == 0:
                path[i] = path[i] + 1

    return -1


if __name__ == "__main__":
    tests = [[2, 3, 1, 1, 4], [1], [1, 0, 1, 2, 4]]
    for test in tests:
        print(jump_gameII(test))
