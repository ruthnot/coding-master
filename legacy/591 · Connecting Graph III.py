"""Description
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

You need to support the following method:

connect(a, b), an edge to connect node a and node b
query(), Returns the number of connected component in the graph


Example
Example 1:

Input:
ConnectingGraph3(5)
query()
connect(1, 2)
query()
connect(2, 4)
query()
connect(1, 4)
query()

Output:[5,4,3,3]
Example 2:

Input:
ConnectingGraph3(6)
query()
query()
query()
query()
query()


Output:
[6,6,6,6,6]
"""


class ConnectingGraph3:
    """
    @param a: An integer
    @param b: An integer
    @return: nothing
    """

    def __init__(self, n):
        # initialize your data structure here.
        self.father = {i: i for i in range(1, n + 1)}
        self.num_connected = n

    def connect(self, a, b):
        # write your code here
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.num_connected -= 1

    def find(self, x):
        node = x
        while self.father[x] != x:
            x = self.father[x]
        root = x
        while self.father[node] != root:
            temp = self.father[node]
            self.father[node] = root
            node = temp
        return root

    """
    @return: An integer
    """

    def query(self):
        # write your code here
        return self.num_connected