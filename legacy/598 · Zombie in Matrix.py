from collections import deque

DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """

    def zombie(self, grid):
        # write your code here
        n, m = len(grid), len(grid[0])
        target = n * m
        initial_zombies = self.get_zombies(grid)
        visited = set(initial_zombies)
        queue = deque(initial_zombies)

        days = -1
        while queue:
            days += 1
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for dx, dy in DIR:
                    new_x, new_y = x + dx, y + dy
                    if not self.is_valid(new_x, new_y, grid) or (new_x, new_y) in visited:
                        continue
                    if grid[new_x][new_y] == 2:
                        visited.add((new_x, new_y))
                        continue
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y))
        return days if len(visited) == target else -1

    def get_zombies(self, grid):
        result = []
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    result.append((x, y))
        return result

    def is_valid(self, x, y, grid):
        n, m = len(grid), len(grid[0])
        if not (0 <= x < n and 0 <= y < m):
            return False
        return True

