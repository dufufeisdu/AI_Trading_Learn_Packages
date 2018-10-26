from tree import Tree


class SumRootTree():
    def __init__(self):
        self.tree = None
        self.result = []

    def __call__(self, tree):
        self.tree = tree
        self.find_sum_root(self.tree, 0)
        print(self.result)
        return sum(self.result)

    def find_sum_root(self, root, sum_value):
        if not root:
            return
        if not root.left and not root.right:
            sum_value *= 10
            sum_value += root.value
            self.result.append(sum_value)
            return
        else:
            sum_value *= 10
            sum_value += root.value
            self.find_sum_root(root.left, sum_value)
            self.find_sum_root(root.right, sum_value)


if __name__ == '__main__':
    root = Tree(2)
    root.left = Tree(3)
    root.right = Tree(4)
    root.left.left = Tree(5)
    root.left.right = Tree(6)
    root.right.right = Tree(8)
    root.right.right.right = Tree(9)
    root.right.right.right.right = Tree(9)
    clss = SumRootTree()
    print(clss(root))
