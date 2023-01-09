class Solution:  # check out 33.N-queens comment
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def total_n_queens(self, n: int) -> int:
        # write your code here
        self.count = 0
        self.dfs(n, [])
        return self.count

    def dfs(self, n, path):
        if len(path) == n:
            self.count += 1
            return
        new_row = len(path)
        for new_col in range(n):
            if not self.is_valid(path, new_row, new_col):
                continue
            path.append(new_col)
            self.dfs(n, path)
            path.pop()

    def is_valid(self, path, n_r, n_c):
        for r, c in enumerate(path):
            if n_c == c:
                return False
            if abs(r - n_r) == abs(c - n_c):
                return False
        return True


class Solution2:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        results = []
        self.dfs(n, [], results)
        return len(results)

    def dfs(self, n, cols, results):
        row = len(cols)
        if row == n:
            results.append(list(cols))
            return
        for j in range(n):
            if not self.isValid(cols, row, j):
                continue
            cols.append(j)
            self.dfs(n, cols, results)
            cols.pop()

    def isValid(self, cols, row, col):
        for i, j in enumerate(cols):
            if j == col:
                return False
            if i - j == row - col or i + j == row + col:
                return False
        return True

