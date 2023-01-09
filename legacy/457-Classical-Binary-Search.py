class Solution:

    def findPosition(self, nums, target):
        if not nums:
            return -1

        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                end = mid
            else:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

if __name__=='__main__':
    a = [1, 2, 2, 4, 5, 5]
    target = 2
    print(Solution().findPosition(a, target))

