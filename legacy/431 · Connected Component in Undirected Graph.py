"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""
from collections import deque
class Solution:
    """
    @param nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet(self, nodes):
        # write your code here
        result = []
        if not nodes:
            return result
        visited = set()

        for node in nodes:
            if node in visited:
                continue
            visited.add(node)
            queue = deque([node])
            component = []
            while queue:
                node = queue.popleft()
                component.append(node.label)
                for neighbor in node.neighbors:
                    if neighbor in visited:
                        continue
                    visited.add(neighbor)
                    queue.append(neighbor)
            result.append(sorted(component))
        return result
