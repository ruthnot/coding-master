class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def find_missing2(self, n: int, str: str) -> int:
        # write your code here
        self.res = -1
        visited = set([])
        self.dfs(n, str, 0, visited)
        return self.res

    def dfs(self, n, str, start, visited):
        if start == len(str) and len(visited) == n - 1:
            self.res = self.find_missing(n, visited)
            return
        if start == len(str) or len(visited) >= n - 1:
            return

        for end in range(start, len(str)):
            num = int(str[start:end+1])
            if num in visited:
                continue
            if num > n or num == 0:  # very important to exclude 0
                break
            visited.add(num)
            self.dfs(n, str, end + 1, visited)
            visited.remove(num)

    def find_missing(self, n, visited):
        for i in range(1, n + 1):
            if i not in visited:
                return i
        return -1




class Solution2:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def findMissing2(self, n, str):
        # write your code here
        self.miss_num = -1
        visited = set()
        self.dfs(n, str, visited)
        return self.miss_num

    def dfs(self, n, str, visited):
        if len(str) == 0 and len(visited) == n - 1:
            self.miss_num = self.find_miss_num(n, visited)
            return

        if len(str) == 0 or len(visited) >= n:
            return

        for i in range(1, len(str) + 1):
            num = int(str[:i])
            if num > n or num == 0:
                break
            if num in visited:
                continue
            visited.add(num)
            self.dfs(n, str[i:], visited)
            visited.remove(num)

    def find_miss_num(self, n, visited):
        for i in range(1, n + 1):
            if i not in visited:
                return i
        return -1



if __name__ == '__main__':
    x = "19201234567891011121314151618"
    y = "56412"
    z = "111097654281222131272625242321320191817161514"
    n = 20
    m = 6
    l = 28
    print(Solution().findMissing2(l, z))






