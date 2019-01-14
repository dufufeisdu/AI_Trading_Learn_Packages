# Incorrect
def median_of_sorted_array(one, two):
    one_start = 0
    two_start = 0
    one_end = len(one) - 1
    two_end = len(two) - 1
    one_mid = one_end // 2
    two_mid = two_end // 2
    while not(one_start == one_end and one_end == one_mid and two_start == two_end and two_mid == two_end):
        if one[one_mid] < two[two_mid]:
            if (one_end - one_start + 1) % 2 == 1:
                one_start = one_mid
            else:
                one_start = one_mid + 1
            one_mid = (one_start + one_end) // 2
            two_end = two_mid
            two_mid = (two_mid + two_start) // 2
        elif two[two_mid] < one[one_mid]:
            if (two_end - two_start + 1) % 2 == 1:
                two_start = two_mid
            else:
                two_start = two_mid + 1
            two_mid = (two_start + two_end) // 2
            one_end = one_mid
            one_mid = (one_start + one_end) // 2
        else:
            return one[one_mid]
    if one[one_mid] < two[two_mid]:
        return one[one_mid]
    else:
        return two[two_mid]


if __name__ == "__main__":
    tests = [[[1, 3, 7], [2, 4, 5, 6, 8, 9]], [
        [2, 4, 5, 6, 8, 9], [1, 3, 7]], [[1, 3, 5, 7, 8], [2, 4, 6, 8]], [[1, 5], [3, 7]]]
    for test in tests:
        print(test, '--->', median_of_sorted_array(*test))
