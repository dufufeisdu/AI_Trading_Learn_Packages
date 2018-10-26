from tree import Tree
from preorder_tree import preorder_tree


def flat_tree(tree):
    stk = []
    p = tree
    while p.left:
        if p.right:
            stk.append(p.right)
            p.right = None
        p = p.left
    while stk:
        right = stk.pop()
        p.left = flat_tree(right)

        while p.left:
            p = p.left

    return tree


def flat_tree_rec(tree):
    if tree == None:
        return
    flat_tree_rec(tree.left)
    flat_tree_rec(tree.right)

    q = tree.right
    p = tree.left
    tree.right = p
    p = tree
    while p.right:
        p = p.right
    p.right = q


def flat_tree_ite(tree):
    stk = [tree]
    p = tree
    while stk:
        p = stk.pop()
        if p.right:
            stk.append(p.right)
        if p.left:
            stk.append(p.left)
            p.right = None


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
    tests = [root1]
    for t in tests:
        flat_tree_rec(t)
        p = t
        while p:
            print(p.value)
            p = p.right
