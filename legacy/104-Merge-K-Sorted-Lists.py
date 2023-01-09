import heapq


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:  # Solution 1: top down
    def mergeKLists(self, lists):
        if len(lists) < 2:
            return lists[0]

        start, end = 0, len(lists)
        mid = (start + end) // 2
        l1 = self.mergeKLists(lists[start:mid])
        l2 = self.mergeKLists(lists[mid:end])
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(None)
        current = dummy
        left, right = l1, l2
        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        if not left:
            current.next = right
        else:
            current.next = left
        return dummy.next


class Solution2:  # Solution 2: bottom up
    def mergeKLists(self, lists):
        if not lists:
            return None

        while len(lists) > 1:
            new_list = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    new_list.append(self.mergeTwoLists(lists[i], lists[i + 1]))
                else:
                    new_list.append(lists[i])
            lists = new_list
        return lists[0]

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(None)
        current = dummy
        left, right = l1, l2
        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        if not left:
            current.next = right
        else:
            current.next = left
        return dummy.next


ListNode.__lt__ = lambda x, y: x.val < y.val


class Solution3:  # Solution 3: Heap
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        heap = []
        for node in lists:
            if node is None:
                continue
            heapq.heappush(heap, node)

        dummy = ListNode(None)
        head = dummy
        while heap:
            new_node = heapq.heappop(heap)
            if new_node.next is not None:
                heapq.heappush(heap, new_node.next)
            head.next = new_node
            head = new_node

        return dummy.next


if __name__=='__main__':
    a = [1, 4, 5, 7]
    l, r = 0, len(a)
    mid = (l + r) // 2
    print(l, r, mid)
    print(a[l:mid], a[mid:r])


