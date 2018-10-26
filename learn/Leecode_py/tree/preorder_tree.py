
from tree import Tree


def preorder_tree(tree):
    stk = []
    result = []

    if not tree:
        return result

    if not isinstance(tree, Tree):
        raise Exception("Not a Tree")
    stk.append(tree)
    while bool(stk):
        curr = stk.pop()
        result.append(curr.value)
        if curr.right is not None:
            stk.append(curr.right)
        if curr.left is not None:
            stk.append(curr.left)

    return result


if __name__ == '__main__':
    root = Tree(2)
    root.left = Tree(3)
    root.right = Tree(4)
    root.left.left = Tree(5)
    root.left.right = Tree(6)
    tests = [root]
    for t in tests:
        print(t, '\'s preorder is: ', preorder_tree(t))
