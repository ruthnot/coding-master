class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climbStairs2(self, n):
        # write your code here
        if n <= 2:
            return max(n, 1)
        if n == 3:
            return 4

        result = [1, 2, 4]

        for _ in range(n - 3):
            result.append(result[-3] + result[-2] + result[-1])

        return result[-1]


if __name__=='__main__':
    print(Solution().climbStairs2(0))
    '1-1-1-1-1'

