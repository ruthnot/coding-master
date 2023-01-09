"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        # write your code here
        if not root:
            return
        self.result = None
        node_set = set()
        self.inorder(root, n, node_set)
        return self.result

    def inorder(self, root, n, node_set):
        if not root:
            return
        self.inorder(root.left, n, node_set)
        if root.val in node_set:
            self.result = [n - root.val, root.val]
        else:
            node_set.add(n - root.val)
        self.inorder(root.right, n, node_set)







if __name__=='__main__':
    a = [None]
    a[0] = 1
    print(a[0])