class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """

    def woodCut(self, L, k):
        # write your code here
        if not L:
            return 0

        start, end = 1, max(L)
        while start + 1 < end:
            mid = (start + end) // 2
            count = self.getCount(L, mid)
            if count >= k:
                start = mid
            else:
                end = mid
        if self.getCount(L, end) >= k:
            return end
        if self.getCount(L, start) >= k:
            return start
        return 0

    def getCount(self, L, length):
        return sum(l // length for l in L)




class Solution2:  # official solution
    def woodCut(self, L, k):
        if not L:
            return 0

        start, end = 1, min(max(L), sum(L) // k)
        if end < 1:
            return 0
        while start + 1 < end:
            mid = (start + end) // 2
            if self.getCount(L, mid) >= k:
                start = mid
            else:
                end = mid
        return end if self.getCount(L, end) >= k else start

    def getCount(self, L, length):
        return sum(l // length for l in L)
