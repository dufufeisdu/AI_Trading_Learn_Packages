def uniqe_path(mx):
    m = len(mx)
    n = len(mx[0])
    if m > n:
        mn = n - 1
    else:
        mn = m - 1
    return select_from(mn, m + n - 1)


def select_from(a, b):
    if a == 0:
        return 1
    denom = 1
    nume = 1
    for i in range(b, b - a, -1):
        nume *= i
    for j in range(a, 0, -1):
        denom *= j
    return int(denom / nume)


# def uniqe_path_II(mx):
