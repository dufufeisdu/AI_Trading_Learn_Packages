

def permutation_sqe(n):
    if n <= 0:
        return []
    if n == 1:
        return ['1']
    nth_permutation = []
    for ele in permutation_sqe(n - 1):
        squence = list(ele)
        nth_element = []
        for j in range(n):
            nth_element = squence[0:j] + [str(n)] + squence[j:]
            nth_element = ''.join(nth_element)
            nth_permutation.append(nth_element)

    return nth_permutation


if __name__ == "__main__":
    for n in range(6):
        print(n, '---->', permutation_sqe(n))
