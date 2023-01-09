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
from collections import deque
class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def min_depth(self, root: TreeNode) -> int:
        # write your code here
        if not root:
            return 0
        queue = deque([root])
        depth = 0
        while queue:
            depth += 1
            for i in range(len(queue)):
                node = queue.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

