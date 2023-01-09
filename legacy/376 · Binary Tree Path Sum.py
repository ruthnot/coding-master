"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum(self, root, target):
        # write your code here
        if not root:
            return []
        results = []
        self.dfs(root, target, [], results)
        return results

    def dfs(self, root, target, result, results):
        if not root:
            return
        result.append(root.val)
        if not root.left and not root.right:
            if sum(result) == target:
                results.append(list(result))
            result.pop()
            return

        self.dfs(root.left, target, result, results)
        self.dfs(root.right, target, result, results)
        result.pop()

