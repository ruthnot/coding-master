class Solution:  #遍历法
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        path, paths = [root], []
        self.findPaths(root, path, paths)
        return paths

    def findPaths(self, node, path, paths):
        if not node:
            return
        if not node.left and not node.right:
            paths.append('->'.join([str(n.val) for n in path]))
            return

        path.append(node.left)
        self.findPaths(node.left, path, paths)
        path.pop()

        path.append(node.right)
        self.findPaths(node.right, path, paths)
        path.pop()


class Solution2:  #分治法
    def binaryTreePaths(self, root):
        paths = []
        if not root:
            return paths
        if not root.left and not root.right:
            return [str(root.val)]

        for path in self.binaryTreePaths(root.left):
            paths.append(str(root.val) + "->" + path)
        for path in self.binaryTreePaths(root.right):
            paths.append(str(root.val) + "->" + path)

        return paths



