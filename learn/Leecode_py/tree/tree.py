import math


class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return "Tree with root " + str(self.value)


def init_tree_from_ls(ls):
    depth = math.ceil(math.log(len(ls)))
    if ls:
        root = Tree(ls[0])
        que = [root]
    for i in range(depth):
        for value in ls[2**i:2**(i + 1) + 1]:
            for q in que:
                pass

    return root


def test_function(func):
    root = Tree(2)
    root.left = Tree(3)
    root.right = Tree(4)
    root.left.left = Tree(5)
    root.left.right = Tree(6)
    root.right.right = Tree(8)
    root.right.right.right = Tree(9)
    root.right.right.right.right = Tree(10)
    print(func(root))


def test_class(clss):
    c = clss()
