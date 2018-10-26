from tree import Tree


def BST_vaild(bst):

    if not bst:
        return True
    left_valid = True
    right_valid = True
    if bst.left:
        left_valid = bst.value > bst.left.value
    if bst.right:
        right_valid = bst.value < bst.right.value
    return left_valid and right_valid and BST_vaild(bst.left) and BST_vaild(bst.right)
