import collections

class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []


from collections import deque
class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def clone_graph(self, node: UndirectedGraphNode) -> UndirectedGraphNode:
        # write your code here
        if not node:
            return node
        root = UndirectedGraphNode(node.label)
        visited = {root.label: root}
        queue = deque([node])
        while queue:
            curr = queue.popleft()
            for n in curr.neighbors:
                if n.label not in visited:
                    visited[n.label] = UndirectedGraphNode(n.label)
                    queue.append(n)
                visited[curr.label].neighbors.append(visited[n.label])
        return root


class Solution2:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        if not node:
            return None

        nodes = self.find_nodes_by_bfs(node)
        mapping = self.copy_nodes(nodes)
        self.copy_edges(nodes, mapping)
        return mapping[node]

    def find_nodes_by_bfs(self, node):
        queue = collections.deque([node])
        visited = set([node])
        while queue:
            cur_node = queue.popleft()
            for n in cur_node.neighbors:
                if n in visited:
                    continue
                queue.append(n)
                visited.add(n)
        return list(visited)

    def copy_nodes(self, nodes):
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)
        return mapping

    def copy_edges(self, nodes, mapping):
        for node in nodes:
            new_node = mapping[node]
            for n in node.neighbors:
                new_neighbor = mapping[n]
                new_node.neighbors.append(new_neighbor)




