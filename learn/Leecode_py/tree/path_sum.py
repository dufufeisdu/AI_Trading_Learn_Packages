from tree import Tree


def path_sum(tree, number):
    if not tree:
        return False
    if not tree.left and not tree.right:
        return number == tree.value
    else:
        return path_sum(tree.left, number - tree.value) or path_sum(tree.right, number - tree.value)


class path_sumII:
    def __init__(self):
        self.result = []

    def __call__(self, sum, tree):
        self.sum = sum
        self.path = []
        self.find_path(sum, tree, self.path)
        return self.result

    def find_path(self, sum, tree, path):
        if not tree:
            return
        path.append(tree)
        if not tree.left and not tree.right:
            if tree.value == sum:
                self.result.append(path)
                return

        if tree.left:
            self.find_path(sum, tree.left, path)

        if tree.right:
            self.find_path(sum, tree.right, path)
        del path[-1]
