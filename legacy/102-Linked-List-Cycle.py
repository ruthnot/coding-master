class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow and fast and fast.next:
            if slow.val == fast.val:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

