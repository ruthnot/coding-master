class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class BST:
    def searchBST(self, root, val):
        if not root:
            return None  # 未找到值为val的节点
        if val < root.val:
            return self.searchBST(root.left, val)  # val小于根节点值，在左子树中查找哦
        elif val > root.val:
            return self.searchBST(root.right, val)  # val大于根节点值，在右子树中查找
        else:
            return root

    def updateBST(self, root, target, val):
        if not root:
            return  # 未找到target节点
        if target < root.val:
            self.updateBST(root.left, target, val)  # target小于根节点值，在左子树中查找哦
        elif target > root.val:
            self.updateBST(root.right, target, val)  # target大于根节点值，在右子树中查找
        else:  # 找到了
            root.val = val

    def insertNode(self, root, node):
        if not root:
            return node
        if root.val > node.val:
            root.left = self.insertNode(root.left, node)
        else:
            root.right = self.insertNode(root.right, node)
        return root

    def removeNode(self, root, value):
        dummy = TreeNode(0)
        dummy.left = root
        parent = self.findNode(dummy, root, value)
        node = None
        if parent.left and parent.left.val == value:
            node = parent.left
        elif parent.right and parent.right.val == value:
            node = parent.right
        else:
            return dummy.left
        self.deleteNode(parent, node)
        return dummy.left

# Helper functions for remove Node
    def findNode(self, parent, node, value):
        if not node:
            return parent
        if node.val == value:
            return parent
        if value < node.val:
            return self.findNode(node, node.left, value)
        else:
            return self.findNode(node, node.right, value)

    def deleteNode(self, parent, node):
        if not node.right:
            if parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.left
        else:
            temp = node.right
            father = node
            while temp.left:
                father = temp
                temp = temp.left
            if father.left == temp:
                father.left = temp.right
            else:
                father.right = temp.right
            if parent.left == node:
                parent.left = temp
            else:
                parent.right = temp
            temp.left = node.left
            temp.right = node.right
