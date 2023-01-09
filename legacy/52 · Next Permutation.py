"""
一直觉得排列的题目很有趣，终于想通了根据当前排列计算出下一个排列的方法，在这里记录一下。
例如 2, 6, 3, 5, 4, 1 这个排列， 我们想要找到下一个刚好比他大的排列，于是可以从后往前看
我们先看后两位 4, 1 能否组成更大的排列，答案是不可以，同理 5, 4, 1也不可以 直到3, 5, 4, 1这个排列，
因为 3 < 5， 我们可以通过重新排列这一段数字，来得到下一个排列 因为我们需要使得新的排列尽量小，
所以我们从后往前找第一个比3更大的数字，发现是4 然后，我们调换3和4的位置，得到4, 5, 3, 1这个数列
因为我们需要使得新生成的数列尽量小，于是我们可以对5, 3, 1进行排序，可以发现在这个算法中，我们得到的末尾数字一定是倒序排列的，
于是我们只需要把它反转即可 最终，我们得到了4, 1, 3, 5这个数列 完整的数列则是2, 6, 4, 1, 3, 5
"""


class Solution:

    def nextPermutation(self, nums):
        for i in range(len(nums)-1, -1, -1):
            # Find the index where larger numbers are possible
            if i > 0 and nums[i] > nums[i-1]:
                # Start again from end to find the smallest number that is bigger than the index number
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        nums[j], nums[i-1] = nums[i-1], nums[j]
                        left, right = i, len(nums)-1
                        # Sort the rest of the nums
                        while left < right:
                            nums[left], nums[right] = nums[right], nums[left]
                            left += 1
                            right -= 1
                        return nums
        # can't find the swappable num, meaning this is the largest permutation
        nums.reverse()
        return nums