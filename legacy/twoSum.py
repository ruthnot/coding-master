

class Solution1: #Hash Set, O(N)
    def twoSum(self, numbers, target):
        hashset = set()
        for i in range(len(numbers)):
            if target - numbers[i] in hashset:
                return [numbers.index(target - numbers[i]), i]
            hashset.add(numbers[i])
        return [-1, -1]


class Solution2: #排序 + 双指针, O(NlogN)
    def twoSum(self, numbers, target):
        if numbers is None:
            return [-1, -1]
        pair = [(nums, idx) for idx, nums in enumerate(numbers)]
        pair.sort()
        left, right = 0, len(pair) - 1
        while left < right:
            if pair[left][0] + pair[right][0] > target:
                right -= 1
            elif pair[left][0] + pair[right][0] < target:
                left += 1
            else:
                return [pair[left][1], pair[right][1]]
        return [-1, -1]


class Solution3: #Two Sum: less than or equal to target
    def twoSum(self, nums, target):
        if nums is None:
            return -1
        nums.sort()
        count = 0
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                count += right - left
                left += 1
        return count


class Solution4: # twoSum III, 数据结构设计，add and find
    def __init__(self):
        self.nums = []
    def add(self, num):
        self.nums.append(num)
        index = len(self.nums) - 1



    def find(self, num):
        pass

if __name__=='__main__':
    numbers = [2, 7, 11, 15]
    target = 24
    print(Solution3().twoSum(numbers, target))