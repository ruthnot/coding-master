import heapq

class Solution:  #Heap + set
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        heap = [1]
        seen = {1}
        curr_ugly = 1

        for _ in range(n):
            curr_ugly = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                new_ugly = curr_ugly * factor
                if new_ugly not in seen:
                    heapq.heappush(heap, new_ugly)
                    seen.add(new_ugly)
        return curr_ugly