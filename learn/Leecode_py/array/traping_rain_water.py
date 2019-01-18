def traping_rain_water(arr):
    """For each pillar with height h, the amount of water it can
    contain is determined by the hightest pillar in
    its left a and hightest pillar in its right b.
    amount=min(a,b)- h,  amount = max(0,amount)
    """
    max_left = [0]
    max_right = [0]
    traped_water = 0
    for ele in arr:
        if max_left[-1] < ele:
            max_left.append(ele)
        else:
            max_left.append(max_left[-1])
    for ele in arr[::-1]:
        if max_right[0] < ele:
            max_right = [ele] + max_right
        else:
            max_right = [max_right[0]] + max_right

    for idx, ele in enumerate(arr):
        ele_water = min(max_left[idx], max_right[idx + 1]) - ele

        if ele_water > 0:
            traped_water += ele_water
    return traped_water


if __name__ == "__main__":
    tests = [[1, 2], [2, 1, 2], [0, 0], [1, 2, 3, 4], [4, 3, 2, 1],
             [4, 3, 0, 1], [2, 0, 0, 2], [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]]
    for test in tests:
        print(test, '---->', traping_rain_water(test))
