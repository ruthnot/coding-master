from typing import (
    List,
)

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        # write your code here
        sorted_nums = sorted(numbers)
        i, j = 0, len(numbers) - 1
        while i < j:
            sums = sorted_nums[i] + sorted_nums[j]
            if sums > target:
                j -= 1
            elif sums < target:
                i += 1
            else:
                break
        if i >= j:
            return None
        results = []
        for k in range(len(numbers)):
            if numbers[k] == sorted_nums[i] or numbers[k] == sorted_nums[j]:
                results.append(k)
            if len(results) == 2:
                break

        return sorted(results)