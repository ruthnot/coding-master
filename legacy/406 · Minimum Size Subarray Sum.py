from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        left = 0
        curr_sum = 0
        res = float('inf')

        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= s:
                res = min(res, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return -1 if res == float('inf') else res