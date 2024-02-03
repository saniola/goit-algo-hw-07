from tree_node import root


def find_minimum_value(root):
    if root is None:
        return None

    while root.left is not None:
        root = root.left

    return root.value


minimum_value = find_minimum_value(root)
print("The minimum value in the tree is:", minimum_value)
