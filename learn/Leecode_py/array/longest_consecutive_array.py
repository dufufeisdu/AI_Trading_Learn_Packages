# O(n)
def longest_consecutive_array(arr):
    if not arr:
        return 0
    hash_table = {ele: 1 for ele in arr}
    max_len = 1
    for element in arr:
        ele = element
        while ele - 1 in hash_table:
            if hash_table[ele - 1] != 1:
                break
            hash_table[element] += 1
            ele -= 1
        ele = element
        while ele + 1 in hash_table:
            if hash_table[ele + 1] != 1:
                break
            hash_table[element] += 1
            ele += 1
        max_len = max(max_len, hash_table[element])
    return max_len


if __name__ == "__main__":
    tests = [[2, 3, 1, 4], [4, 3, 2, 1], [
        1, 3, 2, 4], [], [1, 5, 2, 6, 7, 9], [1, 5, 2, 3, 6, 2, 7, 9, 4, 8]]
    for test in tests:
        print(test, '--->', longest_consecutive_array(test))
