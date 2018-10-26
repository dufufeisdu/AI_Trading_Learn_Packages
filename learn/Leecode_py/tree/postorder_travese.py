
from tree import Tree


def postorder_travese(tree):
    stk = []
    result = []

    if not tree:
        return result

    if not isinstance(tree, Tree):
        raise Exception("Not a Tree")
    p = tree
    while True:
        while p:
            stk.append(p)
            p = p.left
        q = None
        while stk:
            p = stk.pop()
            if p.right == q:
                result.append(p.value)
                q = p
            else:
                stk.append(p)
                p = p.right
                break
        if not stk:
            break
    return result


if __name__ == '__main__':
    root = Tree(2)
    root.left = Tree(3)
    root.right = Tree(4)
    root.left.left = Tree(5)
    root.left.right = Tree(6)
    tests = [root]
    for t in tests:
        print(t, '\'s preorder is: ', postorder_travese(t))
