

def subset(ls, path, step, result):
    if step == len(ls):
        result.append(path)
        return
    subset(ls, path, step + 1, result)
    path.append(ls[step])
    subset(ls, path, step + 1, result)
    path.pop()


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    result = []
    path = []
    subset(A, path, 0, result)
    print(result)
