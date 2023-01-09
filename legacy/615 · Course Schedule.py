from collections import deque
class Solution:
    """
    @param numCourses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        degree = {i: 0 for i in range(numCourses)}
        edges = {i: [] for i in range(numCourses)}
        for after, pre in prerequisites:
            degree[after] += 1
            edges[pre].append(after)
        start = [x for x in range(numCourses) if degree[x] == 0]
        queue = deque(start)
        count = 0
        while queue:
            course = queue.popleft()
            count += 1
            for after in edges[course]:
                degree[after] -= 1
                if degree[after] == 0:
                    queue.append(after)
        return count == numCourses
