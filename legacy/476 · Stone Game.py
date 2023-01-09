from typing import (
    List,
)


class Solution:
    """
    @param a: An integer array
    @return: An integer
    """

    def stone_game(self, a: List[int]) -> int:
        # write your code here
        if not a:
            return 0
        n = len(a)
        dp = [[0] * n for _ in range(n)]
        sums = [[0] * n for _ in range(n)]

        for i in range(n):
            sums[i][i] = a[i]
            for j in range(i + 1, n):
                sums[i][j] = sums[i][j - 1] + a[j]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + sums[i][j])

        return dp[0][n - 1]

