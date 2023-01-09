"""
2 3 4
1
"""


class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """

    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        array = []
        i, j = 0, 0
        while i < m and j < n:
            if A[i] <= B[j]:
                array.append(A[i])
                i += 1
            else:
                array.append(B[j])
                j += 1
        while i < m:
            array.append(A[i])
            i += 1
        while j < n:
            array.append(B[j])
            j += 1
        for k in range(m + n):
            A[k] = array[k]







