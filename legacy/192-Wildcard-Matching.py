class Solution:  # DP
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """

    def is_match(self, s: str, p: str) -> bool:
        # write your code here
        if s is None or p is None:
            return False
        n, m = len(s), len(p)

        dp = [[False] * (m + 1) for _ in range(n + 1)]

        dp[0][0] = True
        for i in range(1, m + 1):
            dp[0][i] = dp[0][i - 1] and p[i - 1] == '*'

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (
                            s[i - 1] == p[j - 1] or p[j - 1] == '?')
        return dp[n][m]


class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        # write your code here
        if s == None or p == None:
            return False
        return self.is_match_helper(s, 0, p, 0, {})


    def all_start(self, p, p_index):
        for i in range(p_index, len(p)):
            if p[i] != '*':
                return False
        return True

    def is_match_char(self, char_s, char_p):
        return char_s == char_p or char_p == '?'

    def is_match_helper(self, s, s_index, p, p_index, memo):
        if p_index == len(p):
            return s_index == len(s)

        if s_index == len(s):
            return self.all_start(p, p_index)

        if (s_index, p_index) in memo:
            return memo[(s_index, p_index)]

        if p[p_index] != '*':
            match = self.is_match_char(s[s_index], p[p_index]) and \
                self.is_match_helper(s, s_index + 1, p, p_index + 1, memo)
        else:
            match = self.is_match_helper(s, s_index, p, p_index + 1, memo) or \
                self.is_match_helper(s, s_index + 1, p, p_index, memo)

        memo[(s_index, p_index)] = match
        return match









