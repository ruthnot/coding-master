class Solution:
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        if s is None or p is None:
            return False

        return self.is_match_helper(s, 0, p, 0, {})

    def star_pair(self, p, p_index):
        if p[-1] != '*':
            return False
        for i in range(p_index, len(p) - 1):
            if p[i] == '*':
                continue
            if p[i + 1] != '*':
                return False
        return True

    def is_match_char(self, s_char, p_char):
        return s_char == p_char or p_char == '.'

    def is_match_helper(self, s, s_index, p, p_index, memo):
        if p_index == len(p):
            return s_index == len(s)

        if s_index == len(s):
            return self.star_pair(p, p_index)

        if (s_index, p_index) in memo:
            return memo[(s_index, p_index)]

        s_char, p_char = s[s_index], p[p_index]

        if p_index < len(p) - 1 and p[p_index + 1] == '*':
            match = self.is_match_helper(s, s_index, p, p_index + 2, memo) or \
                    (self.is_match_char(s_char, p_char) and self.is_match_helper(s, s_index + 1, p, p_index, memo))
        else:
            match = self.is_match_char(s_char, p_char) and \
                self.is_match_helper(s, s_index + 1, p, p_index + 1, memo)
        memo[(s_index, p_index)] = match
        return match

if __name__ == '__main__':
    a = "1234"

    print(a[1])


