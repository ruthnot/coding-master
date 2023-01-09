class Solution:
    """
    @param str: a string of numbers
    @return: the maximum value
    """
    def max_value(self, str: str) -> int:
        # write your code here
        if not str:
            return 0
        nums = [int(i) for i in str]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('-inf')
                for k in range(i, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k+1][j], dp[i][k] * dp[k+1][j])

        return dp[0][n-1]