class Solution:
    # Same algorithm as below, tune to my own naming taste
    # put draw function at the end instead of during dfs
    # in draw, an extra reverse function is needed due to the limitation of the test cases lintcode provided
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """

    def solveNQueens(self, n):
        # write your code here
        result = []
        self.dfs(n, [], result)
        return self.draw(n, result)

    def dfs(self, n, path, result):
        if len(path) == n:
            result.append(path[:])
            return
        new_row = len(path)
        for new_col in range(n):
            if not self.is_valid(path, new_row, new_col):
                continue
            path.append(new_col)
            self.dfs(n, path, result)
            path.pop()

    def is_valid(self, path, new_row, new_col):
        for r, c in enumerate(path):
            if new_col == c:
                return False
            if abs(r - new_row) == abs(c - new_col):
                return False
        return True

    def draw(self, n, result):
        solutions = []
        for path in reversed(result):
            solution = []
            for col in path:
                row = ['.' for _ in range(n)]
                row[col] = 'Q'
                solution.append(''.join(row))
            solutions.append(solution)
        return solutions




class Solution2:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        results = []
        self.dfs(n, [], results)
        return results

    def dfs(self, n, cols, results):
        new_row = len(cols)
        if new_row == n:
            results.append(self.draw(cols))
            return
        for new_col in range(n):
            if not self.is_valid(cols, new_row, new_col):
                continue
            cols.append(new_col)
            self.dfs(n, cols, results)
            cols.pop()

    def is_valid(self, cols, new_row, new_col):
        for r, c in enumerate(cols):
            if c == new_col:
                return False
            if abs(new_row - r) == abs(new_col - c):
                return False
        return True

    def draw(self, cols):
        board = []
        n = len(cols)
        for i in range(n):
            row = ['Q' if cols[i] == j else '.' for j in range(n)]
            board.append(''.join(row))
        return board


if __name__=='__main__':
    print(Solution().solveNQueens(4))






