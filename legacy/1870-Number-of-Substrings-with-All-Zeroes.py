class Solution:
    """
    @param str: the string
    @return: the number of substrings
    """
    def stringCount(self, str):
        # Write your code here.
        if not str:
            return 0

        count = 0
        j = 1
        for i in range(len(str)):
            if str[i] == '1':
                continue
            count += 1
            j = max(j, i + 1)
            while j < len(str) and str[j] == '0':
                count += j - i
                j += 1
        return count


class Solution2:
    """
    @param str: the string
    @return: the number of substrings
    """
    def stringCount(self, str):
        # Write your code here.
        if not str:
            return None
        sum = 0
        l, r = 0, 0
        while l < len(str):
            r += 1
            while r < len(str) and str[r] == '0':
                r += 1
            count = 0
            while l < len(str) and l <= r:
                if str[l] != '0':
                    l += 1
                    break
                l += 1
                count += 1
                sum += count
        return sum


if __name__ == '__main__':
    str = '00010011'
    print(Solution().stringCount(str))



