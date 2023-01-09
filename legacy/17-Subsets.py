
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        sorted_nums = sorted(nums)
        results = []
        self.dfs(sorted_nums, 0, [], results)
        return results

    def dfs(self, nums, index, result, results):
        results.append(list(result))
        for i in range(index, len(nums)):
            result.append(nums[i])
            self.dfs(nums, i + 1, result, results)
            result.pop()

class Solution2:  # DFS w/o Backtracking
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        self.results = []
        nums.sort()
        self.dfs(nums, [], 0)
        return self.results

    def dfs(self, nums, subsets, index):
        if index == len(nums):
            self.results.append(list(subsets))
            return
        subsets.append(nums[index])
        self.dfs(nums, subsets, index + 1)
        subsets.pop()
        self.dfs(nums, subsets, index + 1)




class Solution3: # BFS 1
    def subsets(self, nums):
        if not nums:
            return [[]]
        queue = [[]]
        index = 0
        while index < len(queue):
            subset = queue[index]
            index += 1
            for num in nums:
                if subset and subset[-1] >= num:
                    continue
                queue.append(subset + [num])
        return queue


class Solution4:  # BFS 2
    def subsets(self, nums):
        if not nums:
            return [[]]
        queue = [[]]
        for num in sorted(nums):
            for i in range(len(queue)):
                subset = list(queue[i])
                subset.append(num)
                queue.append(subset)
        return queue




if __name__=='__main__':
    a = [0, 1]
    a.sort()
    print(a)