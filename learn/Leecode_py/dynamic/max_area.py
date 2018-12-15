

# this is an INCORRECT solution!!

# from copy import deepcopy


# def max_area(arr):
#     area = 0

#     wraped_arr = deepcopy(arr)
#     header = [0 for i in range(len(wraped_arr) + 1)]
#     wraped_arr = [[0] + ele for ele in wraped_arr]
#     wraped_arr = [header] + wraped_arr
#     print(wraped_arr)
#     for i in range(1, len(wraped_arr)):
#         for j in range(1, len(wraped_arr)):
#             if wraped_arr[i][j] == 1:
#                 wraped_arr[i][j] += max(wraped_arr[i - 1]
#                                         [j], wraped_arr[i][j - 1])
#                 area = max(area, wraped_arr[i][j])
#     return area


# correct:
# L will record the left most consecutive start index
# R will record the right most consecutive end index
# H will record the height of the most consecutive 1 from the top
# this three matrix contain everthing needed to compute the max area of the rectangle
def max_area(arr):
    if not arr:
        return 0

    m = len(arr)
    n = len(arr[0])
    H = [0] * n
    L = [0] * n
    R = [n] * n
    ret = 0
    for i in range(m):
        left = 0
        right = n
        for j in range(n):
            if arr[i][j] == 1:
                H[j] += 1
                L[j] = max(L[j], left)
            else:
                left = j + 1
                H[j] = 0
                L[j] = 0
                R[j] = n
        for k in range(n - 1, -1, -1):
            if arr[i][k] == 1:
                R[k] = min(R[k], right)
                ret = max(ret, H[k] * (R[k] - L[k]))
            else:
                right = k
    return ret


def max_area_mine(arr):
    if not arr:
        return 0

    m = len(arr)
    n = len(arr[0])
    H = [0] * n
    L = [0] * n
    R = [n] * n
    ret = 0
    for i in range(m):
        left = 0
        right = n
        for j in range(n):
            if arr[i][j] == 1:
                H[j] += 1
                L[j] = left
            else:
                H[j] = 0
                L[j] = 0
                R[j] = n
                left = j + 1
        for k in range(n - 1, -1, -1):
            if arr[i][k] == 1:
                R[k] = right
                ret = max(ret, H[k] * (R[k] - L[k]))
            else:
                right = k + 1
    return ret


if __name__ == "__main__":
    test = [[1, 0, 1, 1, 1],
            # [1, 0, 1, 1, 0],
            # [1, 0, 1, 1, 1],
            # [1, 0, 1, 1, 0],
            # [0, 0, 0, 1, 0]
            ]
    print(max_area(test))
