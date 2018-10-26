
def merge_sorted(A, B):
    ia = len(A)
    ib = len(B)
    A = A + B
    for i in range(ia + ib - 1, -1, -1):

        if ia < 1 or ib < 1:
            break
        if A[ia - 1] > B[ib - 1]:
            A[i] = A[ia - 1]
            ia -= 1
        else:
            A[i] = B[ib - 1]
            ib -= 1
    if ia < 0:
        A = B[0:ib] + A[ib - 1:]

    return A


if __name__ == '__main__':
    A = [1, 3, 5, 6, 12]
    B = [2, 3, 4, 7, 10]
    print(merge_sorted(A, B))
