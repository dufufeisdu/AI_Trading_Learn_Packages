# from start to end of index of arr
# area = max(area,(end-start)*min(start, end))
# if start > end end--
# else: start++


def contain_water(arr):
    if len(arr) < 2:
        return 0

    start = 0
    end = len(arr) - 1
    area = 0
    while end > start:
        area = max(area, (end - start) * min(arr[start], arr[end]))
        if arr[start] > arr[end]:
            end -= 1
        else:
            start += 1
    return area


if __name__ == "__main__":
    tests = [[1, 2, 10, 10, 2, 0], [1, 0, 1, 5, 1]]
    for test in tests:
        print(contain_water(test))
