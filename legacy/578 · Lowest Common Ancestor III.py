"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """

    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        a, b, lca = self.dfs(root, A, B)
        return lca if a and b else None

    def dfs(self, root, A, B):
        if not root:
            return False, False, None

        l_a, l_b, l_lca = self.dfs(root.left, A, B)
        r_a, r_b, r_lca = self.dfs(root.right, A, B)

        curr_a = l_a or r_a
        curr_b = l_b or r_b
        if root == A:
            return True, curr_b, root
        if root == B:
            return curr_a, True, root
        if l_lca and r_lca:
            return curr_a, curr_b, root
        if l_lca:
            return curr_a, curr_b, l_lca
        if r_lca:
            return curr_a, curr_b, r_lca
        return curr_a, curr_b, None
