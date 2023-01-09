class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def length_of_longest_substring(self, s: str) -> int:
        # write your code here
        if not s:
            return 0
        max_size = float('-inf')
        nums = set()
        right = 0

        for left in range(len(s)):
            while right < len(s) and s[right] not in nums:
                nums.add(s[right])
                right += 1
            max_size = max(max_size, right - left)
            nums.remove(s[left])
            left += 1
        return max_size