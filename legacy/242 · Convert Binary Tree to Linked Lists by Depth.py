"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
from collections import deque
class Solution:  #BFS
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        if not root:
            return []
        linked_list = []
        queue = deque([root])
        while queue:
            dummy = ListNode(None)
            curr = dummy
            for _ in range(len(queue)):
                node = queue.popleft()
                curr.next = ListNode(node.val)
                curr = curr.next
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            linked_list.append(dummy.next)
        return linked_list

class Solution2:  # Should have better solution
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        hashset = {}
        self.dfs(root, 0, hashset)
        return self.output(hashset)

    def dfs(self, root, level, hashset):
        if not root:
            return
        if level not in hashset:
            hashset[level] = []
        hashset[level].append(ListNode(root.val))
        self.dfs(root.left, level + 1, hashset)
        self.dfs(root.right, level + 1, hashset)

    def output(self, hashset):
        results = []
        for level, node_list in hashset.items():
            for i in range(len(node_list) - 1):
                node_list[i].next = node_list[i + 1]
            results.append(node_list[0])
        return results

