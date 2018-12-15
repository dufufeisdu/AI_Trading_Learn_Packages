# times of insert opration is the len(str1)-len(str2),
# and you can insert everythin, which is trivial
# delete/replace is the key ,by using brutal force, T will be (m*n)


def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    if m == 0 or n == 0:
        return abs(m - n)
    if m < n:
