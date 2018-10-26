def find_largest_hist_area(arr):

    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 0:
        return 0
    else:
        m = min(arr)
        i = arr.index(m)
        area = m * len(arr)
        tu = [area, find_largest_hist_area(
            arr[0:i]), find_largest_hist_area(arr[i + 1:])]
        return max(tu)


if __name__ == '__main__':
    tests = [[1, 2, 1, 4, 1], [3, 4, 5]]
    for t in tests:
        print(t, ':', find_largest_hist_area(t))
