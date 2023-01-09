class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        # Write your code here
        if not nums:
            return -1
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if num == number:
                break
        else:
            return -1

        for num in count:
            if count[num] == 1:
                return num

