class Solution:
    """
    @param s: A string
    @param dict: A set of word
    @return: the number of possible sentences.
    """
    def wordBreak3(self, s, dict):
        # Write your code here
        if not s or not dict:
            return 0

        max_length, lower_dict = self.initialize(dict)
        return self.memo_search(s.lower(), 0, max_length, lower_dict, {})

    def initialize(self, dict):
        max_length, lower_dict = 0, set()
        for word in dict:
            max_length = max(max_length, len(word))
            lower_dict.add(word.lower())
        return max_length, lower_dict

    def memo_search(self, s, index, max_length, lower_dict, memo):
        if index == len(s):
            return 1

        if index in memo:
            return memo[index]

        result = 0

        for end in range(index + 1, len(s) + 1):
            if end - index > max_length:
                break

            word = s[index:end]
            if word not in lower_dict:
                continue

            result += self.memo_search(s, end, max_length, lower_dict, memo)

        memo[index] = result
        return memo[index]


