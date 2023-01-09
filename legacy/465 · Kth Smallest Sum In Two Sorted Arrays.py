'''
Description
Given two integer arrays sorted in ascending order and an integer k.
Define sum = a + b, where a is an element from the first array and b is an element from the second one.
Find the kth smallest sum out of all possible sums.

Example 1

Input:
a = [1, 7, 11]
b = [2, 4, 6]
k = 3
Output: 7
Explanation: The sums are [3, 5, 7, 9, 11, 13, 13, 15, 17] and the 3th is 7.
Example 2

Input:
a = [1, 7, 11]
b = [2, 4, 6]
k = 4
Output: 9
Explanation: The sums are [3, 5, 7, 9, 11, 13, 13, 15, 17] and the 4th is 9.
Example 3

Input:
a = [1, 7, 11]
b = [2, 4, 6]
k = 8
Output: 15
Explanation: The sums are [3, 5, 7, 9, 11, 13, 13, 15, 17] and the 8th is 15
'''
from typing import (
    List,
)
from heapq import heappush, heappop
class Solution:
    """
    @param a: an integer arrays sorted in ascending order
    @param b: an integer arrays sorted in ascending order
    @param k: An integer
    @return: An integer
    """
    def kth_smallest_sum(self, a: List[int], b: List[int], k: int) -> int:
        # write your code here
        heap = []
        for i in range(len(b)):
            heappush(heap, (b[i] + a[0], 0, i))
        val = None
        for _ in range(k):
            val, a_idx, b_idx = heappop(heap)
            if a_idx == len(a) - 1:
                continue
            new_val = b[b_idx] + a[a_idx + 1]
            heappush(heap, (new_val, a_idx+1, b_idx))
        return val


from heapq import *

class Solution2:
    """
    @param A: an integer arrays sorted in ascending order
    @param B: an integer arrays sorted in ascending order
    @param k: An integer
    @return: An integer
    """
    def kthSmallestSum(self, A, B, k):
        # write your code here
        # 初始化 优先队列 ，我们优先队列的一个元素包括三个值 ：数字和大小，数字在数组A位置，数字在数组B位置
        heap = []
        for i in range(len(B)):
            heappush(heap, [A[0] + B[i], 0, i])
        while k > 1:
            k -= 1
            # 取出堆中最小值
            point = heappop(heap)
            value = point[0]
            aIdx = point[1]
            bIdx = point[2]
            # 已经是所在数组的最后一个元素了
            if (aIdx == len(A) - 1):
                continue
            else:
                # 压入该数组的下一个元素
                newvalue = A[aIdx + 1] + B[bIdx]
                heappush(heap, [newvalue, aIdx + 1, bIdx])
        return heappop(heap)[0]