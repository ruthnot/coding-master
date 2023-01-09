import collections
class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """

    def accountsMerge(self, accounts):
        # create graph
        n = len(accounts)
        self.f = {}  # self.f[email] = email
        self.name = {}
        for i in range(n):
            emails = accounts[i][1:]
            for j in range(len(emails)):
                if emails[j] not in self.f:
                    self.f[emails[j]] = emails[j]
                self.union(emails[0], emails[j])
                self.name[emails[j]] = accounts[i][0]

        res = collections.defaultdict(set)
        for i in range(n):
            emails = accounts[i][1:]
            for j in range(len(emails)):
                root = self.find(emails[j])
                res[root].add(emails[j])
        L = []
        for k, v in res.items():
            L.append([self.name[k]] + sorted(list(v)))
        return L

    def union(self, a, b):
        fa = self.find(a)
        fb = self.find(b)
        if fa != fb:
            self.f[fa] = fb

    def find(self, a):
        if self.f[a] == a:
            return a
        self.f[a] = self.find(self.f[a])
        return self.f[a]