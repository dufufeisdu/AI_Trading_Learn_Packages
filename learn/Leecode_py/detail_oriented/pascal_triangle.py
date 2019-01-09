def pascal_triangle(n):
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    start = [[1], [1, 1]]
    for i in range(2, n):
        current = [1]
        for ele_index in range(1, i):
            prev = start[-1]
            current = current + [prev[ele_index] + prev[ele_index - 1]]
        current = current + [1]
        start = start + [current]
    return start


if __name__ == "__main__":
    tests = [1, 2, 3, 4, 10]
    for test in tests:
        print(pascal_triangle(test))
