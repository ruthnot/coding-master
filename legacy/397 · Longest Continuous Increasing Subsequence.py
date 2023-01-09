from typing import (
    List,
)

class Solution:
    """
    @param a: An array of Integer
    @return: an integer
    """
    def longest_increasing_continuous_subsequence(self, a: List[int]) -> int:
        # write your code here
        if not a:
            return 0
        n = len(a)
        dp1 = [1] * n
        dp2 = [1] * n
        for i in range(1, n):
            if a[i] > a[i - 1]:
                dp1[i] += dp1[i - 1]
        for j in range(n - 2, -1, -1):
            if a[j] > a[j + 1]:
                dp2[j] += dp2[j + 1]
        return max(max(dp1), max(dp2))

