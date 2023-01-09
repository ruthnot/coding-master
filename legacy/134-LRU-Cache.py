class LinkedNode:
    def __init__(self, key=None, val=None, next=None):
        self.key = key
        self.val = val
        self.next = next

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self.dummy = LinkedNode()
        self.tail = self.dummy
        self.key_to_prev = {}

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.key_to_prev:
            return -1
        self.kick(key)
        return self.tail.val

    def push_back(self, node):
        self.key_to_prev[node.key] = self.tail
        self.tail.next = node
        self.tail = node
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.key_to_prev:
            self.kick(key)
            self.tail.val = value
            return

        node = LinkedNode(key, value, None)
        self.push_back(node)
        if len(self.key_to_prev) > self.capacity:
            self.pop_front()

    def pop_front(self):
        head = self.dummy.next
        new_head = head.next
        del self.key_to_prev[head.key]
        self.dummy.next = new_head
        self.key_to_prev[new_head.key] = self.dummy

    def kick(self, key):
        prev = self.key_to_prev[key]
        key_node = prev.next

        if key_node == self.tail:
            return

        prev.next = key_node.next
        self.key_to_prev[key_node.next.key] = prev
        key_node.next = None

        return self.push_back(key_node)


