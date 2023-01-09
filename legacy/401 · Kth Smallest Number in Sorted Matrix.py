

from typing import (
    List,
)
from heapq import heappop, heappush
class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    def kth_smallest(self, matrix: List[List[int]], k: int) -> int:
        # write your code here
        heap = []
        for i in range(len(matrix)):
            heappush(heap, (matrix[i][0], i, 0))

        for _ in range(k):
            val, row, col = heappop(heap)
            if col == len(matrix[0]) - 1:
                continue
            heappush(heap, (matrix[row][col+1], row, col+1))
        return val


class Solution2:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        # write your code here
        # 初始化 优先堆 ，我们堆的一个元素包括三个值 ：数字大小，数字在哪个数组里，数字在数组的哪个位置
        heap = []
        for i in range(len(matrix)):
            # 如果这个数组为空 则不用压入
            if len(matrix[i]) == 0:
                continue
            # matrix[i][0] 权值大小  i 在第i个数组   0 在该数组的0位置
            heappush(heap, [matrix[i][0], i, 0])
        while k > 1:
            k -= 1
            # 取出堆中最小值
            point = heappop(heap)
            value = point[0]
            arraysIdx = point[1]
            idx = point[2]
            # 已经是所在数组的最后一个元素了
            if (idx == len(matrix[arraysIdx]) - 1):
                continue
            else:
                # 压入该数组的下一个元素
                newvalue = matrix[arraysIdx][idx + 1]
                heappush(heap, [newvalue, arraysIdx, idx + 1])
        return heappop(heap)[0]