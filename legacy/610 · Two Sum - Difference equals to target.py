from typing import (
    List,
)
"""
1 2 3 4 5
"""

class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (index1 < index2)
    """
    def two_sum7(self, nums: List[int], target: int) -> List[int]:
        # write your code here
        if len(nums) < 2:
            return [-1, -1]
        target = abs(target)
        left, right = 0, 1
        while left < right and right < len(nums):
            diff = nums[right] - nums[left]
            if diff > target:
                left += 1
                if left == right:
                    right += 1
            elif diff < target:
                right += 1
            else:
                return [nums[left], nums[right]]
        return [-1, -1]

