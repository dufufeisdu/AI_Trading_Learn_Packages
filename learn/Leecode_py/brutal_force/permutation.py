

def permutation(ls):
    if len(ls) == 0:
        return []
    if len(ls) == 1:
        return [ls]
    result = []
    for i in range(0, len(ls)):
        swap(ls, i, 0)
        prev = ls[0:1]
        result += [prev + i for i in permutation(ls[1:])]
        swap(ls, i, 0)
    return result


def swap(ls, i, j):
    a = ls[i]
    ls[i] = ls[j]
    ls[j] = a


if __name__ == '__main__':
    A = [1, 2, 3]

    print(permutation(A))
