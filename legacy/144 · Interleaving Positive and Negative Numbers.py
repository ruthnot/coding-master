class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """

    def rerange(self, A):
        # write your code here
        pos, neg = 0, 0
        for num in A:
            if num > 0:
                pos += 1
            else:
                neg += 1
        self.partition(A, pos > neg)
        self.interleave(A, pos == neg)

    def partition(self, A, start_positive):
        flag = 1 if start_positive else -1
        left, right = 0, len(A) - 1
        while left <= right:
            while left <= right and A[left] * flag > 0:
                left += 1
            while left <= right and A[right] * flag < 0:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

    def interleave(self, A, has_same_length):
        left = 1
        right = len(A) - 2 if has_same_length else len(A) - 1
        while left < right:
            A[left], A[right] = A[right], A[left]
            left, right = left + 2, right - 2



