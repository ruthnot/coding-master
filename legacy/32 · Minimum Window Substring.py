class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def min_window(self, source: str, target: str) -> str:
        # write your code here
        count = {}
        for c in target:
            count[c] = count.get(c, 0) + 1
        needed = len(count)

        res, start, end = float('inf'), -1, -1

        left = 0
        for right in range(len(source)):
            c = source[right]
            if c in count:
                count[c] -= 1
                if count[c] == 0:
                    needed -= 1
            while needed == 0:
                if right - left + 1 < res:
                    res, start, end = right - left + 1, left, right
                c = source[left]
                if c in count:
                    count[c] += 1
                    if count[c] == 1:
                        needed += 1
                left += 1
        return source[start:end+1] if start != -1 else ""