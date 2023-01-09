class Solution:
    """
    @param str: An array of char
    @param left: a left offset
    @param right: a right offset
    @return: return a rotate string
    """

    def RotateString2(self, str, left, right):
        # write your code here
        offset = (left - right) % len(str)
        rightStr = str[:offset]
        leftStr = str[offset:]
        return leftStr + rightStr


