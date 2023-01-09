from typing import (
    List,
)
KEY = {'2': 'abc',
       '3': 'def',
       '4': 'ghi',
       '5': 'jkl',
       '6': 'mno',
       '7': 'pqrs',
       '8': 'tuv',
       '9': 'wxyz'}

class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letter_combinations(self, digits: str) -> List[str]:
        # write your code here
        if not digits:
            return []
        result = []
        self.dfs(digits, 0, [], result)
        return result

    def dfs(self, digits, index, path, result):
        if index >= len(digits):
            result.append(''.join(path))
            return
        for char in KEY[digits[index]]:
            path.append(char)
            self.dfs(digits, index + 1, path, result)
            path.pop()