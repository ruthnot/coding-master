class Solution:

    def twoSum6(self, nums, target):
        if not nums or len(nums) < 2:
            return 0

        count = 0
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            two_sum = nums[left] + nums[right]
            if two_sum < target:
                left += 1
            elif two_sum > target:
                right -= 1
            else:
                count += 1
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
        return count

if __name__ == '__main__':
    a = [1, 0, -1]
    res = Solution().twoSum6(a, 0)
    print(res)