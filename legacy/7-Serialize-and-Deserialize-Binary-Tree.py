class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        if root is None:
            return "{}"
        queue = [root]
        index = 0
        while index < len(queue):
            if queue[index] is not None:
                queue.append(queue[index].left)
                queue.append(queue[index].right)
            index += 1
        while queue[-1] is None:
            queue.pop()

        return '{%s}' % ','.join([str(node.val) if node is not None else '#' for node in queue])


    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        data = data.strip('\n')
        if data == '{}':
            return None
        vals = data[1:-1].split(',')

        root = TreeNode(int(vals[0]))
        queue = [root]
        isLeftChild = True
        index = 0

        for val in vals[1:]:
            if val is not '#':
                node = TreeNode(int(val))
                if isLeftChild:
                    queue[index].left = node
                else:
                    queue[index].right = node

                queue.append(node)
            if not isLeftChild:
                index += 1
            isLeftChild = not isLeftChild
        return root

if __name__ == '__main__':
    x = [1, 2, None, 3, None, 5]
    res = '{}'.format(','.join([str(val) if val is not None else '#' for val in x]))
    # res = '%s' % ','.join([str(val) if val is not None else '#' for val in x])
    print(res)