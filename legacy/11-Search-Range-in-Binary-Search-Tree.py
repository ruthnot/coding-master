"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        result = []
        self.travel(root, k1, k2, result)
        return result

    def travel(self, root, k1, k2, result):
        if not root:
            return
        if k1 < root.val:
            self.travel(root.left, k1, k2, result)
        if k1 <= root.val <= k2:
            result.append(root.val)
        if root.val < k2:
            self.travel(root.right, k1, k2, result)


class Solution2:  # not optimal, need sorted function at the end
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """

    def searchRange(self, root, k1, k2):
        # write your code here
        res = []
        if not root:
            return res
        if k1 <= root.val <= k2:
            res.append(root.val)
            res += self.searchRange(root.left, k1, root.val)
            res += self.searchRange(root.right, root.val, k2)
        elif root.val < k1:
            res += self.searchRange(root.right, k1, k2)
        else:
            res += self.searchRange(root.left, k1, k2)
        return sorted(res)





if __name__ == '__main__':
    a = [1, 4, 3]
    b = [4, 1, 4]
    print(a + [])


