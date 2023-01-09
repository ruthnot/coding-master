class Solution:

    def findMin(self, nums):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:   # here nums[mid] > nums[start] also work if no sorted input in test cases
                start = mid
            else:
                end = mid

        return min(nums[start], nums[end])

class Solution2:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        min_val = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < min_val:
                return nums[i]
        return min_val
