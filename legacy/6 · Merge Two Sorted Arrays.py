from typing import (
    List,
)


class Solution:
    """
    @param a: sorted integer array A
    @param b: sorted integer array B
    @return: A new sorted integer array
    """

    def merge_sorted_array(self, a: List[int], b: List[int]) -> List[int]:
        # write your code here
        res = []
        l, r = 0, 0
        while l < len(a) and r < len(b):
            a_num, b_num = a[l], b[r]
            if a_num < b_num:
                res.append(a_num)
                l += 1
            else:
                res.append(b_num)
                r += 1
        while l < len(a):
            res.append(a[l])
            l += 1
        while r < len(b):
            res.append(b[r])
            r += 1
        return res



