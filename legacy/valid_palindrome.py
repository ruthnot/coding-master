

class Solution1: #同向双指针 O(N)
    def is_palindrome(self, s):
        if not s:
            return False
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not self.is_valid(s[left]):
                left += 1
            while left < right and not self.is_valid(s[right]):
                right -= 1
            if left < right and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def is_valid(self, char):
        return char.isdigit() or char.isalpha()


class Solution2: #Valid PalindromeII 能否去除最多一个值使其成为palindrome
    def validPalindrome(self, s):
        if s is None:
            return False
        left, right = self.findDifference(s, 0, len(s)-1)

        if left >= right:
            return True

        return self.isPalindrome(s, left+1, right) or self.isPalindrome(s, left, right-1)

    def isPalindrome(self, s, left, right):
        left, right = self.findDifference(s, left, right)
        return left >= right

    def findDifference(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return left, right
            left += 1
            right -= 1
        return left, right


if __name__=='__main__':
    _ = Solution1()
    res = _.is_palindrome("A man, a plan, a canal: Panama")
    print(res)