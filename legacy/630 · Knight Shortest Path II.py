
from collections import deque
DIRECTION = [(1, 2), (-1, 2), (2, 1), (-2, 1)]

class Solution:  # BFS
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2(self, grid):
        # write your code here
        n, m = len(grid), len(grid[0])
        start = (0, 0)
        target = (n - 1, m - 1)

        visited = set(start)
        queue = deque([start])
        steps = 0
        while queue:
            size = len(queue)
            steps += 1
            for _ in range(size):
                cell = queue.popleft()
                for dir_x, dir_y in DIRECTION:
                    new_cell = (cell[0] + dir_x, cell[1] + dir_y)
                    if not self.is_valid(new_cell, grid) or new_cell in visited:
                        continue
                    if new_cell == target:
                        return steps
                    visited.add(new_cell)
                    queue.append(new_cell)
        return -1

    def is_valid(self, cell, grid):
        x, y = cell[0], cell[1]
        n, m = len(grid), len(grid[0])
        if not (0 <= x < n and 0 <= y < m):
            return False
        return not grid[x][y]




DIR = [(-1, -2), (1, -2), (-2, -1), (2, -1)]
class Solution:   # DP
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortest_path2(self, grid: List[List[bool]]) -> int:
        # write your code here

        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]

        dp[0][0] = 0

        for j in range(n):    # NOTICE, FIRST LOOP COL, THEN ROW
            for i in range(m):
                if grid[i][j]:
                    continue
                for dir in DIR:
                    x, y = i + dir[0], j + dir[1]
                    if 0 <= x < m and 0 <= y < n:
                        dp[i][j] = min(dp[i][j], dp[x][y] + 1)
        if dp[m - 1][n - 1] == float('inf'):
            return -1

        return dp[m - 1][n - 1]

