from tree import Tree


class Next_tree(Tree):
    def __init__(self, value):
        super().__init__(value)
        self.next = None

# key point is how to find the next silbling when they don't have common parent
# And should use the condition that it is a complete tree
# another key point is constant space


def tree_next_right(root):
    root.next = None

    return root
