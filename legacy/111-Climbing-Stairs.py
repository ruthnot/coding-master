class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n <= 2:
            return n
        result = [1, 2]
        for _ in range(n - 2):
            result.append(result[-2] + result[-1])
        return result[-1]



if __name__ == '__main__':
    n = 3
    print(Solution().climbStairs(n))



