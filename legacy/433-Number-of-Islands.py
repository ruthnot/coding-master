from collections import deque
import math
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        visited = set()
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visited or not grid[i][j]:
                    continue
                result += 1
                self.dfs(grid, i, j, visited)
        return result

    def dfs(self, grid, i, j, visited):
        if (i, j) in visited:
            return
        visited.add((i, j))
        for dir in DIR:
            new_i, new_j = i + dir[0], j + dir[1]
            if self.isValid(new_i, new_j, grid) and (new_i, new_j) not in visited and grid[new_i][new_j]:
                self.dfs(grid, new_i, new_j, visited)

    def isValid(self, i, j, grid):
        if i < 0 or i >= len(grid):
            return False
        if j < 0 or j >= len(grid[0]):
            return False
        return True



class Solution2:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        islands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islands += 1
        return islands

    def bfs(self, grid, x, y, visited):
        queue = deque([(x, y)])
        visited.add((x, y))
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in DIRECTIONS:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.is_valid(grid, next_x, next_y, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))

    def is_valid(self, grid, x, y, visited):
        n, m = len(grid), len(grid[0])
        if not (0 <= x < n and 0 <= y < m):
            return False
        if (x, y) in visited:
            return False
        return grid[x][y]









if __name__=='__main__':
    a = (1, -2)
    b = (4, 5)
    x = set(a)
    x.add(b)
    print(x)

