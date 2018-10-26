
from tree import Tree


def inorder_travese(tree):
    result = []
    stk = []
    if tree is None:
        return stk
    if not isinstance(tree, Tree):
        raise Exception("Invaild tree")
    p = tree
    while stk or p:
        if p:
            stk.append(p)
            p = p.left
        else:
            p = stk[-1]
            result.append(p.value)
            stk.pop()
            p = p.right
    return result


if __name__ == '__main__':
    root = Tree(2)
    root.left = Tree(3)
    root.right = Tree(4)
    root.left.left = Tree(5)
    root.left.right = Tree(6)
    tests = [root]
    for t in tests:
        print(t, '\'s preorder is: ', inorder_travese(t))
