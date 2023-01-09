
class Solution: # Quicksort
    def Sort(self, nums):
        if nums is None:
            return

        self.quickSort(a=nums, start=0, end=len(nums)-1)
        return nums

    def quickSort(self, a, start, end):
        if start >= end:
            return

        left, right = start, end
        pivot = a[int((left + right) / 2)]

        while left <= right:
            while left <= right and a[left] < pivot:
                left += 1
            while left <= right and a[right] > pivot:
                right -= 1
            if left <= right:
                a[left], a[right] = a[right], a[left]
                left += 1
                right -= 1

        self.quickSort(a, start, right)
        self.quickSort(a, left, end)


if __name__=='__main__':
    nums = [3,4,1,0,6,8,7,9]
    print(Solution().Sort(nums))



