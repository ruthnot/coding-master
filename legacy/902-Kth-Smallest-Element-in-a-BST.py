"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """

    def kthSmallest(self, root, k):
        # write your code here
        self.count = 0
        self.result = None
        self.update_count(root, k)
        return self.result.val

    def update_count(self, root, k):
        if not root:
            return
        self.update_count(root.left, k)
        self.count += 1
        if self.count == k:
            self.result = root
            return
        self.update_count(root.right, k)

class Solution2:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        stack = []
        while root:
            stack.append(root)
            root = root.left

        for i in range(k - 1):
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
        return stack[-1].val


class Solution3:  # Recursion
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """

    def kthSmallest(self, root, k):
        # write your code here
        self.ordered_val = []
        self.in_order_sort(root)
        print(self.ordered_val)
        return self.ordered_val[k - 1]

    def in_order_sort(self, root):
        if root is None:
            return

        self.in_order_sort(root.left)
        self.ordered_val.append(root.val)
        self.in_order_sort(root.right)