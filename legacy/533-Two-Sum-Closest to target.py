class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        # write your code here
        nums.sort()
        result = float('inf')
        left, right = 0, len(nums) - 1
        while left < right:
            twoSum = nums[left] + nums[right]
            if twoSum < target:
                result = min(result, target - twoSum)
                left += 1
            else:
                result = min(result, twoSum - target)
                right -= 1
        return result



