from typing import (
    List,
)
# 0 0 1 1 1 2
# 0 1 1 0 1 2
# 0 1 0 1 1 2

# 2 3 0 1

class Solution:
    """
    @param a: an integer array
    @return: nothing
    """

    def sort_integers2(self, a: List[int]):
        # write your code here
        self.sort(a, 0, len(a) - 1)

    def sort(self, a, start, end):
        if start >= end:
            return
        left, right = start, end
        pivot = a[(left + right) // 2]
        while left <= right:
            while left <= right and a[left] < pivot:
                left += 1
            while left <= right and a[right] > pivot:
                right -= 1
            if left <= right:
                a[left], a[right] = a[right], a[left]
                left += 1
                right -= 1

        self.sort(a, start, right)
        self.sort(a, left, end)

