from typing import (
    List,
)

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def three_sum_closest(self, numbers: List[int], target: int) -> int:
        # write your code here
        numbers.sort()
        ans = float('inf')
        for i in range(len(numbers)):
            left, right = i + 1, len(numbers) - 1
            while left < right:
                sum = numbers[left] + numbers[right] + numbers[i]
                if abs(ans - target) > abs(sum - target):
                    ans = sum
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    return sum
        return ans
