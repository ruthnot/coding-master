from typing import (
    List,
)


class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """

    def copy_books(self, pages: List[int], k: int) -> int:
        # write your code here
        if not pages or not k:
            return 0
        n = len(pages)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + pages[i - 1]

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        for i in range(k + 1):
            dp[0][i] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for prev in range(i):
                    cost = prefix_sum[i] - prefix_sum[prev]
                    dp[i][j] = min(dp[i][j], max(dp[prev][j - 1], cost))

        return dp[n][k]