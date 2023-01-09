import collections

DIRECTIONS = {
    'U': [0, -1],
    'R': [1, 0],
    'D': [0, 1],
    'L': [-1, 0]
}


class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """

    def shortestDistance(self, maze, start, destination):
        # (x, y, direction)
        queue = collections.deque()
        distance = {}

        start = (start[0], start[1], None)
        destination = (destination[0], destination[1], None)

        queue.append(start)
        distance[start] = 0

        while queue:
            (curr_x, curr_y, curr_dire) = queue.popleft()
            if (curr_x, curr_y, curr_dire) == destination:
                return distance[(curr_x, curr_y, curr_dire)]

            if curr_dire != None:
                new_x, new_y = curr_x + DIRECTIONS[curr_dire][0], curr_y + DIRECTIONS[curr_dire][1]
                if self.is_vaild(maze, new_x, new_y):
                    if (new_x, new_y, curr_dire) in distance:
                        continue
                    queue.append((new_x, new_y, curr_dire))
                    distance[(new_x, new_y, curr_dire)] = distance[(curr_x, curr_y, curr_dire)] + 1
                else:
                    if (curr_x, curr_y, None) in distance:
                        continue
                    queue.append((curr_x, curr_y, None))
                    distance[(curr_x, curr_y, None)] = distance[(curr_x, curr_y, curr_dire)]
            else:
                for new_dire in DIRECTIONS:
                    new_x, new_y = curr_x + DIRECTIONS[new_dire][0], curr_y + DIRECTIONS[new_dire][1]
                    if self.is_vaild(maze, new_x, new_y):
                        if (new_x, new_y, new_dire) in distance:
                            continue
                        queue.append((new_x, new_y, new_dire))
                        distance[(new_x, new_y, new_dire)] = distance[(curr_x, curr_y, curr_dire)] + 1

        return -1

    def is_vaild(self, maze, x, y):
        n, m = len(maze), len(maze[0])

        if x < 0 or x >= n:
            return False
        if y < 0 or y >= m:
            return False

        return not maze[x][y]