class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """

    def kClosestNumbers(self, A, target, k):
        # write your code here
        if not A:
            return []
        left = self.binarySearch(A, target)
        right = left + 1
        res = []

        for _ in range(k):
            if left < 0:
                res.append(A[right])
                right += 1
            elif right >= len(A):
                res.append(A[left])
                left -= 1
            elif A[right] - target < target - A[left]:
                res.append(A[right])
                right += 1
            else:
                res.append(A[left])
                left -= 1
        return res

    def binarySearch(self, A, target):
        # find lowerClosest, works for fine UpperClosest too, just change accordingly
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] < target:
                left = mid
            elif A[mid] >= target:
                right = mid
        if A[left] <= target:
            return left
        if A[right] <= target:
            return right
        return -1


class Solution2:
    # Jiuzhang solution

    def kClosestNumbers(self, A, target, k):
        right = self.findUpperClosest(A, target)
        left = right - 1

        res = []
        for _ in range(k):
            if self.isLeftCloser(A, target, left, right):
                res.append(A[left])
                left -= 1
            else:
                res.append(A[right])
                right += 1
        return res

    def isLeftCloser(self, A, target, left, right):
        if left < 0:
            return False
        if right >= len(A):
            return True
        return target - A[left] <= A[right] - target

    def findUpperClosest(self, A, target):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid
        if A[start] >= target:
            return start
        if A[end] >= target:
            return end
        return len(A)


