"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import collections


class Solution:  # 使用单队列
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        queue = collections.deque([root])
        while queue:
            res.append([node.val for node in queue])
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res


class Solution2: # 使用双队列
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            res.append([node.val for node in queue])
            next_queue = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
        return res

class Solution3: # Dummy node
    def levelOrder(self, root):
        if not root:
            return []
        queue = collections.deque([root, None])
        res, level = [], []
        while queue:
            node = queue.popleft()
            if node is None:
                res.append(level)
                level = []
                if queue:
                    queue.append(None)
                continue
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res


if __name__=='__main__':
    _ = Solution3()


