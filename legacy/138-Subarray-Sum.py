class Solution: #prefix sum
    def subarraySum(self, nums):
        prefix_hash = {0: -1}
        prefix_sum = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            if prefix_sum in prefix_hash:
                return prefix_hash[prefix_sum] + 1, i
            prefix_hash[prefix_sum] = i
        return -1, -1



class Solution2: #Naive double for loop
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here

        for i in range(len(nums)):
            target = nums[i]
            if not target:
                return i, i
            for j in range(i + 1, len(nums)):
                target += nums[j]
                if not target:
                    return [i, j]
        return -1, -1




if __name__=='__main__':
    a = [0]
    res = Solution().subarraySum(a)
    print(res)