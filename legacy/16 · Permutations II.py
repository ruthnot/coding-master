from typing import (
    List,
)


class Solution:  # DFS
    """
    @param nums: A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        sorted_nums = sorted(nums)
        results = []
        visited = [False] * len(nums)
        self.dfs(sorted_nums, visited, [], results)
        return results

    def dfs(self, nums, visited, result, results):
        if len(result) == len(nums):
            results.append(list(result))
            return

        for i in range(len(nums)):
            if visited[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue
            result.append(nums[i])
            visited[i] = True
            self.dfs(nums, visited, result, results)
            visited[i] = False
            result.pop()


class Solution2:  # Non-recursive
    """
    @param nums: A list of integers
    @return: A list of unique permutations
    """
    def permute_unique(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        if not nums:
            return [[]]
        result = []
        nums.sort()
        stack = []
        check = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            stack.append([nums[i]])
            check.append([False] * len(nums))
            check[-1][i] = True

        while stack:
            path = stack.pop()
            visited = check.pop()
            if len(path) == len(nums):
                result.append(path)
                continue
            for i in range(len(nums)):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                path.append(nums[i])
                stack.append(path[:])
                path.pop()

                visited[i] = True
                check.append(visited[:])
                visited[i] = False

        return result