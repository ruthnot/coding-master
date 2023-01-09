from collections import deque


class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """

    def sequenceReconstruction(self, org, seqs):
        # write your code here
        graph = self.create_graph(seqs)
        in_degree = self.get_in_degree(graph)
        order = self.top_sort(graph, in_degree)
        return order == org

    def create_graph(self, seqs):
        graph = {}
        for seq in seqs:
            for node in seq:
                if node in graph:
                    continue
                graph[node] = set()
        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].add(seq[i])
        return graph

    def get_in_degree(self, graph):
        in_dgree = {x: 0 for x in graph}
        for node, neighbors in graph.items():
            for neighbor in neighbors:
                in_dgree[neighbor] += 1
        return in_dgree

    def top_sort(self, graph, in_degree):
        start_nodes = [x for x in in_degree if in_degree[x] == 0]
        queue = deque(start_nodes)
        order = []
        while queue:
            if len(queue) > 1:
                return None
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return order


