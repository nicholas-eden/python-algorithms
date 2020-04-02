# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_symmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self.are_symmetric(root.left, root.right)

    def are_symmetric(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None or right is None:
            return left == right

        if left.val != right.val:
            return False

        return self.are_symmetric(left.left, right.right) and self.are_symmetric(left.right, right.left)
