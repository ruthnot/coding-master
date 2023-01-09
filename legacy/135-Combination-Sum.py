class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        if candidates is None:
            return []
        sorted_candidates = sorted(set(list(candidates)))
        subsets = []
        self.dfs(sorted_candidates, 0, target, [], subsets)
        return subsets

    def dfs(self, candidates, index, target, subset, subsets):
        if target == 0:
            subsets.append(list(subset))
            return

        if target < 0:
            return

        for i in range(index, len(candidates)):
            subset.append(candidates[i])
            self.dfs(candidates, i, target - candidates[i], subset, subsets)
            subset.pop()


if __name__ == '__main__':
    A = [1]
    target = 3
    res = Solution().combinationSum(A, target)
    print(res)