from typing import (
    List,
)

class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """

    def kthSmallest(self, k, nums):
        # write your code here
        return self.quickSelect(nums, 0, len(nums) - 1, k - 1)

    def quickSelect(self, nums, start, end, k):
        if start == end:
            return nums[start]
        left, right = start, end
        pivot = nums[(left + right) // 2]  # Warning: don't assign pivot as an index

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        if right >= k:
            return self.quickSelect(nums, start, right, k)
        elif left <= k:
            return self.quickSelect(nums, left, end, k)
        else:
            return nums[k]