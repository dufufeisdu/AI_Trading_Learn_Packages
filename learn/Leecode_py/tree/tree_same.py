from tree import Tree


def tree_same(tree1, tree2):
    if not(tree1 or tree2):
        return True
    if not(tree1 and tree2):
        return False
    if tree1.value != tree2.value:
        return False
    return tree_same(tree1.left, tree2.left) and tree_same(tree1.right, tree2.right)


if __name__ == '__main__':
    root = Tree(2)
    root.left = Tree(3)
    root.right = Tree(4)
    root.left.left = Tree(5)
    root.left.right = Tree(6)
    root.right.right = Tree(8)

    root1 = Tree(2)
    root1.left = Tree(3)
    root1.right = Tree(4)
    root1.left.left = Tree(5)
    root1.left.right = Tree(6)
    root1.right.right = Tree(8)
    root1.right.left = Tree(7)
    tests = [[root, root]]
    for t in tests:
        print(t, '\'s preorder is: ', tree_same(*t))
