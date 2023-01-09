class Solution1: # Naive O(N^2)
    def strStr(self, source, target):
        if not source and not target:
            return 0
        for i in range(len(source) - len(target) + 1):
            for j in range(len(target)):
                if source[i + j] != target[j]:
                    break
            else:
                return i
        return -1


class Solution2: # Robin-Karp (Hash function) O(N+M)
    def __init__(self):
        self.BASE = 1000000

    def strStr(self, source, target):
        if not source or not target:
            return -1

        m = len(target)
        if m == 0:
            return 0

        # 31 ^ m
        power = 1
        for i in range(m):
            power = power * 31 % self.BASE

        targetCode = 0
        for i in range(m):
            targetCode = (targetCode * 31 + ord(target[i])) % self.BASE

        hashCode = 0
        for i in range(len(source)):
            # abc + d
            hashCode = (hashCode * 31 + ord(source[i])) % self.BASE
            if (i < m - 1):
                continue
            # abcd - a
            if (i >= m):
                hashCode = hashCode - (ord(source[i - m]) * power) % self.BASE
                if (hashCode < 0):
                    hashCode += self.BASE
            if hashCode == targetCode:
                if source[i-m+1:i+1] == target:
                    return i-m+1
        return -1









if __name__=='__main__':

    #abc = (a*31^2 + b*31^1 + c) % 10^6
    #abcd =(a*31^3 + b*31^2+ c*31^1 + d) % 10^6
    #abcd = (abc * 31 + d) % 10^6 = ((a*31^2 + b*31^1 + c) % 10^6 * 31 + d) % 10^6
    _ = Solution2()
    source = 'abcde'
    target = 'de'
    res = _.strStr(source, target)
    print(res)

    a = [0, 1, 2]
    a.pop(a.index(2))
    print(a)