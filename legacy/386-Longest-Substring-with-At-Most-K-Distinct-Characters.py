

class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        # write your code here
        if not s or k == 0:
            return 0
        res = float('-inf')
        freq = {}
        right = 0
        for left in range(len(s)):
            while right < len(s) and (len(freq) < k or s[right] in freq):
                c = s[right]
                freq[c] = freq.get(c, 0) + 1
                right += 1
            res = max(res, right - left)

            c = s[left]
            freq[c] -= 1
            if freq[c] == 0:
                del freq[c]

        return res


class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        # write your code here
        res = float('-inf')
        freq = {}
        right = 0
        for left in range(len(s)):
            while right < len(s) and len(freq) <= k:
                c = s[right]
                freq[c] = freq.get(c, 0) + 1
                right += 1
            res = max(res, right - left)

            c = s[left]
            freq[c] -= 1
            if freq[c] == 0:
                freq.pop(c)
        return res
class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    # e c e b a
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if not k or not s:
            return 0
        j = 0
        longest = 0
        counter = {}
        for i in range(len(s)):
            while j < len(s) and len(counter) <= k:
                counter[s[j]] = counter.get(s[j], 0) + 1
                j += 1
            if len(counter) > k:
                longest = max(longest, j - i - 1)
            else:
                longest = max(longest, j - i)
            counter[s[i]] -= 1
            if counter[s[i]] == 0:
                del counter[s[i]]

        return longest




class Solution2:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if not s:
            return 0
        counter = {}
        left = 0
        longest = 0
        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1
            while left <= right and len(counter) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            longest = max(longest, right - left + 1)
        return longest





if __name__ == '__main__':
    s = "eqgkcwGFvjjmxutystqdfhuMblWbylgjxsxgnoh"
    k = 16
    s2 = "eceba"
    k2 = 3
    s3 = "w"
    k3 = 1
    print(Solution().lengthOfLongestSubstringKDistinct(s, k))
    print(Solution().lengthOfLongestSubstringKDistinct(s2, k2))
    print(Solution().lengthOfLongestSubstringKDistinct(s3, k3))






