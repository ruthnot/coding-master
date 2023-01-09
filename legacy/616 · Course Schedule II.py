from collections import deque
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        indegree = {i: 0 for i in range(numCourses)}
        edges = {i: [] for i in range(numCourses)}
        for right, left in prerequisites:
            indegree[right] += 1
            edges[left].append(right)

        start_nodes = [x for x in range(numCourses) if indegree[x] == 0]
        queue = deque(start_nodes)
        order = []
        while queue:
            left = queue.popleft()
            order.append(left)
            for right in edges[left]:
                indegree[right] -=1
                if indegree[right] == 0:
                    queue.append(right)
        return order if len(order) == numCourses else []