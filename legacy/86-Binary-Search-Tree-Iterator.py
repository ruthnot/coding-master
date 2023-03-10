
class BSTIterator:
    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        while root is not None:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        return len(self.stack) > 0

    def _next(self):
        node = self.stack[-1]
        if node.right is not None:
            n = node.right
            while n is not None:
                self.stack.append(n)
                n = n.left
        else:
            n = self.stack.pop()
            while self.stack and self.stack[-1].right == n:
                n = self.stack.pop()
        return node
