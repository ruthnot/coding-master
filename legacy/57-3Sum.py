

class Solution:
    def threeSum(self, numbers):
        results = []

        if not numbers or len(numbers) < 3:
            return results

        numbers.sort()

        length = len(numbers)
        for i in range(0, length - 2):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            left = i + 1
            right = length - 1
            target = -numbers[i]
            self.twoSum(numbers, left, right, target, results)
        return results

    def twoSum(self, numbers, left, right, target, results):
        while left < right:
            two_sum = numbers[left] + numbers[right]
            if two_sum < target:
                left += 1
            elif two_sum > target:
                right -= 1
            else:
                results.append([-target, numbers[left], numbers[right]])
                left += 1
                right -= 1
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1

if __name__ == '__main__':
    a = [-7, -7, 2, 2, 3, 4, 5, 5]
    res = Solution().threeSum(a)
    print(res)