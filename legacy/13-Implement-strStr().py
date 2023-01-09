class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        if not source and not target:
            return 0
        for i in range(len(source) - len(target) + 1):
            for j in range(len(target)):
                if source[i + j] != target[j]:
                    break
            else:
                return i
        return -1


class Solution2:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        m = len(source)
        n = len(target)
        if not target:
            return 0

        for i in range(m):
            if source[i] != target[0]:
                continue
            if n + i <= m and source[i:n+i] == target:
                return i
        return -1