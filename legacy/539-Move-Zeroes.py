class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def move_zeroes(self, nums: List[int]):
        # write your code here
        left, right = 0, 0
        while right < len(nums):
            while right < len(nums):
                if nums[right] != 0:
                    break
                right += 1
            if right < len(nums):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1


class Solution2:  # 同向双指针
    def moveZeroes(self, nums):
        # write your code here
        if not nums:
            return nums
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != 0:
                if i != j:
                    nums[i] = nums[j]
                i += 1
            j += 1

        while i < len(nums):
            if nums[i] != 0:
                nums[i] = 0
            i += 1

class Solution3:  # 相向双指针
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        if not nums:
            return None
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] == 0:
                nums.append(nums.pop(left))
                right -= 1
                continue
            left += 1


if __name__=='__main__':
    print(5)

