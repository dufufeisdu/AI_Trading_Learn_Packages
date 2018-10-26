from tree import Tree


def level_order_traveseI(tree):
    if tree:
        que = [tree]
    result = []
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
        que = que2
    return result


def level_order_traveseII(tree):
    """bottom up, from leaf to root"""
    result = level_order_traveseI(tree)
    result.reverse()
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
        print(t, '\'s preorder is: ', level_order_traveseII(t))
