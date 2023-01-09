
class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (num1 < num2)
    """

    def twoSum7(self, nums, target):
        # write your code here
        if not nums or len(nums) < 2:
            return [-1, -1]

        target = abs(target)

        i, j = 0, 1
        while j < len(nums):
            if nums[j] - nums[i] == target:
                return [nums[i], nums[j]]
            elif nums[j] - nums[i] < target:
                j += 1
            else:
                i += 1
                j = max(j, i + 1)  # 保证j永远不被i追上
        return [-1, -1]


class Solution2:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (num1 < num2)
    """
    def twoSum7(self, nums, target):
        # write your code here
        if not nums:
            return [-1, -1]

        goal = abs(target)
        j = 1
        for i in range(len(nums)):
            j = max(i + 1, j)
            while j < len(nums) and nums[j] - nums[i] < goal:
                j += 1
            if j >= len(nums):
                break
            if nums[j] - nums[i] == goal:
                return [nums[i], nums[j]]
        return [-1, -1]





if __name__ == '__main__':
    nums = [1, 2, 5, 7]
    target = 3
    print(Solution().twoSum7(nums, target))