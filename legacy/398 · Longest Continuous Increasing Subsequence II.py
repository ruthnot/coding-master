from typing import (
    List,
)

class Solution:
    """
    @param matrix: A 2D-array of integers
    @return: an integer
    """
    def longest_continuous_increasing_subsequence2(self, matrix: List[List[int]]) -> int:
        # write your code here
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((matrix[i][j], i, j))
        cells.sort()

        longest = {}
        for val, x, y in cells:
            longest[(x, y)] = 1
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                new_val = matrix[nx][ny]
                if (nx, ny) in longest and new_val < val:
                    longest[(x, y)] = max(longest[(x, y)], longest[(nx, ny)] + 1)
        return max(longest.values())