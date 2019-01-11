import unittest


def remove_duplicate(sorted_arr):
    length = len(sorted_arr)
    if length <= 1:
        return sorted_arr
    j = 1
    for i in range(1, length):
        if sorted_arr[i] != sorted_arr[j - 1]:
            sorted_arr[j] = sorted_arr[i]
            j += 1
    return sorted_arr[:j]


def remove_duplicate_more_than_twice(sorted_arr, max_duplicate=2):
    length = len(sorted_arr)
    if length <= 2:
        return sorted_arr
    j = 2
    if sorted_arr[0] == sorted_arr[1]:
        duplicate = 2
    else:
        duplicate = 0
    for i in range(2, length):
        if sorted_arr[i] != sorted_arr[j - 1]:
            sorted_arr[j] = sorted_arr[i]
            j += 1
            duplicate = 0

        elif duplicate < max_duplicate - 1:
            sorted_arr[j] = sorted_arr[i]
            j += 1
            duplicate += 1

    return sorted_arr[:j]

# incorrect
# def remove_duplicate_more_than_nth(sorted_arr, max_duplicate=2):
#     n = len(sorted_arr)
#     if n <= 2:
#         return sorted_arr
#     j = 2
#     for i in range(2, n):
#         if sorted_arr[j - 2] != sorted_arr[i]:
#             sorted_arr[j] = sorted_arr[i]
#             j += 1
#     return sorted_arr[:j]


class Test_Remove_Duplicate(unittest.TestCase):
    pass


if __name__ == "__main__":
    tests = [[], [1], [1, 1, 1], [1, 2, 1, 1], [1, 1, 2, 2], [
        1, 1, 1, 1], [1, 1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5]]
    I_result = [[], [1], [1], [1, 2], [1, 2], [1], [1, 2, 3, 4, 5]]
    II_result = [[], [1], [1, 1, 1], [1, 1, 2], [
        1, 1, 2, 2], [1, 1], [1, 1, 2, 3, 3, 4, 4, 5, 5]]
    for idx, test in enumerate(tests):
        # unittest.TestCase().assertEqual(
        #     remove_duplicate(tests[i]), I_result[i], 'Incorrect')
        print("Problem One:", test, "--->", remove_duplicate(test))
        # print("Problme Two:", test, '--->',
        #       remove_duplicate_more_than_nth(test))
