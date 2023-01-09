from typing import (
    List,
)

class Solution:
    """
    @param a: A list of integers
    @return: A boolean
    """
    def can_jump(self, a: List[int]) -> bool:
        # write your code here
        dp = [False] * len(a)
        dp[-1] = True
        for i in range(len(a) - 2, -1, -1):
            max_step = a[i]
            if max_step == 0:
                continue
            for j in range(1, max_step + 1):
                if dp[i + j]:
                    dp[i] = True
                    break
        return dp[0]
