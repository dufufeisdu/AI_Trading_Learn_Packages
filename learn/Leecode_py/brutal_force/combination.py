

def combination(n, k):
    return wraper(list(range(n)), k)


def wraper(ls, k):
    if k == 0:
        return [[]]
    result = []
    for i in range(len(ls)):
        res = [ls[i:i + 1] + comb for comb in wraper(ls[(i + 1):], k - 1)]
        result = result + res
    return result


def swap(ls, i, j):
    a = ls[i]
    ls[i] = ls[j]
    ls[j] = a


if __name__ == '__main__':

    print(combination(5, 2))
