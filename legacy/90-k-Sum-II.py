class Solution:
    """
    @param A: an integer array
    @param k: a postive integer <= length(A)
    @param target: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        # write your code here
        results = []
        self.dfs(A, k, target, 0, [], results)
        return results

    def dfs(self, nums, k, target, index, result, results):
        if k == 0 and target == 0:
            results.append(list(result))
            return

        if k == 0 or target <= 0:
            return

        for i in range(index, len(nums)):
            result.append(nums[i])
            new_target = target - nums[i]
            new_k = k - 1
            self.dfs(nums, new_k, new_target, i + 1, result, results)
            result.pop()

if __name__ == '__main__':
    A = [1, 2, 3, 4]
    k = 2
    target = 5
    result = Solution().kSumII(A, k, target)
    print(result)





