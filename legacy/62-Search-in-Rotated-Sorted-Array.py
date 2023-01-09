class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if not A:
            return -1

        pivot = self.findPivot(A)
        if target > A[-1]:
            start, end = 0, pivot - 1
        else:
            start, end = pivot, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1

    def findPivot(self, A):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] > A[end]:
                start = mid
            else:
                end = mid
        return start if A[start] < A[end] else end






class Solution2: #official
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """

    def search(self, A, target):
        if not A:
            return -1
        # write your code here
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] > A[end]:
                start = mid
            elif A[mid] < A[end]:
                end = mid
            else:
                end = mid
        pivot = start if A[start] < A[end] else end

        if target <= A[len(A) - 1]:
            start, end = pivot, len(A) - 1
        else:
            start, end = 0, pivot - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            elif A[mid] > target:
                end = mid
            else:
                end = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1

if __name__=='__main__':
    x = [6,8,9,1,3,5]
    y = 5
    res = Solution().search(x, y)
    print(res)