class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        if not s:
            return [[]]
        combinations = []
        self.dfs(s, 0, [], combinations)
        return combinations

    def dfs(self, s, i, combination, combinations):
        if i == len(s):
            combinations.append(list(combination))
            return

        combination.append(s[i])
        self.dfs(s, i + 1, combination, combinations)
        combination.pop()

        if i >= len(s) - 1:
            return

        combination.append(s[i:i + 2])
        self.dfs(s, i + 2, combination, combinations)
        combination.pop()



class Solution2:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        results = []
        self.dfs(s, [], results)
        return results

    def dfs(self, s, result, results):
        if len(s) == 0:
            results.append(list(result))
            return
        if len(s) > 0:
            result.append(s[0])
            substr = s[1:]
            self.dfs(substr, result, results)
            result.pop()

        if len(s) > 1:
            result.append(s[0:2])
            substr = s[2:]
            self.dfs(substr, result, results)
            result.pop()

if __name__=='__main__':
     x = "12345"
     print(Solution().splitString(x))
