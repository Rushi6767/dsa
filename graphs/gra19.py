"""
207. Course Schedule
"""
from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adj_list = [[]for _ in range(numCourses)]

        # O(n)
        for u,v in prerequisites:
            adj_list[u].append(v)
            indegrees[v] += 1
        
        queue = deque()
        result = []

        # O(n)
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        # O(V + E)
        while queue:
            current_node = queue.popleft()
            result.append(current_node)

            for adj in adj_list[current_node]:
                indegrees[adj] -= 1
                if indegrees[adj] == 0:
                    queue.append(adj)

        if len(result) == numCourses:
            return True
        return False

numCourses = 2
# prerequisites = [[1,0]]
prerequisites = [[1,0],[0,1]]
s =  Solution()
print(s.canFinish(numCourses, prerequisites))

"""
Time complexity :O(n) + O(n) + O(v + E)
Space complexity :O(n) + O(n) +O(n) == O(3n)
space : indegrees, adj_list, queue
"""