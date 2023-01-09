class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def num_decodings(self, s: str) -> int:
        # write your code here
        if not s:
            return 0
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1 if 0 < int(s[0]) <= 26 else 0
        for i in range(2, n + 1):
            if 0 < int(s[i - 1]) <= 26:
                dp[i] += dp[i - 1]
            if s[i - 2] != '0' and 0 < int(s[i - 2] + s[i - 1]) <= 26:
                dp[i] += dp[i - 2]
        return dp[n] if n >= 1 else 0