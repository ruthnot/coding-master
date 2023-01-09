"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        self.min_sum = float('inf')
        self.min_node = None
        self.find_tree_sum(root)
        return self.min_node

    def find_tree_sum(self, root):
        if not root:
            return 0

        left_sum = self.find_tree_sum(root.left)
        right_sum = self.find_tree_sum(root.right)
        root_sum = left_sum + right_sum + root.val
        if root_sum < self.min_sum:
            self.min_node = root
            self.min_sum = root_sum
        return root_sum