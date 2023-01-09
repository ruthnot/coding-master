from typing import (
    List,
)

class Solution:   # Basic version, won't pass check, need optimization
    """
    @param nums: a set of distinct positive integers
    @return: the largest subset
    """

    def largest_divisible_subset(self, nums: List[int]) -> List[int]:
        # write your code here
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        res = []
        dp = [1] * n
        prev = [None] * n
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        prev[i] = j
        # print(prev)
        max_path = 0
        max_idx = None
        for i in range(n):
            if dp[i] > max_path:
                max_path = dp[i]
                max_idx = i
        # print(max_idx)

        path_idx = max_idx
        while path_idx is not None:
            val = nums[path_idx]
            res.append(val)
            path_idx = prev[path_idx]
        return res[::-1]


class Solution:
    """
    @param nums: a set of distinct positive integers
    @return: the largest subset
    """

    def largest_divisible_subset(self, nums: List[int]) -> List[int]:
        # write your code here
        if not nums:
            return []

        nums.sort()
        n = len(nums)

        dp, prev = {}, {}
        for num in nums:
            dp[num] = 1
            prev[num] = -1

        last_num = nums[0]
        for num in nums:
            for factor in self.get_factors(num):
                if factor not in dp:
                    continue

                if dp[num] < dp[factor] + 1:
                    dp[num] = dp[factor] + 1
                    prev[num] = factor
            if dp[num] > dp[last_num]:
                last_num = num

        return self.get_path(prev, last_num)

    def get_path(self, prev, last_num):
        path = []
        while last_num != -1:
            path.append(last_num)
            last_num = prev[last_num]
        return path[::-1]

    def get_factors(self, num):
        if num == 1:
            return []
        factor = 1
        factors = []
        while factor * factor <= num:
            if num % factor == 0:
                factors.append(factor)
                if factor * factor != num and factor != 1:
                    factors.append(num // factor)
            factor += 1
        return factors




