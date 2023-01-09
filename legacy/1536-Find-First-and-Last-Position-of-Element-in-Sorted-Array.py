class Solution:
    """
    @param nums: the array of integers
    @param target:
    @return: the starting and ending position
    """
    def searchRange(self, nums, target):
        # Write your code here.
        first = self.searchFirst(nums, target)
        last = self.searchLast(nums, target)
        return [first, last]

    def searchFirst(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid
            else :
                start = mid
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        return -1

    def searchLast(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        if nums[end] == target:
            return end
        elif nums[start] == target:
            return start
        return -1
