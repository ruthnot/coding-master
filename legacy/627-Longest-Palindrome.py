class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        counter = 0
        hashtable = dict()
        for i in s:
            if i in hashtable and hashtable[i] == 1:
                counter += 2
                hashtable[i] -= 1
            else:
                hashtable[i] = 1

        for i in hashtable:
            if hashtable[i] == 1:
                counter += 1
                break

        return counter