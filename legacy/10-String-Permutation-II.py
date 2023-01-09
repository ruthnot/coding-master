class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        # write your code here
        if str is None:
            return [""]

        chars = sorted(list(str))
        visited = [False] * len(chars)
        permutations = []
        self.dfs(chars, visited, [], permutations)
        return permutations

    def dfs(self, chars, visited, permutation, permutations):
        if len(permutation) == len(chars):
            permutations.append(''.join(permutation))
            return

        for i in range(len(chars)):
            if visited[i]:
                continue

            if i > 0 and chars[i - 1] == chars[i] and not visited[i - 1]:
                continue

            visited[i] = True
            permutation.append(chars[i])
            self.dfs(chars, visited, permutation, permutations)
            permutation.pop()
            visited[i] = False


if __name__=='__main__':
    a = 'abcdefga'
    res = Solution().stringPermutation2(a)
    print(res)

