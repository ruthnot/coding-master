from typing import (
    List,
)


class Solution:  # DFS
    """
    @param nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        permutations = []
        visited = [False] * len(nums)
        self.dfs(nums, visited, [], permutations)
        return permutations

    def dfs(self, nums, visited, permutation, permutations):
        if len(permutation) == len(nums):
            permutations.append(list(permutation))
            return
        for i in range(len(nums)):
            if visited[i]:
                continue
            visited[i] = True
            permutation.append(nums[i])
            self.dfs(nums, visited, permutation, permutations)
            permutation.pop()
            visited[i] = False


class Solution2:  # Non-recursion
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        result = []
        stack = [[i] for i in nums]
        while stack:
            last = stack.pop()
            if len(last) == len(nums):
                result.append(last)
                continue
            for n in nums:
                if n not in last:
                    stack.append(last + [n])
        return result

