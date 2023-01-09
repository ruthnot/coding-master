
class Solution: # Merge Sort
    def Sort(self, nums):
        if not nums:
            return
        temp = [0 for _ in range(len(nums))]
        self.mergeSort(nums, 0, len(nums)-1, temp)
        return nums

    def mergeSort(self, nums, start, end, temp):
        if start >= end:
            return
        mid = (start + end) // 2
        self.mergeSort(nums, start, mid, temp)
        self.mergeSort(nums, mid + 1, end, temp)
        self.merge(nums, start, mid, end, temp)

    def merge(self, nums, start, mid, end, temp):
        left, right = start, mid + 1
        index = start
        while left <= mid and right <= end:
            if nums[left] < nums[right]:
                temp[index] = nums[left]
                left += 1
            else:
                temp[index] = nums[right]
                right += 1
            index += 1

        while left <= mid:
            temp[index] = nums[left]
            left += 1
            index += 1

        while right <= end:
            temp[index] = nums[right]
            right += 1
            index += 1

        for i in range(start, end + 1):
            nums[i] = temp[i]


if __name__=='__main__':
    nums = [3, 4, 1, 0, 6, 8, 7, 9]
    print(Solution().Sort(nums))
