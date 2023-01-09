# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

import collections
import math

DIRECTIONS = [(1, 2), (1, -2), (-1, 2), (-1, -2),
              (2, 1), (2, -1), (-2, 1), (-2, -1)]


class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """

    def shortestPath(self, grid, source, destination):
        # write your code here
        if not grid or not grid[0]:
            return -1

        queue = collections.deque([(source.x, source.y)])
        visited = {(source.x, source.y): 0}

        while queue:
            x, y = queue.popleft()
            if (x, y) == (destination.x, destination.y):
                return visited[(x, y)]
            for dx, dy in DIRECTIONS:
                new_x, new_y = x + dx, y + dy
                if not self.is_valid(new_x, new_y, grid):
                    continue
                if (new_x, new_y) in visited:
                    continue
                queue.append((new_x, new_y))
                visited[(new_x, new_y)] = visited[(x, y)] + 1

        return -1

    def is_valid(self, x, y, grid):
        m, n = len(grid), len(grid[0])
        if not (0 <= x < m and 0 <= y < n):
            return False
        return not grid[x][y]



if __name__=='__main__':
    grid = [[0,0,0],[0,0,0],[0,0,0]]
    source = Point(2, 0)
    destination = Point(2, 2)

    res = Solution().shortestPath(grid, source, destination)
    print(res)











