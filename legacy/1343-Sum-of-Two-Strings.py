class Solution:
    """
    @param A: a string
    @param B: a string
    @return: return the sum of two strings
    """
    def SumofTwoStrings(self, A, B):
        # write your code here

        result = []

        length = max(len(A), len(B))

        for i in range(1, length + 1):
            a = 0 if i > len(A) else int(A[-i])
            b = 0 if i > len(B) else int(B[-i])
            sum = a + b

            result.insert(0, str(sum))
        return "".join(result)


class Solution2:
    """
    @param A: a string
    @param B: a string
    @return: return the sum of two strings
    """
    def SumofTwoStrings(self, A, B):
        # write your code here
        res = []
        min_len = min(len(A), len(B))
        for i in range(-1, -1 * (min_len + 1), -1):
            res.insert(0, str(int(A[i]) + int(B[i])))
        if len(A) > min_len:
            res.insert(0, A[:(len(A) - min_len)])
        elif len(B) > min_len:
            res.insert(0, B[:(len(B) - min_len)])

        return "".join(res)

if __name__ == '__main__':
    a = "2"
    b = "321"
    print(Solution().SumofTwoStrings(a, b))