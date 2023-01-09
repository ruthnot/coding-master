class Solution:
    def characterReplacement(self, s, k):
        # write your code here
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


class Solution2:
    """
    @param s: a string
    @param k: a integer
    @return: return a integer
    """
    def characterReplacement(self, s, k):
        # write your code here
        j = 0
        counter = {}
        maxFreq = 0
        answer = 0
        for i in range(len(s)):
            while j < len(s) and j - i - maxFreq <= k:
                counter[s[j]] = counter.get(s[j], 0) + 1
                maxFreq = max(maxFreq, counter[s[j]])
                j += 1
            if j - i - maxFreq > k:
                answer = max(answer, j - i - 1)
            else:
                answer = max(answer, j - i)

            counter[s[i]] -= 1
            maxFreq = max(counter.values())
        return answer