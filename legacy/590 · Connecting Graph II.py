"""
Description
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

You need to support the following method:

connect(a, b), an edge to connect node a and node b
query(a), Returns the number of connected component nodes which include node a.


Example
Example 1:

Input:
ConnectingGraph2(5)
query(1)
connect(1, 2)
query(1)
connect(2, 4)
query(1)
connect(1, 4)
query(1)
Output:[1,2,3,3]
Example 2:

Input:
ConnectingGraph2(6)
query(1)
query(2)
query(1)
query(5)
query(1)

Output:
[1,1,1,1,1]
"""

class ConnectingGraph2:
    """
    @param: n: An integer
    """
    def __init__(self, n):#初始化
        self.father = {}
        self.nodeNum = {}
        for i in range(n + 1):
            self.father[i] = i
            self.nodeNum[i] = 1
    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):#合并
        roota,rootb = self.find(a),self.find(b)
        if roota != rootb:
            self.father[roota] = rootb
            #记录root块的点数
            self.nodeNum[rootb] += self.nodeNum[roota]

    def query(self, a):#询问
        return self.nodeNum[self.find(a)]

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
    def find(self,x):#查询
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
    """
    #递归写法
    def find(self,x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    """