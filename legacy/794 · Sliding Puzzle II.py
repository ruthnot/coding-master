from typing import (
    List,
)
DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
from collections import deque
from copy import deepcopy
class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """
    def min_move_step(self, init_state: List[List[int]], final_state: List[List[int]]) -> int:
        # # write your code here
        moves = -1
        init_str, final_str = self.serialize(init_state), self.serialize(final_state)
        queue = deque([init_str])
        visited = set([init_str])
        while queue:
            moves += 1
            for i in range(len(queue)):
                curr_str = queue.popleft()
                if curr_str == final_str:
                    return moves
                zero_x, zero_y = self.find_zero(curr_str)
                for dx, dy in DIR:
                    target_x, target_y = zero_x + dx, zero_y + dy
                    if not self.is_valid(target_x, target_y):
                        continue
                    new_str = self.swap(curr_str, zero_x, zero_y, target_x, target_y)
                    if new_str and new_str not in visited:
                        visited.add(new_str)
                        queue.append(new_str)
        return -1

    def find_zero(self, string):
        for i in range(len(string)):
            if string[i] == '0':
                return i // 3, i % 3

    def is_valid(self, x, y):
        if not (0 <= x < 3 and 0 <= y < 3):
            return False
        return True

    def swap(self, string, zero_x, zero_y, target_x, target_y):
        new_string = list(string)
        old, new = zero_x * 3 + zero_y, target_x * 3 + target_y
        new_string[old], new_string[new] = new_string[new], new_string[old]
        return ''.join(new_string)

    def serialize(self, state):
        res = ""
        for i in range(3):
            for j in range(3):
                res += str(state[i][j])
        return res


