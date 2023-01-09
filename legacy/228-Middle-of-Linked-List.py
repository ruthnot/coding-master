class Solution1: #快慢指针
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middleNode(self, head):
        if not head:
            return None
        slow, fast = head, head
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow


class Solution2: #创建list
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """

    def middleNode(self, head):
        if not head:
            return None
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        mid = (len(nodes) - 1) // 2
        return nodes[mid]
