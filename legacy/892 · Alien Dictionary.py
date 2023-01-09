from typing import (
    List,
)
from heapq import heapify, heappop, heappush


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alien_order(self, words: List[str]) -> str:
        # Write your code here
        # Build graph
        in_degree = {char: 0 for word in words for char in word}
        neighbors = {char: set() for word in words for char in word}
        for pos in range(len(words) - 1):
            for i in range(min(len(words[pos]), len(words[pos + 1]))):
                pre, next = words[pos][i], words[pos + 1][i]

                if i == min(len(words[pos]), len(words[pos + 1])) - 1:
                    if len(words[pos]) > len(words[pos + 1]):
                        if pre == next:
                            print(pos, i)
                            return ""

                if pre != next:
                    in_degree[next] += 1
                    neighbors[pre].add(next)
                    break

        # Topological Sort
        heap = [char for char in in_degree if in_degree[char] == 0]
        heapify(heap)
        order = []
        while heap:
            # for _ in range(len(heap)):
            char = heappop(heap)
            order.append(char)
            for child in neighbors[char]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    heappush(heap, child)

        if len(order) != len(in_degree):
            return ""
        return ''.join(order)



