"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

import collections
from collections import deque
class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        in_degree = {n: 0 for n in graph}
        for n in graph:
            for neighbor in n.neighbors:
                in_degree[neighbor] += 1
        result = []
        queue = deque([])
        for key, val in in_degree.items():
            if val == 0:
                queue.append(key)
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
            result.append(node)
        return result

class Solution2:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        node_to_indegree = self.get_indegree(graph)
        start_nodes = [n for n in graph if node_to_indegree[n] == 0]
        queue = collections.deque(start_nodes)

        order = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for n in node.neighbors:
                node_to_indegree[n] -= 1
                if node_to_indegree[n] == 0:
                    queue.append(n)
        return order

    def get_indegree(self, graph):
        node_to_indegree = {x: 0 for x in graph}

        for node in graph:
            for n in node.neighbors:
                node_to_indegree[n] += 1
        return node_to_indegree