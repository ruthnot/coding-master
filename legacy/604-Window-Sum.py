class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    def winSum(self, nums, k):
        # write your code here
        result = []
        j = 0
        window_sum = 0
        for i in range(len(nums)):
            while j < len(nums) and j - i < k:
                window_sum += nums[j]
                j += 1
            if j - i == k:
                result.append(window_sum)
            window_sum -= nums[i]
        return result

if __name__ == '__main__':
    s = [1, 2, 7, 8, 5]
    print(Solution().winSum(s, 3))
