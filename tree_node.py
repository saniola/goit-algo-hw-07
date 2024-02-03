class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# OUR TREE
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(18)
