

class TwoSum: #Solution 1: sorted list + 双指针 （但是会超时）
    def __init__(self):
        self.nums = []

    def add(self, number):
        self.nums.append(number)
        index = len(self.nums) - 1
        while index > 0 and self.nums[index] < self.nums[index - 1]:
            self.nums[index], self.nums[index - 1] = self.nums[index - 1], self.nums[index]
            index -= 1

    def find(self, value):
        left, right = 0, len(self.nums) - 1
        while left < right:
            two_sum = self.nums[left] + self.nums[right]
            if two_sum < value:
                left += 1
            elif two_sum > value:
                right -= 1
            else:
                return True
        return False


class TwoSum2: # Hashset
    def __init__(self):
        self.num_cnt_dict = {}

    def add(self, number):
        self.num_cnt_dict[number] = self.num_cnt_dict.get(number, 0) + 1

    def find(self, value):
        for num1 in self.num_cnt_dict:
            num2 = value - num1
            num2cnt = 2 if (num1 == num2) else 1
            if self.num_cnt_dict.get(num2, 0) >= num2cnt:
                return True
        return False


if __name__=='__main__':
    a = [1,2,3]
    for i in range(len(a)-1, -1, -1):
        print(a[i])