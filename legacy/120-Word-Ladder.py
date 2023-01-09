import collections
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """

    def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(end) # why? because later we are using word == end,
                      # so end has to be in the queue to be consider as "word", and be poped out during BFS
                      # if we use hasOneDiff(word, end), however, we don't need to add end into dict
                      # but need to write hasOneDiff function (listed below). Notice the final distance needs to add 1, too

        queue = collections.deque([start])
        visited = {start}

        distance = 0
        while queue:
            distance += 1
            size = len(queue)
            for i in range(size):
                word = queue.popleft()
                if word == end:
                    return distance
                for next_word in self.find_next_words(word, dict):
                    if next_word in visited:
                        continue
                    queue.append(next_word)
                    visited.add(next_word)
        return 0

    def find_next_words(self, word, dict):
        next_words = []
        for i in range(len(word)):
            left = word[:i]
            right = word[i+1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                new_word = left + char + right
                if new_word in dict:
                    next_words.append(new_word)
        return next_words


    def find_next_words_slow(self, word, dict):
        next_words = []
        for next_word in dict:
            has_one_diff = False
            for i in range(len(word)):
                if next_word[i] != word[i]:
                    if has_one_diff:
                        has_one_diff = False
                        break
                    has_one_diff = True
            if has_one_diff:
                next_words.append(next_word)
        return next_words

    def hasOneDiff(self, word, end):
        # one_diff = False
        # for i in range(len(word)):
        #     if word[i] != end[i] and not one_diff:
        #         one_diff = True
        #     elif word[i] != end[i] and one_diff:
        #         one_diff = False
        #         break
        return sum([word[i] != end[i] for i in range(len(word))]) == 1


if __name__=='__main__':
    start = "a"
    end = "c"
    dict = {"a", "b", "c"}
    print(Solution().ladderLength(start, end, dict))

