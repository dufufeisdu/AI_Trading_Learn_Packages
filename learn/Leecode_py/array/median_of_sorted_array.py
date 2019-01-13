def median_of_sorted_array(arr_a, arr_b):
    a = 0
    b = 0
    e = len(arr_a) - 1
    f = len(arr_b) - 1
    c = e // 2
    d = f // 2
    while not(a == e and e == c and b == f and d == f):
        if arr_a[c] < arr_b[d]:
            a = c
            c = (c + e) // 2
            f = d
            d = (d + b) // 2
        elif arr_a[c] > arr_b[d]:
            e = c
            c = (a + c) // 2
            b = d
            d = (d + f) // 2
        else:
            return arr_a[c]
    if arr_a[c] < arr_b[d]:
        return arr_a[c]
    else:
        return arr_b[d]
