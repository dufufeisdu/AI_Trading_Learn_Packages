def spril_matrix(m):
    if not m:
        return m
    row = len(m)
    col = len(m[0])
    start = []
    start_row = 0
    end_row = row
    start_col = 0
    end_col = col
    while True:

        for i in range(start_col, end_col):
            start.append(m[start_row][i])
        start_row += 1
        if start_col > end_col:
            break

        for i in range(start_row, end_row):
            start.append(m[i][end_col - 1])
        end_col -= 1

        for i in range(end_col - 1, start_col - 1, -1):
            start.append(m[end_row - 1][i])
        end_row -= 1

        for i in range(end_row - 1, start_row - 1, -1):
            start.append(m[i][start_col])
        start_col += 1

    return start


if __name__ == "__main__":
    tests = [
        [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20]],

        [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]]
    ]
    for test in tests:
        print(spril_matrix(test))
