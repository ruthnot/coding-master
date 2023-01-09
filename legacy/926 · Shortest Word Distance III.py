from typing import (
    List,
)

class Solution:
    """
    @param words: a list of words
    @param word1: a string
    @param word2: a string
    @return: the shortest distance between word1 and word2 in the list
    """
    def shortest_word_distance(self, words: List[str], word1: str, word2: str) -> int:
        # Write your code here
        if word1 != word2:
            return self.non_repeat(words, word1, word2)
        else:
            return self.repeat(words, word1)

    def repeat(self, words, word):
        min_dist = float('inf')
        idx1, idx2 = None, None
        flag1, flag2 = True, False
        for i in range(len(words)):
            if words[i] == word and flag1:
                idx1 = i
                flag1 = False
                flag2 = True
            elif words[i] == word and flag2:
                idx2 = i
                flag2 = False
                flag1 = True
            if idx1 is not None and idx2 is not None:
                min_dist = min(min_dist, abs(idx1 - idx2))
        return min_dist


    def non_repeat(self, words, word1, word2):
        min_dist = float('inf')
        idx1, idx2 = None, None
        for i in range(len(words)):
            if words[i] == word1:
                idx1 = i
            elif words[i] == word2:
                idx2 = i
            if idx1 is not None and idx2 is not None:
                min_dist = min(min_dist, abs(idx1 - idx2))
        return min_dist