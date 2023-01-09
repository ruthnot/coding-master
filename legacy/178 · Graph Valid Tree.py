from collections import deque


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        # write your code here
        if len(edges) != n - 1:
            return False

        neighbors = {x: [] for x in range(n)}
        for x, y in edges:
            neighbors[x].append(y)
            neighbors[y].append(x)
        visited = {0}
        queue = deque([0])
        while queue:
            node = queue.popleft()
            for neighbor in neighbors[node]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append(neighbor)
        return len(visited) == n

