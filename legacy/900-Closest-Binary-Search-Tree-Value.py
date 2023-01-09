"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""



class Solution:  # Non-recursion
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """

    def closestValue(self, root, target):
        # write your code here

        upper = root
        lower = root
        while root:
            if root.val > target:
                upper = root
                root = root.left
            elif root.val < target:
                lower = root
                root = root.right
            else:
                return root.val

        if abs(upper.val - target) > abs(lower.val - target):
            return lower.val
        return upper.val


class Solution2:  # Recurision + Binary Search
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """

    def closestValue(self, root, target):
        # write your code here
        self.sorted_list = []
        self.dfs(root)
        res = self.binary_search(self.sorted_list, target)
        return res

    def dfs(self, root):
        if root is None:
            return

        self.dfs(root.left)
        self.sorted_list.append(root.val)
        self.dfs(root.right)


    def binary_search(self, sorted_list, target):
        start, end = 0, len(sorted_list) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if sorted_list[mid] < target:
                start = mid
            elif sorted_list[mid] >= target:
                end = mid

        start_val = sorted_list[start]
        end_val = sorted_list[end]
        return start_val if abs(start_val - target) <= abs(end_val - target) else end_val

