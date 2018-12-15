

# Find the edge of paths
# start from the edge caculate the next path value
from copy import deepcopy


def shortest_path(arr):
    m = len(arr)
    if m == 0:
        return 0
    n = len(arr[0])
    if n == 0:
        return 0

    path = deepcopy(arr)

    for i in range(1, n):
        path[0][i] += path[0][i - 1]

    for i in range(1, m):
        path[i][0] += path[i - 1][0]

    for i in range(1, m):
        for j in range(1, n):
            path[i][j] += min(path[i - 1][j], path[i][j - 1])
    return path[m - 1][n - 1]


if __name__ == "__main__":
    test = [[1, 2, 3, 4, 5],
            [2, 1, 3, 4, 5],
            [3, 2, 1, 4, 5],
            [4, 3, 2, 1, 5],
            [5, 4, 3, 2, 1]]
    print(shortest_path(test))
