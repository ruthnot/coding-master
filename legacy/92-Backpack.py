from typing import (
    List,
)

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @return: The maximum size
    """
    def back_pack(self, m: int, a: List[int]) -> int:
        # write your code here
        n = len(a)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            dp[i][0] = True
            for j in range(1, m + 1):
                if j >= a[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - a[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        for j in range(m, -1, -1):
            if dp[n][j]:
                return j
        return -1
