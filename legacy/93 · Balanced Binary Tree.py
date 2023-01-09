from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def is_balanced(self, root: TreeNode) -> bool:
        # write your code here

        depth, res = self.dfs(root)
        return res

    def dfs(self, root):
        if not root:
            return 0, True
        left_depth, left_res = self.dfs(root.left)
        right_depth, right_res = self.dfs(root.right)
        if not (left_res and right_res):
            return None, False
        if abs(left_depth - right_depth) > 1:
            return None, False
        return max(left_depth, right_depth) + 1, True



