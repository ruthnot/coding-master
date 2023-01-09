DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
from collections import deque

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def hasPath(self, maze, start, destination):
        # write your code here
        if not maze or not maze[0]:
            return False

        visited = {tuple(start)}
        queue = deque({tuple(start)})
        while queue:
            x, y = queue.popleft()
            if (x, y) == tuple(destination):
                return True
            for direction in DIR:
                next_valid = self.find_next_valid(maze, (x, y), direction)
                if next_valid not in visited:
                    queue.append(next_valid)
                    visited.add(next_valid)
        return False

    def find_next_valid(self, maze, current, direction):
        while True:
            candidate = (current[0] + direction[0], current[1] + direction[1])
            if not self.is_valid(maze, candidate):
                return current
            current = candidate

    def is_valid(self, maze, node):
        m, n = len(maze), len(maze[0])
        x, y = node
        if not (0 <= x < m and 0 <= y < n):
            return False
        return not maze[x][y]






if __name__=='__main__':
#     map = [[0,0,1,0,0],
#  [0,0,0,0,0],
#  [0,0,0,1,0],
#  [1,1,0,1,1],
#  [0,0,0,0,0]
# ]
#     start = [0,4]
#     end = [4,4]
#     print(Solution().hasPath(map, start, end))
#
    a = (1, 2)
    b = (2, 3)
    c = a + b
    print(c)


