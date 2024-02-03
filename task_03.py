from tree_node import root


def find_sum_of_values(root):
    if root is None:
        return 0

    left_sum = find_sum_of_values(root.left)

    right_sum = find_sum_of_values(root.right)

    return root.value + left_sum + right_sum


total_sum = find_sum_of_values(root)
print("The sum of all values in the tree is:", total_sum)
