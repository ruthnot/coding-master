class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # write your code here
        if not s or not wordDict:
            return []
        max_length = len(max(wordDict, key=len))
        results = []
        self.dfs(s, 0, max_length, wordDict, {}, [], results)
        return results

    def dfs(self, s, index, max_length, word_set, memo, path, results):
        if index == len(s):
            results.append(" ".join(path))
            return
        if not self.is_possible(s, index, max_length, word_set, memo):
            return

        for end in range(index + 1, len(s) + 1):
            if end - index > max_length:
                break
            word = s[index:end]
            if word not in word_set:
                continue
            path.append(word)
            self.dfs(s, end, max_length, word_set, memo, path, results)
            path.pop()

    def is_possible(self, s, index, max_length, word_set, memo):
        if index in memo:
            return memo[index]

        if index == len(s):
            return True

        for end in range(index + 1, len(s) + 1):
            if end - index > max_length:
                break

            word = s[index:end]
            if word not in word_set:
                continue
            if self.is_possible(s, end, max_length, word_set, memo):
                memo[index] = True
                return True
        memo[index] = False
        return False




if __name__=="__main__":
    s = "lintcode"
    words = ["de", "ding", "co", "code", "lint"]
    print(Solution().wordBreak(s, words))


