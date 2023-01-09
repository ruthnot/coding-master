class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if not nums:
            return 0

        nums.sort()
        j = 1
        for i in range(len(nums)):
            j = max(j, i + 1)
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            if j >= len(nums):
                return i + 1
            nums[i + 1] = nums[j]
            # 0 0 0 1 1 1 2 2 2


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().deduplication(nums))