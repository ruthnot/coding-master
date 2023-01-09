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
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        self.average = float('-inf')
        self.node = None
        self.dfs(root)
        return self.node

    def dfs(self, node):
        if not node:
            return 0, 0
        left_sum, left_size = self.dfs(node.left)
        right_sum, right_size = self.dfs(node.right)
        node_sum = left_sum + right_sum + node.val
        node_size = left_size + right_size + 1
        if node_sum / node_size > self.average:
            self.average = node_sum / node_size
            self.node = node
        return node_sum, node_size


if __name__ == '__main__':
    a = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16]
    b = [-2,-4,-5,-8,-9,-10,-11,-16]
    res1 = sum(a) / len(a)
    res2 = sum(b) / len(b)
    print(1 / 3)

