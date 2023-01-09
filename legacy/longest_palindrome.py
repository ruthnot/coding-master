# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution1: # Triple For Loop O(N^3)
    def longestPalindrome(self, s):
        if not s:
            return None
        for length in range(len(s), 0 , -1):
            for count in range(len(s) - length + 1):
                if self.is_Palindrome(s, count, count + length - 1):
                    return s[count: count + length]
        return ""

    def is_Palindrome(self, input_string, start_idx, end_idx):
        while start_idx < end_idx and input_string[start_idx] == input_string[end_idx]:
            start_idx += 1
            end_idx -= 1
        return start_idx >= end_idx


class Solution2: # 中心线背向双指针 Enumeration O(N^2)
    def longestPalindrome(self, s):
        if not s:
            return s
        answer = (0, 0)
        for mid in range(len(s)):
            answer = max(answer, self.get_palindrome_from(s, mid, mid))
            answer = max(answer, self.get_palindrome_from(s, mid, mid+1))
        return s[answer[1]: answer[0] + answer[1]]

    def get_palindrome_from(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1, left + 1


class Solution3: # Dynamic Programming O(N^2)
    def longestPalindrome(self, s):
        if not s:
            return s
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]

        for i in range(n):
            is_palindrome[i][i] = True
        for i in range(1, n):
            is_palindrome[i][i-1] = True

        start, longest = 0, 1
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                is_palindrome[i][j] = is_palindrome[i+1][j-1] and s[i] == s[j]
                if is_palindrome[i][j] and length > longest:
                    longest = length
                    start = i
        return s[start: start+longest]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    _ = Solution3()
    result = _.longestPalindrome("abbcbba")
    print(result)


