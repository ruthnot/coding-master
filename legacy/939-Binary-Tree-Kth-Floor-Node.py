class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

from collections import deque
class Solution:
    """
    @param root: the root node
    @param k: an integer
    @return: the number of nodes in the k-th layer of the binary tree
    """
    def kthfloorNode(self, root, k):
        # Write your code here
        if not root:
            return 0
        depth = 0
        queue = deque([root])
        while queue:
            depth += 1
            if depth >= k:
                return len(queue)
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return -1




