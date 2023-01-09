class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """
    def min_cost(self, n: int, roads: List[List[int]]) -> int:
        # Write your code here
        graph = self.build_graph(n, roads)
        self.min_cost = float('inf')
        visited = set([1])
        self.dfs(n, 1, graph, visited, 0)
        return self.min_cost

    def dfs(self, n, city, graph, visited, cost):
        if len(visited) == n:
            self.min_cost = min(self.min_cost, cost)
            return
        if cost > self.min_cost:
            return
        for next_city, next_cost in graph[city].items():
            if next_city in visited:
                continue
            visited.add(next_city)
            self.dfs(n, next_city, graph, visited, cost + next_cost)
            visited.remove(next_city)

    def build_graph(self, n, roads):
        graph = {}
        for i in range(1, n + 1):
            graph[i] = {}
            for j in range(1, n + 1):
                graph[i][j] = float('inf')
        for x, y, c in roads:
            graph[x][y] = min(graph[x][y], c)
            graph[y][x] = min(graph[y][x], c)
        return graph


class Solution2:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """

    def minCost(self, n, roads):
        # Write your code here
        self.min_cost = float('inf')
        visited = set([1])
        path = [1]
        graph = self.build_graph(n, roads)
        self.dfs(n, graph, 1, path, visited, 0)
        return self.min_cost

    def dfs(self, n, graph, curr_city, path, visited, cost):
        if len(visited) == n:
            self.min_cost = min(self.min_cost, cost)
            return
        for next_city in graph[curr_city]:
            if next_city in visited:
                continue
            if self.has_better_path(graph, path, next_city):
                continue
            visited.add(next_city)
            path.append(next_city)
            self.dfs(n, graph, next_city, path, visited, cost + graph[curr_city][next_city])
            path.pop()
            visited.remove(next_city)

    def has_better_path(self, graph, path, next_city):
        for i in range(1, len(path)):
            current = graph[path[i - 1]][path[i]] + graph[path[-1]][next_city]
            proposal = graph[path[i - 1]][path[-1]] + graph[path[i]][next_city]
            if current > proposal:
                return True
        return False

    def build_graph(self, n, roads):
        graph = {}
        for i in range(1, n + 1):
            graph[i] = {}
            for j in range(1, n + 1):
                graph[i][j] = float('inf')
        for x, y, c in roads:
            graph[x][y] = min(graph[x][y], c)
            graph[y][x] = min(graph[y][x], c)

        return graph


