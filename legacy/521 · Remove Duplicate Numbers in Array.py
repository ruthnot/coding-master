
class Solution1:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if not nums:
            return 0
        nums.sort()
        l, r = 0, 0
        while r < len(nums):
            if nums[r] == nums[l]:
                r += 1
            else:
                l += 1
                nums[l] = nums[r]
                r += 1
        return l + 1


class Solution2:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if not nums:
            return 0
        nums.sort()
        l, r = 0, 0
        while r < len(nums):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
            r += 1
        return l + 1