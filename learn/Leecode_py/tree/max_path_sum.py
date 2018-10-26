from tree import *


def max_path_sum(root):
    if not root:
        return 0, 0
    else:
        left_one_most, left_all = max_path_sum(root.left)
        right_one_most, right_all = max_path_sum(root.right)

        all = max(left_one_most + right_one_most +
                  root.value, left_all, right_all)
        # if all < 0:
        #     all = root.value

        one_path = max(left_one_most + root.vlaue, right_one_most + root.value)

        return one_path, all
