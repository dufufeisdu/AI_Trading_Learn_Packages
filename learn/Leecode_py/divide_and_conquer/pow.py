def pow_dc(num, times):

    if times == 1:
        return num
    if times == 0:
        return 1
    (result, reminder) = divmod(times, 2)
    res = pow_dc(num, result)

    return res * res * pow_dc(num, reminder)


if __name__ == "__main__":
    tests = [[1, 0], [2, 10], [10, 1], [10, 3], [10, 5]]
    for test in tests:
        print(pow_dc(*test))
