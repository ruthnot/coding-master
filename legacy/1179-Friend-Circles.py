from typing import (
    List,
)

class Solution:  # DFS
    """
    @param m: a matrix
    @return: the total number of friend circles among all the students
    """

    def find_circle_num(self, m: List[List[int]]) -> int:
        # Write your code here
        count = 0
        visited = set([])
        for i in range(len(m)):
            if i not in visited:
                count += 1
            self.dfs(i, m, visited)
        return count

    def dfs(self, start, m, visited):
        if start in visited:
            return
        visited.add(start)
        for end in range(len(m)):
            if end == start or end in visited:
                continue
            if not m[start][end]:
                continue
            self.dfs(end, m, visited)


from collections import deque
class Solution2:   # BFS
    """
    @param m: a matrix
    @return: the total number of friend circles among all the students
    """
    def find_circle_num(self, m: List[List[int]]) -> int:
        # Write your code here
        count = 0
        visited = set([])
        for i in range(len(m)):
            if i in visited:
                continue
            queue = deque([i])
            while queue:
                i = queue.popleft()
                for j in range(len(m)):
                    if i == j or j in visited:
                        continue
                    if not m[i][j]:
                        continue
                    queue.append(j)
                    visited.add(j)
            count += 1
        return count


class Solution3:  # DFS 2
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students
    """
    def findCircleNum(self, M):
        # Write your code here

        visited = set()
        result = 0
        for i in range(len(M)):
            if i in visited:
                continue
            result += 1
            self.dfs(M, i, visited)
        return result

    def dfs(self, M, curr, visited):
        if curr in visited:
            return
        visited.add(curr)
        for i in range(len(M)):
            if M[curr][i] and i not in visited:
                self.dfs(M, i, visited)

class Solution4: # BFS 2
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students
    """

    def findCircleNum(self, M):
        if not M or not M[0]:
            return 0
        visited = set()
        result = 0
        for i in range(len(M)):
            if i not in visited:
                result += 1
                self.bfs(M, i, visited)
        return result

    def bfs(self, M, student, visited):
        queue = deque([student])
        while queue:
            i = queue.popleft()
            for j in range(len(M[0])):
                if j not in visited and M[i][j]:
                    visited.add(j)
                    queue.append(j)

if __name__=='__main__':
    '''
    1 0 0 1
    0 1 1 0
    0 1 1 1
    1 0 1 1
    (0, 3) (1, 2) (2, 3) 
    1 1 0
    1 1 0
    0 0 1
    
    1 1 0
    1 1 1
    0 1 1
    '''
    # m = [[1,1,0],[1,1,0],[0,0,1]]
    # m = [[1,1,0],[1,1,1],[0,1,1]]
    m = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    res = Solution().findCircleNum(m)
    print(res)
