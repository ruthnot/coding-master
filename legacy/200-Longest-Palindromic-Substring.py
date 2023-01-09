class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        if not s:
            return None
        longest = 1
        longest_idx = (0, 1)
        for i in range(len(s) - 1):
            longest_odd, idx_odd = self.validPalindrome(s, i, l=i, r=i)
            if longest_odd > longest:
                longest = longest_odd
                longest_idx = idx_odd
            if i + 1 >= len(s) or s[i] != s[i+1]:
                continue

            longest_even, idx_even = self.validPalindrome(s, i, l=i, r=i+1)
            if longest_even > longest:
                longest = longest_even
                longest_idx = idx_even
        return s[longest_idx[0]:longest_idx[1]+1]

    def validPalindrome(self, s, i, l, r):
        longest = r - l + 1
        while 0 <= (l - 1) and (r + 1) < len(s):
            if s[l - 1] != s[r + 1]:
                break
            longest += 2
            l -= 1
            r += 1
        return longest, (l, r)


class Solution:  # DP
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """

    def longest_palindrome(self, s: str) -> str:
        # write your code here
        if not s:
            return ""

        n = len(s)
        dp = [[False] * n for _ in range(n)]

        maxLen = 1
        maxIdx = 0

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                maxLen = 2
                maxIdx = i

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                if dp[i][j] and length > maxLen:
                    maxLen = length
                    maxIdx = i

        return s[maxIdx:maxIdx + maxLen]