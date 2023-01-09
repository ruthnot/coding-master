from collections import deque
class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        answers = []
        # nums = deque([i for i in range(1, n + 1)])
        nums = [i for i in range(1, n + 1)]
        self.dfs(k, nums, 0, [], answers)

        return answers

    def dfs(self, k, nums, idx, answer, answers):
        if len(answer) == k:
            answers.append(list(answer))
            return
        for i in range(idx, len(nums)):
            answer.append(nums[i])
            self.dfs(k, nums, i + 1, answer, answers)
            answer.pop()

if __name__ == '__main__':
    a = "1 2 3 4 5 6"
    n = 4
    k = 2
    print(Solution().combine(n, k))






