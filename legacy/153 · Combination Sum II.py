"""
1, 1, 2, 5, 6, 7, 10
"""


class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """

    def combinationSum2(self, num, target):
        # write your code here
        sorted_num = sorted(num)
        combos = []
        self.dfs(sorted_num, target, 0, [], combos)
        return combos

    def dfs(self, num, target, index, combo, combos):
        if sum(combo) == target:
            combos.append(list(combo))
            return
        if sum(combo) > target:
            return

        for i in range(index, len(num)):
            if i != index and num[i] == num[i - 1]:
                continue
            combo.append(num[i])
            self.dfs(num, target, i + 1, combo, combos)
            combo.pop()




