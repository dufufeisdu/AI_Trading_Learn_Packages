def two_sum(arr, target):
    hash_table = {ele: idx for ele, idx in enumerate(arr)}
    for idx, ele in enumerate(arr):
        if target - ele in hash_table:
            return idx, hash_table[target - ele]
    return None


def three_sum(arr):
    hash_table = {}
    all_arr = []
    for ele in arr:
        if ele in hash_table:
            hash_table[ele] += 1
        else:
            hash_table[ele] = 1
    for ele in arr:
        if hash_table[ele] == 0:
            continue
        hash_table[ele] -= 1
        target = -ele

        for element in hash_table:
            if hash_table[element] > 0:
                hash_table[element] -= 1
                if target - element in hash_table and hash_table[target - element] != 0:
                    one_solution = tuple(
                        sorted([ele, element, target - element]))
                    all_arr.append(one_solution)
        hash_table[ele] = 0

    return all_arr


def three_sum_closest(arr, target):
    """1 sort the array
       2 for each element except for itself,
       go through the sorted array from the start and the end,
       find the sum of two element closest to 0
    """
    length = len(arr)
    if length < 3:
        return None
    arr = sorted(arr)
    res = [arr[0], arr[1], arr[2]]
    closest = abs(arr[0] + arr[1] + arr[2] - target)

    for idx, one in enumerate(arr[:length // 2]):
        start = 0
        end = len(arr) - 1
        while start != end:
            if start == idx:
                start += 1
                continue
            else:
                gap = one + arr[start] + arr[end] - target
                if abs(gap) < closest:
                    closest = abs(gap)
                    res = [one, arr[start], arr[end]]
                if gap > 0:
                    end -= 1
                elif gap == 0:
                    return [one, arr[start], arr[end]]
                else:
                    start += 1
    return res


if __name__ == "__main__":
    tests = [[-1, 0, 1, 2, -1, 4], [1, 1, -2], [-1, 2, 1, -4]]
    for test in tests:
        print(test, '--->', three_sum(test))

    for test in tests:
        print(test, '--->', three_sum_closest(test, 1))
