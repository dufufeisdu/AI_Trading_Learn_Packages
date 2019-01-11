def find_rotated_point(rotated_array):
    """Use binary search. Swap the start and the end when finds the rotated area"""
    start = 0
    end = len(rotated_array)
    if end == 1:
        return 0
    if end == 0:
        return -1
    end = end - 1

    while start != end - 1:
        mid = (start + end) // 2
        if rotated_array[start] <= rotated_array[mid]:
            start = mid
        elif rotated_array[mid] <= rotated_array[end]:
            end = mid
        else:
            return - 1
    return start


def rotated_array_search(rotated_array, ele):
    start = 0
    end = len(rotated_array) - 1
    pos = -1
    while start != end - 1:
        mid = (start + end) // 2
        if rotated_array[mid] ==
        if rotated_array[start] <= rotated_array[mid]:
            if rotated_array[start] < ele and ele <= rotated_array[mid]:
                end = mid
            elif rotated_array[start] == ele and rotated_array[end] != ele:
                return start
            elif rotated_array[start] == ele and rotated_array[end] == ele:
                start = mid
            else:
                start = mid

        else:
            if rotated_array[mid] < ele and ele <= rotated_array[end]:
                start = mid
            elif rotated_array[mid] == ele and rotated_array[start] != ele:
                end = mid
            else:
                end = mid
        if rotated_array[start] == ele:
            return start
        elif rotated_array[end] == ele:
            return end
        return -1


if __name__ == "__main__":
    tests = [[1], [2, 1], [2, 3, 1], [2, 3, 4, 1], [3, 4, 1, 2], [
        3, 4, 5, 1, 2], [3, 4, 5, 6, 1, 2], [4, 5, 6, 7, 1, 2, 3]]
    for test in tests:
        print(test, "--rotate pos->", rotated_point(test))
