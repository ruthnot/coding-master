Difficulty: Medium

Tags: DFS

Need Review: False

Date Added: 2023-09-24

[LintCode: 596 · Minimum Subtree](https://www.lintcode.com/problem/596/?_from=collection&fromId=161)

## Description 

Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.

Notice
LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.

Example

Given a binary tree:

     1
   /   \
 -5     2
 / \   /  \
0   2 -4  -5

return the node1.

## Solution 
 ```python 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.min_node = None
        self.min_sum = float('inf')
        
    def min_sub_tree(self, root):
        self.dfs(root)
        return self.min_node
    
    def dfs(self, node):
        if node is None:
            return 0
        l_sum = self.dfs(node.left)
        r_sum = self.dfs(node.right)
        curr_sum = node.val + l_sum + r_sum
        if curr_sum < self.min_sum:
            self.min_node = node
            self.min_sum = curr_sum
        return curr_sum

n1 = TreeNode(1)
n2 = TreeNode(-5)
n3 = TreeNode(2)
n4 = TreeNode(0)
n5 = TreeNode(2)
n6 = TreeNode(-4)
n7 = TreeNode(-5)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

x = Solution()
ans = x.min_sub_tree(n1)
print(ans.val)
 ``` 
## Notes
