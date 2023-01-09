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
    @param target: An integer
    @return: all valid paths
             we will sort your return value in output
    """
    # 每个节点可以选择跳过，或加入path。
    # 如果选择加入path，接下来的所有子节点不能跳过 （当红不能有gap）
    # 有可能有负值节点，所以要走完整棵树

    def binary_tree_path_sum2(self, root: TreeNode, target: int) -> List[List[int]]:
        # write your code here
        result = []
        self.dfs_skip_curr(root, target, [], result)
        return result

    def dfs_skip_curr(self, root, target, path, result):
        if not root:
            return
        self.dfs_add_curr(root, target, path, result)
        self.dfs_skip_curr(root.left, target, path, result)
        self.dfs_skip_curr(root.right, target, path, result)

    def dfs_add_curr(self, root, target, path, result):
        if not root:
            return
        path.append(root.val)
        if sum(path) == target:
            result.append(path[:])
        self.dfs_add_curr(root.left, target, path, result)
        self.dfs_add_curr(root.right, target, path, result)
        path.pop()
