DIRECTIONS = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]

# Trie + DFS


# Pure DFS
class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        if board is None or len(board) == 0:
            return []

        word_set = set(words)
        prefix_set = set()

        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i + 1])

        result_set = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, board[i][j], word_set, prefix_set, set([(i, j)]), result_set)
        return list(result_set)

    def dfs(self, board, x, y, word, word_set, prefix_set, visited, result_set):
        if word not in prefix_set:
            return

        if word in word_set:
            result_set.add(word)

        for dx, dy in DIRECTIONS:
            new_x = x + dx
            new_y = y + dy

            if not self.is_valid(board, new_x, new_y) or (new_x, new_y) in visited:
                continue

            visited.add((new_x, new_y))
            self.dfs(board, new_x, new_y, word + board[new_x][new_y], word_set, prefix_set, visited, result_set)
            visited.remove((new_x, new_y))

    def is_valid(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])


