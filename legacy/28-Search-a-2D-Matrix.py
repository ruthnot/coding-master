class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if self.get_val(matrix, mid) < target:
                start = mid
            else:
                end = mid

        if self.get_val(matrix, start) == target or self.get_val(matrix, end) == target:
            return True
        return False

    def get_val(self, matrix, index):
        n = len(matrix[0])
        i = index // n
        j = index % n
        return matrix[i][j]

if __name__ == '__main__':
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    matrix2 = [[5]]
    target = 3
    print(Solution().searchMatrix(matrix2, target))