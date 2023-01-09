"""
2,0,2,2,1,2,2,1,2,0,0,0,1
i


"""





class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        left, mid, right = 0, 0, len(nums) - 1
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1
        return nums

class Solution2:
    def sortColors(self, nums):
        if not nums:
            return

        color_count = [0] * 3

        for num in nums:
            color_count[num] += 1

        index = 0
        for i in range(len(color_count)):
            count = color_count[i]
            while count > 0:
                nums[index] = i
                count -= 1
                index += 1


class Solution3:  # need quick sort method
    def sortColors(self, nums):
        pass