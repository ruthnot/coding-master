"""
Sample Walk through:
[1, 2, 2, 3]
1 - 12 - 122 - 1223
       - 123
    12'
    13
2 - 22 - 223
    23
2'
3
"""

class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """

    def subsetsWithDup(self, nums):
        # write your code here
        if not nums:
            return [[]]
        sorted_nums = sorted(nums)
        results = []
        self.dfs(sorted_nums, 0, [], results)
        return results

    def dfs(self, nums, index, result, results):
        results.append(list(result))

        for i in range(index, len(nums)):
            if (i > index and nums[i] == nums[i - 1]):
                continue
            result.append(nums[i])
            self.dfs(nums, i + 1, result, results)
            result.pop()



