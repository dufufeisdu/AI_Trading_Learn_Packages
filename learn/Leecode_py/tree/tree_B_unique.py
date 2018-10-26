from tree import Tree


class tree_B_unique():
    cache = {0: 1, 1: 1
             }

    def __init__(self, number):

        self.n = number

    def caculate_n(self, n):
        if n in tree_B_unique.cache:
            return tree_B_unique.cache[n]

        sum = 0
        for i in range(n):
            sum += self.caculate_n(
                i) * self.caculate_n(n - i - 1)
        tree_B_unique.cache[n] = sum
        return tree_B_unique.cache[n]

    def __repr__(self):
        return str(self.cache[self.n])


if __name__ == '__main__':
    tests = [0, 1, 2, 3, 4, 5, 6, 6, 7, 8]

    for t in tests:
        tree_num = tree_B_unique(t)
        tree_num.caculate_n(tree_num.n)
        print(t, '=', tree_num)
