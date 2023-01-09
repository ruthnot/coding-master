from typing import (
    List,
)

from copy import deepcopy
"""
Definition for a point:
"""
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class UnionFind:
    def __init__(self):
        self.father = {}
        self.count = 0

    def union(self, p1, p2):
        root_a, root_b = self.find(p1), self.find(p2)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.count -= 1

    def find(self, point):
        path = []
        while point != self.father[point]:
            path.append(point)
            point = self.father[point]
        for p in path:
            self.father[p] = point
        return point


class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def num_islands2(self, n: int, m: int, operators: List[Point]) -> List[int]:
        # write your code here
        islands = set()
        results = []
        uf = UnionFind()
        for operator in operators:
            x, y = operator.x, operator.y
            if (x, y) in islands:
                results.append(uf.count)
                continue
            islands.add((x, y))
            uf.father[(x, y)] = (x, y)
            uf.count += 1
            for dx, dy in DIR:
                nx, ny = x + dx, y + dy
                if (nx, ny) in islands:
                    uf.union((x, y), (nx, ny))
            results.append(uf.count)
        return results