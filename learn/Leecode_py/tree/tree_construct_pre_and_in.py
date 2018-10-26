from tree import Tree


def construct_tree_from_pre_and_in(pre_order, in_order):
    if not pre_order:
        return None
    root = Tree(pre_order[0])
    index = in_order.index(pre_order[0])

    left_in_order = in_order[:index]
    right_in_order = in_order[index + 1:]
    left_pre_order = pre_order[1:len(left_in_order) + 1]
    right_pre_order = pre_order[len(left_in_order) + 1:]

    root.left = construct_tree_from_pre_and_in(left_pre_order, left_in_order)
    root.right = construct_tree_from_pre_and_in(
        right_pre_order, right_in_order)
    return root
