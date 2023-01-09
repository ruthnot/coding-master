"""
Description
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

You need to support the following method:

connect(a, b), add an edge to connect node a and node b`.
query(a, b), check if two nodes are connected


Example
Example 1:

Input:
ConnectingGraph(5)
query(1, 2)
connect(1, 2)
query(1, 3)
connect(2, 4)
query(1, 4)
Output:
[false,false,true]
Example 2:

Input:
ConnectingGraph(6)
query(1, 2)
query(2, 3)
query(1, 3)
query(5, 6)
query(1, 4)

Output:
[false,false,false,false,false]
"""


class ConnectingGraph:
    """
    @param: n: An integer
    """
    def __init__(self, n):#初始化
        self.father = {}
        for i in range(n + 1):
            self.father[i] = i
    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):#合并
        roota,rootb = self.find(a),self.find(b)
        if roota != rootb :
            self.father[roota] = rootb
    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """
    def query(self, a, b):#询问
        return self.find(a) == self.find(b)

    def find(self, x):#查询
        x2 = x
        if self.father[x] == x:
            return x
        while self.father[x] != x:
            x = self.father[x]
        #路径压缩
        while x2 != x:
            temp = self.father[x2]
            self.father[x2] = x
            x2 = temp
        return x

    """
    #递归写法
    def find(self,x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    """