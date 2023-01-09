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
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        return self.helper(root)[0]

    def helper(self, root):
        if not root:
            return True, -float('inf'), float('inf')

        is_left, max_left, _ = self.helper(root.left)
        is_right, _, min_right = self.helper(root.right)

        if not is_left or not is_right:
            return False, None, None
        if not max_left < root.val < min_right:
            return False, None, None

        curr_min = min(node.val for node in [root, root.left, root.right] if node)
        curr_max = max(node.val for node in [root, root.left, root.right] if node)

        return True, curr_max, curr_min


class Solution2:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        isValid, minVal, maxVal = self.dfs(root)
        return isValid

    def dfs(self, root):
        # write your code here
        if not root:
            return True, None, None  # is_valid, min, max
        isLeft, minLeft, maxLeft = self.dfs(root.left)
        isRight, minRight, maxRight = self.dfs(root.right)

        isSelf = True
        minSelf = min(val for val in [minLeft, minRight, root.val] if val is not None)
        maxSelf = max(val for val in [maxLeft, maxRight, root.val] if val is not None)

        if not (isLeft and isRight):
            isSelf = False
        if maxLeft and root.val <= maxLeft:
            isSelf = False
        if minRight and root.val >= minRight:
            isSelf = False
        return isSelf, minSelf, maxSelf



if __name__=='__main__':
    x = (None, 0, None)
    print(min(val for val in [None, 0, None] if val is not None))