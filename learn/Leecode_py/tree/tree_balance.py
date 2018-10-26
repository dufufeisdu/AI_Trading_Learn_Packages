from tree import Tree


def is_tree_balance(tree):
    isbalance, height = height_and_balance(tree)
    return isbalance


def height_and_balance(tree):
    if tree is None:
        return True, 0
    is_left_balance, left_height = height_and_balance(tree.left)
    is_right_balance, right_height = height_and_balance(tree.right)
    if not is_left_balance or not is_right_balance:
        return False, left_height
    else:
        if abs(left_height - right_height) <= 1:
            if left_height > right_height:
                return True, left_height + 1
            else:
                return True, right_height + 1
        else:
            return False, left_height


if __name__ == '__main__':
    root = Tree(2)
    root.left = Tree(3)
    root.right = Tree(4)
    root.left.left = Tree(5)
    root.left.right = Tree(6)
    root.right.right = Tree(8)
    root.right.right.right = Tree(9)
    root.right.right.right.right = Tree(10)
    tests = [root]
    for t in tests:
        print(t, '\'s balance is: ', is_tree_balance(t))
