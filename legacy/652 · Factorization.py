import math

class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """
    def get_factors(self, n: int) -> List[List[int]]:
        # write your code here
        result = []
        self.dfs(n, 2, [], result)
        return result

    def dfs(self, n, factor, path, result):
        if path:
            path.append(n)
            result.append(path[:])
            path.pop()

        for i in range(factor, int(math.sqrt(n)) + 1):
            if n % i != 0:
                continue
            path.append(i)
            self.dfs(n // i, i, path, result)
            path.pop()
