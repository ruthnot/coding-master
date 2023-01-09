from typing import (
    List,
)
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
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binary_tree_paths(self, root: TreeNode) -> List[str]:
        # write your code here
        results = []
        self.dfs(root, [], results)
        return results

    def dfs(self, root, result, results):
        if not root:
            return
        if not result:
            result.append(str(root.val))
        else:
            result.append("->" + str(root.val))

        if not root.left and not root.right:
            results.append("".join(result))
            result.pop()
            return

        self.dfs(root.left, result, results)
        self.dfs(root.right, result, results)
        result.pop()

