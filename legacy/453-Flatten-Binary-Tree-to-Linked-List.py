"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root: TreeNode):
        # write your code here
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            temp_right = root.right
            root.right = root.left
            root.left = None
            # find the last node of flatten left tree, and attach the previous right to it
            curr = root
            while curr.right:
                curr = curr.right
            curr.right = temp_right


class Solution2:  # Official Answer
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    def flatten(self, root):
        # write your code here
        self.flatten_and_return_last_node(root)

    def flatten_and_return_last_node(self, root):
        if root is None:
            return None

        left_last = self.flatten_and_return_last_node(root.left)
        right_last = self.flatten_and_return_last_node(root.right)

        if left_last is not None:
            left_last.right = root.right
            root.right = root.left
            root.left = None

        return right_last or left_last or root


