

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.traverse(root, 0)

    def traverse(self, node: TreeNode, depth: int) -> int:
        if node is None:
            return depth

        return max(self.traverse(node.left, depth + 1), self.traverse(node.right, depth + 1))
