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


if __name__ == "__main__":
    tests = [[-1, 0, 1, 2, -1, 4], [1, 1, -2]]
    for test in tests:
        print(test, '--->', three_sum(test))
