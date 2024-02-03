from tree_node import root


def find_largest_value(root):
    if root is None:
        return None

    largest = find_largest_value(root.right)

    if largest is None or root.value > largest:
        largest = root.value

    left_largest = find_largest_value(root.left)

    if left_largest is not None and left_largest > largest:
        largest = left_largest

    return largest


largest_value = find_largest_value(root)
print("The largest value in the tree is:", largest_value)
