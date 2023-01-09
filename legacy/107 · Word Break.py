from typing import (
    Set,
)


class Solution:
    """
    @param s: A string
    @param word_set: A dictionary of words dict
    @return: A boolean
    """
    def word_break(self, s: str, word_set: Set[str]) -> bool:
        # write your code here
        if not s:
            return True
        n = len(s)
        max_length = max([len(word) for word in word_set]) if word_set else 0

        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for l in range(1, max_length + 1):
                if i < l:
                    break
                if not dp[i - l]:
                    continue
                word = s[i - l:i]
                if word in word_set:
                    dp[i] = True
                    break
        return dp[n]



class Solution:  # (Not optimized, won't pass unit test)
    """
    @param s: A string
    @param word_set: A dictionary of words dict
    @return: A boolean
    """
    def word_break(self, s: str, word_set: Set[str]) -> bool:
        # write your code here
        if not s:
            return True
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if not dp[j]:
                    continue
                word = s[j:i]
                if word in word_set:
                    dp[i] = True
                    break
        return dp[n]