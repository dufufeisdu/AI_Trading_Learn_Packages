from tree import Tree


def tree_travese_zg_level(tree):
    if tree:
        que = [tree]
    result = []
    order = False
    while que:
        que2 = []
        result.append([])
        while que:
            p = que.pop()
            result[-1].append(p.value)
            if p.left:
                que2.insert(0, p.left)
            if p.right:
                que2.insert(0, p.right)
        if order:
            result[-1].reverse()
        order = not order
        que = que2
    return result


if __name__ == '__main__':
    root = Tree(2)
    root.left = Tree(3)
    root.right = Tree(4)
    root.left.left = Tree(5)
    root.left.right = Tree(6)
    root.right.right = Tree(8)
    tests = [root]
    for t in tests:
        print(t, '\'s preorder is: ', tree_travese_zg_level(t))
