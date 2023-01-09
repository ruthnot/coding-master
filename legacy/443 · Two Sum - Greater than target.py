class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        # write your code here
        if not nums:
            return 0
        cnt = 0
        nums.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            sums = nums[i] + nums[j]
            if sums <= target:
                i += 1
            else:
                cnt += j - i
                j -= 1
        return cnt
